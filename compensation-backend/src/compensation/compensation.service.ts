import { BadRequestException, Injectable } from '@nestjs/common';
import { Compensation, Prisma } from '@prisma/client';
import { createHash } from 'crypto';
import { PrismaService } from '../prisma.service';
import { canonicalCompany } from '../common/company-normalizer';
import { CompareCompensationDto, IngestCompensationDto, QueryCompensationDto } from './dto';

@Injectable()
export class CompensationService {
  constructor(private readonly prisma: PrismaService) {}

  private fingerprint(input: { companyId: string; role: string; level: string; location: string; currency: string; baseSalary: number; bonus: number; stock: number; source: string; sourceRef?: string }) {
    return createHash('sha256').update(JSON.stringify(input)).digest('hex');
  }

  async ingest(dto: IngestCompensationDto) {
    const companyKey = canonicalCompany(dto.company);
    if (!companyKey || dto.baseSalary <= 0) throw new BadRequestException('Invalid compensation record');
    const bonus = dto.bonus ?? 0;
    const stock = dto.stock ?? 0;
    const company = await this.prisma.company.upsert({
      where: { canonical: companyKey },
      create: { canonical: companyKey, displayName: dto.company.trim() },
      update: {},
    });
    await this.prisma.companyAlias.upsert({
      where: { normalized: dto.company.trim().toLowerCase() },
      create: { normalized: dto.company.trim().toLowerCase(), rawName: dto.company.trim(), companyId: company.id },
      update: { companyId: company.id, rawName: dto.company.trim() },
    });
    const payload = { companyId: company.id, role: dto.role.trim(), level: dto.level.trim(), location: dto.location.trim(), currency: dto.currency.toUpperCase(), baseSalary: dto.baseSalary, bonus, stock, source: dto.source.trim(), sourceRef: dto.sourceRef?.trim() };
    const fingerprint = this.fingerprint(payload);
    return this.prisma.compensation.upsert({
      where: { fingerprint },
      create: { ...payload, totalComp: dto.baseSalary + bonus + stock, fingerprint },
      update: {},
      include: { company: true },
    });
  }

  async search(q: QueryCompensationDto) {
    const where: Prisma.CompensationWhereInput = {};
    if (q.company) where.company = { canonical: canonicalCompany(q.company) };
    if (q.role) where.role = { contains: q.role.trim() };
    if (q.level) where.level = { contains: q.level.trim() };
    if (q.location) where.location = { contains: q.location.trim() };
    const page = q.page ?? 1;
    const limit = Math.min(q.limit ?? 20, 100);
    const [items, total] = await this.prisma.$transaction([
      this.prisma.compensation.findMany({ where, include: { company: true }, orderBy: { totalComp: 'desc' }, skip: (page - 1) * limit, take: limit }),
      this.prisma.compensation.count({ where }),
    ]);
    return { data: items, meta: { page, limit, total, pages: Math.ceil(total / limit) } };
  }

  async companies() {
    return this.prisma.company.findMany({ include: { _count: { select: { entries: true } } }, orderBy: { displayName: 'asc' } });
  }

  async aggregate() {
    const rows = await this.prisma.compensation.groupBy({ by: ['companyId'], _count: { _all: true }, _avg: { totalComp: true }, _min: { totalComp: true }, _max: { totalComp: true } });
    const companies = await this.prisma.company.findMany({ where: { id: { in: rows.map(r => r.companyId) } } });
    const names = new Map(companies.map(c => [c.id, c.displayName]));
    return rows.map(r => ({ companyId: r.companyId, company: names.get(r.companyId), count: r._count._all, averageTotalComp: Math.round(r._avg.totalComp ?? 0), minTotalComp: r._min.totalComp, maxTotalComp: r._max.totalComp })).sort((a,b) => b.averageTotalComp - a.averageTotalComp);
  }

  async compare(dto: CompareCompensationDto) {
    const companies = dto.companies.split(',').map(c => canonicalCompany(c)).filter(Boolean);
    const rows = await this.prisma.compensation.findMany({ where: { role: dto.role.trim(), level: dto.level.trim(), location: dto.location.trim(), company: { canonical: { in: companies } } }, include: { company: true }, orderBy: { totalComp: 'desc' } });
    return { criteria: { role: dto.role, level: dto.level, location: dto.location, companies }, data: rows };
  }
}

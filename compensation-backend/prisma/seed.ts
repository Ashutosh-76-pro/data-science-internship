import { PrismaClient } from '@prisma/client';
import { createHash } from 'crypto';
const prisma = new PrismaClient();

const data = [
  ['Google LLC','Software Engineer','L3','Bengaluru',1800000,200000,600000],
  ['Google India','Software Engineer','L4','Bengaluru',2600000,300000,900000],
  ['Microsoft Corporation','Software Engineer','SDE 2','Bengaluru',2200000,250000,700000],
  ['Amazon India','Software Development Engineer','SDE II','Hyderabad',2100000,200000,500000],
  ['Meta Platforms','Software Engineer','E4','Bengaluru',2800000,350000,1100000],
  ['Infosys Limited','Software Engineer','SE','Pune',700000,50000,0],
  ['TCS Ltd','Software Engineer','Digital','Noida',850000,75000,0],
  ['Google','Backend Engineer','L4','Hyderabad',2500000,300000,850000],
  ['Microsoft','Backend Engineer','SDE 2','Hyderabad',2300000,250000,750000],
  ['Amazon','Backend Engineer','SDE II','Hyderabad',2150000,220000,550000]
] as const;

async function main() {
  for (const [companyRaw, role, level, location, baseSalary, bonus, stock] of data) {
    const canonical = companyRaw.toLowerCase().replace(/\b(incorporated|inc|limited|ltd|llc|corp|corporation|plc)\.?\b/g, '').replace(/[^a-z0-9]+/g, ' ').trim().replace(/\s+/g, ' ');
    const alias = companyRaw.toLowerCase().trim();
    const company = await prisma.company.upsert({ where: { canonical }, create: { canonical, displayName: canonical.replace(/\b\w/g, c => c.toUpperCase()) }, update: {} });
    await prisma.companyAlias.upsert({ where: { normalized: alias }, create: { normalized: alias, rawName: companyRaw, companyId: company.id }, update: { companyId: company.id } });
    const payload = { companyId: company.id, role, level, location, currency: 'INR', baseSalary, bonus, stock, source: 'generated-demo', sourceRef: 'seed' };
    const fingerprint = createHash('sha256').update(JSON.stringify(payload)).digest('hex');
    await prisma.compensation.upsert({ where: { fingerprint }, create: { ...payload, totalComp: baseSalary + bonus + stock, fingerprint }, update: {} });
  }
}
main().finally(() => prisma.$disconnect());

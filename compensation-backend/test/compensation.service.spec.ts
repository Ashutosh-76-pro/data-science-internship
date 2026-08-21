import { CompensationService } from '../src/compensation/compensation.service';

describe('CompensationService', () => {
  it('calculates total compensation with omitted bonus and stock as zero', async () => {
    const prisma: any = {
      company: {
        upsert: jest.fn().mockResolvedValue({ id: 'c1', canonical: 'google', displayName: 'Google' }),
      },
      companyAlias: {
        upsert: jest.fn().mockResolvedValue({}),
      },
      compensation: {
        upsert: jest.fn().mockImplementation(async ({ create }: any) => create),
      },
    };
    const service = new CompensationService(prisma);
    const result: any = await service.ingest({ company: 'Google LLC', role: 'Engineer', level: 'L3', location: 'Bengaluru', currency: 'inr', baseSalary: 1000000, source: 'test' });
    expect(result.totalComp).toBe(1000000);
    expect(result.bonus).toBe(0);
    expect(result.stock).toBe(0);
  });
});

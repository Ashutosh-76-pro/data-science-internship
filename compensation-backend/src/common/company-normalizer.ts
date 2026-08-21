export function normalizeCompanyName(value: string): string {
  return value
    .normalize('NFKC')
    .toLowerCase()
    .replace(/&/g, ' and ')
    .replace(/\b(incorporated|inc|limited|ltd|llc|corp|corporation|plc)\.?\b/g, '')
    .replace(/[^a-z0-9]+/g, ' ')
    .trim()
    .replace(/\s+/g, ' ');
}

export const COMPANY_ALIASES: Record<string, string> = {
  'google llc': 'google',
  'google india': 'google',
  'alphabet': 'google',
  'meta platforms': 'meta',
  'facebook': 'meta',
  'microsoft corporation': 'microsoft',
  'amazon web services': 'amazon',
  'amazon india': 'amazon',
};

export function canonicalCompany(value: string): string {
  const normalized = normalizeCompanyName(value);
  return COMPANY_ALIASES[normalized] ?? normalized;
}

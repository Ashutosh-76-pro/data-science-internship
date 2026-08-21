# Compensation Intelligence Backend

Production-style backend for a salary comparison platform. All compensation records are persisted in SQLite through Prisma; the API is the only access path expected by a frontend.

## Stack
- Node.js + TypeScript
- NestJS REST API
- Prisma ORM
- SQLite (easy local evaluation; PostgreSQL-ready schema)
- class-validator / class-transformer

## Architecture
```text
HTTP -> Controller -> ValidationPipe -> Service -> Prisma -> SQLite
                         |
                         +-> company normalization
                         +-> total compensation calculation
                         +-> duplicate fingerprinting
```

## Data model
- `Company`: one canonical company record.
- `CompanyAlias`: raw company names mapped to a canonical company.
- `Compensation`: normalized salary observations with base, bonus, stock and computed total compensation.

Indexes cover company, role, level, location and total compensation. A SHA-256 fingerprint is unique to make ingestion idempotent.

## Setup
```bash
cd compensation-backend
npm install
cp .env.example .env
npx prisma generate
npx prisma migrate dev
npm run prisma:seed
npm run dev
```

API runs on `http://localhost:4000`.

## REST API
### Health
`GET /api/v1/health`

### Ingest
`POST /api/v1/compensations`

```json
{
  "company": "Google India",
  "role": "Software Engineer",
  "level": "L4",
  "location": "Bengaluru",
  "currency": "INR",
  "baseSalary": 2600000,
  "bonus": 300000,
  "stock": 900000,
  "source": "demo"
}
```

Bonus and stock are optional and default to `0`. `totalComp` is always calculated by the backend.

### Search / filters / pagination
`GET /api/v1/compensations?company=google&role=Software%20Engineer&level=L4&location=Bengaluru&page=1&limit=20`

### Company aggregation
`GET /api/v1/companies/aggregation`

Returns count, average, minimum and maximum total compensation by canonical company.

### Company list
`GET /api/v1/companies`

### Compensation comparison
`GET /api/v1/compensations/compare?role=Software%20Engineer&level=L4&location=Bengaluru&companies=Google,Microsoft,Meta`

## Reliability rules
1. Unknown fields are rejected by `ValidationPipe` (`forbidNonWhitelisted`).
2. Required strings cannot be empty.
3. Base salary must be a positive integer.
4. Bonus and stock cannot be negative.
5. Missing bonus/stock become zero.
6. Company names are canonicalized before persistence.
7. Duplicate observations are idempotent through a unique SHA-256 fingerprint.
8. Total compensation is calculated server-side as `base + bonus + stock`.
9. Search is database-backed with bounded pagination (`limit <= 100`).
10. No frontend-only salary data is required.

## Demo data
`prisma/seed.ts` contains generated, non-proprietary records solely for evaluation. It intentionally includes aliases such as Google LLC / Google India / Google so normalization can be demonstrated.

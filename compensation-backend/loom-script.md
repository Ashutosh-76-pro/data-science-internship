# Loom walkthrough — 5 to 10 minutes

## 0:00–0:45 — Problem
“This backend powers a compensation intelligence platform. The important principle is that compensation must be comparable by normalized company, role, level and location, not by raw job-title strings alone.”

## 0:45–2:00 — Architecture
Show `README.md`, then `src/app.module.ts`, controller and service.
Explain: HTTP request -> NestJS ValidationPipe -> controller -> service -> Prisma -> SQLite.

## 2:00–3:15 — Schema
Open `prisma/schema.prisma`.
Explain Company, CompanyAlias and Compensation. Point out indexes and the unique fingerprint. Explain why salary observations belong to a normalized company rather than storing company strings repeatedly.

## 3:15–4:30 — Validation and ingestion
Open `src/compensation/dto.ts` and `compensation.service.ts`.
Show positive base salary validation, non-negative bonus/stock, whitelist validation, defaults to zero, company canonicalization, and server-side total compensation.

## 4:30–5:45 — Duplicate handling
Explain the SHA-256 fingerprint. Send the same POST twice and show that the second request is idempotent rather than creating another row.

## 5:45–7:00 — Search and filtering
Call `GET /api/v1/compensations` with company, role, level, location, page and limit. Show database-backed pagination and metadata.

## 7:00–8:15 — Aggregation and comparison
Call `/companies/aggregation` and `/compensations/compare`. Explain that aggregation and comparison operate on database records and computed total compensation.

## 8:15–9:00 — Reliability
Show the test file. Mention rejected unknown fields, invalid salary values, bounded pagination, normalized company names, idempotent ingestion and generated seed data.

## 9:00–9:30 — Close
“This implementation keeps compensation logic in the backend and database. A frontend can consume these APIs without hardcoded salary records, which makes the system testable and extensible.”

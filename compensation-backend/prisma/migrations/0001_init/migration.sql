CREATE TABLE "Company" (
  "id" TEXT NOT NULL PRIMARY KEY,
  "canonical" TEXT NOT NULL,
  "displayName" TEXT NOT NULL,
  "createdAt" DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
  "updatedAt" DATETIME NOT NULL
);
CREATE UNIQUE INDEX "Company_canonical_key" ON "Company"("canonical");

CREATE TABLE "CompanyAlias" (
  "id" TEXT NOT NULL PRIMARY KEY,
  "normalized" TEXT NOT NULL,
  "rawName" TEXT NOT NULL,
  "companyId" TEXT NOT NULL,
  CONSTRAINT "CompanyAlias_companyId_fkey" FOREIGN KEY ("companyId") REFERENCES "Company"("id") ON DELETE CASCADE ON UPDATE CASCADE
);
CREATE UNIQUE INDEX "CompanyAlias_normalized_key" ON "CompanyAlias"("normalized");

CREATE TABLE "Compensation" (
  "id" TEXT NOT NULL PRIMARY KEY,
  "companyId" TEXT NOT NULL,
  "role" TEXT NOT NULL,
  "level" TEXT NOT NULL,
  "location" TEXT NOT NULL,
  "currency" TEXT NOT NULL DEFAULT 'INR',
  "baseSalary" INTEGER NOT NULL,
  "bonus" INTEGER NOT NULL DEFAULT 0,
  "stock" INTEGER NOT NULL DEFAULT 0,
  "totalComp" INTEGER NOT NULL,
  "source" TEXT NOT NULL,
  "sourceRef" TEXT,
  "sourceRecord" TEXT,
  "fingerprint" TEXT NOT NULL,
  "createdAt" DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
  "updatedAt" DATETIME NOT NULL,
  CONSTRAINT "Compensation_companyId_fkey" FOREIGN KEY ("companyId") REFERENCES "Company"("id") ON DELETE RESTRICT ON UPDATE CASCADE
);
CREATE UNIQUE INDEX "Compensation_fingerprint_key" ON "Compensation"("fingerprint");
CREATE INDEX "Compensation_companyId_idx" ON "Compensation"("companyId");
CREATE INDEX "Compensation_role_idx" ON "Compensation"("role");
CREATE INDEX "Compensation_level_idx" ON "Compensation"("level");
CREATE INDEX "Compensation_location_idx" ON "Compensation"("location");
CREATE INDEX "Compensation_totalComp_idx" ON "Compensation"("totalComp");

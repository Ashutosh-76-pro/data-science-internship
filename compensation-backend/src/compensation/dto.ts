import { Type } from 'class-transformer';
import { IsInt, IsOptional, IsPositive, IsString, Min, MinLength } from 'class-validator';

export class IngestCompensationDto {
  @IsString() @MinLength(1) company!: string;
  @IsString() @MinLength(1) role!: string;
  @IsString() @MinLength(1) level!: string;
  @IsString() @MinLength(1) location!: string;
  @IsString() @MinLength(3) currency!: string;
  @Type(() => Number) @IsInt() @IsPositive() baseSalary!: number;
  @Type(() => Number) @IsInt() @Min(0) @IsOptional() bonus?: number;
  @Type(() => Number) @IsInt() @Min(0) @IsOptional() stock?: number;
  @IsString() @MinLength(1) source!: string;
  @IsString() @IsOptional() sourceRef?: string;
}

export class QueryCompensationDto {
  @IsString() @IsOptional() company?: string;
  @IsString() @IsOptional() role?: string;
  @IsString() @IsOptional() level?: string;
  @IsString() @IsOptional() location?: string;
  @Type(() => Number) @IsInt() @Min(1) @IsOptional() page = 1;
  @Type(() => Number) @IsInt() @Min(1) @IsOptional() limit = 20;
}

export class CompareCompensationDto {
  @IsString() @MinLength(1) role!: string;
  @IsString() @MinLength(1) level!: string;
  @IsString() @MinLength(1) location!: string;
  @IsString() @MinLength(1) companies!: string;
}

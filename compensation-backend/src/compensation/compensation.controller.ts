import { Body, Controller, Get, Post, Query } from '@nestjs/common';
import { CompensationService } from './compensation.service';
import { CompareCompensationDto, IngestCompensationDto, QueryCompensationDto } from './dto';

@Controller('api/v1')
export class CompensationController {
  constructor(private readonly service: CompensationService) {}

  @Post('compensations')
  ingest(@Body() dto: IngestCompensationDto) { return this.service.ingest(dto); }

  @Get('compensations')
  search(@Query() query: QueryCompensationDto) { return this.service.search(query); }

  @Get('companies')
  companies() { return this.service.companies(); }

  @Get('companies/aggregation')
  aggregate() { return this.service.aggregate(); }

  @Get('compensations/compare')
  compare(@Query() query: CompareCompensationDto) { return this.service.compare(query); }

  @Get('health')
  health() { return { status: 'ok', service: 'compensation-api', timestamp: new Date().toISOString() }; }
}

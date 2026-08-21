import { Module } from '@nestjs/common';
import { PrismaService } from './prisma.service';
import { CompensationController } from './compensation/compensation.controller';
import { CompensationService } from './compensation/compensation.service';

@Module({ controllers: [CompensationController], providers: [PrismaService, CompensationService] })
export class AppModule {}

---
title: PRD 템플릿 (Product Requirements Document)
type: meta
tags: [template, prd, planning, meta]
author: Dave Han
status: Draft
created: 2026-06-07
updated: 2026-06-07
---

# PRD 템플릿 (Product Requirements Document)

> 이 문서는 신규 프로젝트/기능 기획을 위한 **PRD 템플릿** 입니다. 복사 후 `[ ]` 플레이스홀더를 채워 사용하세요.

- **작성자:** Dave Han
- **프로젝트명:** [프로젝트명 기입]
- **상태:** Draft
- **협업 부서:** PM, 개발, QA (DevOps/CTI 등 필요시 추가)

---

## 1. 배경 및 목적 (Background & Objectives)

- **문제 정의:** 현재 비즈니스나 시스템에서 해결해야 할 핵심 과제.
- **목표 및 기대 효과:** 이 개발을 통해 달성하고자 하는 구체적인 성과 및 OKR (예: 레거시 의존성 0% 달성 등).

## 2. 대상 고객 및 요구사항 (Target Audience & Requirements)

- **주요 대상:** 시스템을 사용할 엔드 유저, 내부 운영자, 혹은 연동되는 타 플랫폼.
- **User Story:** "사용자는 [목적]을 달성하기 위해 [어떤 기능]을 할 수 있어야 한다."

### 기능적 요구사항 (Functional Requirements)

- [ ] 세부 기능 1
- [ ] 세부 기능 2

## 3. 시스템 설계 및 아키텍처 정책 (System & Architecture)

- **설계 원칙:** 도메인 주도 설계(DDD), 헥사고날 아키텍처, 이벤트 기반 아키텍처(EDA) 적용 방안.
- **데이터/인프라 요구사항:** Snowflake, Kafka, 데이터 동기화(Backfilling) 요구사항, 또는 신규 인프라 확장 필요성.
- **비기능적 요구사항 (Non-Functional):** 성능 수준, 보안 감사(VAPT) 고려사항, 트래픽 처리 목표.

## 4. 품질 보증 및 리스크 관리 (QA & Risk Management)

- **테스트 및 리뷰 전략:** Claude Code 등을 활용한 단위 테스트 및 코드 리뷰 자동화 파이프라인 계획.
- **블로커 및 의존성 트래킹:** 주간 Red/Yellow/Green 상태 지표 기반의 리스크 공유 및 타 팀 의존성(블로커) 해결 계획.

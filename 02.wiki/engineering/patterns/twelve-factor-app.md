---
title: Twelve-Factor App
type: engineering
category: pattern
tags: [saas, cloud-native, methodology, twelve-factor, architecture, devops]
related: [pets-vs-cattle, refactoring]
first-seen: 12factor-net
sources: [12factor-net]
created: 2026-06-27
updated: 2026-06-27
---

# Twelve-Factor App

**12-Factor App**은 [[heroku|Heroku]] 기여자들([[adam-wiggins|Adam Wiggins]] 외)이 SaaS 앱 운영 경험을 종합해 정리한 12가지 설계 원칙 모음이다. 목표는 이식성(portability)·확장성(scalability)·dev/prod 수렴을 통한 continuous deployment이며, 언어·백킹 서비스에 무관하게 적용된다. 컨테이너·Kubernetes·서버리스 같은 현대 cloud-native 관행의 사상적 토대다.

이 페이지는 [[12factor-net|소스]]의 **12요소 레퍼런스**다. 각 factor는 *원칙 → 핵심 → 안티패턴* 순으로 정리한다.

## 12 Factors

### I. Codebase — 하나의 코드베이스, 여러 배포
> One codebase tracked in revision control, many deploys.

- 앱 하나당 버전관리되는 코드베이스 하나. 코드베이스↔앱은 1:1.
- 같은 코드베이스에서 dev / staging / production 등 여러 **deploy**가 나온다.
- 안티패턴: 여러 앱이 코드를 공유 → 공유분은 라이브러리(의존성)로 분리해야 함.

### II. Dependencies — 의존성 명시·격리
> Explicitly declare and isolate dependencies.

- 의존성을 **dependency declaration manifest**로 완전하고 명시적으로 선언 (예: `package.json`, `Cargo.toml`, `requirements.txt`).
- 실행 시 격리(isolation) 도구로 시스템 전역 패키지 누수를 차단 (vendoring / virtualenv / 컨테이너).
- 안티패턴: 시스템에 깔린 도구(`curl`, ImageMagick 등)가 있다고 *암묵적으로* 가정.

### III. Config — 설정은 환경에
> Store config in the environment.

- 배포마다 달라지는 값(DB 핸들, 자격증명, 호스트명)은 **환경 변수(env vars)**에 저장.
- 코드는 그대로 둔 채 환경만 바꿔 어디서나 배포 가능 → config와 code의 엄격한 분리.
- 리트머스 테스트: *지금 코드베이스를 오픈소스로 공개해도 자격증명이 새지 않는가?*
- 안티패턴: 언어별 config 파일에 상수로 박거나, 환경 그룹("dev"/"prod")으로 묶기.

### IV. Backing services — 백킹 서비스는 첨부 리소스
> Treat backing services as attached resources.

- DB·큐·캐시·SMTP·외부 API 등 모든 backing service를 URL/자격증명으로 접근하는 **attached resource**로 취급.
- 로컬 서비스와 서드파티 서비스를 코드 변경 없이 교체 가능 (예: 로컬 MySQL → Amazon RDS).
- 안티패턴: 특정 서비스 인스턴스를 코드에 강결합.

### V. Build, release, run — 빌드·릴리스·실행 분리
> Strictly separate build and run stages.

- **build**(코드→실행 가능 번들) → **release**(빌드+config) → **run**(실행)을 엄격히 분리.
- 모든 release는 고유 ID(타임스탬프/증가 번호)를 갖고 **불변(immutable)**, 롤백 가능.
- 안티패턴: 런타임에 코드를 직접 수정 → build로 되돌릴 방법이 없어짐.

### VI. Processes — 무상태 프로세스
> Execute the app as one or more stateless processes.

- 앱을 **stateless · share-nothing** 프로세스로 실행. 영속 데이터는 backing service(IV)에 저장.
- 메모리/로컬 디스크는 단일 트랜잭션 내 캐시로만 — 다음 요청에서 남아있다고 가정 금지.
- 안티패턴: sticky session(사용자 세션을 프로세스 메모리에 캐싱) → [[pets-vs-cattle|pet]]화.

### VII. Port binding — 포트 바인딩으로 노출
> Export services via port binding.

- 앱이 **자기 자신을 웹 서버로** 만들어 포트에 바인딩해 서비스 제공 (런타임에 웹서버 주입 의존 X).
- 한 앱이 다른 앱의 backing service가 될 수 있다(URL로 접근).
- 안티패턴: Apache/Tomcat 등 외부 웹서버 컨테이너에 코드를 주입해야만 동작.

### VIII. Concurrency — 프로세스 모델로 수평 확장
> Scale out via the process model.

- 작업 유형별 **process type**(web / worker 등)으로 나누고, type별 프로세스 수를 늘려 **수평 확장(scale out)**.
- 프로세스는 일급 시민 — OS 프로세스 매니저에 위임, 자체 데몬화/PID 파일 금지.
- 안티패턴: 단일 프로세스를 더 큰 머신으로 키우는 수직 확장에만 의존.

### IX. Disposability — 빠른 기동·우아한 종료
> Maximize robustness with fast startup and graceful shutdown.

- 프로세스는 **즉시 시작·종료 가능(disposable)**해야 한다 → 빠른 elastic scaling·배포.
- 짧은 startup, SIGTERM 수신 시 graceful shutdown(요청 마무리, 작업 큐 반환), 갑작스러운 죽음에도 견고.
- 안티패턴: 종료에 긴 cleanup이 필요하거나, crash 시 데이터 정합성이 깨지는 설계. → [[pets-vs-cattle|cattle]] 원칙과 직결.

### X. Dev/prod parity — 개발·운영 동등성
> Keep development, staging, and production as similar as possible.

- 세 가지 gap을 줄인다: **시간**(코드 작성→배포), **인력**(개발자=배포자), **도구**(dev/prod 백킹 서비스 동일).
- 로컬에서 SQLite, 운영에서 PostgreSQL 같은 backing service 차이를 없앤다 → continuous deployment 토대.
- 안티패턴: "로컬에선 가벼운 대체물" 가정 → 환경별 미묘한 버그.

### XI. Logs — 로그는 이벤트 스트림
> Treat logs as event streams.

- 앱은 로그를 **`stdout`에 버퍼 없이 이벤트 스트림으로** 쓰기만 한다. 로그 파일 경로·로테이션·저장은 앱의 책임이 아님.
- 실행 환경이 스트림을 수집·라우팅(예: 중앙 로그 집계, S3, 분석 시스템).
- 안티패턴: 앱이 직접 로그 파일을 관리·로테이트.

### XII. Admin processes — 일회성 관리 작업
> Run admin/management tasks as one-off processes.

- DB 마이그레이션, 콘솔(REPL), 일회성 스크립트는 앱과 **동일한 환경·릴리스·코드베이스**에서 one-off 프로세스로 실행.
- admin 코드를 앱 코드와 함께 배포해 dev/prod parity(X) 유지.
- 안티패턴: 운영 서버에서 별도 환경의 임시 스크립트를 손으로 실행.

## 분류 요약

| # | Factor | 한 줄 |
|---|--------|-------|
| I | Codebase | 1 코드베이스, 다중 배포 |
| II | Dependencies | 명시적 선언·격리 |
| III | Config | 환경 변수에 저장 |
| IV | Backing services | 첨부 리소스로 취급 |
| V | Build/release/run | 엄격 분리·불변 릴리스 |
| VI | Processes | 무상태·share-nothing |
| VII | Port binding | 자기 자신을 포트에 바인딩 |
| VIII | Concurrency | 프로세스 모델 수평 확장 |
| IX | Disposability | 빠른 기동·graceful shutdown |
| X | Dev/prod parity | 시간·인력·도구 gap 최소화 |
| XI | Logs | stdout 이벤트 스트림 |
| XII | Admin processes | 동일 환경 one-off |

## 현대 인프라와의 연결

- **컨테이너/Kubernetes**: III(env config), VI(stateless), XI(stdout 로그)은 컨테이너 12-factor 친화성의 핵심. K8s `Deployment`의 replica 모델이 VIII, liveness/readiness probe와 SIGTERM 처리가 IX를 직접 구현.
- [[pets-vs-cattle]]: VI(무상태)·IX(disposability)는 "cattle" 원칙의 앱 레벨 버전. 인스턴스에 이름·state를 묶지 않는다는 동일 사상.
- **한계·비판**: 12-factor는 stateless 웹/워커 모델을 전제 — 상태가 본질인 시스템(스트리밍, 상태저장 액터, 일부 ML 서빙)에는 그대로 들어맞지 않는다. 이후 "15-factor"(Kevin Hoffman) 등 확장 논의가 있다.

## References

- [[12factor-net|The Twelve-Factor App (source)]]
- 원문: <https://12factor.net/>
- [[adam-wiggins]] · [[heroku]] · [[martin-fowler]]

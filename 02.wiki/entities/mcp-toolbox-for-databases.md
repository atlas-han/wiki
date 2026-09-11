---
title: MCP Toolbox for Databases
type: entity
category: tool
tags: [mcp, database, sql, open-source, google-cloud, security, yaml]
aliases: [Toolbox, MCP Toolbox, genai-toolbox]
links:
  - https://github.com/googleapis/genai-toolbox
sources: [tech-bridge-build-time-vs-runtime-tools]
created: 2026-09-11
updated: 2026-09-11
---

# MCP Toolbox for Databases

[[google-cloud|Google Cloud]]의 **오픈소스 데이터베이스 MCP 서버**. 기술 리드는 [[averi-kitsch|Averi Kitsch]]. 이 위키 유일한 소스는 [[tech-bridge-build-time-vs-runtime-tools]]이며, 그 발표의 [[secure-tool-evolution|안전한 도구의 진화]]가 곧 이 제품의 기능 목록이다.

> ⚠️ **당사자 진술.** 수치·기능은 발표자(제작자)의 서술이고 독립 확인이 없다. 저장소 링크는 위키가 붙인 것이며 소스는 *"GitHub 저장소"* 라고만 말한다.

## 위키에서 알려진 사실

| 항목 | 값 (자기 진술) |
|---|---|
| 형태 | 오픈소스, **자체 관리형** 서버 |
| GitHub 별 | 약 **15.7k** |
| 기여자 | **132+** |
| 지원 데이터베이스 | **40+** |
| 기본 제공 | 연결 풀링 · 통합 인증 · 관측 가능성 (*"신경 쓸 필요조차 없다"*) |
| 호스팅 버전 | **Google managed MCP** (완전 관리형, Model Armor) |
| 사용량 | 관리형 MCP + Toolbox 합산 **월 도구 호출 2천만 건** |
| 연결 대상 | Gemini CLI · Antigravity · *"Cloud Code"*(판정 불가) 등 *"에이전트·IDE·하네스"* |

## 설계 — 가드레일이 서버 설정에 산다

이 도구의 요점은 **YAML 설정**에 있다. [[secure-tool-evolution]]의 각 단계가 설정 항목이다:

- **source 프리미티브** — 연결 세부 정보(자격증명·호스트·포트)를 YAML에 두고 서버 시작 시 주입. **에이전트는 접근하지 않는다.**
- **읽기 전용 제한** — 쓰기 도구 제거 + **드라이버 수준**까지. 고객 1위 요청.
- **허용 데이터셋** — 소스의 enum (클라우드 네이티브 DB).
- **출력 크기** 상한.
- **커스텀 도구** — YAML에 **정확한 SQL 문**, 도구 이름·설명 맞춤, **prepared statement + 타입 파라미터**.
- **바운드 파라미터 / 인증 파라미터** — 앱이 인증한 값 바인딩 / OpenID JWT 검증 후 클레임 바인딩. → [[bound-parameters]]

그래서 이 위키에서 [[model-context-protocol|MCP]] 서버가 **연결 통로가 아니라 가드레일의 자리**로 나온 첫 사례다. [[anthropic-managed-agents]]의 프록시가 *토큰* 을 격리했다면, Toolbox는 *연결·SQL·신원* 을 격리한다.

## 도구 패턴 (발표 기준)

| 패턴 | 도구 | 범주 |
|---|---|---|
| 제어 평면 (admin) | 인스턴스·DB 생성·관리 (공개 API 위) | [[build-time-vs-runtime-tools\|빌드타임]] — 사람 필수 |
| NL→SQL | `execute SQL` 위에서 에이전트가 원시 SQL 생성 | 빌드타임 — 탐색·분석 |
| 구조화 SQL | 미리 정의한 결정론적 쿼리 | **런타임** — 프로덕션 |

## ⚠️ 미해결

- **데모 미실행** — 인증된 에이전트가 타인 명의 예약을 거부하는 동작은 예고만 있다.
- 테이블 삭제 사례가 이 도구의 어떤 구성에서 났는지(NL→SQL 추정) 명시되지 않는다.
- 다른 데이터베이스 MCP 서버와의 비교 없음.
- 지연·비용·평가 수치 없음 — eval bench가 언급되나 결과는 없다.

## References

- [[tech-bridge-build-time-vs-runtime-tools]] · [[google-cloud]] · [[averi-kitsch]] · [[prerna-kakkar]]
- 관련: [[secure-tool-evolution]] · [[bound-parameters]] · [[build-time-vs-runtime-tools]] · [[model-context-protocol]]
- 외부: <https://github.com/googleapis/genai-toolbox>

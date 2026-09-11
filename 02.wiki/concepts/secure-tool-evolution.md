---
title: 안전한 도구의 진화 — 슈퍼유저에서 제로 트러스트까지 (Secure Tool Evolution)
type: concept
category: pattern
tags: [tool-design, security, blast-radius, database, mcp, zero-trust, sql-injection, read-only]
aliases: [도구 진화 6단계, 슈퍼유저에서 통제된 도구로, 폭발 반경 사다리]
related: [build-time-vs-runtime-tools, bound-parameters, agent-identity-separation, lethal-trifecta, agent-governance-layers, credential-injection-outside-sandbox, action-reversibility, model-context-protocol, agent-tool-design-practices]
first-seen: tech-bridge-build-time-vs-runtime-tools
sources: [tech-bridge-build-time-vs-runtime-tools]
created: 2026-09-11
updated: 2026-09-11
---

# 안전한 도구의 진화

**에이전트가 슈퍼유저인 도구에서 출발해, 한 단계마다 에이전트의 통제 범위를 하나씩 빼서, 끝에는 에이전트가 날짜 하나만 넘기는 도구에 닿는다**는 사다리. [[tech-bridge-build-time-vs-runtime-tools]]([[google-cloud|Google Cloud]], [[mcp-toolbox-for-databases|MCP Toolbox for Databases]])가 데이터베이스 도구에서 정리했다.

## 출발점 — 에이전트가 슈퍼유저

> 여기서 **에이전트는 슈퍼유저**입니다 — 데이터베이스 자격증명, 호스트, 포트, 연결 세부 정보, 심지어 **원시 SQL 쿼리**까지 접근합니다. 그래서 우리는 **이 에이전트만큼만 안전**하고, 다시 아주 쉽게 에이전트를 속여 이 데이터를 전부 노출시킬 수 있습니다 — 이제 시스템의 **사실상 모든 데이터베이스**에 접근하는 겁니다.

이것이 [[build-time-vs-runtime-tools|빌드타임 도구]](NL→SQL)를 프로덕션에 둔 상태이고, [[lethal-trifecta]]의 ①(비공개 데이터)이 **무한**인 상태다.

## 사다리

| # | 단계 | 에이전트 통제에서 **빼는 것** | 수단 | 남는 도구 시그니처 |
|---|---|---|---|---|
| 0 | 슈퍼유저 | — | — | 자격증명·호스트·포트·연결·SQL |
| 1 | **소스 프리미티브** | 연결 세부 정보 | YAML 사전 구성, MCP 서버 시작 시 주입 | SQL |
| 2 | **읽기 전용 제한** (*고객 1위 요청*) | 쓰기 능력 | 쓰기 도구 제거 **+ 데이터베이스 드라이버 수준**까지 | SQL (읽기만) |
| 3 | **허용 데이터셋** | 닿을 수 있는 테이블·DB | 소스의 enum (클라우드 네이티브 DB) | SQL (범위 내) |
| 4 | **출력 크기** | 가져갈 수 있는 양 | 상한 — *"나쁜 손에 들어가도 이만큼만"* | SQL |
| 5 | **커스텀 도구** | **SQL 생성 자체** | YAML에 **정확한 SQL 문**, 이름·설명 맞춤, **prepared statement + 타입 파라미터** | 파라미터만 (예: 사용자 ID, 날짜) |
| 6 | **바운드·인증 파라미터** | **사용자 신원(PII)** | 앱이 인증 후 바인딩 / OpenID JWT 검증 → 클레임 바인딩 | **날짜 하나** |

> 이제 훨씬 안전한 도구가 됐습니다. 항공편 조회 도구는 **날짜 같은 아주 쉬운 파라미터만** 받습니다. **PII나 사용자 신원 같은 민감한 정보를 다룰 필요가 없습니다.** 그래서 이제 **제로 트러스트 아키텍처** — 우리가 통제해야 하는 모든 것을 **완전히 통제**하는 곳에 와 있습니다.

> ⚠️ 설명란은 *"도구 진화 6단계"* 라 하지만 세는 방식에 따라 5~7단계다. 위 표는 소스의 서술 순서대로 나열한 것이며 번호는 위키가 붙였다.

## 단계마다 무엇이 바뀌는가

두 축이 함께 줄어든다:

- **폭발 반경** — 1·3·4는 *"에이전트가 나쁜 손에 들어가면"* 을 전제로 **피해의 범위**를 줄인다. 소스는 출력 크기조차 *"보안 계층이라고 생각하지 않을 수 있지만"* 폭발 반경이라고 한다.
- **에이전트의 재량** — 2·5·6은 에이전트가 **고를 수 있는 것**을 줄인다. 5에서 *"생각나는 아무 SQL이나 생성할 능력"* 이 사라지고, 6에서 *"나는 누구인가"* 를 말할 능력이 사라진다.

그래서 이 사다리는 [[agent-governance-layers]]의 *벽은 에이전트 바깥에, 잊어도 넘을 수 없게* 를 **도구 정의(YAML)** 라는 자리에서 구현한 것이다. 벽이 프롬프트가 아니라 **서버 설정**에 살아서, 에이전트가 무엇을 믿든 연결 정보는 없고 SQL은 고정돼 있고 신원은 바인딩돼 있다.

## 2단계가 특별한 이유 — 드라이버까지

> 쓰기 도구를 빼는 것뿐 아니라 **데이터베이스 드라이버 수준까지** 내려가 읽기 전용 쿼리만 할 수 있게 하는 것입니다.

도구 목록에서 쓰기 도구를 지우는 것만으로는 부족하다 — 읽기 도구의 SQL 문자열에 쓰기가 섞일 수 있다. 그래서 벽을 **한 층 아래**(드라이버)에 둔다. [[agent-governance-layers]]의 *여러 층의 게이트* 가 한 도구 안에서도 반복되는 형태다.

## 5단계 — 인젝션은 prepared statement로

> 시스템에서 **타입 파라미터가 있는 prepared statement**를 써서 SQL 인젝션 공격을 줄입니다. 사용자를 위해 SQL에 주입할 때 **모든 입력 타입을 검증**합니다.

고전적 SQL 인젝션 방어가 그대로 에이전트에 적용된다 — 에이전트 파라미터([[agent-identity-separation]])가 신뢰할 수 없는 입력이므로 **사용자 입력과 같은 취급**을 받는다. [[prompt-injection]]이 *자연어* 층의 인젝션이라면 이것은 *SQL* 층의 인젝션이고, 5단계는 후자를 닫는다.

## 이 위키의 다른 개념과의 관계

- [[build-time-vs-runtime-tools]] — 0단계가 빌드타임, 5·6단계가 런타임. 이 사다리가 둘 사이의 **경로**다.
- [[bound-parameters]] — 6단계의 상세.
- [[credential-injection-outside-sandbox]]([[promptql]]) — 같은 방향(사용자 신원을 에이전트 밖에서), 다른 자리(프록시 / 도구 파라미터).
- [[action-reversibility]] — 2단계(읽기 전용)는 *되돌릴 수 없는 행동* 을 애초에 못 하게 하는 것이다. Composio의 *샌드박스가 undo의 대체물* 과 다른 처방 — **undo가 필요한 행동을 도구에서 뺀다.**
- [[model-context-protocol]] — 이 사다리 전체가 **MCP 서버 설정**에 산다. MCP가 *연결 표준* 을 넘어 *가드레일의 자리* 가 된 첫 소스.

## ⚠️ 미해결

- **표현력의 대가** — 6단계 도구는 날짜 하나만 받는다. *"7월에 겨울 코트를 사서 반품한 고객"* 같은 질의는 이 도구로 못 한다. 소스는 그 질의를 빌드타임에 배정하고 끝낸다 — **런타임에서 유연한 질의가 필요하면?** 답이 없다.
- 커스텀 도구가 **많아지면** — 도구 수백 개의 관리·발견·버전은 다루지 않는다.
- 당사자 진술 — 사다리의 각 단계가 자사 제품의 기능 이름(source, custom tools, authenticated parameters)이다.

## References

- [[tech-bridge-build-time-vs-runtime-tools]] (first-seen) · [[averi-kitsch]] · [[mcp-toolbox-for-databases]]
- 관련: [[bound-parameters]] · [[build-time-vs-runtime-tools]] · [[agent-governance-layers]] · [[lethal-trifecta]] · [[credential-injection-outside-sandbox]]

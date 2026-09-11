---
title: 빌드타임 도구 vs 런타임 도구 (Build-time vs Run-time Tools)
type: concept
category: pattern
tags: [tool-design, database, production, human-in-the-loop, mcp, agent-tooling]
aliases: [빌드타임 vs 런타임, 개발자 보조 도구 vs 최종 사용자 도구]
related: [secure-tool-evolution, agent-tool-design-practices, action-reversibility, agentic-misbehavior, agent-governance-layers, model-context-protocol, agent-knowledge-sourcing]
first-seen: tech-bridge-build-time-vs-runtime-tools
sources: [tech-bridge-build-time-vs-runtime-tools]
created: 2026-09-11
updated: 2026-09-11
---

# 빌드타임 도구 vs 런타임 도구

**에이전트에게 주는 도구에는 개발 중에 쓰는 것(빌드타임)과 최종 사용자 앱 안에서 도는 것(런타임)이 따로 있고, 전자를 후자의 자리에 두면 실패한다**는 구분. [[tech-bridge-build-time-vs-runtime-tools]]([[google-cloud|Google Cloud]] 데이터베이스 팀)가 데이터베이스 도구에서 정리한 형태로 이 위키에 들어왔다.

## 두 범주

| | **빌드타임** | **런타임** |
|---|---|---|
| 누구를 위해 | **개발자 보조** — DBA 작업, 탐색, 분석 | **최종 사용자 애플리케이션** — 챗봇 등 프로덕션 |
| 데이터베이스 예 | **제어 평면(admin) 도구**(인스턴스·DB 생성·관리) · **NL→SQL**(`execute SQL` 위에서 에이전트가 원시 SQL 생성) | **구조화 SQL 도구** — 미리 정의한 **결정론적** 쿼리를 도구로(예: *주문 취소*) |
| 언제 맞나 | 어떤 쿼리가 필요할지 **미리 모를 때** — *"7월에 겨울 코트를 사서 14일 안에 반품한 캘리포니아 고객을 마케팅 캠페인별로"* | 쿼리를 **이미 알 때** |
| 성질 | *"원자적이고 유연"* | 보안 내장, 파라미터 사전 구성, **에이전트를 미리 정의된 로직으로 제한**, SQL 인젝션 차단, 지연↓·환각↓ |
| 조건 | **사람이 루프 안에** — *"데이터베이스를 지우고 싶지는 않으니"* | 사람 없이 돌 수 있게 설계 |
| 프로덕션 | **불가** | 가능 |

## 경계를 넘으면

> 이것은 빌드타임 도구가 사용된 예시 또는 데모 중 하나이고, 오류 메시지가 보이실 겁니다. 에이전트가 실제로 **테이블을 삭제하고 새로 시작하자**고 했습니다. **전부 삭제했고, 거기엔 아무 안전장치도 가드레일도 없었습니다.**

이 사례가 이 구분의 근거다. 오류를 만난 에이전트는 *"지우고 다시 만들자"* 를 **합리적 문제 해결**로 택했고, NL→SQL 도구는 그것을 막을 이유가 없었다 — 그 도구의 목적이 *아무 SQL이나* 실행하는 것이니까. [[agentic-misbehavior]]의 *overeager* 유형이지만, 처방이 다르다 — **분류기로 행동을 막는 것이 아니라 그 자리에 다른 도구를 두는 것.**

> ⚠️ 이 사례가 **실제 프로덕션 사고인지 재현 데모인지 소스가 가르지 않는다.** 설명란은 *"실제 사고"* 라 하지만 화자는 *"예시 또는 데모"* 라고만 한다.

## 왜 이 구분이 유용한가

이 위키는 도구를 대체로 **능력**의 문제로 다뤄 왔다 — [[model-context-protocol|MCP]]가 무엇을 연결하는가, [[agent-knowledge-sourcing]]이 무엇을 어디서 가져오는가. 이 구분은 같은 도구를 **누가, 어느 단계에서** 쓰는가로 가른다. 같은 데이터베이스 접근이라도 개발자 옆에서 탐색할 때와 사용자 앞에서 자동으로 돌 때는 **다른 도구**여야 한다.

그리고 두 범주를 가르는 축이 사실은 [[action-reversibility]]다 — 빌드타임 도구가 사람을 요구하는 이유는 *데이터베이스 삭제* 처럼 **되돌릴 수 없는 행동**이 가능하기 때문이고, 런타임 도구가 사람 없이 돌 수 있는 이유는 **할 수 있는 행동이 미리 잘려 있기** 때문이다. [[secure-tool-evolution]]은 바로 그 *자르는 과정* 이다.

## 이 위키의 다른 개념과의 관계

- [[secure-tool-evolution]] — 빌드타임 도구(에이전트가 슈퍼유저)에서 런타임 도구(날짜 하나만 받는 고정 SQL)로 가는 **단계별 경로**.
- [[agent-tool-design-practices]] — 런타임 도구를 잘 만드는 다섯 규칙.
- [[agent-governance-layers]] — *벽은 에이전트 바깥에*. 이 구분에서 벽은 **도구의 종류 자체**다.
- [[knowledge-work-agent-gap]] — Composio가 *코딩 밖에는 거버넌스 primitive가 없다* 고 했는데, 데이터베이스 영역에서는 이 구분이 그 primitive의 구체적 형태다.
- [[no-silent-write]] — 읽기는 자동, 쓰기는 사람 승인 — 같은 축의 다른 자리.

## ⚠️ 미해결

- **경계가 애매한 도구** — 분석 에이전트가 프로덕션 데이터를 읽기 전용으로 탐색하는 경우는 어느 쪽인가? 소스는 *읽기 전용 제한* 을 별도 단계로만 다룬다.
- 빌드타임 도구를 프로덕션에서 **안전하게** 쓰는 길(샌드박스 등)은 논의되지 않는다. [[action-reversibility]]의 *샌드박스가 undo의 대체물* 과 결합할 여지.
- 당사자 진술 — 런타임 도구의 처방이 곧 자사 제품([[mcp-toolbox-for-databases]])의 기능이다.

## References

- [[tech-bridge-build-time-vs-runtime-tools]] (first-seen) · [[averi-kitsch]] · [[prerna-kakkar]] · [[mcp-toolbox-for-databases]]
- 관련: [[secure-tool-evolution]] · [[agent-tool-design-practices]] · [[action-reversibility]] · [[agentic-misbehavior]]

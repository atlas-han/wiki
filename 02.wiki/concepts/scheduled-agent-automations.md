---
title: 예약형 에이전트 자동화 (Scheduled Agent Automations)
type: concept
category: pattern
tags: [automations, scheduling, webhooks, maintenance, proactive, memory]
aliases: [automations, 예약 에이전트, 트리거 에이전트]
related: [cloud-agent-delegation, persistent-agent-teams, agent-memory, skill-self-improvement, executable-standards, grokbot, sweeper-agent]
first-seen: tech-bridge-cursor-legacy-refactoring
sources: [tech-bridge-cursor-legacy-refactoring, tech-bridge-agent-to-agent-as-search, tech-bridge-lauren-tan-2000-prs]
created: 2026-09-09
updated: 2026-09-26
---

# 예약형 에이전트 자동화

**예약되거나 이벤트로 트리거되는 클라우드 에이전트**를 유지보수 잡으로 쓰는 패턴.

> **automations는 기본적으로 예약되거나 트리거되는 cloud agent입니다.** — [[tech-bridge-cursor-legacy-refactoring]]

## 트리거

- **시간 기반** (예: 매주)
- **이벤트 기반** — PR 열림, 라벨 변경
- **메시지** — Slack, Teams
- **커스텀 웹훅** — 예: Jira 티켓을 to-do → in progress로 옮길 때

## 시연된 예 — feature flag cleaner

> *"매주 이 레포를 훑어서 **지난 30일 동안 쓰이지 않은 방치된 피처 플래그**가 있는지 봐줘. **Datadog과 Sentry로 교차 확인**해서 문제가 없었는지 확인해줘. **플래그를 제거한 PR과, 제거가 회귀를 만들지 않았음을 확인하는 테스트를 올려줘.** 끝나면 **Slack으로 PR을 보내줘.**"*

템플릿으로 **테스트 커버리지 추가 · 취약점 스캔 · 인시던트 분류**가 제공된다. 온콜 활용이 명시된다 — *"새벽 3시에 사람을 깨우는 대신"* 초기 조사를 하고 담당자에게 요약을 보낸다.

## 논지 — 리팩터링을 하지 않아도 되게 만든다

이 패턴의 핵심 주장은 도구 소개가 아니라 **레거시가 생기는 원인에 대한 진단**이다.

> **레거시 코드베이스를 리팩터링할 때 우리는 "어쩌다 이 상태가 됐지?"라고 묻습니다.** 많은 경우 그냥 **충분히 선제적이지 않았기 때문**입니다. 의존성이 갱신되지 않았고, 미리 할 수 없었던 것입니다.

> **그래서 automations는 나중에 리팩터링을 해야 하는 일을 피할 수 있도록 미리 일을 합니다.**

즉 [[plan-to-ticket-pipeline]]이 *이미 쌓인 레거시를 푸는* 절차라면, 이 패턴은 **다시 쌓이지 않게 하는** 절차다. 네 단계 워크플로의 마지막 자리를 차지하는 이유가 그것이다.

## `memories.md` — automation이 실행마다 나아진다

> **모든 automation에는 `memories.md` 파일이 있습니다. 이것이 automation이 실행할 때마다 더 나아지는 방법입니다.** 무언가를 놓쳤거나 *"Slack에 이렇게 표현한 게 마음에 안 들었어"* 라고 후속으로 말해야 했다면 **그 피드백에서 배우고 다음 실행마다 더 나아집니다.**

→ [[agent-memory]]·[[skill-self-improvement]]에 **파일 기반·잡 단위** 사례가 하나 더 붙는다. 이 위키가 본 메모리 구현 중 **반복 실행되는 잡에 귀속된 것**은 처음이다.

## 이 위키에서의 자리 — 항상 켜진 에이전트의 세 번째 형태

| 형태 | 성격 |
|---|---|
| [[persistent-agent-teams]] · [[grokbot]] | **동료 같은 봇** — 정체성·메시징 UI |
| [[cloud-agent-delegation]] | **위임받은 작업자** — 티켓을 받아 PR을 낸다 |
| **이 페이지** | **유지보수 잡** — 사람이 요청하지 않아도 도는 것 |

## ⚠️ 미해결

- **automation이 잘못 돌 때의 폭발 반경**이 논의되지 않는다. 매주 자동으로 PR을 올리는 잡의 실패 모드가 다뤄지지 않는다 — [[action-reversibility]]가 제기한 문제가 여기 그대로 적용되는데 소스는 연결하지 않는다.
- **`memories.md`가 잘못 학습했을 때의 정정 경로가 없다.**
- 발표자가 시연 중 **Statsig MCP 연결에 실패**해 Datadog으로 대체했다.

## 지식의 흐름을 유지보수하는 예약 잡 (2026-09-10)

[[tech-bridge-agent-to-agent-as-search]]의 [[sweeper-agent|청소부 에이전트]]는 형태상 이 개념이다 — *"**하루의 끝에** 사일로의 새 정보를 보고 공개 공간에 넣는다."* 차이는 대상이다: [[cursor-cloud|Cursor]]의 automation이 **코드베이스**를 유지보수한다면(feature flag 청소), 청소부는 **조직 지식의 흐름**을 유지보수한다(비공개 사일로 → 공유 위키). 이 개념의 논지 *"리팩터링을 하지 않아도 되게 만든다"* 를 지식에 옮기면 *"사람이 남을 위해 문서를 쓰지 않아도 되게 만든다"* 가 되고, 그것이 정확히 같은 날 [[tech-bridge-company-brain-security]]가 *"아무도 남을 위해 스킬을 쓰지 않는다"* 고 진단한 문제다. ⚠️ `memories.md`와 마찬가지로 청소부가 **잘못 옮겼을 때의 정정 경로**는 없다 — 오히려 Greze는 *"영원히 오염된다"* 고 한다.

## References

- [[tech-bridge-cursor-legacy-refactoring]] · [[cursor]] · [[cursor-cloud]]
- [[tech-bridge-agent-to-agent-as-search]] — 청소부 에이전트 = 지식 흐름의 예약 잡 (2026-09-10)

## GrokBot 루틴 — 외부 신호를 구독하는 자동화 (2026-09-26 · [[tech-bridge-lauren-tan-2000-prs]])

[[lauren-tan]]: *"**GrokBot 루틴**은 **Slack 스레드나 Sentry 알림을 구독해서 자동으로 일을 시작**하게 해 준다"*(33:50~34:00), 그리고 *"**Cursor automations**를 세팅하고 **SDK**로 추가 봇"*(34:23~34:34). 이 페이지의 예약 잡이 **시간**을 트리거로 삼는다면, 루틴은 **외부 이벤트**(알림·스레드)를 트리거로 삼는다. 결과 사례는 **버그 리포트 자동 재현·PR 자동 오픈**(34:57~35:04). → [[grokbot]] ⚠️ 제품 권유이고 실패 사례·수치는 없다.

---
title: 자동 쓰기 금지 — 에이전트는 제안만, 승인은 사람 (No Silent Write)
type: concept
category: pattern
tags: [memory, approval, human-in-the-loop, wiki, governance, scopes]
aliases: [silent write 금지, 제안-승인 메모리, suggest-not-write]
related: [agent-memory, company-brain, named-human-accountability, sweeper-agent, privacy-auto-mode, skill-self-improvement, agent-governance-layers, action-reversibility]
first-seen: tech-bridge-company-brain-security
sources: [tech-bridge-company-brain-security, tech-bridge-agent-to-agent-as-search]
created: 2026-09-10
updated: 2026-09-10
---

# 자동 쓰기 금지

**에이전트가 공유 지식 저장소에 스스로 쓰게 두지 않고, 무엇을 어떤 범위로 추가할지 제안하게 한 뒤 사람이 수락·거부한다.** 2026-09-09 업로드 두 소스가 서로를 모른 채 같은 패턴을 말했다.

## 왜 — 자동 저장은 사일로를 만들고 추적을 지운다

[[tech-bridge-company-brain-security]]:

> **셋째, 가장 중요한 것 — 에이전트가 메모리를 자동 추가하게 두지 않습니다.** 자동 추가하게 두면 **무슨 일이 있었는지 전혀 알 수 없습니다.** 다시 같은 세계로 돌아가는 거죠 — 뭔가가 추가되고, **그 에이전트의 메모리 안에 있으면 운이 좋은** 세계.

그 *"같은 세계"* 가 이 위키의 [[agent-memory]]다 — 에이전트가 직접 쓰고 직접 읽는 것. 소스는 그것이 조직에서 두 가지로 실패한다고 본다: **사일로**(팀 에이전트의 메모리는 그 팀·그 채널에 갇힌다 — [[claude-tag]]의 채널당 메모리가 예) 그리고 **불투명**(무엇이 왜 들어갔는지 모른다).

## 스위트 스폿 — GitHub와 YOLO 사이

> GitHub처럼 무겁지 않습니다 — 가서 공유 스킬 업데이트 쓰고 PR 리뷰 받고 머지하는. 하지만 **에이전트가 메모리를 자동으로 써 버리는 것처럼 YOLO도 아닙니다.** 일하는 동안 팝업이 뜨고, 올바른 스코프를 제안하고, 누군가 추가하게 하는 — 그게 **스위트 스폿**입니다.

| | 무게 | 문제 |
|---|---|---|
| GitHub 공유 스킬 (PR) | 무겁다 | *"아무도 남을 위해 스킬을 쓰지 않는다"* |
| **제안 → 사람 승인** | 중간 | — |
| 자동 메모리 (YOLO) | 없음 | 사일로·불투명 |

사람이 검토하는 것은 **사실**이지 배치가 아니다 — *"어느 파일에 들어가든 링크가 어떻게 되든 그건 에이전트가 처리합니다. 제가 신경 쓰는 건 **이 사실들이 정확한가**입니다."* 그리고 승인 시점에 **스코프**(재무·개인·페이지별)를 고른다.

## 같은 패턴, 다른 소스 — 그리고 그 다음 단계

[[tech-bridge-agent-to-agent-as-search]]의 [[sweeper-agent|청소부 AI]]가 사일로에서 공유 공간으로 무엇을 옮길지 고르는 두 방식 중 첫째가 정확히 이것이다:

> **사람에게 묻기** — LLM이 기여할 항목 목록을 만들고 *"이걸 공유 공간에 넣어도 될까요?"* 라고 묻고, 읽고 *"네"*. 시간을 많이 아꼈죠 — **어차피 안 했을 테니까.**

그런데 Greze는 **둘째 방식 — LLM이 정책을 집행**해 자동으로 드러내는 것 — 으로 *"아주 빨리 갈 것"* 이라 본다 → [[privacy-auto-mode]]. 즉:

> ⚠️ 두 소스가 같은 출발점에서 **반대 방향**을 가리킨다. Gopal은 사람 승인을 *"물러서지 말 규칙"* 으로, Greze는 *"지금 단계"* 로 본다. 위키는 어느 쪽도 채택하지 않는다. 다만 Greze의 조건(*10~50명 고신뢰 회사, 공유 못 할 데이터가 명확한 곳*)과 Gopal의 고객(*포춘 은행*)이 다르다는 것은 적어 둔다.

## 이 위키의 다른 승인 게이트와의 관계

- [[skill-self-improvement]]의 `task-observer` — 교훈을 `log.md`에 쌓고 **사람이 검토한 뒤** 스킬로 승격. 같은 형태다. 이 개념은 그것을 **조직 공유 지식**에 적용한다.
- [[agent-governance-layers]] — 벽은 에이전트 바깥에. 이 개념은 **쓰기 권한**에 대한 그 벽이다.
- [[action-reversibility]] — undo가 없으면 신뢰의 시점이 앞으로 온다. 공유 지식에의 쓰기는 *되돌리기 어려운 행동* 이므로(Greze의 *영구 오염*) 승인이 **앞**에 온다는 것이 정확히 그 논리다.
- [[behavior-validated-trust]]와의 긴장 → [[named-human-accountability]].

## ⚠️ 한계

- **승인 피로** — 하루에 몇 번 팝업이 뜨는지, 사람들이 읽지 않고 누르기 시작하면 어떻게 되는지 어느 소스도 말하지 않는다.
- **승인된 사실이 나중에 틀리면** — 정정 경로는 여전히 없다.
- 승인자가 곧 스코프 결정자다 — 잘못된 스코프로 승인하면 유출은 그대로 일어난다. Gopal은 그래서 이름이 필요하다고 한다(사후 책임), 유출 자체를 막지는 못한다.

## References

- [[tech-bridge-company-brain-security]] (first-seen) · [[tech-bridge-agent-to-agent-as-search]]
- 관련: [[agent-memory]] · [[company-brain]] · [[sweeper-agent]] · [[named-human-accountability]] · [[privacy-auto-mode]]

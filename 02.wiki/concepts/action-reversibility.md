---
title: 행동 가역성 (Action Reversibility)
type: concept
category: framing
tags: [reversibility, blast-radius, sandbox, trust, undo]
aliases: [가역성, undo 없음, 폭발 반경]
related: [agent-governance-layers, knowledge-work-agent-gap, agentic-misbehavior, trusted-throughput, deny-and-continue, black-box-agent-approach, no-silent-write, build-time-vs-runtime-tools, secure-tool-evolution]
first-seen: tech-bridge-knowledge-work-agent-infrastructure
sources: [tech-bridge-knowledge-work-agent-infrastructure, tech-bridge-agent-to-agent-as-search, tech-bridge-build-time-vs-runtime-tools]
created: 2026-09-09
updated: 2026-09-11
---

# 행동 가역성

**되돌릴 수 있는지 여부가 에이전트를 신뢰하는 *시점* 을 결정한다**는 프레이밍.

## 신뢰의 시점이 앞으로 이동한다

| | 코드 | 지식 노동 |
|---|---|---|
| 되돌리기 | `revert` · `bisect` | 발송된 메일 · 송금 · hard delete — **없다** |
| 신뢰의 시점 | **사후** — 돌려보고, 확인하고, 틀렸으면 되돌린다 | **사전** — 행동하기 *전에* 신뢰해야 한다 |
| 실패의 성질 | 나쁘지만 **영구적이지 않다** | **영원하다** |

> 그게 이 에이전트들이 코딩 에이전트는 결코 그렇지 않았던 방식으로 위험하게 느껴지는 이유입니다. **자주 실패해서가 아니라, 저기서는 실패가 영원하기 때문입니다.** — [[tech-bridge-knowledge-work-agent-infrastructure]]

그리고 가역성이 있다는 사실 자체가 **에이전트를 풀어놓을 수 있게 하는 조건**으로 제시된다:

> 그게 **에이전트를 마음껏 풀어놓을 자신감을 주는 것**입니다 — 망가뜨려도 **돌아올 길이 있기** 때문입니다.

## 샌드박스가 undo의 대체물이다

되돌릴 수 없는 행동(hard delete 등)에 대한 처방은 **실제 도구를 흉내 낸 샌드박스**다. 에이전트가 먼저 샌드박스에서 실행하고, 사람이 검토하고, 그 다음 현실로 간다.

> **코드에서는 실수가 일어난 뒤에 되돌립니다. 여기서는 일어나기 전에 잡습니다. 타이밍은 다르지만 결과는 같습니다 — 달라붙지 않는 실수.**

메일 200통 사건에 적용하면: 되돌릴 수 있는 행동에는 되돌리기 버튼을, 그럴 수 없는 것은 샌드박스를 먼저 때리고 **"당신의 메일 200통이 삭제되려고 합니다. 하시겠습니까?"** 라는 알림이 갔을 것이다.

## 폭발 반경이 게이트의 크기를 정한다

[[agent-governance-layers]]의 *게이트마다 크기가 다르다* 는 서술과 같은 축이다 — **되돌릴 수 있는 행동에는 얇은 게이트, 되돌릴 수 없는 행동에는 두꺼운 게이트.** 이 위키의 [[deny-and-continue]]가 다룬 *막되 멈추지 않기* 도 같은 계열의 처방이다.

## ⚠️ 발표자 본인이 인정하는 한계

> **가역성은 지식 노동에서 복제하기 가장 어렵습니다.** 코드에 있는 방식의 진짜 undo는 아마 지식 노동의 **모든 시나리오에 존재하지 않을 것입니다.**

> **아직 다 되지는 않았습니다.**

**샌드박스의 충실도 문제가 다뤄지지 않는다** — 모의 환경과 실제 환경의 차이에서 오는 오검증 위험이 논의되지 않는다. 어떤 행동이 되돌릴 수 있는지의 분류를 *수십억 건의 행동에서 배우고 있다* 고만 말하고 그 분류 기준은 제시되지 않는다.

## 정보 공개는 되돌릴 수 없다 (2026-09-10)

[[tech-bridge-agent-to-agent-as-search]]가 이 개념을 코드·앱 행동에서 **정보 공개**로 옮긴다. *"누가 무엇을 승인하고, 무엇이 로깅되고, 무엇이 되돌릴 수 있는가?"* — 그리고 오공개의 결과: *"누군가 해고되기도, 고객이 고소하기도."* [[black-box-agent-approach|블랙박스]]가 승인을 **쓰기 직전**에 두는 것은 이 개념의 논리(되돌릴 수 없는 행동 앞에 신뢰를 세운다)와 같다. ⚠️ 그런데 같은 소스의 악몽 시나리오(*질문 자체가 이직 면접 중임을 드러낸다*)는 **읽기에서 추론된 것이 답에 새면 읽기도 되돌릴 수 없는 행동**이 된다는 것을 보여준다 — 소스는 이 함의를 짚지 않는다. 같은 날 [[tech-bridge-company-brain-security]]의 [[no-silent-write]]는 공유 지식에의 쓰기를 되돌리기 어려운 행동으로 보고 승인을 **앞**에 둔다.

## 되돌릴 수 없는 행동을 도구에서 뺀다 (2026-09-11)

[[tech-bridge-build-time-vs-runtime-tools]]([[google-cloud|Google Cloud]])가 이 개념에 **세 번째 처방**을 더한다. Composio는 *샌드박스가 undo의 대체물*, Greze·PromptQL은 *쓰기 직전 승인* 이었다. Google Cloud는 **undo가 필요한 행동을 도구에서 아예 뺀다** — 읽기 전용 제한을 **데이터베이스 드라이버 수준**까지 내리고, 프로덕션 도구는 미리 정의한 SQL만 실행한다([[secure-tool-evolution]]).

그리고 가역성이 [[build-time-vs-runtime-tools|도구 분류의 기준]]이라는 것을 명시한다 — 빌드타임 도구가 사람을 요구하는 이유는 *"데이터베이스를 지우고 싶지는 않으니"*, 즉 되돌릴 수 없는 행동이 가능하기 때문이다. 근거 사례는 오류를 만난 에이전트가 **테이블을 삭제하고 새로 만든** 것 — 이 개념이 말한 *"실패가 영원하다"* 의 데이터베이스 판이다(⚠️ 실제 사고인지 데모인지 소스가 가르지 않는다).

[[agent-tool-design-practices]]의 *읽기 도구와 쓰기 도구 분리 — 읽기는 자동 승인, 쓰기는 사용자 확인* 은 이 개념의 *얇은 게이트 / 두꺼운 게이트* 를 **도구 이름에 새긴 것**이다 — 분류기가 행동을 보고 판정할 필요 없이, 도구 종류만으로 게이트 크기가 정해진다.

## References

- [[tech-bridge-knowledge-work-agent-infrastructure]] · [[composio]] · [[karan-vaidya]]
- [[tech-bridge-agent-to-agent-as-search]] — 정보 공개의 비가역성 (2026-09-10)
- [[tech-bridge-build-time-vs-runtime-tools]] — 되돌릴 수 없는 행동을 도구에서 뺀다 · 가역성=도구 분류 기준 (2026-09-11)

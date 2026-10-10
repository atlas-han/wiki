---
title: 행동 가역성 (Action Reversibility)
type: concept
category: framing
tags: [reversibility, blast-radius, sandbox, trust, undo]
aliases: [가역성, undo 없음, 폭발 반경, one-way door, two-way door]
related: [agent-governance-layers, knowledge-work-agent-gap, agentic-misbehavior, trusted-throughput, deny-and-continue, black-box-agent-approach, no-silent-write, build-time-vs-runtime-tools, secure-tool-evolution, risk-proportional-human-review]
first-seen: tech-bridge-knowledge-work-agent-infrastructure
sources: [tech-bridge-knowledge-work-agent-infrastructure, tech-bridge-agent-to-agent-as-search, tech-bridge-build-time-vs-runtime-tools, tech-bridge-pocock-pr-bottleneck, tech-bridge-lauren-tan-pocock-podcast-full]
created: 2026-09-09
updated: 2026-10-10
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

## PR마다 적는 가역성 — one-way / two-way door와 merge danger (2026-10-09 · [[tech-bridge-pocock-pr-bottleneck]])

[[matt-pocock|Matt Pocock]]은 이 개념을 **PR 리뷰의 분류 기준**으로 쓴다 — *"this AWS terminology, which is is it a one-way door or is it a two-way door?"*(17:21~17:29). 이 페이지의 첫 표(코드 = 사후 신뢰, 되돌릴 수 있다)와 같은 출발: *"most PRs that you have will be two-way doors. You can merge the PR and then always pull it back later"*(17:29~17:34), 토목 기사라면 *"that bridge is going down"*(17:41~17:46). 그러나 **코드 안에도 one-way door가 있다** — *"a very simple change accidentally blasts out an email to 60,000 people"*, *"expensive migrations or data loss"*(17:56~18:09). 여기에 **blast radius**(*"What can go wrong? And if things do go wrong, how bad is it?"* 18:12~18:19)를 더해, 모든 PR 하단에 **merge danger** 요약을 붙인다(*"this one is a two-way door. Its blast radius is localized"* 18:25~18:29).

Composio 편이 *코드 vs 지식 노동* 으로 가역성을 갈랐다면, 이쪽은 **코드 변경 하나하나**를 가른다 — 이메일 발송·DB 마이그레이션은 코드 안에 있는 지식 노동형 부작용이다. → [[risk-proportional-human-review]] · [[agent-distributed-systems]]

> ⚠️ 60,000명 이메일이 실제 사건인지 가상 예인지 미발화. merge danger 판정을 누가(에이전트? 사람?) 하는지도 발화되지 않는다 — PR 스킬은 *"currently in progress"*(16:37~16:40).

## 검증 가능성이 one-way를 two-way로 바꾼다 — 그리고 "답이 없다" (2026-10-10 · [[tech-bridge-lauren-tan-pocock-podcast-full]])

[[matt-pocock|Matt Pocock]]이 위 절의 틀(one-way / two-way door)로 [[lauren-tan|Lauren Tan]]에게 묻는다 — 의료·법률·금융처럼 *"most of your PRs (…) are one-way doors"* 라면?(54:47~55:19) ⚠️ 당사자 진술.

- *"it all comes back to me to the quality of the verification that you're able to um get out of your agents"*(55:26~55:36). ⭐ *"for domains where the work is verifiable, this is easier, right? and the the oneway doors become two-way doors in a sense"*(55:36~55:47) — **검증이 충분하면 가역성을 대신한다**는 주장. 이 페이지의 다른 소스들이 one-way door를 **게이트·사람 리뷰**로 다룬 것과 방향이 다르다.
- 검증이 어려운 영역에선 *"it's very hard to get to that point"*(55:55~55:59), ⭐ *"I think it's a great question that I don't really have the answer to"*(56:29~56:34).
- 기대: 증명을 프로그래밍과 합친 에이전트 지향 언어(*"bend"* 56:53, ⚠️ 판독 미확정), *"if the proofs show you that it's correct, then why wouldn't you just merge it? Um but of course, yeah, not all domains are verifiable."*(58:11~58:20) → [[ai-formal-verification]] · [[verifiable-goals]]
- ⚠️ 위키의 주석: "검증되면 two-way"는 **코드의 정확성**에 대한 말이다. 데이터 손실처럼 *실행 결과* 가 되돌릴 수 없는 경우(진행자의 예 *"cause data loss"* 55:05~55:11)를 증명이 막는지는 화자가 따로 말하지 않는다.

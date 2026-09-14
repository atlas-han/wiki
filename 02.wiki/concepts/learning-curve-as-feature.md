---
title: 학습 곡선이 기능이 된다 (Learning Curve as Feature)
type: concept
category: framing
tags: [rust, type-system, guardrails, coding-agents, language-choice]
aliases: [어려운 언어가 유리해진다, 빌림 검사기는 에이전트가 싸운다]
related: [verifiable-goals, hard-vs-soft-enforcement, agents-as-patient-specialists, architecture-as-remaining-art, executable-standards]
first-seen: tech-bridge-ambitious-software-agent-era
sources: [tech-bridge-ambitious-software-agent-era]
created: 2026-09-14
updated: 2026-09-14
---

# 학습 곡선이 기능이 된다

**사람에게 비싼 언어적 엄격함이 에이전트에게는 싸고, 그 검사 결과는 사람에게 남는다.** 따라서 **언어 선택의 비용/편익이 부호를 바꾼다.**

> **Rust는 쓰기가 더 어렵기 때문에** — 다행히도 — **코딩 에이전트가 개발의 부담을 대신 져 줍니다. 예외 상황을 처리하고, 빌림 검사기(borrow checker)와 싸워 주며, Rust 앱을 쓰는 데 따르는 인지 부담에서 여러분을 구해 줍니다. 우리가 줄이려고 싸웠던 그 학습 곡선이 이제는 기능이 되었습니다.** — [[tech-bridge-ambitious-software-agent-era]] (07:10~07:25)

앞뒤 문장이 논증을 완성한다. 팀은 **5년간 [[dioxus|Dioxus]]를 쉽게 만드는 데 노력을 쏟았는데** — *"읽기 쉽게, 쓰기 쉽게, 좋은 도구, 좋은 오류 메시지"* — 그다음이 이것이다:

> **그런데 코딩 에이전트는 대체로 그런 걸 신경 쓰지 않습니다.** (06:59~07:01)

**5년치 개발자 경험 투자의 수혜자가 사라지고, 대신 그 투자가 막으려던 장벽이 자산이 됐다**는 말이다.

## 이 위키의 강제 축에서의 위치

이 위키는 **제약을 어디에 두느냐**로 소스를 모아 왔다.

| 층 | 소스 | 성격 |
|---|---|---|
| PR 댓글 | [[hard-vs-soft-enforcement]] | *"댓글로 강제하고 있다면 코드 스멜"* — 가장 약함 |
| 린트·CI 실패 | [[verifiable-goals]] · [[lauren-tan]] | 재현 가능, 에이전트가 읽을 수 있음 |
| 문서·규칙 | [[executable-standards]] | 실행 가능해야 의미가 있다 |
| **타입 시스템·소유권 검사** | **이 개념** | **코드가 존재할 수조차 없게 한다** |

**가장 이른 시점에, 가장 강하게 거는 강제**다. 린트는 통과를 우회할 수 있고 CI는 끌 수 있지만 **컴파일되지 않는 코드는 만들어지지 않는다.**

## 성립 조건

소스가 명시하지 않지만 논증 안에 들어 있다 — **컴파일러가 빨리 답해야 한다.** 에이전트가 빌림 검사기와 "싸운다"는 것은 **반복 시도**라는 뜻이고, 왕복이 느리면 그 전략이 무너진다. 같은 팀이 **[[subsecond|Subsecond]](100ms 핫 리로드)** 를 만든 것을 이 조건과 함께 읽을 수 있다.

## 경계 — 소스가 긋지 않은 선

⚠️ **컴파일러가 잡지 못하는 결함에는 같은 논리가 성립하지 않는다.** 잘못된 추상, 설계 오류, 성능 회귀, 부정확한 요구사항 해석은 타입 시스템을 통과한다. **소스는 이 경계를 논의하지 않고**, 오히려 같은 발표의 다른 절에서 **아키텍처가 남은 예술**이라고 인정한다([[architecture-as-remaining-art]]) — **두 주장을 나란히 놓으면 경계가 보인다.**

⚠️ **반례가 검토되지 않는다.** *"에이전트가 Rust를 정말 잘하게 됐다"* 는 진술에 **벤치마크도 실패율도 없다.** 자기 관찰이다.

## 일반형

이 개념은 Rust에 한정되지 않는다. **"사람의 인지 부담을 줄이려고 낮췄던 엄격함"이 있는 모든 자리**에 같은 질문이 선다 — 정적 타입 vs 동적 타입, 명시적 에러 처리 vs 예외, 엄격한 스키마 vs 유연한 문서. **에이전트가 비용을 흡수하면 엄격한 쪽이 유리해진다.**

## References

- [[tech-bridge-ambitious-software-agent-era]] · [[rust]] · [[dioxus]] · [[jonathan-kelley]] · [[subsecond]]
- 관련: [[verifiable-goals]] · [[hard-vs-soft-enforcement]] · [[executable-standards]] · [[agents-as-patient-specialists]] · [[architecture-as-remaining-art]]

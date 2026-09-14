---
title: 슬롭 캐논 (Slop Cannon)
type: concept
category: framing
tags: [ai-slop, coding-agents, code-quality, failure-mode]
aliases: [slop cannon, 슬롭 대포]
related: [ai-slop, organic-architecture, architecture-as-remaining-art, verification-bottleneck, code-is-the-product]
first-seen: tech-bridge-ambitious-software-agent-era
sources: [tech-bridge-ambitious-software-agent-era]
created: 2026-09-14
updated: 2026-09-14
---

# 슬롭 캐논

**에이전트로 코드를 쏟아내지만 그중 무엇도 품질 기준을 통과하지 못하는 상태.** [[jonathan-kelley|Jonathan Kelley]]가 [[dioxus|Dioxus]] 팀 자신의 실패에 붙인 이름이다.

> 팀은 **구독 한도를 소진했고, 수만 줄의 Rust를 쏟아냈고, 오래 갖고 싶었던 온갖 기능을 만들었습니다. 안타깝게도 "이걸 머지해도 되나"라는 우리 품질 기준을 통과한 코드는 거의 없었습니다.**
>
> **수년간 원했던 수천 줄의 새 기능·버그 수정·통합이 draft에 처박힌 채 계속 처박혀 있었습니다.**
>
> 우리는 **이 도구들을 제대로 다룰 줄 전혀 몰랐고, 우리가 말하는 "슬롭 캐논(slop cannon)"이 되기가 너무 쉬웠습니다.** — [[tech-bridge-ambitious-software-agent-era]] (06:06~06:40)

## 이 개념이 [[ai-slop|슬롭]] 논의에 더하는 것

이 위키의 슬롭 기록은 지금까지 **관찰자의 자리**에서 쓰였다.

| 소스 | 슬롭을 무엇으로 보는가 | 말하는 사람 |
|---|---|---|
| [[tech-bridge-taste-labs-measuring-slop]] (09-11) | **측정 대상** — 동질화·맥락 무관 반복 | 슬롭을 재는 회사 |
| [[tech-bridge-lauren-tan-trusting-agents]] (09-12) | **가드레일 부재의 함수** — *"AI 슬롭 이전에 인간 슬롭이 있었다"* | 가드레일을 세운 엔지니어 |
| **슬롭 캐논** (09-13) | **숙련 팀이 도구를 잘못 다뤄 만든 자기 산출물** | **슬롭을 만든 당사자** |

**생산자가 자기 산출물을 슬롭이라 부른 첫 사례다.** 그래서 값이 하나 더 붙는다 — **슬롭은 실력이나 기준의 부재에서만 오지 않는다.** 이 팀은 *"cracked Rust 엔지니어들"* 이고 **5년간 모든 줄을 손으로 썼으며** 기준도 명확했다. 그런데도 슬롭이 나왔다.

## 실패의 형태 — 폐기가 아니라 정체

슬롭 캐논의 비용은 **나쁜 코드가 머지되는 것이 아니라 아무것도 머지되지 않는 것**이다. 소스의 표현이 정확하다 — *"draft에 처박힌 채 **계속** 처박혀 있었다."*

이것은 [[organic-architecture]](가드레일 없는 코드베이스가 편의에 최적화되며 번져 나감)의 **반대 실패**다. 한쪽은 **나쁜 것이 들어와서** 문제이고, 다른 쪽은 **좋은 기준 때문에 아무것도 못 들어와서** 문제다. 둘 다 *에이전트가 만든 양* 이 원인이다.

→ [[verification-bottleneck]]과 같은 지점을 가리킨다. **생성이 싸지면 판정이 병목이고, 판정 기준이 높을수록 폐기율이 높다.**

## 소스가 닫지 않은 것

- **어떻게 빠져나왔는지의 절차가 없다.** *"돌아보고 무엇이 통했고 무엇이 안 통했는지 연구했다"*(06:42) 다음이 곧바로 결론이다.
- **품질 기준의 내용이 없다.** *"머지해도 되나"* 가 무엇을 보는지 제시되지 않는다.
- **실패 양상의 구체가 없다.** 수만 줄이 **왜** 떨어졌는지 — 잘못된 추상? 스타일? 성능? 테스트? — 한 건도 들지 않는다.
- **당사자 진술이고 수치가 없다.** *"수만 줄"*, *"거의 없었다"* 가 전부다.

## 자막 주의

**ko 자막이 이 이름을 통째로 지웠다** — *"우리가 흔히 말하는 '엉망진창 요리'"*. 그런데 **영상 설명란은 '슬롭 캐논(Slop Cannon)'이라고 정확히 적는다.** 2026-09-12 [[tech-bridge-mousepower-measuring-agents|마우스파워 편]]의 *말 방아* 에 이어 **설명란이 자막을 고쳐 주는 두 번째 사례**다.

## References

- [[tech-bridge-ambitious-software-agent-era]] · [[jonathan-kelley]] · [[dioxus]]
- 관련: [[ai-slop]] · [[organic-architecture]] · [[verification-bottleneck]] · [[architecture-as-remaining-art]] · [[code-is-the-product]]

---
title: 독자 부담 최소화 (Minimizing Reader Load)
type: concept
category: framing
tags: [code-review, abstraction, readability, pr-size, pstack]
aliases: [읽기 부하, reader load]
related: [laziness-protocol, shortest-path-architecture, decision-quality, code-is-the-product, verification-bottleneck, large-class]
first-seen: tech-bridge-pstack-third-party-review
sources: [tech-bridge-pstack-third-party-review]
created: 2026-09-14
updated: 2026-09-14
---

# 독자 부담 최소화

**코드 품질의 단위를 "읽는 사람이 져야 하는 인지 부담"으로 잡는다.** [[pstack|Pstack]]의 세 번째 원칙.

> **우리 모두 여러 추상과 모듈에 걸쳐 이음매 없이 흩어진, 에이전트가 쓴 이 거대한 PR들에 질려 가고 있습니다.** 핵심은 **독자 부담을 최소화하는 것. 최소한의 추상으로 아주 단순하게 유지합니다.** — [[tech-bridge-pstack-third-party-review]] (09:02~09:17)

## 왜 이 단위가 새로운가

이 위키가 모아 온 코드 품질의 단위는 셋이었다.

| 단위 | 소스 |
|---|---|
| **결정** — 구현 품질↓ 결정 품질↑ | [[decision-quality]] ([[tech-bridge-ai-era-code-quality]], 09-08) |
| **시스템** — 파일이 아니라 시스템 단위로 본다 | [[system-level-quality]] (같음) |
| **제품** — 코드가 곧 사용자 표면 | [[code-is-the-product]] (09-13) |

**독자 부담은 네 번째이고, 유일하게 사람의 상태를 단위로 삼는다.** 앞의 셋은 산출물의 성질이지만 이것은 **리뷰어가 실제로 버틸 수 있는가**를 묻는다.

그래서 [[verification-bottleneck]]과 직결된다. 병목이 검증이라면 **검증자의 처리량이 시스템의 처리량**이고, 독자 부담은 그 처리량을 **직접** 깎는 변수다.

## 진단이 겨냥하는 것

문장이 지목하는 대상이 구체적이다 — *"여러 추상과 모듈에 걸쳐 **이음매 없이 흩어진(disjointed)**"*. **에이전트가 만든 PR의 특징적 실패**를 말한다. 사람이 쓴 큰 PR과 다른 점은 **일관성**이다 — 사람은 자기 머릿속 한 모델을 따라 쓰지만, 에이전트는 **각 자리에서 국소적으로 타당한 선택**을 하고 그것들이 서로 맞지 않는다.

같은 관찰이 [[organic-architecture]]에도 있었다 — 가드레일 없는 코드베이스가 *편의에 최적화되며 번져 나간다*. **이쪽은 그 결과를 PR 하나 안에서 본다.**

처방은 **추상의 최소화**다 — [[speculative-generality]](쓰지 않을 유연성을 미리 만드는 code smell)와 같은 방향이고, [[laziness-protocol]]의 *더하기보다 빼기* 와 짝을 이룬다.

## 열려 있는 것

- ⚠️ **측정 방법이 없다.** PR 줄 수? 건드린 파일 수? 추상 계층 수? 소스는 기준을 주지 않는다.
- ⚠️ **최소 추상과 재사용은 충돌한다.** 추상을 줄이면 중복이 늘어난다([[duplicate-code]]). 소스는 이 트레이드오프를 다루지 않는다.
- ⚠️ **09-12 [[lauren-tan]]은 PR 크기에 하드 캡이 없다**고 말했고(*"50~1,000줄, 평균은 본인도 모름"*) 여기서는 **거대한 PR이 문제**라고 한다. **같은 스택을 둘러싼 두 진술이 긴장 관계**다 — 크기 자체가 아니라 **일관성**이 기준이라고 읽으면 화해되지만, **어느 소스도 그렇게 말하지 않는다.** 표시만 한다.

## References

- [[tech-bridge-pstack-third-party-review]] · [[pstack]] · [[lauren-tan]]
- 관련: [[laziness-protocol]] · [[decision-quality]] · [[system-level-quality]] · [[code-is-the-product]] · [[verification-bottleneck]] · [[organic-architecture]] · [[speculative-generality]] · [[duplicate-code]] · [[large-class]]

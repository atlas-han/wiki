---
title: 일회용 가상 카드 번호 (One-Time Virtual Card)
type: concept
category: pattern
tags: [security, payments, privacy, agents, meta, muse]
aliases: [가상 카드, 일회용 카드 번호, virtual card number]
related: [least-privilege-connectors, credential-injection-outside-sandbox, confidential-vm, sentinel-agent, transaction-cut-monetization, action-reversibility]
first-seen: tech-bridge-zuckerberg-muse-in-daily-use
sources: [tech-bridge-zuckerberg-muse-in-daily-use]
created: 2026-09-17
updated: 2026-09-17
---

# 일회용 가상 카드 번호

**에이전트가 결제할 때마다 일회용 가상 카드 번호를 발급해, 실제 카드 번호가 판매자에게 닿지 않게 하는 층.** [[muse|Muse]] 보안 아키텍처에서 [[tech-bridge-zuckerberg-muse-in-daily-use]]로 처음 들어왔다.

> 제 신용카드는 안전한 결제 시스템에 저장되지만, **실제로 거래가 이뤄질 때 Muse는 일회용 가상 카드 번호로 결제합니다. 그래서 판매자는 제 진짜 번호를 절대 보지 못합니다.** — 진행자 (18:53~19:07)

> ⚠️ ko 자막이 *"제 실제 **전화번호**"* 로 옮겼다. **카드 번호다.**

⚠️ **앞 편에도 "일회용 카드 번호"라는 말은 나온다** — 다만 *"에이전트는 신용카드·비밀번호·**일회용 카드 번호**를 알아서는 안 된다"* 는 **자격증명 저장소 설명의 일부**였고, **판매자가 실제 번호를 보지 못한다는 메커니즘은 이 편이 처음**이다.

## 이 페이지의 핵심 논거 — 귀찮음이 보안을 막는다

가상 카드 자체는 새 기술이 아니다. 이 소스가 더하는 것은 **왜 그동안 안 쓰였는가**에 대한 답이다.

> **제가 직접 거래할 때는 "그냥 신용카드를 쓸까 아니면 이런 가상 카드를 하나 만들까" 생각하곤 합니다. 그런데 가상 카드를 만드는 건 추가 수고가 들죠. 그래서 대개는 그냥 평소 카드를 씁니다.** — [[mark-zuckerberg]] (19:23~19:35)

> **이게 이런 일을 대신 떠맡아 주는 에이전트를 갖는 것의 가치 중 하나입니다 — 에이전트는 그 추가 수고를 마다하지 않습니다.** (19:35~19:43)

**보안 기능의 채택을 막는 것이 기술이 아니라 마찰이고, 에이전트는 마찰을 느끼지 않는다.** 이 명제는 결제 밖으로도 일반화된다 — *사람이 귀찮아서 건너뛰는 안전 절차*가 에이전트에게는 비용이 아니다.

⚠️ 뒤집으면 같은 명제가 위험이기도 하다 — **에이전트는 위험한 절차도 마다하지 않는다.** 소스는 이 방향을 말하지 않는다.

## Muse 보안 스택에서의 자리

앞 편([[tech-bridge-zuckerberg-muse-personal-agent]])이 세운 네 겹에 **다섯째 겹**으로 붙는다.

| 층 | 막는 것 |
|---|---|
| [[confidential-vm]] | 운영자(Meta)가 내용을 보는 것 |
| [[sentinel-agent]] | 민감 데이터가 나가는 것 |
| [[least-privilege-connectors]] | 커넥터가 과한 권한을 갖는 것 |
| **자격증명 저장소** | 에이전트가 카드 번호·비밀번호를 **아는 것** |
| **일회용 가상 카드** | **판매자**가 실제 번호를 갖는 것 |

마지막 둘의 구분이 중요하다 — 저장소는 **에이전트를 향한** 최소 노출이고, 가상 카드는 **거래 상대를 향한** 최소 노출이다. 같은 원칙([[least-privilege-connectors|필요한 최소한만 노출]])이 **두 방향으로** 적용된다.

> **근본 아키텍처와 설계가 기본적으로 가능한 한 최소의 권한을 주고, 하려는 일을 완료하는 데 필요한 최소의 정보만 노출하는 것입니다.** (20:08~20:21)

## 되돌릴 수 있음과의 관계

[[action-reversibility]]는 *에이전트 행동을 되돌릴 수 있게 설계하라*고 말한다. 일회용 카드는 **되돌리는 장치가 아니라 피해를 가두는 장치**다 — 번호가 유출돼도 그 번호는 이미 죽어 있다. **사후 복구보다 사전 격리**에 가깝다.

## 미해결 사항

- **발급 주체** — Meta인가 카드사인가 결제 파트너인가. 앞 편이 말한 **Stripe**와의 관계가 이 편에 없다.
- **한도·유효기간**, 구독처럼 반복되는 결제는 어떻게 되는지.
- **환불·분쟁·차지백** — 일회용 번호로 산 것을 어떻게 돌려받는지.
- **판매자가 번호를 거부하는 경우**(가상 카드를 막는 가맹점이 있다).
- **결제 승인 UX** — *"처음 거래할 때는 허락을 받는다"* 이후 반복 거래의 규칙.
- **[[transaction-cut-monetization|커머스 수수료]]와 같은 결제 경로를 쓰는지** — 소스가 두 이야기를 연결하지 않는다.

## References

- [[tech-bridge-zuckerberg-muse-in-daily-use]] · [[muse]] · [[mark-zuckerberg]]
- 같은 스택: [[confidential-vm]] · [[sentinel-agent]] · [[least-privilege-connectors]]
- 관련: [[credential-injection-outside-sandbox]] · [[action-reversibility]] · [[transaction-cut-monetization]] · [[no-silent-write]]

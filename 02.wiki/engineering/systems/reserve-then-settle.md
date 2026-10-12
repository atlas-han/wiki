---
title: "Reserve-then-Settle — AI 사용의 사전 승인·사후 정산"
type: engineering
category: system
tags: [metering, entitlements, billing, ledger, concurrency, idempotency, credits, budgets, ai-pricing, agents]
aliases: [reserve before inference settle after, 사전 승인 사후 정산, hold and settle, check before consume, 추론 전 예약]
related: [agent-distributed-systems, software-marginal-cost, overspending-underusing-loop, bring-your-own-subscription, durable-execution]
first-seen: tech-bridge-stigg-ai-companies-building-banks
sources: [tech-bridge-stigg-ai-companies-building-banks]
created: 2026-10-12
updated: 2026-10-12
---

# Reserve-then-Settle

**AI 제품에서 사용 = 원가이므로, 권한·한도·잔액 검사를 청구서 뒤가 아니라 요청 경로(hot path)에서 동기로 먼저 하고 — 필요하면 금액을 예약(reserve/hold)하고 — 실제 사용량의 정산(settle)과 원장 갱신은 비동기로 뒤에 하는 구조.** [[dor-sasson|Dor Sasson]]([[stigg|Stigg]])이 [[tech-bridge-stigg-ai-companies-building-banks]]에서 은행·ATM에 빗대 세웠다.

> *"we actually need to enforce and and do this synchronously before we actually update the balances and reconcile and settle in in async way after after effects. So, hot bath[=hot path] actually get checked synchronously, and everything that comes after is basically reconciled after."* (06:48~07:06)
>
> *"When you draw the cash, it does the check if you're allowed to draw it doesn't happen after you get the cash. It happens before you draw the cash."* (07:10~07:21)

> ⚠️ **벤더의 프레이밍.** 화자는 이 계층을 파는 회사의 CEO다. 근거로 든 OpenAI financial engineering 팀의 2월 공개물(07:43~07:59)과 Anthropic 사례는 화자의 요약이고 이 위키는 원 자료를 확인하지 않았다. 아래 구성 요소는 **분산 시스템·결제 시스템의 기존 기법**이고 새로운 것은 *AI 사용량이 그 대상이 됐다* 는 주장이다.

## 왜 — "검사가 청구서 뒤에 온다"

지금 대부분의 구조: *"the check and the settlements are happening after after the inference, after the usage is being logged. And that's typically too late."*(06:09~06:18) 결과는 사는 쪽의 *"sticker shock"*(05:03~05:08) — [[overspending-underusing-loop]] — 과 파는 쪽의 마진 문제(06:27~06:35), 그리고 채널을 구분하지 못해 **기능을 통째로 끄는** 대응(화자의 Anthropic × OpenClaw 해석, 03:08~03:25).

## 구성 요소 (화자가 든 것)

| 요소 | 내용 (en-orig) | 기존 기법과의 대응 |
|---|---|---|
| **동기 결정 폭포** | *"a decision waterfall that needs to consider in runtime what is the client, the user, the agent is allowed to do"*(08:06~08:14) — 기능 접근 · 플랜의 rate limit · trial·프로모션 여부(08:21~08:33). *"a single synchronous evaluation"*, *"the priority is deterministic"*(08:56~09:08) | entitlement / policy evaluation |
| **reserve → settle** | *"reserve before inference and settle actuals after"*(14:36~14:42) | 카드 결제의 승인(authorization hold) → 매입(capture) |
| **에이전트 중간 검사** | 에이전트 작업의 비용을 미리 모르므로 *"check those balances as the agent continues to get work"*, *"reserve an account for them in advance, and then asynchronously after effect reconcile"*(15:42~15:53) | 점진적 승인(incremental authorization) |
| **동시성** | *"like 10,000 agents trying to reach out to the same dollar pool"*(10:31~10:35) | double spend 방지 — 잔액 예약·잠금 |
| **멱등성·감사** | *"Think about item potency[=idempotency] and auditability of those um requests"*(11:25~11:32) | 멱등성 키, 원장 → [[agent-distributed-systems]] |
| **크레딧 출처별 차감 순서** | 1,700 크레딧이 다 같지 않다 — 먼저 받은 것? 프로모션? *"single integer"* 잔액으로는 안 된다(12:04~12:37) | 다중 잔액 버킷, 소진 우선순위 |
| **계층적 풀·예산·지출 한도** | *"credit pools are no longer flat"* — *"allocations, budgets, spend caps"*(13:05~13:18), 팀·사용자·에이전트별 사용 내역(13:39~13:46) | 계층적 쿼터 |
| **VPC 내부 원장·계량** | *"deploying this this architecture, this ledger, this metering within their VPC"*(15:17~15:23) — 지연·비용·데이터 주권 | 배포 위치 선택 |

⚠️ 화자는 동시성 문제를 *"a classic double double spend problem. It comes from the accounting world. It's a double entry bookkeeping"*(10:55~11:01)로 잇는다 — **double spend(동시 인출 방지)와 double-entry bookkeeping(복식부기 원장)은 다른 개념**이다. 둘 다 필요할 수 있지만 같은 해법이 아니다.

## 함의 — 가격 변경이 인프라 변경이 된다

*"they didn't change the pricing. All they did was change the pace in which tokens get burned (…) So that effectively was a pricing change."*(17:22~17:36) → *"it's not just financial changes, it's an infrastructure change."*(17:38~17:42) — 단가표가 아니라 **소비율**을 바꾸는 가격 정책은 런타임 계층 없이는 실행할 수 없다는 주장(⚠️ OpenAI 4월 변경에 대한 화자의 해석).

## 이 위키에서의 좌표

- [[agent-distributed-systems]] — 같은 도구(멱등성·상태 불명·보상)를 **돈을 쓰는 부작용**에 적용한 판.
- [[software-marginal-cost]] — 한계비용이 생긴 소프트웨어에서 *누가 비용을 대는가* 를 **요청마다 런타임에 결정**하는 계층.
- [[bring-your-own-subscription]] — 구독 토큰을 제3자 앱에 들고 가려면 *어느 채널이 어느 구독을 얼마나 쓰는지* 를 구분하는 이 계층이 전제된다(위키의 독해).
- [[overspending-underusing-loop]] — 사는 쪽 증상. 이 구조는 그 원인을 *검사 시점* 에서 찾는다.
- [[durable-execution]] — 장시간 에이전트의 중간 잔액 검사·예약은 실행 모델의 체크포인트와 겹칠 수 있다(⚠️ 소스는 연결하지 않는다).

## ⚠️ 유보

- 지연 비용 — hot path의 동기 검사가 추론 지연에 얼마를 더하는지, 실패 시 열림(fail-open)/닫힘(fail-closed) 정책 — 소스에 없다.
- 예약 금액을 어떻게 정하는가(에이전트 비용을 *"you don't know in advance"* 라면서) — 소스에 없다.

## References

- [[tech-bridge-stigg-ai-companies-building-banks]] — first-seen
- [[stigg]] · [[dor-sasson]]
- 관련: [[agent-distributed-systems]] · [[software-marginal-cost]] · [[overspending-underusing-loop]] · [[bring-your-own-subscription]]

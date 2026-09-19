---
title: 첫 음성까지의 시간 (Time to First Audio, TTFA)
type: concept
category: metric
tags: [voice-agents, latency, ux, metric, abandonment]
aliases: [TTFA, 첫 음성 응답 시간]
related: [voice-agent-pipeline, voice-latency-thinking-tradeoff, token-fertility, model-mixing-economics]
first-seen: tech-bridge-voice-agent-failure-modes
sources: [tech-bridge-voice-agent-failure-modes]
created: 2026-09-19
updated: 2026-09-19
---

# 첫 음성까지의 시간 (TTFA)

**사용자가 말을 멈춘 순간부터 에이전트가 말을 시작할 때까지의 시간.** 보이스 에이전트의 기본 지표이고, [[tech-bridge-voice-agent-failure-modes]]가 이 위키에 들여왔다.

> 보통 대부분의 사람들은 **첫 음성 재생 시간**, 즉 **사용자가 [에이전트]에게 말을 멈추고 [에이전트]가 말을 시작하는 시간**으로 이를 측정합니다. (05:00~05:18)

## 티어

| 구간 | 체감 | 소스의 표현 |
|---|---|---|
| **< 550ms** | 자연스러움 | *"대부분의 사람들이 원하는 값 — 플랫폼들이 그렇게 광고하기 때문"* |
| **750 ~ 1,200ms** | 눈에 띔·거슬림 | **"대부분이 결국 도착하는 곳"** |
| **> 1,200ms** | — | **"사용자들이 전화를 끊기 시작한다"** |

> 대부분의 사람들은 **550[ms] 미만**을 원합니다. **왜냐하면 플랫폼이나 솔루션, 또는 여러 계층에서 그렇게 광고하기 때문이죠.** 하지만 제 생각에는 **대부분 750에서 1.2 사이의 값으로 귀결**될 것 같습니다. **성능이 정말 형편없는 제품들은 결국 1.2를 넘게 되고, 그러면 사용자들이 전화를 끊기 시작하는 현상이 나타나기 시작합니다.** (05:36~05:58)

**두 개의 숫자가 갈라진다** — *광고되는 값* 과 *도달하는 값*. 그 격차(550 → 750~1200)가 이 발표 전체의 출발점이다.

## 왜 이 지표가 이 위키에서 새로운가

이 위키에서 지연은 지금까지 **비용의 대리 변수**([[model-mixing-economics]])이거나 **배치 작업의 대기 시간**이었다. 둘 다 *느리면 더 기다리거나 더 낸다* 는 성격이다.

TTFA는 다르다. **넘으면 사용자가 사라진다** — 되돌릴 수 없는 이탈이고, 그래서 **하드 제약**이 된다. 그 제약이 위로 올라가 모델 선택까지 되민다:

- **thinking을 못 쓴다** → [[voice-latency-thinking-tradeoff]]
- **토크나이저가 예산의 일부가 된다** → [[token-fertility]]
- **꼬리 지연(P90·P95)이 평균보다 중요해진다** — 프런티어 모델의 P50은 450~500ms지만 P90·P95가 1.2~1.3초로 튄다. **평균은 통과하고 꼬리가 사용자를 잃는다.**

마지막 항목이 중요하다. 이 위키의 다른 성능 논의는 대부분 평균이나 총량으로 이야기하는데, **여기서는 분포의 꼬리가 제품을 정한다.**

## ⚠️ 유보

- **세 티어의 출처가 없다.** *"광고된다"* 는 말만 있고 누가 광고하는지, 550이라는 숫자가 어디서 왔는지 없다.
- **이탈률 데이터가 없다.** *"끊기 시작한다"* 뿐 — 1.2초에서 몇 %가 끊는지, 통화 종류(인바운드/아웃바운드·고객센터/예약)에 따라 다른지 없다.
- **각 층의 지연 배분**이 *"슬라이드에 있다"* 고만 하고 자막에 숫자가 없다.
- **TTFA와 TTFT의 관계**가 정리되지 않는다 — 07:59의 *"P50 TTF[T] 450~500"* 은 LLM 층의 값이고 TTFA는 파이프라인 전체의 값인데, 둘을 잇는 계산이 제시되지 않는다.
- **무음 대응**(filler·백채널링)이 티어를 바꾸는지 — barge-in 절이 통째로 생략돼 다루지 않는다.

## References

- [[tech-bridge-voice-agent-failure-modes]] — first-seen
- [[venky-b]] · [[plivo]]
- 관련: [[voice-agent-pipeline]] · [[voice-latency-thinking-tradeoff]] · [[token-fertility]] · [[model-mixing-economics]] · [[groq]] · [[cerebras]]

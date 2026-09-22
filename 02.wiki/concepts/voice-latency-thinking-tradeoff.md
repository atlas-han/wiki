---
title: 지연 제약이 thinking을 금지한다 (Voice Latency vs Thinking)
type: concept
category: framing
tags: [voice-agents, latency, reasoning, test-time-compute, model-selection, constraint]
aliases: [음성 에이전트의 아이러니, thinking을 끄는 제약]
related: [time-to-first-audio, voice-agent-pipeline, model-mixing-economics, fixed-budget-alpha, true-cost-to-perfect-answer]
first-seen: tech-bridge-voice-agent-failure-modes
sources: [tech-bridge-voice-agent-failure-modes, tech-bridge-exa-perfect-search-for-agents]
created: 2026-09-19
updated: 2026-09-22
---

# 지연 제약이 thinking을 금지한다

**지난 1년 LLM 발전의 대부분이 thinking·강화학습에서 왔는데, 실시간 음성 에이전트는 바로 그 thinking을 꺼야 한다.** [[tech-bridge-voice-agent-failure-modes]]에서 [[venky-b|Venky B]]가 *"아이러니"* 라고 부른 관찰이다. **이 소스에서 가장 값진 한 문장**이고, 이 위키가 암묵적으로 깔고 있던 전제를 깬다.

> **음성 [에이전트]의 아이러니는 거의 항상 음성 [대화]를 담당하는 LLM이나 [에이전트]가 사고(thinking) 기능을 꺼야 한다는 점이죠. 그러니까 지난 1년 동안 LLM [계층]에서 이루어진 모든 발전은 이제 여기에는 전혀 적용되지 않는다는 거죠?** (06:53~07:11)

> 물론 여러분은 **더 나은 지시 이행이나 도구 호출**을 할 수 있는 더 나은 모델들을 가지고 있지만, **충분히 빠른 속도를 원한다면 사고 계층에 내장된 거의 모든 지능 기능은 기본적으로 꺼져 있는 상태**입니다. (07:11~07:29)

## 무엇이 깨지는가

이 위키의 여러 페이지가 **테스트 타임 컴퓨트를 어떻게 잘 쓸 것인가**를 다뤄 왔다:

| 페이지 | 전제 |
|---|---|
| [[fixed-budget-alpha]] | 예산을 고정하고 **역할을 나누면** 알파가 남는다 |
| [[true-cost-to-perfect-answer]] | 합격률로 나눈 **진짜 비용**으로 재라 |
| [[token-roles]] | 토큰은 대체 가능하지 않다 — **역할을 주라** |
| [[generator-evaluator-pattern]] | 채점자를 붙여 **반복하라** |

**넷 다 "더 쓸 수 있다"를 전제한다.** 이 도메인은 그 레버 자체를 금지한다 — 반복도 조언자도 채점자도 **한 턴 안에 1.2초를 넘기면 쓸 수 없다.**

그래서 남는 개선 축이 좁아진다:

| 여전히 쓸 수 있는 것 | 못 쓰는 것 |
|---|---|
| 더 나은 **지시 이행** | **thinking / 추론 예산** |
| 더 나은 **도구 호출 성공률** | 다회 반복·자기 교정 루프 |
| **구조**(타입 지정 필드 · 필드 단위 평가) | 실행 중 **채점자·조언자 붙이기** |
| 더 빠른 **토크나이저**([[token-fertility]]) | — |

**그리고 이 소스의 처방 전체가 그 남은 축 위에 있다.** 다섯 실패 모드 중 넷이 LLM 바깥(전사·필드·평가·정규화)인 이유가 여기 있다 — 모델을 더 생각하게 만들 수 없으니 **주변을 고친다.**

## 일반화 — 제약이 기법을 고른다

이 위키가 지금까지 모은 에이전트 기법들은 대체로 **긴 호흡의 작업**(코딩·리서치·마이그레이션)에서 나왔다. 그 도메인에서는 시간이 비용일 뿐이다. 실시간 상호작용이 들어오면 **같은 기법 목록에서 절반이 탈락한다.**

→ 기법을 옮길 때 물어야 할 것: **이 기법은 몇 초를 쓰는가, 그리고 그 도메인은 몇 초를 허용하는가.**

## ⚠️ 유보

- **"거의 항상"의 예외**가 무엇인지 없다 — 어떤 통화·어떤 턴에서는 thinking을 켤 수 있는지(예: 사용자에게 *"잠시만요"* 라고 말한 뒤).
- **비동기 thinking**(말하면서 뒤에서 생각하기, 다음 턴을 미리 계산하기)이 다뤄지지 않는다.
- **speech-to-speech 모델**이 이 트레이드오프를 바꾸는지 — 소스가 그 대비를 끝내 정리하지 않는다.
- *"지난 1년의 발전 대부분이 thinking에서 왔다"* 는 **화자의 요약**이고 근거가 없다.
- 이 제약이 **다른 실시간 도메인**(음성 이외의 인터랙티브 UI)에도 같은 정도로 걸리는지 소스의 범위 밖이다.


## 공급자 쪽에서 온 짝 (2026-09-22 추가)

이 페이지는 **실시간 제약이 thinking을 금지하므로 모델 바깥을 고칠 수밖에 없다**고 말하고, 이 위키는 그때 질문 하나를 세웠다 — ***이 기법은 몇 초를 쓰는가, 그 도메인은 몇 초를 허용하는가.***

**그 "모델 바깥"의 부품 하나가 자기 수치를 들고 들어왔다.**

> **200밀리초 검색 엔드포인트**입니다. (…) **인간에게는 너무 빠르죠. 하지만 우리는 인간을 위해 봉사하는 것이 아닙니다.** (…) [음성 에이전트]가 내부적으로 검색을 수행해야 하는 경우 **매 밀리초가 중요합니다.** — [[will-bryk]], [[tech-bridge-exa-perfect-search-for-agents]] (11:08~11:27)

→ **[[search-latency-tiers]]**

**[[venky-b|Venky B]]가 제약을 말했다면 [[will-bryk|Bryk]]은 그 제약 아래 팔리는 부품을 말한다.** ⚠️ **다만 벤더 자기 보고이고 퍼센타일·코퍼스·설정이 없다.** 그리고 ⚠️ **음성 에이전트의 전체 지연 예산에서 검색이 차지하는 몫은 두 소스 어느 쪽에도 없다** — 09-19에 세운 질문은 **아직 답을 받지 못했다.**

## References

- [[tech-bridge-voice-agent-failure-modes]] — first-seen · [[tech-bridge-exa-perfect-search-for-agents]]
- [[venky-b]] · [[plivo]]
- 관련: [[time-to-first-audio]] · [[voice-agent-pipeline]] · [[token-fertility]] · [[model-mixing-economics]] · [[fixed-budget-alpha]] · [[true-cost-to-perfect-answer]] · [[token-roles]] · [[generator-evaluator-pattern]]

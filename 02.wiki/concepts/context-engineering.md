---
title: Context Engineering
type: concept
category: technique
tags: [llm, context-window, agent, prompting]
related: [context-resets-and-compaction, context-anxiety, agent-harness-design, harness-engineering, agi-definition, agent-org-adoption]
first-seen: anthropic-managed-agents
sources: [anthropic-managed-agents, anthropic-harness-design-long-running-apps, tech-bridge-harness-engineering, tech-bridge-multimodal-commerce-agent, tech-bridge-jensen-huang-g20-agi, tech-bridge-altman-g20-economic-boom]
created: 2026-05-25
updated: 2026-09-07
---

# Context Engineering

LLM의 context window에 무엇을 넣고, 어떤 순서로 배치하고, 언제 다시 fetch하고, 어떻게 transform할지에 대한 설계 영역. [[anthropic|Anthropic]]은 별도 글 [Effective context engineering for AI agents](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents)를 보유. 본 위키에서는 [[anthropic-managed-agents]]와 [[anthropic-harness-design-long-running-apps]] 안에서 언급.

## 주요 기법 (Anthropic 글 인용)

- **Compaction** — 진행 중 context를 요약해 길이를 줄임 ([[context-resets-and-compaction]])
- **Context trimming** — 오래된 tool 결과·thinking block 등을 선택적으로 제거
- **Memory tool** — context를 파일에 써서 세션 간 학습
- **Context reset** — 깨끗한 새 agent로 handoff
- **Session as external context object** — context를 window *밖*에 두고 슬라이스로 가져옴 ([[anthropic-managed-agents]] 패턴)

> It is difficult to know which tokens the future turns will need. ... Prior work has explored ways to address this by storing context as an object that lives *outside* the context window.

## Prompt cache 친화적 조직

Managed Agents 모델에서 fetched event를 transform하는 한 가지 목적은 **prompt cache hit율**을 최대화하는 context 배치. [[transcript-classifier]]의 stage 1→stage 2 디자인도 동일 원리 — stage 2는 stage 1과 거의 동일 prompt로 cache hit.

## Generator-Evaluator 관점

[[anthropic-harness-design-long-running-apps]]에서 sprint construct가 사라진 후, **자동 compaction**이 [[claude-agent-sdk|Agent SDK]] 차원에서 context growth를 처리하는 것으로 충분해짐. → context engineering의 *어디까지를 harness가 담당하고 어디부터 SDK·플랫폼이 담당하는가*가 빠르게 이동 중.

## Harness engineering으로의 진화 (2026 프레이밍)

[[tech-bridge-harness-engineering]] 영상은 context engineering을 *"2025년의 화두"* 로 두고, 2026년의 [[harness-engineering|harness engineering]]을 그 **직접적 진화**로 제시한다. 단일 세션 수준에서는 둘이 거의 같은 질문(올바른 컨텍스트 생태계)을 공유하지만, harness engineering이 더하는 것은 **control**(루프·다중 세션 오케스트레이션·sub-agent)과 **mindset 리프레임**(*every mistake becomes a rule*). 즉 *어디까지가 context engineering이고 어디부터가 harness engineering인가*의 경계는, 위 [Generator-Evaluator 관점](#generator-evaluator-관점)에서 본 *harness ↔ SDK/플랫폼* 경계 이동과 마찬가지로 빠르게 움직이는 중.

## 컨텍스트를 신뢰 등급별 슬롯으로 나누기 (2026-09-04)

[[tech-bridge-multimodal-commerce-agent]]의 **working state**는 컨텍스트를 통짜 텍스트가 아니라 **필드별로 나눈 상태**로 다룬다 ([[fuzzy-intent-discovery]]).

| 슬롯 | 성격 | 갱신 |
|---|---|---|
| **hard constraint** | 쿼리에서 그대로 뽑힌 확정 조건 | 고정 |
| **soft constraint** + **confidence score** | 이미지 등에서 추론한 선호 | 대화 중 계속 갱신 |
| **real-time variable** | 재고 등 | **믿지 않고 매번 재조회** |

두 가지가 이 위키에 새롭다. 첫째, **추론된 항목에 자기 확신도가 함께 저장된다** — 그래서 "신뢰도를 올리는 것"이 에이전트의 행동 목표가 될 수 있다. 둘째, **믿으면 안 되는 필드가 명시적으로 구분된다** — *"오래된 정보라면 아무 의미가 없기 때문"*.

[[agent-distributed-systems]]가 *"에이전트 메모리는 무효화 가능한 캐시"* 라고 한 것과 같은 문제를 **상태 스키마 층위**에서 다룬 형태다. 컨텍스트를 "무엇을 넣을까"가 아니라 **"각 항목을 얼마나 믿을까"** 로 묻는다.

## 조직 규모의 맥락 — 온보딩 비유 (2026-09-06 · [[tech-bridge-jensen-huang-g20-agi]])

이 페이지는 지금까지 **한 세션의 context window**를 다뤘다. [[jensen-huang|Jensen Huang]]은 같은 문제를 **회사 규모**에서 말한다.

> 이러한 아이들이 우리 회사에 들어오게 될 때, 우리는 **여전히 그들에게 적절한 맥락(context)을 제공하는 데 상당한 투자**를 해야 합니다. (…) 당신은 MIT 박사 학위를 가진 신입 졸업생을 온보딩하는 데 쏟는 에너지처럼, 그들에게 **맥락, 목적, 관련성, 접근성** 등 모든 것을 제공하는 데 모든 에너지를 쏟을 것입니다.

넷 중 둘(맥락·접근성)은 이 페이지의 어휘로 곧장 번역된다 — *무엇을 넣을 것인가*와 *어디에 접근할 수 있는가*([[model-context-protocol]]·[[brain-hands-decoupling]]의 자격 증명 주입). 나머지 둘(**목적·관련성**)은 이 위키에서 [[intent-md]]·[[agent-skills]]·[[agent-org-adoption]]이 다루는 층이다. Huang의 주장은 이 넷이 **AGI 이후에도 남는 일**이라는 것이고, 그래서 이 페이지의 *"harness ↔ SDK/플랫폼 경계가 이동한다"* 는 관찰에 한 단서가 붙는다 — 세션 층의 맥락 관리는 플랫폼으로 내려가도, **조직 층의 맥락 제공**은 내려갈 곳이 없다.

⚠️ 인프라 판매자의 발언이며, "남는다"는 주장의 근거는 온보딩 비유 하나다.

## 공급 경계 — 맥락은 판매자가 줄 수 없다 (2026-09-07 · [[tech-bridge-altman-g20-economic-boom]])

이 페이지는 맥락을 **세션 안의 문제**로 다뤘고, [[jensen-huang]]이 그것을 **조직의 온보딩 문제**로 키웠다. G20에서 [[sam-altman]]이 세 번째 위치를 놓는다 — **모델 제공자가 할 수 없는 일**이라는 선언이다.

> **세계에서 가장 똑똑한 사람들이 우리 동네로 이사 와서 저를 위해 일하겠다고 해도, 서로 모른다면** — 세상에서 가장 똑똑한 사람들이 모여 저녁 식사를 하는데 제대로 대화를 나눌 수 없다면 그다지 즐거운 저녁 식사가 아니잖아요. **그렇다면 우리는 맥락에 대해 어떻게 생각해야 할까요?**

> 그건 **우리 쪽에서 나올 일도 아니고, 나와서도 안 된다**고 생각합니다. **저희는 이 엔진을 제공할 것입니다.** (…) 설령 그렇다 하더라도 **우리가 잘 해낼 거라고는 생각하지 않지만** (…)

세 소스가 같은 층을 세 위치에서 가리킨다:

| 층위 | 소스 | 맥락은 누구의 일인가 |
|---|---|---|
| 세션 | 이 페이지의 기존 논의 | 하네스 설계자 |
| 조직 | [[tech-bridge-jensen-huang-g20-agi]] | *"기업이 하는 일이고, 리더가 하는 일"* |
| **공급 경계** | [[tech-bridge-altman-g20-economic-boom]] | **고객 쪽 — 판매자는 못 한다** |

[[agent-org-adoption]]·[[agent-skills]]가 다뤄온 *"조직 지식을 에이전트에 넣는 일"* 이 왜 고객에게 남는지에 대한 **공급자 본인의 답**이다.

⚠️ 이 선 긋기는 책임의 배분이기도 하다 — 결과가 나쁠 때 맥락 부족은 고객의 몫이 된다. 소스는 그 함의를 다루지 않는다.

## References

- [[anthropic-managed-agents]]
- [[anthropic-harness-design-long-running-apps]]
- [[tech-bridge-harness-engineering]]
- [Effective context engineering for AI agents](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents)
- [[tech-bridge-jensen-huang-g20-agi]] — 온보딩 비유 (Jensen Huang, 2026-09-06)

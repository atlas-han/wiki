---
title: Long-Context for Agents
type: concept
category: architecture
tags: [long-context, agent, tool-calls, context-window, minimax]
aliases: [긴 컨텍스트, 100만 토큰 컨텍스트]
related: [context-engineering, context-resets-and-compaction, sparse-attention, agent-distributed-systems, attention-mechanism]
first-seen: tech-bridge-minimax-m3-long-context
sources: [tech-bridge-minimax-m3-long-context]
created: 2026-09-08
updated: 2026-09-08
---

# Long-Context for Agents

컨텍스트 길이를 **요약 편의**가 아니라 **에이전트 실행의 요구사항**으로 보는 관점. [[tech-bridge-minimax-m3-long-context]]에서 [[olive-song]]이 [[minimax-m3|MiniMax M3]]의 100만 토큰을 설명하며 제시한다.

## 논증 — 자기 회사의 이전 모델이 반례다

이 관점의 힘은 **더 긴 컨텍스트를 이미 갖고 있었다는 사실**에서 나온다.

> 긴 컨텍스트에 대한 이야기는 **MiniMax M1과 MiniMax-01까지 거슬러 올라갑니다.** 당시 모델은 실제로 **1천만 개의 토큰 컨텍스트**를 처리할 수 있었습니다. (…) 하지만 **그때는 에이전트 모델이 아니었죠.** 예를 들어 **책을 입력하면 리뷰를 제공하는** 등의 기능을 수행했습니다.

> 이제 **에이전트가 전체 환경과 상호 작용하고 모든 도구 응답을 받고 여러 라운드를 거치는 상황**에서는 **짧은 컨텍스트로는 복잡한 작업을 수행하기에 충분하지 않습니다.**

**1천만 > 100만인데 뒤엣것이 진보로 제시된다.** 축이 *얼마나 넣을 수 있나*에서 **그 길이가 무엇으로 채워지나**로 옮겨갔기 때문이다.

| | 비-에이전트 긴 컨텍스트 (M1·MiniMax-01) | 에이전트 긴 컨텍스트 (M3) |
|---|---|---|
| 무엇이 들어오나 | **사람이 한 번에 넣는 것** (책 한 권) | **실행이 만들어내는 것** — 도구 응답·환경 관측 |
| 언제 들어오나 | 앞에서 한 번 | **라운드마다 누적** |
| 길이 | 1천만 | 100만 |

⚠️ **왜 줄었는지는 소스에 없다.** 게스트의 논지는 *"그때는 에이전트가 아니었다"* 뿐이고, 에이전트화하면서 길이가 10분의 1이 된 이유(연산량·품질·MSA의 제약 중 무엇인지)를 설명하지 않는다.

## 이 위키의 반대편 처방과 나란히

같은 압력에 대해 이 위키는 지금까지 **줄이는** 답을 모아 왔다.

| 방향 | 답 | 출처 |
|---|---|---|
| **줄인다** | compaction · trimming · context reset · 외부 객체화 | [[context-engineering]] · [[context-resets-and-compaction]] · [[anthropic-managed-agents]] |
| **믿을 것만 믿는다** | 신뢰 등급 슬롯(hard/soft/real-time) | [[context-engineering]] (2026-09-04) |
| **캐시로 본다** | 메모리는 무효화 가능한 캐시 | [[agent-distributed-systems]] |
| **늘린다** | 100만 토큰 + [[sparse-attention\|MSA]] | **이 페이지** |

넷이 **같은 관찰**에서 갈라져 나온다 — *에이전트의 컨텍스트 소비는 사람의 것과 종류가 다르다*. [[context-engineering]]이 *"어디까지를 하니스가 담당하고 어디부터 SDK·플랫폼이 담당하는가"* 가 이동 중이라고 적었는데, 이 소스는 **그 경계 아래에 모델 자체**를 하나 더 놓는다. 컨텍스트가 충분히 길면 하니스의 compaction 층이 얇아진다 — [[harness-pruning]]이 *"모델이 좋아지면 하네스를 지운다"* 고 한 것의 컨텍스트 축 사례가 된다.

⚠️ **이 대비는 위키가 놓는 것이다.** 소스는 compaction 계열을 **언급조차 하지 않는다.**

## 무엇이 길이를 요구하는가 (소스가 든 것)

- **도구 응답(tool feedback)** 의 누적
- **다중 라운드** 상호작용
- **환경 전체**와의 상호작용
- 멀티모달 입력 — *"아주 긴 영상을 이해"*, PowerPoint, 비정형 보고서 ([[native-multimodal-pretraining]])

마지막 항목이 길이 요구를 **곱한다**는 점을 소스가 직접 잇지는 않지만, 같은 대담 안에 두 주장이 함께 있다.

## 미해결 사항

- **1천만 → 100만**의 이유.
- **길이가 늘면 정말 compaction이 필요 없어지는가** — 소스가 다루지 않는다. 비용 축(긴 컨텍스트는 싸지 않다)도 없다.
- *"functional한 100만"* 의 기준 — 무엇을 통과해야 실효 길이로 치는지 벤치마크가 제시되지 않는다.

## References

- [[tech-bridge-minimax-m3-long-context]] · [[minimax-m3]] · [[olive-song]]
- 관련: [[sparse-attention]] · [[context-engineering]] · [[context-resets-and-compaction]] · [[harness-pruning]] · [[agent-distributed-systems]] · [[native-multimodal-pretraining]]

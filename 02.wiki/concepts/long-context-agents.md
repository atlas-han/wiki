---
title: Long-Context for Agents
type: concept
category: architecture
tags: [long-context, agent, tool-calls, context-window, minimax]
aliases: [긴 컨텍스트, 100만 토큰 컨텍스트]
related: [context-engineering, context-resets-and-compaction, sparse-attention, agent-distributed-systems, attention-mechanism, context-rot]
first-seen: tech-bridge-minimax-m3-long-context
sources: [tech-bridge-minimax-m3-long-context, tech-bridge-bm25-agentic-search, tech-bridge-knowledge-agents-not-coding-agents, tech-bridge-oracle-agent-memory-harness]
created: 2026-09-08
updated: 2026-09-24
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

## ⭐ 2026-09-20 — 정면으로 만나는 두 반론

같은 날 같은 무대의 두 발표가 **"컨텍스트를 늘리면 해결된다"를 각자 다른 근거로 부정한다.**

| | [[jo-bergum\|Bergum]] ([[tech-bridge-bm25-agentic-search]]) | [[benjamin-clavie\|Clavié]] ([[tech-bridge-knowledge-agents-not-coding-agents]]) |
|---|---|---|
| 한계의 근거 | **품질 저하** — *"품질 저하가 시작되기 전까지 약 35만 개의 토큰"*(06:19) | **비용 + 절대 규모** — *"1억 토큰 컨텍스트가 나와도 (a) 돈이 아주 많이 들고 (b) 한 개 주 법전의 절반도 못 담는다"*(16:47~17:03) |
| 비유 | **플로피 디스크 한 장** | **한 개 주의 법전** |
| 결론 | 검색이 필요하다 | **오케스트레이션이 필요하다** → [[orchestrator-searcher-split]] |

→ [[context-window-as-floppy-disk]]

**모순은 아니고 축이 다르다.** 이 페이지가 묻는 것은 *루프를 돌리려면 얼마나 들어가야 하나*이고 채우는 것은 **실행이 만들어낸 것**(도구 응답)이다. 저쪽이 묻는 것은 *들어갈 수 있는 것보다 코퍼스가 크면 어떻게 하나*이고 채우는 것은 **밖에서 가져온 것**(문서)이다.

> ⚠️ **세 소스 다 자기 주장에 유리한 쪽 수치만 든다.** 이 페이지가 이미 적었듯 [[minimax|MiniMax]]는 *왜 1천만에서 100만으로 줄었는지* 말하지 않았고, [[jo-bergum|Bergum]]의 *35만 토큰* 은 화자가 **스스로 *"제 의견으로는"* 이라고 명시**한 값이며, [[benjamin-clavie|Clavié]]의 *1억 토큰* 은 가상의 숫자다. **이 위키는 어느 쪽 숫자도 채택하지 않는다.**

## References

- [[tech-bridge-minimax-m3-long-context]] · [[minimax-m3]] · [[olive-song]]
- 관련: [[sparse-attention]] · [[context-engineering]] · [[context-resets-and-compaction]] · [[harness-pruning]] · [[agent-distributed-systems]] · [[native-multimodal-pretraining]]

## 2026-09-24 — 세 번째 반론: context rot

[[tech-bridge-oracle-agent-memory-harness]]([[ignacio-martinez|Ignacio Martinez]] / [[oracle|Oracle]])가 **창 확장론을 이름으로 반박**한다 — *"'1500만 컨텍스트 윈도우'를 믿는 사람들"*(25:09~25:19)에게 창은 **단기 기억의 한 유형**일 뿐이고, 많이 넣을수록 항목당 주의가 희석되며([[context-rot]]), 어텐션 행렬은 n²로 커진다(26:35~26:57). 처방은 **창을 가능한 한 작게**(27:00~27:03) + 장기 기억은 외부 저장소로.

⚠️ **측정은 없다** — 이 페이지의 MiniMax 쪽과 마찬가지로. 그리고 **제곱 비용 논거는 [[sparse-attention]]이 정확히 겨냥하는 것**이라, 두 논거 중 *주의 희석*만이 이 페이지의 처방에 대한 실질적 반론으로 남는다. → [[context-rot]]의 ⚠️ Contradiction.

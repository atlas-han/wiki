---
title: 컨텍스트 창은 플로피 디스크다 (Context Window as Floppy Disk)
type: concept
category: framing
tags: [context-window, retrieval, limits, agi, long-context]
aliases: [플로피 디스크 비유, floppy disk analogy]
related: [long-context-agents, context-engineering, retrieval-not-reasoning-bottleneck, agentic-search, context-resets-and-compaction, orchestrator-searcher-split]
first-seen: tech-bridge-bm25-agentic-search
sources: [tech-bridge-bm25-agentic-search, tech-bridge-knowledge-agents-not-coding-agents]
created: 2026-09-21
updated: 2026-09-21
---

# 컨텍스트 창은 플로피 디스크다

**컨텍스트 창을 "크다/작다"가 아니라 *고정된 한 장*으로 보는 프레이밍.** 한 장에 무엇을 담을지 골라야 하고, **모델이 아무리 좋아져도 그 고르는 일은 사라지지 않는다.**

> 제가 80년대에 살았던 구세대라서 그런지, **컨텍스트 창을 플로피 디스크에 비유**하는 걸 좋아해요. (…) **플로피 디스크 하나에는 약 1.4 메가바이트의 데이터**를 저장할 수 있었습니다. 그리고 **현재 모델들은 품질 저하가 시작되기 전까지 약 35만 개의 토큰 정도를 감당할 수 있을 거라고 [제 의견으로는] 생각합니다. 그러니까, 데이터가 담긴 플로피 디스크 하나 분량입니다.** — [[jo-bergum]], [[tech-bridge-bm25-agentic-search]] (05:56~06:22)

> ⚠️ **35만 토큰은 측정이 아니다.** 화자가 *"in my opinion"* 이라고 명시한다. **출처·방법·모델이 없다.** 이 위키는 **비유를 받고 숫자는 받지 않는다.**

## ⭐ 가장 멀리 가는 주장 — 검색이 AGI보다 오래 산다

> 인공 일반 지능(AGI)과 같은 **완벽한 모델을 얻더라도**, [실수를 전혀 하지 않는 모델을 얻더라도] **여전히 사용 가능한 컨텍스트 창의 크기가 플로피 디스크 크기 정도로 제한될 겁니다. 따라서 해당 컨텍스트 창에 무엇이 들어갈지 결정해야 합니다.** (07:36~07:53)

**이 위키에서 "모델이 좋아지면 사라진다"가 아니라 "모델이 좋아져도 남는다"로 분류된 몇 안 되는 문제다.**

이 위키의 기본 서사는 [[harness-pruning]]이 대표한다 — **하니스의 부품은 모델이 좋아지면 dead weight가 된다.** [[agent-harness-design]]의 *"harnesses encode assumptions about what the model can't do — those assumptions go stale"* 가 그 문장이다. 그런데 **이 주장은 검색을 그 범주에서 빼낸다**: 검색은 *모델이 못 하는 것에 대한 가정*이 아니라 **용량이라는 물리적 제약에 대한 대응**이기 때문이다.

⚠️ **화자 자신이 단서를 단다** — *"인공 일반 지능(AGI)이 등장하면 그들은 그냥 브라우저를 사용할 수도 있겠죠. 두고 보면 알 겁니다"*(14:24~14:28). **본인도 확정하지 않는다.**

## 같은 날 두 번 독립적으로 나온 논증

[[benjamin-clavie|Clavié]]가 같은 무대에서 같은 구조의 말을 한다 — **비유는 다르고 결론은 같다.**

> **설령 1억 토큰 컨텍스트를 가진 모델이 나온다 해도, (a) 그건 돈이 아주 많이 들 것이고, (b) 그건 여전히 아무것도 아닙니다. 한 개 주(state)의 법전의 절반도 못 담습니다. 미국 전체는 고사하고, 국제법이나 전문 분야 판례는 말할 것도 없습니다.** — [[tech-bridge-knowledge-agents-not-coding-agents]] (16:47~17:03)

| | [[jo-bergum\|Bergum]] | [[benjamin-clavie\|Clavié]] |
|---|---|---|
| 한계의 근거 | **품질 저하** — 길어지면 망가진다 | **비용 + 절대 규모** — 늘려도 코퍼스에 못 미친다 |
| 비유 | 플로피 디스크 1장 | **한 개 주의 법전** |
| 결론 | 검색이 필요하다 | **오케스트레이션이 필요하다** → [[orchestrator-searcher-split]] |

**둘 다 "컨텍스트를 늘리면 해결된다"를 각자의 방식으로 부정한다.**

## 이 위키의 긴 컨텍스트 논의와 정면으로 만난다

[[long-context-agents]]([[minimax|MiniMax]], 09-08)는 **긴 컨텍스트를 에이전트 실행의 요구사항**으로 놓았다 — *"짧은 컨텍스트로는 복잡한 작업을 수행하기에 충분하지 않습니다."* 그 페이지는 **1천만 토큰을 이미 갖고 있었다**는 사실까지 기록한다.

**모순은 아니고 축이 다르다.**

| | [[long-context-agents]] | 이 페이지 |
|---|---|---|
| 묻는 것 | **얼마나 들어가야 루프가 도는가** | **들어갈 수 있는 것보다 코퍼스가 크면 어떻게 하는가** |
| 전제 | 채우는 것은 **실행이 만들어낸 것**(도구 응답) | 채우는 것은 **밖에서 가져온 것**(문서) |
| 답 | 길이를 늘린다 | **고른다** |

> ⚠️ **두 소스 다 자기 주장에 유리한 쪽 수치만 든다.** [[minimax|MiniMax]]는 *왜 1천만에서 100만으로 줄었는지* 말하지 않았고, 여기서는 *35만 토큰* 의 근거가 화자 의견뿐이다. **이 위키는 어느 쪽 숫자도 채택하지 않는다.**

## 이 위키의 세 가지 대응

같은 압력에 이 위키가 이미 모아 둔 답들 사이에 이 페이지가 앉는다.

| 대응 | 방법 | 페이지 |
|---|---|---|
| **줄인다** | 리셋·압축 | [[context-resets-and-compaction]] |
| **고른다** | 무엇을 넣을지 설계 | [[context-engineering]] · [[push-vs-pull-context-retrieval]] |
| **펼쳐 놓고 찾게 한다** | 파일 시스템에 두고 프리미티브로 탐색 | [[file-system-agent]] · [[corpus-as-filesystem-workspace]] |
| **쪼갠다** | 서브 에이전트에 나눠 담는다 | [[orchestrator-searcher-split]] |

## References

- [[tech-bridge-bm25-agentic-search]] · [[tech-bridge-knowledge-agents-not-coding-agents]]
- 인물: [[jo-bergum]] · [[benjamin-clavie]]
- 개념: [[agentic-search]] · [[retrieval-not-reasoning-bottleneck]] · [[corpus-as-filesystem-workspace]] · [[orchestrator-searcher-split]]
- 정면으로 만나는 곳: [[long-context-agents]] · [[harness-pruning]] · [[agent-harness-design]]
- 같은 압력의 다른 답: [[context-engineering]] · [[context-resets-and-compaction]] · [[push-vs-pull-context-retrieval]] · [[file-system-agent]]

---
title: 오라클 갭 (Oracle Gap)
type: concept
category: technique
tags: [evaluation, retrieval, ceiling, measurement, knowledge-work]
aliases: [oracle gap, 완벽한 문서와의 거리]
related: [retrieval-not-reasoning-bottleneck, orchestrator-searcher-split, tools-are-not-neutral, browsecomp-plus, ir-evaluation-obsolescence, which-bm25-problem, all-or-nothing-accuracy]
first-seen: tech-bridge-knowledge-agents-not-coding-agents
sources: [tech-bridge-knowledge-agents-not-coding-agents]
created: 2026-09-21
updated: 2026-09-21
---

# 오라클 갭 (Oracle Gap)

**완벽한 문서를 손에 쥐여 줬을 때의 성능과, 내 검색 시스템이 실제로 내는 성능의 차이.** 검색이 얼마를 까먹고 있는지를 **하나의 숫자**로 만든다.

> 저는 그것을 **오라클 갭(oracle gap)** 으로 생각하는 걸 좋아합니다. **오라클 갭은 완벽한 문서와 여러분의 검색 시스템 사이의 차이입니다.** — [[benjamin-clavie]], [[tech-bridge-knowledge-agents-not-coding-agents]] (14:31~14:41)

> **여기서 오라클 갭은 에이전트를 쓰기 전에 약 10포인트였고, 에이전트를 쓴 뒤에는 6포인트로 내려갑니다. 그러니까 실수가 약 40% 줄어든 겁니다.** (14:41~14:53)

## ⭐ 같은 날 같은 양이 두 번 나왔다 — 한 번은 이름 없이

[[jo-bergum|Bergum]]이 같은 무대에서 **정확히 이 차이를 실험으로 보여 주고 이름을 붙이지 않는다.**

| | [[retrieval-not-reasoning-bottleneck]] ([[jo-bergum\|Bergum]]) | **오라클 갭** ([[benjamin-clavie\|Clavié]]) |
|---|---|---|
| 상한 조건 | **증거 문서를 컨텍스트에 인위적으로 채워 넣는다** | **완벽한 문서** |
| 실제 조건 | 검색 도구가 달린 하네스 | 내 검색 시스템 |
| 결론의 형태 | **정성** — *"추론은 병목이 아니다"* | **정량** — *"10포인트"* |
| 처방 | 검색 품질·쿼리 구성 | **아키텍처(분업)** → [[orchestrator-searcher-split]] |

**두 발표자가 서로를 모른 채 같은 측정 도구를 쓴다.** Bergum은 그것으로 *어디가 병목인가*를 논증하고, Clavié는 그것으로 *내 개선이 얼마짜리인가*를 잰다.

## 왜 이 지표가 유용한가

**정확도 절대값보다 덜 속인다.** 88.9%가 좋은지 나쁜지는 과제 난이도에 달렸지만, **오라클 갭은 "같은 과제에서 완벽한 검색이라면 얼마였을까"를 기준으로 삼으므로 난이도가 상쇄된다.**

그래서 이 지표는 **무엇을 고칠지 알려 준다** — 갭이 크면 검색을, 작은데 절대값이 낮으면 모델·추론을.

이것이 [[ir-evaluation-obsolescence]]가 남긴 공백을 메운다. 그쪽은 *"nDCG 대신 작업 성공을 보라"* 였는데, **작업 성공률만으로는 실패의 책임이 어디인지 알 수 없다.** 오라클 갭이 그 분해를 준다.

## ⚠️ 남는 갭이 설명되지 않는다

소스 자신이 그것을 인정한다:

> **왜 내 에이전트는 88.9를 받는데 인간은 99.4를 받죠? 10%를 그냥 테이블에 두고 오는 셈입니다. 그런데 저는 그걸 이해할 수 없습니다 — 그건 에이전트고, 벤치마크에서 10턴을 받습니다. 완전한 에이전틱 시스템이고, 자기 결과에 대해 생각할 기회를 얻는데도 성능을 놓치고 있는 겁니다.** (13:38~14:00)

**분업으로 10 → 6까지 줄었지만 6이 왜 남는지는 소스에 없다.**

## ⚠️ 측정의 조건

- **오라클이 무엇인지 정의되지 않는다** — *"완벽한 문서"* 가 골든 문서 집합인지, 인간 전문가의 성능(99.4)인지 **자막에서 구분되지 않는다.** 두 문단이 섞여 있다.
- **벤치마크 이름이 판독되지 않는다** — *"[MQA]"*([[hugging-face|Hugging Face]]·[Snowflake] 공동 공개 PDF 기반 기업용 과제). → [[tech-bridge-knowledge-agents-not-coding-agents]]
- **10 → 6이 어느 시스템 쌍인지**, 서처 개수·모델·비용이 전부 없다.
- **당사자 진술이다** — 갭을 좁힌 것이 자사 제품이다.

→ **이 위키는 지표의 형태를 받고 수치는 받지 않는다.** [[which-bm25-problem]]이 이 소스 자신에게도 적용된다.

## References

- [[tech-bridge-knowledge-agents-not-coding-agents]] · [[benjamin-clavie]] · [[mixedbread]]
- 쌍을 이루는 관측: [[retrieval-not-reasoning-bottleneck]] · [[browsecomp-plus]]
- 개념: [[orchestrator-searcher-split]] · [[tools-are-not-neutral]] · [[ir-evaluation-obsolescence]] · [[which-bm25-problem]]

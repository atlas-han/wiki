---
title: BrowseComp-Plus
type: entity
category: tool
tags: [benchmark, deep-research, agentic-search, retrieval, evaluation]
aliases: [BrowseComp+, BrowseComp Plus, 브라우즈컴프 플러스]
sources: [tech-bridge-bm25-agentic-search, tech-bridge-knowledge-agents-not-coding-agents]
created: 2026-09-21
updated: 2026-09-21
---

# BrowseComp-Plus

**심층 연구(deep research) 벤치마크.** 수수께끼 같은 질문을 주고, 모델이 `search` 도구 하나만 가지고 **검색 → 읽기 → 쿼리 재구성**을 반복해 정답에 닿는지를 잰다.

**이 위키에 검색 품질을 최종 정답률로 환산해 주는 첫 벤치마크**다. 지금까지의 평가 페이지들([[skill-evals]]·[[field-level-unit-test-evals]]·[[terminal-bench]])은 **작업 수행**을 쟀지 **무엇을 찾아왔는가**를 재지 않았다.

## 프로토콜

| 항목 | 내용 |
|---|---|
| 과제 | **수수께끼(riddle) 형태의 긴 질문** — *"펍 퀴즈라고 생각해 보세요"* |
| 도구 | **`search` 하나** — 쿼리 문자열을 받아 스니펫을 돌려준다 |
| 루프 | 쿼리 실행 → 응답 읽기 → **재구성** → 컨텍스트가 차거나 답을 찾을 때까지 |
| 채점 | 질문마다 **골든 정답(golden reference answer)** 이 있고 종단 일치를 본다 |
| 문항 수 | **830개** |

> 이 모든 질문에는 **기준이 되는 정확한 답이 있어서 모델과 전체 과정이 그 답과 정확히 일치하는지 확인할 수 있습니다.** — [[jo-bergum]], [[tech-bridge-bm25-agentic-search]] (05:35~05:43)

## 이 벤치마크가 보여 준 것

**검색 품질이 종단 정확도를 정한다**는 것을 분해해서 보여 준 것이 이 위키가 이 벤치마크에서 얻은 값이다.

- 필요한 **증거 문서를 컨텍스트에 인위적으로 채워 넣으면 정확도가 매우 높다** → **추론은 병목이 아니다.**
- 같은 모델을 **검색 도구가 달린 하네스에 놓으면 정확도가 떨어진다** → 병목은 **하네스의 쿼리 구성 능력 + 검색 품질**이다.

→ [[retrieval-not-reasoning-bottleneck]]

그리고 **자기 기준선이 문제가 됐다**:

> [BrowseComp-Plus]도 BM25를 기준선으로 사용하지만, **알고 보니 그 기준선은 형편없었습니다.** (…) **최근 논문에서 사용된 매개변수는 이러한 긴 문서를 처리하기에 적합하지 않은 것으로 나타났습니다.** — (09:54~10:23)

→ [[which-bm25-problem]]

## ⚠️ 코퍼스 크기가 세 갈래다

**같은 날 같은 무대의 두 발표가 이 벤치마크의 규모를 다르게 말하고, 그중 하나는 자기 발표 안에서도 두 번 다르게 말한다.**

| 출처 | 말한 크기 | 위치 |
|---|---|---|
| [[jo-bergum\|Bergum]] | *"약 10만 5천 건에서 10만 건"* | 05:28 |
| [[benjamin-clavie\|Clavié]] | **20만 개** | 09:20 |
| [[benjamin-clavie\|Clavié]] (같은 발표) | **10만 개** | 11:03 |

**어느 것도 확인할 근거가 이 소스들에 없다.** 이 위키는 **판정하지 않고 대조만 기록한다.**

## ⚠️ 그 밖에 미확정

- **논문·저자·기관** — *"작년에 논문에 발표됐어요"*(04:51)뿐이고 **이름이 없다.**
- **"작년"이 언제인지** — 두 소스 다 **촬영 시점이 미확정**이라 환산할 수 없다.
- **리더보드의 운영 주체** — [[benjamin-clavie|Clavié]]가 *"[BrowseComp-Plus] 리더보드"*(09:18)라 부르지만 누가 유지하는지 없다.
- **정확도 수치의 대응** — [[benjamin-clavie|Clavié]]는 60% / 70~80 / 90 / 89.8 / 90.2를 말하는데 **어느 시스템이 어느 값인지 슬라이드를 봐야 알 수 있고 자막에는 없다.**

## References

- [[tech-bridge-bm25-agentic-search]] · [[tech-bridge-knowledge-agents-not-coding-agents]]
- 개념: [[retrieval-not-reasoning-bottleneck]] · [[which-bm25-problem]] · [[agentic-search]] · [[ir-evaluation-obsolescence]] · [[bm25]]
- 인물: [[jo-bergum]] · [[benjamin-clavie]]

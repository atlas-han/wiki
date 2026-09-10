---
title: 블랙박스 접근 (Black-Box Agent Approach)
type: concept
category: pattern
tags: [black-box, privacy, approval, write-gate, audit, multi-agent, silos]
aliases: [블랙박스 에이전트, 쓰기 시점 승인]
related: [agent-collaboration-as-search, credential-injection-outside-sandbox, agent-governance-layers, agent-action-record, action-reversibility, privacy-auto-mode, no-silent-write]
first-seen: tech-bridge-agent-to-agent-as-search
sources: [tech-bridge-agent-to-agent-as-search]
created: 2026-09-10
updated: 2026-09-10
---

# 블랙박스 접근

**아무도 트레이스에 접근할 수 없는 LLM이 모든 사일로를 읽어 답(또는 쓰기 직전)까지 간 뒤, 그 쓰기에 필요했던 정보의 소유자에게만 승인을 요청하는 것.** [[jean-denis-greze]]가 다섯 전략 중 *"아주 강력한데 실제로는 많이 못 봤다"* 고 한 것.

> **다른 사람들의 사일로 정보를 봐야만 답할 수 있는 질문**을 할 때, **아무도 트레이스에 접근할 수 없는 LLM**이 모든 데이터에 접근해 답에 도달합니다 — 답을 얻거나, **쓰기(write)인 도구 호출을 하기 직전**까지. 그러고 **그 도구 호출에 어떤 정보가 필요했는지** 보고, **그 정보를 소유한 사람에게만** 승인을 요청합니다. — [[tech-bridge-agent-to-agent-as-search]]

## 예 — 100명 회사에서 CFO 소개 받기

| 단계 | 누가 | 승인 |
|---|---|---|
| 요청이 모두의 에이전트로 간다 | — | — |
| 모두의 에이전트가 **자기 Gmail·사일로**를 뒤진다 | 100개 에이전트 | **없음** (*"자동으로, 아무 사람에게도 묻지 않고"*) |
| 블랙박스가 연결된 20명을 받고 가장 강한 연결(Bob)을 고른다 | 블랙박스 | 없음 |
| **Bob에게만** *"이 정보를 공유해도 될까요?"* | Bob | **있음** |

전략 4(사람 통로 — 100명 모두에게 승인 요청)의 스팸 문제를 **승인 대상을 필요한 사람으로 좁혀** 푼다.

## 벽의 위치 — 입구에서 출구로

[[agent-governance-layers]]의 두 층으로 읽으면 이 접근은 **①접근 제어를 읽기에서 풀고 쓰기·공유 시점에서만 건다.** 같은 날 [[tech-bridge-company-brain-security|PromptQL 편]]의 [[credential-injection-outside-sandbox]]가 **읽기부터** 사용자 단위로 잠그는 것과 정반대다.

| | 읽기 | 쓰기/공유 |
|---|---|---|
| [[credential-injection-outside-sandbox]] (PromptQL) | 사용자 클레임으로만 | 사용자 자격증명으로만 |
| **블랙박스** (Greze) | **전부** | 정보 소유자 승인 |

두 소스는 서로를 모른다. 전제 조건이 다르다 — PromptQL의 고객은 포춘 은행, Greze의 조건은 *"회사 안에서는 불가능하지 않고 보안·컴플라이언스 팀도 괜찮다고 할 수 있다"*.

## 화자가 직접 다는 한계 셋

1. **블랙박스를 신뢰해야 한다** — *"전체 접근을 가진 LLM을 위해 모든 사일로를 허물어도 되고, 그것이 공유의 순간까지는 허락을 묻지 않는다는 것을."*
2. **마지막 답과 함께 다른 정보가 새면 안 된다** — 악몽: *"다른 회사 채용 담당자와 연결돼 있나?"* 로 **이직 면접 중임을 알아내는** 것. 승인은 Bob이 하지만 유출되는 것은 **질문 자체가 드러내는 추론**이다.
3. **진짜 블랙박스일 수는 없다** — *"회사의 누군가가 언젠가 감사하고 싶어 할 겁니다. CISO 조직 어딘가에 모든 데이터에 접근하는 사람이 있어야 합니다."* → 그 사람이 있으면 블랙박스가 아니다. 소스는 이 모순을 인지하고 닫지 않는다.

## 이 위키의 다른 논의와의 관계

- [[agent-action-record]] — 트레이스에 아무도 접근 못 한다는 전제와 *모든 행동을 기록하라* 는 Composio의 처방이 **충돌**한다. Greze의 셋째 한계가 그 충돌의 자인이다.
- [[action-reversibility]] — 승인이 **쓰기 직전**에 오는 것은 *되돌릴 수 없는 행동 앞에 신뢰를 세운다* 는 Composio의 논리와 같다. 읽기는 되돌릴 필요가 없다고 보는 셈이다 — ⚠️ 하지만 한계 2가 보여주듯 **읽은 것에서 추론된 것이 답에 새면** 읽기도 되돌릴 수 없는 행동이 된다.
- [[no-silent-write]] — 같은 *쓰기 시점 승인* 이되 승인자가 다르다: PromptQL은 **쓰는 사람**, 블랙박스는 **정보 소유자**.

## References

- [[tech-bridge-agent-to-agent-as-search]] (first-seen) · [[jean-denis-greze]]
- 관련: [[agent-collaboration-as-search]] · [[credential-injection-outside-sandbox]] · [[agent-governance-layers]] · [[agent-action-record]] · [[privacy-auto-mode]]

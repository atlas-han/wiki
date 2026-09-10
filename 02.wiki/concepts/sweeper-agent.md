---
title: 청소부 에이전트 (Sweeper Agent)
type: concept
category: pattern
tags: [sweeper, silo, shared-wiki, policy, scheduled, privacy, knowledge-flow]
aliases: [sweeper AI, AI 정리 에이전트, 청소부 AI]
related: [company-brain, llm-wiki-pattern, no-silent-write, privacy-auto-mode, scheduled-agent-automations, agent-memory, prompt-injection, agent-collaboration-as-search]
first-seen: tech-bridge-agent-to-agent-as-search
sources: [tech-bridge-agent-to-agent-as-search]
created: 2026-09-10
updated: 2026-09-10
---

# 청소부 에이전트

**각 비공개 사일로 안에 에이전트를 하나 두고, "무엇이 사일로에 남아야 하는가"의 정책과 "어떤 공유 공간이 있는가"의 설명을 준 뒤, 하루의 끝에 새 정보 중 공유해도 되는 것을 공유 공간으로 옮기게 하는 것.** [[jean-denis-greze]]가 *"이 발표에 정말 잘 되는 좋은 아이디어가 하나 있다면 이것"* 이라 한 패턴.

> 각 비공개 사일로 안에 AI가 하나 있습니다. 그 AI는 **무엇이 사일로 안에 남아야 하는지에 대한 정책**을 갖고, **당신이 가진 모든 공유 공간의 설명**도 갖습니다. 그리고 **하루의 끝에** 사일로의 새 정보를 보고 공개 공간에 — 회사에 공개인 공간에 — 넣습니다. — [[tech-bridge-agent-to-agent-as-search]]

## 개인 위키의 회사 버전

> 여러분 모두가 AI에게 시켜 만드는 개인 위키 — 제가 당신의 목표와 친구를 알 수 있게 하는 — 와 같은데 **회사 수준**인 거죠.

즉 [[llm-wiki-pattern]]의 **ingest 단계를 사일로 경계를 넘는 자동 파이프라인**으로 만든 것이다. 발표자의 베팅: *"오픈소스 claw 계열 세계와 작은 회사 양쪽에서 **즉각적 ROI**가 있을 하나는 **AI가 자동으로 만드는 위키**"*. 이 vault 자체가 그 패턴의 개인판이고, 이 페이지는 그것의 **다중 사일로 판**을 기록한다.

## 어려운 부분 — 무엇을 옮길지 누가 정하는가

| 방식 | 무엇 | 발표자의 판정 |
|---|---|---|
| **사람에게 묻기** | LLM이 목록을 만들고 *"넣어도 될까요?"* → 사람이 *"네"* | *"시간을 많이 아꼈다 — 어차피 안 했을 테니"* → [[no-silent-write]] |
| **LLM이 정책 집행** | 정책을 맡겨 자동으로 드러냄 | *"그쪽으로 아주 빨리 간다"*, **6개월 안에**, 단 **10~50명 고신뢰 회사**부터 → [[privacy-auto-mode]] |

첫째가 같은 날 [[tech-bridge-company-brain-security|PromptQL 편]]의 규칙과 정확히 같고, 둘째는 PromptQL이 가지 않는 곳이다.

## 이 위키의 다른 자동화와의 관계

- [[scheduled-agent-automations]] ([[cursor-cloud|Cursor]]) — *"하루의 끝에"* 도는 것이므로 형태상 **예약형 자동화**다. Cursor의 것이 코드베이스를 유지보수한다면 이것은 **지식의 흐름**을 유지보수한다.
- [[agent-memory]] — 개인 에이전트의 메모리(사일로)에서 조직 공유 지식으로의 **승격 경로**다. 이 위키가 미해결로 둔 *여러 에이전트 간 공유* 에 대한 첫 구체적 답이다.
- [[company-brain]] — 회사 두뇌의 **입력 파이프라인** 후보. PromptQL은 사람이 일하는 중 팝업으로 넣고, 청소부는 하루 끝에 일괄로 넣는다.

## ⚠️ 실패 지점 — 화자 자신이 단다

- **사일로 안의 [[prompt-injection]]** — *"더 열린 사일로에 누가 나쁜 걸 넣고, 에이전틱 검색의 일부로 그걸 꺼내면."* 청소부가 그것을 **공유 공간으로 옮기면** 오염이 퍼진다.
- **영구 오염** — *"LLM이 실수해서 정보 하나가 틀리면 영원히 오염된다."* Apex→Ivy 사례.
- **오공개** — 사람이 없으면 오탐·잘못된 공개. *"누군가 해고되기도, 고객이 고소하기도."*
- 정책을 집행하는 LLM의 취약성 — [[agent-governance-layers]]가 던진 질문이 그대로 남는다.

## References

- [[tech-bridge-agent-to-agent-as-search]] (first-seen) · [[jean-denis-greze]]
- 관련: [[company-brain]] · [[llm-wiki-pattern]] · [[no-silent-write]] · [[privacy-auto-mode]] · [[scheduled-agent-automations]]

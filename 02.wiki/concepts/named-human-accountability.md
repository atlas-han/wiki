---
title: 모든 변경에 사람의 이름 (Named Human Accountability)
type: concept
category: pattern
tags: [accountability, attribution, wiki, governance, audit, authorship]
aliases: [사람 이름 규칙, human-backed changes]
related: [no-silent-write, company-brain, behavior-validated-trust, agent-action-record, decision-quality, agentic-misbehavior]
first-seen: tech-bridge-company-brain-security
sources: [tech-bridge-company-brain-security]
created: 2026-09-10
updated: 2026-09-10
---

# 모든 변경에 사람의 이름

**공유 지식 저장소의 모든 변경은 사람의 이름으로 뒷받침되어야 하며, "에이전트가 추가했다"는 항목은 허용되지 않는다.** [[tech-bridge-company-brain-security]]의 두 규칙 중 둘째.

> 위키 안에 *"Claude가 이걸 추가했다"*, *"당신의 AI 에이전트가 추가했다"*, *"Hermes가 추가했다"* 는 **허용되지 않습니다.** 아니, **"Tan이 이걸 추가했다."** 그 이름이 있어야 **"이 사람이 실수해서 모두의 급여를 모두에게 보이게 했다"** 로 되돌아갈 수 있습니다. 그러면 시정 조치를 취할 수 있죠 — 개선 계획(PIP)에 넣든, *"위키 편집하는 법을 몰랐군요"* 하든.

## 목적은 신뢰가 아니라 귀속이다

이 규칙은 [[tech-bridge-ai-era-code-quality|IBM 편]]의 [[behavior-validated-trust]] — *"작성자(authorship)가 아니라 검증된 행동(evidence)을 신뢰하라"* — 와 **정면으로 마주 본다.** 하지만 묻는 것이 다르다.

| | [[behavior-validated-trust]] | 이 개념 |
|---|---|---|
| 질문 | 이 변경을 **믿어도 되는가** | 이 변경이 문제였을 때 **누구에게 가는가** |
| 근거 | 테스트·검증 | 이름 |
| 시점 | 머지 전 | 사고 후 |

둘은 양립한다 — 검증으로 믿고, 이름으로 책임진다. **어느 소스도 그 구분을 짓지 않는다.** 그리고 이 개념이 전제하는 것이 하나 있다: 공유 지식에는 **테스트가 없다**(사실의 정확성은 코드처럼 실행해 검증할 수 없다). 그래서 코드에서는 evidence가 authorship을 대체할 수 있어도 위키에서는 **사람 이름이 마지막 보루**가 된다.

## 규칙의 순서

> 하나, 모든 것이 하나의 전사 위키로. 둘, 모든 변경에 사람 이름. **그렇게 정하면** 둘째 범위로 갈 수 있습니다 — **그들이 그렇게 하기 쉽게** 만들어야 하고, 그래서 **스코프**가 필요합니다.

즉 이름 규칙이 **먼저**이고 스코프·UX([[no-silent-write]])는 그것을 **가능하게 하는 수단**이다. 사람이 이름을 걸 수 있으려면 승인이 가벼워야 한다.

## 이 위키의 다른 기록 논의와의 관계

- [[agent-action-record]] — Composio는 *에이전트가 무엇을 했는가* 를 기록한다. 이 개념은 *어느 사람이 승인했는가* 를 기록한다. 감사 로그의 **두 열**이다. 같은 날 [[tech-bridge-agent-to-agent-as-search|Greze 편]]이 던진 *"누가 무엇을 승인하고, 무엇이 로깅되고, 무엇이 되돌릴 수 있는가"* 의 첫째 항에 대한 답이다.
- [[decision-quality]] — IBM이 *판단은 사람 몫* 이라 한 것의 **행정적 형태**다: 판단에 이름이 붙는다.
- [[agentic-misbehavior]] — 인턴이 모두의 급여를 보게 되는 사고는 [[agent-governance-layers]]의 메일 200통 사고와 달리 **에이전트가 아니라 승인한 사람의 실수**로 분류된다. 이 규칙은 그 분류를 가능하게 하는 장치다.

## ⚠️ 한계

- **징벌의 역효과** 미논의 — 이름이 붙으면 사람들이 승인을 피하고, 그러면 두뇌가 자라지 않는다(발표자 자신의 *일일 업데이트 수* 지표가 떨어진다). 소스는 이 긴장을 말하지 않는다.
- 여러 사람이 논쟁으로 만든 지식([[multiplayer-agent-context]])에는 **누구의 이름**이 붙는가 — 없다.
- 당사자 진술.

## References

- [[tech-bridge-company-brain-security]] (first-seen) · [[tanmai-gopal]]
- 관련: [[no-silent-write]] · [[behavior-validated-trust]] · [[agent-action-record]] · [[company-brain]]

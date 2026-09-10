---
title: 지식 노동 에이전트 격차 (Knowledge Work Agent Gap)
type: concept
category: framing
tags: [knowledge-work, agent-infrastructure, primitives, bottleneck]
aliases: [지식 노동 격차, six primitives]
related: [agent-action-record, agent-governance-layers, action-reversibility, agent-org-adoption, trusted-throughput, generator-evaluator-pattern, company-brain]
first-seen: tech-bridge-knowledge-work-agent-infrastructure
sources: [tech-bridge-knowledge-work-agent-infrastructure, tech-bridge-company-brain-security]
created: 2026-09-09
updated: 2026-09-10
---

# 지식 노동 에이전트 격차

**같은 모델이 코딩에서는 자율적으로 일하고 지원·영업·채용에서는 눈을 감고 일하는 이유는 모델이 아니라 주변 인프라에 있다**는 프레이밍.

> 코딩과 관련된 모든 인프라와 시스템이 **말 그대로 에이전트를 위해 설계되었기 때문에** 가능했던 것입니다. — [[karan-vaidya]], [[tech-bridge-knowledge-work-agent-infrastructure]]

## 여섯 primitive

주장은 목록의 형태를 갖는다 — **코딩은 여섯을 다 갖고 있었고 지식 노동은 하나도 갖고 있지 않다.**

| primitive | 코딩에서 주어지는 것 | 지식 노동의 상태 |
|---|---|---|
| **중앙화** | 코드베이스 = 단일 진실 원천 | 한 거래가 5개 앱에 흩어짐, 앱마다 로그인 |
| **히스토리** | Git이 공짜로 기록 | 앱들이 히스토리를 보관하지 않음 → 매번 백지 |
| **맥락** | 아키텍처·스타일이 코드베이스 안에 | 사람이 머릿속에서 실을 엮어야 함 |
| **검증** | 테스트·타입·컴파일러·linter가 사람 없이 루프를 닫음 | *"이게 애초에 나갔어야 했는가"* 를 물을 검사가 없음 |
| **거버넌스** | 브랜치·리뷰어·code owner·배포 분리 | 권한이 흩어져 결국 프롬프팅으로 처리 |
| **가역성** | `revert`·`bisect` | 발송·송금·hard delete에 undo 없음 |

## 왜 이 프레이밍이 유용한가

이 위키는 에이전트가 코딩 밖에서 잘 안 되는 현상을 여러 소스에서 봐 왔지만([[agent-org-adoption]]·[[persistent-agent-teams]]), 대개 **채택·조직 문제**로 설명됐다. 이 프레이밍은 그것을 **환경의 결손 목록**으로 바꾼다 — 즉 *에이전트를 더 잘 쓰는 법* 이 아니라 *무엇을 지어야 하는가* 의 문제로.

그리고 [[sutton-bitter-lesson]]류의 *모델이 좋아지면 해결된다* 는 기대에 반례를 놓는다:

> **2년 동안 모델이 병목이었습니다. 이제 모델은 소프트웨어 엔지니어링이 100% 자율적일 만큼 충분히 좋아졌습니다. 그런데 이제는 그 외의 모든 것이 병목입니다.**

## ⚠️ 이 주장을 읽을 때

- **당사자 진술.** 이 여섯을 파는 회사([[composio]])의 창업자가 한 주장이다. *병목이 인프라* 라는 결론과 *그가 인프라를 판다* 는 사실을 분리해 읽을 수 없다.
- **여섯의 우선순위·상호작용이 논의되지 않는다.** 무엇부터 세워야 하는지, 하나만 있으면 어떤지 소스가 답하지 않는다.
- **"소프트웨어 엔지니어링은 100% 자율적"** 이라는 전제 자체가 이 위키의 다른 소스들과 충돌한다 — [[tech-bridge-ai-era-code-quality|IBM 편]]은 같은 날 *결정은 여전히 사람 몫* 이라고 말하고, [[tech-bridge-cursor-legacy-refactoring|Cursor 편]]의 라이브 마이그레이션은 시간 안에 끝나지 않았다. > ⚠️ Contradiction: 위키는 어느 쪽도 채택하지 않고 셋을 나란히 둔다.

## 같은 진단, 다른 처방 — 회사 두뇌 (2026-09-10)

[[tech-bridge-company-brain-security]]가 이 개념의 출발점(*코딩 에이전트는 코딩 주변 인프라 덕에 된다*)을 공유하되 **반대 방향의 처방**을 낸다. Composio는 코딩 밖에 여섯 primitive를 새로 짓자 하고, [[tanmai-gopal]]은 **코딩 에이전트를 그대로 두고 회사 지식을 그것이 읽을 마크다운으로** 만들자 한다 — *"Claude Code가 모든 것에 쓰인다. Claude Cowork도, Codex 앱도 같은 아키텍처. 저희는 그것을 위한 두뇌를 만든다."* → [[company-brain]]. 여섯 primitive로 보면 회사 두뇌는 **중앙화·맥락·거버넌스** 셋을 마크다운+스코프로 덮고 히스토리·검증·가역성은 다루지 않는다. 두 소스는 서로를 모른다(이틀 연속 이 채널에 올라왔다). 그리고 이 개념의 전제 *"소프트웨어 엔지니어링은 100% 자율적"* 에 PromptQL 편은 반례를 하나 더한다 — 자사 SRE 사례에서 에이전트는 *"스킬이 없어서 형편없이 실패"* 했고 사람 둘의 논쟁이 원인을 찾았다([[multiplayer-agent-context]]).

## References

- [[tech-bridge-knowledge-work-agent-infrastructure]] · [[composio]] · [[karan-vaidya]]
- [[tech-bridge-company-brain-security]] — 같은 진단, 다른 처방 · [[company-brain]] (2026-09-10)

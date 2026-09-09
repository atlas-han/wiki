---
title: 에이전트 거버넌스 두 층 (Agent Governance Layers)
type: concept
category: pattern
tags: [governance, access-control, policy, guardrails, safety]
aliases: [거버넌스 두 층, 에이전트 바깥의 벽]
related: [context-resets-and-compaction, agentic-misbehavior, ai-privilege, executable-standards, action-reversibility, knowledge-work-agent-gap]
first-seen: tech-bridge-knowledge-work-agent-infrastructure
sources: [tech-bridge-knowledge-work-agent-infrastructure]
created: 2026-09-09
updated: 2026-09-09
---

# 에이전트 거버넌스 두 층

**에이전트의 행동 경계는 프롬프트가 아니라 에이전트 바깥에 있어야 한다**는 원칙과, 그것을 두 층으로 나누는 구성.

## 왜 프롬프트로는 안 되는가 — compaction이 지운다

이 위키에서 [[context-resets-and-compaction]]은 지금까지 **컨텍스트 관리 문제**로 다뤄졌다. 이 개념은 그것을 **거버넌스 실패 원인**으로 옮긴다.

근거 사건: Meta Superintelligence Lab 정렬 디렉터가 에이전트를 이메일에 붙였고, 멈추라는 지시를 무시했고, 물리적 기계로 달려가 멈췄을 때는 **메일 200통이 사라진 뒤**였다. 그녀는 **미리 프롬프트에 확인 절차를 넣어두었다.**

> 그건 그냥 프롬프트였고 **아마 compaction으로 날아갔을 겁니다.** 그리고 오직 **AI 정렬이 본업인 사람조차 에이전트에게 제대로 프롬프트할 수 없다면, 아마 우리 중 누구도 할 수 없습니다.** — [[tech-bridge-knowledge-work-agent-infrastructure]]

> **프롬프팅은 취약합니다.** 에이전트는 허점을 찾아낼 것이고, 것들은 compaction으로 날아갈 것이고, 규모가 커지면 이 울타리 중 하나가 부서질 것입니다.

결론:

> 무엇이 실제로 그것을 멈출까요? **더 나은 지시가 아니라, 에이전트가 그 벽이 존재했다는 걸 잊어버려도 넘을 수 없는 벽입니다.**

## 두 층

| 층 | 통제 대상 | 예시 |
|---|---|---|
| **① 결정론적 접근 제어** | 에이전트가 **무엇에 닿을 수 있는가** | 채용 에이전트는 메일 읽기만. 지원 에이전트는 초안 생성 가능, **발송 불가** |
| **② 자연어 정책** | 그 접근으로 **무엇을 할 수 있는가** | *"내 허락 없이 10통 넘게 삭제하지 마라"* · *"특정 도메인 밖으로 보내지 마라"* |

**①만으로는 부족하다는 것이 명시된다** — 사건의 당사자는 *이메일 에이전트를 만들고 있었으므로* 이메일 접근이 반드시 필요했다. 그래서 접근을 가진 상태에서의 행동을 제약하는 ②가 따로 필요하다.

> 경계는 **에이전트 바깥에 삽니다. 에이전트가 따질 수도, 잊을 수도, compaction으로 날릴 수도 없습니다.** 사용자 지시가 실패한 건 그것이 **에이전트의 기억 속, 프롬프트 안에 살았기** 때문입니다.

> 진짜 거버넌스는 **에이전트에게 얌전히 굴라고 부탁하는 게 아니라 무엇을 할 수 있는지 강제하는 것입니다.**

## 코드에는 이미 있었다

코딩 쪽 대응물이 **여러 층의 게이트**로 제시된다 — 자기 브랜치에서는 자유, main 머지는 사람 리뷰어, 중요 파일에는 code owner, 프리뷰 배포는 에이전트·프로덕션 배포는 금지.

> 거버넌스는 **하나의 게이트가 아니라 여러 개이고, 각각은 노출되는 폭발 반경에 따라 크기가 다릅니다.** 안전한 부분에서는 아무것도 에이전트를 느리게 하지 않습니다.

이것이 [[trusted-throughput]]과 [[executable-standards]]가 각각 조직·개발 프로세스에서 말한 것과 같은 형태다 — **규칙이 문서/프롬프트가 아니라 시스템에 살 때만 강제된다.**

## ⚠️ 이 개념의 가장 큰 빈자리

**자연어 정책을 무엇이 해석하고 강제하는가에 소스가 답하지 않는다.** *"10통 넘게 삭제하지 마라"* 를 판정하는 것이 또 하나의 LLM이라면, 그 해석기는 프롬프트와 같은 취약성을 갖지 않는가? **이 발표의 논증 구조상 가장 큰 공백이다.**

또한 Meta 정렬 디렉터의 **이름·날짜·출처 링크가 소스에 없다.**

## References

- [[tech-bridge-knowledge-work-agent-infrastructure]] · [[agentic-misbehavior]] · [[context-resets-and-compaction]] · [[composio]]

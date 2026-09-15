---
title: 멀티플레이어 에이전트 컨텍스트 (Multiplayer Agent Context)
type: concept
category: pattern
tags: [multiplayer, shared-agent, slack, knowledge-creation, privilege, incident-management]
aliases: [공유 AI, 멀티플레이어 에이전트]
related: [company-brain, credential-injection-outside-sandbox, claude-tag, goal-level-delegation, persistent-agent-teams, no-silent-write, agent-org-adoption]
first-seen: tech-bridge-company-brain-security
sources: [tech-bridge-company-brain-security, tech-bridge-one-designer-plus-ai]
created: 2026-09-10
updated: 2026-09-15
---

# 멀티플레이어 에이전트 컨텍스트

**여러 사람이 하나의 에이전트를 공유 컨텍스트로, 서로 다른 권한 수준을 동시에 갖고 쓰는 것.** [[tech-bridge-company-brain-security]]가 [[company-brain|회사 두뇌]]의 둘째 사용 사례로 놓고 *"아빠 사용 사례, 진짜 큰 놈"* 이라 부른 것.

> 이제 한 사람이 이메일에 답하는 게 아니라 **여러 명이 공유 컨텍스트로 서로 다른 권한 수준을 동시에 갖고 문제를 푸는** 거니까요. 그리고 이것이 **회사 두뇌 지식이 가장 많이 만들어지는 상호작용**입니다.

첫째 사용 사례(남의 지식이 **내** 에이전트로)와의 차이는 **동시성과 권한**이다. 예: 협업 인시던트 관리 — *"로그 가져와, 코드베이스 조사해, PR 올려, 스테이징 배포, 프로덕션 배포, 알림 설정"* 을 여러 사람이 한 에이전트로.

## 지식은 논쟁에서 나온다

소스의 SRE 사례가 이 개념의 핵심 주장을 담는다.

1. 에이전트가 스킬 없이 조사에 실패한다.
2. 엔지니어가 고친다 — *"OpenTelemetry span name을 써"*, *"LIKE 대신 equals 쿼리를 써"*.
3. 에이전트가 **학습을 제안**한다 — *LIKE가 아니라 equals* / *페이지 이름에 커스텀 접두사를 붙이면 문제*.
4. **다른 사람이 합류**해 *"여기서 내린 기술적 결정이 잘못됐어"* — 논쟁.
5. 논쟁이 드러낸 것: *"누군가 문서화하지 않은 기술적 결정"*. 근본 원인.

> **그 논쟁이 지식을 만듭니다.** (…) 이전 제안은 *"페이지에 접두사가 있다"* 였는데 이제 두뇌에 기록되는 것은 **"페이지에 접두사가 있으면 안 된다. 있으면 프로덕션에서 조회 문제가 생긴다"** 입니다. 이건 **여러 사람이 서로 이야기하며 함께 문제를 풀 때** 일어납니다. Slack 스레드에서 두 사람이 대화하며 문제를 풀 때 그것이 **최고 품질의 컨텍스트**를 만듭니다.

즉 에이전트 혼자 제안한 학습(3)은 **증상**이었고, 사람 둘의 논쟁(4→5)이 **원인**을 찾았다. 이것이 [[no-silent-write]]가 *사실 검토* 이상인 이유이고, 에이전트가 자동 저장했다면 **증상이 지식으로 굳었을** 것이다.

## 이 위키의 다른 "여러 사람 + 에이전트"와의 관계

| | 무엇 | 이 개념과의 차이 |
|---|---|---|
| [[claude-tag]] | Slack에서 팀이 에이전트를 태그 — 소스가 직접 *"Claude Tag와 비슷한 멀티플레이어 아이디어"* 라 한다 | Claude Tag의 채널당 메모리는 **사일로**라는 것이 이 소스의 비판 |
| [[goal-level-delegation]] | 위임의 **단위**(목표) | 이 개념은 위임의 **주체 수** |
| [[persistent-agent-teams]] | 에이전트가 여럿, 사람은 매니저 | 이 개념은 **사람이 여럿, 에이전트는 하나** — 정반대 형태 |
| [[agent-org-adoption]] | 조직이 에이전트를 도입하는 곡선 | 이 개념은 도입된 뒤의 **동시 사용** 형태 |

## 대가 — 권한 상승

> 여러 사람에게 둘러싸여 **모든 것을 할 수 있는 에이전트**를 만들면 무섭죠. 엔지니어는 PR 작업이 허용됐는데 **이제 내가 같은 에이전트로 프로덕션에 배포할 수 있으니까요.** (…) 하지만 **같은 자리에 있는 것에 큰 가치가 있죠 — 거기에 모든 지식이 있으니까.**

가치(지식이 한 자리에)와 위험(권한이 한 자리에)이 **같은 원인**에서 온다. 처방은 에이전트가 **말하는 사람의 자격증명**으로 행동하는 것 → [[credential-injection-outside-sandbox]].

## ⚠️ 미해결

- 논쟁으로 만든 지식에 **누구의 이름**이 붙는가([[named-human-accountability]]) — 없다.
- 동시에 여러 사람이 지시할 때의 **충돌 해소** — 없다.
- *"가장 많이 만들어진다"* 의 근거 — 사례 하나.
- 당사자 진술.


## 2026-09-15 — 에이전트의 거처가 워크플로를 정한다 (디자인 사례)

[[tech-bridge-one-designer-plus-ai]]에서 [[vincent-wendy|Vincent Wendy]]의 작업 경로는 **Slack → [[figma|Figma]] → 다시 Slack**이고, 그 이유가 아키텍처가 아니라 **거처**다.

> ***"[[devin|Devin]]이 Slack 안에 살기 때문"***

그래서 *"리서치 → 제품 → 피드백 루프"* 라는 디자인 씽킹이 *"저한테는 그냥 낡았다"* 가 된다. **도구가 어디에 있느냐가 프로세스를 다시 쓴다** → [[design-handoff-friction]].

## References

- [[tech-bridge-company-brain-security]] (first-seen) · [[tanmai-gopal]]
- 관련: [[company-brain]] · [[credential-injection-outside-sandbox]] · [[claude-tag]] · [[no-silent-write]]

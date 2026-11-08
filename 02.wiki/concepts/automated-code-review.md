---
title: "자동 코드 리뷰 (Automated Code Review)"
type: concept
category: pattern
tags: [code-review, verification, multi-pass, false-positives, human-on-the-loop, prompt-injection, review-harness, agents]
aliases: [AI 코드 리뷰, 리뷰 하네스, review harness, 기본 의심 리뷰어]
related: [verification-bottleneck, mergeability-gap, generator-evaluator-pattern, risk-proportional-human-review, named-human-accountability, prompt-injection, test-harness-vs-test-authoring, code-knowledge-graph, production-trace-eval-flywheel, harness-engineering, trusted-throughput, structure-sensitive-tests, deep-modules, agent-plus-program-analysis, review-model-inversion]
first-seen: tech-bridge-death-of-code-review
sources: [tech-bridge-death-of-code-review, tech-bridge-pocock-pr-bottleneck, tech-bridge-rails-harness-engineering, tech-bridge-gitar-agentic-pr-validation, tech-bridge-sentry-stop-prompting-codify-linters, tech-bridge-atlassian-build-your-own-sdlc, tech-bridge-ai-labs-claude-code-verification-review-loop, tech-bridge-rob-shocks-grokbot-manager-coding-agents, tech-bridge-greptile-daksh-gupta-build-review-agent, tech-bridge-anthropic-code-review-seven-layers]
created: 2026-10-03
updated: 2026-11-08
---

# 자동 코드 리뷰

**PR 리뷰를 사람 대신 모델·에이전트가 수행하는 것, 그리고 그것을 "더 똑똑한 리뷰어 하나"가 아니라 사람이 설계한 시스템(리뷰 하네스)으로 만드는 일.** [[laurie-voss|Laurie Voss]]가 [[tech-bridge-death-of-code-review]]에서 업계 현황을 정리하며 내린 결론은 *"review didn't disappear (…) it got rebuilt as a system and that system is built by humans"*(18:17~18:25)이다.

## 현장 규모 (화자 진술, 벤더 수치)

- GitHub Copilot 리뷰어: 리뷰 6천만 건, GitHub 전체 코드 리뷰의 *"more than one in five"*(11:02~11:10) — *"machine review of pull requests is the mainstream default"*.
- CodeRabbit: PR 1,300만+(13:43~13:47). Greptile: 저장소 전체 그래프(13:48~13:56). Graphite: 자기 제안의 수락/거절로 eval 세트(13:56~14:03).
- [[cursor|Cursor]]: 리뷰어 아키텍처를 공개(11:24~11:30).

## 설계에서 반복되는 교훈

| 교훈 | 내용 | en-orig |
|---|---|---|
| **오탐이 리뷰어를 죽인다** | 좋은 코드를 나쁘다고 플래그하는 리뷰어는 *"is going to get ignored"*. Cursor 1세대는 diff마다 **8패스**, 리뷰어 **순서 셔플**(순서가 결과를 바꿨다) — 목적은 오탐 필터 | 11:32~12:00 |
| **다중 패스 + 합의** | 베이징대 연구: 여러 패스를 돌리고 **합의한 것만** 남기면 리뷰 품질 *"up to 44%"*. *"The multipass trick keeps getting rediscovered"* | 12:05~12:24 |
| **에이전트형 리뷰어** | Cursor 재구축: 모델이 diff를 추론하고 도구를 부르고 *"decides where to dig"* | 12:26~12:34 |
| ⭐ **기본 의심** | 모델은 *"that looks good to me so ship it"* — 사람과 똑같이. *"don't trust the code by default. Assume there is something wrong with it."* → *"it is about being suspicious by default"* | 12:36~12:58 |
| **리뷰 + 수정 융합** | 리뷰어가 발견에서 **수정 에이전트**를 띄워 diff를 돌려준다. 다음 단계는 리뷰어가 **코드를 실행해 버그 보고를 증명**. *"the line between reviewing and rewriting is getting very thin"* | 13:04~13:33 |
| **리뷰를 리뷰하는 루프** | [[codex\|Codex]]가 자기 변경을 리뷰하고 더 많은 에이전트가 그 리뷰를 리뷰, *"until every agent reviewer is satisfied"*. 변경마다 앱을 부팅·UI 확인, 로깅 스택 노출 | 17:23~17:48 |

→ 기본 의심은 [[generator-evaluator-pattern]]의 *평가자는 생성자와 다르게 튜닝한다* 와 같은 결론. 다중 패스·합의는 [[agent-swarm]]의 검증 쪽 사용.

## 성공 지표 — "사람이 수락하는가"

> *"all of them are using the same metric as their definition of success which is is a human accepting my answer"* (14:06~14:14)

Cursor는 이를 **resolution rate**라 부르고 52% → 70%+로 올렸다(14:15~14:22). *"They are training their harnesses to get better at the definition of good as defined by human acceptance"*(14:26~14:33). → [[mergeability-gap]]: 모델 학습이 따라갈 길을 하네스가 먼저 간다.

> ⚠️ **위키의 표시 — 수락률은 Goodhart 대상이다.** 같은 발표의 프롬프트 인젝션 연구(아래)가 보여 주듯 **사람도 속는다**(35%). 수락률을 최적화하는 리뷰어는 *사람이 받아들이기 쉬운* 방향으로 갈 수 있다. [[trusted-throughput]]의 *"대시보드는 연기 감지기"* 경고와 같은 자리. Voss는 이 긴장을 짚지 않는다.

## 사람은 어디에 남는가

**in the loop가 아니라 on the loop.** Nicholas Carlini의 C 컴파일러 실험(에이전트 16개, 약 2,000 세션)은 *"no human in the loop"* 였지만 *"there was absolutely a human on the loop"* — 리뷰·검사 시스템, 테스트 하네스, 피드백 시스템을 사람이 썼다(15:07~15:32). → [[test-harness-vs-test-authoring]]

사람 체크포인트가 살아남는 세 자리(19:42~20:08): **싸게 검증할 수 없는 곳**, **폭발 반경이 큰 곳**(보안 민감 환경), **누군가 이름을 걸어야 하는 곳**. → [[risk-proportional-human-review]] · [[named-human-accountability]]

역할은 *"from inspecting the code directly to designing and tuning the systems that inspect the code and designing the definition of good"*(20:13~20:22)으로 올라간다. 처방: *"stop reviewing PRs. Um, it is the wrong level of abstraction for 2026"*(23:19~23:25), *"building uh a reliable review harness. Codify your definitions of good, your company context, your domain knowledge"*(23:34~23:43).

## 취약점 — 리뷰어는 설득당한다

- [[anthropic|Anthropic]] 자동 보안 리뷰어 README: *"not hardened against prompt injection attacks uh and should only be re used to review trusted PRs"*(20:39~20:47) — 리뷰 대상이 리뷰어를 설득해 발견을 철회시킬 수 있다.
- 3월 연구(이름 미발화): 무해한 커밋 메시지로 포장한 취약 코드가 자동 리뷰 에이전트를 **88%** 속였다, 사람은 **35%**(20:59~21:12). *"you don't just lose a reviewer, you lose the thing that was hard to fool"*(21:15~21:19).
- 그리고 *"confidently framed bad code is exactly the kind of code that agents are very good at producing"*(21:24~21:28).

→ [[prompt-injection]] — PR 본문·커밋 메시지·코드 주석이 **리뷰어의 입력**이 되는 순간, 리뷰 대상이 곧 공격 벡터다.

## 마지막 리뷰어 — 프로덕션

*"once the premerge review is all machines, watching what the code actually does becomes the last reviewer standing"*(21:55~22:00) — 테스트 결과가 아니라 **궤적**. → [[production-trace-eval-flywheel]]

## 한 사람이 지은 리뷰 하네스 — Pocock (2026-10-09 · [[tech-bridge-pocock-pr-bottleneck]])

Voss가 업계 수준에서 *"리뷰 하네스를 지어라"* 로 끝냈다면, [[matt-pocock|Matt Pocock]]은 자기 스킬로 그 부품을 보여 준다.

| 부품 | 내용 | en-orig |
|---|---|---|
| **표준은 리뷰어에게** | 구현 에이전트는 탐색·수정·디버깅으로 과부하 — *"don't put coding standards in your implement agent"*. 리뷰 스킬은 diff + 저장소의 coding standards 파일을 **서브에이전트**에서 검사 — *"review is actually underloaded"* | 11:34~13:18 |
| **전역 지시에 넣지 않는다** | AGENTS.md에 두면 *"they sort of drown out your implement. It may read them, it may not."* | 14:07~14:14 |
| ⭐ **외주하지 않는다** | 범용 리뷰어는 너무 일반적이면 오탐, 너무 구체적이면 다른 스택에서 못 쓴다 → *"don't outsource automated review. Build your own. Build up your own coding standards over time."* | 14:47~15:09 |
| ⭐ **댓글이 아니라 커밋** | 댓글은 *"providing more work for the human reviewer"* → *"The reviewer should commit. It should make fixes."* 질문이 있을 때만 댓글 | 15:33~16:00 |
| **구현=작동, 리뷰=좋게** | *"implement, you make it work, and then code review, you actually make it good"* — red-green-refactor를 두 컨텍스트 창으로 | 13:38~13:58 |

> ⚠️ **Contradiction: 벤더 리뷰어.** 이 페이지의 현장 표(Copilot 6천만, CodeRabbit 1,300만, Cursor)는 자동 리뷰의 기본값이 **벤더 제품**임을 보여 주는데, Pocock은 Cursor Bugbot·CodeRabbit을 쓰는 팀에 *"don't outsource"* 라 한다. 근거(오탐 vs 범용성)는 Cursor 1세대가 꼽은 문제와 같다 — **문제 인식은 같고 처방(벤더의 다중 패스 vs 팀 고유 표준)이 갈린다.** 커밋하는 리뷰어는 Cursor의 *리뷰 + 수정 융합* 과 같은 결론이다.

> ⚠️ 리뷰어의 커밋을 **누가 리뷰하나**(Voss의 *"who reviews the reviewer"*)는 Pocock 편에서 다뤄지지 않는다. 측정 없음, 화자 자신의 스킬.

## 개인 규모 — 좁은 리뷰 스킬 셋을 서브에이전트로 (2026-10-09 · [[tech-bridge-rails-harness-engineering]])

위 표가 벤더 규모라면 [[joel-quenneville|Joël Quenneville]]은 **한 개발자의 하네스** 규모다. 원칙은 **좁게** — *"Don't just try to dump a bunch of like random programming wisdom into a skill file. Instead, focus it on a particular theory of what good code is."*(17:15~17:24). 그의 스킬 셋은 자기 PR 리뷰 순서다: **구조**(해법이 문제에 맞나) → **메서드 단위** → **폴리시**(가독성·문서화)(17:27~17:47). 손으로 부르면 [[human-plumbing]]이므로 서브에이전트로 — *"That helps with bias"*(18:08~18:13), 다섯 줄짜리 스킬이 차례로 호출(*"This is not real orchestration"* 18:20).

왜 같은 휴리스틱을 AGENTS.md가 아니라 리뷰에 두나 — *"apply them backwards to a concrete program I've already generated. It's much easier to find violations in a program I've written now than for all possible programs I could generate in the future."*(20:00~20:12) → [[feedforward-feedback-steering]]의 feedback·inferential 칸. ⚠️ 측정 없음 — 리뷰 스킬이 무엇을 얼마나 잡았는지 수치가 없다.

## 리뷰 너머 CI·머지까지 — Gitar (2026-10-14 · [[tech-bridge-gitar-agentic-pr-validation]])

[[gitar|Gitar]](현재 [[sonar|Sonar]])가 업계 목록에 더해진다. 이 페이지의 설계 교훈 둘을 그대로 제품 기능으로 말한다.

- 오탐이 리뷰어를 죽인다 → *"our goal has been to really make this experience as noisefree as possible, both in the way we handle the UX as well as posting issues that are real and really matter."*(04:01~04:12) 목표이고, 오탐률은 미발화다.
- 리뷰 + 수정 융합 → *"automatically loop until all the fish[=] issues have been fixed in your PR and you have a green PR ready to merge."*(05:04~05:11)

범위는 리뷰 밖으로 넓어진다. 머지 차단(*"block merging if there are any unresolved code review findings"* 04:25~04:31), CI 실패 근본 원인 요약과 flaky 탐지(04:31~04:40), 규칙 기반 자동 승인·머지(05:14~05:31)까지 다룬다. 이 페이지의 성공 지표(*"사람이 수락하는가"*)에 해당하는 수치는 내지 않는다. 결합 방향은 [[agent-plus-program-analysis]] 참고.

## 정책 하나당 서브에이전트 하나, stand down까지 루프 — grumpy engineer (2026-10-14 · [[tech-bridge-sentry-stop-prompting-codify-linters]])

[[greg-pstrucha|Greg Pstrucha]]([[sentry|Sentry]])는 linter로 표현할 수 없는 판단(상태 3개짜리 state machine이 작은 PR 하나로 10개로 부푸는 것, 10:55~11:04)을 위해 **저장소 정책**을 먼저 쓴다. 정책 예시는 *"I don't want too many tests. I want stronger tests."*, *"I do not want a code that's too defensive."*, 원치 않는 상태를 타입으로 표현할 수 없게 할 것(11:45~12:15)이다. 그다음 리뷰 스킬을 둔다.

> *"I created a skill that I called grumpy engineer. We call it Garfield internally. And the way it works is it takes all the policies and run sub agents for each of the policies and the sub agent can either give feedback or stand down. And we loop that. (…) we will loop that until the agent stands stands down and says I I'm okay with that. I validate that this is fine. And only then I read the code."* (12:18~12:50)

- 바로 위 Quenneville(구조 → 메서드 → 폴리시 스킬을 차례로)와 같은 계열이다. 차이는 둘이다. 축이 **리뷰 관점이 아니라 정책 단위**이고, **모두 승인할 때까지 반복**한다.
- 사람은 남는다. *"the goal here isn't to remove the code review quite yet (…) but more so to raise the floor"*(13:07~13:15). 성공 지표는 *"how much I'm casting[=cursing?] at the agent"*(12:51~12:55)이고 화자도 정성적이라고 인정한다(13:04~13:07).
- ⚠️ 측정 없음. 정책 수와 루프 횟수 상한, 서브에이전트끼리 상충할 때의 처리는 발화되지 않는다. `en`·ko는 성공 지표를 "delegate/위임"으로 바꾼다.

## 잡음 필터를 따로 학습한다 — Atlassian AI reviewer (2026-10-17 · [[tech-bridge-atlassian-build-your-own-sdlc]])

[[andy-wong|Andy Wong]]([[atlassian|Atlassian]]): *"some of the code review processes (…) provide a little bit too many comments that are not of a high value. So we (…) train a few models ourselves filter those"*(05:35~05:51) → *"around 40% uh human code resolution rate which is rather close to human baseline of 45"*(06:11~06:20). 리뷰어 본체와 별개로 **저가치 댓글을 거르는 모델**을 둔다. "오탐이 리뷰어를 죽인다"는 교훈의 다른 구현이다. 리뷰 맥락은 diff 너머(Jira·Confluence·Slack)까지 넓힌다(04:24~04:43). 기준은 중앙 관리 standards(Markdown)로 둔다.

> ⚠️ "human code resolution rate"의 정의·분모가 발화되지 않는다. en-orig "45"에는 단위도 없다. Cursor의 resolution rate 52%→70%+(위 표)와 **같은 지표인지 알 수 없어 비교하지 않는다**.

## ⚠️ 유보

- **모든 수치가 벤더 발표 또는 화자의 2차 인용**이다(Copilot 6천만, CodeRabbit 1,300만, Cursor 52→70%, 베이징대 44%, 88% vs 35%).
- 화자는 Arize(관측 플랫폼) 소속 — *"I'm not going to give a pitch for Arise here"*(22:13~22:15)라 했지만, 결론(프로덕션이 마지막 리뷰어)은 소속 회사의 시장과 겹친다.
- 한 소스. 다중 패스·기본 의심의 효과를 독립 측정한 소스는 아직 없다.

## 투표하는 AI 리뷰와 사고 PR 시험지 — Anthropic (2026-11-08 · [[tech-bridge-anthropic-code-review-seven-layers]])

해설 전달(Claude Code 팀):

- 모든 PR에 여러 에이전트가 동시에 버그를 찾고, *"다른 에이전트 그룹이 그 지적 하나하나에 투표를 합니다. 충분히 동의를 얻은 지적만 살아남아요."*(02:54~02:57) 사소한 스타일 지적은 버리고 심각도순. 효과: 실질적 리뷰 코멘트를 받는 PR 16% → 54%.
- ⭐ 리뷰어 평가: *"과거에 사고를 냈던 PR에 모아 시험 문제로 만들고 리뷰어가 매일이 시험을 봐요."*(05:19~05:23) — 11-04 Greptile 편의 *사고 PR 데이터셋*과 같은 방향이다.
- 끝없는 루프의 종료 규칙은 [[review-loop-termination]].

## References

- [[tech-bridge-death-of-code-review]] · [[laurie-voss]]
- [[tech-bridge-sentry-stop-prompting-codify-linters]] — 정책별 서브에이전트 루프 grumpy engineer (Greg Pstrucha)
- 관련: [[mergeability-gap]] · [[verification-bottleneck]] · [[generator-evaluator-pattern]] · [[risk-proportional-human-review]] · [[prompt-injection]] · [[cursor]] · [[codex]] · [[code-knowledge-graph]]
- [[tech-bridge-pocock-pr-bottleneck]] — 한 사람이 지은 리뷰 하네스 (Matt Pocock)
- [[tech-bridge-rails-harness-engineering]] — 좁은 리뷰 스킬 셋 (Joël Quenneville)

## 별도 리뷰어 · REVIEW.md · 반복 실수는 지시문으로 — Anthropic 관행과 AI Labs 구현 (2026-11-02 · [[tech-bridge-ai-labs-claude-code-verification-review-loop]])

[[ai-labs|AI Labs]](설명란 근거)가 [[anthropic|Anthropic]] [[claude-code|Claude Code]] 팀의 리뷰 글을 요약한다(⚠️ 2차 전달, 기사 미확인).

- **[Anthropic] 리뷰 질문의 교체**: *"Instead of asking whether someone read the code, they started asking what could go wrong with the change and how to catch it."*(01:33~01:38)
- **[Anthropic] 만든 에이전트 ≠ 리뷰 에이전트**: 만든 쪽은 *"ends up agreeing with itself"*(05:04~05:06) → *"a separate reviewer agent. The reviewer checks every change before a person looks at it."*(05:08~05:14) 효과는 수치 없이 *"far more of their changes get a review that catches something real"*(05:16~05:17). ⚠️ Team · Enterprise 한정, 가벼운 판본 = code review 명령(effort level)이라는 제품 진술은 미확인.
- **[Anthropic → AI Labs] REVIEW.md**: 기사는 규칙 파일을 권하고, 발표자는 그것을 CLAUDE.md에서 링크해 세션마다 로드한다. 내용 — *"what counts as a real failure in the app and how serious each problem is. It should also say what to ignore and how to report the review"*(06:13~06:19). 10-30 Osmani의 *"codify (…) taste in your team's shared like Claude.md, Agents.md"* 와 같은 자리에 **리뷰 전용 파일**이 들어온다.
- ⭐ **[Anthropic] 반복 실수 → 지시문**: *"when the Claude code teams[=team's] reviewer keeps finding the same mistake, they change the instructions Claude reads and Claude stops making it."*(08:18~08:24) **[AI Labs]** `review.md` 하단 *"rules learned over time"* — 놓친 버그 **와 반복 오탐** 둘 다 규칙이 되고, 루프가 한 줄 규칙을 제안해 *"only adds it if you approve"*(08:53~08:55). 10-17 Atlassian의 *잡음 필터를 따로 학습* 과 같은 문제(오탐)를 **사람 승인 한 줄 규칙**으로 푼다.
- **[Anthropic] classifier로 깊이 배분** → [[risk-proportional-human-review]], **루프 종료 세 규칙** → [[review-loop-termination]].

## "move most of the review reading to machines" — Anthropic 수치의 또 다른 전달 (2026-11-03 · [[tech-bridge-rob-shocks-grokbot-manager-coding-agents]])

[[rob-shocks|Rob Shocks]](설명란 근거)가 Anthropic 사례를 한 문단으로 전한다(⚠️ 출처 미발화, 설명란의 Anthropic 코드 리뷰 글은 열어 보지 않았다).

- *"From June to September, their merged pull requests to Claude code more than doubled. And the share that they had to revert fell by more than 40%."*(06:18~06:26) 인용: *"We didn't remove review, but we did move most of the review reading to machines."*(06:33~06:38)
- 이 페이지의 기존 Anthropic 기록(위 11-02 절, 하루 리뷰할 변경 2,500 → 30,000+)과 **범위(Claude Code vs Anthropic 전체)와 배율(2배 vs 12배)이 다르다.** 합치지 않는다. **revert 비율**은 이 위키의 Anthropic 리뷰 이야기에서 처음 나오는 **품질 쪽 지표**다. 다만 분모와 기준은 발화되지 않는다.
- **[Alan Wells 전달]** 3인 팀이 사람 코드 리뷰 없이 PR을 내보내려고 *"stopped all new product work for about 6 weeks just to build all the validation in."*(06:52~06:56) 자동 리뷰로 가는 **선투자 비용**의 사례다(소속 · 출처 미발화).

## 직접 만들면 깨지는 곳 다섯과 처방 — 리뷰 제품 회사의 절차 (2026-11-04 · [[tech-bridge-greptile-daksh-gupta-build-review-agent]])

[[daksh-gupta|Daksh Gupta]](설명란 근거, [[greptile|Greptile]] 공동창업자)가 *"many people think that's actually all it takes to build a review agent."*(01:16~01:19)라는 뼈대(샌드박스 + PR 웹훅 + 프롬프트)에서 출발한다. ⚠️ 벤더 당사자이고 수치는 전부 자사 진술이다.

- **문제 다섯**: 버그 누락 · 맥락 누락 · 비용(⚠️ *"between three and up to $25 per poll[=pull] request"*(02:30~02:33)) · nitpick · 돌릴 때마다 새 지적.
- ⭐ **잡음이 코드를 망가뜨린다** — 이 페이지의 *오탐이 리뷰어를 죽인다* 는 사람이 무시한다는 뜻이었다. 여기서 경로가 하나 더 생긴다: *"they leave comments on GitHub and your coding agent picks them up and resolves them."*(03:08~03:11) *"They're going to look at review comments and just address all of them and you'll end up with extremely painfully defensive code"*(03:12~03:18) 리뷰어와 코딩 에이전트를 닫힌 루프로 연결할수록 잡음의 비용이 커진다는 말이다 → [[review-loop-termination]]
- ⭐ **프롬프트를 고쳐도 나빠졌는지 모른다** — *"when you change a small thing in the prompt, it'll have a weirdly big impact on the number of comments"*(04:29~04:34) *"You don't know the counterfactual."*(04:39~04:40) 이유는 희소성이다: ⚠️ *"only about one out of every thousand pull requests has a genuinely catastrophic bug in it. One every thousand lines of code has a catastrophic bug in it."*(04:57~05:04) ⚠️ PR과 줄, 두 단위가 연달아 나오고 어느 쪽이 측정값인지 미확정이다.
- **처방 순서(발표자)**: 프롬프트(유형별 버그 목록 · nitpick 정의) → 사고 PR 데이터셋([[production-trace-eval-flywheel]]) → 모델 뒤집기([[review-model-inversion]]) → 코드 · 문서 맥락([[context-engine]] · [[agentic-search]]) → 자율 테스트([[agent-visual-qa]]) → 모델별 비용 분배([[model-mixing-economics]]).
- **버그만이 아니다** — *"code can be very very bad even if it's not buggy."*(10:00~10:02) *"your correct code can actually still be quite wrong."*(10:35~10:37) Slack 한두 문장으로 시킨 일이면 리뷰어는 티켓 · 문서 없이 의도를 판단할 수 없다.

> ⚠️ **성공 지표가 이 페이지의 기록과 다르다.** 위 Voss 절은 리뷰 제품들의 성공 지표를 *사람이 수락하는가*로 정리했고 Greptile을 같은 목록에 올렸다. 이 발표는 **사고 PR을 얼마나 잡는가**를 제시하고 수락률은 말하지 않는다. Greptile의 실제 내부 지표는 확인하지 않았다. 사고 PR 재생은 **재현율 쪽**만 재고, nitpick을 줄였는지(정밀도 쪽)를 어떻게 재는지는 말하지 않는다.

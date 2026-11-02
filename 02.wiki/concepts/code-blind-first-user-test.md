---
title: "코드를 못 보는 첫 사용자 테스트 — 빌드를 모르는 에이전트에게 앱을 쓰게 한다 (Code-Blind First-User Test)"
type: concept
category: technique
tags: [first-time-user, fresh-context, user-testing, dogfooding, hooks, subagents, sandbox-database, claude-code, ai-labs, anthropic]
aliases: [first-time user test, first-time user skill, 첫 사용자 테스트, 처음 쓰는 사용자처럼, fresh agent user test, code-blind agent, 코드 읽기 차단 에이전트]
related: [agent-change-evidence, agent-verification-skill, three-level-agent-review, generator-evaluator-pattern, hook-enforced-workflow, action-reversibility, automated-code-review]
first-seen: tech-bridge-ai-labs-claude-code-verification-review-loop
sources: [tech-bridge-ai-labs-claude-code-verification-review-loop]
created: 2026-11-02
updated: 2026-11-02
---

# 코드를 못 보는 첫 사용자 테스트

**모든 eval이 통과해도 새는 문제를 찾기 위해, 앱이 만들어지는 과정을 본 적 없고 코드를 읽는 것이 막힌 새 에이전트에게 실제로 띄운 앱을 처음 쓰는 고객처럼 쓰게 하고, 막히는 곳을 보고받는 기법.** [[tech-bridge-ai-labs-claude-code-verification-review-loop]]에서 [[ai-labs|AI Labs]]가 [[anthropic|Anthropic]] [[claude-code|Claude Code]] 팀의 dogfooding을 출발점으로 제안한 구현이다.

## 출발점 — [Anthropic] 직접 사용 (발표자 전달)

- *"even when the loop finishes and every eval passes, some mistakes will still get through. So, you need two more things, which are a way to find those mistakes and a way to undo them fast."*(11:30~11:40)
- *"To find the mistakes, they use the product themselves every day, so they often spot a problem before their customers do."*(11:46~11:52)

## 왜 새 에이전트인가 — [AI Labs]

- *"But you already know how the feature works, so you'll miss some things. To catch those, you can send a fresh agent that never saw the app being built to use the live app like a first-time customer."*(11:57~12:06)
- 만든 사람(사람이든 builder 에이전트든)은 기능의 의도를 알기 때문에 그 의도대로만 쓴다. 같은 영상의 리뷰어 논리 — 만든 에이전트는 *"ends up agreeing with itself"*(05:04~05:06) — 를 **코드 리뷰에서 사용 경험으로** 옮긴 것이다.

## 구성 — [AI Labs]

| 장치 | 목적 | en-orig |
|---|---|---|
| 코드 읽기 차단 서브에이전트 | 앱이 무엇인지 모르게 | *"It should use sub agents that are blocked from reading the app's code, so they don't know what the app is about."*(12:12~12:17) |
| 임시 데이터베이스 | 실제 데이터 보호 | *"It also gives the test a temporary database, so it doesn't touch your real data"*(12:28~12:33) |
| 차단 훅 + 터미널 우회 차단 | 지시가 아니라 강제 | *"The agent would normally get around that block with terminal commands. So, the hook stops it from reading the code that way, too."*(12:37~12:42) |
| 실행 · 보고 | 기능 단위 | 기능을 지정하면 앱을 열고 *"an agent that knows nothing about how the app was built"*(12:50~12:54)을 띄운 뒤, 발견 사항과 *"suggests fixes you can apply"*(13:00~13:00) |

목표: *"go through the app the way a first-time user would and find every place where someone might get stuck."*(12:19~12:23)

> ⭐ 터미널 우회 차단은 [[hook-enforced-workflow]]의 실례다 — "코드를 읽지 마라"는 지시는 에이전트가 `cat` 같은 셸 명령으로 넘어간다는 관찰(발표자 진술)이 훅을 정당화한다.

## 이 위키에서의 자리

- [[three-level-agent-review]](10-20)의 *맥락 없는 검토자*(*"no history, no drafts, and no conclusions to agree with"*)가 **문서**를 읽는 쪽이었다면, 여기서는 **입력을 코드에서 화면으로** 바꾸고 차단을 훅으로 강제한다.
- [[agent-change-evidence]]의 *"similar to a real user"*(10-30 Osmani, Anthropic 1인칭)는 builder가 자기 변경을 사용자처럼 시험하는 것이었다. 이 기법은 **시험자를 builder와 분리**한다.
- 이 단계 뒤에 같은 영상은 *빨리 되돌리기*를 둔다 — [[action-reversibility]]: *"The Claude code team can undo almost anything they release in minutes, and that's what lets them read less."*(11:40~11:46)

## ⚠️ 유보

- AI Labs의 한 번 시연이다. 무엇을 찾았는지 구체적 결과 · 오탐률 · 비용은 나오지 않는다.
- "코드를 못 보면 무엇을 하는 앱인지 모른다"는 전제는 UI가 스스로 설명적이어야 한다는 가정을 품는다 — 라벨 · 문서 없는 내부 도구에서는 소음이 많을 수 있다(위키 해석).
- Anthropic 쪽은 *매일 직접 쓴다* 까지이고, 코드 차단 에이전트는 AI Labs의 제안이다.

## References

- [[tech-bridge-ai-labs-claude-code-verification-review-loop]] §10
- [[three-level-agent-review]] · [[agent-change-evidence]] · [[hook-enforced-workflow]]

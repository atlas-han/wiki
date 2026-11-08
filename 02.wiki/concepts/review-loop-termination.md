---
title: "리뷰 루프 종료 조건 — builder와 reviewer는 언제 멈추는가 (Review Loop Termination)"
type: concept
category: pattern
tags: [review-loop, termination, generator-evaluator, automated-code-review, agent-loops, token-cost, claude-code, anthropic, ai-labs]
aliases: [review loop termination, 리뷰 루프 종료, 끝나지 않는 루프, 무한 리뷰 루프, 세 라운드 규칙, three-round rule, delta-only review]
related: [generator-evaluator-pattern, automated-code-review, three-level-agent-review, verification-cost-asymmetry, true-cost-to-perfect-answer, agent-loop-size, risk-proportional-human-review]
first-seen: tech-bridge-ai-labs-claude-code-verification-review-loop
sources: [tech-bridge-ai-labs-claude-code-verification-review-loop, tech-bridge-greptile-daksh-gupta-build-review-agent, tech-bridge-anthropic-code-review-seven-layers]
created: 2026-11-02
updated: 2026-11-08
---

# 리뷰 루프 종료 조건

**builder 에이전트와 reviewer 에이전트를 돌리는 루프는 스스로 멈추지 않는다. reviewer는 이미 있던 문제를 하나씩 다시 찾아내고, builder는 그 지점만 고친다. 그래서 루프에는 "모든 검사가 통과하면 멈춘다" 말고 별도의 종료 규칙이 필요하다** — 라운드 상한과 접근 재설계, 변경분만 다시 보는 리뷰, 문제 종류를 붙인 보고. [[tech-bridge-ai-labs-claude-code-verification-review-loop]]에서 [[ai-labs|AI Labs]]가 [[anthropic|Anthropic]] [[claude-code|Claude Code]] 팀의 사례를 전달하고(⚠️ 2차 전달, 기사 원문 미확인) 자기 구현 수치를 붙였다.

> *"The builder and the reviewer agents don't know when to stop, so they can keep going back and forth trying to find and fix issues."*(09:57~10:04)

## 실패 사례 — [Anthropic] (발표자 전달)

- *"The Claude code team once had a change that went back and forth more than 50 times like this. The agents kept going until someone manually stopped the loop."*(10:04~10:12)
- 원인 진단: *"When the team looked at what the reviewer kept reporting, about 59% of it had been there since the very first round. So, the reviewer was mostly finding the old problems again and again."*(10:12~10:22)
- 비용: *"on your plan, every one of those rounds uses up your limits."*(10:22~10:24) — ⚠️ 기사에 대한 반응이 *"it only works if you have unlimited tokens"*(10:28~10:30)였다는 진술은 출처 미발화.

## 세 규칙 — [Anthropic] (발표자 전달)

| 규칙 | 무엇을 막나 | en-orig |
|---|---|---|
| 1. **3라운드 후 재설계** | 같은 방식으로 더 고치는 것 | *"after three rounds, the reviewer stops listing more problems and tells the builder to rethink how it's building the feature."*(10:33~10:39) · *"If the feature is still failing after three rounds of fixes, more work in the same way wouldn't get it there."*(10:39~10:44) |
| 2. **변경분만, 재보고 금지** | 전체를 다시 훑어 옛 문제를 하나씩 꺼내는 것 | *"after the first round, the reviewer only checks what the last fixes changed and doesn't report anything it has already reported."*(10:46~10:53) |
| 3. **문제 종류 명시** | 지적된 한 곳만 고치는 것 | *"when the reviewer finds a problem, it says what kind of problem it is. That way, the builder fixes that kind of problem everywhere it shows up and not only in the one spot the reviewer found."*(10:58~11:08) |

효과: *"With those three rules in place, more of their changes passed review on the very first try."*(11:08~11:12) — ⚠️ 수치 없음.

> ⚠️ 발표자는 세 규칙을 *"So, the team added three rules"*(10:30~10:32)로 토큰 불만 바로 뒤에 놓는다. **불만 때문에 규칙이 추가됐다는 인과는 발표자 화법**이고, 세 규칙이 기사에 처음부터 있었는지는 확인하지 않았다.

## 변형 — [AI Labs] 5라운드 · 2라운드 정체

- *"Our review loop works the same way, but each of our rounds does more work. It builds the feature and checks every eval in the browser, and then it reviews the code. That's why we set it to stop after five rounds instead of three."*(11:12~11:24)
- 정체 감지: *"The loop can also stop before it gets to five when the same problem is still there after two rounds of fixes."*(11:24~11:30)
- 기본 종료 조건은 *"all all evals pass and the review doesn't find anything new"*(08:03~08:07)이고, `state.md`가 라운드와 남은 실패를 기록한다(07:37~07:44). 같은 문제의 재등장은 앞 라운드와 대조해 `review.md`의 학습 규칙 후보가 된다(08:44~08:55).

> ⚠️ 상한 5의 근거는 "라운드당 일이 더 많다"는 한 문장뿐이고, 측정 · 실패 사례는 없다.

## 이 위키에서의 자리

- [[generator-evaluator-pattern]]의 **종료 쪽 공백**을 메운다. 이 위키에서 루프 상한은 플랫폼 파라미터(Managed Agents Outcome의 *max iterations*, 10-19)로만, 혹은 *모두 stand down할 때까지*(10-14 [[automated-code-review]]의 grumpy engineer, 상한 미발화)로만 나왔다. 여기서는 상한이 **무엇을 할지**(재설계 지시)와 **reviewer가 무엇을 보지 말지**(이미 본 것)가 함께 나온다.
- 규칙 2는 reviewer의 *fresh context*(같은 판단에 동의하지 않게 하려는 장치, [[three-level-agent-review]]의 *"brand new reviewers"*)와 **긴장**한다 — 맥락을 지우면 이미 보고한 것을 모른다. 이 영상은 둘을 어떻게 함께 두는지(보고 이력을 state 파일로 넘기는지 등) 말하지 않는다.
- 규칙 3(종류로 보고 → 모든 곳을 고친다)은 같은 영상의 *반복 실수는 지시문으로*(→ [[automated-code-review]] 2026-11-02 절)와 같은 방향이다: **지적을 인스턴스에서 클래스로 올린다.**
- 비용 쪽에서는 [[verification-cost-asymmetry]] · [[true-cost-to-perfect-answer]]의 사례 — 검증 루프도 상한이 없으면 생성보다 비싸진다.

## ⚠️ 유보

- Anthropic 쪽 수치(50회+, 59%)와 세 규칙은 발표자가 기사를 요약한 것이다. 기사(`claude.dev/blog/solving-code-review-at-anthropic`)는 열어 보지 않았다.
- 효과는 *"more of their changes passed review on the very first try"* 뿐, 비율 · 비용 절감 수치 없음.
- AI Labs 판본은 한 번의 시연.

## 한국어 해설판 — 세 라운드 규칙과 결과 수치 (2026-11-08 · [[tech-bridge-anthropic-code-review-seven-layers]])

같은 Anthropic 글을 Tech Bridge가 한국어로 다시 정리했다(2차 전달, 블로그 미열람). AI Labs 편에 없던 내용:

- 원인 설명: 사람은 닛을 1초 만에 넘기지만 *"AI 작성은[=작성자는] 그걸 그대로 고칩니다."*(04:46) → 또 커밋, 또 리뷰.
- 규칙: *"세 번 돌면 리뷰어가 접근 방식부터 다시 생각해 보라고 하고 그다음부턴 바뀐 부부만[=부분만] 다시 봅니다."*(04:51~04:58) + 버그 종류를 짚기 + 반복 금지.
- ⭐ 결과(이 위키 첫 기록): 한 번에 통과하는 PR 65% → 78%, 다섯 번 이상 도는 PR 8.9% → 1.5%(05:08~05:14).
- 리뷰어 개선 루프: 과거 사고 PR을 시험지로 매일 채점하고, 프롬프트 · 도구 · 모델 변경은 점수가 오를 때만 남긴다.
- ⚠️ 59% · 50회는 AI Labs 편과 일치한다. 새 수치는 대조하지 않았다.

## References

- [[tech-bridge-ai-labs-claude-code-verification-review-loop]] §6 · §9
- [[generator-evaluator-pattern]] · [[automated-code-review]] · [[three-level-agent-review]]

## 돌릴 때마다 새 버그 — "fractally infinite" (2026-11-04 · [[tech-bridge-greptile-daksh-gupta-build-review-agent]])

[[daksh-gupta|Daksh Gupta]](설명란 근거, [[greptile|Greptile]])는 끝나지 않는 이유를 다르게 설명한다: *"every time you run a review agent on the same poll[=pull] request, you will somehow find new bugs"*(03:26~03:29) · *"bugs will appear to be fractally infinite."*(03:35~03:37)

- > ⚠️ **Contradiction(약): 옛 문제인가, 새 문제인가.** 위 Anthropic 기록(AI Labs 전달)은 reviewer 보고의 약 59%가 첫 라운드부터 있던 것이라 했고, 여기서는 매번 새것을 찾는다고 한다. 저쪽은 수정이 낀 builder-reviewer 라운드이고 여기는 같은 PR의 재실행이라 조건이 다르다. 양쪽 다 측정 방법은 확인하지 않았다.
- **루프의 다른 쪽 비용** — *"coding agents not discerning."*(03:11~03:12) 지적을 전부 반영하면 *"extremely painfully defensive code"*(03:15~03:18)가 남는다. 이 페이지의 규칙들은 라운드 수와 토큰을 막는다. 이 발화는 **멈춘 뒤 코드에 남는 흔적**을 말한다.
- 발표자의 처방은 종료 규칙이 아니라 입구 쪽이다(버그 유형 지정 · nitpick 금지, 03:51~04:17). 라운드 상한은 말하지 않는다.

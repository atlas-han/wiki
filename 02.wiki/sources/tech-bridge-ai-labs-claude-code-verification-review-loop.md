---
title: "Tech Bridge — Claude Code, 완료했다고 끝이 아니다 (AI Labs): Anthropic 코드 리뷰 방식 해설과 eval · 리뷰 루프 · 첫 사용자 테스트 구현"
type: source
tags: [claude-code, anthropic, automated-code-review, verification, evals, review-md, claude-md, hooks, agent-skills, subagents, generator-evaluator, risk-classifier, review-loop-termination, first-time-user-test, git-rollback, dogfooding, ai-labs, vendor-claim, video]
source-url: https://www.youtube.com/watch?v=IGTdL4IPLq8
source-type: video
author: Tech Bridge (번역 재배포, 내레이션 없음) · 원 제작자 [[ai-labs]](설명란 근거 — 발화에 이름 없음, 1인칭 복수 "we") · 발표자 개인 미상 · 원본 영상 링크 · 녹화일 미상
date-published: 2026-11-01
ingested: 2026-11-02
created: 2026-11-02
updated: 2026-11-02
---

# Tech Bridge — Claude Code, 완료했다고 끝이 아니다 (AI Labs)

[[tech-bridge|Tech Bridge]]의 **14:00 해설 · 화면 시연 영상, 공식 챕터 11, 내레이션 없음.** 오디오는 `English (US) original (default)` + 더빙 7개 언어이고 **한국어 트랙 · `ko-orig`가 없다** — 10-27 Voss 편 이후 이어지는 영어 원본 오디오만 있는 구성이라 **인용은 en-orig로만** 한다. 제목의 "[한글자막]"과 달리 수동 자막은 없다. 00:00~00:22(첫 챕터 "소개" 거의 전체)는 무캡션이다. `upload_date` 20261101(UTC)은 KST로 **11-02 06:45**다. raw: `01.raw/articles/2026-11-01_Claude Code 완료했다고 끝이 아니다 - 검증과 리뷰 루프 만들기.md`.

[[ai-labs|AI Labs]]가 [[anthropic|Anthropic]] [[claude-code|Claude Code]] 팀의 코드 리뷰 글(설명란 링크, ⚠️ 열어 보지 않음)을 단계별로 요약하고, 각 단계를 **Claude에게 만들게 한 자기 스킬**로 옮겨 보인다. 테제(발표자):

> **모델이 좋아질수록 리뷰할 양이 늘어난다. 리뷰는 건너뛸 수 없으니 "누가 하느냐"가 문제다 — 에이전트가 증거를 내게 하고, 만든 에이전트와 다른 리뷰어를 두고, 위험에 비례해 깊이를 정하고, 루프에 종료 규칙을 두고, 그래도 새는 것은 빨리 찾고 빨리 되돌린다.**

> *"As the models get better, reviewing what your agent builds matters even more than it ever did before."*(00:22~00:27) · *"So, review is a step you can't skip, and the real question is who does it?"*(01:26~01:28)

### 두 층을 나눠 읽는다

설명란: *"AI Labs가 제안한 구현과 앤트로픽 팀의 실제 프로세스는 구분해 설명합니다."* 이 페이지도 각 항목에 **[Anthropic]**(발표자가 Claude Code 팀 · Anthropic 기사를 전달) / **[AI Labs]**(발표자 자기 구현 · 시청자에게 권하는 프롬프트)를 붙인다.

| 단계 | [Anthropic] 팀 관행 (발표자 전달) | [AI Labs] 구현 |
|---|---|---|
| 1. 구현 전 검증 기준 | 완료 대신 증거(테스트 · 디자인 대비 스크린샷), *"a list of checks"* | write-eval 스킬: 기능별 `eval.md` · 목업 · 사람 승인 · 완료 차단 훅 |
| 2. 별도 리뷰어 | 만든 에이전트와 다른 리뷰어(Team · Enterprise), 가벼운 판본 = code review 명령 | — (명령을 그대로 씀) |
| 3. 리뷰 규칙 | `REVIEW.md`에 규칙을 쓰라는 기사 권고 | `review.md`를 CLAUDE.md에 링크해 세션마다 로드 |
| 4. 반복 루프 | — | review-loop 스킬: orchestrator · builder · verifier · reviewer, `state.md` |
| 5. 반복 실수 | 같은 실수를 계속 찾으면 지시문을 고친다 | `review.md` 하단 *"rules learned over time"*, 승인 시 한 줄 규칙 추가 |
| 6. 위험 비례 | classifier 에이전트가 모든 변경을 분류 | 위험 등급 스킬 → 높을수록 엄격한 eval (3등급 기준은 경계 불분명) |
| 7. 루프 종료 | 50회+ 왕복 · 59% 재보고 → 세 규칙 | 5라운드 상한 · 같은 문제 2라운드 정체 시 종료 |
| 8. 새는 것 찾기 | 매일 직접 사용(dogfooding) | 코드를 못 읽는 first-time user 에이전트 |
| 9. 되돌리기 | *"undo almost anything they release in minutes"* | fix-a-bug 스킬 · 기능별 Git 브랜치 · 작동 버전 저장 |

> ⚠️ **원 제작자 귀속은 설명란 근거다.** 발화에 "AI Labs"가 없고 태그에도 없다. 발화로 확인되는 것은 **1인칭 복수 채널 화법** — *"We've shown many ways to give Claude evals in our earlier videos."*(02:53~02:55), *"we turned that into a skill"*(02:59~03:00). 위키의 이전 AI Labs 두 편([[tech-bridge-six-agent-skills]] · [[tech-bridge-graft-code-knowledge-graph]])과 같은 화법 · 같은 미해결(개인 이름 없음)이다.
>
> ⚠️ **Anthropic 쪽은 전부 2차 전달이다.** 숫자 · 관행 · 제품 동작(Team · Enterprise 한정, effort level, REVIEW.md 로딩)은 발표자가 기사를 요약한 것이고, 위키는 설명란 링크(`claude.dev/blog/solving-code-review-at-anthropic` · `code.claude.com/docs`)를 열지 않았다.

## 1. 소개 (00:00~00:23)

en-orig에 발화가 없다(무캡션, 첫 큐 00:22.9). 이 챕터의 내용은 쓰지 않는다.

## 2. 왜 검토가 병목이 될까 (00:23~02:09)

- 모델이 몇 시간씩 혼자 기능 목록을 만든다 → **[Anthropic]** *"The Claude code team sees that as a problem because more features being built faster also means there's way more to review."*(00:36~00:42)
- ⭐ **[Anthropic]** *"Across Anthropic, the number of changes to review every day went from about 2,500 to over 30,000 in just 4 months."*(00:42~00:49)
- **[Anthropic]** 리뷰를 서두르면: *"instead of saving time, you end up spending twice as much time as you would on the review itself, first checking the changes and then fixing the bugs that slip through."*(01:13~01:20)
- ⭐ **[Anthropic] 질문을 바꿨다**: *"Instead of asking whether someone read the code, they started asking what could go wrong with the change and how to catch it."*(01:33~01:38)
- **[Anthropic] 검사 시점을 바꿨다**: *"Now, they happen while Claude is building instead of waiting until the end."*(01:46~01:49) — 발표자는 이것이 이미 Claude Code 사용 경험에 보인다고 덧붙인다(01:49~01:56).

> ⚠️ **10-30 Osmani 편과 숫자의 단위가 다르다.** [[tech-bridge-anthropic-30k-merges-verification]]에서는 진행 쪽이 *"30,000 code changes every single day"* 를 **merging**으로, Addy가 *"2,500 changes all the way back in May"* 를 기간 단위 없이 말했다. 여기서는 **"리뷰할 변경 하루"** 와 **"4개월"** 이 붙는다. 같은 Anthropic 수치의 다른 전달로 보이지만(추정), 원 기사와 대조하지 않았다.

→ [[verification-bottleneck]]

## 3. 구현 전에 검증 기준 만들기 (02:09~04:55)

- **[Anthropic]** 빌드 중 검사는 작다. 그래서 더 깊은 검사가 팀 프로세스의 첫 단계: *"Before a change goes anywhere, they ask Claude to run something that proves it works and to show them the result instead of just saying it's done. That can be the app's tests or a screenshot compared with the design."*(02:23~02:32)
- **[Anthropic]** [[boris-cherny|Boris Cherny]] 전달: *"Boris Cherny, who is the creator of Claude code, says that the best way to get Claude to work well is to give it away[=a way] to prove it did the work right."*(02:32~02:41) — ⚠️ 발표자의 간접 인용, 출처 미발화.
- **[Anthropic]** *"the team's advice is to give your agent a list of checks it can run."*(02:41~02:45) 발표자 정의: eval은 *"a fixed test that tells you whether the work is done. It has to be strict enough that bad work fails it."*(02:47~02:53)
- ⭐ **[AI Labs] write-eval 스킬** — *"Claude code's team mentions their own way to set up these checks, and we turned that into a skill."*(02:57~03:00)
  - 데모 앱에 `specs` 폴더 → 기능별 폴더 → 요구사항 파일(*"rd.md"*, 03:10, ASR — PRD.md 등 미확정). 스킬이 기능마다 `eval.md`를 쓴다 — *"the actual method the agent will use to check its work"*(03:21~03:25).
  - **목업 먼저**: 디자인이 있으면 앱에 바로 짓지 않고 단순한 웹 페이지(mock-up)로 만든 뒤 그것을 기준으로 삼는다 — *"we can quickly see how the feature will look without wasting too many tokens."*(03:38~03:42)
  - **사람 승인 게이트**: *"once it has written the evals, it needs to get them reviewed by you, and without that review, it shouldn't build anything."*(03:44~03:50)
  - **완료 차단 훅**: *"create a hook that makes sure agent doesn't mark the task as done until the evals have passed."*(03:50~03:56)
  - 결과물: `.claude` 폴더의 스킬 + eval 템플릿. 실행하면 요구사항 · eval을 쓰고, 훅으로 점검하며 여러 번 왕복, 목업 생성, 상태 *draft → in review*(04:24~04:29), *"it tells you every decision it made on its own"*(04:29~04:31), 다른 화면 상태 · 모바일 레이아웃까지 보여 준다. 사람이 `eval.md`와 목업을 둘 다 보고 승인하면 *"reviewed and ready for building"*(04:53~04:54).

→ [[agent-verification-skill]] · [[verifiable-goals]] · [[hook-enforced-workflow]] · [[skill-evals]]

## 4. 별도 리뷰어의 역할 (04:55~05:41)

- ⭐ *"the agent that reviews it shouldn't be the same one that built it because that agent made every decision in the change and ends up agreeing with itself."*(04:58~05:06)
- **[Anthropic]** *"the Claude code team's second check is a separate reviewer agent. The reviewer checks every change before a person looks at it."*(05:06~05:14) 효과: *"far more of their changes get a review that catches something real."*(05:16~05:17, 수치 없음)
- **[Anthropic] 제품 쪽(발표자 진술)**: *"That review agent is only available on the team and enterprise plans for now, but a lighter version already comes with Claude code as the code review command."*(05:17~05:26) — 별도 에이전트가 변경 전체를 읽고 *"the mistakes that would break your app"*(05:30~05:32)을 보고한다. effort level: *"At low effort, it only reports what it's most sure about and the higher levels check more of your app."*(05:35~05:41)

> ⚠️ 플랜 한정 · 명령 이름 · effort 동작은 **위키가 확인하지 않은 제품 진술**이다. 명령 문자열(`/…`)은 발화되지 않는다.

→ [[automated-code-review]] · [[generator-evaluator-pattern]]

## 5. REVIEW.md로 검토 규칙 지정 (05:41~06:35)

- **[Anthropic]** *"Anthropic's article on this says to write your rules in a file called review.md."*(05:43~05:47)
- **[AI Labs] 로딩 문제와 우회**: *"By default, this file isn't read unless you ask Claude to do so."*(05:47~05:52, ⚠️ 발표자 진술) → 규칙을 CLAUDE.md에 직접 넣지 말고 별도 파일로 두고 **CLAUDE.md에서 링크**하면 새 세션마다 함께 로드되어 code review 명령도 읽는다(05:57~06:10 · 06:30~06:34).
- 내용: *"what counts as a real failure in the app and how serious each problem is. It should also say what to ignore and how to report the review along with all the ways you want the app tested."*(06:13~06:20)

> ⚠️ "Anthropic 기사는 REVIEW.md를 권한다"와 "기본으로는 안 읽힌다"는 **다른 층의 진술**이다 — 앞은 기사 전달, 뒤는 발표자의 로컬 사용 관찰(혹은 해석). 기사가 REVIEW.md를 어느 리뷰 제품(Team · Enterprise 리뷰어)용으로 말했는지는 이 영상만으로 알 수 없다.

→ [[automated-code-review]] · [[llm-coding-guidelines]]

## 6. 구현·검증·리뷰 반복하기 (06:35~08:08) — [AI Labs]

- review-loop 스킬 프롬프트: 기능을 빌드하고 `eval.md`로 확인, *"It uses sub-agents with fresh context windows. This way, they don't have the same context as the main agent, so they don't just agree with what the main agent did. It should keep looping until all the evals have passed."*(06:44~06:56)
- 구조 — 메인 에이전트 = **orchestrator**(루프 실행, 에이전트마다 별도 컨텍스트), **builder**(요구사항 문서로 빌드), **verifier**(eval마다 passed/failed), **reviewer**(*"find anything the evals missed and it uses the rules in your review.md"* 07:26~07:30)(07:02~07:30).
- 실행: `state.md`가 라운드와 남은 실패를 추적(07:37~07:44), write-eval 훅이 builder 중 *"calling the feature done too early"*(07:51~07:53)를 막고, 스스로 못 내리는 결정에서는 progress report를 보여 주고 묻는다(07:58~08:03).
- 종료: *"The loop only stops when all all evals pass and the review doesn't find anything new"*(08:03~08:07).

→ [[generator-evaluator-pattern]] · [[three-level-agent-review]]

## 7. 반복되는 실수에서 배우기 (08:08~08:55)

- 문제: *"Claude doesn't remember mistakes from earlier sessions. So, it makes the same mistake on the next feature"*(08:11~08:14)
- ⭐ **[Anthropic]** *"when the Claude code teams[=team's] reviewer keeps finding the same mistake, they change the instructions Claude reads and Claude stops making it."*(08:18~08:24)
- **[AI Labs]** `review.md` 하단 *"a section for rules learned over time"*(08:28~08:30). 놓친 버그가 나중에 드러나면 규칙 추가, **오탐을 계속 내도 규칙 추가**(08:32~08:42). review-loop이 같은 문제의 재등장을 앞 라운드와 대조하고 *"it suggests a one-line rule for that part and only adds it if you approve."*(08:51~08:55)

→ [[automated-code-review]] · [[shift-left-interventions]]

## 8. 위험도에 맞춰 검토하기 (08:55~09:53)

- **[Anthropic]** *"a change needs to get checked harder when a mistake in that feature could do more damage."*(09:00~09:05) — 사람이 고르지 않는다: *"They have an agent that sorts every change for them, which they call a classifier."*(09:09~09:13)
- ⚠️ **[경계 불분명]** 한 질문으로 분류 — *"what happens to a customer if a feature breaks"*(09:17~09:18): 보기만 틀리면 **low**, 기능이 멈추지만 잃는 것이 없으면 **medium**(나중에 고칠 수 있다), 돈을 잃거나 잠기거나 남의 데이터를 보게 되면 **high** — *"You can't take those back once they happen."*(09:34~09:36) 이 3등급은 *"You can sort your own changes as well"*(09:13~09:15) 뒤에 나와 Anthropic classifier의 기준인지 발표자 제안인지 갈리지 않는다.
- **[AI Labs]** 그 질문을 등급 스킬로(ASR *"scale"*) 만들고, 빌드 전에 돌려 등급을 write-eval 스킬에 넘긴다 — *"a high-risk feature gets stricter evals than a low-risk one."*(09:49~09:53)

→ [[risk-proportional-human-review]] · [[action-reversibility]] · [[transcript-classifier]]

## 9. 끝나지 않는 루프 막기 (09:53~11:33)

- 문제: *"The builder and the reviewer agents don't know when to stop"*(09:57~10:00)
- ⭐ **[Anthropic]** *"The Claude code team once had a change that went back and forth more than 50 times like this. The agents kept going until someone manually stopped the loop."*(10:04~10:12) · *"about 59% of it had been there since the very first round."*(10:15~10:18)
- 비용: *"on your plan, every one of those rounds uses up your limits."*(10:22~10:24) · ⚠️ *"People's main complaint about Anthropic's article was that it only works if you have unlimited tokens."*(10:26~10:30) — 반응의 출처 미발화.
- ⭐ **[Anthropic] 세 규칙**(10:30~11:08):
  1. *"after three rounds, the reviewer stops listing more problems and tells the builder to rethink how it's building the feature."*(10:33~10:39)
  2. *"after the first round, the reviewer only checks what the last fixes changed and doesn't report anything it has already reported."*(10:46~10:53)
  3. *"when the reviewer finds a problem, it says what kind of problem it is. That way, the builder fixes that kind of problem everywhere it shows up"*(10:58~11:06)
  - 효과: *"more of their changes passed review on the very first try."*(11:10~11:12, 수치 없음)
- **[AI Labs]** *"each of our rounds does more work. It builds the feature and checks every eval in the browser, and then it reviews the code. That's why we set it to stop after five rounds instead of three."*(11:14~11:24) + *"when the same problem is still there after two rounds of fixes"*(11:26~11:30) 조기 종료.

> ⚠️ "불만 → 세 규칙 추가"의 인과는 발표자 화법이다(*"So, the team added three rules"*). 세 규칙이 기사 원문에 처음부터 있었는지 모른다.

→ [[review-loop-termination]](신규) · [[generator-evaluator-pattern]]

## 10. 처음 쓰는 사용자처럼 시험하기 (11:33~13:03)

- ⭐ **[Anthropic]** *"The Claude code team can undo almost anything they release in minutes, and that's what lets them read less."*(11:40~11:46) · *"they use the product themselves every day, so they often spot a problem before their customers do."*(11:48~11:52)
- **[AI Labs]** 내가 쓰면 이미 알아서 놓친다(11:57~12:02) → *"you can send a fresh agent that never saw the app being built to use the live app like a first-time customer."*(12:00~12:06)
  - 프롬프트: *"It should use sub agents that are blocked from reading the app's code, so they don't know what the app is about."*(12:12~12:17), 막힐 만한 곳을 전부 찾는다.
  - 생성물: first-time user 스킬 + 에이전트, **임시 데이터베이스**(*"so it doesn't touch your real data"* 12:30~12:35), 코드 읽기 차단 훅 — *"The agent would normally get around that block with terminal commands. So, the hook stops it from reading the code that way, too."*(12:37~12:42)
  - 실행: 기능을 지정하면 앱을 열고 *"an agent that knows nothing about how the app was built"*(12:50~12:54)을 띄워 기다린 뒤 발견 사항과 수정 제안을 보고한다.

→ [[code-blind-first-user-test]](신규) · [[hook-enforced-workflow]] · [[agent-change-evidence]]

## 11. 문제 재현과 변경 되돌리기 (13:03~14:00) — [AI Labs]

- *"Finding the mistakes is one half and the other half is undoing the changes that caused them."*(13:02~13:06) Git: 기능마다 브랜치(13:10~13:16).
- fix-a-bug 스킬: *"It tries to make the bug happen again by going through the same steps and then checks whether it's[=its] guess about the cause was right."*(13:32~13:37) → 보고 · 수정.
- CLAUDE.md에 *"use Git and make its own branch for each feature. It should also save every version that works."*(13:43~13:50) → 저장된 버전을 거슬러 원인 변경을 찾고 롤백(13:51~13:57). 영상은 여기서 끝난다.

→ [[action-reversibility]]

## 등장 개체

- 조직 · 제작자: [[ai-labs]](설명란 근거, 세 번째 소스) · [[anthropic]] · [[tech-bridge]]
- 인물: [[boris-cherny]](발표자 간접 인용 한 마디)
- 제품: [[claude-code]](code review 명령 · Team/Enterprise 리뷰어 · 훅 · 스킬 · CLAUDE.md) · Git(페이지 없음)
- 개념: [[review-loop-termination]](신규) · [[code-blind-first-user-test]](신규) · [[automated-code-review]] · [[verification-bottleneck]] · [[agent-verification-skill]] · [[generator-evaluator-pattern]] · [[risk-proportional-human-review]] · [[hook-enforced-workflow]] · [[action-reversibility]] · [[verifiable-goals]] · [[three-level-agent-review]]

## 이 위키에서의 좌표

- **Anthropic 코드 리뷰 이야기의 세 번째 전달.** 09-03 [[tech-bridge-claude-code-team-workflow]](Claude Code 팀 대담) → 10-30 [[tech-bridge-anthropic-30k-merges-verification]](Addy Osmani, 내부자 1인칭) → 이 편(외부 제작자가 기사를 요약). 겹치는 것: *사람처럼 시험한 증거*, 훅, 규칙 파일(Osmani의 *"Claude.md, Agents.md"* ↔ 여기의 `REVIEW.md`). 새로 붙는 것: **별도 리뷰어 · classifier · 루프 종료 세 규칙 · 되돌리기가 읽기를 줄인다.**
- 10-14 [[tech-bridge-sentry-stop-prompting-codify-linters]]의 grumpy engineer는 *"loop that until the agent stands down"* — 상한이 발화되지 않았다. 이 편은 그 루프가 **50회+ 왕복으로 터진 사례와 처방**을 준다 → [[review-loop-termination]].
- 10-20 [[tech-bridge-three-level-agent-review]]의 *맥락 없는 검토자*가 문서 검토 쪽이었다면, 여기서는 **코드를 못 읽게 막은 사용자 에이전트**로 제품 쪽에 온다 → [[code-blind-first-user-test]].

## ⚠️ 유보

- 원 제작자 AI Labs는 설명란 근거, 발표자 개인 미상, 원본 링크 · 녹화일 없음. 00:00~00:22 무캡션.
- Anthropic 쪽 수치(2,500 → 30,000+ · 2배 시간 · 50회+ · 59%)와 제품 진술(Team · Enterprise · effort level · REVIEW.md 로딩)은 발표자 전달이고 기사와 대조하지 않았다.
- 위험 3등급의 귀속, "불만 → 세 규칙" 인과는 불분명하다.
- AI Labs 스킬들은 시연이다. 효과 · 비용 측정 없음.
- ASR: *"rd.md"*, *"right eval skill"* · *"right eval scale"*, *"scale"*(=skill 추정), *"give it away"*(=a way). ko는 2,500을 "명"으로, Anthropic을 "인류원리주의"로, *"isn't read"* 를 "생성되지 않습니다"로 옮겨 인용하지 않았다.

## References

- raw: `01.raw/articles/2026-11-01_Claude Code 완료했다고 끝이 아니다 - 검증과 리뷰 루프 만들기.md`
- https://www.youtube.com/watch?v=IGTdL4IPLq8
- 설명란 관련 자료(⚠️ 열어 보지 않았다): https://claude.dev/blog/solving-code-review-at-anthropic/ · https://code.claude.com/docs/

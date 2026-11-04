---
title: "Tech Bridge — 클로드 코드 토큰을 아끼는 MS 도구, 실제로 얼마나 줄었을까? (AI Labs): Token Economizer의 세 가지 절감, micro skills 인젝션, 콜드 스타트와 세션 기록 수정판"
type: source
tags: [token-economizer, microsoft, claude-code, codex, github-copilot, token-cost, tool-pruning, micro-skills, stuck-detection, hooks, plugin, prompt-injection, cold-start, session-history, graft, ai-labs, vendor-claim, video]
source-url: https://www.youtube.com/watch?v=FNpUPkAOE4g
source-type: video
author: Tech Bridge (번역 재배포, 내레이션 없음) · 원 제작자 [[ai-labs]](설명란 근거 — 발화 · 태그에 이름 없음, 1인칭 복수 "our channel" · "we", Graft 편 자기 언급으로 간접 정합) · 발표자 개인 이름 · 원본 링크 · 녹화일 미상
date-published: 2026-11-03
ingested: 2026-11-04
created: 2026-11-04
updated: 2026-11-04
---

# Tech Bridge — 클로드 코드 토큰을 아끼는 MS 도구, 실제로 얼마나 줄었을까? (AI Labs)

[[tech-bridge|Tech Bridge]]의 **10:54 해설 · 시연 영상, 공식 챕터 12, 내레이션 없음.** 오디오는 `English (US) original (default)` + 더빙 7개 언어이고 **한국어 트랙 · `ko-orig`가 없다** — 영어 원본 오디오만 있는 구성이라 **인용은 en-orig로만** 한다. 제목의 "[한글자막]"과 달리 수동 자막은 없다. 00:00~00:23(첫 챕터 "소개" 전체)은 무캡션이고, **마지막 문장은 *"of a difference as you keep using"*(10:52)에서 잘린다.** `upload_date` 20261103 = 18:00 KST. raw: `01.raw/articles/2026-11-03_클로드 코드 토큰을 아끼는 MS 도구 실제로 얼마나 줄었을까.md`.

[[ai-labs|AI Labs]](설명란 근거)가 [[microsoft|Microsoft]]의 플러그인 [[token-economizer|Token Economizer]]를 설명하고, 약점 하나(처음에는 아낄 것이 없다)를 고친 **자기 수정판**으로 측정해 보여 준다. 테제(발표자):

> **이 도구는 지도를 만들지 않고 사용자가 일하는 방식을 지켜보며 배운다. 반복 실수 · 쓰지 않는 도구 · 막힌 작업 세 군데의 낭비를 줄이지만, 처음에는 오히려 비용이 늘고 프로젝트마다 다시 배운다. 이미 있는 세션 기록에서 먼저 배우게 하면 그 공백을 메울 수 있다.**

> *"Instead of making a map, it learns from how you work."*(00:43~00:45) · *"it can even cost you more while it's still learning."*(06:48~06:52) · *"On our project, every message went from about 34,300 tokens down to about 24,400, which is about 29% less on every single message."*(09:45~09:57)

### 세 층을 나눠 읽는다

| 층 | 무엇 | 근거의 성격 |
|---|---|---|
| **[Microsoft]** | 277개 버그 · 6개 프로젝트 · 5개 구성, Sonnet 5 −23.6% · Opus 4.8 −30.9%, 도구 끄기가 가장 많이 아낌, 여섯 번째 작업쯤 싸짐 | 발표자 **전달**. 위키는 저장소를 열어 보지 않았다 |
| **[제품 동작]** | 임계값(10메시지 · 최소 2세션), 3세션마다 사실 추출, 훅 구조, 기본값, 명령 | 발표자 **설명**. 공식 문서와 대조하지 않았다 |
| **[AI Labs]** | 수정판(세션 기록 선학습), 276개 · 29%, 303개 · 99 → 79 스텝 · 약 21% | 발표자 **측정**. 특정 프로젝트, 시험 조건 대부분 미발화 |

> ⚠️ **화자 귀속은 설명란 근거다.** 발화 · 태그에 "AI Labs"가 없다. 설명란 *"AI LABS가 기존 세션 기록을 활용하도록 도구를 수정한 과정"* 이 유일한 이름이다. *"We've covered a few of them on our channel too, and Graft is one of them."*(00:24~00:28)은 이 위키의 AI Labs Graft 편([[tech-bridge-graft-code-knowledge-graph]])과 맞아 간접 근거가 된다. 발표자 개인 이름은 이번에도 없다.

## 1. 소개 (00:00~00:23)

en-orig에 발화가 없다(무캡션, 첫 큐 00:23.0). 이 챕터의 내용은 쓰지 않는다.

## 2. 토큰 이코노마이저의 실험 결과 (00:23~01:26)

- **Graft와의 대비** — *"Graft and a lot of other tools make a map of all the files in your project before you start."*(00:30~00:34) 반면 *"It watches every session and the commands your agent runs in it, and it keeps track of where tokens are being wasted. Then, it cuts that waste out of the sessions that come after."*(00:45~00:55) → [[graft]] · [[code-knowledge-graph]]
- **[Microsoft] 시험** — *"They gave the agent 277 real bugs to fix from six real projects on GitHub, and they had it fix each project's bugs one after another."*(00:59~01:09) *"They did that on five different setups across Claude Code, Codex, and GitHub Copilot."*(01:09~01:13) *"On every one of those setups, the tasks cost less with the tool than without it."*(01:13~01:17) ⭐ *"On Claude Code, Sonnet 5 cost 23.6% less and Opus 4.8 cost 30.9% less."*(01:17~01:22)

> ⚠️ **숫자는 다섯 구성 중 둘만 발화된다.** Codex · GitHub Copilot 쪽 숫자와 모델은 없다. 위키는 시험 데이터를 보지 않았다. ⚠️ **`en` · ko는 모델을 바꾼다** — en `Sonnet 3.5 ... Opus 3`, ko *"소네트 3.5의 가격은 23.6달러였습니다"*(01:19). 이 페이지는 en-orig를 따른다. *"Sonnet 5"* · *"Opus 4.8"* 은 이 위키에 처음 나오는 표기라 페이지를 만들지 않았다.

## 3. 토큰은 어디에서 낭비될까 (01:26~02:36)

- *"Since models don't remember things on their own, you also need to send them extra context about everything in your project."*(01:44~01:50)
- *"So, every request carries the instructions the agent always follows and the list of every tool it can use to work on your project."*(01:50~01:56) *"It also carries the MCP tools and skills you've added along with the whole conversation up to that point."*(01:59~02:02)
- 실수: *"It fixes a mistake in one session, but the next time you run it in the same project, it has to learn the same thing again by failing at it."*(02:15~02:21) 도구: *"On top of that, it carries around tools it never even uses."*(02:21~02:25)

> ⚠️ *"the list of every tool"* 는 일반화다. 이 위키의 [[deferred-tool-context]]는 도구 이름만 싣거나 검색으로 불러오는 하네스들을 기록해 왔다. 발표자는 지연 로딩을 말하지 않는다 → 11절의 도구당 토큰 산술 참조.

## 4. 반복 실수를 기억하는 마이크로스킬 (02:36~03:18)

- 대상: *"like running a tool or a command that doesn't work."*(02:38~02:40)
- ⭐ **[제품 동작]** *"When it sees Claude making the same mistake multiple times, it writes it down as a fact about your project. These facts are called micro skills."*(02:53~03:01) *"Once a few more sessions confirm that a fact is right, the tool saves it for that project."*(03:01~03:05) 효과: *"That way your agent already knows this didn't work before, so it doesn't try it again."*(03:12~03:16)

→ [[token-economizer]] · [[run-trace-skill-distillation]] · [[skill-self-improvement]] · [[trace-to-memory-loop]]

## 5. 쓰지 않는 도구를 줄인다 (03:18~03:46)

- ⭐ **[제품 동작] 임계값** — *"If one of them doesn't get used across 10 of your messages over at least two sessions, the tool turns it off for that project."*(03:22~03:28)
- ⭐ **[Microsoft] + 경고** — *"Microsoft's own numbers show this one saves the most tokens because it reduces the tools that are being sent at each turn, but it does this without asking you. So, you won't even know it took a tool out of your context window."*(03:30~03:42)

> ⚠️ **Contradiction: 알려 주는가.** 설명란은 *"공식 문서는 도구의 동작을 한 줄로 알린다고 설명합니다(2026년 11월 2일 확인)."* 라고 적는다. 발화의 *"you won't even know"* · *"without telling you"*(09:28~09:29)와 어긋난다. 설명란은 "도구의 동작"이 도구 끄기인지 명시하지 않으며, 정정 주석으로 읽는 것은 추정이다. 공식 문서를 열어 보지 않아 미확정이다.

→ [[usage-based-tool-pruning]](신규) · [[deferred-tool-context]] · [[token-minimization-trap]]

## 6. 막힌 작업에서 빠져나오기 (03:46~04:17)

- 조건: *"Sometimes an agent works on a task and can't find a way to do it."*(03:49~03:51) *"And sometimes it keeps going for way longer than Claude usually takes to answer one of your messages in that project."*(03:55~04:01)
- ⭐ **[제품 동작] 사다리** — *"When the tool sees this, it asks a model to check if Claude is really stuck."*(04:01~04:04) *"Only if it is, the tool tells Claude once to try something different, so it doesn't stay stuck in a loop."*(04:04~04:10) *"If Claude is still stuck after that, the tool tells you to press escape and stop it. It never stops Claude by itself."*(04:10~04:16)
- 이 위키의 읽기: 같은 도구가 **도구를 끌 때는 묻지 않고, 멈출 때는 사람에게 넘긴다.** 자율의 선이 기능마다 다르다. 발표자는 이 대비를 말하지 않는다.

→ [[review-loop-termination]] · [[hidden-harness-calls]](막힘 확인도 모델 호출이다)

## 7. 설치와 자동 실행 방식 (04:17~05:20)

- *"this tool is actually a plugin that's available for Claude code, Codex, and a few other AI agents."*(04:16~04:20) 설치는 저장소의 install 절에서 명령을 복사한다(04:23~04:36).
- ⭐ **훅이 전부를 돌린다** — *"The hooks run on their own at set times, like when a session starts or when you send a message."*(04:42~04:48)

| 시점 | 하는 일 (en-orig) |
|---|---|
| 세션 시작 | *"The micro skills we talked about get handed to Claude by a hook that runs at the start of every session"*(04:53~04:57) |
| 도구 사용 후마다 | *"another hook checks on it after every tool it uses, and that's how the plugin knows when Claude is stuck and needs a push."*(05:03~05:09) |
| 세션 끝 | *"once the session ends, the plugin looks back over everything that happened in it, all on its own."*(05:09~05:14) *"That's where it learns new facts for next time and keeps count of the tools that never got used."*(05:14~05:18) |

→ [[hook-enforced-workflow]] · [[graft]](세션 시작 · 프롬프트 · 편집 후 훅과 비교)

## 8. 설정과 프롬프트 인젝션 위험 (05:20~06:24)

- **기본값** — *"you'll see that most of its features are turned on, but micro skills are turned off when you first install it."*(05:22~05:28) 이유 둘.
- ① **한도** — *"Once it's on, every three sessions it asks a model to read through your recent sessions and write the facts, and that uses some of your own limit."*(05:32~05:40) → [[hidden-harness-calls]]
- ⭐ ② **안전** — *"The facts it writes come from whatever the commands in your project print out, and Claude reads them at the start of every session as if they were true facts about your project."*(05:42~05:50) *"So, if you download a project from someone else, whoever made it could hide instructions in what its commands print. Those instructions would end up in the facts, and Claude would treat them as true in every session unless you change them yourself."*(05:50~06:01) *"This is basically what's known as a prompt injection. That's why Microsoft leaves the choice to you."*(06:03~06:07) → [[prompt-injection]]
- **발표자 권고** — *"But for your own projects, you should turn it on because in Microsoft's tests, it was the feature that saved a lot of tokens."*(06:07~06:13)

> ⚠️ 5절은 도구 끄기가 *"the most"*, 여기는 micro skills가 *"a lot"* 이라 en-orig에서는 충돌하지 않는다. **`en`은 여기를 `saved the most tokens`로 고쳐 쓰므로 `en`만 보면 모순이 생긴다.**
>
> ⚠️ 위키의 판단: "자기 프로젝트"가 안전하다는 선은 발표자의 것이다. 자기 프로젝트의 명령도 외부 입력(의존성 · 로그 · 내려받은 데이터)을 출력할 수 있는데, 이 경우는 말하지 않는다. 사람 승인 단계도 말하지 않는다. 검증은 *"a few more sessions"* 뿐이고, 같은 명령을 다시 돌리면 같은 출력이 나온다는 점에서 인젝션을 걸러 주는지는 미상이다.

## 9. 처음에는 왜 비용이 늘까 (06:24~07:16)

- *"So, when you first install it, it hasn't learned anything yet, which means it won't save you anything at first."*(06:31~06:35)
- ⭐ **[Microsoft]** *"And at first, it can even cost you more while it's still learning. In Microsoft's own tests, almost every project cost more with the plugin at first and only got cheaper by the sixth task."*(06:48~06:58)
- *"And this happens in every single project because the plugin learns each project on its own and nothing carries over from one to the next."*(06:58~07:06)
- 실마리: *"But Claude Code already saves all your sessions in the main.claud folder for 30 days"*(07:06~07:11)

> ⚠️ 01:13의 *"On every one of those setups, the tasks cost less"* 는 **구성 전체의 합계**로 읽어야 앞뒤가 맞는다(위키의 읽기). 프로젝트 초반에는 더 비싸다는 것이 이 절의 말이다. *"almost every project"* 와 바로 뒤의 *"every single project"* 는 표현이 어긋난다. 30일 보관은 발표자 진술이고 위키는 확인하지 않았다.

## 10. 기존 세션 활용 실험 (07:16~08:21) — [AI Labs]

- ⭐ **수정** — *"We gave it the repo and asked it to change the tool"*(07:17~07:19), *"instead of starting from a blank state with no memory of what happened before, it goes through the session history that Claude stores in the main.claud folder first."*(07:21~07:29)
- 프롬프트는 자막에 없다: *"you can pause here and copy the prompt from the screen."*(07:35~07:39)
- 결과물: *"it starts a task that runs in the background and goes through the sessions you've run before in the same folder."*(07:50~07:56) 전역 설치가 안 됐으면 Claude에게 다시 시키라고 한다(08:01~08:05).
- 한계: *"This won't do anything for a brand new project because there's no history to read"*(08:09~08:13)

> ⚠️ 위키의 판단: 수정판은 Microsoft 판이 아니다. 과거 세션을 한꺼번에 읽으면 8절의 인젝션 표면이 지난 세션 출력으로 넓어질 수 있는데 발표자는 이 점을 말하지 않는다. 수정판의 품질 · 유지보수 · 배포도 발화되지 않는다. 또 수정 작업 · 백그라운드 읽기 자체의 사용량은 보고되지 않는다.

## 11. 사용 현황과 절감량 확인 (08:21~10:11) — [AI Labs] 데모 프로젝트

*"we installed our changed version and used it on a demo project."*(08:20~08:22)

| 명령(발화 표기) | 보여 주는 것 (en-orig) |
|---|---|
| status | *"It shows how many sessions it has learned from, how many tokens those sessions used, and what each of its features has done so far."*(08:33~08:39) |
| micro skills | *"It lists the facts the plugin hands Claude at the start of every session and the ones it's still checking."*(08:58~09:05) |
| tool prune | *"next to each one, it shows how many sessions and messages went by without that tool being used."*(09:16~09:20) |
| tool prune measure | *"It counts how many tokens every message takes with all your tools and how many it takes with only the ones you use."*(09:41~09:45) |
| tool prune restore | *"you can just run the tool prune restore command with the name of the tool, and it gives that tool back."*(10:03~10:07) |

- 상태: *"In our project, it had already learned from four sessions and the stuck check hadn't needed to step in once, but it already had a long list of tools it could turn off."*(08:39~08:49)
- ⭐ **276개** — *"On our project, 276 tools had gone unused across all four sessions, and since the plugin turns them off without telling you, this command is the place to check whenever Claude suddenly can't do something it used to do."*(09:20~09:33)
- ⭐ **29%** — *"On our project, every message went from about 34,300 tokens down to about 24,400, which is about 29% less on every single message."*(09:45~09:57)
- **되돌리기** — *"A tool the plugin turned off stays off in that project"*(09:59~10:01), *"And once you've given a tool back, the plug-in won't turn it off again."*(10:07~10:11)

> ⚠️ **29%는 비용이 아니라 측정 명령이 계산한 메시지당 토큰이다.** 한 프로젝트, 수정판, 도구 끄기 하나만의 값이고 캐시 할인을 반영하는지 말하지 않는다 → [[prompt-caching]]. 산술: 9,900토큰 ÷ 276개 ≈ **도구당 약 36토큰**(위키 계산, 276개가 측정 대상과 같다고 가정). 전체 스키마라기엔 작아 보여서 이미 지연 로딩된 이름 목록만 빠진 값일 수도 있지만(추정), 발표자는 설명하지 않는다 → [[deferred-tool-context]].

## 12. 세 가지 작업 비교 결과 (10:11~10:54) — [AI Labs] 다른 앱

- 준비: *"When we tested it on another app, we first ran five sessions on it with the plug-in on, so that it had something to learn from. In those sessions, it turned off 303 tools."*(10:11~10:19)
- 설계: *"Then we gave Claude three new tasks on that app and ran each one twice, once with the plug-in and once without. Both runs started from the exact same code."*(10:19~10:28)
- ⭐ **결과** — *"Without the plug-in, Claude took 99 steps to finish all three tasks. With the plug-in, it took 79 steps and the whole thing cost about 21% less. Both versions also passed the same checks."*(10:30~10:40)
- 단서: *"So, in the first sessions, when the plug-in hadn't learned anything yet, it cost a little more than a session without it."*(10:42~10:47) *"The savings started showing up in later sessions once it had learned something."*(10:47~10:50) *"So, you're going to see more of a difference as you keep using"*(10:50~10:52) — **영상이 여기서 끊긴다.**

> ⚠️ **3과제 각 2회(반복 없음).** 앱 · 모델 · 검사 내용, 수정판 · micro skills 사용 여부는 발화되지 않는다. 5세션 학습의 추가 비용은 21% 계산에 포함되지 않은 것으로 읽힌다(설계상 추정). 21%가 플러그인 자신의 모델 호출을 포함하는지도 말하지 않는다 → [[hidden-harness-calls]]. 99 → 79는 약 20.2% 감소이고 비용 21%와 비슷하다(위키 계산). ⚠️ `en`은 잘린 마지막 문장을 `continue using it`으로 완성한다.

## 등장 개체

- 제작자 · 조직: [[ai-labs]](설명란 근거) · [[microsoft]] · [[tech-bridge]]
- 제품 · 도구: [[token-economizer]](신규) · [[claude-code]] · [[codex]] · [[graft]] · GitHub Copilot(페이지 없음, 시험 구성으로 한 번) · Sonnet 5 · Opus 4.8(페이지 없음)
- 개념: [[usage-based-tool-pruning]](신규) · [[deferred-tool-context]] · [[token-minimization-trap]] · [[prompt-injection]] · [[run-trace-skill-distillation]] · [[skill-self-improvement]] · [[trace-to-memory-loop]] · [[hook-enforced-workflow]] · [[hidden-harness-calls]] · [[prompt-caching]] · [[review-loop-termination]] · [[code-knowledge-graph]]

## 이 위키에서의 좌표

- **[[ai-labs|AI Labs]]의 네 번째 소스.** 09-15 Graft 편과 형식이 같다(남의 토큰 절감 도구 소개 + 자기 수정판 + 비교 측정). 커뮤니티 언급은 이번에 없고 프롬프트를 화면으로 공개한다.
- **토큰 절감의 다른 축.** [[graft]]는 *찾는 비용*을 사전 인덱스로, [[deferred-tool-context]]는 *도구 정의 비용*을 필요할 때 로드로 줄였다. 여기서는 **과거 사용 이력**으로 끈다 → [[usage-based-tool-pruning]]. [[token-minimization-trap]]이 *빼도 되는 것*으로 꼽은 큰 도구 카탈로그의 자동화 판이기도 하다.
- **[[hidden-harness-calls]]의 사용자 쪽 대응물.** 토큰을 아끼는 도구도 자기 모델 호출(사실 추출 · 막힘 확인)로 한도를 쓴다.
- **트레이스 → 지식 루프의 작은 판.** [[run-trace-skill-distillation]]이 조직 스킬이라면, 여기서는 **프로젝트 사실 한 줄**이고, 외부 출력이 재료라는 위험을 만든 쪽이 직접 말한다 → [[prompt-injection]].

## ⚠️ 유보

- 화자는 설명란 근거(+ Graft 자기 언급 간접 정합), 개인 이름 · 원본 링크 · 녹화일 없음. 00:00~00:23 무캡션, 마지막 문장이 잘린다.
- **모든 절감 수치는 전달 또는 특정 프로젝트의 측정이다.** Microsoft 23.6% · 30.9%는 저장소 미열람, 발표자 29% · 21%는 수정판 · 소규모 · 조건 미발화. 단위도 다르다(비용 vs 메시지당 토큰 vs 스텝). 합치지 않는다.
- 설명란의 *"한 줄로 알린다"* 와 발화의 *"without telling you"* 가 어긋난다(미확정).
- 저장소 https://github.com/microsoft/TokenEconomizer 와 공식 문서는 **열어 보지 않았다.** 임계값 · 명령 철자 · 기본값 · 라이선스 미확인.
- 고친 판본의 프롬프트는 화면에만 있어 자막에 없다.
- ASR: *"main.claud"*(`.claude` 추정). `en`은 모델명을 Sonnet 3.5 · Opus 3으로, *"a lot of"* 를 `the most`로 바꾸고, ko는 23.6%를 *"23.6달러"* 로, 끈 도구의 전송 중단을 *"남게 됩니다 (…) 전송됩니다"* 로, plug-in을 *"보충제"* 로 옮겨 인용하지 않았다.

## References

- raw: `01.raw/articles/2026-11-03_클로드 코드 토큰을 아끼는 MS 도구 실제로 얼마나 줄었을까.md`
- https://www.youtube.com/watch?v=FNpUPkAOE4g
- 설명란 관련 자료(⚠️ 열어 보지 않았다): https://github.com/microsoft/TokenEconomizer

---
title: "Tech Bridge — 코드를 잘 짜는데, Codex는 왜 불편해졌을까? (Ben Davis 추정): priority view · ChatGPT/Codex 분리 · Spaces, 기능보다 기반"
type: source
tags: [codex, chatgpt, openai, product-cohesion, product-taste, verifier, enshittification, primitives, threads, spaces, sidebar, user-review, video]
source-url: https://www.youtube.com/watch?v=-B-967gXzHY
source-type: video
author: Tech Bridge (발췌 + 무캡션 한국어 해설 추정) · 화자 [[ben-davis]] 추정(설명란 · 태그 근거 — 발화에 이름 없음) · 원본 영상 · 녹화일 미상
date-published: 2026-10-30
ingested: 2026-10-31
created: 2026-10-31
updated: 2026-10-31
---

# Tech Bridge — 코드를 잘 짜는데, Codex는 왜 불편해졌을까? (Ben Davis 추정)

[[tech-bridge|Tech Bridge]]의 **6:51 발췌, 공식 챕터 8.** 오디오는 `Korean original (default)` + `English (US)` 두 트랙이고 `ko-orig`가 없다 — 10-28 [[tech-bridge-anthropic-fold-subagents-into-skills]]와 같은 구성이라 **인용은 en-orig로만** 한다. 무캡션 6구간이 챕터 경계와 겹쳐 **한국어 해설 구간으로 추정**하지만 내용은 어느 자막에도 없다. raw: `01.raw/articles/2026-10-30_코드를 잘 짜는데 Codex는 왜 불편해졌을까.md`.

테제:

> **모델은 검증기(verifier)가 있는 문제 — 테스트를 초록으로 — 는 끝까지 푼다. 그러나 제품 경험과 UI는 verifier 함수로 표현되지 않아서, 기능 출시가 쉬워질수록 이음매가 거칠어진다. Codex · ChatGPT가 그 가장 눈에 띄는 예다. 처방은 기능을 더하기 전에 덜어내고, Codex thread를 모든 표면의 공통 기본 단위로 다시 세우는 것이다.**

> *"Anything that can't be expressed with a clean verifier function the models still just aren't amazing at."*(00:52~00:56) · *"The cohesion just isn't there at the product level"*(04:07~04:09) · *"It's never been easier to ship a feature"*(04:31~04:33) · *"A Coda[=Codex] thread should become the base building block for everything."*(05:20~05:24)

> ⚠️ **화자 신원은 설명란 · 태그 근거다.** 발화에 이름이 없다. 설명란 본문 *"Ben Davis가 Codex를 쓰며 느낀"* 과 info.json `tags`의 `Ben Davis`가 근거다. 발화로 확인되는 것은 **채널을 운영하는 1인칭 사용자**라는 점뿐이다 — 편집자가 있고, Final Cut으로 영상을 준비하고, 이 영상도 Spaces에서 기획했다(02:27~02:33, 02:52~02:56). → [[ben-davis]] **추정.**
>
> ⚠️ **1인 사용자의 진술.** 제품 동작 묘사(priority view, chat · work · Codex 분리, Spaces의 화면 강제 이동, headless 제어)는 OpenAI 측 확인 · 버전 정보가 없다. 녹화일 미상.
>
> ⚠️ **"Coda"는 Codex로 판독**(raw 헤더 참고). Coda(coda.io)도 실제 문서 도구 이름이라 추정이다.

## 1. 모델은 강한데, 제품은 왜 불편할까? (00:00~00:12)

en-orig에 영어 발화가 없다(무캡션 — 한국어 해설 추정). 이 챕터의 내용은 쓰지 않는다.

## 2. priority view와 최근 기록의 차이 (00:12~00:39)

- 기대: *"The priority view is supposed to be a to-do list of the threads that need attention so that you can go work on them and then when you're done with them you dismiss them and they disappear down into the void."*(00:12~00:20)
- 실제: *"In Codex that's not how they work. This is basically just a timeline of what you have worked on in order."*(00:20~00:27)
- 화자는 뒤에서 사이드바의 *"priority view"*(03:37~03:41)로 다시 돌아가므로, priority view는 **Codex 사이드바에 실재하는 보기 이름**으로 읽힌다. ⚠️ 그 동작이 버그인지 의도인지는 발화되지 않는다.

## 3. 테스트로 검증하기 어려운 제품 판단 (00:39~01:35)

- ⭐ *"even though yes again unlimited tokens the models are not good at making open-ended product decisions that require for lack of better word human taste and discernment and decision-making."*(00:41~00:50)
- *"Anything that can't be expressed with a clean verifier function the models still just aren't amazing at. Opus is the best at it of anything but it's still not perfect or there."*(00:52~01:00) — 경쟁사 모델(Opus, 버전 미발화)을 기준점으로 든다.
- 대비: 모델은 *"solving these incredible novel math problems"*, *"grinding down full rewrites of gigantic projects in Rust"*(01:02~01:06) — *"all of these problems can be expressed with some sort of hill for them to climb. You have a test suite you need to get them all green."*(01:09~01:13) → *"It can loop and run in circles until it optimizes itself"*(01:16~01:20).
- ⭐ *"You can't really do that for product experience and UI. It's very hard to encode that into a verifier function. Maybe eventually someone will figure it out. At least right now they haven't figured it out"*(01:23~01:32)

→ [[verifiable-goals]](경계: verifier가 없는 곳) · [[taste-vs-judgment]] · [[taste-encoded-evals]](*"maybe eventually someone will figure it out"* 의 한 후보)

## 4. ChatGPT와 Codex를 나누는 방식 (01:35~02:22)

- *"So you got Codex and chat GPT that split which already is very confusing to most people."*(01:34~01:41)
- 의도는 이해한다: *"they want to have the same agent be the thing that runs everything which is Codex."*(01:41~01:45)
- ⭐ 처방: *"just make it chat GPT powered by Codex. Just power the normal chat GPT with Codex. Don't do this work split. There's like a chat and a work and a Codex. It's so weird. Just make all of them Codex under hood."*(01:47~01:59)
- 같은 입구, 다른 요청: *"If I send a prompt that is a bunch of coding stuff, it'll do coding stuff. If my little sister sends a prompt that's asking about basic school work, it'll just answer with that."*(01:59~02:07)
- ⚠️ *"a chat and a work and a Codex"* 가 ChatGPT의 어떤 표면(모드 · 탭 · 앱)을 가리키는지 발화로 특정되지 않는다.

## 5. Spaces의 장점과 어색한 연결 (02:22~04:25)

**장점(화자의 실사용):**

- *"spaces one of the big new headline features that they shipped and it is quite good. I actually am using it a lot."*(02:21~02:27)
- 반복 작업의 템플릿: 영상마다 템플릿에서 복사한 단계(Final Cut 준비)가 있고, *"you can save prompts inside of it to fire off into a codex thread and make those happen."*(02:47~02:51)
- ⭐ **공유**: *"my editor can go into our shared spaces here, go into this video. He can hit the prompt here, prep the video in final cut just with this pre-rolled prompt"*(02:52~03:00). 썸네일용 스크린샷 추출 · 업로드 체크리스트 · 설명란 템플릿도 같은 방식(03:02~03:12).
- 한 줄 평: *"It's basically notion with a bunch of AI stuff built into it with a lot of rough edges around it."*(03:14~03:18)

**거친 이음매:**

- 변경 시 화면 강제 이동: *"when it makes changes, it will force your view, your entire computer back onto that page to focus it so that you can watch the model make the change for some reason. I don't know what reason. Really, really annoying"*(03:23~03:34)
- 같은 thread가 두 곳에: 사이드바에서 열면 Spaces 페이지에 붙은 thread인데, 전체 보기로 열면 *"it's a normal codex thread, but also it's here and it's just it's weird."*(03:48~03:56)
- ⭐ *"you have the threads and you have the spaces and they are trying to stick them together and they're just not doing it very well"*(03:56~04:03) → *"The cohesion just isn't there at the product level, especially across such a big and ambitious thing like Coda[=Codex]."*(04:07~04:11)

> ⚠️ **이 Spaces가 [[chatgpt-space|ChatGPT의 Space]](DevDay 2026, Altman 발화)와 같은 제품인지 미확정.** 둘 다 OpenAI의 최근 문서형 협업 기능이고 *"new headline features"* 라는 표현도 맞지만, 이 영상은 *spaces*(복수)를 Codex thread와 묶어 말하고 ChatGPT Space라는 이름 · 링크는 없다. 같은 페이지로 합치지 않고 교차 참조만 한다.

→ [[product-polish-patterns]](rough edges) · [[codex]]

## 6. 기능을 더하기 전에 정할 것 (04:25~05:08)

- *"there's been a lot of you can call it enshitification where things just keep getting more and more features and random nonsense."*(04:25~04:31)
- ⭐ *"It's never been easier to ship a feature, to make something new and put it in production. (…) You give a model a task, it will perform that task. The problem is they're not going to do it in the best possible way, and a lot of weird edges are going to naturally start to form. If you don't have a very strong vision, and especially way to say no to things."*(04:31~04:52)
- *"Coda[=Codex] and ChatGPT are not the only example of this. They're just the most glaringly obvious one, which is why I'm using them and dunking on them here."*(04:52~04:57) — 화자 스스로 **비판 목적의 사례 선택**임을 밝힌다.

→ [[primitives-before-features]](신규) · [[slop-cannon]](출시 비용 0의 다른 얼굴)

## 7. 대화(thread)를 공통 기반으로 만든다면 (05:08~06:33)

처방은 순서가 있다.

1. **덜어내기**: *"the first thing I would do would be gutting most of it. Like I I would start cutting features before I made new ones."*(05:09~05:16)
2. **thread를 기본 단위로**: *"A Coda[=Codex] thread should become the base building block for everything. That should be the building block for the CLI, for the desktop app, for the web app, everything."*(05:20~05:30) — *"so I'd fix that primitive."*(05:32~05:35)
3. **Spaces는 그 위의 별도 primitive**: *"Once you have that primitive really locked in, then I think it becomes a little bit easier to then make spaces a separate primitive sitting over here."*(05:37~05:44) — space 안의 page가 *"an entity that can then be manipulated by a thread directly whenever you want to."*(05:51~05:55)
4. **위치 무관**: *"Should also be very easy to take a thread and throw it in the cloud or have it local."*(05:55~06:01) · *"Spaces can easily be controlled headlessly. Right now they can be, but not really."*(06:01~06:06)
5. **결합 끊기**: *"I wouldn't have threads tied directly to the spaces."*(06:06~06:09) — composer는 두되 누르면 **normal thread**가 열리고 Space는 *"in context as part of the prompt because you fired it from here"*(06:17~06:20)로만 들어간다.

- 마무리: *"they they need to fix the foundation first, and the foundation is fundamentally pretty broken right now. I trust they'll do it. There's tons of talented people there."*(06:23~06:31)

> ⚠️ **"이미 공통 하네스는 있다"와의 관계.** [[codex-app-server]]의 당사자 설명은 App Server가 *"the core protocol that underpins the Codex app, the Codex CLI, uh, the Codex VS code extension"* 라는 것이었다([[tech-bridge-cooking-with-codex]]). 즉 **프로토콜 층의 공통 기반은 있다**고 OpenAI가 말하고, 이 화자는 **제품 층(thread가 보이고 다뤄지는 방식)의 공통 기반이 없다**고 말한다. 층이 달라 모순은 아니다.

→ [[primitives-before-features]] · [[codex-app-server]] · [[subagent-vs-thread-handoff]](thread를 단위로 보는 다른 소스)

## 8. 기능보다 먼저, 제품의 기반 (06:33~06:51)

en-orig는 06:32~06:35 *"something out here."* 로 끝나고, 나머지는 무캡션(한국어 해설 추정)이다.

## 등장 개체

- 인물: [[ben-davis]](추정, 신규) · *"my editor"* · *"my little sister"*(이름 없음)
- 조직 · 제품: [[openai]] · [[codex]](priority view · thread · CLI · 데스크톱 · 웹 앱) · ChatGPT(페이지 없음) · Spaces(→ [[chatgpt-space]]와의 동일성 미확정) · Opus(버전 미발화 — 페이지 연결 안 함) · Notion · Final Cut(비유 · 도구 언급, 페이지 없음)
- 개념: [[primitives-before-features]](신규) · [[verifiable-goals]] · [[taste-vs-judgment]] · [[product-polish-patterns]]

## 이 위키에서의 좌표

- [[codex]] 페이지의 소스는 대부분 **OpenAI 당사자**(Altman · Brockman · developer experience 팀) 또는 **기능 관찰**이었다. 이 편은 **외부 사용자가 제품 표면 전체의 일관성을 비판하는 첫 소스**다.
- [[verifiable-goals]]의 *"verifier를 만들 수 없는 곳"* 경계(09-01 [[signal-layer]])가 **제품 UX**라는 구체적 자리를 얻는다 — 그리고 그 결과가 실제 제품에 보인다는 주장으로 이어진다.
- [[tech-bridge-codex-app-server]] · [[tech-bridge-cooking-with-codex]]가 **같은 하네스가 모든 표면을 돈다**고 했다면, 이 편은 **같은 thread가 모든 표면의 기본 단위여야 한다**고 한다.

## ⚠️ 유보

- 화자 신원 설명란 · 태그 근거, 원본 영상 · 녹화일 미상, 앞뒤 맥락(*"again unlimited tokens"*) 잘림.
- 한국어 해설(추정) 구간은 자막이 없어 내용 불명.
- 제품 동작은 1인 체감, 버전 미상. Spaces와 ChatGPT Space의 동일성 미확정.
- *"Coda"* → Codex 판독 추정. ko는 기계 번역이라 인용하지 않았다(spaces → "공간", thread → "실").

## References

- raw: `01.raw/articles/2026-10-30_코드를 잘 짜는데 Codex는 왜 불편해졌을까.md`
- https://www.youtube.com/watch?v=-B-967gXzHY

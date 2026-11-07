---
title: "Tech Bridge — 바이브코딩을 멈추세요: AI 에이전트와 TDD로 코딩하는 EXACT (Emily Bache × Marco Emrich · Ferdinand Ade): 예시 매핑, 테스트 목록, 예측형 TDD"
type: source
tags: [tdd, example-mapping, exact-coding, vibe-coding, subagents, predictive-tdd, code-quality, mutation-testing, human-in-the-loop, emily-bache, codecentric, video]
source-url: https://www.youtube.com/watch?v=hRhjL6BsxTU
source-type: video
author: Tech Bridge (번역 재배포 + 한국어 해설) · 진행 [[emily-bache]](설명란 · tags 근거 — 발화에 이름 없음) · 인터뷰이 Marco Emrich · Ferdinand Ade(codecentric, 설명란 근거) · 원본 링크 · 녹화일 미상
date-published: 2026-11-06
ingested: 2026-11-07
created: 2026-11-07
updated: 2026-11-07
---

# Tech Bridge — 바이브코딩을 멈추세요: AI 에이전트와 TDD로 코딩하는 EXACT

[[tech-bridge|Tech Bridge]]의 **17:04 인터뷰 편집본, 공식 챕터 14, 짧은 한국어 해설 포함.** 오디오는 `English (US) original (default)` + 더빙 7개 언어이고 **한국어 트랙 · `ko-orig`가 없어** 인용은 en-orig로만 한다. en-orig에는 한국어 해설이 없고 무캡션 간격 11곳으로만 보인다. 그 내용은 **`en` 트랙에만** 남아 있다(유보 참조). `upload_date` 20261106 = 2026-11-07 07:00 KST. raw: `01.raw/articles/2026-11-06_바이브코딩을 멈추세요 AI 에이전트와 TDD로 코딩하는 EXACT.md`.

[[emily-bache|Emily Bache]](설명란 근거)가 codecentric의 Marco Emrich · Ferdinand Ade(설명란 근거)에게 [[exact-coding|EXACT 코딩]]을 묻는다. 바깥 루프에서 **사람들이 예시로 무엇을 만들지 정하고**, 안쪽 루프에서 **에이전트가 TDD로 그것을 제대로 만든다.** 정리(이 페이지의 말):

> **올바른 것을 만드는 일은 예시 매핑으로, 그것을 올바르게 만드는 일은 예측형 TDD로 나눈다. 효과는 자기들 실험실에서 쟀다. 대가는 토큰이고, 사람이 빠져도 되는지는 아직 답이 없다.**

> ⚠️ **실험의 수치 대부분이 화면 표에 있고 영상을 보지 않았다.** 품질 · 비용 비교의 실제 값은 이 페이지에 없다. 실험은 만든 사람들이 직접 돌렸고 외부 재현은 영상에 나오지 않는다.

## 핵심 주장

1. **TDD의 핵심은 예시다.** 에이전트는 *"they seem to do better with concrete examples than only a theoretical description of what you want."*(00:45~00:50)
2. **산문 요구보다 예시 매핑이 정확도를 크게 올린다.** *"the correctness increases by 60 70% 80% even in some cases"*(05:43~05:50)
3. **스펙 프레임워크는 읽을 마크다운만 늘린다.** *"it becomes more and more lines of markdown."*(07:42~07:44) 대신 사고를 앞으로 당긴다.
4. **지시 없는 TDD는 싸고, EXACT는 품질이 낫다.** *"much higher code quality, much better unit tests, although at a higher cost in tokens."*(09:34~09:42)
5. **단계별 서브에이전트의 이득은 모델이 좋아질수록 줄었다.** 남은 것은 리팩터링 전담 하나이고 그 이득도 작다.

## 챕터별 요약

### 00:00 도입 · 00:22 예시 주도 개발이라는 관점
- 진행자는 TDD를 *"exampleg guided development"*(00:30)로 부르자는 제안을 전한다. ASR *"Daniel Turus North"*(00:22) · *"Matt Wyn"*(00:22)는 `en` 표기로 Daniel Terhorst-North · Matt Wynne이다.
- *"examples are at the heart of the exact coding workflow"*(00:50~00:53)

### 01:11 EXACT를 만든 이유
- 출발은 컨퍼런스 · 고객 프로젝트 실험이다. 바이브 코딩(ASR *wipe coding*)은 *"something that produces code but maybe not exactly what you want"*(01:22~01:27)을 내고 품질 문제도 있었다.
- 이름은 말장난이다: *"we want to get exactly what we want, not what you get with VIP coding."*(01:52~01:56)

### 02:34 EXACT 워크플로
세 단계다 → [[exact-coding]].
- **예시 매핑.** *"That's a technique from Matt Wyn of BDD fame for collaborating with stakeholders to map out a user story."*(02:41~02:46)
- **테스트 목록.** [[kent-beck|Kent Beck]]의 Canon TDD에서 왔다: *"you keep track of the whole problem that you need to solve in a natural language list of ideas for test cases."*(02:57~03:01)
- **안쪽 TDD 루프.** *"one item from the list at a time, going through red, green, refactor"*(03:08~03:10)

### 03:21 예시 매핑은 사람을 위한 것
- 이 단계는 *"is made for humans"*(03:26)이고 정신 모델을 빨리 세우는 것이 목적이다. 에이전트의 역할은 뒤에 온다: *"the LLM is checking if we are missing any obvious permutations"*(03:50~03:55)

### 04:33 실험실과 예시 매핑 결과
- 학습 데이터 오염을 피하려고 새 코드 카타를 만들었다: *"new code carters which of course aren't previously in the training data"*(04:52~04:56) 채점은 *"a complete test suite of acceptance tests which they don't show the LLM"*(05:02~05:07)로 한다.
- 비교군은 규칙을 산문으로만 준 경우다(*"this is basically wipe coding"*(05:32~05:34)). 결과는 위 주장 2다.
- `en`에만 있는 해설: `Claim Office` 27% → 94%, `Sphinx` 15% → 100%, `Opus 5` 모델로 칸마다 6회(06:04~06:17). ⚠️ `en`은 고쳐 쓴 문장이고 표를 보지 않아 인용하지 않는다. 카타 이름과 모델명도 미확정이다.

### 06:21 현실의 모호함과 스펙 주도 개발
- 진행자의 반론: 처음부터 설명을 잘 쓰면 되지 않나? Ferdinand는 제품 팀과 자기 일을 나눈다. Claude Code 팀은 *"they're basically building a tool themselves for themselves."*(06:39~06:43) 반면 컨설턴트는 *"we are not the experts"*(06:54~06:55)이고 *"there is always a lot of ambiguity in the requirements."*(06:55~06:59)
- 스펙 프레임워크 비판(BMAD 언급): *"You kind of have the same looks good to me feeling you have you always had with a really big um porest."*(07:52~07:58) 처방은 *"frontload or shift left some of the thinking"*(08:04~08:06)이다. → [[spec-driven-development]] · [[shift-left-interventions]]
- 진행자의 요약: *"examples, sticky notes, conversations"*(08:24)

### 08:52 안쪽 루프: 품질과 비용 데이터
- 세 조건을 비교한다. plain TDD는 *"Plain TDD means just telling the LM to do TDD with very little explanation."*(09:02~09:08)이고 *"is much cheaper in token cost"*(09:10~09:12)이다. 지표는 최장 함수, *"Cognitive max is a static analysis measurement of code complexity."*(09:21~09:25), *"mutation score is how good the tests are at finding bugs."*(09:28~09:30)다. → [[structure-sensitive-tests]]
- ⚠️ 표의 값은 자막에 없다. 방향만 기록한다.

### 10:03 서브 에이전트 실험
- 시작은 TDD 커맨드 하나였다. Ferdinand가 *"loss in the middle paper"*(10:40)를 근거로 제안했다: *"the longer the context gets the more gets lost in the middle of the context."*(10:42~10:47) 그래서 *"it would make sense to have each phase in a single sub agent with a fresh context"*(10:51~10:56) → [[context-rot]]
- 이 질문을 검증하려던 작업이 실험실이 됐다: *"a Sunday evening project that turned into an entire test lab"*(11:18~11:20)
- ⭐ Opus 5.5 · Claude Code의 현재 답: *"better results with two agents. The main agent doing most of the TDD workflow and a separate sub agent for the refactoring step."*(11:37~11:44) 효과는 *"measurably better code quality although actually not by much."*(11:47~11:49)
- ⭐ 모델에 따라 답이 바뀐다: *"with OPU 4.6 the spread was much larger even."*(11:58~12:01) *"Nowadays the additional value from the refactoring agent is not so strong but the additional value from having a dedicated TDD approach is still visible."*(12:06~12:14) → [[subagent-folding]]

### 12:35 예측형 TDD
- *"before you do any TDD step, you have to predict what the result would be."*(12:58~13:04) 예를 들면 *"this test will be red and for what reason will it be failing?"*(13:07~13:11) 진행자는 Ted M. Young의 TDD 게임과 cyber-dojo에서 알려진 방법이라고 소개한다.
- 작동 이유는 가설로 말한다: *"the prediction brings the problem to the front of the context for the LLM"*(13:37~13:42) 스스로 단서를 단다: *"we would need to bring a um LLM researcher here"*(13:30~13:35)

### 14:07 사람은 얼마나 개입해야 할까
- *"there is no clear answer to this question right now."*(14:18~14:20) 그래서 하니스에서 *"you actually get the choice to select the autonomy level"*(14:28~14:30)
- 개인 경험: *"the more I actually look after it, stay in the loop, understand what the LLM is doing and make course corrections, the better the result actually is."*(14:54~15:04) ⚠️ 이 부분은 측정이 아니다.

### 15:23 TDD를 잘 몰라도 될까 · 16:25 정리
- *"he tried teaching TDD for 20 years and now finally uh something listens"*(15:37~15:42)는 농담이라고 밝힌다. 답은 *"you could start without having full TDD knowledge"*(15:53~15:55)와 *"it's not so hard to get started."*(16:06~16:08)다. 지식이 깊으면 하니스를 고칠 수 있다.
- 진행자의 정리: *"build the right thing with example mapping"*(16:30~16:32) 그리고 *"build the thing right with predictive test-driven development"*(16:37~16:40)

## 등장 개체

- 인물: [[emily-bache]](설명란 근거) · Marco Emrich · Ferdinand Ade(→ [[exact-coding]]에 기록) · [[kent-beck]] · Daniel Terhorst-North · Matt Wynne · Ted M. Young(언급 수준) · [[tech-bridge]]
- 조직: codecentric(설명란 근거, 언급 수준)
- 제품: [[claude-code]] · BMAD · cyber-dojo(언급 수준)
- 개념: [[exact-coding]] · [[spec-driven-development]] · [[shift-left-interventions]] · [[context-rot]] · [[subagent-folding]] · [[structure-sensitive-tests]] · [[harness-pruning]]

## 이 위키에서의 좌표

- **[[spec-driven-development]]의 반대 진영이되 이유가 다르다.** [[kent-beck|Beck]]은 SDD를 폭포수로 비판했다. 여기서는 사람이 긴 문서를 제대로 검토하지 못한다는 UX 문제로 비판하고, 앞단의 사고를 대화와 예시로 옮긴다.
- **서브에이전트 논의에 드문 비교 실험을 더한다.** [[subagent-folding]]의 권고와 같은 방향이고, 이득이 모델 세대에 따라 변한다고 말한다. 다만 값을 보지 못했다.
- 측정 지표에 mutation score가 들어간다. [[structure-sensitive-tests]]는 *거짓말하는 테스트*의 자동 탐지가 소스에 없다고 적어 두었는데, 이 영상은 그 지표로 조건을 비교한다(위키의 읽기).

## ⚠️ 유보

- 영상을 보지 않았다. 워크플로 그림 · 데이터 표 · 값은 자막으로 확인할 수 없다.
- 실험은 제작자 본인들의 것이다. 표본 크기, 카타 구성, 통계 처리, 외부 재현은 발화에 없다. *60 70% 80%*도 범위 표현일 뿐이다.
- 무캡션 간격 11곳(00:00~00:22 · 02:17~02:34 · 04:11~04:33 · 06:00~06:22 · 08:34~08:52 · 09:42~09:55 · 09:55~10:04 · 12:14~12:36 · 13:47~14:07 · 16:08~16:25 · 16:45~17:00). 대부분 챕터 경계와 겹치며 한국어 해설 구간으로 추정한다. 일부는 `en`에도 내용이 없다.
- `en`에만 있는 진술은 인용하지 않는다: 위 카타 수치, 카드 색 설명(04:12~04:22), 오픈소스 공개 · 집필 · 자율 수준 3단계(16:15~16:23).
- 화자 구분: Ferdinand의 발화로 확인되는 곳은 진행자가 소개한 구간뿐이다(06:34 · 07:20 · 10:16 추정). 다른 답은 누구 말인지 정하지 않았다.
- 인명: `Bache`는 설명란 · tags 근거다. 인터뷰이의 성은 ASR *Emerick* · *Ara*, `en` `Emrich` · `Ada`, 설명란 Emrich · Ade로 갈린다. 설명란을 따른다.
- `en-orig`의 *"loss in the middle paper"*(10:40)는 lost in the middle로 읽었다. 논문 원문은 열지 않았다.

## References

- raw: `01.raw/articles/2026-11-06_바이브코딩을 멈추세요 AI 에이전트와 TDD로 코딩하는 EXACT.md`
- https://www.youtube.com/watch?v=hRhjL6BsxTU

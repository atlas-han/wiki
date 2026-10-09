---
title: "Tech Bridge — 글을 쓰지 않는 AI 모델? Jev의 정체 (IBM Technology): System 1 모델, RLCD와 보정된 확률, 임계값으로 자동/사람/무시"
type: source
tags: [jev, typesafe, system-1-model, calibration, rlcd, rlhf, rlvr, post-training, confidence-threshold, human-in-the-loop, guardrails, jevons-paradox, ibm, video]
source-url: https://www.youtube.com/watch?v=9tPnHRSUNFA
source-type: video
author: Tech Bridge (한영자막 재배포) · 원본 [[ibm|IBM]] Technology 계열 1인 화이트보드 해설(⚠️ 화자 무명 — 자막·설명란 모두 이름 없음, IBM 판정은 설명란 `#IBMTechnology`·`ibm.biz` 링크뿐) · 주제 [[typesafe-ai|TypeSafe]]의 [[jev|Jev]] · 촬영 시점 미확정
date-published: 2026-10-03
ingested: 2026-10-09
created: 2026-10-09
updated: 2026-10-09
---

# Tech Bridge — 글을 쓰지 않는 AI 모델? Jev의 정체 (IBM Technology)

[[tech-bridge|Tech Bridge]]가 재배포한 **14:51 1인 화이트보드 해설, 공식 챕터 10개.** [[ibm|IBM]] Technology 계열(설명란 기준) 무명 화자가 [[typesafe-ai|TypeSafe]]의 [[jev|Jev]]를 **제3자 입장에서** 설명한다. 이 위키에 Jev를 서술하는 **두 번째 소스**이고, 첫 소스([[tech-bridge-jev-agent-harness]], LangChain)가 비워 둔 세 칸을 채운다 — **① 학습 목표(RLCD — reinforcement learning for calibrated decisions), ② 반환 확률이 보정(calibrated)되어 있다는 주장, ③ 이름의 유래(Jevons paradox).** 그 위에 개념 하나가 생긴다 → [[model-calibration]] (신규).

> **소프트웨어 안의 결정 대부분은 System 2가 아니라 빠른 판단이다. Jev는 그런 판단을 텍스트 없이, 선택지마다 확률로 한꺼번에 돌려준다. 그 확률이 보정돼 있다면 — 80%라고 할 때 약 80%가 맞는다면 — 코드는 임계값으로 자동 처리 / 사람 호출 / 무시를 나눌 수 있고, 임계값이 곧 자동 경로의 오류율이 된다. RLHF는 확신에 찬 말투를, RLVR은 정답만 보상하므로 "얼마나 확신해야 하는가"는 아무도 학습시키지 않았다 — 그것을 보상하는 것이 RLCD다.**

> *"it's an AI model that doesn't actually write any text. It actually answers questions by picking from a list and then giving a probability for each one of those answers"* (00:09~00:20) · *"a lot of decisions inside software are not really system two. They're just kind of quick judgment calls"* (01:58~02:05) · *"Because the numbers are calibrated, the threshold also tells us roughly how often the automatic path will be wrong. So the more a mistake is going to cost, the higher we would set the threshold."* (12:05~12:20)

ASR·ko 보정: ko는 이 채널 평균보다 정확하지만 **TypeSafe를 "어떤 유형의 안전장치"로**(04:54), **LLM 학습을 "법학 석사 과정 교육"으로**(07:01), *takes text in as of today* 를 **"오늘부터 문자 메시지만 받습니다"로**(12:43), 0.9 임계값을 **"9점"으로**(11:11) 옮겼고, Jev를 **"사람"·"담당자"** 로 세 번 의인화했다. en-orig는 Kahneman을 세 번 다르게(*"Carneaman"·"Carnean"·"Cardaman"*), Jev를 네 번 *"Jeff"* 로, Jevons를 *"Jevans"* 로 들었다. ⚠️ **`en` 트랙은 en-orig와 완전히 같다** — 독립 판독 근거가 아니다. 전체 목록은 raw. **인용은 en-orig에서만** 했다.

> ⚠️ **RLCD와 "보정"은 TypeSafe 주장의 재진술이다.** 화자 스스로 *"TypeSafe haven't published much about Jev's architecture, so I'll stick to what they have said"*(09:30~09:37). 자료 이름·링크·보정 곡선 실측은 없다 — 화이트보드의 대각선은 **잘 보정된 모델이 어떻게 생겼는가** 의 설명이지 Jev의 측정치가 아니다(09:54~10:35). **이 위키는 TypeSafe 원 자료를 확인하지 않았다.**
>
> ⚠️ **수치 0개.** 0.9 · 0.85 · 임계값 0.9/0.1은 칠판의 가상 값이다. LangChain 편의 *"20~200배 빠르고 40~400배 저렴"* 같은 배수도 이 편엔 없다 — *"so much faster and cheaper"*(05:33~05:36)뿐.
>
> ⚠️ **화자·시점.** 화자 이름은 자막·설명란 어디에도 없다(IBM 계열 소스 중 무명은 이번이 네 번째). 촬영 시점 단서는 *"a new AI model"*(00:04), *"as of today"*(12:43)뿐 — **미확정.** 업로드는 2026-10-03.

## 1. System 1 / System 2 — Jev가 노리는 자리 (00:00~02:09)

- Jev = *"a new AI model from a startup called TypeSafe"*(00:04~00:06), TypeSafe는 이를 *"a new type of AI model (…) a system one model"* 이라 부른다(00:20~00:24). 이름은 Daniel Kahneman 『Thinking, Fast and Slow』에서 — System 1은 *"fast and automatic"*(2×2), System 2는 *"slow and deliberate"*(17×24)(00:24~01:24).
- 챗봇은 토큰을 하나씩, 추론 모델은 chain of thought까지 써 내려간다 — *"basically as close to a system 2 model as AI gets"*(01:51~01:58). 그러나 소프트웨어 안의 많은 결정은 *"just kind of quick judgment calls"*(02:04~02:05).

→ [[system-1-model]]

## 2. 고객 지원 이메일 하나, 질문 셋 (02:09~04:04)

- *"I was charged twice this month. Please fix it."*(02:18~02:21) → 소프트웨어가 물어야 할 것: **환불 요청인가**(예/아니오) · **어느 팀**(billing/technical/sales) · **얼마나 급한가**(02:34~02:56). 사람은 훑어보기만 해도 안다 — *"That's kind of a system one bit of work"*(03:10~03:12).
- 지금의 흔한 방법: LLM에 보내 JSON으로 답을 받는다. ⭐ *"that mostly works, but it doesn't come back with a reliable sense of how sure the model is"*(03:41~03:46). 모델에게 확신도를 물어도 *"whatever it responds with wouldn't necessarily actually match the real probabilities the model used to come up with its answer"*(03:54~04:02). → [[preference-reward-asymmetry]]

## 3. 입력 = state + 질문, 출력 = 확률 (04:04~06:52)

| | 내용 (화자 진술) | en-orig |
|---|---|---|
| **state** | *"the data the decision is about"* — 지원 이메일 + 최근 청구 내역 | 04:14~04:32 |
| **질문 유형** | 예/아니오 = *"which type safe calls a null"*(⚠️ 미판독, LangChain 편은 Boolean) · **choice**(목록에서 하나) · **score**(low~critical 척도) | 04:43~05:10 |
| **한 요청** | 세 질문을 *"in a single request"*, LLM처럼 토큰을 하나씩 쓰지 않고 *"all three answers, they all come back at once"* | 05:14~05:31 |
| **출력** | 환불: 숫자 하나(예 0.9) · 팀: **선택지마다** 확률(billing 0.85) · urgency: 척도 위 값 | 05:46~06:35 |
| **선택지 제약** | *"the answer to choice can only be the options that we give it"* | 06:21~06:26 |
| **오답 가능성** | *"the model can still pick the wrong options (…) but the probability tells us how likely that is"* | 06:38~06:48 |

⭐ 속도·비용의 이유를 **구조로** 설명한다: *"Jeff[=Jev] doesn't generate any text. So all three answers, they all come back at once. And that's a big part of why this is so much faster and cheaper than an LLM on these types of questions."*(05:24~05:36) — LangChain 편의 *"병렬로 답한다"* 와 같은 주장의 이유 쪽이다.

> ⚠️ **LangChain 편과 같은 예시 골격.** 두 소스 모두 *지원 티켓 → 어느 팀(choice) · 긴급도 · 예/아니오* 를 든다(LangChain 편은 Boolean = 긴급한가, score = 얼마나 화났나; 이 편은 Boolean = 환불인가, score = 긴급도). **둘 다 TypeSafe 문서의 예시를 옮겼을 가능성**이 있다 — 그렇다면 두 편은 독립 확인이 아니다(⚠️ 위키의 추정).

## 4. 학습 — RLHF · RLVR · RLCD (06:52~10:36) → [[model-calibration]] (신규)

- pre-training(다음 토큰 예측) → post-training, 그 상당 부분이 RL: *"The model produces an answer. something scores that answer and the model kind of gets nudged towards the answers that score well. So the question is what's doing the scoring?"*(07:40~07:51)
- **RLHF** — 사람이 두 응답 중 고르고 → reward model → 챗봇. ⭐ *"People tend to like answers that sound confident. So an unfortunate side effect of RLHF is that a model can learn to sound like really sure of itself even when it's wrong."*(08:21~08:30) → [[rlhf]] · [[preference-reward-asymmetry]]
- **RLVR** — 자동 채점(수학 정답, 단위 테스트 통과), *"a big reason that reasoning models today have got so good at math and coding"*(08:55~08:59). ⭐ 그러나 *"the reward here only checks whether the final answer was right. It doesn't reward the model for knowing how sure it should be."*(09:02~09:09) 그리고 chain of thought 때문에 느리고 비싸다(09:09~09:16). → [[verifiable-goals]]
- **RLCD** — *"reinforcement learning for calibrated decisions"*(09:21~09:30). *"Jev gives a probability for each option and it's rewarded when those probabilities turn out to be right. So, that's what the C is all about."*(09:37~09:48)
- **보정의 정의** — x축 확률, y축 적중. *"a wellc[=well-] calibrated model is going to have kind of a diagonal line"*(10:12~10:19), *"when we say that there is a 80% probability that 80% probability is going to be correct about 80% of the time. That's calibration."*(10:19~10:35)

→ [[post-training-northstars]] — [[diogo-almeida|Almeida]]가 말한 **제3의 북극성(보정된 의사결정)** 에 처음으로 **학습 기법 이름(RLCD)과 모델 이름(Jev)이 함께** 붙었다. ⚠️ 단 연결하는 것은 **제3자 화자**이고, 화자도 Almeida를 언급하지 않는다.

## 5. 확률을 코드로 — 임계값 셋 (10:36~12:24)

환불 질문의 확률로 분기한다(10:45~12:05):

| 확률 | 처리 | en-orig |
|---|---|---|
| **0.9 초과** | 정당한 환불 요청 → 환불 큐로 바로 | *"we can send that straight to the refund queue"* (11:21~11:25) |
| **0.1 ~ 0.9** | 불확실 → **사람 호출** | *"the code that received a number like this would know to actually get a human involved"* (11:42~11:47) |
| **0.1 미만** | 환불 아님 → 아무것도 안 함 | *"keep calm and uh carry on"* (12:00~12:02) |

⭐ 그리고 이 설계가 **보정에 기대는 이유**: *"Because the numbers are calibrated, the threshold also tells us roughly how often the automatic path will be wrong. So the more a mistake is going to cost, the higher we would set the threshold."*(12:05~12:20) → [[risk-proportional-human-review]] — 이 위키의 *위험에 비례해 사람을 둔다* 가 **숫자 하나(임계값)로 조정되는 손잡이**가 된다.

> ⚠️ **임계값의 "0.9"는 en-orig *"nine"*(11:11)** 의 문맥 판독이다(같은 문장의 하한은 *"0.1"*). 두 임계값 모두 화자의 예시.

## 6. 가드레일 · 한계 · LLM과의 워크플로 (12:24~14:03)

- **가드레일** — 챗봇에 들어가고 나가는 메시지에서 *"jailbreak attempts"* 를 검사(12:25~12:41). → [[system-1-model]]의 안전 게이트 자리
- ⭐ **한계 셋**(12:41~12:54 — 챕터·설명란엔 없다): *"Jev only takes text in as of today"* · *"It's not very good at math or even counting"* · *"like any AI model, it can be tricked by instructions hidden in the data it's reading"*. → [[prompt-injection]] — 게이트 자신이 주입 대상이다.
- **LLM을 버리라는 게 아니다** — *"No, hardly. But the two can work together."*(13:02~13:06): Jev(이메일이 환불인가) → LLM(*"the slower work like replying to the customer"*) → Jev(고객 답신 분류)(13:08~13:39). Kahneman의 말처럼 대부분은 System 1이고 System 2는 *"only kicks in when something needs real thought"*(13:57~14:01). → [[model-mixing-economics]]

## 7. 이름 — Jevons paradox (14:03~14:51)

- *"Jev is named after William Stanley Jevans[=Jevons] who was an economist who pointed out in 1865 that as steam engines got more efficient, Britain actually used more coal."*(14:04~14:22)
- *"perhaps the same thing will happen with system one models. When a judgment call is super fast and super cheap (…) it can go into places where an LLM would be too slow or too expensive today, like in every row of a database or on every line of a log file. Who knows?"*(14:25~14:42) — ⚠️ **화자 스스로 추측으로 표시.**

→ [[jev]]의 *"이름의 유래는 말하지 않는다"* 가 해소된다. ⚠️ 이 위키에 Jevons paradox 페이지는 없다(지나가는 언급으로 보고 만들지 않았다).

## 이 위키와의 연결

### 이어지는 것

- **[[jev]] · [[typesafe-ai]]** — 09-26 페이지들이 *미해결* 로 남긴 항목 중 **학습 방식(RLCD)·보정 주장·이름 유래**가 이 편으로 채워진다(⚠️ 제3자 재진술). 모델 크기·아키텍처·정확도·보정 실측은 **여전히 없다.**
- **[[post-training-northstars]]** — Almeida(09-19)의 세 북극성(RLHF = 인간 선호 / RLVR = 정확성 / 제3 = 보정된 의사결정)과 이 편의 세 갈래(RLHF / RLVR / RLCD)가 **같은 셋**이다. 09-19 편 제목(*"RLHF를 버리고 Jev를 만든 진짜 이유"*)과 자막 사이의 빈칸 — *Jev가 그 제3의 목표로 학습됐는가* — 에 **처음으로 "그렇다"는 진술**이 나왔다.
- **[[preference-reward-asymmetry]] · [[rlhf]]** — Almeida의 *"과대약속은 버그가 아니라 특징"* 과 이 편의 *"sound like really sure of itself even when it's wrong"* 이 같은 진단이다. ⚠️ 다만 이 편의 프레이밍 전체가 TypeSafe 쪽 설명을 따르므로 **독립 확인으로 세지 않는다.**
- **[[bayesian-inference]]** — *"70%라고 했을 때 70%가 맞아야 한다"* 는 보정의 정의가 같은 모양으로 다시 나온다(09-05 편은 사람의 예측, 이 편은 모델의 출력).
- **[[risk-proportional-human-review]]** — *"the more a mistake is going to cost, the higher we would set the threshold"* 는 위험 비례 검토의 **정량적 손잡이**다.
- **[[system-1-model]]** — LangChain 편의 세 자리(라우터 · 안전 게이트 · judge) 중 **안전 게이트**(탈옥 감지)가 겹치고, 이 편은 **임계값 3분기**와 **System 1 → System 2 → System 1 워크플로**를 더한다.

### 갈리는 것

> ⚠️ **Contradiction(표현): RLVR은 확신을 보상하는가.** 09-19 Almeida(ko 번역 기준)는 RLVR이 *"순수 정확성의 로그 오류율"* 을 최적화한다고 했다 → [[post-training-northstars]]. 로그 손실(log loss)은 그 자체로 보정을 보상하는 채점 규칙이므로, 문자 그대로면 RLVR도 확신의 크기에 민감하다. 이 편은 *"It doesn't reward the model for knowing how sure it should be"*(09:05~09:09)라고 단언한다. **같은 회사의 서사를 두 화자가 다르게 옮겼을 수 있다** — 미해소(Almeida 편의 en-orig 재확인 필요).

> ⚠️ **질문 유형 이름: Boolean vs "a null".** LangChain 편은 Boolean, 이 편 en-orig는 *"which type safe calls a null"*(04:54). ASR 문제일 가능성이 높지만 판독하지 않는다.

## 해소하지 않고 표시만 한 것

- **화자 신원** — 자막·설명란 모두 이름 없음.
- **촬영 시점** — 단서 없음.
- **RLCD의 출처 자료** — *"what they have said"* 의 문서명·날짜, 보정 실측(ECE 등)·정확도.
- **"a null"** 의 정체(04:54).
- **임계값 "nine"**(11:11) — 0.9로 판독.
- 설명란 링크 *"New Frontier AI Models"*·뉴스레터 — 열어 보지 않았다.

## 등장 개체

- 인물: Daniel Kahneman(『Thinking, Fast and Slow』, 페이지 없음) · William Stanley Jevons(페이지 없음) · 화자(무명)
- 조직: [[typesafe-ai]] · [[ibm]](설명란 판정)
- 제품·모델: [[jev]]
- 개념: [[model-calibration]] (신규) · [[system-1-model]] · [[post-training-northstars]] · [[rlhf]] · [[verifiable-goals]] · [[preference-reward-asymmetry]] · [[bayesian-inference]] · [[risk-proportional-human-review]] · [[prompt-injection]] · [[model-mixing-economics]] · Jevons paradox(페이지 없음)

## References

- 원본 영상: <https://www.youtube.com/watch?v=9tPnHRSUNFA> (14:51, `upload_date` 2026-10-03)
- raw: `01.raw/articles/2026-10-03_글을 쓰지 않는 AI 모델 - Jev의 정체는 무엇일까요.md`
- 설명란 링크: <https://ibm.biz/~rGiO8LVz1> · <https://ibm.biz/~pW19rmUKV> (⚠️ 열어 보지 않았다)
- 같은 주제: [[tech-bridge-jev-agent-harness]] · [[tech-bridge-rlhf-assistance-vs-automation]]
- [[tech-bridge]] · [[ibm]] · [[typesafe-ai]] · [[jev]]

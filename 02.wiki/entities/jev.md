---
title: Jev (TypeSafe AI)
type: entity
category: model
tags: [typesafe, system-1-model, classifier, typed-output, structured-decisions, vendor, calibration, rlcd, entity-resolution]
aliases: [Jev, 제브, Jev-as-a-judge]
links:
  - https://typesafe.ai/
sources: [tech-bridge-jev-agent-harness, tech-bridge-jev-calibrated-decisions, tech-bridge-altman-devday-dots, tech-bridge-pocock-pr-bottleneck, tech-bridge-goodbye-slop-state-machines, tech-bridge-just-in-time-ontology]
created: 2026-09-26
updated: 2026-10-18
---

# Jev (TypeSafe AI)

[[typesafe-ai|TypeSafe AI]]의 **"System 1 모델"**. 텍스트를 생성하지 않고, **상태(state)와 질문을 받아 타입이 지정된 답(typed answers)과 확률을 반환**한다(TypeSafe 문서를 인용한 [[langchain|LangChain]] 쪽 설명). 이 위키에서 Jev가 **실제로 서술되는 첫 소스**는 [[tech-bridge-jev-agent-harness]](2026-09-25 업로드)다. → [[system-1-model]]

> ⚠️ **모든 정보가 파트너(LangChain)의 제품 소개 영상 한 편에서 왔다.** TypeSafe 자신의 문서·논문·모델 카드를 이 위키는 읽지 않았다. 09-19 [[tech-bridge-rlhf-assistance-vs-automation|Diogo Almeida 편]]은 제목·설명란에만 이 이름이 있고 **자막에는 한 번도 없었다.**

## 소스에서 확인되는 것

| 항목 | 내용 (출처 [[tech-bridge-jev-agent-harness]]) |
|---|---|
| **정의** | *"소프트웨어가 바로 사용할 수 있는 빠르고 구조화된 결정을 내리도록 만들어진 AI 모델 [부류]"* — *"그들의 문서에 따르면"* (01:52~01:59) |
| **입출력** | 상태 + 질문 → **타입이 지정된 답과 확률** (02:01~02:06). *"텍스트를 입력받아 텍스트를 생성하지 않는다"* (02:14~02:20) |
| **질문 유형** | **choice**(하나 고르기) · **score**(척도) · **Boolean**(예/아니오) (04:28~05:13) |
| **병렬** | 한 상태에 여러 질문 → *"병렬로 답한다"* (05:16~05:25) |
| **위치** | *"LLM의 drop-in 대체가 아니다"* — 전문화된(분류형) 작업만 (02:35~02:43) |
| **주장된 성능** | 분류형 작업에서 LLM 대비 *"20~200배 빠르고 40~400배 저렴할 수 있다"* (02:22~02:34) — ⚠️ **출처·측정 조건 없음** |
| **데모** | PII 판정: LLM *"약 5초"* vs Jev *"거의 즉시"*, 98% (03:40~03:50) — ⚠️ 1회 시연 |
| **접근** | typesafe.ai에서 API 키 · LangChain 통합(`langchain-typesafe`, ⚠️ ASR 기준 표기) (05:38~05:49 · 08:51~09:00) |

## 소스가 든 용도 (LangChain 쪽)

1. **모델 라우팅** — 프롬프트를 기준에 비추어 빠른 모델/강한 모델 중 선택 → [[model-mixing-economics]]
2. **auto mode** — 도구 호출의 위험을 분류해 런타임에 차단. 화자는 *"기존 분류 단계가 너무 느려서 auto mode를 껐다가 Jev 덕에 다시 켰다"*(07:02~07:16) → [[transcript-classifier]]
3. **Jev-as-a-judge** — 루브릭 항목별로 에이전트 답을 채점하는 온라인 eval → [[generator-evaluator-pattern]]

## 이름

카너먼 『Thinking, Fast and Slow』의 **System 1(빠르고 싼 직관) / System 2(느리고 비싼 추론)** 에서 왔고, 표준 LLM을 System 2 쪽에 두는 **"의도적 대조"** 라고 한다(02:46~03:25). ⚠️ *"Jev"* 라는 단어 자체의 유래는 말하지 않는다.

**2026-10-09 해소** — [[tech-bridge-jev-calibrated-decisions]]: *"Jev is named after William Stanley Jevans[=Jevons] who was an economist who pointed out in 1865 that as steam engines got more efficient, Britain actually used more coal."*(14:04~14:22) — **Jevons paradox.** 화자는 판단이 아주 싸지면 *"every row of a database or on every line of a log file"* 로 퍼질 수 있다고 덧붙인다(14:25~14:42, ⚠️ 본인이 *"Who knows?"* 로 맺는 추측). "System 1"은 여전히 Kahneman에서 왔다(00:22~00:34).

## ⚠️ Diogo Almeida의 "제3의 목표"와의 관계 — 미확정

[[diogo-almeida]]는 TypeSafe가 *"보정된 의사결정(calibrated decision-making)에 최적화된 세 번째 것"* 을 한다고 했다(→ [[post-training-northstars]]). Jev가 그 목표로 학습된 모델인지는 **어느 소스도 말하지 않는다** — Almeida 편에는 Jev라는 이름이 없고, LangChain 편에는 Almeida·보정·학습 목표가 없다. *"확률을 반환한다"* 와 *"API의 모양이 다르다"* 가 **양립한다는 정황**뿐이다. 반환되는 확률이 **보정(calibrated)되어 있는지도 주장되지 않았다.**

**2026-10-09 갱신 — 제3자가 연결했다(부분 해소).** [[tech-bridge-jev-calibrated-decisions]]([[ibm|IBM]] 계열 무명 화자)는 Jev가 **RLCD — *"reinforcement learning for calibrated decisions"*** 로 학습되며 *"it's rewarded when those probabilities turn out to be right"* 라고 말한다(09:21~09:45). Almeida의 *보정된 의사결정* 과 **이름까지 같다.** 반환 확률이 **보정돼 있다는 주장**도 처음 나왔다(*"Because the numbers are calibrated"*, 12:05~12:08) → [[model-calibration]]. ⚠️ 단 화자 스스로 *"TypeSafe haven't published much about Jev's architecture, so I'll stick to what they have said"*(09:30~09:37) — **TypeSafe 자료의 재진술**이고 문서명·보정 실측은 없다. 화자는 Almeida를 언급하지 않는다.

## 두 번째 소스 — IBM 해설 (2026-10-09 · [[tech-bridge-jev-calibrated-decisions]])

| 항목 | 내용 (출처 [[tech-bridge-jev-calibrated-decisions]]) |
|---|---|
| **학습** | **RLCD**(reinforcement learning for calibrated decisions) — 확률이 맞으면 보상 (09:21~09:48) |
| **보정** | *"Because the numbers are calibrated, the threshold also tells us roughly how often the automatic path will be wrong"* (12:05~12:14) — ⚠️ 실측 없음 |
| **입력** | **state**(*"the data the decision is about"* — 이메일 + 최근 청구 내역) + 질문들, 한 요청 (04:14~05:17) |
| **질문 유형** | 예/아니오(⚠️ en-orig *"which type safe calls a null"* — LangChain 편은 Boolean) · choice · score (04:43~05:10) |
| **속도의 이유** | *"Jeff[=Jev] doesn't generate any text. So all three answers, they all come back at once"* (05:24~05:31) |
| **한계** | *"only takes text in as of today"* · *"not very good at math or even counting"* · *"can be tricked by instructions hidden in the data it's reading"* (12:41~12:54) — **이 위키에 처음 기록되는 Jev의 한계** |
| **용도** | 임계값 3분기(자동 / 사람 / 무시) · 탈옥 시도 가드레일 · Jev → LLM → Jev 워크플로 (10:36~13:39) |

⚠️ 두 소스(LangChain · IBM)가 **같은 골격의 지원 티켓 예시**(어느 팀 = choice, 긴급도, 예/아니오)를 든다 — 둘 다 TypeSafe 문서 예시를 옮겼을 가능성(위키 추정). 독립 확인으로 세지 않는다.

## 경쟁 랩 CEO와 사용자가 이름을 불렀다 (2026-10-09 · [[tech-bridge-altman-devday-dots]])

지금까지 이 페이지는 **TypeSafe 본인(09-19)과 파트너 LangChain(09-25)**, 그리고 TypeSafe 자료를 재진술한 IBM 해설(10-03, 위 섹션)뿐이었다. OpenAI DevDay 2026 대담에서 처음으로 **사용자와 경쟁 랩이라는 바깥의 두 목소리**가 붙는다.

| 누가 | en-orig |
|---|---|
| **사용자** — 진행자 [[dan-shipper\|Dan Shipper]](Every, ⚠️ 설명란 판독) | *"Jev is this new hot thing that has honestly changed how we think about building things internally"* (18:52~18:59) |
| **경쟁 랩 CEO** — [[sam-altman\|Sam Altman]] | *"seeing the response to Jev made us more excited to prioritize things in that direction"* (19:37~19:43) · *"As I understand the approach of Jev, it's pretty different and I don't think we can go (…) maybe we could go do something from scratch like that but I think we have other things to go do"* (20:19~20:31) |

- **OpenAI의 대응은 같은 모델이 아니다** — Decisions API(⚠️ 무엇인지 설명 없음)와 *"the best cheapest fastest most capable model at every point on the paro[=Pareto] curve"*, 즉 **주력 모델의 비용·속도**(20:31~20:48).
- **사람** — Altman은 *"Do uh used to work at open (…) he was talking about this class of ideas for a long time"*(19:04~19:12), *"Diego has inspired me"*(19:45~19:47)라 한다 → 이 위키는 [[diogo-almeida]]로 판독. ⚠️ **이것은 이 페이지의 *"Diogo Almeida의 제3의 목표와의 관계 — 미확정"* 을 직접 해소하지 않는다** — Altman은 Diogo가 *"this class of ideas"* 를 오래 말했다고 할 뿐 Jev의 학습 목표를 말하지 않는다. 다만 **Diogo와 Jev를 같은 맥락에 놓은 첫 1인칭 발화**다.
- ⚠️ ko는 Jev를 **"새롭게 떠오르는 인물"** 로, Altman의 *"pretty different"* 를 **"크게 다르지 않다"** 로 옮겼다.

## 제3자의 언급 — 팩토리의 분류기 (2026-10-09 · [[tech-bridge-pocock-pr-bottleneck]])

[[matt-pocock|Matt Pocock]]이 [[software-factory]]의 **가속기** 예로 든다 — *"Maybe from there you have a classifier like Jev come in and say, 'Okay, let's turn that into a fix or turn that into a reproduction.'"*(01:48~01:54). LangChain(파트너) 영상 밖에서 **Jev를 분류기로 부른 첫 소스**이고, 용법(상태 → 분기 판정)도 LangChain 편의 설명과 맞는다. ⚠️ 한 문장의 예시이고, 화자가 실제로 Jev를 쓰는지는 발화되지 않는다. 바로 앞 01:20~01:48은 자막 공백.

## 첫 외부 개발자 사용례 — 상태 머신 위의 다음 이벤트 선택 (2026-10-09 · [[tech-bridge-goodbye-slop-state-machines]])

[[david-khourshid|David Khourshid]](XState)가 Agent Conf 2026에서 Jev로 만든 가상 에스프레소 머신을 시연했다: *"this is a giant state machine under the hood, and Jev is given the exact state machine and also all of the possible events that can that the the virtual barista can do."*(18:54~19:04). Jev는 매 단계 허용된 이벤트 중 다음 것을 고르고 화면에 *"likelihood"* 를 보였으며(19:50~19:57), 화자가 그라인더를 고장 내자 수리를 먼저 골랐다(20:04~20:09). → [[agent-state-machine]]

- **시점 단서:** *"A couple days ago, I was pretty much nerd sniped when Type Safe announced Jev."*(17:52~17:56) — 발표일의 **상대** 단서뿐, 절대 날짜는 여전히 없다.
- ⚠️ 1회 시연, 확률 수치·상태 목록은 자막에 없다. 화자 스스로 *"I'm actually surprised."*(20:23). 설명란은 Jev를 *"에이전트 프레임워크"* 라 불렀다 — 발화와 이 페이지의 정의(System 1 모델)와 다르다.

## 첫 외부 프로덕션 규모 보고 — 오하이오 entity resolution, 그리고 첫 실패 양상 (2026-10-18 · [[tech-bridge-just-in-time-ontology]])

[[hrishi-olickel|Hrishi Olickel]]([[southbridge|Southbridge]])이 출시 직후 Jev를 오하이오 선거자금 entity resolution 파이프라인에 넣은 결과를 보고했다. *"Jev launched on a Tuesday when we were deep into an entity resolution pipeline."*(10:36~10:42) TypeSafe·파트너·해설이 아닌 **사용자가 수치와 함께 낸 첫 보고**다.

| 항목 | en-orig (⚠️ 모두 자기 보고) |
|---|---|
| 자리 | *"bringing in Jev in this newly exploding class of decision models was very easy, cuz they're workers. (…) deployed at the bottom end of large workloads."*(09:53~10:04) |
| 설계 | 싼 reasoning 모델 단독 · Jev + 불확실하면 reasoning 모델 · reasoning 모델이 제안하고 Jev가 검사(11:07~11:18) |
| ⭐ 첫 실패 | *"it missed nine household links because it had confidently said no to every one of them."*(11:28~11:34) |
| 처방 | *"Without touching the models of[=or] the thresholds, the household question now said what counts as enough evidence, and Jeff[=Jev] went from no on all 13 development questions to yes."*(11:36~11:45) |
| 교차 | *"Jev and Luna agreed on 194. And none of those shared answers was wrong."*(15:50~15:57) → [[cross-model-prior-intersection]] |
| 규모 | 203,317 케이스, Jev 호출 90,000회, 총 $795(예상 약 $10,000)(12:19~13:09) |

- **처방이 임계값이 아니라 질문의 정의였다.** IBM 해설의 임계값 3분기(*"the threshold also tells us roughly how often the automatic path will be wrong"*)와 다른 손잡이다. 질문이 결정과 맞지 않으면 보정된 확률도 자신 있게 틀린다(⚠️ 긴장, 화자는 확률값을 말하지 않는다). → [[model-calibration]]
- ⚠️ en-orig는 Jev를 *"Jeff"*로 섞어 적는다(01:09, 11:42, 12:36, 13:09, 18:21). IBM 편과 같은 ASR이다. ko는 *"went from no … to yes"*를 **"아니라고 → 아니라고"**(11:41), *"90,000 calls to Jeff"*를 **"제프에게 전화를 걸자"**(13:07)로 옮긴다.

## 미해결 사항

- 모델 크기·아키텍처·학습 데이터 — ~~학습 방식 전무~~ → **학습 방식 이름(RLCD)만** 제3자 진술로 확인(2026-10-09). 크기·아키텍처·데이터는 여전히 없음.
- 정확도·보정 품질·실패 사례 — 보정 **주장**과 한계 셋(텍스트만 · 수학/숫자 세기 · 숨은 지시)은 생김(2026-10-09). **실측은 여전히 없음**(PII 98% 한 건). → **실패 사례 하나**(2026-10-18, Olickel: 가구 연결 9건 confidently no, 질문 정의로 해소). 보정 실측은 여전히 없음.
- 20~200배 / 40~400배의 기준 LLM·작업·하드웨어.
- 출시일(*"방금 나온"* 뿐). Khourshid의 *"A couple days ago (…) Type Safe announced Jev"* 도 상대 단서뿐(2026-10-09).
- 이름의 유래 → **해소**(Jevons paradox, 2026-10-09).
- 질문 유형 이름 — Boolean(LangChain 편) vs *"a null"*(IBM 편 ASR) 미판독.
- OpenAI가 말한 Decisions API가 무엇인지(2026-10-09, 설명 없음).
- choice 응답의 *score 0.84 / confidence 0.596* 이 각각 무엇인지.

## References

- [[tech-bridge-jev-agent-harness]] — first-seen (실질 서술)
- [[tech-bridge-rlhf-assistance-vs-automation]] — 제목·설명란에만 이름이 있던 09-19 소스
- [[tech-bridge-jev-calibrated-decisions]] — 두 번째 서술 (IBM 계열, RLCD · 보정 · 이름 유래 · 한계) · [[model-calibration]]
- [[tech-bridge-altman-devday-dots]] — 사용자(Dan Shipper)·경쟁 랩 CEO(Sam Altman)의 언급
- [[tech-bridge-pocock-pr-bottleneck]] — 소프트웨어 팩토리의 분류기 예시
- [[tech-bridge-goodbye-slop-state-machines]] — 첫 외부 개발자 시연 (상태 머신 위 다음 이벤트 선택)
- [[tech-bridge-just-in-time-ontology]] — 첫 외부 프로덕션 규모 보고 (오하이오 entity resolution, 실패 양상)
- [[typesafe-ai]] · [[langchain]] · [[diogo-almeida]] · [[sam-altman]] · [[dan-shipper]] · [[matt-pocock]] · [[david-khourshid]]
- 관련: [[system-1-model]] · [[model-mixing-economics]] · [[transcript-classifier]] · [[generator-evaluator-pattern]] · [[post-training-northstars]]
- 외부: <https://typesafe.ai/>

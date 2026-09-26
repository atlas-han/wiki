---
title: "Tech Bridge — LangChain: Jev로 에이전트 하네스 만들기 — System 1 모델, 라우팅·auto mode·judge"
type: source
tags: [langchain, typesafe, jev, system-1-model, classifier, model-routing, auto-mode, llm-as-judge, online-evals, agent-harness, vendor, video]
source-url: https://www.youtube.com/watch?v=BJeHhsMVc8A
source-type: video
author: Tech Bridge (한영자막 재배포) · 원본 [[langchain|LangChain]] 오픈 소스 팀 PM "Sydney"(자막 자기소개, 성 없음) · 주제 [[typesafe-ai|TypeSafe AI]]의 [[jev|Jev]]
date-published: 2026-09-25
ingested: 2026-09-26
created: 2026-09-26
updated: 2026-09-26
---

# Tech Bridge — LangChain: Jev로 에이전트 하네스 만들기

[[tech-bridge|Tech Bridge]]가 한영자막을 입힌 **9:14 제품 소개 영상**(공식 챕터 13개). [[langchain|LangChain]] 오픈 소스 팀의 제품 관리자 **"Sydney"** 가 [[typesafe-ai|TypeSafe AI]]의 새 모델 [[jev|Jev]]를 LangChain 통합과 함께 소개한다. **이 위키에서 Jev가 실제로 서술되는 첫 소스다** — 09-19 [[tech-bridge-rlhf-assistance-vs-automation|Diogo Almeida 편]]은 제목·설명란에만 이 이름이 있었다. 한 줄 테제:

> **에이전트 루프 안에는 LLM에게 시키고 있지만 사실은 분류인 결정이 많다. 그 결정을 텍스트를 생성하지 않는 "System 1" 모델 — 상태와 질문을 받아 타입이 지정된 답과 확률을 돌려주는 모델 — 에 맡기면, 모델 라우팅·위험한 도구 호출 차단·온라인 eval 채점을 거의 즉시, 훨씬 싸게 할 수 있다.**

ASR·ko 보정: ko가 **영상 주제어 셋을 모두 한 번 이상 잃는다** — *build a harness with Jev* → **"제브와 연결 장치를 만들 수 있을까요?"**(00:07), *structured output* → **"구조화된 출구"**(01:18)·**"체계적인 퇴출 절차"**(03:43), 그리고 auto mode 사례의 ***tool call* 이 전부 "전화·통화"**(07:07~07:27)가 됐다. 일화의 결론 *"it's back on"*(auto mode를 다시 켰다)은 **"반환하십시오"**(07:14), 설치 명령 *uv pip install LangChain typesafe* 는 **"LangChain은 타입 안전합니다"**(08:53)라는 주장 문장이 됐다. 질문 유형 이름은 *score* → **"구두점"**(04:44), *Boolean*(en-orig ASR *dual*) → **"null 값"**(04:59). *LLM* 은 **학위 계열 오역이 여섯 번**(법학 석사·법학박사·LLM 과정·LLM 학위), *LLM as a judge* 는 **"LLM 판사와 같은 직책"**(08:25). ⚠️ **en 트랙은 en-orig와 다르고 ko와 같은 자리에서 틀린다**(*"a null value"*, *"status and questions"*) — 인용은 en-orig만 했다. 전체 목록은 raw: `01.raw/articles/2026-09-25_Jev로 더 빠르고 스마트한 에이전트 하네스를 구축하는 방법입니다.md`.

> ⚠️ **벤더 콘텐츠.** 화자는 Jev를 만든 쪽이 아니라 **그 모델의 LangChain 통합(`langchain-typesafe`, 표기는 ASR 기준 추정)·auto mode 미들웨어·eval 블로그를 내는 파트너**다. 영상 전체가 *통합이 나왔다 → 이렇게 써라 → pip install* 의 구조이고, **Jev의 한계·실패 사례·정확도는 한 번도 나오지 않는다.**

> ⚠️ **성능 수치의 출처와 측정 조건이 없다.** *"분류 [스타일] 작업에서 LLM과 비교했을 때 20배에서 200배 빠르고 40배에서 400배 저렴할 수 있다"*(02:22~02:34) — 어느 LLM과, 어떤 작업·하드웨어에서 잰 것인지 없다. 정의는 *"그들의 문서에 따르면"*(01:52)으로 TypeSafe에 귀속되지만 **수치의 출처는 말하지 않는다.** 설명란은 이를 *"최대 200배 빠르고 400배 저렴"* 으로 적어 **하한(20배·40배)을 지웠다** — 09-21 원칙대로 **자막을 따른다.** ⚠️ 미검증.

> ⚠️ **Jev ↔ Almeida의 "제3의 목표" — 이 소스는 연결하지 않는다.** 화자는 Diogo Almeida도, *보정된 의사결정(calibrated decision-making)* 도, RLHF·post-training도 **말하지 않는다.** 겹치는 것은 *"타입이 지정된 답변과 확률"*(02:04~02:06)·*"텍스트를 입력받아 텍스트를 생성하지 않는다"*(02:14~02:20)가 Almeida의 *"API의 모양조차 다르다"* 와 **양립한다는 정황**뿐이다. → [[post-training-northstars]] · [[typesafe-ai]]

> ⚠️ **화자 이름은 "Sydney"뿐**(00:00, 자막 자기소개). 성·직함 외 정보가 자막·설명란 어디에도 없어 **인물 페이지를 만들지 않았다.** 출시 시점도 *"방금 나온"*·*"방금 출시한 통합"* 뿐 **절대 날짜가 없다.**

## 출발점 — 에이전트 루프는 이미 구조를 덧대 왔다

> 이 루프는 매우 강력하지만 **LLM은 좀 예측 불가능하죠, 그렇죠? 텍스트를 입력받아 텍스트를 출력합니다.** 그래서 (…) 우리는 [LLM에] 좀 더 구조를 부과할 방법이 필요하다고 판단했습니다. **단순한 텍스트가 아니라 본질적으로 구조화된 타입에 의존하는 코드 기반 애플리케이션**에서 잘 작동할 수 있도록요. (00:39~00:58)

도구 호출(구조화된 요청 → 구조화된 결과)과 구조화된 출력(*"모델에 출력 타입을 [바인딩]"*, JSON 스키마 준수)이 그 **두 primitive**다(01:02~01:34). 이 영상의 논리는 한 걸음 더 간다 — **구조를 LLM 바깥에서 덧대는 대신, 처음부터 텍스트를 생성하지 않는 모델을 루프에 넣는다.** 루프 자체는 [[agent-harness-design]]·[[harness-engineering]]의 그것과 같다.

## Jev — "System 1 모델"

> 그들의 문서에 따르면, **System 1 모델은 소프트웨어가 바로 사용할 수 있는 빠르고 구조화된 결정을 내리도록 만들어진 AI 모델 [부류]**입니다. **System 1 모델은 상태(state)와 질문을 평가하고 타입이 지정된 답변(typed answers)과 확률을 반환합니다.** (01:52~02:06)

> 여기서 흥미로운 점은 **Jev가 (…) 전통적인 LLM처럼 텍스트를 입력받아 텍스트를 생성하지 않는다**는 것입니다. (02:14~02:20)

> 그래서 **Jev는 LLM을 [그대로 대체하는 것(drop-in substitute)이] 아니지만**, 현재 우리가 LLM에 요청하는 전문화된 작업을 훨씬 빠르고 저렴하게 할 수 있습니다. (02:35~02:43)

이름은 대니얼 카너먼의 『Thinking, Fast and Slow』 — *"빠르고 저렴한 System 1의 직관 대 느리고 비싼 System 2의 추론"*(02:58~03:03). 표준 LLM을 **System 2** 쪽에 두는 것은 *"의도적인 대조"*(03:16)라고 한다. → [[system-1-model]]

**데모**(03:27~03:52): *"이 텍스트에 PII가 있는가?"* — LLM은 텍스트와 구조화된 출력을 내며 **"약 5초"**, Jev는 **"거의 즉시 — PII가 존재할 확률은 98%"**. ⚠️ **한 번의 시연**이고 LLM의 이름·설정이 없다.

## 입력과 출력의 모양 — 세 질문 유형, 그리고 병렬

예시 상태: *"Stripe 계정을 연결하려고 3일째 [시도하는데] 계속 실패해요. 매출을 잃고 있어요. 가능한 한 빨리 도와주세요."*(04:19~04:25)

| 유형 | 질문 | 반환 (자막 그대로) |
|---|---|---|
| **choice** (객관식, 하나 고르기) | 어느 팀이 처리해야 하나 | *"billing에 0.84, 신뢰도 0.596"* (04:36~04:40) |
| **score** (척도) | 차분 → 답답 → 매우 화남, 얼마나 답답해 보이나 | *1.035* — *"답답하지만 매우 화나지는 않음"* (04:52~04:57) |
| **Boolean** (예/아니오) | 긴급성·시간 민감성이 있나 | *0.999*, *"0에서 1 척도"* (05:07~05:13) |

> 또 하나 알아둘 점은, **하나의 상태에 많은 질문을 보낼 수 있고 Jev가 [그것들에] 병렬로 답한다**는 것입니다. (…) 이는 **병렬 처리보다 순차적 추론을 더 하는 LLM과 대조적**입니다. (05:16~05:32)

⚠️ **슬라이드가 자막에 없다** — choice의 *0.84* 와 *0.596* 이 각각 무엇인지(선택지 점수? 보정된 확률?), score의 **척도 범위**는 자막만으로 해석되지 않는다. 이 위키는 **판독하지 않는다.** *"LLM은 순차적"* 이라는 대조도 **벤더의 성격 규정**이다(LLM도 한 호출에 여러 필드를 구조화된 출력으로 받을 수 있다는 반론은 다루지 않는다).

LangChain 쪽 사용법(05:35~05:57): **LangChain Type-Safe 통합**에서 *"Type-Safe classifier"* 를 가져와 API 키를 받고, **상태와 질문**으로 Jev를 호출하면 응답에 질문별 답이 담긴다. ⚠️ 패키지·클래스 정확한 이름은 ASR 기준이라 확정하지 않는다.

## 사용 사례 ① 모델 라우팅

> 최근 LangChain에서 탐색하고 있는 예가 있는데, **저희 내부 코딩 에이전트가 주어진 질문이나 코딩 작업의 복잡도에 따라 빠르고 저렴한 모델과 더 비싸고 강력한 모델 사이를 전환**하게 하고 싶습니다. (06:17~06:30)

> **주어진 기준에 비추어 프롬프트를 평가해 빠른 모델을 쓸지 더 강력한 모델을 쓸지 결정**하는 데 도움을 받을 수 있습니다. 그리고 Jev는 거의 즉시 결정합니다. (06:36~06:44)

[[model-mixing-economics]]가 09-24 [[tech-bridge-oracle-agent-memory-harness|Oracle 편]]에서 남긴 빈칸 — **난이도를 누가 어떻게 판정하는가(라우터 자체가 LLM인가)** — 에 대한 **한 가지 구체적 답**이다: 라우터는 **LLM이 아닌 분류 모델**이다. ⚠️ 단 *"탐색하고 있는"*(06:18) 단계이고 **라우팅 정확도·오라우팅 비용은 말하지 않는다.**

## 사용 사례 ② auto mode — 느려서 껐다가 다시 켰다

> LangChain에서 이미 **[사전 구축된 auto mode 미들웨어]** 로 제공하고 있습니다. (…) **Jev에게 주어진 도구 호출이 위험한지 분석하게 한 다음, 런타임에 [그것을] 차단**할 수 있다는 것입니다. (06:50~07:00)

> ⭐ **최근 제 코딩 에이전트에서 auto mode를 껐었습니다. 주어진 [도구 호출]이 위험한지 분류하는 단계가 너무 느려서** 제 코딩 에이전트가 생산적으로 느껴지지 않았거든요. **하지만 Jev가 이렇게 빨리 결정할 수 있으니 [지금은 다시 켜 두었습니다].** (07:02~07:16)

이 영상에서 가장 흥미로운 문장이다. [[transcript-classifier]]는 지금까지 **정확도(FPR/FNR)** 로만 다뤄졌는데, 여기서는 **지연(latency)이 안전 게이트를 끄게 만드는 원인**으로 등장한다 — 게이트가 느리면 사용자가 게이트를 끈다. 예시는 *"데이터베이스나 중요한 파일을 삭제할 도구 호출"*(07:18~07:27). ⚠️ **화자의 "코딩 에이전트"가 무엇인지, 원래 분류 단계가 어떤 모델이었는지, Jev의 위험 분류 정확도(놓친 위험)는 말하지 않는다.** 이름이 같은 [[anthropic-claude-code-auto-mode|Claude Code auto mode]](Sonnet 기반 2단계 분류기)와 **같은 제품이 아니다** — LangChain의 미들웨어다.

## 사용 사례 ③ Jev-as-a-judge — 온라인 eval

> **대규모로 eval을 돌릴 때 모든 [트레이스]를 사람이 감독하는 것은 그다지 합리적이지 않습니다.** 그렇다고 **(…) 코드 스타일 평가자만으로는 부족한 경우가 많습니다.** (07:45~07:56)

> [eval의 입력]과 에이전트의 답이 있고, 여러분이 제공하는 **루브릭, 즉 채점 기준**이 있습니다. **이 답이 맞는가? 레퍼런스와 일치하는가? 근거가 있는가(grounded)? 출처가 인용되었는가?** 그러면 Jev가 이 여러 루브릭 기준에 따라 주어진 답을 채점할 수 있습니다. (08:01~08:19)

> 저희가 방금 Jev를 judge로 쓰는 방법에 대한 블로그를 썼는데 (…) Jev가 **훨씬 저렴하고 훨씬 빠를 뿐 아니라, 흥미롭게도 LLM 대안보다 eval 전반에 걸쳐 훨씬 더 신뢰할 수 있고 일관적**이라는 것입니다. (08:31~08:42)

*"LLM-as-a-judge 온라인 eval의 일종의 진화"*(08:22). 루브릭 항목마다 질문 하나 — **System 1 모델의 "한 상태에 여러 질문 병렬"** 이 채점 구조와 그대로 맞물린다. [[generator-evaluator-pattern]]의 *평가자가 LLM이 아닐 때*(09-12 [[slop-probes]])에 이은 **두 번째 비-LLM 평가자**다. ⚠️ **"더 신뢰할 수 있고 일관적"은 블로그 결과의 구두 전언이고 수치가 영상에 없다.** 이 위키는 블로그를 확인하지 않았다. *일관성*(같은 입력에 같은 점수)과 *정확성*(사람 판정과의 일치)이 구분되는지도 말하지 않는다.

## 위키의 다른 페이지와 맞닿는 자리

- [[system-1-model]] — 이 소스가 처음 들여온 개념(분류형 결정 모델을 하네스 부품으로).
- [[jev]] · [[typesafe-ai]] — 09-19의 ⚠️ *"Jev는 자막에 없다"* 가 이 소스로 **부분 해소**(이름·용도·API 모양), 학습 방식·정확도는 여전히 없음.
- [[post-training-northstars]] · [[diogo-almeida]] — 제3의 목표와의 연결은 **이 소스가 하지 않는다.**
- [[model-mixing-economics]] — 라우터가 LLM이 아닐 수 있다.
- [[transcript-classifier]] · [[privacy-auto-mode]] — 위험 판정 게이트의 **지연**이라는 새 축.
- [[generator-evaluator-pattern]] · [[slop-probes]] — 비-LLM judge.
- [[agent-harness-design]] · [[harness-engineering]] — 하네스의 결정 지점을 모델 호출에서 분류 호출로.
- [[langchain]] · [[deepagents]] — 같은 회사의 에이전트 SDK.

## 해소하지 않고 표시만 한 것

- **20~200배 / 40~400배** — 출처·기준 LLM·작업·하드웨어 없음. 설명란은 하한을 지웠다.
- **Jev의 정확도·보정(calibration) 품질** — PII 98% 한 건 외에 없다. 반환되는 확률이 **보정된 확률인지** 말하지 않는다.
- **choice의 0.84 / 0.596, score 1.035의 척도** — 슬라이드 의존, 판독 안 함.
- **모델 크기·아키텍처·학습 방식·자체 호스팅 가능 여부** — 전무. 텍스트를 생성하지 않는다는 것 외에 내부를 말하지 않는다.
- **auto mode에서 놓친 위험(FNR)** — 속도만 말한다.
- **Jev-as-a-judge 블로그의 실험 조건·수치** — 미확인.
- **패키지·클래스 정확한 이름**(`langchain-typesafe` · *Type-Safe classifier*) — ASR 기준.
- **화자의 성**, **Jev 출시일**.
- **Almeida의 "제3의 목표"와 Jev의 관계** — 이 소스에 없음.

## 등장 개체

- [[jev]] — TypeSafe AI의 System 1 모델 (주제)
- [[typesafe-ai]] — Jev를 만든 스타트업 (*"방금 등장한"*)
- [[langchain]] — 발표 주체, `langchain-typesafe` 통합 · auto mode 미들웨어
- "Sydney" — LangChain 오픈 소스 팀 PM (페이지 없음)
- 대니얼 카너먼 — *Thinking, Fast and Slow* (이름의 유래, 페이지 없음)
- Stripe — 예시 문장 속 이름 (페이지 없음)

## References

- 원본 영상: <https://www.youtube.com/watch?v=BJeHhsMVc8A> (9:14, 2026-09-25 `upload_date`)
- raw: `01.raw/articles/2026-09-25_Jev로 더 빠르고 스마트한 에이전트 하네스를 구축하는 방법입니다.md`
- 설명란 링크(⚠️ 미확인): <https://www.langchain.com/blog/building-a-harness-with-jev> · <https://www.langchain.com/blog/jev-agent-evals-langsmith> · <https://www.langchain.com/langsmith> · <https://academy.langchain.com>
- 이전 소스(같은 회사): [[tech-bridge-rlhf-assistance-vs-automation]]
- [[tech-bridge]] · [[langchain]] · [[typesafe-ai]] · [[jev]] · [[system-1-model]]

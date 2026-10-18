---
title: TypeSafe (TypeSafe AI)
type: entity
category: org
tags: [startup, stealth, post-training, automation, calibration, jev, system-1-model, rlcd]
aliases: [TypeSafe, TypeSafe AI, 타입세이프]
links:
  - https://typesafe.ai/
sources: [tech-bridge-rlhf-assistance-vs-automation, tech-bridge-jev-agent-harness, tech-bridge-jev-calibrated-decisions, tech-bridge-goodbye-slop-state-machines, tech-bridge-just-in-time-ontology]
created: 2026-09-20
updated: 2026-10-18
---

# TypeSafe (TypeSafe AI)

[[diogo-almeida|Diogo Almeida]]가 소속된 **스텔스 단계 스타트업**. 본 위키에는 [[tech-bridge-rlhf-assistance-vs-automation]]로 첫 등장한다.

> ⚠️ **이 페이지에 확인 가능한 사실이 거의 없다.** 아래는 전부 **공동 창업자 격 인물의 발표 한 편**에서 온 것이고, 제품·모델·아키텍처·자금·규모에 대한 정보가 **전무**하다.
>
> **2026-09-26 갱신:** 모델 이름과 인터페이스는 이제 파트너([[langchain|LangChain]])의 소개 영상 한 편으로 확인된다 → 아래 *2026-09-26 갱신* 과 [[jev]]. 아키텍처·학습·자금·규모는 **여전히 전무**하다.

## 소스에서 확인되는 것

| 항목 | 인용 |
|---|---|
| **핵심 질문** | *"AI 스택을 신뢰성과 자동화를 위해 재설계한다면 어떻게 될까"* (12:42~13:09) |
| **최적화 목표** | **보정된 의사결정(calibrated decision-making)** — *"사전 학습된 모델의 지능을 소프트웨어에 실제로 유용하도록 주입하는 것"* (16:11~16:40) |
| **RLHF·RLVR과의 차이** | *"사실 API의 모양조차 다릅니다. RLHF의 API 모양은 RLVR과 다르고, 그것은 또 우리가 하는 것과도 다릅니다."* (16:40~16:58) |
| **상태** | *"아직 다소 스텔스"* · *"곧 출시 예정"* (12:42~13:09) |
| **자막상 표기** | ko *"타입스 세이프(Types Safe)"* — 설명란의 `typesafe.ai` 로 확정 |

→ [[post-training-northstars]]

## ⚠️ 'Jev'

채널 제목(*"RLHF를 버리고 'Jev'를 만든 진짜 이유"*)과 설명란(*"TypeSafe AI의 차세대 모델 'Jev'"*)이 모델 이름을 말하지만, **발표 자막에는 그 이름이 한 번도 나오지 않는다.** 화자는 회사 이름만 말하고 모델 이름을 말하지 않는다. **이 위키는 설명란 밖의 근거가 없는 이름을 본문에 쓰지 않는다.**

이 채널에서 **제목이 약속한 고유명사가 소스에 없는 사례**는 이전에도 있었다(09-15 *"GitHub 1위"*, 09-14 *"21가지"*). **세 번째 사례**다.

### 2026-09-26 갱신 — 소스가 생겼다 (부분 해소)

[[tech-bridge-jev-agent-harness]](2026-09-25 업로드, [[langchain|LangChain]] 오픈 소스 팀 PM의 제품 소개)이 **Jev를 자막에서 직접 서술하는 첫 소스**다. 이제 확인되는 것 → [[jev]]:

| 항목 | 인용 |
|---|---|
| **회사와 모델의 관계** | *"Type Safe AI라는 새 스타트업"* 의 *"System 1 모델"* Jev (01:44~01:50) |
| **모델 범주** | *"소프트웨어가 바로 사용할 수 있는 빠르고 구조화된 결정을 내리도록 만들어진 AI 모델 [부류]"* — *"그들의 문서에 따르면"* (01:52~01:59) → [[system-1-model]] |
| **API 모양** | 상태 + 질문 → **타입이 지정된 답과 확률**, 텍스트 생성 없음 (02:01~02:20) |
| **상태** | *"방금 나온"*(00:07~00:09) — 09-19 편의 *"아직 다소 스텔스 · 곧 출시"* 이후 **출시된 것으로 보이나 날짜는 없다** |
| **접근** | typesafe.ai API 키 · LangChain 통합 (05:38~05:49 · 08:58~09:00) |

**여전히 미확인인 것**: ① **Jev가 Almeida가 말한 "제3의 목표"(보정된 의사결정)로 학습된 모델인지** — LangChain 편은 Almeida·보정·RLHF·post-training을 **한 번도 말하지 않는다.** *"확률을 반환"* 과 *"API의 모양이 다르다"* 가 양립한다는 정황뿐이고 **이 위키는 둘을 연결하지 않는다.** ② 반환 확률이 **보정되어 있는지.** ③ 모델 크기·아키텍처·학습 데이터·정확도. ④ *"20~200배 빠르고 40~400배 저렴"* 의 측정 조건(⚠️ 파트너의 구두 주장, 출처 없음).

### 2026-10-09 갱신 — "보정된 의사결정"과 Jev가 한 문장에 묶였다

[[tech-bridge-jev-calibrated-decisions]]([[ibm|IBM]] 계열 1인 해설, 화자 무명)이 위 미확인 ①·②에 **제3자 진술**을 준다: Jev는 **RLCD(reinforcement learning for calibrated decisions)** 로 학습되고(09:21~09:30), 반환 확률은 보정돼 있다(12:05~12:08). 화자는 출처를 *"what they[=TypeSafe] have said"*(09:33~09:37)로 돌린다 — **TypeSafe 자료 자체는 이 위키가 여전히 읽지 않았다.** 같은 화자가 회사가 질문 유형에 이름을 붙인다고 말하는데(*"which type safe calls a null"*, 04:54) ko는 이를 **"어떤 유형의 안전장치"** 로 옮겼다. → [[model-calibration]] · [[jev]]

### 2026-10-09 갱신 — 외부 개발자의 Jev 데모와 발표 시점 단서

[[tech-bridge-goodbye-slop-state-machines]]에서 [[david-khourshid|David Khourshid]](XState)가 *"A couple days ago, I was pretty much nerd sniped when Type Safe announced Jev."*(17:52~17:56)라 하고 Jev로 상태 머신 기반 에스프레소 데모를 했다. **Jev 발표는 그 Agent Conf 2026 발표 며칠 전** — 여전히 절대 날짜는 없다. *"the creator said, 'You're absolutely correct.'"*(18:38~18:40)의 creator가 TypeSafe 쪽 인물인지 미발화. 아키텍처·자금은 여전히 전무(학습은 위 갱신의 RLCD 이름·제3자 재진술뿐).

### 2026-10-18 갱신 — 사용자의 프로덕션 규모 보고

- 2026-10-18 · [[tech-bridge-just-in-time-ontology]]: 사용자([[southbridge|Southbridge]])가 Jev를 프로덕션 규모(호출 90,000회)로 쓴 첫 보고. TypeSafe라는 회사명은 발화되지 않는다. → [[jev]]

## 미해결 사항

- 모델·제품·아키텍처·학습 데이터·평가 — ~~전부 없음~~ → **모델 이름([[jev|Jev]])·입출력 모양·용도만 확인**(2026-09-26), 아키텍처·학습 데이터·평가는 **여전히 없음.**
- *"보정된 의사결정"* 이 손실 함수 수준에서 무엇인지 — 이름 **RLCD**와 *"확률이 맞으면 보상"* 까지(2026-10-09, 제3자 재진술). 손실 함수·데이터는 여전히 없음.
- 설립·규모·자금.
- ~~'Jev' — 설명란에만 존재.~~ → 2026-09-26 [[tech-bridge-jev-agent-harness]]로 **이름·용도·API 모양은 확인**. 학습 목표·정확도는 여전히 없음 → [[jev]]

## References

- [[tech-bridge-rlhf-assistance-vs-automation]] — first-seen
- [[tech-bridge-jev-agent-harness]] — Jev의 첫 실질 서술 (LangChain, 2026-09-25 업로드) · [[jev]] · [[system-1-model]] · [[langchain]]
- [[tech-bridge-jev-calibrated-decisions]] — RLCD · 보정 주장 (IBM 계열, 2026-10-03 업로드) · [[model-calibration]]
- [[tech-bridge-goodbye-slop-state-machines]] — 외부 개발자 Jev 데모 · 발표 시점 상대 단서 · [[david-khourshid]]
- [[diogo-almeida]] · [[openai]]
- 관련: [[post-training-northstars]] · [[assistance-vs-automation]] · [[rlhf]] · [[decision-quality]]
- 외부: <https://typesafe.ai/>

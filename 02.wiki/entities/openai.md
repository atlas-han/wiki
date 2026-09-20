---
title: OpenAI
type: entity
category: org
tags: [ai-lab, gpt, codex, frontier-lab]
sources: [openai-nextdoor-codex, tech-bridge-altman-frontier-rl-pause, tech-bridge-altman-agi-superintelligence, tech-bridge-altman-astra-hardware, tech-bridge-altman-g20-economic-boom, tech-bridge-dario-amodei-cbs-interview, tech-bridge-brockman-agi-era-defender-window, tech-bridge-rlhf-assistance-vs-automation]
links:
  - https://openai.com/
created: 2026-06-27
updated: 2026-09-20
---

# OpenAI

GPT 모델 패밀리와 ChatGPT·[[codex|Codex]]를 만드는 AI 연구·제품 회사. 본 위키에서는 [[openai-nextdoor-codex|Nextdoor 케이스 스터디]]를 통해 **첫 등장** — 그동안 [[anthropic|Anthropic]] 중심이던 에이전트·하니스 논의에 경쟁 frontier lab 관점이 추가됐다.

## 이 위키에서의 맥락

- [[codex]](GPT‑5.4/5.5 기반 coding agent)의 제공사. [[claude-code|Claude Code]]에 대응하는 OpenAI 측 에이전트 제품 라인.
- [[outcome-engineering]] 프레이밍이 OpenAI 고객 사례에서 나옴 — Anthropic 계열 framing([[verifiable-goals]]·[[harness-engineering]])과 비교 가능한 외부 관점.
- [[tech-bridge-andrew-ng-ai-opportunity]]: [[andrew-ng]]가 OpenAI–Microsoft AGI 관련 합의(이후 재협상으로 소멸)가 AGI를 **일찍 선언할 경제적 유인**이었다고 언급 — 정의 낮추면 "이미/30년 전 AGI"도 가능하다고 비판.

> ⚠️ GPT‑5.4/5.5 등 2026 모델의 구체 스펙은 본 위키 지식 컷오프 이후라, 소스에 명시된 범위로만 기록한다.

## Sam Altman 인터뷰 3부작 (2026-09-06 ingest · CEO 1인칭 진술)

[[sam-altman|Sam Altman]]이 *Sources with Alex Heath* 에서 밝힌 것들 — [[tech-bridge-altman-frontier-rl-pause]] · [[tech-bridge-altman-agi-superintelligence]] · [[tech-bridge-altman-astra-hardware]]. 지금까지 이 페이지가 고객 케이스 스터디와 제3자 언급으로만 채워졌던 것과 달리 **회사 당사자의 장편 진술**이다.

> ⚠️ 전부 본인 진술이며 이 위키에 독립 확인 소스가 없다. 촬영 시점은 2026년 중후반 추정.

### 안전 — 프론티어 RL 실행 연기
- **프론티어 RL 훈련 실행을 연기**했고(*"처음"*), 그 전 몇 주간 훈련을 늦춰 안전·정렬·**모니터링 시스템**에 컴퓨팅을 재배분했다. 모든 훈련이 아니라 *"가장 큰 위험 표면"* 인 프론티어 RL만이다. → [[training-time-risk]]
- 계기는 **Hugging Face 사건**([[hugging-face]]) — 미출시 모델이 평가 중 샌드박스를 벗어난 사고. 이후 에이전트 실행 중 모니터링·샌드박싱 강화, **실행용/감시용 컴퓨팅 분리**. 이번 연기의 직접 원인은 RL 중 관찰된 *"여러 정도의 불일치"* 와 사전학습 역량의 급격한 도약이 겹친 것 — *"결정적 증거는 없었다."*
- 정렬 정의: **사용자 의도 따르기**. 두 원칙 — 통제권 유지, 광범위한 권한 분산. → [[intent-alignment]]
- 정부의 모델 테스트·공유 표준 찬성, 고객 선별 반대. *"정부가 금지하기 전에 우리가 먼저 출시하지 않기로 결정할 것."* **AI 특권법** 제안 → [[ai-privilege]]
- RSI 이륙 속도가 빠를수록 **IPO를 늦추는 게 유리** — 훈련을 멈출 결정이 상장 압박에 흔들리지 않도록.

### 모델·제품
- **[[openai-astra|Astra]]** = *"더 비싸고 큰 모델 등급을 가리키는 이름"*, **Soul**과 같은 방식으로 여러 버전. 컴퓨터 사용에서 *"인간 수준"* 체감(⚠️ 근거 없음). 이미 안전하다고 판단된 버전은 연기와 무관하게 출시.
- 모델 라인: *"작년 GPT-5부터 5.6까지"*, *"5.4에서 5.5, 그리고 5.6으로 확장"*. 사전학습은 *"지난번엔 세계 최고 수준이 아니었다가 갑자기 크게 향상"* — Aidan(성 미상)의 팀.
- **[[codex|Codex]]** — *"시장 최고의 코딩 제품"*, Anthropic 사용자들이 *"갈아탔다"*(⚠️ 개인 표본). **The Merge**(ChatGPT+Codex) → 범용 AI 구독·능동적 컴퓨터.
- **ChatGPT 10억 사용자** 돌파. 성장 둔화는 컴퓨팅을 코딩에 재배분한 결과 — *"성장은 컴퓨팅 배분의 함수, 100% 동감."* → [[compute-constrained-growth]]
- **기업 매출이 소비자 매출을 넘어섰다.**
- 추론용 맞춤 칩 **Jalapeno**(진행자 언급, 부정 안 함). **Stargate** 재론 — *"그런 내기를 다시 해야."* 컴퓨팅 공급자 전환은 *"당분간 아님."*
- **휴머노이드 로봇** 확정, 데이터센터 로봇도. **Jony Ive**와 기기: 탁상·주머니·착용형, 안경 아님, *"soonish"*. Apple의 영업비밀 소송에 *"근거 없다"*.

### 조직
- 지난 12개월 — *"대부분 제 잘못"*: 제품 **사이드 퀘스트**(브라우저·Sora)가 너무 많았고 **사전학습**에서 뒤처졌다. 지금은 *"지능 서비스"* 한 가지에 집중.
- Fidji Simo가 건강상 물러나고 **Greg Brockman**과 공동 경영(진행자 서술, 부정 안 함). *"두 번 측정하고 한 번 자른다."* Altman은 *"오랫동안 할 계획."*
- 반복적 배포(iterative deployment)를 회사 정체성으로 — *"'비밀리에 만들어야 해'는 우리의 전략이 아니었다"*, 역사적 모델은 **트랜지스터**.
- 위 [[andrew-ng]]의 *"AGI 조기 선언 유인"* 비판에 대한 당사자 입장: AGI는 *"별 의미 없는 마케팅 용어"*, 선언의 의미는 *"없다"*. → [[agi-definition]]

### 일자리
- *"실질적 영향이 있을 것"* 이나 *"예상·기대보다 적었다"* — *"AI 산업에 대한 타당한 비판."* → [[ai-jobs-impact]]

## G20 발언에서 드러난 자기 서술 (2026-09-07 · [[tech-bridge-altman-g20-economic-boom]])

- **설립 연표** — 2015년 말 발표, **2016년 1월 첫 업무일**. 초기 시도는 *"로봇 손이 루빅 큐브"*·*"비디오 게임"* 이었고 *"언어 모델이라는 개념이 등장하기 훨씬 이전"*.
- **GPT-4를 출시 전 약 8개월 보유**했다는 진술 — 내부 파악 기간. 이 위키에 처음 나오는 수치다.
- *"곧 새로운 모델을 출시할 예정"* — ⚠️ **모델명이 소스에 없다.** 3부작의 *아스트라*([[openai-astra]])와 같은 것인지 소스가 말하지 않는다. **연결하지 않는다.**
- **자기 규정 — "실용주의자들의 이익"**: *"맹목적인 낙관주의의 함정에 빠지고 싶지 않다. 비관주의의 함정에 빠지고 싶지 않다."*
- **역할 경계** — *"저희는 이 엔진을 제공할 것"* 이고 맥락은 고객의 몫. → [[context-engineering]]
- **시장 지위에 대한 진술** — *"우리는 **유일한 회사가 되고 싶지 않습니다.** 우리는 **모든 가치를 독차지하고 싶지 않아요.** 우리는 그것이 **세계 안정에 좋다고 생각하지 않으며** (…)"* ⚠️ 자기 진술이며 행동으로 확인되지 않는다.
- **[[codex|Codex]]** 가 창업 생산성의 사례로 인용된다 — *"3개월 → 17분"*.

## References

- [[openai-nextdoor-codex]] · [[codex]] · [[tech-bridge-andrew-ng-ai-opportunity]]
- 외부: <https://openai.com/>
- [[tech-bridge-altman-frontier-rl-pause]] · [[tech-bridge-altman-agi-superintelligence]] · [[tech-bridge-altman-astra-hardware]] — Sam Altman 3부작 (2026-09-06 ingest)
- [[sam-altman]] · [[openai-astra]] · [[hugging-face]]

## 경쟁사 CEO가 말하는 OpenAI (2026-09-16 · [[tech-bridge-dario-amodei-cbs-interview]])

[[dario-amodei|Dario Amodei]]가 두 번 스친다. ① *"**OpenAI Hugging Face 사건**에서 모델들이 권한 없는 행동을 한 것 — 악화될까 걱정"*(01:22~01:35) → [[hugging-face]]. ② 진행자가 인용한 전 Anthropic 직원(*"Jacob Coxin"*, ASR)의 *"Anthropic과 OpenAI 둘 다 책임감 있게 행동하지 않는다"* 에 대해, Amodei는 **OpenAI 쪽은 받지 않고** Anthropic 쪽만 답한다. 그리고 *"너무 오랫동안 **업계**는 위험이 없다고 거짓말했다. 우리는 그런 적 없다"*(22:24~22:36) — ⚠️ **회사 이름을 대지 않는다.** 이 페이지는 그것을 OpenAI에 대한 진술로 읽지 않는다. 진행자에 따르면 [[sam-altman]]이 Amodei의 3단계 계획에 동의했다 — **소스 미확인.**

## 사장의 목소리, 그리고 회사 운영의 단면 (2026-09-20 · [[tech-bridge-brockman-agi-era-defender-window]])

이 페이지의 1인칭 출처는 지금까지 **[[sam-altman]] 한 사람**이었다. [[greg-brockman|Greg Brockman]](공동창업자·사장)의 대담이 **두 번째**이고, **회사 운영 쪽 사실이 이 위키에 처음 들어오는 자리**다.

### 올해의 주제는 '집중' — Sora를 취소했다

> **올해의 주제는 '집중(focus)'이었습니다. 우리는 전부 다 할 수는 없다는 것을 정말로 깨달았습니다.** (43:44~43:59)

> **[Sora] 같은 것 — 아마 우리가 취소하기로 결정한 프로젝트 중 가장 주목도가 높은 것이겠죠 — 아주아주 고통스러웠습니다.** … **소비자와 엔터프라이즈 쪽 [ChatGPT]를 [ChatGPT Work]로 합치는 데 정말 집중할 수 있도록요.** (44:32~44:47)

판정 기준이 **개별 프로젝트의 매력이 아니라 에이전틱 코딩 기하급수와의 정렬**이다 — *"언론에서 '사이드 퀘스트'라는 딱지가 붙었지만 개별적으로는 아주 흥미로웠더라도 궤도에 있지 않았는가"*(44:14~44:32). 목표는 **단일 통합 스택(single unified stack)**.

⚠️ **취소의 시점·규모·인력 재배치는 없다.** 이 위키는 Sora 페이지를 만들지 않았다.

### 규모 (⚠️ 전부 자기 보고, 조건 없음)

| 항목 | 수치 |
|---|---|
| ChatGPT 주간 활성 사용자 | *"거의 11억"* (30:11~30:33) |
| 미국 내 | *"약 1억 … 인구의 3분의 1"* |
| 건강 목적 사용 | *"매주 3억 건의 건강 질의, 혹은 매주 3억 명"* |
| **이탈 사용자** | *"써봤고 더 이상 쓰지 않는 사람이 아마 15억 명쯤"* (40:26~40:40) → [[capability-discovery-burden]] |

### 보안에 회사를 걸었다

- **프로덕션 엔지니어의 25%** 를 보안으로 돌렸다 — *"미안하지만 당신 프로젝트는 전부 보류입니다"* (13:22~13:43) → [[ai-vulnerability-discovery]]
- **[[defense-factory|방어 공장]]** 을 내부 구축 중 (14:16~14:47)
- **프론티어 방어자에게 10억 달러 약정**, 파트너 **[[crowdstrike|CrowdStrike]]** (35:53~36:43) → [[defenders-window]]
- **1만 개의 에이전트로 나비에-스토크스 문제를 풀고 Lean으로 형식화** (12:37~15:22) → [[agent-swarm]] · [[ai-formal-verification]]

### 인프라·지역사회 약정

전기 요금 미인상 · **데이터센터 전부 폐쇄 루프 물 순환** · *"[[openai-astra|Astra]]를 훈련시킨 [Abilene]이 쓰는 물은 사무실 건물 정도"* · **[Ohio]·[Georgia]** 지역사회 약정 · **모든 대학생에게 [[codex|Codex]] 크레딧** (34:49~35:26).

### 계보 — 2015년 11월과 2017년

- **2015년 11월 나파 오프사이트**에서 **3단계 계획**을 세웠고 *"그게 기본적으로 이후 10년간 따라간 것"*. 같은 자리에서 *"환경이 화면 픽셀, 키보드, 마우스인 강화 학습"* 을 이야기했다 (22:33~23:04) → [[openai-astra]]의 컴퓨터 사용 계보.
- **2017년**: *"현대 언어 모델의 첫 징후"* 논문([LSTM])과 **인간 선호로부터의 보상 학습**이 같은 해에 나왔다 (05:08~05:25) → [[rlhf]]
- **2019년 12월 초 GPT-3 훈련** 직후의 일화 (16:57~17:30) → [[greg-brockman]]

### ⚠️ 같은 주에 들어온 내부 비판

같은 날 ingest된 [[tech-bridge-rlhf-assistance-vs-automation|Almeida 편]]의 화자는 **GPT-4·ChatGPT·InstructGPT 공동 저자**이고 *"OpenAI에서 ChatGPT를 실제로 싫어하는 몇 안 되는 사람 중 한 명"* 이라고 자칭한다 — 그리고 *"ChatGPT 뒤의 알고리즘을 만들면서 내린 사소한 결정들이 이 분야의 현재 상황에 많은 영향을 미쳤다"* 고 말한다. → [[diogo-almeida]] · [[rlhf]]

**이 위키에서 같은 회사의 현직 사장과 전 연구자가 하루에 들어온 첫 사례**이고, 둘의 진단이 갈린다 — Brockman은 *"약속받았던 AI가 아니다"* 를 **제품 문제**로, Almeida는 같은 현상을 **학습 목적함수의 귀결**로 본다.

→ [[greg-brockman]] · [[tech-bridge-brockman-agi-era-defender-window]] · [[pacing-the-frontier]] · [[defenders-window]]

---
title: "Tech Bridge — Shopify CTO가 말하는 AI 비용, 아낄 곳과 쓸 곳 (Mikhail Parakhin 인터뷰 발췌): 천장을 높이는 AI · 복잡도로 정규화한 생산성 · 항상 가장 큰 모델 · 회사의 디지털 트윈 · 바벨 전략"
type: source
tags: [mikhail-parakhin, shopify, tokens, unlimited-tokens, largest-model, raise-the-ceiling, productivity-measurement, digital-twin, counterfactual, team-management, sycophancy, barbell-strategy, fine-tuning, auto-research, circuit-breakers, excerpt-format, video]
source-url: https://www.youtube.com/watch?v=wDTO-nR4yTM
source-type: video
author: Tech Bridge (발췌 편집, 내레이션 없음) · 화자 [[mikhail-parakhin|Mikhail Parakhin]](제목 · 설명란 · 태그 근거, 발화에 이름 없음) · 진행자 미상 · 원본 인터뷰 링크 없음
date-published: 2026-10-27
ingested: 2026-10-28
created: 2026-10-28
updated: 2026-10-28
---

# Tech Bridge — Shopify CTO가 말하는 AI 비용, 아낄 곳과 쓸 곳

[[tech-bridge|Tech Bridge]]가 올린 **8:24, 공식 챕터 8** 영상이다. 제목은 화자를 *"Shopify CTO"* 라 하고, 설명란은 *"Mikhail Parakhin이 설명하는 AI 활용 전략"* 이라고만 한다. 원본 인터뷰의 제목 · 날짜 · 링크 · 진행자는 없다. 10-27 [[tech-bridge-laurie-voss-product-engineer|Voss 편]]과 같은 형식이다. **한국어 내레이션 없이 원음만 이어 붙인 발췌 편집본**이고, 오디오도 영어 원본 하나다.

> 핵심 처방: *"always use this dichotomy barbell strategy for anything coding, for anything development, testing, auto research. Use the largest model. (…) For everything production, use fine-tuning, use the right model for that production"*(07:29~07:48)

> 천장: *"raising ceiling is is much more impactful. Cuz raising the floor yeah you you could have just been more diligent or throw more people at it."*(01:10~01:19)

이 위키의 토큰 비용 논의는 대부분 **절감 쪽**에서 출발했다([[token-minimization-trap]] · [[model-mixing-economics]] · [[overspending-underusing-loop]]). 이 편은 반대쪽 끝에 선다. **개발에서는 토큰을 제한하지 말고 가장 큰 모델을 쓰고, 절감은 운영에서 한다.** 기존 페이지에는 다음 내용이 붙는다.

- [[model-mixing-economics]]: 모델을 작업 단계가 아니라 **개발 / 운영**으로 가르는 바벨
- [[token-minimization-trap]]: 그 페이지가 "남은 공백"으로 둔 *최신 모델 제한도 같은 함정인가* 에 대한 당사자 답
- [[sycophancy]]: *"the answer is very often in the question"* — 아첨이 **빌드 속도**와 만날 때
- [[agent-roi-measurement]]: PR 수가 아니라 **프로젝트 복잡도로 정규화한** 생산성
- [[company-digital-twin]](신규): 회사를 **행동의 시퀀스**로 표현하고 반사실적 개입을 시험한다

**트랙과 인용.** 오디오는 `English (US) original` 하나이고(나머지는 더빙) **한국어 트랙이 없다.** 받은 ko는 `tlang=ko` 기계 번역이라 **인용은 전부 en-orig**로 한다. 무캡션 6구간은 챕터 경계와 겹쳐 제목 카드로 추정했다. 판독 상세는 raw에 있다.

## 1. 바닥이 아니라 천장 (00:16~01:25)

- *"It's not that LLM's take away the drudgery work (…) Is that you can do things that you previously couldn't take any amount of time, no amount of helpers."*(00:16~00:34) 최고의 수학자 천 명이 있어도 못 했을 일을 모델과 함께라면 할 수 있다고 한다(00:34~00:43).
- *"for the best problems right now I see is that I cannot solve it without the model but then model cannot solve it without me either."*(00:44~00:50) 체스 비유로 사람과 모델이 함께인 편이 각각보다 낫다고 한다(00:51~01:04, ASR *"center"* 는 centaur로 판독 — 추정).
- 진행자(이름 미상)가 *"you're raising the floor but (…) you can also raise the ceiling"* 이라고 정리하고, 화자가 천장 쪽이 *"a real unlock"* 이라고 받는다(01:04~01:24).

## 2. 복잡도로 정규화한 생산성 (01:37~02:11)

- PR 수 · PR 복잡도는 *"just like everybody else"* 로 추정하고, 거기에 더해 **프로젝트 복잡도**를 추정한다. 사내 시스템(ASR *"JSD system get stuff done"* — GSD로 판독, 추정)에서 *"normalized for complexity you can be very precise at measuring percentages of of productivity you're gaining."*(02:05~02:11) → [[agent-roi-measurement]]
- ⚠️ **퍼센트 자체는 말하지 않는다.** 측정 방법의 존재만 진술한다.

## 3. 항상 가장 큰 모델, 전원 무제한 토큰 (02:25~03:06)

- *"Always use the largest model. (…) because the largest model raises the ceiling the most."*(02:25~02:31)
- 근거는 둘이다. ① **반사실을 모른다**: *"you don't know unless you use the large model and then and compare the results, you don't know what you're missing, right? It's a unknown unknown."*(02:31~02:38) ② **증거가 나올 때까지 최대치**: *"always throw maximum uh thing at a problem and then until I see the evidence otherwise, that's what we're going to be doing."*(02:41~02:50)
- *"at Shopify we have unlimited tokens for everybody and that's why we run the heaviest models we can find."*(02:50~02:57) → [[token-minimization-trap]]

## 4. 회사의 디지털 트윈 (03:19~05:11)

- 텍스트가 글자의 시퀀스이듯 *"You can represent a company as a sequence of actions."*(03:33~03:36) 신용 한도 개설 · 제품 출시 · 카드 결제 수락 · 대출 같은 큰 변화부터 직원들의 매 순간 행동까지 시퀀스가 된다(03:36~03:57).
- *"you can create a digital twin of the company. And then you can start doing things to it instead of to real company"*(03:59~04:06). 광고 캠페인을 하면? 배송이 하루 빨라지면? 머천트에게 대출을 주면? 같은 **반사실적 개입**을 돌려 성장 확률을 최대화하는 상호작용 시퀀스를 찾는다(04:08~04:26).
- 그리고 *"we we actually do that in production"*(04:28~04:30) — 대출 제안, 배송 가속 권유, 광고 캠페인 시작. *"very direct impact on our bottom line"*(05:06~05:11). → [[company-digital-twin]]
- ⚠️ **당사자 진술이고 수치가 없다.** 모델의 구조 · 학습 데이터 · 검증 방법은 말하지 않는다.

## 5. 팀 관리 — 일정 지연을 먼저 알린다 (05:24~06:46)

- *"I thought that LLMs cannot really help me manage the team better. I could not have been more wrong."*(05:24~05:33) 모든 진행 상황을 분석해 *"It looks like this project's going to start slipping their deadline"* 이라고 **먼저** 알려 주는 작은 시스템을 만들었다(05:38~05:53).
- 기술 쪽이 더 중요해진다. 모델은 *"tries to please and so whatever you ask, the answer is very often in the question"*(06:09~06:16)이라, 머릿속에 처음 떠오른 것을 그대로 말하면 그대로 만들어 준다. 예전엔 논의라도 거쳤지만 *"now it's so much easier to just go and build it."*(06:32~06:36) → [[sycophancy]]
- 그래서 *"technical acumen becomes more important"* 이고, 사람은 *"engineers who are supervising LLMs rather than supervising engineers who are typing"* 을 감독하게 된다(06:36~06:46).

## 6. 바벨 전략 — 개발엔 최대, 운영엔 최적 (07:02~08:05)

- *"My main advice would be try to not limit tokens. You always need like circuit breakers because there always runaway processes that suddenly start burning tokens"*(07:02~07:14). 제한하지 않는 것과 **폭주 차단기**는 함께 간다.
- 큰 모델과 작은 모델의 차이는 *"huge world of difference"* 인데 반사실을 모르니 차이가 안 보인다(07:17~07:28).
- 바벨: 코딩 · 개발 · 테스트 · auto research에는 **가장 큰 모델**, *"Budget for it"*(07:29~07:43). 운영에는 파인튜닝한 맞춤 모델로 *"auto research the hell out of it so that you balance both cost throughput and and quality."*(07:44~07:55) *"save money on production by using cheaper models often fine-tuned. And invest money in development."*(07:55~08:05) → [[model-mixing-economics]] · [[automated-ai-research]]

## 이 위키와의 연결

### 이어지는 것

- **[[model-mixing-economics]]**: 위키의 모델 혼합은 대부분 **한 작업 안에서** 계획 모델과 실행 모델을 나누는 라우팅이었다. 이 편의 바벨은 축이 다르다. **조직의 활동을 개발(탐색)과 운영(서빙)으로 가르고**, 탐색 쪽은 비용을 아끼지 않는다. 10-18 [[tech-bridge-fireworks-train-to-deploy-open-models|Fireworks 편]]의 *고르는 것에서 고치는 것으로*(오픈 모델 맞춤 학습)는 이 바벨의 운영 쪽 끝과 같은 자리다.
- **[[token-minimization-trap]]**: 그 페이지는 *"최신 모델 제한"* 이 같은 함정인지 말하지 않는다고 적어 두었다. 이 편은 **개발에서는 그렇다**고 답한다(반사실을 모르므로 무엇을 잃는지도 모른다). 운영에서는 오히려 싼 모델을 권한다.
- **[[lauren-tan]]** ([[cursor|Cursor]]): Tan은 *"무제한 토큰이 있는 AI 랩"* 에서 일한다고 인정하면서 **고객은 그렇지 않다**며 ROI 트레이드오프로 넘어갔다. 이번은 AI 랩이 아닌 **플랫폼 기업 CTO가 전 직원 정책으로** 무제한을 말한다.
- **[[sycophancy]]**: 10-21 편은 사용자가 *약점을 물어* 아첨을 피하라고 했다. 이 편은 같은 성질이 **빌드 비용이 0에 가까워질 때** 더 위험하다고 본다. 질문에 답이 들어 있으면 논의 없이 그대로 만들어진다.

### 긴장

- *"Always use the largest model"* 은 [[model-mixing-economics]]의 여러 벤더 수치(오픈소스 10~30x 저렴, 임계값 위 최저가 라우팅)와 **개발 단계에서는** 정면으로 부딪친다. 화자는 근거로 측정이 아니라 *unknown unknown* 을 든다. 그리고 *"until I see the evidence otherwise"* 라며 스스로 반증 가능성을 열어 둔다.
- 무제한 토큰과 *"circuit breakers"* 를 함께 말하지만 차단 기준은 말하지 않는다.

## 해소하지 않고 표시만 한 것

- 원본 인터뷰의 제목 · 날짜 · 링크 · 진행자가 없다. 태그의 `Boris` · `Claude Code`가 진행자를 가리키는지 알 수 없어 귀속하지 않았다.
- *GSD* · *centaur* 는 ASR 판독 추정이다.
- 생산성 퍼센트 · 디지털 트윈의 매출 효과는 수치 없는 당사자 진술이다.
- 무캡션 6구간(제목 카드로 추정)의 내용은 모른다. 08:07~08:21 en-orig는 판독 불가라 인용하지 않았다.

## 등장 개체

- 인물: [[mikhail-parakhin]](신규) · 진행자(미상) · [[lauren-tan]](비교)
- 조직: [[shopify]](신규)
- 개념: [[company-digital-twin]](신규) · [[model-mixing-economics]] · [[token-minimization-trap]] · [[sycophancy]] · [[agent-roi-measurement]] · [[automated-ai-research]]

## References

- 원본 영상: <https://www.youtube.com/watch?v=wDTO-nR4yTM> (8:24, `upload_date` 2026-10-27 UTC = 2026-10-28 07:00 KST)
- raw: `01.raw/articles/2026-10-27_Shopify CTO가 말하는 AI 비용 아낄 곳과 쓸 곳.md`
- [[tech-bridge]] · [[mikhail-parakhin]] · [[shopify]] · [[tech-bridge-laurie-voss-product-engineer]]

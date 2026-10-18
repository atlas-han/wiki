---
title: "Tech Bridge — 지능을 빌리는 건 그만 (Jetashree Ravi · Fireworks AI): 오픈 모델은 production-ready이고 격차는 맞춤 학습으로 닫으며, 스택은 '한 번 서빙'에서 학습 → 배포 → 모니터링 → 재학습 루프로 간다"
type: source
tags: [open-models, closed-vs-open-models, fine-tuning, sft, rft, dpo, evaluator-function, hyperparameters, managed-training, training-api, training-agent, inference-engine, cuda-kernels, speculative-decoding, draft-model, disaggregation, quantization, data-flywheel, hot-loading, zero-downtime-deploy, numerical-fidelity, train-serve-parity, vendor-lock-in, cursor-composer, vendor-pitch, fireworks-ai, video]
source-url: https://www.youtube.com/watch?v=Eu4D795nMsQ
source-type: video
author: Tech Bridge (한영자막 재배포) · 발표 Jetashree Ravi([[fireworks-ai|Fireworks AI]] applied machine learning 팀 일부 리드 — **이름·소속은 자막에서 자기소개**(en-orig *"Jyotishree"*, 애칭 *"Jet"*), 철자와 성 Ravi는 설명란) · 행사명 미발화(설명란 ai.engineer 링크 → AI Engineer 계열 추정) · 녹화일 미발화
date-published: 2026-10-17
ingested: 2026-10-18
created: 2026-10-18
updated: 2026-10-18
---

# Tech Bridge — 지능을 빌리는 건 그만 (Jetashree Ravi · Fireworks AI)

[[tech-bridge|Tech Bridge]]가 재배포한 **18:48 단독 발표**다. 끝에 질문을 받겠다고 하지만 Q&A는 영상에 없다. 공식 챕터는 `meta.txt` 기준 17개다. 이 영상은 앞선 회차들에서 멤버십 전용이라 건너뛰었고([[tech-bridge]] 대기 목록, 목록 `upload_date` 20261013), 2026-10-18 회차에 `availability: public`, `upload_date` 20261017로 받았다. 화자 [[jetashree-ravi|Jetashree Ravi]]가 자기소개한다: *"I work at Firework. I lead part of the applied machine learning team. My name is Jyotishree, but feel free to call me Jet if that's easier."*(00:51~01:01) 발표는 **자사 플랫폼 소개**다. 추론 엔진, 학습 제품 세 가지, 학습·서빙 통합의 이점을 차례로 말하고 끝 4분은 데모다. 테제는 다음과 같다.

> **오픈소스 모델은 대부분 production-ready다. 폐쇄형에 못 미치는 곳에서는 맞춤 학습이 차별화 요인이다. 그래서 AI 스택은 모델을 한 번 서빙하고 끝내는 것에서, 같은 오픈 모델을 학습 → 배포 → 모니터링 → 피드백 → 체크포인트에서 재학습하는 연속 루프로 바뀐다. 이 루프를 매끄럽게 하려면 학습과 서빙이 같은 플랫폼에 있어야 한다(한 번 클릭 배포, 무중단 가중치 교체, 수치 일치).**

> *"the AI stack itself for most of our customers and users is shifting from let's just serve a model once once and that's done to a more continuous loop that is improving from training to inferencing the same open-source model itself."*(01:51~02:08) · *"when customers are switching from closed-source to open-source models, their biggest bottleneck or the gap is quality."*(06:58~07:05) · *"What hot loading essentially means is when you have a new checkpoint, uh you you can directly go to live deployment without any downtime itself."*(12:46~12:56) · *"numerics is not always compatible when you train on a different platform and host on a different platform."*(13:26~13:33)

이 위키에 처음 들어오는 것이 셋이다. ① **추론 제공자·학습 플랫폼 벤더**([[fireworks-ai]], 신규 제안). 지금까지 이 위키의 모델 이야기는 프런티어 랩과 하네스 쪽이었다. ② **오픈 모델을 자기 데이터로 계속 고치는 루프**([[open-model-customization-loop]], 신규 제안). SFT·RFT·DPO, 학습 제품의 세 층, hot loading, train-serve 수치 일치를 한곳에 묶는다. ③ **[[speculative-decoding]]**(신규 제안). 위키에 처음 나오는 추론 최적화 기법이고, 고객이 draft model을 직접 학습한다는 서술이 붙는다. 나머지는 기존 페이지에 붙는 증언이다.
- [[model-mixing-economics]]: 폐쇄형 모델의 비용 부담(손들기)과 오픈 모델로의 전환
- [[continual-learning]]: 배포 후 가중치를 계속 바꾸는 실무 형태. 다만 이 발표의 루프는 주기적 재학습이다
- [[production-trace-eval-flywheel]]: 같은 "flywheel"이지만 eval 태스크가 아니라 가중치로 돈다
- [[rlhf]]·[[post-training-northstars]]: RFT의 *"evaluator function"*, DPO
- [[inference-speed-as-capability]]: 자체 CUDA 커널, latency 목표, speculative decoding
- [[cursor]]·[[vercel]]·[[weights-and-biases]]·[[glm-5]]: 고객 사례와 연동, 예시 모델

ASR·ko 보정. ko는 **이름과 ML 용어를 낱말 뜻으로 옮긴다.** Fireworks는 "불꽃놀이", FireAttention은 "화재 주의"·"소방차"·"인재 유지"(06:09), DPO는 **"데이터 보호 책임자(DPO)"**(10:03), speculator는 **"투기꾼"**(11:56), weights는 **"페소"**(13:04), checkpoint는 "검문소"(12:51)다. hot loading의 정의 문장은 **"나는 휴식 시간 없이 산다"**(12:54)로 끝난다. 반전과 단위 오류도 있다.
- *at scale* → **"규모가 작아지면"**(02:21)
- *quality is a big bottleneck* → **"품질은 훌륭했습니다"**(04:17)
- *30 trillion tokens* → **"300억 개의 토큰"**(03:02, `en` *"30 billion"* 공유)
- 하루 *5 trillion tokens* → **"5조 달러"**(03:11)

en-orig는 GenSpark를 한 번 *"Genpact"*(10:15)로 적는다. 전체 목록은 raw에 있다.

> ⚠️ **당사자 발표이고 수치는 모두 자사 주장이다.** 기준선·지표·기간이 발화되지 않는다. *"30 trillion tokens"*(03:02~03:05)는 시간 단위가 없다(바로 뒤 *"5 trillion tokens a day"*로 보아 하루 단위로 읽힌다). Cursor *"13x faster inference"*(03:46~03:48)는 무엇보다 빠른지 말하지 않는다. Vercel *"40x latency improvement"*(04:04~04:06)는 기준선이 없다. GenSpark *"12% quality improvement"*(04:39)는 품질 지표가 없다. *"327 million CDC"*(04:51~04:53)는 통화 단위가 없고 *"CDC"*는 판독 보류다. 고객사 쪽 진술은 없다.
>
> ⚠️ **train-serve 통합의 근거는 한 문장이다.** *"a lot of the time customers use platform A for training and host on platform B. But what happens when you do that is you'll have issues in quality of the model"*(13:14~13:26)의 사례·수치·원인 분석은 없다. 같은 논리는 학습과 서빙을 한 벤더에 묶는 쪽을 편든다. 아래 "갈리는 것"을 볼 것.
>
> ⚠️ **제목은 업로더의 프레이밍이다.** *"지능을 빌리는 건 그만"*과 *"특화 AI"*는 발화되지 않는다. 화자의 틀은 폐쇄형 → 오픈 모델 전환과 맞춤 학습이다.
>
> ⚠️ **행사와 시점.** 행사명·도시·날짜는 발화되지 않는다. 설명란의 `https://ai.engineer`와 AI Engineer 링크로 **[[ai-engineer|AI Engineer]] 계열을 추정**할 뿐 확정하지 않는다. 시점 단서는 *"This number was actually pre-GLM 5.2 release."*(03:06~03:09)뿐이다.

## 1. 손들기와 세 가지 사실 (00:00~02:08)

- 손들기: *"How many of you actually today use a closed-source model like ChatGPT or Anthropic? Okay. How many of you feel like it's getting really expensive really quickly? Okay. That's that's a good percentage of you all."*(00:04~00:20) 응답 수는 발화되지 않는다.
- 전환의 이유: *"switching from closed-source model to open-source models for cost reasons, performance reasons"*(00:24~00:30). 발표의 범위는 *"where these open-source models shine and how to make the performance or quality of these open-source models match the closed-source models"*(00:39~00:49)다.
- ⭐ 세 가지 사실(*"three fundamental truths"* 01:20~01:22):
  1. *"open-source models for the most part are production-ready. If any of you have used GLM 5.2, you know that that is true especially for the coding use cases."*(01:23~01:33)
  2. *"if open-source models don't like beat or match the quality of closed-source models, the differentiating factor comes from how you customize, train, and improve these open-source models"*(01:35~01:48)
  3. *"the AI stack itself (…) is shifting from let's just serve a model once once and that's done to a more continuous loop that is improving from training to inferencing the same open-source model itself."*(01:51~02:08)

⚠️ 셋 모두 주장이고 근거는 GLM 5.2 사용 경험에 기댄 1번의 한 문장뿐이다. 2번은 **"오픈 모델이 폐쇄형을 이긴다"**가 아니라 **"못 미치는 곳에서는 맞춤 학습으로 닫는다"**다.

→ [[open-model-customization-loop]](신규) · [[model-mixing-economics]](비용) · [[glm-5]](*"GLM 5.2"* — 대조 안 함) · [[continual-learning]]

## 2. Fireworks의 자리와 규모 (02:11~05:00)

- *"that's where Fireworks kind of comes in. It makes the whole process of you having to go through the continuous journey of training these open-source models as well as hosting these open-source models at scale much more easier and also much more cost-effective as well."*(02:11~02:25)
- ⚠️ 규모(03:02~03:24): *"we serve about 30 trillion tokens and it's increasing. This number was actually pre-GLM 5.2 release. I'm sure this has pretty much kind of increased by about at least 5 trillion tokens a day now with the GLM 5.2 release. We support more than 10,000 companies globally and process about 200k requests a particular second itself."*
- ⚠️ 고객 사례:

| 고객 | 한 일 (발화) | 결과 (발화) |
|---|---|---|
| [[cursor\|Cursor]] | *"the Composer 2 model for Cursor was trained and also hosted on our platform today"*(03:39~03:43) | *"13x faster inference because of the fire attention engine"*(03:46~03:51). 비교 대상 미발화 |
| [[vercel\|Vercel]] | *"We helped them actually fine tune and also host the model on our platform"*(03:58~04:03) | *"a 40x latency improvement"*(04:04~04:06). 어느 모델·기준선인지 미발화 |
| GenSpark | 폐쇄형 → 오픈 전환에서 *"quality is a big bottleneck or was a big bottleneck for them"*(04:19~04:23). *"We did a RFT for them. We helped them clean the data set, define evaluator functions"*(04:29~04:34) | *"12% quality improvement"*(04:39~04:41). 지표 미발화 |

- 회사: *"we have raised around 327 million CDC a while ago and we are about 200 people working at Firework."*(04:48~04:56)

→ [[fireworks-ai]](신규) · [[cursor]](Composer 2를 외부 플랫폼에서 학습·호스팅했다는 **벤더 측 진술**) · [[vercel]]

## 3. 추론 — FireAttention, 자체 CUDA 커널, speculative decoding (05:00~06:51)

- *"At Firework, we have our own inference engine called fire attention. So you have a model, you have GPUs and the way the model sits on top of the GPUs is through a translation layer called CUDA kernels and as part of fire attention, we build our own CUDA kernel."*(05:11~05:27)
- ⭐ 워크로드별 최적화: *"customer like Vercel (…) tell us Uh they have X input tokens, Y output tokens, uh they have Z prompt prompt cache hit rate, and they want to meet so-and-so latency targets. And we help them optimize this whole inference stack including that CUDA kernel"*(05:41~05:59). 목표는 *"serve this model uh at a cheaper price, but also (…) meet their performance target and for their specific workload"*(06:01~06:08)다.
- 잘 알려진 기법: *"speculative decoding, disaggregation, quantization"*(06:19~06:22). 이름만 나온다.
- ⭐ draft model 학습: *"In terms of speculative decoding itself, we also allow customers to train their draft models on our platform. Uh so they can even upload the data set very similar to how they do for fine-tuning for training a draft model, uh which helps them uh make the model the main model perform much faster, uh meet latency requirements, also gives you better throughput if the draft model is trained uh very well."*(06:22~06:49)

⚠️ speculative decoding의 원리(draft가 토큰을 제안하고 main model이 검증)는 발화되지 않는다. 화자가 말하는 것은 **draft model도 학습 대상이 된다**는 것과 그 효과(속도·latency·throughput, 조건부)까지다. 배포 후 모니터링 지표에도 *"how your speculator is working"*(11:55~11:57)이 들어간다.

→ [[speculative-decoding]](신규) · [[inference-speed-as-capability]] · [[fireworks-ai]](FireAttention 섹션)

## 4. 학습 제품의 세 형태 (06:51~10:41)

전환 지점은 품질이다: *"people actually get to this stage mainly once they're happy with model quality. But when customers are switching from closed-source to open-source models, their biggest bottleneck or the gap is quality. And the way we we try to solve for it is through our training product."*(06:54~07:11)

| 형태 | 대상 (발화) | 하는 일 (발화) |
|---|---|---|
| **Training Agent** | *"product managers and builders that (…) got into this AI inferencing and training field very recently"*(07:22~07:30) | UI에서 업로드한 data set과 작업 설명을 주면 *"It will even let you choose the model. It will clean the data set for you. It will also help you do the hyperparameter fine-tuning"*(07:46~07:54) |
| **관리형 학습 (managed training)** | *"what most of our customers use today"*(08:13~08:16) | API 또는 UI. *"inputting the hyperparameters (…) choosing a model, uploading the data set itself, and then clicking a button"*(08:26~08:34). 관측: epoch별 학습·loss 대시보드, W&B API 키로 지표 내보내기(08:44~09:09) |
| **Training API** | *"very popular among some of the ML engineers"*(09:19~09:25) | *"let's ML engineers define their own training loop and loss functions"*(09:32~09:38). 관리형의 범위를 넘을 때 |

- 방법: *"these different flavors (…) offered for a supervised fine-tuning, reinforcement fine-tuning, and even DPO as well. Um nowadays, I think RFT has become extremely extremely popular."*(09:50~10:09)
- ⭐ RFT의 어려운 자리는 평가 함수다: *"if you ever need help in helping define a good evaluator function, then we have worked with customers like Genpact[=GenSpark] (…) to help them define an evaluator function, clean the data set, um and also choose the right hyper parameters especially for RFT."*(10:09~10:26)
- ⚠️ *"Unfortunately, the training agent itself does not support RFT, so it does not uh help you clean the data set or even do the hyper parameter tweaking, but we are more than happy to help you do it if you have a big use case in mind."*(10:28~10:41) 가장 인기 있다는 방법(RFT)이 가장 쉬운 진입로(Agent)에 없고, 그 공백을 **사람의 지원**이 메운다.

→ [[open-model-customization-loop]] · [[rlhf]](DPO는 선호 데이터 계열) · [[post-training-northstars]](RFT의 evaluator function ≈ 검증 가능한 보상) · [[verifiable-goals]] · [[weights-and-biases]](관리형 학습의 지표 내보내기) · [[ai-engineer-vs-ml-researcher]](세 형태가 사용자층으로 나뉜다)

## 5. 데이터 flywheel (10:54~12:13)

- *"most people prefer doing a continuous loop where they train, host, train, host as they get new and new data and feedback from their users."*(11:08~11:15)
- ⭐ 고리: 학습이 끝나면 *"You just are one click away from deploying these models into production. And once you've deployed, you can monitor. We have uh monitoring metrics for the number of tokens, cache hit rate, how your speculator is working if you've trained a speculator. Uh we help you collect gather feedback from all the all the metrics that you have collected. And if you choose to also retrain on the same platform from the end from the checkpoint that you were using to a new checkpoint itself."*(11:43~12:13)

⚠️ 고리에서 **"피드백"이 무엇인지**(사용자 평가, 로그, 라벨)와 그것이 어떻게 학습 데이터가 되는지는 발화되지 않는다. 나열된 모니터링 지표(토큰 수, cache hit rate, speculator)는 서빙 지표이고 품질 지표가 아니다.

→ [[open-model-customization-loop]] · [[production-trace-eval-flywheel]](같은 말 "flywheel", 도는 것이 다르다) · [[continual-learning]]

## 6. 루프를 가능하게 하는 것 — GPU, hot loading, 수치 일치 (12:13~13:58)

- GPU: *"definitely having a host of GPUs. We do have We do partner with different cloud and neo cloud providers"*(12:17~12:27)
- ⭐ hot loading: *"this has become really popular especially when we were training models for cursor. And this was actually a feature we implemented specifically for cursor, and then we thought would be useful for general public"*(12:34~12:46). *"when you have a new checkpoint, uh you you can directly go to live deployment without any downtime itself. So, if you have a deployment and you've gone through this continuous loop and trained a new checkpoint, then you can just click a button and swap out the weights"*(12:48~13:06)
- ⭐ numerical fidelity: *"a lot of the time customers use platform A for training and host on platform B. But what happens when you do that is you'll have issues in quality of the model. And the reason you have those issues is numerics is not always compatible when you train on a different platform and host on a different platform. So, that's why we offer training and inferencing on the same platform and ensure that you won't find any numerical differences"*(13:14~13:42)
- *"because training and inferences on the same platform, you're just one click away from deploying this model at production scale."*(13:48~13:58)

⚠️ 수치 불일치의 원인(정밀도·커널·양자화 차이 등)은 발화되지 않는다. *"ensure that you won't find any numerical differences"*는 보증 문구이고 검증 방법은 나오지 않는다.

→ [[open-model-customization-loop]](hot loading · train-serve 수치 일치 섹션) · [[compute-constrained-growth]](*"neo cloud"* — 이 위키에서는 Altman이 우려의 대상으로 언급했다) · [[cursor]]

## 7. 데모 — Training Agent, 관리형 학습 (14:02~18:30)

화면은 확인하지 않았다. 발화만 옮긴다.

- **Training Agent**(14:08~16:05): 학습 data set과 eval data set을 지정하고 fine-tune과 hyperparameter·모델 선택을 맡긴다. 에이전트가 **SFT 계획**을 내고 *"tells you why it selected the base model in this case it selected Qwen-3-8B"*(14:52~14:58). 사람이 승인하면 단계마다 진행을 알리고, 끝에 config·base model·hyperparameter 요약과 *"metrics such as accuracy and F1 score"*(15:50~15:53), *"recommended next step"*(16:02~16:05)을 준다.
- **관리형 학습**(16:07~18:07): data set·모델 선택 → evaluator 설정에서 eval data set → 선택적 hyperparameter → *"create"*. 완료된 job에서 data set·hyperparameter·loss를 보고, *"clone these training runs and reproduce it with different settings"*(17:25~17:31). 배포는 custom model을 골라 *"deploy"*하거나 *"throughput, fast, minimal"*(17:52~17:56) 템플릿을 쓴다.
- **Training API**: *"I unfortunately don't have an entire demo for our training API because the setup itself differs from customer to customer"*(18:10~18:19). 웹사이트의 cookbook을 가리킨다.

⚠️ 데모의 Training Agent 결과(accuracy·F1 값)는 발화되지 않는다. 계획을 보고 *"approve"*(15:10~15:16)하는 단계는 사람에게 남는다.

→ [[fireworks-ai]] · [[open-model-customization-loop]]

## 이 위키와의 연결

### 이어지는 것

- **[[model-mixing-economics]]: 비용 압력이 모델 교체로 간다.** 이 페이지의 기존 서술은 한 작업 안에서 단계마다 모델을 고르는 것이고, "Anthropic 모델은 비싸서 피한다"는 화자도 있었다. Ravi의 손들기(00:11~00:20)는 같은 압력이 **폐쇄형 → 오픈 모델 전환**으로 이어진다고 본다. 다만 그다음 단계는 고르는 것이 아니라 **학습해서 고치는 것**이다.
- **[[continual-learning]]: 실무 쪽의 근사.** Ghahramani는 지금 방식을 *"거대한 모델을 학습시킨 다음 (…) 몇 달 후에 또 다른 거대한 모델을 학습"*이라고 했다. Ravi의 *"train, host, train, host"*(11:10~11:13)와 hot loading은 그 주기를 줄이는 운영 쪽 답이다. 그래도 연속 갱신이 아니라 **체크포인트 단위의 재학습**이고, catastrophic forgetting 같은 문제는 다루지 않는다.
- **[[production-trace-eval-flywheel]]: 같은 이름, 다른 축.** 기존 flywheel은 프로덕션 트레이스를 **eval 태스크**로 바꿔 하네스·프롬프트를 고친다. Fireworks의 flywheel은 피드백을 **가중치**로 되돌린다. 두 루프는 겹칠 수 있다(RFT의 evaluator function이 eval과 같은 것을 재는 경우). 발표는 이 연결을 말하지 않는다.
- **[[post-training-northstars]]·[[rlhf]]: 랩 밖의 post-training.** 이 위키의 post-training 서술은 프런티어 랩의 목적 함수였다. 여기서는 SFT·RFT·DPO가 **고객이 버튼으로 고르는 제품 옵션**이 된다. 어려운 자리는 그대로다. RFT에서 Fireworks가 직접 돕는 것이 *"define a good evaluator function"*(10:12~10:14)이다.
- **[[inference-speed-as-capability]]: 속도를 사는 다른 길.** Altman은 속도를 모델 공급자의 새 축으로 말했다. Ravi는 **워크로드별 커널 최적화와 draft model 학습**으로 고객 쪽에서 latency 목표를 맞춘다고 한다.
- **[[cursor]]: Composer의 학습·서빙 자리.** 이 위키는 Composer를 Cursor 자체 모델(2.5)로 적었다. 이 발표는 **Composer 2가 Fireworks에서 학습·호스팅됐고 hot loading이 Cursor용으로 만들어졌다**고 말한다(03:39~03:43, 12:34~12:44). ⚠️ 벤더 측 진술이고 Cursor 쪽 확인은 없다.

### 갈리는 것

> ⚠️ **긴장: 학습과 서빙을 한 플랫폼에 묶을 것인가.** Ravi의 numerical fidelity 논리(13:14~13:42)와 한 번 클릭 배포(13:48~13:58)는 **학습과 추론을 같은 벤더에 두라**는 쪽이다. [[tech-bridge-tailscale-aperture-ai-without-lock-in|Tailscale 편]]의 Guercio는 각 층에서 고를 수 있어야 한다며 벤더 통합을 오답으로 놓았다. [[tech-bridge-openhands-sandboxing-coding-agents|OpenHands 편]]의 Brennan은 GitHub Actions를 *"proprietary standard"*라고 비판했다. 오픈 모델로 옮기는 동기 중 하나가 폐쇄형 공급자에서 벗어나는 것인데, 이 발표의 처방은 **학습·서빙 층에서 다시 한 벤더를 고르는 것**이다. 수치 불일치 주장 자체는 검증되지 않았다.

> **"오픈 모델은 production-ready"의 강도.** 1번 사실(01:23~01:33)은 GLM 5.2 경험을 근거로 단정한다. 2번 사실과 07:03~07:05는 **품질이 전환의 가장 큰 병목**이라고 한다. 둘은 모순이 아니다(대부분 쓸 만하지만 특정 작업에서는 격차가 있다). 다만 발표는 어느 작업에서 격차가 얼마인지 말하지 않는다. 이 위키의 [[model-mixing-economics]] 사례들은 오픈 모델을 주로 **싼 실행 모델**로 쓴다.

> **Training Agent의 공백.** 화자 스스로 *"RFT has become extremely extremely popular"*(10:07~10:09)라고 하면서, 입문자용 Training Agent는 RFT를 지원하지 않는다고 한다(10:28~10:30). 데모의 Agent는 SFT를 골랐다. "누구나 버튼으로"와 "가장 인기 있는 방법은 사람의 도움이 필요하다" 사이의 거리가 발표 안에 있다.

## 해소하지 않고 표시만 한 것

- 모든 고객 수치(13x·40x·12%)의 기준선·지표·측정 조건. 고객사 쪽 진술.
- *"30 trillion tokens"*의 기간 단위. *"327 million CDC"*의 뜻과 통화.
- *"GenSpark Lava builds"*(04:11)의 구조. *"Genpact"*(10:15)가 ASR인지 말실수인지.
- train-serve 수치 불일치의 원인과 크기. *"won't find any numerical differences"*의 검증 방법.
- 피드백이 학습 데이터가 되는 경로. 재학습의 주기·비용.
- speculative decoding 외 기법(disaggregation·quantization)의 내용. 이름만 나온다.
- *"swap out the weights (…) with the new endpoints"*(13:04~13:08)의 *endpoints*.
- 행사명·도시·녹화일. 슬라이드와 데모 화면.

## 등장 개체

- 인물: [[jetashree-ravi|Jetashree Ravi]](신규 제안 — 이름은 자막에서 자기소개(en-orig *"Jyotishree"*), 철자와 성은 설명란)
- 조직: [[fireworks-ai|Fireworks AI]](신규 제안 — FireAttention·학습 제품 셋은 이 페이지에 섹션으로) · [[cursor|Cursor]](Composer 2, hot loading) · [[vercel|Vercel]](fine-tune + 호스팅, 40x) · [[weights-and-biases|Weights & Biases]](지표 내보내기) · [[anthropic|Anthropic]](손들기 질문의 폐쇄형 예) · [[ai-engineer|AI Engineer]](⚠️ 설명란 링크만, 추정) · GenSpark — 페이지 없음(사례 하나)
- 모델·제품: [[glm-5|GLM]](*"GLM 5.2"*, 대조 안 함) · Composer 2 · Qwen3 8B(*"Qwen-3-8B"*, 데모의 base model — [[qwen3-5]]와 다른 모델) · ChatGPT · CUDA — 페이지 없는 것은 언급만
- 개념: [[open-model-customization-loop]](신규 제안) · [[speculative-decoding]](신규 제안) · [[model-mixing-economics]] · [[continual-learning]] · [[production-trace-eval-flywheel]] · [[rlhf]] · [[post-training-northstars]] · [[verifiable-goals]] · [[inference-speed-as-capability]] · [[compute-constrained-growth]] · [[ai-engineer-vs-ml-researcher]]

## References

- 원본 영상: <https://www.youtube.com/watch?v=Eu4D795nMsQ> (18:48, `upload_date` 2026-10-17, 멤버 전용 → 공개)
- raw: `01.raw/articles/2026-10-17_지능을 빌리는 건 그만 - 특화 AI의 학습부터 배포까지.md`
- 설명란 링크: <https://fireworks.ai> · <https://docs.fireworks.ai/fine-tuning/managed-finetuning-intro> · <https://docs.fireworks.ai/fine-tuning/supervised-fine-tuning> · <https://www.linkedin.com/in/jetashree-ravi/> · <https://github.com/jraviS2023> · <https://ai.engineer> (⚠️ 열어 보지 않았다)
- lock-in의 다른 서술: [[tech-bridge-tailscale-aperture-ai-without-lock-in]] · [[tech-bridge-openhands-sandboxing-coding-agents]]
- [[tech-bridge]] · [[fireworks-ai]] · [[jetashree-ravi]]

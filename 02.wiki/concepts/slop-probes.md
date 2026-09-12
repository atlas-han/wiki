---
title: 슬롭 프로브 (Slop Probes)
type: concept
category: technique
tags: [evaluation, classifier, ai-slop, design, llm-as-judge, gate]
aliases: [probes, baby classifiers, 프로브, 소형 분류기]
related: [ai-slop, generator-evaluator-pattern, transcript-classifier, signal-layer, verifiable-goals, multimodal-elicitation, structured-brand-context]
first-seen: tech-bridge-taste-labs-measuring-slop
sources: [tech-bridge-taste-labs-measuring-slop]
created: 2026-09-12
updated: 2026-09-12
---

# 슬롭 프로브

**주관적 산출물(웹사이트 디자인)에서 객관화할 수 있는 특징을 마이닝하고, 특징 하나를 발견하는 소형 분류기("baby classifier")를 훈련한 뒤, 여러 분류기가 동시에 켜지는 빈도로 [[ai-slop|슬롭]]을 예측하는 방법.** [[taste-labs|Taste Labs]]의 [[thais-castello-branco]]가 [[tech-bridge-taste-labs-measuring-slop]]에서 소개했다.

## 절차

> 저희는 이걸 **프로브(probes)** 라고 부르는데, 기본적으로 두 가지를 했습니다. (07:23~07:25)

| 단계 | 내용 |
|---|---|
| 1. 패턴 마이닝 | 10년치 웹사이트 200만 개 + 합성 AI 사이트에서 **추출할 수 있는 특징** — *"더 객관적으로 만들 수 있는 특성: 색상, 타이포그래피, 레이아웃, 대상(audience)"* — 을 **구조화**한다 |
| 2. 프로브 훈련 | *"작은 분류기(baby classifiers)라고 생각하세요 — **이 하나의 특성을 발견하는 능력**을 어떻게 훈련할까"* (07:44~07:50) |
| 3. 결합 | 슬롭 사이트에서 *"어떤 프로브들이 '이 사이트는 AI 슬롭일 가능성이 매우 높다'를 뜻하는지"* 식별 — **여러 개가 동시에 나타나는 빈도** |

핵심은 *하나의 큰 판정기* 가 아니라 **작은 단일 특징 판정기의 앙상블**이라는 것이다. 슬롭은 정의상 **반복**이므로 특징의 동시 출현 빈도가 신호가 된다.

## 주장 — LLM-as-a-judge보다 낫다

> 이것은 **LLM에게 "훌륭한 인간 품질인가, AI가 생성한 슬롭인가" 판단하게 하는 대부분의 LLM-as-a-judge 방식보다 더 잘 수행됐습니다.** (08:13~08:22)

> ⚠️ **수치·설정 없음.** 정확도, 비교한 LLM·프롬프트, 표본, 프로브 개수 전부 소스에 없다. *"예측 능력이 아주 높았다"* 는 자기 진술. 당사자(평가·데이터 판매자).

## 용도 — 측정에서 게이트로

> 작은 분류기가 좋은 예였죠 — 그것을 **슬롭의 게이트**로 써서 **에이전트가 슬롭을 출시(ship)하지 못하게** 할 수 있습니다. (11:41~11:48)

즉 프로브는 연구 도구이자 **에이전트 파이프라인의 검증 단계**다. [[structured-brand-context|Brand API]]가 *"에이전트가 실제로 궤도에 있는가"* 를 판단하는 자리에도 같은 장치가 들어갈 수 있으나 소스는 명시하지 않는다.

## 이 위키에서의 자리

- **[[generator-evaluator-pattern]]의 평가자가 LLM이 아닌 첫 사례.** 이 위키의 평가자는 전부 LLM이었다 — Anthropic의 회의적 evaluator, [[managed-agents]]의 `outcomes`, [[google-deepmind|DeepMind]]의 auto-rater 12종. 프로브는 **LLM 밖의 소형 분류기**로 같은 자리를 채우고, 그것이 LLM 판정보다 낫다고 주장한다. 두 접근의 차이: LLM evaluator는 *기준을 프롬프트에 쓰고*, 프로브는 *기준을 데이터에서 마이닝* 한다 → 슬롭이 [[ai-slop|움직이는 표적]]이라면 후자가 유리하나, **갱신 주기는 소스에 없다.**
- **[[transcript-classifier]]와의 대비.** 그쪽도 *실행 전 게이트* 이지만 **LLM 기반**이고 대상이 *행동의 위험* 이다. 프로브는 **산출물의 품질**을 게이트한다 — [[agentic-misbehavior]]가 아니라 [[ai-slop]]을 막는다.
- **[[signal-layer]]의 채점기 경계선이 또 한 번 안쪽으로.** Hall은 *자동 채점기가 없는 영역* 이 남는다고 했고, [[multimodal-elicitation]]은 *발견 과정의 효율* 을 채점해 그 선을 밀었다. 프로브는 **산출물의 미학적 특징 자체**를 채점한다 — 단, 방법은 *"디자인을 거의 결정론적인 조각(팔레트·대비·정렬)으로 분해"* 하는 것이라, 경계선은 여전히 *분해되지 않는 것*(전문가가 갈리는 미학)에 남는다. 화자 자신이 그 부분은 *"데이터에 더 가까운 것에 기대야"* 한다고 인정한다.
- **[[verifiable-goals]]** — *"고치려면 먼저 측정해야 한다"* 를 주관 영역에 적용한 것. verifier를 만들 수 없다고 여겨진 자리에 verifier를 만든 시도.

## ⚠️ 미해결

- 프로브가 재는 것은 *AI 슬롭일 가능성* 이지 *훌륭함* 이 아니다 — 화자도 *"훌륭함은 정의하기 어렵다"* 고 인정. 게이트는 **나쁜 것을 막을 뿐 좋은 것을 만들지 않는다.**
- 합성 AI 사이트를 어떤 모델로 생성했는지 없음 → 프로브가 *특정 모델의 습관* 을 배웠을 가능성을 배제할 수 없다.
- 사람이 만든 슬롭(AI 이전의 동질화)과 AI 슬롭을 프로브가 구분하는지 없음.

## References

- [[tech-bridge-taste-labs-measuring-slop]] (first-seen) · [[taste-labs]] · [[thais-castello-branco]]
- 관련: [[ai-slop]] · [[generator-evaluator-pattern]] · [[transcript-classifier]] · [[signal-layer]]

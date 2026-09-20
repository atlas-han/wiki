---
title: AGI 정의 논쟁 (AGI vs Superintelligence)
type: concept
category: theory
tags: [agi, superintelligence, definition, milestone, openai, nvidia, andrew-ng]
related: [ai-jobs-impact, intelligence-as-infrastructure, compute-constrained-growth, agent-harness-design, sutton-bitter-lesson, regulatory-capture, one-continuous-exponential]
first-seen: tech-bridge-altman-agi-superintelligence
sources: [tech-bridge-altman-agi-superintelligence, tech-bridge-jensen-huang-g20-agi, tech-bridge-andrew-ng-ai-opportunity, tech-bridge-altman-g20-economic-boom, tech-bridge-brockman-agi-era-defender-window]
created: 2026-09-06
updated: 2026-09-20
---

# AGI 정의 논쟁 (AGI vs Superintelligence)

**"AGI"가 무엇을 뜻하고, 도달했다는 선언이 무엇을 바꾸는가**에 대한 이 위키의 세 입장. 2026-09-06 ingest에서 [[sam-altman|Sam Altman]]과 [[jensen-huang|Jensen Huang]]의 진술이 하루에 들어오면서, 이미 있던 [[andrew-ng|Andrew Ng]]의 입장과 함께 한 페이지가 됐다.

## 세 입장

| 화자 | 정의에 대한 태도 | 도달 여부 | 선언의 의미 |
|---|---|---|---|
| [[andrew-ng]] ([[tech-bridge-andrew-ng-ai-opportunity]]) | *"임의 지적 과제"* 로 정의하면 **decades** | 아직 | 조기 선언은 **정의 낮추기**·계약 인센티브 문제 |
| [[sam-altman]] ([[tech-bridge-altman-agi-superintelligence]]) | *"아주 모호하게 정의된 (…) 별 의미 없는 마케팅 용어"* | *"어느 정도는요. 적어도 비슷하긴 해요"* | *"저는 그게 중요하다고 생각하지 않아요. 없습니다"* |
| [[jensen-huang]] ([[tech-bridge-jensen-huang-g20-agi]]) | 정의를 주지 않음 | *"우리가 이미 거의 그 단계에 도달했다"* | *"굉장히 중요한 의미를 지니거나, 아니면 아무 의미도 없거나"* → 사고 실험으로 답함 |

세 사람이 **같은 단어의 무의미함**에는 동의하면서 서로 다른 이유로 그렇게 말한다는 점이 흥미롭다. Ng는 *정의를 낮추는 유인*을, Altman은 *용어의 다의성*을, Huang은 *도달 이후에도 남는 일*을 근거로 든다.

## Altman — 이정표에서 경사로로

> **AGI는 하나의 이정표처럼 느껴졌는데, 초지능은 무한히 확장될 수 있는 무언가처럼 느껴집니다.**

> 이 모든 것에서 중요한 것은 어떤 이정표나 특정 용어가 아니라, 우리가 **역량과 잠재력이 기하급수적으로 증가하는 추세**에 있다는 점.

내부 어휘가 이미 바뀌었다고 한다 — *"구내식당에서 우리가 AGI에 도달했는지 아닌지 (…) 논쟁을 아주 오랫동안 들어본 적이 없습니다."* 대신 *"초지능의 지속적인 경사로(continuous ramp)"*. 진행자는 이를 *"골대를 옮겼다"* 는 대중 반응으로 받는다.

체감의 단위도 제시된다 — *"2020년으로 돌아가서 (…) **20분 안에 성공을 거두고**, 새로운 과학을 발견하고, 회사 창업을 돕고, 복잡한 코드를 작성할 수 있는 시스템이 있다면, 그걸 AGI라고 부르시겠어요? **아마 그랬을 거예요.**"* 즉 정의는 **회고적으로만** 만족된다는 관찰.

> ⚠️ 진행자가 인용한 정의(*"경제적으로 가장 가치 있는 대부분의 작업에서 인간보다 뛰어난 성능을 발휘하는 고도로 자율적인 시스템"*)는 자막상 *"Y Combinator's charter"* 이지만, 문구는 OpenAI Charter의 AGI 정의와 일치한다. ASR 오류 가능성은 위키의 추정이다.

## Huang — 도달해도 하네스는 남는다

Huang의 답은 정의가 아니라 **온보딩 사고 실험**이다.

> 이러한 아이들이 우리 회사에 들어오게 될 때, 우리는 **여전히 그들에게 적절한 맥락을 제공하는 데 상당한 투자**를 해야 합니다. 결론적으로, **AGI가 등장하더라도 모든 기업의 문제가 해결되는 것은 아니라는 점**입니다. (…) 그 모든 하네싱, 그 모든 환경 조성이 바로 **기업이 하는 일이고, 리더가 하는 일**입니다.

즉 "AGI"라는 임계값이 무엇이든, 그 너머에도 [[agent-harness-design]]·[[context-engineering]]·[[agent-org-adoption]]이 다루는 일이 그대로 남는다. 이 위키가 하네스를 *모델 결함의 보완*([[harness-pruning]])으로 봐 온 것과 대비된다 — Huang의 하네스는 **결함 보완이 아니라 맥락 부여**이고, 그래서 모델이 아무리 좋아져도 사라지지 않는다.

## 왜 이 논쟁이 이 위키에 중요한가

세 입장의 차이는 각자가 무엇을 파는가와 정렬돼 있다 — Ng는 교육·규제 비판([[regulatory-capture]]), Altman은 지능 서비스와 컴퓨트([[compute-constrained-growth]]), Huang은 인프라([[intelligence-as-infrastructure]]). **정의를 낮추거나 무의미화하는 것이 누구에게 유리한가**를 함께 읽어야 한다. Ng가 바로 그 점을 경고했다.

그리고 실무적 함의는 셋 다 같다 — [[ai-jobs-impact]]에서 보듯, "AGI 도달"이 곧 "일이 사라진다"로 번역되지 않는다고 세 사람 모두 말한다.

## ⚠️ 유보

- 셋 다 **소스가 인터뷰·연설**이고 측정 가능한 정의를 제시하지 않는다.
- Altman의 *"최신 내부 모델"* 에 대한 서술은 검증 불가.
- 이 페이지는 위키가 세 입장을 **나란히 둔 것**이지, 어느 하나를 채택한 것이 아니다.

## 도착점 없는 곡선 (2026-09-07 · [[tech-bridge-altman-g20-economic-boom]])

이 페이지의 정의들은 모두 **도착점을 어떻게 규정할 것인가**를 다뤘다. G20에서 [[sam-altman]]이 제시한 역사관은 **도착이라는 사건 형식 자체와 어긋난다** — 농업·산업·컴퓨터 혁명을 *"하나의 혁명, 하나의 기하급수적인 기술 발전"* 으로 보고, *"이것이 마지막 혁명이다"* 라는 서술을 명시적으로 거부한다. 연속 지수에는 문턱이 없다. → [[one-continuous-exponential]]

같은 회의에서 [[jensen-huang]]이 *"사실상 이미 도달했다"* 고 한 것과 대비된다 — 한쪽은 문턱을 이미 지났다 하고, 다른 쪽은 문턱이라는 개념을 쓰지 않는다.

> ⚠️ **이 소스에서 Altman은 AGI라는 단어를 쓰지 않는다.** 위 대조는 프레임 수준이며, 그가 3부작([[tech-bridge-altman-agi-superintelligence]])의 AGI/초지능 구분을 철회했다는 뜻이 **아니다.** 두 소스를 합쳐 하나의 입장으로 만들지 않는다.

## References

- [[tech-bridge-altman-agi-superintelligence]] — first-seen
- [[tech-bridge-jensen-huang-g20-agi]] · [[tech-bridge-andrew-ng-ai-opportunity]]
- 관련: [[ai-jobs-impact]] · [[intelligence-as-infrastructure]] · [[compute-constrained-growth]] · [[agent-harness-design]]

## 네 번째 입장 — 선언하되 모델을 가리키지 않는다 (2026-09-20 · [[tech-bridge-brockman-agi-era-defender-window]])

위 표의 세 입장은 전부 **"AGI"라는 단어의 무의미함**으로 수렴했다. [[greg-brockman|Greg Brockman]]은 **그 무의미함에 동의하면서 선언을 한다** — 그리고 선언이 가리키는 것이 **모델의 속성이 아니다.**

| 화자 | 정의에 대한 태도 | 도달 여부 | 선언의 의미 |
|---|---|---|---|
| [[greg-brockman]] ([[tech-bridge-brockman-agi-era-defender-window]]) | *"시점(point in time)이라기보다 흐릿한 스펙트럼(fuzzy spectrum)으로 드러났다"* | *"[[openai-astra\|Astra]]를 AGI라고 불러도 꽤 합리적"* | **어느 모델인지는 상관없다** — 선언이 바꾸는 것은 **회사가 따라야 할 공정** |

> **그것이 이 모델인지, 이전 모델인지, 다음 모델인지는 논쟁할 수 있습니다. 상관없습니다. 요점은 우리가 새로운 국면에 있다는 것이고, 거기서는 안전·보안·정렬을 배포 시점만이 아니라 개발 시점과 평가까지 거슬러 올라가 정말로 생각해야 한다는 것입니다.** (47:48~48:02)

**이것이 이 표의 다른 세 칸과 종류가 다르다.** Ng·Altman·Huang은 전부 *정의가 무엇을 뜻하는가* 를 다뤘고, 그래서 세 사람 모두 **선언을 하지 않거나 무의미하다고 했다.** Brockman은 **정의를 포기하면서 선언을 유지하고, 선언의 지시 대상을 모델에서 공정으로 옮긴다.** → [[pacing-the-frontier]]

**[[sam-altman]]과 같은 회사에서 나온 진술인데 용도가 다르다는 점이 중요하다.** Altman의 *"별 의미 없는 마케팅 용어"* 는 **기대를 낮추는** 쪽이었고, Brockman의 *"우리는 AGI 시대에 있다"* 는 **내부 기준을 올리는** 쪽이다. 두 진술은 모순이 아니라 **같은 용어의 두 용도**다.

### 근거 쪽 — 왜 시점이 없는가

> 이제, 그것은 여전히 **들쭉날쭉합니다.** … **우리가 정말 있어야 할 곳은 전 범위에 걸쳐 훨씬 더 고른 상태**입니다. (38:47~39:16)

→ **[[jagged-capability-frontier]]** — **"들쭉날쭉하다"는 것이 곧 "단일한 문턱이 성립하지 않는다"** 는 것이다. 이 표의 위 세 입장이 *정의를 어떻게 잡을 것인가* 로 다퉜다면, 여기서는 **경계의 모양 자체**가 논거가 된다.

그리고 체감의 단위가 하나 제시된다 — **24시간 일관 실행**(*"24시간 동안 일관성 있게 돌면서 … 아주 다양한 도메인에 걸쳐"*, 38:42~38:47). ⚠️ **측정 조건은 없다.**

### [[jensen-huang|Huang]]과의 관계

Huang의 *"AGI가 등장하더라도 모든 기업의 문제가 해결되는 것은 아니다"* 와 **같은 구조인데 남는 일의 종류가 다르다** — Huang은 **맥락 부여**(하네싱)가 남는다고 했고, Brockman은 **안전·보안·정렬의 운영**이 남는다고 한다. **둘 다 임계값 이후를 말하지만, 한쪽은 기업의 일이고 다른 쪽은 랩의 일이다.**

> ⚠️ **당사자 진술이고 강제력이 없다.** *"기준"* 이 무엇인지, 누가 판정하는지, 못 맞추면 무엇이 멈추는지 소스에 없다. 그리고 **정부·외부 검증이 대담 전체에서 한 번도 언급되지 않는다** — [[dario-amodei]]의 3단계 계획과 갈리는 지점이다.

→ [[greg-brockman]] · [[pacing-the-frontier]] · [[jagged-capability-frontier]] · [[openai-astra]]

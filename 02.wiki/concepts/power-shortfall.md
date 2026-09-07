---
title: Power Shortfall (전력이 컴퓨팅의 상한이다)
type: concept
category: theory
tags: [power-grid, electricity, data-center, compute, gpu, export-controls, infrastructure]
related: [compute-constrained-growth, intelligence-as-infrastructure, humanoid-robot-scaling, trusted-throughput]
first-seen: tech-bridge-elon-musk-g20-ai-future
sources: [tech-bridge-elon-musk-g20-ai-future, tech-bridge-jensen-huang-g20-agi, tech-bridge-altman-g20-economic-boom]
created: 2026-09-07
updated: 2026-09-07
---

# Power Shortfall (전력이 컴퓨팅의 상한이다)

**AI 칩 생산 속도가 전력 공급 증가 속도를 앞지르면서, 컴퓨팅의 실질 제약이 자본도 칩도 아닌 전기가 된다는 진단.** [[elon-musk|Elon Musk]]가 G20에서 수치와 함께 제시했다 → [[tech-bridge-elon-musk-g20-ai-future]].

## 산수

> 사실, **심각한 전력 위기가 존재합니다.** (…) **2027년에는 AI 칩에 필요한 전력이 최소 15기가와트(GW) 부족**할 것으로 예상됩니다.

| 항목 | 연 증가율 |
|---|---|
| **AI 칩 생산** | **40~50%** |
| **중국 외 가용 전력** | **10~20%** |

> 당연히 **더 빨리 상승하는 것이 결국 더 느리게 상승하는 것을 압도**하게 될 것입니다.

두 지수의 격차가 결손을 만든다는 것이 논증 전부다. 시점은 *"먼 미래는 아니라는 거죠"* — 부족은 *"내년"*, 15 GW 수치는 2027년.

## 중국이 분모에서 빠지는 이유

> 중국은 **엄청난 양의 전력을 보유**하고 있죠. 하지만 **GPU 수출 금지 때문에 중국에서는 최신 칩을 사용하는 데이터 센터를 구축할 수 없습니다.** 그래서 정말로 고려해야 할 점은 **중국 이외 지역에서 전력 생산량이 어떻게 증가하고 있느냐**는 것입니다.

수출 통제가 **전력과 칩을 서로 다른 지리에 가둔다**는 관찰이다 — 전력이 남는 곳에 칩이 없고, 칩이 있는 곳에 전력이 모자란다. 이 위키에서 수출 통제가 **정치 사안이 아니라 수급 계산의 항**으로 나온 첫 사례다.

## 세 화자가 같은 병목을 세 층에서 가리킨다

같은 G20 회의의 세 세션이 같은 제약을 서로 다른 단위로 말한다.

| 화자 | 단위 | 진술 |
|---|---|---|
| [[jensen-huang]] ([[intelligence-as-infrastructure]]) | **비용** | *"1 GW ≈ 500~600억 달러, 2020년대 말까지 100 GW"* |
| [[elon-musk]] (이 페이지) | **결손** | *"2027년 최소 15 GW 부족"* |
| [[sam-altman]] ([[compute-constrained-growth]]) | **수요** | *"효율성 향상을 찾을 때마다 수요가 다 잡아먹는다"* |

세 진술이 합쳐지면 하나의 그림이 된다 — **수요는 효율로 줄지 않고(Altman), 공급은 GW당 수백억 달러가 들며(Huang), 그 결과 결손이 남는다(Musk).** 어느 하나도 다른 둘과 모순되지 않는다. ⚠️ 셋 다 그 결손을 메우는 것을 파는 위치에 있다는 점도 함께 읽는다.

[[compute-constrained-growth]]가 *"성장은 컴퓨팅 배분의 함수"* 라고 했다면, 이 페이지는 그 함수의 **정의역에 물리적 상한**이 있다고 말한다.

## 처방 — 각국에 기회

> 전 세계 국가들이 AI 데이터 센터에 관심이 있다면, **많은 전력을 생산할 수 있는 시설을 구축하고 AI 기업에 제공할 수 있는 기회**를 만들어준다고 생각합니다. 물론 그 대가로 이러한 AI 데이터 센터들은 **세금을 내고 합리적인 수수료** 등을 지불해야 할 것입니다.

같은 회의에서 세 판매자가 각국에 **서로 다른 층**을 권한다: 칩과 확산(Huang) · 모델 사용(Altman) · **발전소**(Musk). [[intelligence-as-infrastructure]]의 5단 케이크로 읽으면 Musk의 처방은 **층 1(에너지)에 집중하라**는 것이다.

⚠️ 그리고 그 처방의 실례로 자기 회사를 든다 — *"[[google-deepmind|Google]]과 [[anthropic|Anthropic]] 등이 **[[spacex|SpaceX]]로부터 컴퓨팅을 임대**하고 있는 것 (…) 이는 **우리 스스로 발전소를 건설**함으로써 가능한 일 (…) **그게 우리가 할 수 있는 유일한 방법**이었어요."* 자기 진술이며 소스 내 확인이 없다.

## ⚠️ 유보

- **수치의 출처가 없다.** *"인공지능 분야를 면밀히 관찰하는 분석가들의 공통적인 추정"* 이라고만 하고 이름·기관·보고서를 대지 않는다. 화자가 바로 앞에서 자기 정보원을 *"X 플랫폼"* 이라 밝혔다는 점을 함께 둔다(화자가 X의 소유주다).
- **15 GW가 무엇 대비 부족인지**의 기준선(총 수요 추정치)이 제시되지 않는다.
- 40~50% / 10~20%의 **기간과 지역 정의**가 느슨하다.
- 재생에너지·원전 신규 도입, 데이터센터 효율 개선 등 **공급 측 대응이 논의되지 않는다.**

## References

- [[tech-bridge-elon-musk-g20-ai-future]] — first-seen
- [[elon-musk]] · [[spacex]]
- 같은 병목의 다른 층: [[tech-bridge-jensen-huang-g20-agi]] · [[tech-bridge-altman-g20-economic-boom]]
- 관련: [[compute-constrained-growth]] · [[intelligence-as-infrastructure]]

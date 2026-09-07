---
title: Regulatory Capture
type: concept
category: theory
tags: [regulation, ai-policy, competition]
related: [cognitive-offloading, intent-alignment, ai-privilege, training-time-risk, agi-definition, default-legal-regulation, intelligence-abundance]
first-seen: tech-bridge-andrew-ng-ai-opportunity
sources: [tech-bridge-andrew-ng-ai-opportunity, tech-bridge-altman-astra-hardware, tech-bridge-altman-agi-superintelligence, tech-bridge-jensen-huang-g20-agi, tech-bridge-bill-gates-ai-warning, tech-bridge-elon-musk-g20-ai-future, tech-bridge-altman-g20-economic-boom]
created: 2026-08-31
updated: 2026-09-07
---

# Regulatory Capture

규제 설계가 기존 사업자 이익에 기울게 되는 현상. 본 위키에는 [[andrew-ng|Andrew Ng]]가 AI 공포 마케팅을 이 프레임으로 읽는 지점([[tech-bridge-andrew-ng-ai-opportunity]])에서 등장.

Ng의 주장: 거대 LLM이 지금 가장 가치 있는 자산인데, 다른 팀이 모델을 학습해 무료로 풀면 기존 사업자에게 치명적. 그래서 일부 leading AI 회사가 핵무기 비유·실수 cherry-pick·데이터센터 오정보로 공포를 키워, 오픈웨이트/저가 대안을 규제 쪽으로 누르려 한다. 회사 이름은 안 밝힘.

같은 정책 공간을 반대 입구로 다루는 자매 소스: [[tech-bridge-bill-gates-ai-warning]] — 산업 자율 규제 불신, 외부 중재자 필요. Ng는 일반 공포 규제에 회의하고, deepfake 같은 **구체 해악은 법으로 처벌**하는 쪽을 가른다.

## 네 입장이 된다 (2026-09-06)  →  다섯 (2026-09-07)

[[sam-altman|Sam Altman]]과 [[jensen-huang|Jensen Huang]]이 하루에 들어오면서 이 페이지의 정책 공간에 입장이 넷이 됐다.

| 화자 | 규제에 대한 입장 | 자율 판단 | 공포에 대한 태도 |
|---|---|---|---|
| [[andrew-ng]] | 일반 공포 규제 회의, **구체 해악만 법으로** | — | 공포 = 기존 사업자의 규제 포획 |
| [[bill-gates]] | **자율 규제는 작동하지 않는다**, 외부 중재자·라이선스 필요 | 불신 | 정당 — *"이번은 다르다"* |
| [[sam-altman]] ([[tech-bridge-altman-astra-hardware]]) | 정부의 **모델 테스트·공유 표준 찬성**, **고객 선별 반대**, 국제 체계 요구 | 신뢰 — 프론티어 훈련을 스스로 늦춤([[training-time-risk]]), *"정부가 금지하기 전에 우리가 먼저"* | 양쪽 경계 — *"양치기 소년도 위험, 눈 감기도 무책임"* |
| [[jensen-huang]] ([[tech-bridge-jensen-huang-g20-agi]]) | **"가상의 피해가 아니라 실제 피해를 규제"**, 기존 기관(FDA·NHTSA)으로 충분 | 전적 — *"제작자의 책임"* | 최악은 *"뒤쳐지는 것"*; *"발전이 오히려 안전성을 높였다"* |
| [[elon-musk]] ([[tech-bridge-elon-musk-g20-ai-future]]) | **기본값을 정하라** — *"새로운 것은 default legal이어야지 default illegal이어서는 안 된다"* → [[default-legal-regulation]] | 전적 | 공포를 논하지 않는다. 비용은 **지연** — *"막지는 못하지만 상당히 늦춘다"* |

Huang의 *"실제 피해"* 처방은 Ng의 *"구체 해악만"* 과 같은 형태이고, Altman의 *"정부 테스트는 찬성"* 은 Gates의 *"외부 중재자"* 에 절반 응답한다. **판매자일수록 자율 판단을 신뢰한다**는 것이 표의 한 축이다 — Ng의 원래 프레임(누가 규제를 원하는가는 누구에게 유리한가로 읽어라)이 여기에도 적용된다.

### Musk의 칸은 층이 다르다 (2026-09-07 추가)

앞의 넷은 모두 **규제의 대상**을 다퉜다 — 공포 vs 구체 해악 vs 실제 피해 vs 데이터 접근. [[elon-musk|Musk]]만 **입증 책임의 기본값**을 문제 삼는다. 목록에 무엇을 넣을지가 아니라 **목록에 없는 것을 어떻게 처리할지**다. 이 층에서 보면 Huang의 *"실제 피해만"* 과 Ng의 *"구체 해악만"* 은 default legal을 **전제하고도 명시하지 않은 것**이고, Gates의 *"라이선스"* 는 default illegal의 한 형태다. → [[default-legal-regulation]]

### 포획의 경로가 처음으로 명시된다

이 페이지는 지금까지 포획의 **결과**만 가지고 있었다([[andrew-ng]]: 공포 마케팅이 오픈웨이트를 규제 쪽으로 누른다). Musk가 **경로**를 댄다:

> 대부분의 국가들이 흔히 하는 것은 **숲에 이미 있는 큰 나무들에게는 과도한 지원**을 제공하고 **어린 묘목들에게는 충분한 지원을 제공하지 않는 것**입니다. (…) 왜냐하면 **대기업들은 대개 각국의 지도부에 접근할 수 있기 때문입니다. 그리고 규모가 작은 스타트업들은 그렇지 못합니다.**

**접근권의 비대칭**이다. Ng의 결과 진술과 모순되지 않고 같은 현상의 다른 절단면이다. 처방은 비대칭의 의도적 보정 — *"시스템은 큰 나무보다는 작은 나무를 지원하는 방향으로 편향되어야."*

> ⚠️ **화자 자신이 가장 큰 나무 중 하나를 여러 그루 소유하고 있다.** 이 진술을 어느 칸에 넣을지 열어 둔다. 이 표의 규칙(누가 규제를 원하는가는 누구에게 유리한가로 읽어라)은 규제 **완화**를 원하는 쪽에도 그대로 적용된다.

### 가격이 포획의 경로가 되는 다섯 번째 길

[[sam-altman|Altman]]이 G20에서 든 세 번째 위험은 **권력 집중**인데, 그 메커니즘이 규제가 아니라 **가격**이다 — *"인공지능을 보편화하지 못한다면 (…) **부유층들이 막대한 돈을 쏟아붓는 물건**이 될 것"*, *"어떤 사람들은 일찍 투자하고 어떤 사람들은 그렇지 않기 때문에 AI가 특정 분야에 집중되는 세상."* → [[intelligence-abundance]] · [[tech-bridge-altman-g20-economic-boom]]

### 걱정을 무엇으로 볼 것인가 — 갈리는 지점 하나 더

| 화자 | 걱정(우려·비관)의 지위 |
|---|---|
| [[jensen-huang]] | **지연 비용** — *"3년 전 속도를 늦춰야 한다던 시기 (…) 사실 그 발전이 오히려 안전성을 높였다"* |
| [[sam-altman]] | **안전의 생산 기제** — *"일이 잘 풀리는 이유 중 하나는 **사람들이 걱정하고** 스트레스를 받고 부정적인 측면을 살펴보고 그것들을 해결하려고 노력하기 때문"* (불 → 도시 화재 → 화재 안전 수칙) |

⚠️ 해소하지 않는다. 같은 회의, 같은 날, 서로 다른 상품을 파는 두 사람이다.

**데이터센터 오정보**에 대해서는 반대편 진술이 붙었다 — Ng가 공포 마케팅의 사례로 든 화제를, Altman이 운영자로서 반박한다(*"38,000 쿼리 = 아몬드 한 개"*, *"현대 데이터센터는 사무실 건물 수준의 물"*, ⚠️ 본인이 단서를 단 수치) → [[tech-bridge-altman-agi-superintelligence]].

그리고 규제의 **대상**이 갈리는 지점 — [[ai-privilege]]에서 Altman은 규제를 모델이 아니라 **정부의 데이터 접근**에 걸자고 한다. 규제 포획 논의가 "누가 모델을 규제하는가"에서 "누가 사용자 데이터에 접근하는가"로 한 칸 옮겨간 형태다.

⚠️ 네 입장을 해소하지 않는다. 넷 다 소스가 있고 인센티브가 다르다.

## References

- [[tech-bridge-andrew-ng-ai-opportunity]] · [[andrew-ng]] · [[tech-bridge-bill-gates-ai-warning]]
- 2026-09-06 추가: [[tech-bridge-altman-astra-hardware]] · [[tech-bridge-altman-agi-superintelligence]] · [[tech-bridge-jensen-huang-g20-agi]] · [[ai-privilege]]
- 2026-09-07 추가: [[tech-bridge-elon-musk-g20-ai-future]] · [[tech-bridge-altman-g20-economic-boom]] · [[default-legal-regulation]] · [[intelligence-abundance]] · [[elon-musk]]

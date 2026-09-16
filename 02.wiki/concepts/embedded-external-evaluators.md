---
title: 상주 외부 평가자 (Embedded External Evaluators)
type: concept
category: pattern
tags: [ai-safety, governance, regulation, evaluation, third-party, speed-limit]
aliases: [식품 검사관 모델, 제3자 상주 평가자, 평가자 처리량이 제한 속도]
related: [regulatory-capture, training-time-risk, verification-bottleneck, swiss-cheese-defense-in-depth, race-to-the-top, joint-democratic-oversight, coordinated-vulnerability-disclosure, uk-aisi]
first-seen: tech-bridge-dario-amodei-cbs-interview
sources: [tech-bridge-dario-amodei-cbs-interview]
created: 2026-09-16
updated: 2026-09-16
---

# 상주 외부 평가자

**제3자(비영리, 언젠가는 정부)의 평가자가 랩 안에 상주하며 모델의 훈련·실행 과정을 관찰하고, 그 회사가 약속한 안전 관행을 지키는지 검증한다.** [[dario-amodei|Dario Amodei]]가 [[tech-bridge-dario-amodei-cbs-interview]]에서 *"몇 시간 전에 낸 에세이"* 의 3단계 계획 중 **첫 단계이자 가장 중요한 것**으로 제시한다.

> ⚠️ **당사자 진술.** 규제 대상 기업의 CEO가 **업계 전체에** 같은 문턱을 제안하는 것이다. [[regulatory-capture]]의 규칙(누가 규제를 원하는가는 누구에게 유리한가로 읽어라)이 여기에도 적용된다.

## 주장

> **첫 단계는 상주 외부 평가자를 두는 것입니다. 제3자 비영리 기관, 언젠가는 정부 기관에서 온 사람들이 저희가 모델을 훈련하고 실행하는 과정을 관찰할 수 있게.** 그것이 궁극적으로는 **모델을 어떻게, 언제 출시하느냐보다 더 중요**하다고 생각합니다 — **더 신중하게 출시하기 위한 전제**이기 때문입니다. (04:10~04:43)

> **누군가 AI 모델을 만들 때마다, 최고의 안전 관행을 이해하고 있는 제3자 평가자가 그 회사가 약속한 안전 관행을 지키고 있는지 검증할 수 있도록. 식품 검사관 같은 것이죠.** (04:48~05:03)

세 가지가 정의된다 — **위치**(회사 안, 과정을 관찰), **소속**(회사 밖, 비영리 → 정부), **대상**(출시물이 아니라 **약속의 이행**). 검사 대상이 *모델* 이 아니라 *회사가 자기가 하겠다고 한 것을 하는가* 라는 점이 [[bill-gates]]의 진단(*"자발적 리뷰는 기준과 시정이 없어 공허하다"*)에 정확히 대응한다 — **기준은 회사가 공개한 약속, 시정은 검사관.**

## 처리량이 제한 속도가 된다

진행자의 반문(*"기술이 이렇게 빠른데 검사관이 따라가나"*)에 대한 답이 이 패턴의 두 번째 절반이다.

> 그들이 할 수 있는 일 중 하나는 **자기들이 따라갈 수 있는 속도를 우리에게 알려 주는 것**입니다. **그것이 기술의 제한 속도를 정하는 요인 중 하나가 될 수 있습니다.** 우리도 이해해야 하고 외부 평가자도 이해해야 합니다. (05:11~05:28)

**검증 처리량 = 배포 속도의 상한**을 **설계로** 세운다. 이 위키가 [[verification-bottleneck]]·[[mousepower]]에서 본 것은 *에이전트 생산물의 검증이 병목이 됐다는 관찰* 이었고, [[verification-cost-asymmetry]]는 *검증이 실행보다 싼 작업만 에이전트에 맞는다* 는 조건이었다. 이 패턴은 그 반대 방향이다 — **검증이 실행보다 느리다면 실행을 검증 속도에 맞춰라.** 이 위키에서 병목을 *제거할 대상* 이 아니라 *의도한 제어 장치* 로 놓는 첫 페이지다.

## 3단계 안에서의 자리

| 단계 | 내용 | 조율 |
|---|---|---|
| **1** | **이 패턴** — 각 랩에 상주 평가자 | 랩 단위 |
| 2 | 여러 업계 참여자가 이에 합의 | 업계 |
| 3 | 출시 안전 기준·속도 기준 | **정부가 방에 있는 상태에서** |

1단계가 *"더 중요"* 하다는 근거는 **전제(predicate)** 라는 것이다 — 관찰이 없으면 2·3단계의 기준이 검증 불가능하다. 이 논리는 [[ai-arms-limitation-lens]]의 *"협상의 핵심은 검증"* 과 같은 것이고, 국내(랩) 층과 국제(정부) 층에서 **같은 구조가 반복**된다.

## 위키의 다른 페이지와의 관계

- [[training-time-risk]] — [[sam-altman]]의 프론티어 RL 연기는 **회사 내부 판단**이었다. 이 패턴은 그 판단을 **외부 관찰 아래** 둔다. 그리고 관찰 대상에 *훈련 과정* 이 명시된다 — 게이트를 훈련 시점으로 앞당긴 것과 일치한다.
- [[uk-aisi]] · [[project-glasswing]] — 이 위키가 아는 **기존 외부 평가**는 *출시 전 모델을 받아 시험하는* 형태였다. 이 패턴은 **과정 안에 들어가는** 형태라 한 단계 깊다.
- [[coordinated-vulnerability-disclosure]] — 절차 규범이 산업 전체에 적용된 선례.
- [[swiss-cheese-defense-in-depth]] — 이 패턴은 **한 장의 치즈**다. 소스도 *"단 하나의 것은 없다"* 고 한다.

## ⚠️ 유보

- **누가 평가자인가** — *"제3자 비영리"* 가 어느 기관인지, **누가 비용을 대는지**, 랩과의 독립성을 어떻게 보장하는지 없다. 이 위키가 [[skill-evals]]·[[tech-bridge-lauren-tan-trusting-agents]] 이래 네 번 표시한 **작성자=검증자** 문제가 **기관 층위에서** 그대로 열려 있다.
- **"약속한 관행"의 내용** — 검사 기준이 회사가 공개한 약속이라면, **약속을 낮게 하는 회사가 유리**해지는 구조를 소스가 다루지 않는다.
- **처리량이 제한 속도가 되면 평가자를 늘리는 인센티브는 누구에게 있는가** — 없다.
- **"경쟁사를 포함한 업계 리더들이 동의"** — 진행자 서술 + 화자의 일반 진술. 누가 무엇에 동의했는지 없다.

## References

- [[tech-bridge-dario-amodei-cbs-interview]] — first-seen
- [[dario-amodei]] · [[anthropic]]
- 관련: [[regulatory-capture]] · [[training-time-risk]] · [[verification-bottleneck]] · [[bill-gates]] · [[ai-arms-limitation-lens]]

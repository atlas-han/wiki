---
title: "체감 생산성과 실제 생산성의 괴리 (Perceived vs Actual Productivity)"
type: concept
category: theory
tags: [developer-productivity, perception-gap, self-report, measurement, change-confidence, ai-adoption, metr]
aliases: [체감 vs 실제 생산성, perception gap, 체감 생산성, perceived productivity, change confidence, 변경 확신]
related: [ai-measurement-framework, dora-metrics, agent-roi-measurement, frontier-engineering, verification-bottleneck, trusted-throughput, agent-trust-curve]
first-seen: tech-bridge-dx-ai-impact-trends
sources: [tech-bridge-dx-ai-impact-trends]
created: 2026-10-03
updated: 2026-10-03
---

# 체감 생산성과 실제 생산성의 괴리

**AI 코딩 도구를 쓰는 개발자가 느끼는 생산성 변화와 측정된 변화가 어긋난다는 관측 — 그리고 그 어긋남이 한 방향(과대평가)만이 아니라는 것.** 이 위키가 모은 생산성 수치는 대부분 **개인 체감**이었다([[frontier-engineering]]의 *"10–20%"*, 여러 화자의 *"10배"*). [[tech-bridge-dx-ai-impact-trends]]([[getdx|DX]], [[justin-reock|Justin Reock]])가 처음으로 **체감과 집계를 나란히** 놓았다.

## 세 가지 어긋남

### 1. 개인 실험 — 느려졌는데 빨라졌다고 느낀다 (METR, 화자 전언)

> *"in these 16 engineers that were part of that study small study flawed study uh the productivity went down by about 19% but the perception went up by about 20%. So there was like a 40% spread in perception of productivity versus actual productivity."* (04:02~04:17)

화자는 이 연구를 *"obviously infamous flawed MER[=METR] study"*(03:49)라 부르고, METR이 *"back in February"* 후속 발표에서 신호 일부가 불완전했다고 밝혔다고 전한다(03:55~04:01). ⚠️ **전언이다** — 이 위키는 METR 원문을 확인하지 않았고 METR 페이지도 없다. "40%"는 −19%와 +20%의 차이(약 39%p).

### 2. 집계 — 체감은 거의 오르지 않았다

> *"This number shows an increase of about four and a halfish percent. Um, but given that that's a full year and given all the investment and cost and new spend on AI, it's interesting that this perceived rate has not (…) crept up a little bit more."* (03:32~03:47)

> *"But here when we look at this on more of an aggregate things interestingly stay uh sort of flat."* (04:17~04:23)

**체감 전달 속도 +약 4.5%(1년).** 시스템 지표도 크지 않다 — PR 처리량 증가 **중앙값 7.7%, 평균 13%, 상위 70%대, "Nobody hit 2x"**(15:19~15:32). 집계에서는 체감과 실제가 **둘 다 작게, 비슷하게** 움직인다. ⚠️ DX 플랫폼 데이터, 벤더 진술.

### 3. 품질 체감끼리의 분열 — 고치기 쉬운데 믿지 못한다

| 설문 지표 | 1년 변화 | en-orig |
|---|---|---|
| 코드 유지보수성(maintainability) | *"gone up almost 4%"* | 06:00~06:05 |
| 변경 확신(change confidence) | *"gone down 6%"* | 06:24~06:29 |
| 점진적 전달(incremental delivery) | *"gone down 10%"* | 08:12~08:14 |

두 지표는 *"traditionally we've seen closely associated"*(06:11~06:17)였는데 갈라졌다.

> *"agents and assistants are making it easier for me to understand and modify the code that's in front of me, but I trust the outputs less. I'm more afraid now of breaking things than I was a year ago. So, it's an interesting psychological effect"* (06:30~06:44)

화자가 꼽은 원인은 **PR 크기 증가**(평균 44 → 72줄, 06:44~07:02). → [[dora-metrics]]

## 읽기 — 체감은 무엇을 재는가

- **1(METR)과 2(DX)는 충돌하지 않는다.** 1은 *통제 실험의 개인*이 크게 과대평가한 것이고, 2는 *대규모 설문의 평균*이 작게 오른 것이다. 공통점: **체감만으로는 효과의 크기를 알 수 없다.** → [[ai-measurement-framework]]가 설문과 시스템 지표를 같이 쓰는 이유.
- **3은 체감이 틀렸다는 게 아니라, 체감이 무엇을 재는지에 따라 방향이 갈린다는 것.** *읽고 고치기*(유지보수성)는 AI가 돕고, *내보내도 되는가*(변경 확신)는 AI가 해친다. 이 위키의 [[verification-bottleneck]] — **생성은 쉬워지고 검증은 어려워진다** — 의 설문 버전.

## 위키의 다른 페이지와

> ⚠️ **Contradiction: 배수 서사 vs 집계.** [[frontier-engineering]](Amazon, [[clare-liguori|Clare Liguori]])은 사내 파일럿의 프로덕션 배포 속도를 *절반은 3x 미만, 다른 절반은 중앙값 4.5x, 일부 10x+* 로 보고했다. DX 집계는 *"Nobody hit 2x"*. 지표(배포 속도 vs PR 처리량)와 모집단(선별 파일럿 vs 플랫폼 전체)이 달라 직접 비교는 안 되지만, **같은 시기 업계의 두 진술이 정면으로 엇갈린다.** 둘 다 당사자 데이터다.

- [[agent-trust-curve]] — 신뢰는 경험으로 쌓인다는 개인 서사. DX의 *변경 확신 −6%* 는 **집계에서는 신뢰가 오히려 줄었다**는 반대 방향의 데이터. 시간 축(1년)이 짧아서인지, 개인과 집계의 차이인지는 미해결.
- [[trusted-throughput]] — 처리량의 값은 신뢰에서 온다. 변경 확신이 떨어지는 동안 처리량만 오르면 그 값은 깎인다.
- [[agent-roi-measurement]] — *"이 방의 모두가 편향돼 있다"* (얼리어답터 표본). 체감의 편향을 표본 쪽에서 본 것.

## 미해결

- DX 설문의 문항·척도 — "4%"·"6%"·"10%"가 응답 점수의 변화인지 동의 비율의 변화인지 미발화.
- METR 후속 발표의 내용 — 화자 전언뿐.
- 변경 확신 하락이 **실제 CFR 상승과 상관**하는지 — 두 데이터를 연결한 분석은 발화되지 않는다.

## References

- [[tech-bridge-dx-ai-impact-trends]] — first-seen
- [[getdx]] · [[justin-reock]]
- [[ai-measurement-framework]] · [[dora-metrics]] · [[verification-bottleneck]] · [[frontier-engineering]] · [[tech-bridge-frontier-engineering]] · [[agent-trust-curve]] · [[trusted-throughput]] · [[agent-roi-measurement]]

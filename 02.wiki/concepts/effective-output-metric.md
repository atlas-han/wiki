---
title: "유효 산출량 (Effective Output Metric) — 줄 수 대신 커밋의 가치를 모델이 채점한다"
type: concept
category: technique
tags: [productivity-measurement, developer-productivity, metrics, salesforce, stanford, ml-scoring, cost-per-output, goodhart]
aliases: [effective output, 유효 산출량, valid output, 유효 산출량 점수, 점수당 비용, cost per score]
related: [perceived-vs-actual-productivity, agentic-coding-maturity-curve, trusted-throughput, effort-output-outcome-mission, model-mixing-economics]
first-seen: tech-bridge-salesforce-claude-code-agentic-shift
sources: [tech-bridge-salesforce-claude-code-agentic-shift]
created: 2026-11-08
updated: 2026-11-08
---

# 유효 산출량 (Effective Output)

**AI 도입의 효과를 코드 줄 수가 아니라 커밋이 실제로 바꾼 것의 가치로 재려는 점수.** [[tech-bridge-salesforce-claude-code-agentic-shift]]의 해설에 따르면 [[salesforce|Salesforce]]가 Stanford 연구진과 함께 만들었다. 커밋마다 머신러닝 모델이 시니어 엔지니어 패널처럼 코드를 보고 점수를 매긴다.

> *"세일즈 포스는 스탠포드 연구진과 함께 유효 산출량이라는 점수를 만들었습니다."*(01:57~02:00)

> ⚠️ **소스 하나, 2차 전달.** 이름(*유효 산출량* — 영어 더빙은 *valid output*)은 해설의 한국어다. 원 명칭 · 모델 · 채점 기준 · Stanford 쪽 논문은 위키가 확인하지 않았다.

## 해설이 전하는 설계

- **문제**: 줄 수를 세면 *주석만 잔뜩 달아도* 점수가 오른다 — 측정이 목표가 되면 왜곡된다는 고전적 문제(Goodhart, 위키의 읽기).
- **가중치**: 주석 · 단순 수정은 낮게, 로직 변경 · 새로 만든 것은 높게.
- **채점자**: 커밋마다 ML 모델이 *"시니어 엔지니어 패널처럼"* 검토.
- **결과**: 점수가 두 배로 뛰었다.
- **다음 단계**: *"이제는 점수당 비용까지 따지면서 정말 효과가 있는지 확인하고 있고요."*(02:18~02:21) — 산출이 아니라 **단위 비용**을 본다 → [[model-mixing-economics]](일에 맞는 모델을 맞는 가격에).

## 위키 안의 연결

- [[perceived-vs-actual-productivity]] — 체감과 측정의 차이를 다룬 페이지. 이 점수는 *측정 쪽*의 한 설계다. 다만 채점자도 모델이라 **모델이 모델의 산출을 채점한다**는 순환이 있다(해설은 다루지 않음).
- [[trusted-throughput]] — 산출량만이 아니라 *믿을 수 있는* 산출량. Salesforce 해설은 같은 영상에서 *코드당 버그 감소 · 장애 5% 감소*를 따로 대며 품질을 별도 지표로 둔다.
- [[effort-output-outcome-mission]] — 이 점수는 output 층이다. outcome(고객 가치)은 아니다.

## 미해결

- 채점 모델의 정확도 · 사람 평가와의 일치도, 점수를 높이려는 행동 변화(새 Goodhart)가 있었는지.
- "두 배"의 기간과 비교 기준.

## References

- [[tech-bridge-salesforce-claude-code-agentic-shift]] (3절)

---
title: 과지출·저활용 둠 루프 (Overspending and Underusing)
type: concept
category: pattern
tags: [token-economics, adoption, budget, fomo, austerity]
aliases: [둠 루프, overspending and underusing, 토큰 맥싱 악순환]
related: [trusted-throughput, token-roles, model-mixing-economics, agent-roi-measurement, agent-org-adoption, compute-constrained-growth, value-maxing, token-minimization-trap]
first-seen: tech-bridge-mousepower-measuring-agents
sources: [tech-bridge-mousepower-measuring-agents, tech-bridge-tokenmaxxing-to-valuemaxxing]
created: 2026-09-13
updated: 2026-09-24
---

# 과지출·저활용 둠 루프

**토큰을 과하게 쓰다가 청구서에 놀라 긴축으로 꺾이고, FOMO가 차오르면 다시 과하게 쓰는 순환.** [[maximillian-piras]]가 [[tech-bridge-mousepower-measuring-agents]]에서 제시했고, 용어 자체는 **Ramp**에서 빌렸다고 밝힌다.

> **토큰 맥싱으로 스스로를 긴축(austerity)으로 몰아넣고, 그러다 루프에서 이탈했다가, FOMO가 다시 차오르면 재시도**하는 악순환이죠.

## 개인 층의 증상

발표 오프닝이 그대로 사례다 — 발표를 하면서 **백그라운드로 여러 에이전트를 병렬로** 돌려 슬라이드를 탐색시키고:

> **청구서를 받기 전까지는 아주 재미있습니다.** 그러다 궁금해지죠 — **이게 다 그만한 가치가 있었나?**

## 조직 층의 증상

> **1년 치 토큰 예산을 한 분기에 다 태우거나 토큰 리더보드 같은 것에 매달리는** 장면이 나옵니다. **인센티브가 정렬되지 않았고, 기술 부문 자체도 가치의 올바른 척도를 못 잡은** 겁니다.

**토큰 리더보드**는 [[trusted-throughput]]이 경고한 Goodhart 문제의 구체적 형태다 — 투입량을 성과로 착각하는 지표.

## 빠져나오는 방향

소스가 든 유일한 반례는 **Coinbase**다 — CEO가 X에 올린 차트로, **기본 모델을 바꾸고 프런티어 모델을 가장 어려운 작업에만 남겼더니 AI 지출이 토큰 사용량에서 갈라지기 시작**했다.

> **이건 좋은 출발입니다.** 하지만 **문제는 여전히 토큰에 너무 집중돼 있다**는 것입니다.

즉 **모델 믹스 최적화는 지출을 줄이지만 루프를 깨지는 못한다** — 루프를 깨는 것은 **가치를 전달하는 척도**다. → [[model-mixing-economics]] · [[agent-roi-measurement]] · [[mousepower]]

## [[trusted-throughput]]과의 관계

같은 단어에서 만난다. 그 페이지의 원 소스([[ironclad|Ironclad]])는 *"'긴축'에 관한 것이 아니라 토큰 사용에 대한 ROI를 향상시키는 것"* 이라고 했고, 이 소스는 **긴축을 루프의 한 국면**으로 그린다.

**같은 진단, 다른 층** — 그쪽은 조직이 스스로에게 쓰는 지표, 이쪽은 **판매자가 고객에게 가치를 전달하는 문제**다.

## 표시해 둔 것

> ⚠️ **수치가 없다.** Ramp 글도 Coinbase 차트도 **링크·날짜·값이 자막에 없다.**

## References

- [[tech-bridge-mousepower-measuring-agents]] · [[trusted-throughput]] · [[model-mixing-economics]] · [[agent-roi-measurement]] · [[token-roles]] · [[maximillian-piras]]

## 순환인가, 단계인가 — 밸류맥싱 편 (2026-09-24 · [[tech-bridge-tokenmaxxing-to-valuemaxxing]])

[[ibm|IBM Technology]] 계열 해설이 같은 두 국면을 다른 이름으로 부른다 — **토큰맥싱**(*"활동량이 많을수록 가치도 커진다는 믿음에 근거해 인공지능 사용을 최대화"*, 01:19~01:24)과 **토큰 최소화**(03:20). 그리고 이 페이지가 긴축에 대해 말하지 않은 것 둘을 더한다:

- **긴축도 같은 함정이다** — *"둘 다 토큰 소비[가] 중요한 주요 지표[라고] 가정합니다. 그 어느 것도 운영 결과를 측정하지 않습니다"*(03:24~03:32). 이 페이지가 Coinbase 반례에 붙인 *"문제는 여전히 토큰에 너무 집중돼 있다"* 를 **국면 전체로** 넓힌 진단이다.
- **긴축이 무엇을 자르는가** — 명백한 낭비(큰 도구 카탈로그·낡은 컨텍스트)를 지나 **작업 설명·도메인 제약·아키텍처 컨텍스트**까지, 그 결과 *입력 500 토큰 절약 → 디버깅·재작업 5,000 토큰*(04:04~04:10, ⚠️ 가상 예시). → [[token-minimization-trap]]

> ⚠️ Contradiction: 이 페이지(Piras)는 맥싱 ↔ 긴축의 **순환**(FOMO가 차오르면 재시도)을, IBM 계열 편은 맥싱 → 최소화 → 가치의 **단계적 진행**(*"첫 번째 장은 [도입]에 대해 다루었[고], 다음 장은 가치"*, 07:57~08:02)을 그린다. 어느 쪽도 조직 사례로 뒷받침하지 않는다. → [[value-maxing]]

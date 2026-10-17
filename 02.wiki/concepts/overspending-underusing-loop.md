---
title: 과지출·저활용 둠 루프 (Overspending and Underusing)
type: concept
category: pattern
tags: [token-economics, adoption, budget, fomo, austerity]
aliases: [둠 루프, overspending and underusing, 토큰 맥싱 악순환]
related: [trusted-throughput, token-roles, model-mixing-economics, agent-roi-measurement, agent-org-adoption, compute-constrained-growth, value-maxing, token-minimization-trap, reserve-then-settle]
first-seen: tech-bridge-mousepower-measuring-agents
sources: [tech-bridge-mousepower-measuring-agents, tech-bridge-tokenmaxxing-to-valuemaxxing, tech-bridge-factory-software-factory, tech-bridge-kimchi-cost-per-task-harness, tech-bridge-stigg-ai-companies-building-banks, tech-bridge-tailscale-aperture-ai-without-lock-in, tech-bridge-factory-bug-report-to-production]
created: 2026-09-13
updated: 2026-10-17
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

## Coinbase 차트, 다르게 읽기 (2026-10-02 · [[tech-bridge-factory-software-factory]])

[[tereza-tizkova|Tereza Tížková]]([[factory-ai|Factory]])도 Coinbase CEO의 트윗 차트를 든다 — *"they continue growing and token maxing but they stopped spending so much money"*(05:30~05:35). 방법으로 넷을 꼽는다: 사람별 기본 모델(프런티어를 기본값으로 밀지 않기), 캐싱, **지출 한도 없이 결과를 보여 달라**, 라우팅(05:36~06:06).

> ⚠️ **Contradiction: 같은 차트(로 보이는 것)의 평가.** 이 페이지의 첫 소스(마우스파워 편)는 Coinbase를 *"좋은 출발이지만 문제는 여전히 토큰에 너무 집중돼 있다"* 로 유보했다. Factory 편은 **토큰 소비가 계속 느는 것을 문제 삼지 않고**(*"token maxing"*) 지출이 갈라진 것을 성공으로 든다. 다만 *지출 한도 없이 결과를 요구* 한다는 레버는 이 페이지의 처방(**결과로 추적**)과 같은 방향이다. 두 소스 모두 차트 수치는 화면뿐이고, 같은 차트인지는 미확정.

## 조직 층의 실명 사례들, 그리고 긴축 대신 단가 (2026-10-09 · [[tech-bridge-kimchi-cost-per-task-harness]])

[[cast-ai|Cast AI]]의 Laura가 든 *"in the last few weeks"* 의 두 뉴스: 인도의 한 회사가 *"spent $500 million on anthropic alone in one months"*, Uber CTO가 *"in the last four months he actually used the entire budget of anthropic for the entire year"*(00:43~01:06) — 이 페이지의 *"1년 치 토큰 예산을 한 분기에"* 의 실명 판본. ⚠️ 둘 다 보도·트윗 미특정. 5억 달러 일화는 [[tech-bridge-trusted-throughput]]에도 있다(같은 보도인지 미확인).

루프의 긴축 국면(*"Companies responded this by limiting the use of token"*, 01:18~01:21)을 Kimchi는 **틀린 대응**으로 보고, 빠져나오는 길을 Coinbase와 같은 방향 — **모델 믹스를 하네스가 자동으로** — 에서 찾는다. 자사 3개월 차트: 토큰 1.5배↑, 비용 1.5배↓(05:06~05:21). ⚠️ 이 페이지의 결론(*모델 믹스 최적화는 지출을 줄이지만 루프를 깨지는 못한다*)에 대한 반례는 아니다 — 가치 척도는 여전히 없다.

## 파는 쪽에서 본 원인 — 검사가 청구서 뒤에 온다 (2026-10-12 · [[tech-bridge-stigg-ai-companies-building-banks]])

[[dor-sasson|Dor Sasson]]([[stigg|Stigg]] CEO)은 이 페이지의 조직 층 증상을 **공급자 인프라의 결함**으로 읽는다 — *"the checks for what you're entitled, what you're allowed to do, whether you're an agent or a user via AI product, happened uh after uh the invoice and not before."*(04:32~04:46) → *"it's sticker shock"*(05:03~05:08). 해법은 은행처럼 *"check before we draw down, before we consume"*(05:20~05:25) → [[reserve-then-settle]]

그가 든 사례(⚠️ 출처 미제시):
- 이름 없는 회사 — *"half a billion of their AI cloud credits just merely having like a few employees burning through the entire organization contract."*(03:44~03:53)
- [[uber|Uber]] — *"torched down their entire uh AI usage consumption budget for the year in just a few weeks into the year."*(03:55~04:04)
- Replit — *"what could happen if uh a single org has three users that are basically burning down the entire credit pool"*(04:07~04:14) — ⚠️ 실제 사건이 아니라 예시로 발화.

> ⚠️ **Contradiction: Uber의 기간.** 위 Kimchi 편(Laura)은 Uber CTO가 *"in the last four months"* 에 연간 Anthropic 예산을 썼다고 했다. Sasson은 *"just a few weeks into the year"*, 공급자 미언급. **넉 달 대 몇 주** — 둘 다 출처 미제시, 이 위키는 판정하지 않는다.
>
> ⚠️ **"5억" 일화의 세 번째 판본.** Laura(인도 회사, Anthropic, 한 달), [[mingsheng-hong|Hong]](한 달에 Claude 5억 달러), Sasson(이름 없는 회사, *"AI cloud credits"*, 직원 몇 명이 조직 계약 전체를 소진). 세부가 다르다 — 같은 사건인지 미확인.
>
> ⚠️ **처방의 대립.** Kimchi는 *토큰 배급은 틀렸다(무제한·저렴하게)*, Sasson은 기업 구매자가 팀·사용자·에이전트별 *"spend caps"*·*"fine-grained control"* 을 원한다(13:14~13:48). 층위가 다르지만(사내 정책 vs 공급자 기능) *통제가 답인가* 에서 갈린다. 둘 다 벤더.

## 청구서 공황의 다른 형태 — 벤더 통합 (2026-10-17 · [[tech-bridge-tailscale-aperture-ai-without-lock-in]])

[[remy-guercio|Remy Guercio]]([[tailscale|Tailscale]])가 지난 6개월 동안 수백 명과 나눈 대화(⚠️ 일화): *"I don't know what's going on. I know we're using a lot of AI. I get, you know, uh I get an Anthropic bill every day. Uh, I get a Codex bill every day."*(03:47~03:56) 공황의 장면은 이렇다: *"finance is talking to you, IT is being like, 'What are you doing?' You know, like we said to you know, use AI, but maybe not use that much AI."*(04:36~04:44) 흔한 반응은 *"we're just going to like consolidate on a single vendor. Maybe two vendors, right?"*(04:09~04:12)이고, 화자는 *"that is not not a great idea."*(04:21~04:23)라고 한다.

이 페이지의 "조직 층의 긴축"이 지출을 줄이는 것이라면, 여기서는 **선택지를 줄이는 것**이 긴축이다. 원인 쪽 진단도 있다. 토큰맥싱은 *"wasted tokens by default"*(02:07~02:12)를 부추긴다. 화자의 처방은 [[ai-gateway]]와 *"ROI maxing"*([[value-maxing]])이다. ⚠️ 벤더 발표. ko는 *"not a great idea"* 를 "아이디어는 좋지만"(04:27~04:29)으로 뒤집는다.

## 벤더의 처방 — 모델 비종속과 "don't token max" (2026-10-17 · [[tech-bridge-factory-bug-report-to-production]])

[[davis-palmie|Davis Palmie]]([[factory-ai|Factory]])는 비용 폭증을 *"headlines"*(Uber CTO의 *"by April"*, Microsoft의 Claude Code 라이선스 회수, 02:45~02:56)로 꺼내고, 답으로 모델 비종속을 든다: *"You want the maximum uh cost efficiency and the minimum effectiveness necessary for each task."*(03:08~03:15) 맺음은 *"And don't token max. Measure what actually matters."*(17:43~17:48)이다. 같은 날 업로드된 Tailscale 편과 함께 **벤더 둘이 "단일 공급자에 묶이지 말라"를 비용 처방으로** 낸다. ⚠️ 일화는 출처 미제시. ko는 맺음을 **"그리고 아닙니다 / 토큰을 최대화하세요."**(17:40~17:44)로 뒤집는다.

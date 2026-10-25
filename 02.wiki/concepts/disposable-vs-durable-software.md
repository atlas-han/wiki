---
title: 일회용 vs 오래 쓰는 소프트웨어 (Disposable vs Durable Software)
type: concept
category: framing
tags: [code-quality, disposable-software, durable-software, engineering-rigor, change-cost, isolation, vibe-coding]
aliases: [disposable software, durable software, 일회용 소프트웨어, 오래 쓰는 코드, 네 가지 기준, four factors]
related: [decision-quality, technical-debt, agent-sandboxing, hard-vs-soft-enforcement, verification-bottleneck, risk-proportional-human-review, action-reversibility, codebase-gardening]
first-seen: tech-bridge-kanat-alexander-disposable-vs-durable
sources: [tech-bridge-kanat-alexander-disposable-vs-durable]
created: 2026-10-25
updated: 2026-10-25
---

# 일회용 vs 오래 쓰는 소프트웨어

**코드 품질에 얼마나 공을 들일지는 그 소프트웨어가 스펙트럼의 어디에 있는지로 정한다**는 틀이다. 위치는 네 기준이 정한다. **실패의 피해(consequences) · 교체 비용(cost of replacement) · 의존 관계(dependencies) · 유지 비용(cost of maintenance)** 이다. 넷 다 낮으면 disposable이고 엔지니어링 엄격함은 필요 없다. 넷 다 높으면 durable이고 수십 년 쌓인 관행이 전부 필요하다. [[max-kanat-alexander|Max Kanat-Alexander]]가 [[tech-bridge-kanat-alexander-disposable-vs-durable]]에서 제시했다.

> *"We can determine where you are on this scale by those four factors (…) If they're all low, it's disposable software. If they're all high, it's durable software. And look, any person who's written software for a long time knows you should air[err] on the side of it being durable."*(03:00~03:20)

## 핵심 주장

1. **"AI가 만들었다"는 기준이 아니다.** 해설: *"AI가 만들었다고 자동으로 일회용이 되는 건 아니에요."*(02:32~02:37) 생성 비용이 0에 가까워져도 **교체 비용만 낮아질 뿐** 나머지 셋은 그대로일 수 있다.
2. **답은 depends가 아니라 yes or no다.** *"does code quality even matter for disposable software? No. For durable software? Yes."*(05:31~05:41)
3. **애매하면 durable 쪽으로 기운다.** *err on the side of durable* 이다.
4. **위치는 움직인다.** 해설: 잠깐 쓸 거라고 이름 붙였어도 *"동료들이 매일 쓰기 시작하고 다른 프로그램까지 연결되면 조건이 달라지죠"*(03:28~03:33). 해설은 Charity Majors(Honeycomb)를 인용해 두 종류가 한 제품 안에 공존하고 시제품이 durable이 될 수 있다고 덧붙인다(⚠️ 원문 미확인).
5. **일회용 지위는 환경으로 지킨다.** 고객 데이터·PII가 없는 격리 환경에만 배포하게 해 *"enforce independence"* 한다(03:46~04:01). 이렇게 피해와 의존을 **설계로 낮추면** 더 자유롭게 버릴 수 있다.
6. **durable의 비용은 낮춘다.** 저장·업로드 때 자동으로 도는 검사, 빠르고 결정적인 테스트, 처음부터 켜 둔 검사 규칙을 쓴다(해설). 단 오탐이 많으면 곤란하고, 완벽함이 아니라 *계속 나아지는가* 를 본다.

## 맡기기 전 세 질문 (해설, 05:51~06:00)

망가지면 누가 곤란해지나(피해)? 다른 곳에서 이 코드를 믿고 쓰나(의존)? 쉽게 다시 만들 수 있나(교체)? — 네 번째인 유지 비용은 질문에서 빠졌다.

## 다른 페이지와의 관계

- [[decision-quality]] — IBM 편([[tech-bridge-ai-era-code-quality]])은 같은 질문 *"AI 시대에 코드 품질은?"* 에 **무엇을 평가하나**(구현 → 결정)로 답했다. 이 틀은 **얼마나 엄격해야 하나**로 답한다. 둘은 서로 보완한다.
- [[technical-debt]] — durable 쪽에서 가장 비싼 것은 Kanat-Alexander가 말한 두 번째 위험, *"make it harder to make future changes"* 다.
- [[agent-sandboxing]] — 같은 *disposable* 이라는 말이 거기서는 **에이전트를 가두는** 환경을, 여기서는 **일회용 코드를 durable 시스템에서 떼어 놓는** 환경을 뜻한다.
- [[risk-proportional-human-review]] · [[action-reversibility]] — 같은 계열의 비례 원칙을 **PR·행동 단위**가 아니라 **소프트웨어 전체의 수명 단위**에 적용한 것이다. *cost of replacement* 는 가역성의 시스템 판이다.

> ⚠️ **이분법의 범위.** yes/no 결론은 네 기준이 **한쪽으로 몰린 양 끝**에 대한 것이다. 섞인 경우(예: 피해는 크지만 교체가 쉬움)에 대한 원음은 자막에 없다.

## References

- [[tech-bridge-kanat-alexander-disposable-vs-durable]] (first-seen)
- [[max-kanat-alexander]] · [[decision-quality]] · [[tech-bridge-ai-era-code-quality]]

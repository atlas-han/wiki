---
title: 일회용 vs 오래 쓰는 소프트웨어 (Disposable vs Durable Software)
type: concept
category: framing
tags: [code-quality, disposable-software, durable-software, engineering-rigor, change-cost, isolation, vibe-coding]
aliases: [disposable software, durable software, 일회용 소프트웨어, 오래 쓰는 코드, 네 가지 기준, four factors]
related: [decision-quality, technical-debt, agent-sandboxing, hard-vs-soft-enforcement, verification-bottleneck, risk-proportional-human-review, action-reversibility, codebase-gardening, shaping-the-build]
first-seen: tech-bridge-kanat-alexander-disposable-vs-durable
sources: [tech-bridge-kanat-alexander-disposable-vs-durable, tech-bridge-andrew-ng-ai-engineering-skills-map, tech-bridge-nick-saraev-karpathy-ai-habits, tech-bridge-karpathy-hackertube-two-hours-five-words, tech-bridge-jonathan-blow-30-years-zero-progress]
created: 2026-10-25
updated: 2026-11-20
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

## 앱은 데이터 위의 포장 — Saraev의 일반화 (2026-11-08 · [[tech-bridge-nick-saraev-karpathy-ai-habits]])

Karpathy가 앱 대신 데이터 소스와 프롬프트를 공유한다는 전달에 화자가 붙인 해석: *"most specific implementations are just sort of wrappers around a core truth, which is the data."*(04:47~04:53) 이 페이지의 축으로 보면 **앱이 일회용, 데이터가 오래가는 쪽**이라는 주장이다 → [[share-data-and-prompt-not-app]]. ⚠️ 개인 프로젝트 맥락의 해석이고, 유지보수 · 보안 책임이 받는 사람에게 넘어가는 점은 다루지 않는다.

## References

- [[tech-bridge-kanat-alexander-disposable-vs-durable]] (first-seen)
- [[max-kanat-alexander]] · [[decision-quality]] · [[tech-bridge-ai-era-code-quality]]

## 수명이 아니라 시점으로 — 단계 의존 (2026-11-01 · [[tech-bridge-andrew-ng-ai-engineering-skills-map]])

[[andrew-ng|Ng]](제목 · 설명란 · 태그 근거)은 같은 질문(얼마나 공들일까)에 **프로젝트 단계**로 답한다. *"for early stage projects, so long as you can do it in a responsible, safe way, build a quick and dirty prototype, see what happens, throw it away, build another quick and dirty prototype, see what happens, and drive rapid learnings."*(07:47~08:01) 그리고 *"there's also a time and place to thinking carefully about architecture"*(08:01~08:05). 이 페이지의 네 기준이 **소프트웨어의 성질**로 위치를 정한다면, Ng은 **같은 프로젝트가 시간에 따라 이동한다**고 본다(핵심 주장 4 *위치는 움직인다* 와 같은 방향). 두 소스 모두 일회용의 조건으로 **민감 데이터 격리**를 단다. → [[shaping-the-build]]

## 2026-11-19 — "크고 버려도 되는 소프트웨어를 마음껏 주문하라" ([[tech-bridge-karpathy-hackertube-two-hours-five-words]])

Karpathy의 10월 초 글의 결론으로 해설이 전한다(⚠️ 2차 전달): *"지능과 코드가 흔해진 만큼 예전 같으면 만들 이유가 없던 크고 버려도 되는 소프트웨어를 마음껏 주문하라고 했습니다."*(05:52~05:58) 일회용 쪽을 **권고** 로 말한 첫 소스다 — 앞선 소스들은 일회용과 오래 쓰는 것을 가르는 기준을 다뤘다.

[[hackertube|HackerTube]]가 그 실례로 놓인다. 서버 코드는 *"바이브 코딩으로 만든 엉망 진창이라서요."*(07:49~07:51) 공개하지 않았고, 남긴 것은 데이터다 — *"해커 튜브에서 진짜 귀한 건 20년치 댓글에서 걸러낸 영상 목록입니다."*(08:57~09:00) 11-08 절의 *앱은 데이터 위의 포장* 과 같은 결론이 이번에는 비용으로도 받쳐진다: 토큰의 90% 넘게가 데이터 선별에, 앱에는 약 100만 토큰이 들었다. → [[share-data-and-prompt-not-app]]

## 2026-11-20 — 서른 줄과 시스템: 조각 사이의 선 ([[tech-bridge-jonathan-blow-30-years-zero-progress]])

[[jonathan-blow|Jonathan Blow]]의 AI 사용 사례는 스펙트럼의 일회용 끝에 있다 — 엑셀 표에 색을 입히는 Visual Basic 30줄, *"쓰고 버릴 코드였습니다."*(04:20) 오래 사는 쪽이 왜 다른지에 대한 그의 설명은 네 기준과 다른 축이다: 프로그램 조각보다 **조각 사이의 선** 이 더 빨리 늘고(*"프로그램 조각이 셋이면 그 사이에 그을 수 있는 선은 셋, 넷이면 여섯입니다."*(04:28~04:31)), *"이 선은 코드에 적혀 있지 않습니다. 여기를 이렇게 짜면 저기가 어떻게 되는지 그 영향과 제약이 선입니다."*(04:34~04:38) 네 기준의 *의존 관계* 를 프로그램 안쪽으로 접어 넣은 그림으로 읽을 수 있다(위키의 읽기).

해설의 권고는 이 틀의 두 끝에 하나씩이다 — 서른 줄짜리 쓰고 버릴 코드에는 AI를 마음껏, *"오래 살 시스템이라면 조각 사이에 선을 그린 지도는 사람이 주고 있습니다."*(11:52~11:55)[주고=쥐고, 추정] 11-18 Karpathy 편의 *크고 버려도 되는 소프트웨어* 보다 일회용의 범위를 훨씬 좁게 잡는다 — Blow는 *어느 크기를 넘으면 드러난다* 고만 하고 그 크기를 말하지 않는다. ⚠️ 한국어 해설 전달.

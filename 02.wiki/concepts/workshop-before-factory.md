---
title: "공장보다 공방 먼저 (Workshop Before Factory)"
type: concept
category: pattern
tags: [software-factory, workshop, human-attention, craft, understanding, pacing, taste, agents, armin-ronacher]
aliases: [workshop before factory, Build the Workshop Before the Software Factory, 공장보다 공방, 공방 먼저, 공방의 조건 셋]
related: [software-factory, orchestras-not-factories, agent-attention-management, cognitive-debt, compressed-review-surface, taste-vs-judgment, named-human-accountability, verification-bottleneck]
first-seen: tech-bridge-armin-ronacher-workshop-before-software-factory
sources: [tech-bridge-armin-ronacher-workshop-before-software-factory]
created: 2026-11-26
updated: 2026-11-26
---

# 공장보다 공방 먼저 (Workshop Before Factory)

**에이전트로 소프트웨어를 대량으로 찍어내는 공장을 짓기 전에, 한 사람이 그 도구를 잘 쓰는 공방부터 지으라는 주장.** [[armin-ronacher|Armin Ronacher]]가 [[ai-engineer|AI Engineer]] Code Summit 발표 *Build the Workshop Before the Software Factory*(제목은 설명란)에서 내놓았고, 위키에는 한국어 해설 [[tech-bridge-armin-ronacher-workshop-before-software-factory]]로 들어왔다. 첫 슬라이드(내레이션이 옮김): *"모두가 소프트웨어 공장을 지으려 한다. 그런데 자기를 포함한 대부분은 공방에서 이 도구를 잘 쓰는 법 조차 아직 못 배웠다."*(00:38~00:43)

> ⚠️ **해설 전달이다.** Ronacher의 원음은 두 자막 트랙 모두 무캡션(열 곳, 약 4분 4초)이라 본인 인용은 0건이고 아래 인용은 전부 한국어 내레이션이다. 수치는 그 한 사람의 [[pi-coding-agent|Pi]] 세션 기록(n=1)이고 계측 방법은 캡션에 없다. 위키는 원본 발표를 열지 않았다.

## 왜 공방이 먼저인가 — 기계는 빨라지고 사람은 그대로

- 모델 쪽: 같은 하네스에서 *"오퍼스 4.6은 2.4분, 지금의 오퍼스 5.5는 14분입니다. 같은 하네스로 여섯 배 가까이 오래 일합니다."*(02:26~02:32) 하루 에이전트 작업 시간은 여섯 시간에서 마흔세 시간으로 — *"여러 에이전트를 동시에 돌리니 근무 시간에 몇 배가 된 겁니다."*(04:08~04:09)
- 사람 쪽: *"하루에 보내는 프롬프트는 100개에서 190개 사이로 거의 평평합니다."*(03:55~03:59) 저장소는 쌓여도(*"새로 만든 깃 저장소는 3월 24개에서 10월 141개까지 쌓였습니다."*(04:13~04:16)) *"하지만 한 달에 닷새 넘게 손본 프로젝트는 매달 여섯 개에서 열 세 개, 이쪽은 평평합니다."*(04:17~04:21)
- 그래서: *"사람의 주의력은 한정돼 있고 사람을 더 늘릴 수도 없다."*(03:30~03:32) *"완전히 자동화해도 사람이 관심이 떠나면 프로젝트는 멈춥니다."*(04:53~04:55) → [[agent-attention-management]]

공장이 늘리는 것은 시작한 프로젝트의 수이고, 살아남는 프로젝트의 수는 사람의 주의력이 정한다는 것이 이 주장의 뼈대다.

## 공방의 조건 셋

*"이렇게는 아니라고 말하기, 진짜 실력과 에이전트 실력의 구분, 그리고 이해하는 만큼만 척도 내기."*(05:06~05:10) (⚠️ 끝의 *척도 내기* 는 ASR을 판독하지 못했다 — 영어 더빙은 *scaling*, 내레이션은 뒤에서 *속도를 조절* · *이해하는 만큼만 달리기* 로 받는다.)

| 조건 | 내레이션에 남은 것 | 무캡션이라 모르는 것 |
|---|---|---|
| ① 이렇게는 아니라고 말하기 | *"에이전트는 목표를 끝내면 보상을 받도록 훈련됩니다."*(05:12~05:14) 그 끝이 *"기능은 다 있는데 하나로 어울리지 않는 소프트웨어."*(05:50~05:51) — *"테스트는 통과해도 이렇게는 아니라고 말해 줄 사람이 필요합니다."*(05:53~05:55) | 보상 훈련에서 *심슨 자동차* 까지 가는 설명(05:17~05:44) |
| ② 진짜 실력과 에이전트 실력의 구분 | *"같은 시스템으로 프롬프트를 넣는데 결과가 다르답니다. 차이를 만드는 건 도구가 아니라 쓰는 사람의 실력이라는 겁니다."*(06:28~06:33) 회의에서 *"중요한 자리에서 다들 질문을 에이전트에게 돌리고 정작 자기 시스템이 뭘 하는지는 모르는 장면입니다."*(06:36~06:42) | 조건의 도입(05:58~06:28) |
| ③ 이해하는 만큼만 | *"셋째 조건은 내가 이해하는 범위 안에서 일하도록 속도를 조절하라는 겁니다."*(06:43~06:47) 장치: *"작업의 70% 쯤 검증으로 넘어가기 직전에 끼어드는 겁니다. 코드를 한 줄씩 읽는 대신 요약을 읽고 방향을 판단합니다."*(07:25~07:31) | 그 방법의 설명(06:56~07:25) — 요약을 누가 어떻게 만드는지 |

## 공방에서 참을 것 · 힘을 쓸 곳

- **참을 것 — 제멋대로 자라는 구현.** 뭐든 직접 만들 수 있게 됐지만 *"이제 에이전트로 어떤 형식이든 구현할 수 있지만 구현이 늘수록 해석도 갈라집니다."*(07:56~07:59) *"표준이 어려운 건 기술이 아니라 사람끼리 합의하는 일이기 때문입니다."*(08:24~08:26) → [[standards-as-market-makers]]
- **쓸 곳 — 탁월함.** *"검증된 소프트웨어, 더 빠른 소프트웨어, 메모리 안전한 언어로 쓰는 소프트웨어."*(08:41~08:44) 비유는 예술가와 CNC — *"더 많이가 아니라 더 높은 품질로."*(01:03)

## 위키의 다른 페이지와

- [[software-factory]] — 이 페이지는 공장의 반대말이 아니라 **선행 조건** 이다. 발표는 공장을 짓지 말라고 하지 않고 순서를 말한다.
- [[orchestras-not-factories]] — 공장 은유 자체를 바꾸자는 쪽. 이쪽은 은유는 두고 규모를 줄인다.
- [[tech-bridge-thariq-shihipar-human-folder-unacceptable]] — *산업 혁명이면서 르네상스* 라는 병치. Ronacher의 *더 많이가 아니라 더 야심찬 작품* 은 그 르네상스 쪽과 같은 방향이다.
- [[cognitive-debt]] · [[named-human-accountability]] — 조건 ③의 뿌리. 같은 사람이 엿새 전 편에서 *사람은 기계가 낸 결과를 이해할 수 있어야 한다* 고 했다([[tech-bridge-zechner-ronacher-verification-is-overrated]]).
- [[compressed-review-surface]] — 조건 ③의 장치(코드 대신 요약)는 리뷰 면을 줄이는 또 하나의 방법이다.
- [[taste-vs-judgment]] — 조건 ①은 테스트가 잡지 못하는 *어울림* 의 판단을 사람에게 남긴다.

## ⚠️ 유보

- 한 사람의 자기 계측이고 한 편의 해설 전달이다. *친구들에게 물어봐도 다들 비슷했다* 는 것 말고는 다른 사람의 자료가 없다.
- 세 조건의 논증은 대부분 무캡션 구간에 있다. 이 페이지는 내레이션이 남긴 결론만 담는다.
- *공방* 이 무엇인지 — 한 사람의 작업 방식인지 팀의 단위인지 — 는 캡션으로 정해지지 않는다.

## References

- [[tech-bridge-armin-ronacher-workshop-before-software-factory]] · [[armin-ronacher]] · [[pi-coding-agent]] · [[software-factory]]

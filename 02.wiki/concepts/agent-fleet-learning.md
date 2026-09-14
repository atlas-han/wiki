---
title: 에이전트 함대 학습 (Agent Fleet Learning)
type: concept
category: theory
tags: [network-effects, multi-agent, privacy, product-strategy, adoption]
aliases: [fleet learning, 함대 학습, 에이전트의 네트워크 효과]
related: [agent-collaboration-as-search, multiplayer-agent-context, agent-org-adoption, personal-superintelligence, skill-self-improvement]
first-seen: tech-bridge-zuckerberg-muse-personal-agent
sources: [tech-bridge-zuckerberg-muse-personal-agent]
created: 2026-09-14
updated: 2026-09-14
---

# 에이전트 함대 학습

**개별 에이전트가 같은 제공자의 다른 에이전트들(함대)로부터 익명화된 통찰을 배우게 해서, 에이전트 제품에 네트워크 효과를 만든다는 전략.**

> **[진행자] 에이전트를 위한 **네트워크 효과 학습**을 도입하는 거군요 — **아무도 정말로 해 본 적 없는** — 에이전트가 함대의 나머지로부터 **익명화된 통찰**을 배우는.**
>
> **네. 지금 업계 대부분은 에이전트를 **싱글 플레이어 게임**처럼 생각합니다.** (…) **내부적으로는 이미 사람들의 에이전트가 서로 상호작용하는 흥미로운 사례가 많습니다. 이번 릴리스에서는 대부분 나가지 않지만, 시간이 지나면 중요한 부분이 될 겁니다. **Muse를 쓰는 사람이 늘수록 그냥 더 좋아집니다.**** — [[tech-bridge-zuckerberg-muse-personal-agent]] (28:05~28:57)

⚠️ **프레이밍("네트워크 효과 학습", "함대")은 진행자가 먼저 꺼냈고 화자가 받았다.** → [[alex-heath]]

## 제품 표면 — "아이디어와 제안"

추상이 아니라 이미 출시된 기능에 걸려 있다.

> **앱을 열면 메인 탭은 Muse와의 채팅**이고, **당신이 말한 것들로부터 어떻게 확장할 수 있는지 아이디어를 보여 주는 탭**이 있습니다. (26:56~27:11)

화자 본인의 예 — 문명 전략 가이드를 **역사 수업으로 확장하자는 아이디어를 Muse가 냈다.** MMA 코칭에 대해서도 *"보내 드릴 프레임을 더 잘 찾도록 개선할까요?"* 라고 **스스로 제안한다.**

> **아이디어가 중요한 건, **함대 전체에서 서로 다른 것에 관심 있는 사람들을 찾을 수 있기 때문**입니다.** (27:38~27:44)

## 왜 이 전략인가 — 도입 문제를 푼다

> **AI의 큰 문제 하나는 **많은 사람이 그걸로 뭘 해야 할지 모른다는 것**입니다. 에이전트 스스로가 도움이 될 만한 걸 제안해 줄 수 있다면 그 문제의 큰 부분이 풀립니다.** (27:46~28:04)

→ [[agent-org-adoption]]

**이 위키가 모은 도입 처방 중 유일하게 "사용자가 배우지 않아도 되는" 답이다.** [[tech-bridge-figma-coding-agents|Figma]]는 챔피언과 교육으로, [[tech-bridge-ai-native-skills]]는 스킬 레지스트리로, [[tech-bridge-multimodal-commerce-agent]]는 [[fuzzy-intent-discovery|의도 발견 대화]]로 풀었다. **여기서는 제안이 집계에서 나온다.**

## 이 위키의 다중 에이전트 축에서

| 소스 | 누가 누구와 만나는가 |
|---|---|
| [[tech-bridge-agent-to-agent-as-search]] (09-09, [[town]]) | **다른 조직의 에이전트** — 신뢰 경계·영구 오염 위험 → [[agent-collaboration-as-search]] |
| [[tech-bridge-grokbot-agent-teams]] (08-31, [[grokbot]]) | **한 사람의 봇 팀** — 코디네이터 봇 |
| **함대 학습** | **같은 제공자의 모든 사용자 에이전트** — 집계 학습 |

**세 번째는 앞의 둘과 위험 구조가 다르다.** Town의 문제는 *상대를 믿을 수 있는가* 였고, 여기서는 **제공자가 집계한다** — 상대를 믿는 문제가 **제공자를 믿는 문제**로 바뀐다.

## 열려 있는 것 — 가장 큰 빈자리

- ⚠️ **"익명화"가 무엇인지 전혀 없다.** 집계 방식, 옵트아웃, 개인 데이터와의 경계, 차분 프라이버시 같은 기법 여부 — 하나도 없다.
- ⚠️ **[[confidential-vm|기밀 VM]]과 같은 대담 안에 있는데 둘이 연결되지 않는다.** *"Meta조차 VM 안을 볼 수 없다"* 와 *"함대에서 익명화된 통찰을 배운다"* 가 **어떻게 양립하는지** 소스가 설명하지 않는다. **이 위키가 이 소스에서 발견한 가장 큰 미해결 긴장이다.**
- ⚠️ **효과 수치가 없다.** *"쓰는 사람이 늘수록 좋아진다"* 에 근거가 없다.
- ⚠️ **"아무도 안 하고 있다"** 에 비교 대상이 없다.
- ⚠️ **[[personal-superintelligence]]와의 긴장.** *각자가 방향을 정한다* 는 테제와 *에이전트가 제안한다* 는 처방 사이에서, 제안의 분포가 곧 방향의 분포가 될 수 있다. 소스는 다루지 않는다.

## References

- [[tech-bridge-zuckerberg-muse-personal-agent]] · [[muse]] · [[meta]] · [[alex-heath]]
- 관련: [[agent-collaboration-as-search]] · [[multiplayer-agent-context]] · [[agent-org-adoption]] · [[personal-superintelligence]] · [[confidential-vm]] · [[skill-self-improvement]] · [[town]] · [[grokbot]]

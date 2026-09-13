---
title: 기능 지도 (Feature Map)
type: concept
category: technique
tags: [context, navigation, bug-reports, ui, skills, agents]
aliases: [feature map, 기능 맵]
related: [agent-verification-skill, agent-knowledge-sourcing, context-engineering, intent-md, agent-skills, fuzzy-intent-discovery]
first-seen: tech-bridge-lauren-tan-trusting-agents
sources: [tech-bridge-lauren-tan-trusting-agents]
created: 2026-09-13
updated: 2026-09-13
---

# 기능 지도

**에이전트에게 "이 앱에 어떤 기능이 있고 각각에 어떻게 도달하는지"를 알려 주는 파일.** [[lauren-tan]]이 [[tech-bridge-lauren-tan-trusting-agents]]에서 [[agent-verification-skill|검증 스킬]]에 딸린 *"아주 독특한 파일"* 로 소개했다.

## 왜 생겼는가

검증 스킬만으로는 부족했던 지점이 이 개념의 출발이다.

> 스킬을 만들어서 **에이전트가 agent window를 실제로 띄우고 트레이스를 뜰 수 있게 됐는데, 에이전트는 agent window가 무엇인지를 전혀 몰랐습니다.**

> 누가 *"왼쪽 사이드바가 버벅인다"* 거나 *"오른쪽 PR 탭이 안 된다"* 고 하면 **에이전트는 허둥댑니다.** (…) **사실상 완전히 쓸모가 없었습니다.**

**앱을 조작할 능력과 앱을 이해할 지식은 별개**라는 것 — 이것이 이 위키에 새로 들어오는 구분이다.

## 무엇이 들어 있는가

- 각 기능이 무엇인지와 **하위 기능들**
- **사용자 관점의 경로** — 거기에 어떻게 도달하는가
- **키보드 단축키**
- **CDP로 요소를 선택할 때 쓰는 DOM 속성**

즉 **사용자 층(무엇)과 자동화 층(어떻게 집는가)을 한 파일에 겹쳐 둔다.**

## 효과 — 제보 품질의 하한을 낮춘다

가장 실용적인 귀결이다.

> 누가 **스크린샷 하나 던지고 "???" 만 적어 놓는** 식이죠. (…) **feature map 없이는 에이전트가 전혀 감이 없습니다.** 있으면 **훨씬 많은 맥락과 이해**를 갖고 **어떻게 내비게이트할지** 압니다.

**모호한 제보를 작업으로 바꾸는 장치**다. → [[fuzzy-intent-discovery]]와 같은 문제([[google-deepmind]]의 *articulation gap*)에 대한 다른 처방 — 그쪽은 **사람에게 되묻고**, 이쪽은 **되묻지 않고 맵으로 메운다.**

## 유지

[[pstack|Pstack]]의 `create verification skill`이 **코드를 탐색해 초기 맵을 만들고**, `maintain verification skill`이 갱신을 맡는다. 제품이 바뀌면 맵도 낡기 때문이다.

## 위키의 다른 페이지와 맞닿는 자리

- **[[intent-md]]** · **[[agent-knowledge-sourcing]]** — 코드베이스 바깥의 지식을 파일로 두는 같은 계열. feature map은 그중 **UI 도달 경로**라는 특정 축이다.
- **[[context-engineering]]** — 무엇을 미리 재료로 넣어 둘지의 사례. 탐색으로 매번 찾게 두지 않고 **한 번 만들어 유지**한다.
- **[[code-knowledge-graph]]** — 코드 구조의 지도가 있다면, 이쪽은 **사용자 표면의 지도**다. 둘이 같지 않다는 것이 요점이다.

## 표시해 둔 것

> ⚠️ 형식·크기·갱신 주기가 소스에 없다. 자동 생성된 초기 맵의 **정확도**도 서술되지 않는다.

## References

- [[tech-bridge-lauren-tan-trusting-agents]] · [[agent-verification-skill]] · [[pstack]] · [[context-engineering]] · [[agent-knowledge-sourcing]] · [[lauren-tan]]

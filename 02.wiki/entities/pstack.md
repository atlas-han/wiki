---
title: Pstack
type: entity
category: tool
tags: [cursor, plugin, skills, verification, evals, lauren-tan]
sources: [tech-bridge-lauren-tan-trusting-agents]
created: 2026-09-13
updated: 2026-09-13
---

# Pstack

[[lauren-tan|Lauren Tan]]이 만든 **[[cursor|Cursor]] 플러그인** — 자기 엔지니어링 관행을 스킬로 묶은 것. 본 위키 첫 등장은 [[tech-bridge-lauren-tan-trusting-agents]].

## 이름

**P는 potato** — 화자의 트위터 핸들 `poteto`에서 온다. **Y Combinator CEO Gary Tan의 `GStack`(Gary Stack)** 을 살짝 놀리며 만든 자기 버전이고, *"공교롭게 성이 같은데 아무 관계도 없다"* 는 농담이 붙는다.

> ⚠️ **ko 자막이 이 대목을 두 번 망가뜨린다** — Gary **Tan** 의 성을 *"스택"* 으로 바꿔 성이 같다는 전제를 지우고, 화자가 자기 도구를 **`GStack`이라 지었다**고 뒤집는다. **자기 도구의 이름은 Pstack이다.**

## 들어 있는 것 (소스에서 언급된 것만)

| 항목 | 내용 |
|---|---|
| **`create verification skill`** | 코드를 탐색해 **초기 [[feature-map]]** 을 포함한 검증 스킬 세트를 세팅해 준다 |
| **`maintain verification skill`** | 그 맵과 스킬을 **최신으로 유지** |
| **`control glass` 스킬** | 화자가 만든 첫 스킬 중 하나(glass = agents window의 사내 코드명). CDP·시뮬레이터로 앱을 띄우고 트레이스를 뜬다 |
| **`how` 스킬** | 에이전트 관찰에서 나온 두 번째 스킬 (ko 자막은 이름을 *"방법"* 으로 번역해 버린다) |
| **`potato mode`의 `eval playbook`** | **눈가림 서브에이전트 eval** 절차 → [[skill-evals]] |

## 만들어진 방식

> 저는 **Pstack을 만들려고 시작한 적이 전혀 없습니다.** 그냥 스킬 몇 개로 시작한 거죠. (…) **에이전트의 온갖 실패 모드를 정말로 관찰**하는 것에서 시작해서, **볼 때마다 "이건 스킬로 만들자"** 했습니다.

→ [[skill-self-improvement]] · [[agent-skills]]

## 화자 본인의 유보

> **저를 믿고 Pstack을 믿으면 연장선에서 에이전트를 믿을 수 있겠지만, 저를 안 믿으신다면 — 그리고 저를 맹목적으로 믿으시라고 권하지 않습니다 — 직접 스킬 세트를 만드시면 됩니다.** **포크해서 자기 것으로 만들고 개선하는 것도 적극 권합니다.**

> ⚠️ 접근 경로는 *"구글에 'Pstack cursor'로 검색하면 나온다"* 가 전부다. **라이선스·배포 형태·버전은 소스에 없다.**

## References

- [[tech-bridge-lauren-tan-trusting-agents]] · [[lauren-tan]] · [[cursor]] · [[feature-map]] · [[skill-evals]] · [[agent-verification-skill]] · [[agent-skills]]

---
title: Design Handoff Friction
type: concept
category: pattern
tags: [design, handoff, pixel-perfect, mcp, workflow, figma]
related: [design-system-as-agent-context, multiplayer-agent-context, goal-level-delegation, model-context-protocol, brain-hands-decoupling]
first-seen: tech-bridge-one-designer-plus-ai
sources: [tech-bridge-one-designer-plus-ai]
created: 2026-09-15
updated: 2026-09-15
---

# Design Handoff Friction

**디자이너와 개발자 사이의 왕복이 디자인 조직의 진짜 병목이었고, 에이전트가 그 왕복의 한쪽 끝을 대체하면 이전에 불가능하던 일이 가능해진다.**

[[tech-bridge-one-designer-plus-ai]]의 진단:

> **예전에는 이게 불가능했습니다. 디자이너와 개발자 사이의 마찰이 너무 컸거든요.** 디자인을 넘기면 픽셀 퍼펙트하게 안 나오고, **그러면 피드백 루프가 엄청났습니다.** (08:11~08:41)

## 마찰을 없앤 세 가지

| 수단 | 하는 일 |
|---|---|
| **자연어 요청** | *"이거 더 정확하게 해 줄 수 있어?"* — 왕복이 대화가 된다 |
| **[[model-context-protocol\|MCP]] 연결** | 디자인 원본에 직접 접근 |
| **스펙 시트** | Figma 플러그인(무료), **PDF에 주석** — 간격·폰트 크기·색상을 명시 |

## 비대칭이 생긴 자리

사람 사이의 핸드오프에서 치명적이던 게으름이 **모델 상대로는 비용이 아니다.**

> **디자이너들은 레이어 이름을 안 짓죠. `frame three`, `frame four` 같은 게 널려 있는데 LLM은 알아듣습니다.** (11:09~11:21)

**대신 수치는 명시해야 한다.** 즉 요구사항이 *이름 붙이기(사람을 위한 서술)* 에서 *치수 명시(기계를 위한 값)* 로 옮겨간다. [[design-system-as-agent-context]]가 그 치수를 미리 못 박아 두는 쪽이라면, 스펙 시트는 **개별 산출물마다 붙이는 주석**이다.

## 워크플로가 도구의 거처를 따라간다

화자는 *"리서치 → 제품 → 피드백 루프"* 라는 디자인 씽킹을 *"저한테는 그냥 낡았다"* 고 말하고, 지금의 경로를 **Slack → Figma → 다시 Slack**이라고 한다. 이유는 아키텍처가 아니라 **거처**다:

> ***"[[devin\|Devin]]이 Slack 안에 살기 때문"*** (10:42~10:44)

[[multiplayer-agent-context]]가 말하던 *에이전트가 어디에 있느냐가 협업 형태를 정한다* 의 디자인 버전이다.

> ⚠️ 마찰이 **없어졌는지 옮겨갔는지** 소스는 묻지 않는다. 픽셀 퍼펙트 판정을 이제 **누가** 하는지(디자이너 본인) → 작성자 = 검증자 문제는 [[agent-visual-qa]]에서 다시 나온다.

## References

- [[tech-bridge-one-designer-plus-ai]] · [[vincent-wendy]] · [[figma]] · [[devin]]

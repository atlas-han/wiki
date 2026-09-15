---
title: Self-Serve Asset Generation
type: concept
category: pattern
tags: [design, scale, delegation, generators, operations]
related: [atomic-design, design-system-as-agent-context, exception-handling-as-the-job, goal-level-delegation, agentic-sites]
first-seen: tech-bridge-one-designer-plus-ai
sources: [tech-bridge-one-designer-plus-ai]
created: 2026-09-15
updated: 2026-09-15
---

# Self-Serve Asset Generation

**디자이너 한 명이 300명을 감당하는 방법은 더 빨리 만드는 것이 아니라, 만드는 일을 넘기는 것이다.**

[[tech-bridge-one-designer-plus-ai]]의 **발표자 공지 그래픽 생성기**:

- **발표자 본인이 직접 만든다** — 고르고, 이름을 바꾸고, 내보낸다.
- 형식이 여럿: **세로 · 가로 · 트레이딩 카드**(*"놀랄 만큼 인기가 좋다"*).
- **헤드샷과 세부 정보가 있으면 자동으로 내보내진다.**
- 전부 **픽셀 퍼펙트** — 품질은 생성기가 보장하고 사용자가 정하지 않는다.

> **발표자가 300명이 넘으니 제가 하나하나 감당하는 건 불가능합니다. 그래서 이걸 만들었습니다.** (09:04~09:14)

## 성립 조건

생성기가 서려면 **원자가 먼저 정의돼 있어야 한다** — [[atomic-design]]·[[design-system-as-agent-context]]. 정의가 없으면 생성기는 **선택지를 열어 줄 수밖에 없고**, 선택지를 열면 **일관성이 깨진다.** 그래서 이 패턴은 *"기초 먼저"* 의 **회수(payoff) 지점**이다.

| | 위임하는 것 | 위임하지 않는 것 |
|---|---|---|
| 발표자 | 이름·사진·형식 선택·내보내기 | **레이아웃·타이포·색·여백** |
| 디자이너 | — | **생성기 자체와 그 안의 모든 결정** |

즉 **위임되는 것은 실행이고, 결정은 여전히 디자이너에게 있다.** [[goal-level-delegation]]이 에이전트에게 하는 구분을 **사람에게** 한 셈이다.

> ⚠️ 접근 범위(발표자만인지 링크만 있으면 누구나인지), 남용 시 처리, 생성기 자체의 유지 비용이 **소스에 없다.** *"여러분도 직접 해 보실 수 있다"* 는 현장 청중을 향한 말이다.

## References

- [[tech-bridge-one-designer-plus-ai]] · [[vincent-wendy]] · [[atomic-design]]

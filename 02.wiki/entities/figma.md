---
title: Figma
type: entity
category: org
tags: [design, engineering, coding-agent]
links:
  - https://www.figma.com/
sources: [tech-bridge-figma-coding-agents, tech-bridge-impeccable-design-steering, tech-bridge-one-designer-plus-ai]
created: 2026-08-29
updated: 2026-09-15
---

# Figma

클라우드 디자인 툴 회사. 본 위키에는 제품의 AI 캔버스보다 **사내 코딩 에이전트 도입** 사례로 먼저 등장한다. [[eyal-blum|Eyal Blum]]의 [[tech-bridge-figma-coding-agents]] 강연이 출처.

## 위키에서 알려진 사실

- 성숙한 엔지니어링 조직에 코딩 에이전트를 넣었을 때의 3막 곡선·검증 우선·기획 전환을 [[agent-org-adoption]]으로 정리.
- 발표 시점에도 자동화는 "아직 다 오지 않았다" — 레거시 의존성 때문에 클라우드 에이전트 범위가 실험 중.
- 본 위키의 Figma 제품(MCP·캔버스 에이전트) 라인은 이 소스가 다루지 않음. 별도 ingest 필요.

## 디자인 도구로서의 Figma (2026-09-12)

[[tech-bridge-impeccable-design-steering]]에서 [[paul-bakaus]]가 Figma를 처음으로 **디자인 도구**로 놓는다 — *"직접 조작(direct manipulation) — 픽셀 공간. Figma에서 마진·패딩을 만지거나 Webflow에서 최종 산출물을 직접 조작하는 것."* 그리고 판정: *"대부분의 작업에서 패딩·마진·간격의 직접 조작은 **고도가 너무 낮다**."* → [[steering-altitude]]

위의 *"Figma 제품 라인은 별도 ingest 필요"* 는 여전하다 — 이 소스도 Figma의 AI 기능을 다루지 않고 **비교 대상**으로만 부른다.


## 2026-09-15 — 디자인 시스템의 거처이자 에이전트의 접점

[[tech-bridge-one-designer-plus-ai]]에서 Figma는 **[[vincent-wendy|Vincent Wendy]]의 "디자인 팀" 구성원**으로 소개된다(*"저와 [[devin|Devin]], GPT, Figma"*). 소스에서 확인되는 쓰임:

- **디자인 시스템의 거처** — 타이포그래피·색상·컴포넌트가 여기 정의되고 웹사이트가 그 안에서 세팅된다 → [[design-system-as-agent-context]]
- **[[model-context-protocol|MCP]] 접점** — 에이전트가 디자인 원본에 접근하는 경로
- **스펙 시트 플러그인** — 무료, **PDF에 주석**을 붙여 간격·폰트 크기·색상을 명시 → [[design-handoff-friction]] (⚠️ **플러그인 이름이 소스에 없다**)
- **벡터화 도구** — 모델이 PNG를 만들면 Figma에서 벡터로 → [[capability-detour]]
- 관찰: *"디자이너들은 레이어 이름을 안 짓는다 — `frame three`, `frame four`. 그런데 LLM은 알아듣는다."*

## References

- [[tech-bridge-figma-coding-agents]] · [[eyal-blum]] · [[agent-org-adoption]]

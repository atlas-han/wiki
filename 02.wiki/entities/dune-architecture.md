---
title: Dune (GrokBot 아키텍처)
type: entity
category: tool
tags: [architecture, electron, react, ci, agents, grokbot, cursor]
sources: [tech-bridge-lauren-tan-trusting-agents]
created: 2026-09-13
updated: 2026-09-13
---

# Dune

[[grokbot|GrokBot]]을 위해 만들어진 아키텍처의 **사내 코드명**. 본 위키 첫 등장은 [[tech-bridge-lauren-tan-trusting-agents]]. 설계 목적이 특이하다 — **에이전트가 코드를 쓰라고 설계됐다.**

> 멘탈 모델은 **"Electron 앱을 위한 Next.js"**. (ko 자막은 *Next.js* 를 *"JavaScript"* 로 풀어 버려 비유가 무너진다.)

## 제약 목록 (소스에서 언급된 것)

| 제약 | 근거 |
|---|---|
| **`useEffect` 금지** | *"React의 가장 큰 함정 중 하나"*. CI가 실패한다 |
| **코드 주석 금지** | *"99%의 경우 에이전트는 코드와 전혀 무관한 역사적 사연을 서술하는 주석을 씁니다"* — 예: *"Lauren이 이건 절대 하지 말라고 했다"* 가 주석에 남는데 **그건 전역 규칙이 아니라 그 PR에 대한 코멘트였다** |
| **feature 단위 디렉터리** | 프레임워크의 명사는 **feature · entry point · transcript card**. 한 feature의 모든 코드가 한 디렉터리에 모여 *"작업의 80%가 캡슐화"* |
| **`electron-main` / `electron-renderer` import 검사** | **의존성 그래프를 CI에서 검사**해 실수로 렌더러 스레드에 무거운 코드가 끌려오지 않게 한다 |

렌더러 제약의 근거는 수치로 제시된다 — **60fps면 프레임당 16ms**, 계산이 무겁거나 IO가 많은 코드가 렌더러로 들어오면 **long task와 jank**가 생긴다. Cursor의 agents window가 겪는 실제 문제이고, *"머지되는 pull request가 너무 많아 그중 어느 하나가 성능을 회귀시킬 수 있다"* 는 것이 하드 강제의 이유다.

## 설계 원칙

> **가장 짧은 경로가 가장 좋은 경로입니다.** (…) **에이전트는 지름길을 좋아하고 문제를 푸는 가장 빠른 길을 찾습니다. 그렇다면 그것을 문제를 푸는 가장 좋은 길로 만들면 되지 않겠습니까?**

그리고 대상이 명시된다 — *"가장 멍청한 에이전트를 위해 설계된 겁니다. 생각할 필요가 없어야 하죠."* → [[shortest-path-architecture]]

## 주장된 효과

- **PR 600건 이상**을 들여 GrokBot 전체를 이 아키텍처로 리팩터링했다(자기 보고).
- *"이제 저는 코드를 정말 거의 안 봅니다."*
- **비엔지니어의 기여** — PM·디자이너가 직접 기능을 내보내고, 화자는 리뷰만 한다: *"아주 엄격한 제약이 엔지니어링 전문가가 아닌 사람도 높은 수준으로 기여하게 해 준다."*
- agents window에는 **아직 적용되지 않았고** 화자가 옮길 계획이라고 말한다.

> ⚠️ **오픈소스가 아니다.** *"아이디어와 원칙의 모음"* 이고 제공 방식은 *"이 화면을 스크린샷 찍어서 에이전트에게 만들어 달라 하라"* 뿐이다. **외부에서 검증할 수 없고, 효과 수치는 전부 자기 보고다.** 주석 금지의 대가(왜 그 코드가 그런지의 지식이 어디 남는가)와 `useEffect` 금지의 대안은 소스에 없다.

## References

- [[tech-bridge-lauren-tan-trusting-agents]] · [[grokbot]] · [[lauren-tan]] · [[shortest-path-architecture]] · [[hard-vs-soft-enforcement]] · [[llm-coding-guidelines]] · [[organic-architecture]]

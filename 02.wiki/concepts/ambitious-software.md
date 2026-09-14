---
title: 대담한 소프트웨어 (Ambitious Software)
type: concept
category: framing
tags: [software-taxonomy, quality, maintenance, release, code-quality]
aliases: [야심찬 소프트웨어, 소프트웨어의 종류]
related: [code-is-the-product, architecture-as-remaining-art, system-level-quality, slop-cannon, decision-quality]
first-seen: tech-bridge-ambitious-software-agent-era
sources: [tech-bridge-ambitious-software-agent-era]
created: 2026-09-14
updated: 2026-09-14
---

# 대담한 소프트웨어

**에이전트 도입 논의가 "어떤 소프트웨어를 만드느냐"에 따라 갈린다**는 주장. [[jonathan-kelley|Jonathan Kelley]]가 발표 본론에 들어가기 전에 **먼저 범주를 나눈다.**

> **무엇이 대담한 소프트웨어 프로젝트인지부터 말하는 게 중요합니다. 세상에는 여러 종류의 소프트웨어가 있고, 매일 무엇을 배포하느냐에 달려 있습니다.** (07:52~08:04)

| 종류 | 무엇이 중요한가 |
|---|---|
| **연구** | *"코드 품질이 가장 중요한 게 아닐 수 있습니다"* |
| **프로토타입** | *"빠르게 반복하고, **빨리 움직이는 게 중요**합니다"* |
| **내부가 보이지 않는 애플리케이션** | *"사람들이 내부 코드를 보지 않습니다. 바깥에서 어떻게 보이는지만 봅니다"* |
| **대담한 소프트웨어** | 아래 |

## 대담한 소프트웨어의 조건

> **우리가 신경 쓰는 건 몇 가지 다른 것입니다. 첫째로, 코드가 항상 작동하고 깨지면 쉽게 고칠 수 있기를 바랍니다.** 요즘 사람들이 충분히 생각하지 않는 게 이거라고 봅니다 — **계속해서 유지보수하기 쉬운 코드를 만들어야 한다는 것.** (08:21~08:40)

> **여러분이 배포하는 속도는 여러분이 깔아 둔 기반(substrate) 위에 얹히고, 기반이 좋지 않으면 그 위에 무엇을 만들어도 좋을 수 없습니다.** (08:40~08:48)

> **패치 릴리스에서 수백만 명이 의존하는 API를 깨뜨리면 안 됩니다. 사람들이 사업을 얹는 프로젝트이므로 릴리스 기준도 높습니다.** 문서·예제·테스트·벤치마크의 **높은 품질을 유지해야 합니다. 뭔가 어긋나면 사람들이 금방 알아냅니다.** (09:15~09:41)

정리하면 네 가지다 — **① 장기 유지보수 가능성 · ② 기반(substrate)의 품질 · ③ 하위 호환 · ④ 주변 자산(문서·예제·테스트·벤치마크)의 품질.**

## 왜 이 구분이 필요한가

**에이전트 도입의 성패 사례가 서로 모순되어 보이는 이유를 설명한다.**

이 위키가 모은 성공 사례는 대부분 앞의 세 범주에 있다 — [[tech-bridge-figma-coding-agents|Figma]]·[[tech-bridge-frontier-engineering|Amazon]]의 사내 도구, [[tech-bridge-agentic-sites|Adobe]]의 생성 사이트, [[tech-bridge-cursor-legacy-refactoring|레거시 마이그레이션]]. **[[slop-cannon|슬롭 캐논]]은 네 번째 범주에서 일어났다.**

**같은 도구, 같은 팀, 다른 기준.** 그래서 이 개념은 **도입 논쟁의 전제를 먼저 맞추라는 요구**로 읽힌다.

## 이 위키의 다른 범주 축과의 관계

- [[task-entropy-matrix]] (09-12) — **작업 단위**로 에이전트 적합성을 가른다.
- [[greenfield-vs-brownfield-agent-risk]] (09-12) — **코드베이스의 나이**로 가른다.
- **이 개념** — **소프트웨어의 종류(누가 무엇을 보는가)** 로 가른다.

**셋이 겹치지 않는 세 축이다.** 이 축의 특징은 **조직이 바꿀 수 없다는 것** — 프레임워크를 만드는 팀이 내일 프로토타입 팀이 되지 않는다.

## 소스가 닫지 않은 것

- ⚠️ **범주 사이의 경계가 없다.** 사내 플랫폼 팀처럼 **내부 사용자가 코드를 읽는** 경우는 어디에 속하는지 논의되지 않는다.
- ⚠️ **네 조건의 우선순위가 없다.** 충돌할 때(빠른 하위 호환 깨기 vs 유지보수성) 무엇이 이기는지 제시되지 않는다.

## References

- [[tech-bridge-ambitious-software-agent-era]] · [[jonathan-kelley]] · [[dioxus]]
- 관련: [[code-is-the-product]] · [[architecture-as-remaining-art]] · [[slop-cannon]] · [[task-entropy-matrix]] · [[greenfield-vs-brownfield-agent-risk]] · [[system-level-quality]]

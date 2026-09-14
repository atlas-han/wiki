---
title: Rust
type: entity
category: tool
tags: [language, systems, type-system, borrow-checker, coding-agents]
sources: [tech-bridge-ambitious-software-agent-era]
created: 2026-09-14
updated: 2026-09-14
---

# Rust

시스템 프로그래밍 언어. 이 위키에는 오래전부터 **다른 페이지의 배경**으로 있었지만([[actix-web]]·[[tokio]]·[[serde]]·[[bun]]의 Zig→Rust 재작성·[[goose]]의 MCP Rust SDK), **언어 자체가 논점이 된 첫 소스는 [[tech-bridge-ambitious-software-agent-era]]** 다.

## 2021년의 선택 근거 ([[jonathan-kelley]] 진술)

> **2021년 당시 Rust는 여전히 틈새 언어**였지만 생태계는 자라고 있었고 툴링도 나아지고 있었으며, **네이티브 성능 · 견고한 타입 시스템 · 간단한 크로스 컴파일**이라는 셋이 저를 완전히 사로잡았습니다.

## 이 위키의 논점 — 어려움의 부호가 바뀌었다

Rust의 대표적 진입 장벽은 **빌림 검사기(borrow checker)** 와 타입 시스템이다. [[tech-bridge-ambitious-software-agent-era]]의 주장은 **그 장벽이 에이전트 시대에 자산이 된다**는 것이다.

> **Rust는 쓰기가 더 어렵기 때문에** — 다행히도 — **코딩 에이전트가 개발의 부담을 대신 져 줍니다. 예외 상황을 처리하고, 빌림 검사기와 싸워 주며, Rust 앱을 쓰는 인지 부담에서 여러분을 구해 줍니다. 우리가 줄이려고 싸웠던 그 학습 곡선이 이제는 기능이 되었습니다.**

→ [[learning-curve-as-feature]]

**강제의 층이 CI가 아니라 컴파일러**라는 점에서 이 위키의 [[verifiable-goals]]·[[hard-vs-soft-enforcement]]와 같은 계열이고, **가장 강한 형태**다 — 09-12 [[tech-bridge-lauren-tan-trusting-agents|Lauren Tan]]이 *"PR에 댓글로 강제하고 있다면 코드 스멜"* 이라며 린트와 CI로 내렸던 것을, 여기서는 **타입 시스템이 이미 하고 있다.**

전제 하나가 붙는다 — **컴파일러가 빨리 답해야 한다.** 그래서 같은 팀이 [[subsecond|Subsecond]](100ms 핫 리로드)를 만들었다고 읽을 수 있다.

> ⚠️ **경계가 그어지지 않았다.** 컴파일러가 잡지 못하는 결함(설계 오류·잘못된 추상·성능 회귀)에는 같은 논리가 성립하지 않는데 소스는 그 경계를 논의하지 않는다.

## 소스가 말하는 부수 효과

- **모든 Rust 프로젝트가 서로 닮아서** 개발자가 새 프로젝트에 뛰어들기 쉽다.
- *"코딩 에이전트가 **Rust를 정말 잘하게 됐다**"* — 화자가 지목한 **지난 6개월의 변화**.

> ⚠️ *"Rust를 정말 잘하게 됐다"* 에 벤치마크나 근거가 없다. 자기 관찰이다.

## 자막 주의

*borrow checker* 가 ko 자막에서 **"빌림 검사기"**, 같은 영상 설명란에서 **"대여 검사기"** 로 **서로 다르게** 옮겨진다. 검색 시 참고.

## References

- [[tech-bridge-ambitious-software-agent-era]] · [[dioxus]] · [[jonathan-kelley]] · [[blitz]] · [[subsecond]]
- 개념: [[learning-curve-as-feature]] · [[verifiable-goals]] · [[hard-vs-soft-enforcement]]
- 생태계 관련: [[actix-web]] · [[tokio]] · [[serde]] · [[bun]] · [[goose]]

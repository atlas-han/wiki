---
title: Rust
type: entity
category: tool
tags: [language, systems, type-system, borrow-checker, coding-agents]
sources: [tech-bridge-ambitious-software-agent-era, tech-bridge-theo-coding-is-gardening, tech-bridge-claude-fable-5-2-announcement, tech-bridge-katelyn-lesse-anthropic-engineers-barely-read-code]
created: 2026-09-14
updated: 2026-11-28
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

## 같은 결론, 다른 이유 — Theo의 TypeScript → Rust (2026-11-11 · [[tech-bridge-theo-coding-is-gardening]])

[[theo|Theo]]는 세 명짜리 팀을 *"조금 더 빠르게 하려고 타입스크립트를 러스트로 다쓰고 있습니다."*(03:28~03:30)[=다시 쓰고] Twitch 시절엔 600~800명이 쓰는 도구라도 다시 쓰는 건 본전이 안 맞았다(해설 전달). 바뀐 계산의 이유는 이 페이지의 *학습 곡선이 자산* 이 아니라 **마찰**이다 — *"마찰은 사람보다 에이전트를 훨씬 세게 막습니다."*(03:34~03:36) → [[agent-friction-multiplier]](신규)

[[fable-5-2|Fable 5.2]] 발표문(해설 전달, [[tech-bridge-claude-fable-5-2-announcement]])에도 Python 핵심 서비스를 Rust로 옮겨 시작 속도가 약 26배 빨라진 사례가 있다(04:20~04:25). ⚠️ 두 소스 모두 재작성의 **품질 · 버그**는 말하지 않는다.

## 2026-11-28 — 써 본 사람이 거의 없는 팀이 Rust를 고른 이유 ([[tech-bridge-katelyn-lesse-anthropic-engineers-barely-read-code]])

[[anthropic|Anthropic]]이 메시지 API의 핵심 층을 Python에서 Rust로 옮긴 사례([[katelyn-lesse|Katelyn Lesse]] 인터뷰의 한국어 해설, 내레이션 전달).

- 출발은 성능이 아니라 **CPU 부족** 이다: *"결국 한 엔지니어가 말을 꺼냈습니다. 완전히 다른 걸 해 보자고. 러스트를 써 보자고요."*(01:18~01:21)
- 사람 쪽 조건은 불리했다: *"그런데 팀에는 러스트를 많이 써 본 사람이 거의 없었습니다."*(01:23~01:24) 그 전의 절충은 Go였다 — *"사실 엔트로픽은 작년부터 새 서비스를 고 언어로 만들고 있었습니다. 효율과 개발 경험 사이의 절충이었습니다."*(01:24~01:30) *"그때는 모델이 언어 차이를 다 메워 줄 만큼은 아니어서 사람이 다루기 편한 언어가 여전히 중요했습니다."*(01:32~01:36)
- 바뀐 것: *"그런데 올해 모델이 좋아지면서 계산이 바뀌었습니다. 구현 세부는 모델이 더 맡을 수 있게 됐으니까요."*(01:38~01:41)
- **컴파일 시점 검사가 에이전트 코드의 신뢰 근거가 된다**: *"컴파일할 때 잡아내는 검사가 아주 많습니다. 사람이 손으로 짤 때는 이게 답답한 장벽이었지만 에이전트가 짤 때는 오히려 믿을 근거가 됩니다."*(01:49~01:57)
- 엔지니어의 Rust 이해: *"케이틀린은 75대 25라고 답합니다. 75는 모델이 짜고 문법은 몰라도 되는 부분, 25는 궁금해서 모델에게 물어보며 배우는 부분입니다."*(02:06~02:14) *"클로드가 코드를 짜주는 게 절반, 무슨 코드인지 가르쳐 주는 게 나머지 절반이라고 했습니다."*(02:15~02:19)
- 결과로 불린 수치: *"파이썬으로 된 핵심 층을 러스트로 옮기는 데 걸린 시간은 다섯에서 여섯 달. 핵심 팀은 몇 명 뿐이었습니다."*(00:10~00:14) *"CPU 사용량은 평균 1/3 정도로 줄었습니다."*(06:13~06:15) ⚠️ 1/3이 무엇의 CPU인지, 앞 문맥이 무캡션이라 이 재작성의 결과라고 단정할 수 없다.

[[tech-bridge-ambitious-software-agent-era]]가 Rust를 *대담한 소프트웨어* 의 언어로 읽은 것과 같은 방향의 근거가 운영 사례로 붙었다 — 사람이 다루기 편한가보다 **기계가 검증해 주는가** 가 언어 선택의 기준으로 올라온다. ⚠️ 사례 하나, 자기 보고. → [[shadow-traffic-verification]]

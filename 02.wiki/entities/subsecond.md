---
title: Subsecond
type: entity
category: tool
tags: [rust, c, cpp, hot-reload, wasm, dioxus, developer-experience]
sources: [tech-bridge-ambitious-software-agent-era]
created: 2026-09-14
updated: 2026-09-14
---

# Subsecond

[[dioxus|Dioxus]] 팀이 만든 **범용 핫 리로드 엔진**. 본 위키 첫 등장은 [[tech-bridge-ambitious-software-agent-era]].

## 동작 (소스에서 확인되는 것)

> **코드 편집을 감시하고, 바뀐 부분만 재컴파일하고, 실행 중인 앱을 제자리에서 패치하는 일을 100밀리초 안에** 끝냅니다. (04:30~04:38)

| 항목 | 값 |
|---|---|
| **대상 언어** | **Rust · C · C++** |
| **왕복 시간** | **100ms** |
| **플랫폼** | *"모든 주요 운영 체제"* + **웹(WebAssembly로 컴파일)** |
| **주장** | *"네이티브 컴파일 코드에 대해 **이만큼 넓은 언어·런타임 지원을 가진 유일한 핫 리로드 엔진**"*, *"지금까지 아무도 이걸 해낸 적이 없다"* |

> ⚠️ **유일성 주장에 근거가 없다.** 비교 대상이 열거되지 않고 100ms의 측정 조건도 없다. **자기 보고다.**
>
> ⚠️ **ko 자막이 이 대목의 주어를 바꿔 놓았다** — *"(Subsecond는) 모든 주요 OS에서 작동하고 웹조차 WebAssembly로 컴파일되어 지원된다"* 가 ko에서는 *"웹 어셈블리는 모든 주요 운영 체제에서 작동하며…"* 가 되어 **지원 범위 주장이 흐려진다.**

## 왜 이 위키에 있는가

**에이전트 시대의 개발자 경험 논의에서 "반복 주기(iteration loop)의 길이"가 처음 구체적인 값으로 나온 자리**다. 이 위키의 [[harness-engineering]]·[[verification-bottleneck]]은 *에이전트가 자기 작업을 확인하는 루프* 를 다뤄 왔는데, Subsecond는 **네이티브 컴파일 언어에서 그 루프를 100ms로 줄이려는 시도**다 — [[learning-curve-as-feature]]가 성립하려면 **컴파일러가 빨리 답해야 한다**는 조건과 직접 맞물린다.

## References

- [[tech-bridge-ambitious-software-agent-era]] · [[dioxus]] · [[jonathan-kelley]] · [[blitz]] · [[rust]]
- 관련: [[learning-curve-as-feature]] · [[harness-engineering]]

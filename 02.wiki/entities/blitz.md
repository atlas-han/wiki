---
title: Blitz
type: entity
category: tool
tags: [rust, rendering, css, html, gpu, dioxus]
sources: [tech-bridge-ambitious-software-agent-era]
created: 2026-09-14
updated: 2026-09-14
---

# Blitz

[[dioxus|Dioxus]]가 만든 **자체 HTML·CSS 렌더링 엔진**. 본 위키 첫 등장은 [[tech-bridge-ambitious-software-agent-era]].

> [[jonathan-kelley|Jonathan Kelley]]는 이것을 *"Dioxus에서 가졌던 가장 대담한 목표 중 하나"* 라 부른다.

## 구성 (소스에서 확인되는 것)

| 요소 | 내용 |
|---|---|
| **CSS 엔진** | **Firefox에서 브라우저급 CSS 엔진을 추출** |
| **DOM** | 자체 HTML DOM |
| **렌더링** | **하이브리드 GPU 파이프라인** |
| **번들 크기** | **5MB 미만** (Electron 대비) |
| **런타임 RAM** | **50MB 미만** |
| **확장** | *"자체 커스텀 컴포넌트, 회전하는 큐브 같은 걸 직접 만들 수 있고 **브라우저를 원하는 대로 맞춤 설정**할 수 있다"* |

> ⚠️ **5MB / 50MB는 자기 보고이고 측정 조건이 없다.** 비교 대상도 *"Electron 앱"* 일반이다.

## 에이전트가 가장 크게 기여한 자리

소스에서 Blitz는 **[[agents-as-patient-specialists|지식 문제]]의 대표 사례**로 쓰인다.

> **에이전트는 CSS 사양을 예외적으로 잘 압니다.** 페인팅이나 레이아웃 문제를 푸는 코드를 쓸 때 **에이전트는 Google Chrome과 Safari가 그걸 정확히 어떻게 처리하는지 즉시 떠올릴 수 있습니다.** 여러분 문제에 맞는 올바른 처리 방법을 알려 주고, **Apple의 Git 저장소 깊숙이 박힌 WebKit 소스 코드를 열어 볼 필요가 없습니다.** (11:11~11:34)

**브라우저 엔진 구현은 "사양이 방대하고 참조 구현이 흩어져 있는" 전형적인 지식 문제**이고, 소스는 이것을 에이전트 강점의 가장 선명한 예로 든다.

## References

- [[tech-bridge-ambitious-software-agent-era]] · [[dioxus]] · [[jonathan-kelley]] · [[subsecond]]
- 개념: [[agents-as-patient-specialists]]

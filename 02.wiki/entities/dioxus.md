---
title: Dioxus
type: entity
category: tool
tags: [rust, framework, cross-platform, ui, open-source]
links:
  - https://github.com/dioxuslabs/dioxus
sources: [tech-bridge-ambitious-software-agent-era]
created: 2026-09-14
updated: 2026-09-14
---

# Dioxus

[[rust|Rust]]로 쓰인 **크로스플랫폼 앱 프레임워크**. 창시자는 [[jonathan-kelley|Jonathan Kelley]]이고, 본 위키 첫 등장은 [[tech-bridge-ambitious-software-agent-era]].

> **표기 주의**: 자막에서 이름이 **네 갈래**로 갈렸다 — en-orig *Diosis · Dioxis · Daxis · DAX*, ko *디오시스 · Dioxis · Daxis · 다이옥시스 · DAX*. **실제 이름은 Dioxus** 이고 설명란의 GitHub 링크(`dioxuslabs/dioxus`)가 확정한다. **양 트랙이 함께 틀린 제품명 중 이 위키 최다 표기 기록**이다(직전은 [[goose|Goose]] 3표기).

## 설계 (소스에서 확인되는 것)

> **수십 가지 툴체인·언어·IDE를 거치는 대신, HTML과 CSS를 마크업으로 삼아 앱 전부를 Rust로 쓰면 어떨까?**

| 요소 | 내용 |
|---|---|
| **언어** | Rust 단일 |
| **마크업** | HTML · CSS |
| **반응성** | React에서 착상 |
| **런타임** | **VM 없음 · IPC 없음 · JavaScript 없음** |
| **대상** | 웹(풀스택) · iOS · Android · 네이티브 — **같은 코드베이스에서 컴포넌트 공유** |
| **시작 비용** | *"성가신 빌드 시스템 설정을 통째로 건너뛴다 — `main.rs` 하나면 된다"* |

**2021년의 문제 진단**: *"React Native는 버벅였고 Flutter는 너무 느렸으며 둘 다 네이티브 API와 잘 맞지 않았다."* 당시 **가져다 쓸 기성품 부품이 거의 없어** 반응성·폰트 렌더링·핫 리로딩·번들링을 전부 맨바닥에서 만들었다 — *"우리에게는 웹 브라우저를 만드는 것 같은 일조차 그 과정에 필요한 한 단계일 뿐이었습니다."*

그 과정에서 나온 두 프로젝트가 [[blitz|Blitz]](렌더링 엔진)와 [[subsecond|Subsecond]](핫 리로드 엔진)다.

## 규모 (2026 · 전부 자기 보고)

| 항목 | 값 |
|---|---|
| GitHub 별 | **약 37,000** |
| 다운로드 | **수백만** |
| 누적 최종 사용자 | **2억 명 이상** (화자 본인이 *"추정"* 이라고 명시) |
| 핵심 엔지니어 | **3명** |

용례로 든 것: **AI 비서, 투표 소프트웨어, 데이터 과학 도구, 우주 위성의 충돌 회피 시스템.**

## 에이전트와의 관계

이 프로젝트가 위키에 들여온 주장은 **Rust의 어려움이 에이전트 시대에 자산이 된다**는 것이다 → [[learning-curve-as-feature]].

에이전트가 실제로 기여한 것으로 소스가 드는 것:
- **Kotlin·Swift 플러그인**을 빌드 시스템에 깊이 통합 — *"손으로는 여러 해"* → **2~3주**(구현 첫날, 2주는 실기기 테스트)
- **릴리스 체크리스트 검증 · 백포팅 · 문서 동기화**
- **퍼징 하네스 구축** → [[test-harness-vs-test-authoring]]

그리고 실패한 것 — **[[slop-cannon|슬롭 캐논]]**: 수만 줄을 쏟아냈으나 *"품질 기준을 통과한 코드는 거의 없었다."*

**릴리스 주기**는 *"주 1회 혹은 주 여러 번"* 으로, *"예전 같으면 그렇게 자주 릴리스하기가 두려웠을 것"* 이라 한다. ⚠️ **패치 릴리스 수는 슬라이드에 있고 자막에 값이 없다.**

## 소유

**[[cognition|Cognition]]이 인수**했고 팀이 합류했다. **시점·조건은 소스에 없다.**

## References

- [[tech-bridge-ambitious-software-agent-era]] · [[jonathan-kelley]] · [[blitz]] · [[subsecond]] · [[cognition]] · [[rust]]
- 개념: [[learning-curve-as-feature]] · [[code-is-the-product]] · [[ambitious-software]] · [[slop-cannon]]
- 외부: <https://github.com/dioxuslabs/dioxus>

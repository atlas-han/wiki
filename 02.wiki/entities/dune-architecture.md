---
title: Dune (GrokBot 아키텍처)
type: entity
category: tool
tags: [architecture, electron, react, ci, agents, grokbot, cursor]
sources: [tech-bridge-lauren-tan-trusting-agents, tech-bridge-lauren-tan-2000-prs, tech-bridge-lauren-tan-agent-dev-workflow]
created: 2026-09-13
updated: 2026-10-09
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

## 세 원칙, host·client, 그리고 "사람에게는 짜증" (2026-09-26 · [[tech-bridge-lauren-tan-2000-prs]])

같은 화자의 녹화 발표가 더한 것:

- **세 원칙**(25:14~26:12) — ① **이미 있는 기술 부채를 삭제** ② **축복받은 패턴에 단일한 포장 경로(single paved path)** — *"관습적인 방법이 하나여야 에이전트가 추측하지 않는다"* ③ **나쁜 패턴을 보면 먼저 린트 규칙** — *"항상 즉시 치울 필요는 없다. 적어도 출혈은 멈춘다."* → [[codebase-gardening]]
- **명사 둘 추가** — **host**(*"GrokBot 가상 머신에서 도는"*)와 **client**(*"Dune 애플리케이션 전체를 구동하는"*). **entry point**는 *"일종의 라우트"*(27:12~27:43).
- **렌더러 예산에 120fps = 8ms** 추가(28:27~28:38). 경계 강제는 여전히 **import·의존성 그래프**(28:53~29:02). *"Cursor agents window에서 얻은 교훈"* 이라 명시.
- **주석 금지의 이유가 다르게 제시됐다** — *"에이전트가 코드 주변의 주석을 **진짜 문제를 풀지 않을 정당화**로 쓰고 반창고로 덮는다"* + **복제되어 퍼진다**(23:41~24:25). 위 표의 *"99%가 무관한 역사적 사연"* 과 **모순이 아니라 다른 층**이다. ⚠️ 대가(지식이 어디 남나)는 이번에도 답이 없다. ⚠️ ko 자막은 이 결정을 **"댓글 금지"** 로 옮겨 **PR 댓글 금지**처럼 읽힌다.
- **대가를 인정한다** — *"사람에게는 꽤 짜증나는 코드베이스일 수도"*(19:45~19:53). 이유는 기여자 구성 — *"디자이너, PM, **CEO**"*(20:06~20:15).
- **Dune이 요점이 아니다** — *"핵심 주제는 Dune이 아니라 여러분 자신의 에이전트 친화 프레임워크"*, **부족 지식을 스타일 가이드 리뷰에서 꺼내 코드베이스에 인코딩**(29:24~30:10).

`useEffect` 금지·*"Electron 앱을 위한 Next.js"*·PR 600건 재작성은 **이번 발표에 나오지 않는다.** 여전히 오픈소스 언급 없음.

## feature 발견 장치와 god file 8개 — 대담 발췌 (2026-10-09 · [[tech-bridge-lauren-tan-agent-dev-workflow]])

> *"But it comes with a lot of really really restrictive lit[=lint] rules"* (ko 트랙 영어 구간 04:41~04:44)
> *"the code base is designed in a way that there's really only one way to do something (…) features all go into a specific directory. Every feature has its own directory (…) there's like a, a...Thing that discovers features, like through a registry and like crawling the code base"* (04:42~05:07)
> *"the very first versions of Grokbot were composed of like eight god files"* (05:47~05:53)

- **새 구성 요소** — feature를 **레지스트리 + 코드베이스 크롤링**으로 발견한다. 위 제약 목록의 *feature 단위 디렉터리* 행을 보완한다.
- **기원** — feature 디렉터리는 *"I'm not going to append to a god file"*(05:40~05:45)에서 나왔고, GrokBot 첫 버전이 **god file 8개**였다. ⚠️ en-orig의 *"at least 100 lines long"*(05:53~05:55)은 god file 치고 작아 자릿수가 의심된다 — 인용하지 않는다.
- **대가의 다른 진술** — *"frees up your own mental capacity, and the agent doesn't have to think about that anymore"*(05:20~05:30). 09-25 발표의 *"사람에게는 짜증"* 과 **다른 측면**(인지 부하 vs 작성 자유)이라 모순으로 두지 않고 나란히 표시한다.
- 해설은 이 프레임워크를 *"공개 설치 도구로 받아들이기보다 기능을 추가할 경로를 어떻게 정했는지에 집중"* 하라고 권한다(ko 04:28~04:35). ko는 이름을 *"듀"*, en-orig 내레이션은 이름을 뺐다.

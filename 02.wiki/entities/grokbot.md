---
title: GrokBot
type: entity
category: product
tags: [persistent-agents, messaging-ui, agent-teams, cursor]
sources: [tech-bridge-grokbot-agent-teams, tech-bridge-cursor-legacy-refactoring, tech-bridge-lauren-tan-trusting-agents, tech-bridge-lauren-tan-2000-prs]
created: 2026-09-01
updated: 2026-09-26
---

# GrokBot

[[cursor|Cursor]]의 지속형(persistent) 개인 에이전트 제품. [[tech-bridge-grokbot-agent-teams]] 인터뷰 **전날 베타 출시**(즉 2026-08-30 전후).

## 구성 요소

| 요소 | 내용 |
|---|---|
| **정체성** | 이름·아바타·성격. [[lauren-tan]]의 봇은 전부 고양이, 원조는 강아지 Benny |
| **자체 컴퓨터** | 사용자가 자리에 없어도 실행. 사용자의 도구에 로그인 (예: LinkedIn) |
| **팀 구조** | 비서실장(chief of staff) 코디네이터가 다른 봇에게 임무 배분·진행 확인 |
| **메시징 UI** | 동료에게 문자하듯. "iMessage처럼 보인다"는 평 |
| **루틴·자동화** | 피드백이 들어오면 자동 실행 → 사람은 코드만 리뷰 |

## 위키에서 알려진 사실

- 데모에서 확인된 것: 마케팅 봇의 LinkedIn 실시간 게시, 비서실장이 사내 "GrokBot wins" 채널 피드백을 모아 **Figma 슬라이드**로 조립, 엔지니어링 봇 팀이 버그를 나눠 받아 **검토용 PR** 반환.
- 사내 채택이 엔지니어링을 넘어 시장 진출·운영·제품 팀까지 확산 — 강한 내부 PMF가 외부 출시 신호가 됐다.
- **GrokBot의 상당 부분이 GrokBot 자체로 만들어졌다.** 에이전트가 문제를 분류하고 코드를 써서 클라우드 에이전트에 연결하는 피드백 루프.
- 로드맵 언급: **iMessage 지원**(봇에게 문자 보내기)이 흔한 요청. 아직 확정 아님.
- 초기 실사용 사례로 Odyssey IMAX 70mm 티켓 예매, 식료품 구매.
- 남은 과제로 자잘한 버그가 인정됐다.

## 두 번째 언급 (2026-09-08 편)

[[tech-bridge-cursor-legacy-refactoring]]의 마지막 답변에서 GrokBot이 다시 나온다. 질문은 *"스케줄로 도는 cloud agent가 **로컬 머신의** 무언가에 접근해야 하면?"* 이었고, 답은 레포에 커밋된 것(스킬·계획·파일)은 되지만 머신에 있는 것은 프라이빗 커넥티비티가 필요하다는 것이었다. 그 다음에:

> **`GrokBot`이라는 정말 멋진 도구가 있습니다. 일반 지식 제품이지만 코딩에도 쓸 수 있습니다.** 그것이 **클라우드와 로컬을 함께 써서 당신 머신에서 여러 가지를 작업하는 정말 좋은 해법**을 갖고 있습니다. **다음 주 목요일에 그걸로 워크샵을 합니다.**

→ 이 위키가 [[tech-bridge-grokbot-agent-teams]]에서 *지속형 개인 에이전트* 로 기록한 GrokBot이, **로컬 머신 접근이라는 [[cursor-cloud|Cursor Cloud]]의 구조적 한계를 메우는 자리**에 놓인다. 두 제품 축이 연결되는 두 번째 지점이다.

> ⚠️ *"일반 지식 제품(general knowledge product)"* 이라는 표현은 이 소스가 처음 쓴다. GrokBot이 코딩 특화가 아니라는 [[cursor]] 페이지의 서술과 일치한다.
> **"다음 주 목요일"** 은 이 소스의 촬영 시점 추정(2026-09-01 무렵)과 맞물리는 단서이며 날짜를 확정하지 않는다.

## 두 번째 소스 — 만들어진 방식과 재작성 (2026-09-12 편)

[[tech-bridge-lauren-tan-trusting-agents]]가 GrokBot의 **코드베이스 쪽 이야기**를 준다.

- **바이브 코딩된 그린필드로 시작했다** — *"아주 빠르게 바이브 코딩됐습니다. **사람은 코드를 전혀 읽지 않았습니다.**"* → [[organic-architecture]]
- **전체를 다시 짰다** — **PR 600건 이상**을 들여 [[dune-architecture|Dune]] 아키텍처로 리팩터링(자기 보고).
- 프레임워크의 명사가 GrokBot의 개념이다 — `feature` · `entry point` · **`transcript card`**(채팅에 보이는 카드).
- **가상화(virtualization)** 가 *"누군가 만든 새 라이브러리"* 로 돌아간다 — **이름은 자막에서 확정 불가.**
- **[[grokbot|Benny]]의 동작이 구체화됐다** — 버그 리포트를 받아 **클라우드에서 자기 데스크톱을 열고 Cursor를 돌려** control 스킬로 재현한다. 소스의 예에서 Benny는 **버그를 재현했으나 이미 main에서 고쳐져 있음을 확인**해 주었다.
- **비엔지니어의 기여 경로** — PM·디자이너가 직접 기능을 내보내고 엔지니어는 리뷰만 한다. 화자는 이를 *"Dune 아키텍처가 버티고 있다는 증거"* 로 읽는다.
- **위치 규정** — Cursor의 기존 표면(agents window·CLI·IDE)은 **파워 유저 도구**였고 GrokBot은 *"기술 분야가 아닌 사람들에게 결정적 순간"*, *"iMessage처럼 보인다"*.

> ⚠️ **출시일 기록을 정정할 근거가 생겼다(확정은 하지 않는다).** 위 *"인터뷰 전날 베타 출시(즉 2026-08-30 전후)"* 는 **[[tech-bridge-grokbot-agent-teams]]의 Tech Bridge 업로드 날짜(08-31)에서 끌어온 추정**이다. 그런데 같은 날 열린 이 워크숍에서 화자는 **GrokBot이 "어제" 출시됐고 [[grok-4-6|Grok 4.6]]이 "오늘" 발표됐으며 "이번 달은 아직 12일밖에 안 됐다"** 고 말한다(양 트랙 일치). **08-30·08-31은 12일이 아니다.**
>
> 이 위키는 2026-09-03에 **"업로드 날짜 ≠ 촬영 날짜"** 를 원칙으로 세웠는데 이 페이지에는 적용되지 않았다. **달을 확정할 근거가 없으므로 어느 쪽도 채택하지 않고 반증 증거만 표시한다.** 자세한 것은 [[tech-bridge-lauren-tan-trusting-agents]]의 시점 절.

## References

- [[tech-bridge-grokbot-agent-teams]] · [[persistent-agent-teams]] · [[cursor]] · [[lauren-tan]] · [[roshan-sadanani]]

## 세 번째 본인 소스 — "바깥 루프" (2026-09-26 · [[tech-bridge-lauren-tan-2000-prs]])

[[lauren-tan]]의 녹화 발표가 GrokBot과 Cursor의 **역할 분담을 처음 말로 정리**한다:

> **GrokBot과 Cursor는 함께 흥미로운 역할**을 합니다. **GrokBot은 제가 바깥 루프(outer loop)라고 부르는 것을 제공하는 데 아주 뛰어나요.** **Slack, Datadog, Sentry, PlanetScale** 등 여러 커넥터에 연결해 정보를 모으고 스스로 좋은 결정을 내리게 할 수 있으니까요. (32:34~33:05)

> **GrokBot 루틴**은 **Slack 스레드나 Sentry 알림을 구독해서 자동으로 일을 시작**하게 해 줍니다. (…) GrokBot은 **바깥 루프에서 오는 이벤트에 자동으로 반응해서 cloud agent를 띄울** 수 있습니다. (33:50~34:20)

- **구도**: GrokBot = **바깥 루프**(외부 신호·이벤트) → Cursor **cloud agents** = 실행 → **코드베이스·규칙·스킬** = 공유 인프라. 여기에 **Cursor automations**와 **SDK**로 *"세팅한 에이전트 인프라를 재사용하는 추가 봇"*(34:23~34:39). 결과 사례(스크린샷): **버그 리포트 자동 재현, PR 자동 오픈**(34:48~35:04).
- 위 구성 요소 표의 **루틴·자동화** 행에 **구독 대상(Slack 스레드·Sentry 알림)** 과 **커넥터 목록**이 처음 채워졌다.
- *"어떤 사람들은 이걸 **회사 두뇌**라고 부르는데 저는 그렇게 정교한 게 필요하다고 생각하지 않는다"*(33:05~33:16) → [[company-brain]]
- **Dune의 host는 "GrokBot 가상 머신에서 돈다"**(27:31~27:36) — 위 *"자체 컴퓨터"* 행과 맞물린다. → [[dune-architecture]]
- 화자 소개가 *"**SpaceX AI에서** GrokBot을 만든다"*(00:03~00:07)로 바뀌었다. ⚠️ 이 페이지 첫 줄의 *"Cursor의 … 제품"* 은 고치지 않는다 — 화자는 *"Cursor가 SpaceX AI의 일부가 되었다"* 는 취지로만 말한다(→ [[cursor]]).

> ⚠️ **당사자의 제품 권유**이고 커넥터·루틴의 가용 범위, 비용, 실패 사례는 없다. ko·en-orig 모두 제품명을 여러 번 틀린다(en-orig *graphbot·Rockbot·Grockbots* / ko *"GraphBot"·"성장봇"*).

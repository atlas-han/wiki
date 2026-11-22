---
title: Devin
type: entity
category: product
tags: [coding-agent, slack, design-automation, qa]
sources: [tech-bridge-one-designer-plus-ai, tech-bridge-ryan-carson-managing-20-agents, tech-bridge-walden-yan-cognition-no-laptop-development]
created: 2026-09-15
updated: 2026-11-22
---

# Devin

**Slack 안에 상주하는 코딩 에이전트.** 이 위키에서 이름만 지나가던([[overview]]의 프레임워크 열거) 것이 [[tech-bridge-one-designer-plus-ai]]에서 **실제 사용 기록으로** 처음 선다. 특이한 것은 그 기록이 **개발 조직이 아니라 디자인 조직에서** 왔다는 점이다.

> **저희는 사무실에서 Devin을 많이 씁니다. 다들 Devin을 써요. 다들 Devin을 남용하다시피 하죠.** — [[vincent-wendy|Vincent Wendy]] (05:49~06:05)

## 소스에서 확인되는 용법

| 쓰임 | 내용 |
|---|---|
| **일정표 생성** | 최신 데이터를 당겨 와 렌더 → PNG 내보내기 → USB로 화면에. 예전엔 [[figma\|Figma]] 수작업 |
| **픽셀 퍼펙트 구현** | *"이거 더 정확하게 해 줄 수 있어?"* · [[model-context-protocol\|MCP]] 연결 · 스펙 시트 제공 |
| **발표자 그래픽 생성기** | 300명 이상이 **본인이 직접** 만들게 하는 도구 → [[self-serve-asset-generation]] |
| **사진 ↔ 인물 매칭** | *"이 사람 누구야?"* — *"틴더 같은 판정"* → [[agent-visual-qa]] |
| **로고 누락 검수** | 140곳 스폰서 배너·티셔츠에서 빠진 로고 찾기. 화자 자기 보고 **정확도 100%** |
| **1회용 기능 추가** | 편집 버튼 없는 생성기에 *"편집 버튼 하나 만들어 줄래?"* → [[exception-handling-as-the-job]] |

## 거처가 워크플로를 정한다

화자의 경로가 **Slack → Figma → 다시 Slack** 인 이유는 아키텍처가 아니라 **Devin이 Slack 안에 살기 때문**이다. [[multiplayer-agent-context]]가 말하던 자리의 구체 사례다 → [[design-handoff-friction]].

## 화자가 놀라워하는 지점

> **놀랍게도 Devin은 시각적으로 감지하는 법을 압니다.** (13:37~13:45)

즉 이 사용자에게 Devin의 값은 **코드 생성**이 아니라 **시각 판정과 1회용 도구 제작**에 있다.

## 미해결 사항

- **제작사** — 소스가 말하지 않는다. 이 위키에 [[cognition]] 페이지가 있으나 **소스가 둘을 연결하지 않으므로 연결하지 않는다.**
- **가격·모델·한도** 언급 없음.
- ⚠️ **자막 표기 주의** — en-orig가 *Devon · def · defin · Deon* 네 표기로 흔들고, 디자인 팀 소개에서는 **`Devin` + `GPT`가 "Devon GBT"라는 한 이름으로 붙었다.** 셋이라는 근거는 **채널 공식 챕터 제목**(*"디자인 팀: Devin, GPT, Figma"*)과 설명란이다.

## References

- [[tech-bridge-one-designer-plus-ai]] · [[vincent-wendy]] · [[figma]]

## 개발 조직의 사용 기록 — 매니저 세션 · 빌더 20개 · 영상 녹화 (2026-11-17 · [[tech-bridge-ryan-carson-managing-20-agents]])

두 번째 소스는 개발 조직에서 온다. [[ryan-carson|Ryan Carson]]([[untangle|Untangle]])의 발표 해설에서 Devin은 **조직도 전체가 올라탄 도구** 다(해설 전달).

- 매니저 에이전트는 *"특별한 프로그램이 아니라 데빈에서 연 세션 하나입니다."*(01:34~01:36) 빌더 · 리뷰 · QA · 머지 큐 매니저도 세션이다.
- Carson이 기대는 기능 셋: **기능을 써 보는 영상 녹화**(없으면 직접 만들어야 하는데 어렵다고 한다) · 자동화(15분마다 매니저에게 빌더 확인을 시킨다) · 세션끼리의 대화.
- 채용 유급 과제에서 지원자에게 Devin 계정을 준다.
- 비용: 8월 How I AI 인터뷰의 제목이 *한 달에 Devin에 2만 달러를 썼다*.

⚠️ 제작사는 이 소스도 말하지 않는다 — 위 미해결 항목 그대로. ko ASR 표기 *데빈 · 데비네*.

## 2026-11-22 — 제작사가 말하는 Devin: 버그 신고에서 배포까지 · 영상 증거 · 직무를 맡는 에이전트 ([[tech-bridge-walden-yan-cognition-no-laptop-development]])

앞선 두 소스는 Devin을 **쓰는** 쪽(디자인 조직 · Untangle)의 기록이었다. 이번은 만드는 쪽 [[cognition|Cognition]]의 [[walden-yan|Walden Yan]]이 자사에서 Devin을 어떻게 쓰는지 말한 발표의 한국어 해설이다. ⚠️ 제작사의 자기 보고, 해설 전달.

- **맡는 범위.** *"버그 신고가 들어오면 분류부터 구현, 테스트, 리뷰까지 데빈이 합니다. 배포와 장애 대응도 마찬가지입니다. 사람은 판단이 필요할 때만 불러옵니다."*(01:25~01:33)
- **Slack과 영상.** *"데빈은 PR을 올리고 고친 화면을 녹화한 영상을 증거로 같이 보냅니다."*(02:58~03:00) 발표 원음(두 자막 트랙 일치): *"And most of the time our engineers don't even need to look open dev and they're just from Slack looking at the recordings that it sends back to them."*(08:15~08:19) — [[tech-bridge-ryan-carson-managing-20-agents]]가 사용자 쪽에서 본 것(영상을 보고 *Ship it*)과 같은 흐름이다. → [[agent-change-evidence]]
- **자기 환경을 돌본다.** 매시간 새로 만드는 가상 머신에서 *"빌드가 깨지면 데빈이 먼저 고칩니다."*(03:58) *"테스트하는 방법도 데빈이 스크립트 파일로 직접 적어둡니다. 코드가 바뀌면 그 스킬도 데빈이 고칩니다."*(04:00~04:03)
- **여럿이 쓰는 기능의 시험.** *"데빈은 가상 머신 하나에서 계정 여러 서로 같은 줌 통화에 들어가 음성을 주고받았습니다."*(04:32~04:36)[=계정 여럿으로(추정)]
- **세션 기록.** *"클라우드에서 돌린 세션은 코드 한 줄 결정 하나까지 기록에 남습니다."*(04:42~04:43) → [[run-trace-skill-distillation]]
- **직무.** 안드로이드 앱 사례에서 Devin은 44일 동안 PR 1,134개를 머지했고 *"커밋의 98.5%를 데빈이 쓰었습니다."*(08:33~08:34)[=썼습니다] 이 방식이 제품으로 나온 것이 [[devin-bots]]다.

⚠️ 제품의 구조(어떤 모델 · 가격 · 세션 한도)는 이번에도 소스에 없다.

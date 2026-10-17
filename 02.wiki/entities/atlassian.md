---
title: Atlassian
type: entity
category: org
tags: [jira, confluence, bitbucket, rovo-dev, sdlc, coding-agents, code-review, context-engine, enterprise]
aliases: [Atlassian, 아틀라시안, Rovo, Rovo Dev, Jira coding agent, JCA, AutoDev, AI reviewer, AI Planner, AI SRE, AI Context Engine, Teamwork Graph, Rovo Chat]
links:
  - "https://www.atlassian.com/software/rovo-dev"
sources: [tech-bridge-atlassian-build-your-own-sdlc]
created: 2026-10-17
updated: 2026-10-17
---

# Atlassian

**Jira·Confluence·Bitbucket을 만드는 회사.** 이 위키에서는 [[tech-bridge-atlassian-build-your-own-sdlc]]에서 처음 소스의 주체가 됐다. [[andy-wong|Andy Wong]] · [[andrei-bocan|Andrei Bocan]] · [[shane-wolf|Shane Wolf]]가 [[ai-engineer|AI Engineer]] World's Fair 워크숍에서 SDLC용 에이전트 제품군을 소개했다. 그 전에는 Claude 플러그인의 Atlassian MCP·스킬로만 언급됐다([[agent-skills]] · [[model-context-protocol]] · [[plan-to-ticket-pipeline]]).

## 전략 — 코드의 왼쪽과 오른쪽

> *"as we have more AI curing[=coding] tools kind of productivity gains from those tools are kind of tapering (…) what our biggest opportunities are tapping on the on the everything left and right of code. So everything involving planning orchestration uh the code review process as well as the operations part"* (01:34~01:58)

⚠️ "tapering"의 근거 데이터는 발화되지 않는다.

## 제품 (2026 World's Fair 워크숍 기준, 당사자 진술)

| 제품 | 발화된 내용 |
|---|---|
| **Jira coding agent (JCA)** | Jira·Confluence·email·Slack 맥락으로 티켓을 계획·구현(02:24~02:55). 수락 기준 체크리스트를 스스로 검증, 호스팅 샌드박스(컨테이너, Docker, BYO 불가)에서 브라우저까지 띄움(25:15~26:13). 모델: Anthropic·OpenAI(Gemini 미확인). *"it's out now"*(27:22) |
| 타사 에이전트 할당 | Jira 티켓을 Claude·Cursor·Codex 등에 할당(03:25~03:32) |
| SDLC automations | Jira 자동화 조건 → 에이전트로 코드 생성(03:39~03:56). Epic 분할 후 JCA 세션 자동 시작에도(53:17~53:36) |
| **AI reviewer + standards** | 버그·기준·요구사항 검사, Jira·Confluence·SCM·Slack 맥락(04:05~04:43). 중앙 관리 standards(Markdown, 저장소 패턴 지정, GitHub·GitLab·Bitbucket Cloud). 자체 학습 모델로 저가치 댓글 필터 → *"around 40% (…) human code resolution rate (…) human baseline of 45"*(06:11~06:20, ⚠️ 정의 미발화). CI check 매핑은 기본 제공 없음(51:58~52:03). skills 지원 *"less than a month ago"*(56:54~56:56) |
| **AutoDev** | 백로그에서 자율 처리 가능한 항목을 골라 PR(39:48~40:02). 기존 코드의 점진적 standards 준수, 1인당 주 3~5 PR·WIP 한도·티켓/주 단위 비용 한도, 저명세 항목은 사람에게 명세 요청, 리뷰어를 Slack으로 호출, ROI insights(40:42~46:15) → [[review-wip-limit]] |
| AI Planner | 기능 아이디어의 저장소 기준 실현 가능성·구현 분해·실행 방법(46:17~47:08). 데모 없음 |
| AI SRE | 이전 incident·Jira·Confluence로 근본 원인·완화 단계, Slack 요약(08:25~09:28). ⚠️ 이름은 챕터·ko 기준 |
| **AI Context Engine** | 그래프 DB(추론 + 명시 연결) 위 agentic search, 모노레포 대신 code context(16:11~19:10). 권위는 사람이 표시(verified badge, 21:03~21:12, 35:55~36:05). *"I think we have 15,000 repositories across the company"*(47:40~47:44). Teamwork Graph CLI로 노출(50:50~51:15) → [[context-engine]] |
| Rovo Chat code context | 얼리 액세스, *"announced it a couple months ago"*(50:05~50:11) |

## ⚠️ 유보

- 전부 당사자 진술이다. 실습이 Wi-Fi 장애로 무산돼 시연은 standards 설정 화면 하나뿐이다.
- 과금(Atlassian credits vs 자기 API 키)은 영상 안에서 답이 엇갈린다(26:33~27:11).
- 제품명 표기는 en-orig ASR(*"Robo Dev"*·*"s sur"*·*"context machine"*)을 챕터·설명란·문맥으로 고친 것이다.

## References

- [[tech-bridge-atlassian-build-your-own-sdlc]] · [[andy-wong]] · [[andrei-bocan]] · [[shane-wolf]] · [[context-engine]] · [[tech-bridge]]

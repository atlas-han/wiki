---
title: Cursor
type: entity
category: org
tags: [ide, coding-agent, grokbot, benchmark]
links:
  - https://cursor.com
sources: [tech-bridge-grokbot-agent-teams, tech-bridge-cursor-legacy-refactoring, tech-bridge-lauren-tan-trusting-agents]
created: 2026-09-01
updated: 2026-09-13
---

# Cursor

AI 코딩 도구·에이전트 회사. 본 위키 첫 등장은 [[tech-bridge-grokbot-agent-teams]].

## 위키에서 알려진 사실

- 제품 축이 둘로 갈라져 있다: **코딩 특화 IDE/에이전트**(파워 개발자 대상)와 **[[grokbot|GrokBot]]**(범용·대중 대상 지속형 봇 팀).
  - [[lauren-tan]]의 대비: Cursor 사용자는 파워 유저라 조절 장치가 많은 코딩 특화 UI가 맞다. GrokBot은 반대로 *"에이전트가 동료처럼 느껴진다면"* 을 물었다.
- **클라우드 에이전트**를 설정해 두면 GrokBot이 그 에이전트를 실행할 수 있다 — 두 축이 연결되는 지점.
- 사내 문화: 여러 사람이 각자 에이전트·Slack 봇을 만들고 있었고, 그 패턴의 **패키지화**가 GrokBot의 출발점.
- **Cursor Bench 3.2** 벤치마크 발표 주체 ([[grok-4-6]] 70.8% @ $2.81 vs Fable 5 Max 70.5% @ $17.32).
- 소스 서술상 **SpaceX와 Grok 4.6을 공동 발표**. ⚠️ 위키는 소스 서술 그대로 기록하며 독립 확인하지 않았다.

## 제품 표면과 하네스 (2026-09-08 편)

[[tech-bridge-cursor-legacy-refactoring]]이 [[tech-bridge-grokbot-agent-teams]]에서 이름만 나왔던 부분을 실제로 채운다.

**네 표면**: **agents 창**(기본 — 에이전트가 각자 저장소에서 옆에 살고 여러 저장소를 가로지름) · **IDE**(VS Code 포크, *"영원히 지원을 멈추지 않겠다"*) · **CLI**(tmux 워크플로 보존, Xcode·Android Studio용) · **[[cursor-cloud|cloud]]**.

**cursor harness** — 이 위키의 [[harness-engineering]]·[[agent-harness-design]]에 Cursor 자신의 정의가 붙는다:

> **플랫폼과 모델 사이에 있는 것을 cursor harness라고 부릅니다.** 그것은 **도구 실행 · 캐시 관리 · 동적 컨텍스트 관리 · 컨텍스트 조립**으로 이루어져 있습니다.

**모델 라인업**: 프런티어 랩 모델 전부 + 오픈소스(Kimi · GLM) + 자체 모델 **Composer**(2.5) + [[grok-4-6|Grok 4.6]]. `auto`라는 **스마트 라우터**가 모델을 자동 선택한다. ⚠️ *"GPT-5.6 Soul"* · *"DeepSeek V4 Flasher Pro"* 는 표기 확정 불가.

**기능**: `/canvas`(코드베이스·파일·스프레드시트·MCP 데이터 → 인터랙티브 시각화, **팀 범위 공유**·PDF 내보내기) · **plan mode**(코드를 쓰지 않고 마크다운 계획서만, `ask question` 도구로 사전 질문 강제 가능) · **내장 브라우저**(`@browser`, IDE에서 `Cmd+Shift+B`) · **에이전트 타일링** · `add to side chat` · **multitask mode**.

**플러그인** — MCP와 스킬을 함께 배포하는 단위다. Atlassian · Datadog · Figma · **Google(Drive·Calendar·Gmail)**. Atlassian·Figma 플러그인은 **각 팀이 퍼블리시한 스킬**을 함께 준다. Cursor는 사내에서 쓰는 스킬 전체를 **`superpowers` 플러그인으로 오픈소스 공개**했다고 말한다. 팀 학습용 **`continual learning` 플러그인**은 `AGENTS.md`에 작업·글쓰기·코딩 스타일을 축적한다 → [[continual-learning]].

**사내 활용**: 문서-구현 동기화를 검사하고 PR을 여는 **Slack 봇**, 금요일 백로그 일괄 실행 → 월요일 PR 리뷰, **유럽/아시아 팀 비동기 인계**, 온콜 인시던트 초기 조사 automation.

> ⚠️ 전부 **당사자 진술**이며 독립 확인이 없다. 발표자 이름은 소스 안에서 **Amita / Amriita** 로 갈리고 설명란에 없어 **위키가 어느 표기도 채택하지 않았다.**

## 내부 실천 — 검증·아키텍처·강제 (2026-09-12 Lauren Tan 편)

[[tech-bridge-lauren-tan-trusting-agents]]가 Cursor 내부의 작업 방식을 여럿 드러낸다.

- **agents window의 사내 코드명은 `glass`** 다. [[lauren-tan]]이 만든 첫 스킬 중 하나가 `control glass`.
- **agents window는 React 애플리케이션**이고, 화자는 원래 **cloud agents 팀**에 합류할 예정이었다가 React 경험 때문에 이쪽을 맡았다. 당시 **출시까지 일주일**이었다.
- **성능 문제가 상존한다** — *"머지되는 pull request가 너무 많아 그중 어느 하나가 성능·안정성·신뢰성을 회귀시킬 수 있다."* 원인의 하나는 **Electron 렌더러/메인 스레드 격리가 부실**한 것(60fps = 프레임당 16ms).
- **agents window에는 아직 [[dune-architecture|Dune]] 아키텍처가 없다.** 화자가 옮길 계획이라고 말한다.
- **bugbot** — *"CI에서 도는 Cursor의 코드 리뷰 도구"*. [[hard-vs-soft-enforcement|강제의 층]]에서는 **소프트**로 분류된다.
- **`/loop`** — eval을 *"전부 10점 만점이 될 때까지"* 반복시키는 데 쓴다. → [[skill-evals]]
- **내부 피드백 채널** — 슬랙에 agents window·GrokBot 피드백이 모이는데 *"제보 품질이 아주 나쁠 때가 많다"*. → [[feature-map]]
- **모델 다양성이 eval의 자산**이다 — *"Cursor의 좋은 점 하나는 아주 많은 모델을 지원한다는 것"* 이라 스킬을 모델 행렬에 걸쳐 평가할 수 있다.
- 화자가 Cursor를 **"AI 랩"** 이라 부르고 **무제한 토큰**을 인정한다.

## References

- [[tech-bridge-grokbot-agent-teams]] · [[grokbot]] · [[grok-4-6]] · [[lauren-tan]] · [[roshan-sadanani]]

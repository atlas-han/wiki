---
title: Cursor
type: entity
category: org
tags: [ide, coding-agent, grokbot, benchmark]
links:
  - https://cursor.com
sources: [tech-bridge-grokbot-agent-teams, tech-bridge-cursor-legacy-refactoring, tech-bridge-lauren-tan-trusting-agents, tech-bridge-exa-perfect-search-for-agents, tech-bridge-lopopolo-agent-harness, tech-bridge-jensen-huang-cbs-interview, tech-bridge-lauren-tan-2000-prs]
created: 2026-09-01
updated: 2026-09-26
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


## 검색을 외부에 맡긴다 (2026-09-22 추가)

> 커서 에이전트가 **최신 기술 문서나 뉴스를 검색하기로 결정할 때 내부적으로 [[exa|Exa]]를 이용하게 될 겁니다.** — [[will-bryk]] ([[exa|Exa]] 창업자), [[tech-bridge-exa-perfect-search-for-agents]] (01:12~01:22)

**이 위키에서 코딩 에이전트의 검색 부품이 외부 벤더로 지목된 첫 자리다.** [[agentic-search]]의 삼분할(모델·하네스·엔진) 중 **엔진을 사 온다**는 뜻이고, [[reference-graph-vs-vector-search]]가 다룬 **코드 인덱싱**과는 다른 축이다 — 이쪽은 **저장소 바깥의 웹**이다.

⚠️ **[[will-bryk|Bryk]] 쪽의 진술이고 Cursor의 확인이 아니다.** 계약 범위·기간·비중은 전혀 없다.

## References

- [[tech-bridge-grokbot-agent-teams]] · [[grokbot]] · [[grok-4-6]] · [[lauren-tan]] · [[roshan-sadanani]] · [[tech-bridge-exa-perfect-search-for-agents]]

## 경쟁사 에피소드가 부른 하네스 (2026-09-23 · [[tech-bridge-lopopolo-agent-harness]])

Google 측 에피소드가 [[antigravity|Antigravity]]·[[claude-code|Claude Code]]와 함께 Cursor를 *"현재 가장 인기 있는 에이전트 하네스"*(24:24~24:28)로 든다. *"어떤 용도에 가장 적합한 것일까요?"*(24:30~24:37)를 묻고 **답하지 않는다.** 위 09-08의 **cursor harness 정의**(도구 실행·캐시·동적 컨텍스트·컨텍스트 조립)와 이 에피소드의 [[ryan-lopopolo|Lopopolo]]가 말한 *"작업을 분류하고 필요한 컨텍스트를 동적으로 파악"*(12:58~13:30)이 같은 자리다.

## NVIDIA 사내 사용 (2026-09-25 · [[tech-bridge-jensen-huang-cbs-interview]])

[[jensen-huang|Jensen Huang]]이 CBS 인터뷰에서 *"우리는 [Cursor]를 사용합니다"*(01:16~01:19)라고 한다 — [[openai-astra|Astra]]·[[claude-code|Claude Code]]·[[cognition|Cognition]]과 나란히. 09-06 G20 편(*"Anthropic, OpenAI, Cursor 같은 기성 AI"*)에 이어 **같은 화자의 두 번째 언급**이다. ⚠️ 규모·용도 없음. ko는 **"커서"**(01:16).

## "우리가 SpaceX AI의 일부가 되기 전" (2026-09-26 · [[tech-bridge-lauren-tan-2000-prs]])

[[lauren-tan]]이 녹화 발표에서: *"6개월 전 제가 처음 Cursor에 합류했을 때, **우리가 SpaceX AI의 일부가 되기 전**"*(02:07~02:17), *"**Cursor와 SpaceX AI**에서 지낸 지난 6개월"*(04:14~04:20), 자기소개는 *"**SpaceX AI에서** GrokBot을 만든다"*(00:03~00:07). 영상 제목은 *"Cursor&xAI 개발자"* — **xAI는 자막에 없다.**

> ⚠️ **이 위키에서 Cursor가 (화자 합류 이후) SpaceX AI의 일부가 되었다는 취지의 첫 발화**다. 위 *"SpaceX와 Grok 4.6을 공동 발표"* 와 같은 방향이지만 **"일부가 되었다"의 형태(인수·편입·제휴)와 시점은 말하지 않는다.** 이 위키는 **조직 구조를 추정하지 않고 발화만 기록**한다. 제목의 *"xAI"* 는 채택하지 않는다(09-12 설명란과 같은 처리).

같은 발표의 Cursor 내부 서술: **agents window = "Cursor IDE를 대체할 새 표면"**(02:28~02:36)이었고 합류 당시 **성능 문제가 많았다**. **Bugbot**은 이번에도 **지침(소프트) 층**으로 분류되고 → [[hard-vs-soft-enforcement]], **Cursor automations·SDK**가 [[grokbot]]의 바깥 루프와 짝을 이룬다(34:23~34:39). ⚠️ ko는 *bugbot* 을 **"오류 봇"** 으로 옮긴다.

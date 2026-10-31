---
title: 예약형 에이전트 자동화 (Scheduled Agent Automations)
type: concept
category: pattern
tags: [automations, scheduling, webhooks, maintenance, proactive, memory]
aliases: [automations, 예약 에이전트, 트리거 에이전트]
related: [cloud-agent-delegation, persistent-agent-teams, agent-memory, skill-self-improvement, executable-standards, grokbot, sweeper-agent, always-on-agent-architecture]
first-seen: tech-bridge-cursor-legacy-refactoring
sources: [tech-bridge-cursor-legacy-refactoring, tech-bridge-agent-to-agent-as-search, tech-bridge-lauren-tan-2000-prs, tech-bridge-tessl-harness-engineering-factory, tech-bridge-cooking-with-codex, tech-bridge-brockman-start-building-before-ready, tech-bridge-five-concepts-coding-with-ai-agents, tech-bridge-openhands-sandboxing-coding-agents, tech-bridge-lee-robinson-always-on-agents, tech-bridge-dan-martell-grokbot-daily-automation]
created: 2026-09-09
updated: 2026-10-31
---

# 예약형 에이전트 자동화

**예약되거나 이벤트로 트리거되는 클라우드 에이전트**를 유지보수 잡으로 쓰는 패턴.

> **automations는 기본적으로 예약되거나 트리거되는 cloud agent입니다.** — [[tech-bridge-cursor-legacy-refactoring]]

## 트리거

- **시간 기반** (예: 매주)
- **이벤트 기반** — PR 열림, 라벨 변경
- **메시지** — Slack, Teams
- **커스텀 웹훅** — 예: Jira 티켓을 to-do → in progress로 옮길 때

## 시연된 예 — feature flag cleaner

> *"매주 이 레포를 훑어서 **지난 30일 동안 쓰이지 않은 방치된 피처 플래그**가 있는지 봐줘. **Datadog과 Sentry로 교차 확인**해서 문제가 없었는지 확인해줘. **플래그를 제거한 PR과, 제거가 회귀를 만들지 않았음을 확인하는 테스트를 올려줘.** 끝나면 **Slack으로 PR을 보내줘.**"*

템플릿으로 **테스트 커버리지 추가 · 취약점 스캔 · 인시던트 분류**가 제공된다. 온콜 활용이 명시된다 — *"새벽 3시에 사람을 깨우는 대신"* 초기 조사를 하고 담당자에게 요약을 보낸다.

## 논지 — 리팩터링을 하지 않아도 되게 만든다

이 패턴의 핵심 주장은 도구 소개가 아니라 **레거시가 생기는 원인에 대한 진단**이다.

> **레거시 코드베이스를 리팩터링할 때 우리는 "어쩌다 이 상태가 됐지?"라고 묻습니다.** 많은 경우 그냥 **충분히 선제적이지 않았기 때문**입니다. 의존성이 갱신되지 않았고, 미리 할 수 없었던 것입니다.

> **그래서 automations는 나중에 리팩터링을 해야 하는 일을 피할 수 있도록 미리 일을 합니다.**

즉 [[plan-to-ticket-pipeline]]이 *이미 쌓인 레거시를 푸는* 절차라면, 이 패턴은 **다시 쌓이지 않게 하는** 절차다. 네 단계 워크플로의 마지막 자리를 차지하는 이유가 그것이다.

## `memories.md` — automation이 실행마다 나아진다

> **모든 automation에는 `memories.md` 파일이 있습니다. 이것이 automation이 실행할 때마다 더 나아지는 방법입니다.** 무언가를 놓쳤거나 *"Slack에 이렇게 표현한 게 마음에 안 들었어"* 라고 후속으로 말해야 했다면 **그 피드백에서 배우고 다음 실행마다 더 나아집니다.**

→ [[agent-memory]]·[[skill-self-improvement]]에 **파일 기반·잡 단위** 사례가 하나 더 붙는다. 이 위키가 본 메모리 구현 중 **반복 실행되는 잡에 귀속된 것**은 처음이다.

## 이 위키에서의 자리 — 항상 켜진 에이전트의 세 번째 형태

| 형태 | 성격 |
|---|---|
| [[persistent-agent-teams]] · [[grokbot]] | **동료 같은 봇** — 정체성·메시징 UI |
| [[cloud-agent-delegation]] | **위임받은 작업자** — 티켓을 받아 PR을 낸다 |
| **이 페이지** | **유지보수 잡** — 사람이 요청하지 않아도 도는 것 |

## ⚠️ 미해결

- **automation이 잘못 돌 때의 폭발 반경**이 논의되지 않는다. 매주 자동으로 PR을 올리는 잡의 실패 모드가 다뤄지지 않는다 — [[action-reversibility]]가 제기한 문제가 여기 그대로 적용되는데 소스는 연결하지 않는다.
- **`memories.md`가 잘못 학습했을 때의 정정 경로가 없다.**
- 발표자가 시연 중 **Statsig MCP 연결에 실패**해 Datadog으로 대체했다.

## 지식의 흐름을 유지보수하는 예약 잡 (2026-09-10)

[[tech-bridge-agent-to-agent-as-search]]의 [[sweeper-agent|청소부 에이전트]]는 형태상 이 개념이다 — *"**하루의 끝에** 사일로의 새 정보를 보고 공개 공간에 넣는다."* 차이는 대상이다: [[cursor-cloud|Cursor]]의 automation이 **코드베이스**를 유지보수한다면(feature flag 청소), 청소부는 **조직 지식의 흐름**을 유지보수한다(비공개 사일로 → 공유 위키). 이 개념의 논지 *"리팩터링을 하지 않아도 되게 만든다"* 를 지식에 옮기면 *"사람이 남을 위해 문서를 쓰지 않아도 되게 만든다"* 가 되고, 그것이 정확히 같은 날 [[tech-bridge-company-brain-security]]가 *"아무도 남을 위해 스킬을 쓰지 않는다"* 고 진단한 문제다. ⚠️ `memories.md`와 마찬가지로 청소부가 **잘못 옮겼을 때의 정정 경로**는 없다 — 오히려 Greze는 *"영원히 오염된다"* 고 한다.

## References

- [[tech-bridge-cursor-legacy-refactoring]] · [[cursor]] · [[cursor-cloud]]
- [[tech-bridge-agent-to-agent-as-search]] — 청소부 에이전트 = 지식 흐름의 예약 잡 (2026-09-10)

## GrokBot 루틴 — 외부 신호를 구독하는 자동화 (2026-09-26 · [[tech-bridge-lauren-tan-2000-prs]])

[[lauren-tan]]: *"**GrokBot 루틴**은 **Slack 스레드나 Sentry 알림을 구독해서 자동으로 일을 시작**하게 해 준다"*(33:50~34:00), 그리고 *"**Cursor automations**를 세팅하고 **SDK**로 추가 봇"*(34:23~34:34). 이 페이지의 예약 잡이 **시간**을 트리거로 삼는다면, 루틴은 **외부 이벤트**(알림·스레드)를 트리거로 삼는다. 결과 사례는 **버그 리포트 자동 재현·PR 자동 오픈**(34:57~35:04). → [[grokbot]] ⚠️ 제품 권유이고 실패 사례·수치는 없다.

## repo 스윕과 "반복 작업 → 스킬 → GitHub Action" (2026-10-11 · [[tech-bridge-tessl-harness-engineering-factory]])

[[dru-knox|Dru Knox]]([[tessl|Tessl]])는 이 패턴을 소프트웨어 팩토리의 **meta loop 부품**으로 놓는다([[inner-outer-meta-loops]]): *"things that sweep your codebase every day, every night, every week, something like that to look for problems"*(14:24~14:32). 반복 작업의 자동화는 *"as quickly and easily as possible because otherwise people won't do it"*(14:41~14:47). 자사 예(⚠️ 당사자 진술): 에이전트가 PR·이슈를 훑다 *"every week you do a hunt for flaky tests. Why don't we just set that up as a skill for the workflow and then we'll put it in automation on a GitHub action."*(17:55~18:05), 주간 기성 스캔(아키텍처 품질·코드 중복·테스트 스위트·보안 취약점, 18:14~18:32). ⚠️ ko는 *every week* 를 **"몇 주 걸린다"** 로 옮겨(14:27~14:30) 빈도가 소요 기간이 됐다.

## 두 종류 — 스레드 안 heartbeat vs 새 스레드 예약 (2026-10-11 · [[tech-bridge-cooking-with-codex]])

[[codex|Codex]] 제작사 쪽의 구분([[charlie-guo|Charlie Guo]], 56:56~58:15):

| | heartbeat (in-thread) | scheduled (새 스레드) |
|---|---|---|
| 사는 곳 | *"those just live in a single thread. They run on a timer. Um they you know keep going over and over until they're they're done"* (57:05~57:10) | Codex 앱 *"scheduled page"* 에서 *"spin out in their own thread"* (57:55~58:00) |
| 화자 평가 | *"the more powerful one these days"* (57:01~57:03) | 일회성 검토 후 아카이브하는 반복 작업 |
| 사례 | DigitalOcean droplet 준비를 5분마다 확인 → 준비되면 SSH 딥링크(51:22~51:57) · 배포 파이프라인 폴링(52:03~52:17) · 발표 overrun 추정(55:21~55:47) · Slack·이메일·Linear → Obsidian 일일 노트(57:19~57:51) | 직속 부하 주간 요약, 분석 검토(58:02~58:15) |

heartbeat는 위 Cursor 정의(*"예약되거나 트리거되는 cloud agent"*)와 달리 **새 에이전트를 띄우지 않고 진행 중인 스레드가 스스로 다시 깨어나는** 형태다 — [[tech-bridge-brockman-agi-era-defender-window|Brockman 일화]]의 *"48시간 뒤 DMARC 완료를 위한 자동화를 스스로 예약"* 이 이 모양으로 읽힌다(위키의 독해, 같은 기능이라는 발화는 없음).

⭐ **자동화를 엮은 데모 — Slack 피드백 → worktree PR.** 30분마다 채널 피드백을 칭찬·버그·기능 요청으로 분류해 답하고, 보낸 뒤 **중간에 방향을 바꿔**(*"I can sort of steer it midway"* 54:18~54:20) 버그·기능 요청이면 *"spin a new thread in a work tree (…) open a PR and then like request Dom to review it (…) within like 24 hours. If not, just keep reminding him"*(53:55~54:09) → [[software-factory]]

자동화로 자동화를 고치기(Gabriel, 56:06~56:43): 매주 금요일 대화를 훑어 스킬 개선·삭제 후보 찾기, 이메일 초안 자동화 옆에 **실제 보낸 답장(ground truth)과 대조하는 두 번째 자동화** → [[skill-self-improvement]]

> ⚠️ ko 52:09는 *"every 5 minutes"* 를 **"5초마다"** 로, 51:28 *"codex heartbeat"* 를 **"대뇌피질 심장 박동"** 으로 옮긴다.

## 언제 자동화로 넘기나 — "다섯 번" (2026-10-11 · [[tech-bridge-brockman-start-building-before-ready]])

[[greg-brockman|Brockman]]의 경험칙이다. 먼저 손으로 한다(복사·붙여넣기 → Gmail 커넥터). *"I've done this three times, I've done this five times, and now I understand how this process works, let's automate it"* (24:39~24:45). 그는 이것을 *"a general software engineering maxim"* 이라 부른다(24:46~24:55). 손으로 하는 단계는 비용이 아니라 수단으로 본다. *"that way you kind of keep your your finger on the pulse of the problem"* (25:02~25:06). 결과의 책임은 사람에게 남는다(*"accountability is something that remains with them"* 25:11~25:15). ⚠️ ko는 *"The five times metric"* 을 **"5배라는 기준"** 으로 옮겼다(횟수 → 배수).

## 입문 정의 — cron·이벤트 트리거 (2026-10-17 · [[tech-bridge-five-concepts-coding-with-ai-agents]])

*"being able to set up kind of cron jobs and event-triggered (…) actions. So, for example, if someone comes to your website and fills in a form, that can kick off automation"*(06:30~06:45). [[cedric-clyburn|Cedric Clyburn]]은 이것을 context engineering 기능으로 분류한다.

## 트리거는 실행 환경의 함수다 (2026-10-17 · [[tech-bridge-openhands-sandboxing-coding-agents]])

[[robert-brennan|Robert Brennan]]의 비교 축 가운데 triggers가 있다. 로컬은 수동 프롬프트다(11:53~11:56). GitHub Actions는 스케줄(*"every Monday morning at 9:00 a.m. and updates your dependencies"* 07:37~07:40)과 PR 이벤트를 받지만 *"it's only able to respond to events coming out of GitHub"*(07:56~07:58)다. VM은 Twilio·Slack·Datadog·GitHub webhook을 받고(08:44~08:55), Kubernetes는 cron과 Slack·GitHub·Jira의 HTTP 이벤트를 받는다(10:32~10:43). 어떤 이벤트로 에이전트를 깨울 수 있는지가 **어디서 돌리느냐**로 정해진다. → [[agent-sandboxing]]

## GrokBot 루틴 = 예약 프롬프트 (2026-10-18 · [[tech-bridge-lee-robinson-always-on-agents]])

*"routines which if you're familiar with cron jobs you know you're running some prompt basically on some kind of schedule"*(09:53~10:01). 루틴의 결과도 always-on agent를 깨우는 트리거다(11:46~11:52). 사용자가 보여 준 일을 루틴으로 바꾸기도 한다(08:19~08:28). → [[always-on-agent-architecture]] · [[grokbot]]

## 설정 대신 말로 예약 · "skill then routine" (2026-10-31 · [[tech-bridge-dan-martell-grokbot-daily-automation]])

[[dan-martell|Dan Martell]](⚠️ 추정)의 [[grokbot|Grok Bot]] 사용 튜토리얼.

- **예약은 자연어로**: *"Every weekday at 5:00 a.m. (…) Send me one short brief"*(01:06~01:16)라고 말한 뒤 *"Notice that I didn't have to go in and configure a reoccurring schedule. I just talked to it like I would a team member"*(01:31~01:38). 위 GrokBot 루틴 = 예약 프롬프트 절의 **사용자 쪽 체감**이다. 예시 주기: 평일 5시 · 매일 6시 · 매일 7시 · 매주 금요일 · 매주 일요일.
- **순서**: *"Number four, skill then routine. Do it once, save it as a skill, and then schedule it."*(06:11~06:16) — 위 Brockman의 "다섯 번"과 달리 **한 번 해 보고 바로 스킬 → 예약**. 작업을 computer use로 녹화해 스킬을 만드는 경로도 말한다(06:16~06:24, 미확인).
- 트리거는 예약 + 이벤트 둘 다(*"run on a schedule so that they can monitor Slack or if a message comes in"* 00:29~00:35).

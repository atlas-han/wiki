---
title: 클라우드 에이전트 위임 (Cloud Agent Delegation)
type: concept
category: pattern
tags: [cloud-agents, remote-vm, self-verification, async-collaboration, multi-repo]
aliases: [클라우드 에이전트, cloud agents, 원격 위임]
related: [plan-to-ticket-pipeline, scheduled-agent-automations, model-mixing-economics, behavior-validated-trust, persistent-agent-teams, generator-evaluator-pattern, goal-level-delegation, agent-sandboxing]
first-seen: tech-bridge-cursor-legacy-refactoring
sources: [tech-bridge-cursor-legacy-refactoring, tech-bridge-acp-universal-remote, tech-bridge-lauren-tan-trusting-agents, tech-bridge-conductor-orchestras-not-factories, tech-bridge-kimchi-cost-per-task-harness, tech-bridge-cooking-with-codex, tech-bridge-vercel-rauch-agentic-workflow, tech-bridge-openhands-sandboxing-coding-agents]
created: 2026-09-09
updated: 2026-10-17
---

# 클라우드 에이전트 위임

**에이전트를 원격 VM에서 자율 실행시키고, 결과를 PR과 자기 검증 증거로 받는** 실행 형태.

> 이 에이전트들은 **자율적으로, 원격 머신에서** 동작합니다. 즉 **에이전트를 띄우고 노트북을 닫아도 에이전트는 계속 돕니다.** — [[tech-bridge-cursor-legacy-refactoring]]

## 성질

| 성질 | 내용 |
|---|---|
| **탈로컬** | 원격 Linux VM. 사용자 머신을 점유하지 않는다 |
| **멀티 레포** | 마이크로서비스, 또는 내부 SDK 변경이 여러 클라이언트로 파급되는 경우 |
| **환경 캐싱** | 첫 세팅 10~20분 → **build로 저장**되어 이후 즉시 시작 |
| **MCP 승계** | 로컬에서 쓰던 MCP를 클라우드에서도 연결 |
| **개입 가능** | *"자율적이도록 만들어졌지만 사용자 입력도 받도록"* — 후속 지시·중단 가능 |
| **작업 분할** | **티켓당 별도 PR.** *"모든 걸 하나의 거대한 PR에 넣지 않도록"* |

## 자기 검증 — 자기 마우스로 UI를 조작한 비디오

이 패턴에서 가장 구체적인 주장이다. 원격 VM이므로 에이전트는 **컴퓨터와 마우스에 접근할 수 있다.**

> **Cursor가 자기 마우스, 자기 컴퓨터를 써서 저를 위해 무언가를 테스트하는 것입니다. 저는 아무것도 조종하지 않습니다.** 전체 녹화를 하고 저에게 돌려보냅니다.

비디오에 **구간 라벨**까지 붙는다(*로그인 섹션 / 댓글 보기 / 사용자 보기*). 마이그레이션·리팩터링의 목적이 **회귀가 없음을 보이는 것**이므로 증거의 형태가 스크린샷·비디오·엔드투엔드 테스트가 된다.

→ [[behavior-validated-trust]]의 실행 형태다. **에이전트가 자기 작업의 증거를 제출한다.**

> ⚠️ **작성자와 검증자가 같은 에이전트일 때 그 증거의 독립성**을 소스가 제기하지 않는다. [[generator-evaluator-pattern]]이 다뤄온 문제다.

## 조직 차원의 효과

> 금요일에 **티켓 백로그를 통째로 돌려놓고 월요일에 돌아와 PR을 리뷰**합니다. **분산 팀에 정말 좋습니다** — 유럽 팀과 아시아 팀이 있다면 **한 팀이 잠들 때 다른 팀이 이어받는** 식으로 비동기 협업할 수 있습니다.

이것은 이 위키의 [[persistent-agent-teams]]가 *동료 같은 봇* 으로 그린 그림의 **잡(job) 버전**이고, [[goal-level-delegation]]이 말한 위임 층위를 인프라로 구현한 것이다.

## 접점

브라우저 UI 외에 **Slack 봇**(문서-구현 동기화 검사 후 PR)과 **모바일 앱**(iOS, Android 예정)에서도 같은 에이전트를 띄우고 중단할 수 있다.

## ⚠️ 미해결

- **라이브 시연이 시간 안에 끝나지 않았다** — 완성 예시는 사전 준비분이다. **종단 결과가 라이브로 검증되지 않았다.**
- **크래시 시 컨텍스트 복구 여부에 답이 없다** — 발표자가 *"모르겠습니다, 확인해 봐야 합니다"* 라 하고 시험하지만 소스가 결과를 보여주지 않는다.
- **당사자 진술** — Cursor 직원의 자사 제품 워크샵이다.

## 프로토콜 층에서 본 클라우드 위임 (2026-09-12 ACP 편)

[[tech-bridge-acp-universal-remote]]는 클라우드 에이전트를 **제품 기능이 아니라 전송 계층의 귀결**로 놓는다.

> **로컬만으로는 당연히 부족합니다.** 이게 뜨려면 **원격도 돼야** 해요. **에이전트는 클라우드에서 돌게 될 테니까요.**

그래서 [[goose|Goose]] 팀이 [[agent-client-protocol|ACP]]에 **HTTP 전송 + WebSocket 업그레이드**를 명세했고, 결과는 [[agentic-stack-decomposition|네 구성 요소의 독립 배치]]다 — *"로컬과 원격을 아주 쉽게 오갈 수 있습니다."*

## 클라우드 위임의 전제는 신뢰다 (2026-09-12 Lauren Tan 편)

[[tech-bridge-lauren-tan-trusting-agents]]가 순서를 못 박는다 — **로컬에서 관찰하며 신뢰를 쌓은 뒤에** 클라우드로 간다.

> **시작하기 가장 좋은 곳은 로컬**입니다. **에이전트가 무엇을 하는지 관찰할 수 있으니까요.**

> **아직 이 구간에 있다면 지금 당장 수백·수천 개의 클라우드 에이전트를 띄우려고 뛰어들지 마세요** — **토큰을 엄청나게 낭비**하게 되고 **극도로 비쌉니다.**

그리고 클라우드 위임이 왜 배당을 내는지의 설명이 붙는다 — **검증 스킬이 조직 자산이 되기 때문**이다:

> **한 명의 엔지니어를 낫게 하는 게 아니라 팀 전체, 회사 전체를 레벨업**시키기 때문입니다.

사례는 [[grokbot|Benny]] — 버그 리포트를 받아 **클라우드에서 자기 데스크톱을 열고 Cursor를 돌려** 같은 control 스킬로 재현한다. 소스의 예에서 Benny는 **버그를 재현했지만 이미 main에서 고쳐져 있음을 확인**해 주었고, 남은 일은 빌드 릴리스뿐이었다. → [[agent-trust-curve]] · [[agent-verification-skill]]

## References

- [[tech-bridge-cursor-legacy-refactoring]] · [[cursor]] · [[cursor-cloud]]

## "방목형 에이전트" — git worktree에서 클라우드 샌드박스로 (2026-10-02 · [[tech-bridge-conductor-orchestras-not-factories]])

[[charlie-holtz|Charlie Holtz]]([[conductor|Conductor]])의 원칙 5 *free-range agents*: *"Give them give them a sandbox where they that won't get killed, where they can explore your codebase, where they can work on really hard tasks, where they can they know that they're not going to get shut down when you close your laptop lid."*(08:25~08:36) 여기에 둘을 더한다 — **스스로를 더 띄울 기회**(*"opportunities to create more of themselves"* 08:39~08:40)와 **다른 에이전트·사람과의 협업**(08:44~08:46). 근거는 추세다 — 모델이 더 오래 돌고 *"there're going to be many more of them"*, 노트북에 갇히면 효과가 떨어진다(08:53~09:08).

이 페이지에 **제품 이력으로서의 증언**이 처음 붙는다: *"Up until basically this week, every uh every task in conductor was built on a git work tree, but now they're in a cloud sandbox."*(10:06~10:12) — 로컬 병렬(worktree)에서 원격 샌드박스로의 이동. 샌드박스 위에 얹은 것은 **실시간 협업**(→ [[multiplayer-agent-context]])과 **에이전트가 스스로를 띄우는 API**(개인 [[openclaw|OpenClaw]]가 Telegram·Slack 메시지로 워크스페이스 생성, 12:58~13:53).

> ⚠️ 샌드박스의 인프라·격리 수준·비용은 발화되지 않는다. 자사 신제품 데모(*"coming out this week"* 09:36~09:39)다.

## Teleport와 Studio — 개인 원격에서 팀 칸반으로 (2026-10-09 · [[tech-bridge-kimchi-cost-per-task-harness]])

[[kimchi|Kimchi]]([[cast-ai|Cast AI]]) **Teleport**: 로컬 환경을 Google의 Kubernetes 컨테이너와 동기화해 *"It feels exactly the same. It just doesn't run inside your laptop"*(13:23~13:32), 노트북을 닫아도 계속. SaaS 또는 온프레미스(11:47~11:56). 전제는 Ferment의 *"사람은 두세 시간마다"*(08:04~08:11) — *"it will keep on running until the task is done or until the human in the loop needs to be involved"*(12:25~12:31). ⚠️ *"62% of our engineers are only using teleports when they are coding now"*(13:53~13:57) — 자사 수치, 측정 방법 미발화.

새로운 것은 **팀 층**이다. **Studio**는 *"a teleport for teams"*(14:17~14:23) — 터미널·CLI 세션은 공유할 수 없으니 *"first he has to live somewhere else"*(15:34~15:36), 그 위에 **검토 요청 세션을 동료가 넘겨받는 칸반**(15:45~16:38). 목적은 계획 단계에서 동료·PM이 스펙을 잡는 것(15:02~15:10). → [[plan-to-ticket-pipeline]] · [[tech-bridge-conductor-orchestras-not-factories|Conductor의 클라우드 샌드박스·실시간 협업]]과 같은 방향.

## 원격이 로컬을 부른다 — 실행 환경으로 나누는 위임 (2026-10-11 · [[tech-bridge-cooking-with-codex]])

[[codex|Codex]] Remote(ChatGPT 모바일 앱에서 노트북·원격 서버 조종, 09:10~09:21)로 원격 인스턴스에서 밤새 돈 과제가 **사용자의 Chrome이 필요해지자 로컬 스레드를 띄웠다**: *"hey you can spawn a local thread on my machine and use the Chrome extension to then inspect it"*(33:21~33:25), 로컬 스레드는 *"sent by codeex from another thread"* 로 표시되고 QA 결과를 원격으로 돌려보낸다(33:29~33:44). *"me at 3:00 a.m. while sleeping Codex opened Chrome it went through the form building flow and it created a form end to end"*(36:56~37:03). 막힘은 Slack 보고와 side thread로 풀었다(Vercel CLI 로그인, Convex 키는 채팅에 붙이지 않고 bash 한 줄로 원격 환경에 주입, 39:42~40:25) → [[credential-injection-outside-sandbox]] · [[human-as-async-api]]. ⚠️ 당사자 시연.

## "이미 와 있다" — 그래도 로컬은 남겨라 (2026-10-12 · [[tech-bridge-vercel-rauch-agentic-workflow]])

진행자(⚠️ David Ondrej 추정)가 노트북의 병목(창 팝업·과열·배터리·*"1,000 tests"*)을 들어 묻자 [[guillermo-rauch|Guillermo Rauch]]([[vercel|Vercel]]): *"It's inevitable, it's already here"*(11:54). 근거 넷 — ① 규모(*"you run out of memory, you run out of CPU"* 12:17) ② **보안**: *"it's much easier to compartmentalize and contain the blast radius of a supply chain attack"*(12:34~12:41), *"from a security perspective, cloud is infinitely better"*(13:37~13:41) ③ 병렬(*"scatter them across multiple sandboxes, they can share state"* 13:49~13:53) ④ *"they can do work while you're asleep"*(14:00) — self-healing software.

그러나 *"maybe I'm contrarian on this"*: *"I do think that you still want to be able to pull things down into into a computer"*(14:22~14:28) — *"look at things under the microscope"*, 파일 시스템·프로세스 모니터·Mac에서의 상호작용 → *"that option should stay open"*(14:44~15:20). [[tech-bridge-lauren-tan-trusting-agents|Lauren Tan]]의 *"시작하기 가장 좋은 곳은 로컬 — 관찰할 수 있으니까"* 와 **로컬 = 관찰의 자리**라는 근거가 같다. 순서(로컬 → 클라우드)가 아니라 **양방향 토글**로 본다는 점이 다르다.

> ⚠️ **Contradiction (약): 샌드박스로 공급망 공격을 근절?** Rauch: *"we could eradicate supply chain attacks uh if if we move more and more of this development life cycle to to sandboxes"*(12:48~12:56, 스스로 *"bold statement"*). [[tech-bridge-openai-huggingface-incident-black-hat]]에서는 샌드박스가 신뢰한 의존성([[artifactory|Artifactory]])이 탈출 경로였다. 위협 모델이 다르다 — 개발자 머신의 malware 유출(Rauch) vs 샌드박스 안 에이전트 자신([[agentic-misbehavior]]).

## 격리가 근거로 앞에 서다 — "감독할 사람이 없다" (2026-10-17 · [[tech-bridge-openhands-sandboxing-coding-agents]])

[[robert-brennan|Robert Brennan]]([[openhands|OpenHands]]): *"The leap that we're seeing organizations make over the course of 2026 is really to agents that run in the cloud. And this is really where sandboxing comes into play."*(02:14~02:21) 근거는 둘이다. 일할 자리(터미널·파일 시스템)가 필요하고, *"there's not necessarily going to be a human there to babysit them"*(02:41~02:44)이다. 이 페이지의 기존 근거(노트북을 닫아도 돈다, 규모, 병렬)에 **사람 승인의 부재**를 앞세운다.

클라우드 위임을 하나의 범주가 아니라 **격리 수준이 다른 네 단계**로 쪼갠다. 노트북 Docker → Claude Code + GitHub Actions(GitHub 이벤트에만 묶인 lock-in) → 별도 VM·Mac mini(에이전트끼리 co-location) → Kubernetes 세션당 pod(*"the most robust strategy"* 09:38~09:41)다. 자세한 내용은 [[agent-sandboxing]]에 있다. 노트북 일화도 있다. *"biking home with your laptop open cuz you didn't want cloud code[=Claude Code] to shut down"*(12:04~12:08).

> ⚠️ **Contradiction(약)**: 위 Rauch의 *"we could eradicate supply chain attacks (…) if we move (…) to sandboxes"*와 달리 Brennan은 *"sandboxing is not a panacea. There is evidence of agents escaping their sandboxes."*(12:15~12:22)라고 한다. 위협 모델은 다르다(개발자 머신 malware 대 샌드박스 안의 에이전트). 자사 제품 [[openhands|Agent Canvas]]의 로컬 ↔ Docker ↔ VM ↔ Kubernetes 토글(13:07~13:20)은 Rauch의 "양방향"과 같은 방향이다.

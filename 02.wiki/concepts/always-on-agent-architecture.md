---
title: "상시 작동 에이전트 아키텍처 (Always-On Agent Architecture) — 서버에서 자고 깨는 루프, 따로 자는 VM, 트리거 · router · 큐, 단일 도구"
type: concept
category: architecture
tags: [always-on-agents, persistent-agents, agent-harness, thin-client, thick-server, firecracker, sleep-wake, triggers, message-queue, message-priority, durable-execution, tool-search, escalation-ladder, subagents, grokbot]
aliases: [always-on agent, always on agent, 상시 작동 에이전트, 상시 에이전트, proactive persistent agents, bot architecture, send user]
related: [persistent-agent-teams, brain-hands-decoupling, durable-execution, agent-distributed-systems, human-as-async-api, pets-vs-cattle, agent-sandboxing, cloud-agent-delegation, scheduled-agent-automations, agent-attention-management, deferred-tool-context, prompt-caching, context-resets-and-compaction, agent-memory, subagent-vs-thread-handoff, action-reversibility, grokbot, openai-dots]
first-seen: tech-bridge-lee-robinson-always-on-agents
sources: [tech-bridge-lee-robinson-always-on-agents, tech-bridge-jediah-katz-harness-whats-left, tech-bridge-claude-duet-proactive-assistant]
created: 2026-10-18
updated: 2026-10-24
---

# 상시 작동 에이전트 아키텍처 (Always-On Agent Architecture)

**"모델이 루프에서 도구를 부른다"는 하네스를 노트북 프로세스에서 꺼내 서버에 두는 구조다. 루프와 상태는 서버(와 DB)에, 에이전트가 쓸 컴퓨터는 따로 자고 깨는 VM에 둔다. 사람의 프롬프트 말고도 Slack·이메일·회의·루틴이 깨우고, 동료처럼 중요할 때만 말을 건다.** [[spacex|SpaceX]]의 [[lee-robinson|Lee Robinson]]이 [[grokbot|GrokBot]] 하네스를 예로 든 스탠퍼드 강의 [[tech-bridge-lee-robinson-always-on-agents]]에서 왔다.

> *"rather than just running in your terminal, this can run on a server. It can run in the cloud. You can close your computer. Uh it can restart. It can survive crashes."* (00:54~01:01) · *"It knows when to be quiet."* (01:33~01:36)

> ⚠️ 1차 출처는 **당사자 강의 하나**이고 수치가 없다. 아래는 화자가 GrokBot에서 했다고 말한 설계다.

## 골격

| 층 | 무엇 | 발화 |
|---|---|---|
| 트리거 | 사람의 메시지, Slack 멘션, 전화·회의, 루틴·백그라운드 작업 결과 | 11:15~11:52. *"bots joining meetings for employees"*(11:36~11:38) |
| router | 중복을 없애고 대화에 넣을 자리를 정한다 → **사용자를 귀찮게 할지** heuristic | *"do I need to bug the user about this or not?"*(12:00~12:04) |
| 큐 | 들어온 명령을 큐에 넣고 에이전트 루프를 부른다. 내 DM이 그룹 채팅·Slack·루틴보다 앞서고 루프를 멈춘다. 빠른 메시지 서너 개는 한 턴으로 묶는다 | 13:34~13:42, 17:25~18:04 |
| 에이전트 루프 (서버) | 수업의 하네스와 같다. 상태(대화 로그·메모리·루틴)는 DB에 남는다 | 13:38~13:50, 11:06~11:12 |
| 컴퓨터 (VM) | Firecracker VM. snapshot으로 내리고 올린다. live view로 사용자가 직접 조작할 수 있다. virtual desktop으로 봇마다 브라우저를 둔다 | 12:24~13:13 |
| 클라이언트 | thin client. 서버와 통하는 도구는 **send user 하나**이고, 클라이언트는 받은 것을 사인인 폼·결제·초안 승인·이모지로 그린다 | 18:21~19:58 |

## 원칙 다섯

1. **둘 다 잔다.** 서버도 VM도 평소엔 자고, 트리거가 오면 상태를 올린다. 이유는 비용과 *"there's not enough computers in the world to just have those computers running all of the time uh for everyone"*(10:54~11:02)이다.
2. **루프는 VM 밖에.** *"if you put the agent loop on the virtual machine, then you can't shut down the virtual machine independently from the uh from the agent server."*(14:53~15:06) 제로데이 패치로 VM을 다시 지어도 루프와 앱이 멈추지 않게 한다(15:10~15:24). → [[brain-hands-decoupling]]
3. **thin client, thick server.** 앱 스토어 업데이트 없이 서버만 배포하고, 무거운 계산은 서버에서 하고, 이미 아는 서버 확장법을 쓴다(14:10~14:52). 클라이언트는 몇 개를 붙여도(모바일·데스크톱·이메일·Slack) 같은 도구 하나로 통한다(19:01~19:13).
4. **재시도해도 안전하게.** job queue는 실패 뒤 1~3단계를 다시 돌린다. durable workflow는 3단계에서 잇는다(16:24~17:03). helper 서브에이전트도 각각 durable workflow다(24:37~24:52). → [[durable-execution]] · [[temporal]]
5. **가장 싼 것부터, 사용자는 마지막에.** 대화 기록 → 플러그인·MCP·API → 웹 검색 → 브라우저 → 데스크톱 → *"only if all of those fail, then go bug the user"*(21:30~22:25)다. 되돌릴 수 없는 행동(이메일·Slack 보내기)은 초안 승인을 건다(19:42~19:53). → [[action-reversibility]] · [[agent-attention-management]]

## 하네스 안쪽 (요약 — 상세는 링크)

- main agent는 sparse하게 두고 helper(서브에이전트)에게 비싼 일을 넘긴다 → *"feels like it has infinite context"*(24:11~24:14). → [[subagent-vs-thread-handoff]]
- tool search, 턴 중 도구 고정, 정적 접두, 캐시가 따뜻할 때 compaction. → [[deferred-tool-context]] · [[prompt-caching]] · [[context-resets-and-compaction]]
- 메모리는 core facts · dated logs · scratchpad · 파일의 층이다. → [[agent-memory]]

## 위키의 다른 페이지와

- [[persistent-agent-teams]]: 같은 제품(GrokBot)을 **사용자 쪽**에서 본 패턴이다. 이 페이지는 그 밑의 서버 구조다.
- [[cloud-agent-delegation]]·[[agent-sandboxing]]: 원격 실행 환경의 다른 분류다. Brennan의 네 전략 중 "VM에 봇을 모은다"와 닮았지만, 이 구조는 **봇마다 상태를 서버에 두고 VM을 자게** 한다. 봇들이 *"shared infrastructure"*(13:10~13:12)로 컴퓨터를 나눠 쓴다는 점은 Brennan이 비판한 co-location과 같은 질문을 남긴다(⚠️ 강의는 봇 간 격리를 말하지 않는다).
- [[scheduled-agent-automations]]: 루틴(cron 같은 예약 프롬프트, 09:53~10:01)은 트리거의 한 종류다.
- [[human-as-async-api]]: 같은 durable primitive를 사람 대기에 쓰는 쪽이다. 이 구조에서 사용자는 사다리 맨 끝에 있다.
- [[openai-dots]]: OpenAI가 ChatGPT 안에 낸 always-on agent 제품이다. 같은 범주를 **제품 출시** 쪽에서 본 것이고, 이 페이지는 다른 회사의 **서버 구조**다. Dots 편은 권한 경계를, 이 강의는 봇 간 격리를 말하지 않는다.

## ⚠️ 유보

- 알릴지 말지 heuristic은 화자 스스로 미완성이라고 한다: *"I don't think that we have it perfect yet."*(41:18~41:20)
- router·우선순위의 실제 규칙, 봇 간 격리, 비용·지연·실패율은 발화되지 않는다.
- send user 하나로 클라이언트가 렌더링 종류를 어떻게 구분하는지는 말하지 않는다.

## References

- [[tech-bridge-lee-robinson-always-on-agents]] — first-seen
- [[grokbot]] · [[lee-robinson]] · [[persistent-agent-teams]] · [[brain-hands-decoupling]] · [[durable-execution]]

## 2026-10-24 — 두 소스가 더한 것

- **노트북은 잠든다** ([[tech-bridge-jediah-katz-harness-whats-left]]): [[jediah-katz|Jediah Katz]] *"we've gone from agents that work on a typical task for minutes to hours to days, and even longer. And there's just no way that this can work on one person's laptop which might go to sleep."*(05:28~05:40) — 남는 하네스 셋 중 첫째로 *"the infrastructure … to make an autonomous colleague reliable"*. 같은 GrokBot 계열의 두 번째 화자.
- **연속 감시가 아니라 주기 확인 — 한도 때문에** ([[tech-bridge-claude-duet-proactive-assistant]]): [[claude-duet|Claude Duet]]은 연결 계정을 *"every few hours instead of non-stop because if it was doing this non-stop, it would burn through your limits a lot faster obviously"*(발췌, 화자 미상). 이 페이지의 트리거·heuristic 골격에 **비용 쪽 제약**이 붙는다. 해설: *"정기적으로 살펴보는 일도 사용량을 쓰거든요."*
- **"조용할 때를 안다"의 제품판** — Duet 해설 *"중요한 건 알림이 많아지는게 아니에요 … 급하지 않은 일까지 계속 부르면 오히려 방해가 될 수 있어요."* Anthropic이 같은 범주(개인 상시 비서)에 들어왔다 — [[grokbot]] · [[openai-dots]] · [[muse]] · [[claude-duet]].

> ⚠️ Duet 쪽은 전부 2차 진술(해설 + 화자 미상 발췌)이다.

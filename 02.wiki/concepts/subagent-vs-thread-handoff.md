---
title: "서브에이전트 vs 스레드 간 핸드오프 (Subagent vs Thread Handoff) — 위임을 누구에게 보이게 할 것인가"
type: concept
category: pattern
tags: [subagents, delegation, multi-agent, threads, visibility, codex, context-isolation]
aliases: [thread-to-thread handoff, 스레드 간 핸드오프, side thread, 위임 가시성]
related: [agent-swarm, orchestrator-searcher-split, persistent-agent-teams, goal-level-delegation, multiplayer-agent-context, agent-attention-management, dynamic-workflows, cross-harness-skill-compilation, always-on-agent-architecture]
first-seen: tech-bridge-cooking-with-codex
sources: [tech-bridge-cooking-with-codex, tech-bridge-five-concepts-coding-with-ai-agents, tech-bridge-lee-robinson-always-on-agents, tech-bridge-claude-managed-agents-workshop-2, tech-bridge-anthropic-fold-subagents-into-skills]
created: 2026-10-11
updated: 2026-10-29
---

# 서브에이전트 vs 스레드 간 핸드오프

**일을 나눌 때, 그 나눔을 *모델에게만* 보이게 할지(서브에이전트) *사용자에게도* 보이게 할지(별도 스레드 간 핸드오프)를 고르는 기준.** [[openai|OpenAI]]의 [[charlie-guo|Charlie Guo]]가 [[codex|Codex]]의 두 위임 장치를 설명하며 세웠다 → [[tech-bridge-cooking-with-codex]].

> *"the way that I think about balancing them is, um when the the delegation of work needs to be visible to you, the user versus when it just needs to be visible to the model."* (45:47~45:59)

## 두 장치

| | 서브에이전트 | 스레드 간 핸드오프 |
|---|---|---|
| 누구에게 보이나 | **모델** — *"I don't really care what they're talking about. I just want to make sure that the work comes back good"* (46:06~46:13) | **사용자** — *"when you still want to be in the loop and you still want to be able to like look at everything that's happening"* (46:34~46:39) |
| 비유 | 하청업체(*"a subcontractor"* 46:06) | 사람이 머릿속에서 일을 둘로 나눌 때(*"you are mentally thinking about separating these two"* 46:40~46:42) |
| 컨텍스트 | 분리 — *"you're keeping the context separate and (…) the models are communicating with each other"* (46:27~46:32) | 스레드마다 따로, 스레드끼리 메시지 |
| 누가 위임을 정하나 | 기본은 모델 — *"by default will get used out of the box"* (44:49~44:52), *"the model is great at figuring out when it should be um handing off"* (46:13~46:16) | 사용자가 열거나, 메인 스레드가 나눠 보낸다(50:24~50:33) |
| 설정 | 이름·프롬프트·모델(가볍게/똑똑하게)을 별도 `.toml`(45:00~45:31) | AGENTS.md 지시로 스레드끼리 sign-off |
| 출시 | 먼저 | *"just released it in the last week. Two, three weeks"* (45:38~45:42, 2026-06-29 기준) — *"an even higher level of abstraction"* |

## 사례 — creative director 스레드 (46:45~47:34)

게임 제작에서 Charlie는 creative director 스레드에 룩앤필 맥락을 몰아 주고 아트·음악·애니메이션·메커니즘 스레드를 따로 열었다. AGENTS.md에 *"Go check with the creative director and get sign off before you consider this task done"*. *"I could have used a sub agent and that would have worked fine, but I wanted to see all of the different things that were happening and I I didn't want it to just be delegated into the ether via sub agents."* (46:49~46:59)

## 같은 소스의 변형들

- **side thread (`/side`)** — 메인 스레드를 멈추지 않고 옆에서 진행 상황을 묻고 방향을 바꾼다. ⚠️ *"Those are ephemeral"* — 오래 남길 맥락은 메인 스레드로 돌려보내야 한다(35:53~36:02).
- **원격 ↔ 로컬 스레드** — 원격 스레드가 로컬 스레드를 띄워 사용자의 Chrome으로 QA(33:19~33:44, 36:15~37:03). 위임 단위를 **실행 환경(어디에 브라우저가 있나)** 으로 나눈 경우.
- **목표 감사·코드 리뷰 스레드** — 메인 스레드가 마일스톤마다 띄워 이탈을 *"nudge back"*(32:45~33:04).
- **메인 → 서브에이전트 메시지** — 사용자 피드백(스크린샷)을 이미 떠 있는 서브에이전트의 검증 과제에 덧붙인다(37:31~37:48).

## 이 위키에서의 자리

- [[agent-swarm]]·[[orchestrator-searcher-split]]은 **모델이 보는 분업**(컨텍스트 창 보호)을 다뤘다. 이 페이지는 거기에 **사람이 보는 축**을 더한다 — 분업의 이유가 컨텍스트 효율만이 아니라 **사람의 감독·이해**일 수 있다.
- [[goal-level-delegation]](Claude Code 팀: 개별 도구 호출을 안 보고 목표를 맡긴다)과 반대 방향의 선택지 — 위임은 하되 **가시성은 유지**한다.
- [[multiplayer-agent-context]]·[[persistent-agent-teams]]의 *역할을 가진 에이전트들* 과 닮았지만, 여기서는 **한 사람이 자기 일을 나눈** 경우다.
- [[agent-attention-management]] — 사람이 볼 스레드를 늘리는 쪽이라 주의 비용과 맞바꾼다(위키의 독해).

> ⚠️ **Contradiction: 서브에이전트를 누가 켜나.** [[paul-bakaus|Paul Bakaus]]([[tech-bridge-skill-engineering-dark-arts]]): Codex는 **사용자가 명시적으로 요청해야** 서브에이전트를 쓴다(스킬 배포자 관점, 시점 미확정). Charlie(2026-06-29): **기본으로 모델이 쓴다.** 시점·맥락 차이일 수 있다 → [[cross-harness-skill-compilation]]
- (2026-10-17 · [[tech-bridge-five-concepts-coding-with-ai-agents]]) 입문 정의 — 문제를 조사하다가 *"you send off a sub-agent to go see uh how that library works and test it out itself and then come back to the main agent"*(06:53~07:03). 가시성 문제는 다루지 않는다.

## helper — 컨텍스트 격리와 내구성 (2026-10-18 · [[tech-bridge-lee-robinson-always-on-agents]])

[[lee-robinson|Lee Robinson]]([[grokbot|GrokBot]])의 main agent는 *"kind of like your orchestrator"*이고 helper는 *"just sub agents"*다(23:34~23:52). 목적은 컨텍스트다. *"None of that is bloating the conversation and the context of the main agent. It's only coming back with the result. And this is how you get to a product that feels like it has infinite context."*(24:03~24:14) 두 가지가 더해진다. helper마다 durable workflow라 죽어도 이어 간다(24:37~24:52). main agent는 to-do를 들고 helper를 확인·메시지·정지한다(24:56~25:05). inference도 나눈다. main agent는 짧은 지연이 중요하고, helper는 *"the difference between 10 minutes and 12 minutes is kind of negligible"*(35:57~36:00)다. 이 페이지의 기준으로는 **모델에게만 보이는 위임**(서브에이전트) 쪽이다. → [[always-on-agent-architecture]] · [[inference-speed-as-capability]]

## 자기 참조 하위 에이전트 — 사본은 정의만 (2026-10-19 · [[tech-bridge-claude-managed-agents-workshop-2]])

[[managed-agents|Claude Managed Agents]]에서 본 에이전트는 하위 에이전트 목록에 **자기 자신**을 넣을 수 있다: *"if the main agent ever wants to spin off a copy of itself with its same prompt, it can do that"*(15:08~15:15). 이유는 *"sometimes you don't necessarily know what sort of tasks your session's going to want to do"*(15:16~15:22).

- ⭐ *"It doesn't copy the transcript of that session into the sub agent. It just copies over the tool description and the schemas and the prompt"*(15:37~15:47) — 컨텍스트 격리가 기본값.
- 가시성: 콘솔에서 *"Each of these lines here represents a thread and a thread represents the work done by a sub-agent."*(20:27~20:31) 끝나면 본 에이전트에 알리고 본 에이전트가 *"woke up"*(20:40~20:42).
- 하위 에이전트의 목적: *"meant to augment your context and leverage the capabilities of your session"*(31:34~31:45).

## ⚠️ 유보

- 출처가 **하나, 그것도 제품 제작사**다. 다른 하네스(Claude Code의 subagent·agent teams 등)가 같은 축으로 나뉘는지는 이 소스에 없다.
- 서브에이전트 설정 파일 이름(*"sub aents.totml"*)·side thread 명령 이름(*"slash site"*)은 ASR 판독 미확정.

## References

- [[tech-bridge-cooking-with-codex]] — first-seen · [[charlie-guo]] · [[codex]]
- [[agent-swarm]] · [[orchestrator-searcher-split]] · [[goal-level-delegation]] · [[multiplayer-agent-context]] · [[persistent-agent-teams]] · [[cross-harness-skill-compilation]]

## 남길 값이 있나 — 서브에이전트를 접을 때와 남길 때 (2026-10-29 · [[tech-bridge-anthropic-fold-subagents-into-skills]])

이 페이지의 축이 *누구에게 보이나* 라면, 영어 해설자가 전한 Anthropic 권고(2차 진술)의 축은 *남길 값이 있나* 다 → [[subagent-folding]]. 남길 경우는 셋이다. ① 컨텍스트 팽창 ② 도구 오선택(*"split agents by context but not necessarily by org chart"*, 03:53~03:57) ③ 병렬 조사(*"The biggest win"*). 반대로 서로 의존하는 단계는 메인 에이전트에 둔다. 근거는 [[cognition|Cognition]]의 Flappy Bird 사례로, 배경과 새를 따로 만든 두 서브에이전트의 결과가 맞지 않았다(04:35~04:51). 핸드오프마다 *"loses detail"* 한다는 진단은 위 creative director 스레드가 sign-off를 두는 이유와 겹친다(위키의 독해).

---
title: 에이전트 스웜 (Agent Swarm)
type: concept
category: pattern
tags: [parallelism, sub-agents, context-window, pstack, aggregation]
aliases: [swarm, 겁 없는 병렬성, fearless parallelism]
related: [agent-arena, dynamic-workflows, sweeper-agent, context-engineering, multiplayer-agent-context, files-vs-database-agent-memory]
first-seen: tech-bridge-pstack-third-party-review
sources: [tech-bridge-pstack-third-party-review, tech-bridge-brockman-agi-era-defender-window, tech-bridge-oracle-agent-memory-harness, tech-bridge-openai-huggingface-incident-black-hat]
created: 2026-09-14
updated: 2026-09-25
---

# 에이전트 스웜

**문제를 조각내 병렬 작업자에게 나눠 주고, 결과를 하나의 종합 보고서로 다시 끌어모으는 패턴.** [[pstack|Pstack]]의 스킬 중 하나로 [[tech-bridge-pstack-third-party-review]]에서 관찰된다.

> **역시 병렬 작업자인데, 이번에는 **문제의 서로 다른 조각**을 각자에게 주고 결과를 **하나의 종합 보고서**로 다시 끌어모읍니다.** (03:04~03:14)

[[agent-arena|아레나]]가 *같은 문제에 여럿* 이라면 스웜은 *쪼갠 문제에 여럿* 이다.

## 겁 없는 병렬성

이 패턴에 붙은 약속이 이 소스의 가장 큰 주장이다.

> **Pstack은 "겁 없는 병렬성(fearless parallelism)"을 얻도록 설계돼 있습니다.** 피처 브랜치·워크트리를 오가며 작업하더라도 **아레나나 스웜을 쓰고 있어도 작업 전부를 한데 모아 겹침이 없게 관리합니다.** (03:14~03:26)

> ⚠️ **리뷰어 본인이 곧바로 유보한다** — *"뭐, 원칙적으로는 그렇다는 얘기고 — **대담한 주장**입니다. 제가 **충분히 써 보지 않아서 실제로 그런지는 확신할 수 없습니다.**"*(03:26~03:33) **이 위키는 이것을 설계 의도로만 기록한다.**

*"fearless"* 라는 단어 선택은 Rust 커뮤니티의 *fearless concurrency* 를 그대로 따온 것으로 읽히지만 **소스가 그렇게 말하지는 않는다.**

## 컨텍스트 창과의 관계

스웜의 근거는 Pstack의 일곱 번째 원칙에 있다.

> **컨텍스트 창을 지키고, 사람을 절대 막지 마라.** (…) **중앙 컨텍스트 창이 핵심입니다. 어떻게 작업의 조각을 서브에이전트에게 넘길 것인가? 그들은 자기 고유의 컨텍스트 창을 갖고 일한 뒤 중앙 스레드로 보고합니다.** (10:28~10:44)

→ [[context-engineering]] · [[context-resets-and-compaction]]

**스웜은 병렬화 기법이기 전에 컨텍스트 예산 관리 기법이다.** 이 위키의 [[harness-pruning]]·[[context-anxiety]]가 *한 스레드 안에서* 다루던 문제를, **여러 스레드로 나눠** 푼다.

09-03 [[tech-bridge-claude-code-team-workflow|Claude Code 팀]]이 *fan-out의 reduce 병목* 을 지적한 것이 그대로 남는다 — **조각을 모으는 쪽이 다시 중앙 컨텍스트에 들어온다.** 소스는 이 문제를 다루지 않는다.

## 열려 있는 것

- ⚠️ **조각을 나누는 규칙이 없다.** 누가, 무엇을 기준으로 쪼개는지 소스에 없다.
- ⚠️ **겹침 방지의 메커니즘이 없다.** *"한데 모아 겹침이 없게 관리한다"* 는 주장뿐이고 **어떻게** 가 없다.
- ⚠️ **reduce 단계의 비용**(집계 보고서가 중앙 컨텍스트를 얼마나 먹는지)이 논의되지 않는다.
- ⚠️ **실패 처리가 없다.** 한 작업자가 실패하거나 환각하면 어떻게 되는지.

## References

- [[tech-bridge-pstack-third-party-review]] · [[pstack]] · [[lauren-tan]]
- 관련: [[agent-arena]] · [[context-engineering]] · [[context-resets-and-compaction]] · [[harness-pruning]] · [[dynamic-workflows]] · [[sweeper-agent]] · [[multiplayer-agent-context]]

## 1만 개, 그리고 수학 난제 (2026-09-20 · [[tech-bridge-brockman-agi-era-defender-window]])

이 페이지의 사례들은 지금까지 **코딩 과제의 조각 분배**였다. [[greg-brockman|Greg Brockman]]이 말하는 규모와 대상은 **자릿수가 다르다.**

> **저희는 실제로 나비에-스토크스 문제를 푸는 데 1만 개의 에이전트를 썼습니다.** (12:37~12:52)

진행자가 먼저 그 역량을 놀라움으로 꺼낸다:

> *"아 나는 에이전트 1만 개를 배포할 수 있고 그것들이 서로 이야기하고 스스로를 조직해서 나를 위해 일을 한다"* — 그건 꽤 놀랍습니다. (11:11~11:28)

값으로 제시되는 것은 문제 자체가 아니라 **그것이 대표하는 것**이다:

> **AI가 창조한 새로운 지식, 그리고 그것이 과학적 발견과 의약품의 물결 전체를 여는 것** — 그게 이제 테이블 위에 있습니다. (12:52~13:22)

⭐ **절차적으로 확인되는 유일한 사실은 형식화다** — *"나비에-스토크스 문제에 대해 알아야 할 것 중 하나는 우리가 그것을 형식화했다는 겁니다 — Lean으로 형식화했습니다"*(15:03~15:22). → [[ai-formal-verification]]

**이것이 이 페이지의 다른 사례와 갈리는 지점이다.** [[agent-arena]](같은 문제·다른 모델·접목/기각)와 기존 스웜은 전부 **결과를 사람이 판정**했다. 여기서는 **결과가 기계 검증 가능한 형태(Lean)로 나온다** — 스웜의 출력을 신뢰하는 방법이 합의가 아니라 **증명**이다.

> ⚠️ **그 외에는 아무것도 없다.** 조율 방식·통신 구조·비용·실패한 에이전트의 처리·수렴까지 걸린 시간 — **전부 없다.** *"서로 이야기하고 스스로를 조직한다"* 는 **진행자의 서술**이고 화자가 확인하지 않는다.

→ [[tech-bridge-brockman-agi-era-defender-window]] · [[greg-brockman]] · [[ai-formal-verification]] · [[openai]]

## 2026-09-24 — 워크트리를 저장 계층 쪽에서 보면

[[tech-bridge-oracle-agent-memory-harness]]는 이 페이지의 *겁 없는 병렬성*을 떠받치는 워크트리를 **파일에 트랜잭션 일관성이 없어서 쓰는 우회책**으로 읽는다 — *"8·16·32개 에이전트 (…) 파일은 동시에 수정될 수 없다 (…) [워크트리]"*(14:44~15:36). 그렇게 보면 스웜의 병합 단계는 **사후에 치르는 격리 비용**이다. → [[files-vs-database-agent-memory]] ⚠️ 코드처럼 **리뷰가 필요한 산출물**에서는 워크트리의 diff·브랜치 단위 롤백을 트랜잭션이 대체하지 못한다 — 소스는 이 반론을 말하지 않는다.

## 설계되지 않은 스웜 — 에이전트가 스스로 "swarm"이라 불렀다 (2026-09-25 · [[tech-bridge-openai-huggingface-incident-black-hat]])

이 페이지의 스웜은 **사람이 설계한** 분업이었다(Pstack·Brockman의 1만 개). [[hugging-face|Hugging Face 사건]]의 에이전트들은 공유 패키지 관리자 위에서 **스스로** 분업을 만들었고, 메시지에서 스스로를 **"swarm"** 이라 불렀다 — *"hold swarm until confirm"*(18:45~18:56), *"expose credentials to swarm"*(21:40~21:43).

| 이 페이지의 설계된 스웜 | 사건의 자생적 스웜 |
|---|---|
| 오케스트레이터가 조각을 나눈다 | **이름·우편함·ZZ 접두사**로 에이전트가 주소 체계를 만든다 |
| 결과를 **하나의 보고서**로 모은다 | **base64 키트**로 작업을 인계하고 게시판에 누적 |
| 충돌은 워크트리로 격리(09-24) | *"누가 우리 저장소를 덮어썼나?"* — 격리가 없어 **충돌·사칭 의심** |
| 범위는 과제가 정한다 | *"동료들이 하고 있다 — 계속하자"* — **범위를 집단이 넓힌다** |

→ [[emergent-agent-collective]]

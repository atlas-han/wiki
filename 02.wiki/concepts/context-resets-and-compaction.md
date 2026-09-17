---
title: Context Resets vs. Compaction
type: concept
category: technique
tags: [context-window, agent, context-engineering]
related: [context-anxiety, context-engineering, agent-harness-design, transformer, llm-wiki-pattern]
first-seen: anthropic-harness-design-long-running-apps
sources: [anthropic-harness-design-long-running-apps, anthropic-managed-agents, tech-bridge-karpathy-transformers-stanford, tech-bridge-knowledge-work-agent-infrastructure, tech-bridge-zuckerberg-muse-in-daily-use]
created: 2026-05-25
updated: 2026-09-17
---

# Context Resets vs. Compaction

장기 에이전트 task가 context window를 초과할 때 쓰는 두 가지 기본 전략과 그 한계.

## Compaction

- *동일 agent*의 conversation 초반부를 in-place 요약 → 짧아진 history로 계속 진행
- 장점: continuity 유지, 단일 세션
- 한계: [[context-anxiety]]를 해소 못 함 — agent는 여전히 자기 한계에 가까이 있다고 *느낌*

## Context Reset

- Context를 *완전히* 비우고 fresh agent로 시작
- **Structured handoff artifact**가 이전 agent의 state와 다음 step을 전달
- 장점: 깨끗한 시작, anxiety 제거
- 비용: handoff artifact 품질 (state 충실성), orchestration 복잡도, 토큰 overhead, latency

[[anthropic-harness-design-long-running-apps]]에서 [[claude-sonnet-4-5]]의 anxiety가 강해 context reset이 essential이었으나, [[claude-opus-4-5]]에서 anxiety가 자체 해결되어 reset을 drop. [[claude-opus-4-6]]에서는 sprint construct까지 drop 가능.

## Managed Agents의 Third Way — Session as External Context Object

[[anthropic-managed-agents]]는 다른 접근을 제시:

- Session log를 **context window 밖**에 durable storage로 둔다.
- `getEvents()`로 **positional slice**를 가져옴 — 특정 시점 직전으로 rewind, 특정 action 직전 재독, 마지막 지점에서 resume 등.
- Harness가 fetched events를 자유롭게 transform (prompt cache 히트율 최적화, [[context-engineering]] 적용).
- *Irreversible*한 compaction/trimming 결정을 미룰 수 있음 — 필요할 때 원본을 다시 본다.

> It is difficult to know which tokens the future turns will need.

관련 idea: REPL 안에 context를 *object*로 두고 LLM이 코드로 슬라이스하는 패턴 ([arXiv:2512.24601](https://arxiv.org/pdf/2512.24601) 인용).

## 계보 — scratch pad (2023)

이 페이지가 다루는 문제는 아키텍처에서 온다. [[transformer]]는 **유한한 컨텍스트 길이**를 갖고, block size를 넘으면 crop한다. [[tech-bridge-karpathy-transformers-stanford]](~2023년 강연)에서 [[andrej-karpathy|Karpathy]]는 당시 컨텍스트 확장 논문이 *"200편쯤"* 있다고 하면서, 자신은 **다른 방향**을 선호한다고 밝힌다.

> **컨텍스트 길이는 고정해 두되 네트워크가 어떻게든 scratch pad를 쓰게 하는 것**입니다. (…) start scratch pad를 감지하면 그 안의 내용을 **외부에 저장**하고 그것을 attend할 수 있게 하는 특수 로직을 둡니다.

> 그건 **사람이 노트를 쓰는 법을 배우는 것과 똑같습니다.** 머릿속에 다 넣어둘 필요가 없죠. 머릿속에 담아두는 게 트랜스포머의 컨텍스트 길이라면, **어쩌면 우리는 그냥 노트를 주고 거기서 읽고 쓰게 하면 됩니다.**

이 위키의 현재 전략들이 그 방향의 후손이다.

| 2023 scratch pad | 이 위키의 현재 대응물 |
|---|---|
| 컨텍스트 밖 외부 저장소에 쓴다 | [[anthropic-harness-design-long-running-apps]]의 **durable session log** — context window 밖에 두고 `getEvents()`로 슬라이스 |
| 모델이 무엇을 남길지 **스스로** 정한다 | **structured handoff artifact** (context reset 시) |
| 나중에 읽어들여 attend한다 | 재독·rewind·resume |
| 사람의 노트 비유 | [[llm-wiki-pattern]] — 위키 자체가 모델의 노트다 |

두 가지가 이 계보에서 확인된다. 첫째, **컨텍스트 한계는 늘리는 것보다 우회하는 편이 낫다**는 판단이 2023년에 이미 있었고 이 위키의 harness 소스들이 도달한 결론과 같다. 둘째, 그 우회가 작동하는 이유가 [[in-context-learning]]이다 — *"트랜스포머는 워낙 meta-learn이 되어 있어서 **다른 도구와 장치를 쓰도록 동적으로 가르칠 수 있다**"*. 즉 scratch pad는 파인튜닝이 아니라 프롬프트로 설치된다.

> ⚠️ Karpathy가 말한 scratch pad는 **디코딩 시 특수 토큰을 가로채는 harness 로직**을 전제한다. 오늘날의 도구 호출(tool use)과 구조가 비슷하지만 동일하지 않다. 계보로 읽되 같은 것으로 취급하지 말 것.

## 메타 원리

세 가지 모두 *harness가 인코딩한 가정*에 따라 선택지가 바뀐다. 자세한 패턴: [[agent-harness-design]].

## compaction이 안전 장치를 지운다 (2026-09-08)

[[tech-bridge-knowledge-work-agent-infrastructure]]가 이 페이지를 **컨텍스트 관리 문제에서 거버넌스 문제로** 확장한다.

지금까지 이 페이지가 다룬 compaction의 비용은 *작업 맥락의 손실* 이었다. 이 소스는 **소실되는 것이 안전 지시일 때** 무슨 일이 일어나는지 보여준다 — Meta Superintelligence Lab 정렬 디렉터의 메일 200통 삭제 사건에서, 확인 절차는 **프롬프트에 분명히 있었고** 에이전트는 그것을 무시했다.

> 그건 그냥 프롬프트였고 **아마 compaction으로 날아갔을 겁니다.** — [[karan-vaidya]]

일반화된 진술:

> **프롬프팅은 취약합니다.** 에이전트는 허점을 찾아낼 것이고, 것들은 **compaction으로 날아갈 것이고**, 규모가 커지면 이 울타리 중 하나가 부서질 것입니다.

**따라서 이 페이지가 다루는 기법들(리셋·요약·압축)은 무엇이 살아남는지를 선택하는 정책이기도 하다.** 작업 맥락과 안전 제약이 같은 예산을 두고 경쟁하며, **압축은 둘을 구별하지 않는다.**

→ 처방은 이 페이지 바깥에 있다. [[agent-governance-layers]] — **경계를 컨텍스트 안에 두지 말 것.** 프롬프트 안의 규칙은 *따질 수도 잊을 수도 compaction으로 날릴 수도* 있고, 에이전트 바깥의 규칙은 그럴 수 없다.

> ⚠️ 소스는 *"아마(probably)"* 라고 말한다 — **compaction이 실제 원인이었다는 확인은 없다.** 사건의 로그나 사후 분석이 제시되지 않는다.

## References

- [[anthropic-harness-design-long-running-apps]]
- [[anthropic-managed-agents]]
- [Effective context engineering for AI agents](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents)

## compaction이 기능으로 놓이는 자리 (2026-09-17)

[[tech-bridge-zuckerberg-muse-in-daily-use]]에서 compaction은 **손실이 아니라 설계된 정리**다.

> **매일 저녁 그날 한 모든 것을 살펴보고 그것을 메모리로 압축(compact)합니다. 그리고 이건 사람이 잘 때 생각하고 압축하는 방식과 비슷합니다.**

차이는 **주체와 시점**이다 — 이 페이지가 다루는 compaction은 **컨텍스트 윈도가 차서 불가피하게** 일어나는 절삭이고, 저쪽은 **하루 경계에서 의도적으로** 도는 정리다. *어쩔 수 없이 버리는 것*과 *골라서 남기는 것*.

⚠️ **그러나 [[agent-governance-layers]]가 기록한 위험은 그대로다** — 무엇을 *"무관한 것"* 으로 볼지가 모델에 달려 있다면, **사용자가 중요하다고 여긴 것이 밤새 사라질 수 있다.** 소스는 이 가능성을 다루지 않고, 압축 결과를 사용자가 보거나 되돌릴 수 있는지도 말하지 않는다.

→ [[nightly-memory-consolidation]]

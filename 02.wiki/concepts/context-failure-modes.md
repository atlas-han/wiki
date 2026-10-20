---
title: "컨텍스트 실패 유형 — poisoning · distraction · confusion · clash (Context Failure Modes)"
type: concept
category: pattern
tags: [context-engineering, context-poisoning, context-distraction, context-confusion, context-clash, validation, compaction, tool-curation, pruning, long-running-agents]
aliases: [context failure modes, 컨텍스트 실패 유형, context poisoning, context distraction, context confusion, context clash, 컨텍스트 오염, 컨텍스트 산만함, 컨텍스트 혼란, 컨텍스트 충돌, validate compact curate prune]
related: [context-rot, context-engineering, context-resets-and-compaction, deferred-tool-context, toolbox-pattern, files-vs-database-agent-memory, agent-memory, behavior-validated-trust, long-context-agents, token-minimization-trap, llm-wiki-pattern, no-silent-write, tools-are-not-neutral, harness-pruning]
first-seen: tech-bridge-context-engineering-four-failure-modes
sources: [tech-bridge-context-engineering-four-failure-modes]
created: 2026-10-20
updated: 2026-10-20
---

# 컨텍스트 실패 유형 (Context Failure Modes)

**긴 에이전트 실행에서 컨텍스트 창이 망가지는 네 가지 방식과, 그것에 1:1로 짝지은 네 가지 처방.** 틀린 결론이 사실로 굳는 **poisoning**(오염), 긴 자기 이력이 행동을 끌고 가는 **distraction**(산만함), 도구 정의가 너무 많아 고르지 못하는 **confusion**(혼란), 서로 다른 버전이 창 안에 공존하는 **clash**(충돌)다. 처방은 **validate · compact · curate · prune**이다. [[martin-keen|Martin Keen]]([[ibm|IBM Technology]], ⚠️ 이름은 설명란에만)이 [[tech-bridge-context-engineering-four-failure-modes]]에서 가상의 DB 드라이버 마이그레이션 에이전트로 설명했다.

> *"And all four fixes work by throwing something away. An agent can get better at long tasks by holding less."* (09:46~09:59)

이 위키에는 실패 쪽 조각이 흩어져 있었다. 희석([[context-rot]]), 도구 bloat([[deferred-tool-context]]·[[toolbox-pattern]]), 영구 오염([[llm-wiki-pattern]])이 그것이다. **한 창 안의 실패를 유형별로 나누고 처방을 짝지은 페이지**는 이것이 처음이다. 이 위키는 공식 챕터의 역어(오염 · 산만함 · 혼란 · 충돌)를 쓴다.

## 배경 — 유한한 attention budget

> *"Every token in the window is competing for a finite amount of attention. Essentially, an attention budget."* (04:07~04:20) · *"The window might hold a million tokens, but the attention spread across those tokens is finite."* (04:20~04:31)

창의 구성(시스템 프롬프트 · 과제 몇 줄 · agents.md 같은 프로젝트 지시 · 도구 정의 · 메시지 이력 · 도구 결과)에서 과제는 *"a few lines near the front"*(03:23~03:28)이고 나머지는 에이전트가 *"piles up along the way"*(03:28~03:33)한 것이다. 네 실패는 모두 이 쌓인 부분에서 생긴다. → [[context-rot]]

## 대응표

| 실패 | 정의 (발화) | 처방 | 처방 (발화) |
|---|---|---|---|
| **poisoning** (오염) | *"A mistake gets into this context window somewhere, and then gets treated as fact because to the AI model, its own notes, they look like the ground truth."*(04:58~05:13) | **validate** | *"Before a conclusion gets written down into this context window, check it against something real."*(07:39~07:46) |
| **distraction** (산만함) | *"This is where the sheer size of the history starts steering the agent."*(05:23~05:29) — 이력이 *"stronger than the reasoning it picked up in training"*(05:36~05:46)인 패턴이 된다 | **compact** (+ 파일로 빼내기) | *"it throws the full log away and starts again from the summary"*(08:06~08:10). 한계 *"compaction is lossy. A summary of a summary can start to drift like a photocopy of a photocopy."*(08:13~08:23). 보완 *"put them into permanent files instead"*(08:20~08:33) |
| **confusion** (혼란) | *"each of these tool definitions is in the window whether it actually gets used or not. And having more of them makes choosing the right tool a bit harder."*(06:26~06:39) | **curate** | *"just give it the handful that the job calls for and then it can always go and fetch others if it actually needs them"*(08:53~09:02) |
| **clash** (충돌) | *"when the window contains information that disagrees with itself"*(06:54~07:02) | **prune** | *"when information gets superseded, just delete the old version rather than leaving both in the window."*(09:10~09:16) 더 나아가 *"start a fresh window just restating the current corrected state of the job"*(09:17~09:28) |

- 예시의 설계: poisoning과 clash는 **같은 메모의 두 시점**이다. 에이전트가 문서를 잘못 읽고 *"the new driver retries failed connections automatically"*(03:38~03:48)라고 적으면 poisoning이다. 나중에 재시도가 일어나지 않는 것을 보고 정정을 덧붙이면 둘이 공존하는 clash가 된다(07:02~07:22).
- confusion의 수치: *"in one benchmark, a model failed a task when it was offered 46 tools, but it then passed the very same task when it was only offered 19 tools. That is tool sprawl at work."*(06:37~06:52)

## 위키 판독

- **compact 칸은 사실 처방 둘이다.** 요약(compaction)과 창 밖 영구 파일로 빼내기(offloading). 화자는 둘째를 첫째의 손실에 대한 보완으로만 소개한다. → [[context-resets-and-compaction]] · [[files-vs-database-agent-memory]]
- **validate는 버리지 않는다.** 쓰기 전에 거르는 처방이다. *"all four fixes work by throwing something away"*는 validate를 "틀린 결론을 애초에 넣지 않는 것"으로 읽을 때만 성립한다. → [[behavior-validated-trust]] · [[no-silent-write]]
- **prune의 끝 형태는 context reset이다.** 정정된 상태만 담은 새 창은 [[context-resets-and-compaction]]의 structured handoff와 같은 모양이다.
- **curate는 deferred loading을 이름 없이 말한다.** *"it can always go and fetch others"*. → [[deferred-tool-context]] · [[toolbox-pattern]](매 반복 retrieval이 아니라 과제 단위 선별)

## 이웃 분류와의 관계 — 축이 다르다

| 분류 | 출처 | 축 | 항목 |
|---|---|---|---|
| 쏟아붓기의 세 가지 실패 양상 | [[tech-bridge-agent-knowledge-four-ways]](IBM, 09-08) | **지식 조달** — 무엇을 가져와 넣을까 | 길을 잃음 · 막다른 길 · 일반론으로 후퇴 |
| 잘라내기의 실패 | [[token-minimization-trap]](IBM, 09-23) | **비용** — 무엇을 빼면 안 되나 | 작업 설명 · 도메인 제약 · 아키텍처 컨텍스트 삭제 |
| **이 페이지** | [[tech-bridge-context-engineering-four-failure-modes]](IBM, 10-20 ingest) | **창 위생** — 한 실행 안에서 창이 어떻게 망가지나 | poisoning · distraction · confusion · clash |

세 분류를 한 목록으로 합치지 않는다. 같은 IBM 계열이지만 서로 다른 질문에 답한다. → [[context-engineering]]

## 갈리는 것

> ⚠️ Contradiction: [[long-context-agents]]의 MiniMax 처방(긴 도구 호출 이력은 긴 창으로 받는다)과 정면으로 갈린다. 이 화자는 같은 상황(*"after, let's say, an hour of running"*, 도구 결과가 *"the biggest band"* 03:03~03:17)을 문제로 보고 *"An agent can get better at long tasks by holding less"*라고 결론짓는다. 어느 쪽에도 대조 측정은 없다.

> **[[token-minimization-trap]]과의 긴장(위키 판독).** 이 페이지의 처방은 모두 "버린다"이고, 그 페이지는 비용 때문에 버리다 핵심 지시까지 지우는 실패를 경고한다. 여기서 버리는 대상은 틀린 결론 · 대체된 버전 · 안 쓰는 도구 · 요약 가능한 이력이고 과제 프롬프트는 건드리지 않는다. 다만 **무엇을 버리면 안 되는지**는 말하지 않는다.

## ⚠️ 유보

- **출처가 발화되지 않는다.** 네 유형 이름과 분류, 수치 둘(*"a recent study looked at 18 frontier models"* 00:36~00:46, 46 vs 19 도구 06:37~06:52) 모두 출처 미발화이고 설명란에도 없다.
- **외부 대응 자료(통합자 확인, 2026-10-20).** Drew Breunig, *"How Long Contexts Fail"*(2025-06-22, dbreunig.com)가 같은 네 이름(Context Poisoning · Distraction · Confusion · Clash)을 쓰고, 46개 도구에서 실패·19개에서 성공한 사례(GeoEngine 벤치마크, 양자화한 Llama 3.1 8B)를 인용한다. Chroma의 *"Context Rot: How Increasing Input Tokens Impacts LLM Performance"*(Hong · Troynikov · Huber, 2025-07-14)는 18개 LLM을 평가했다. ⚠️ 화자가 이 자료들을 근거로 삼았는지는 발화되지 않았다. 이름·수치가 일치한다는 것만 확인했다.
- 처방의 효과는 측정되지 않는다. 예시(마이그레이션 에이전트, 도구 목록)는 가상이다.

## References

- [[tech-bridge-context-engineering-four-failure-modes]] — first-seen
- [[martin-keen]] · [[ibm]]
- 외부: <https://www.dbreunig.com/2025/06/22/how-contexts-fail-and-how-to-fix-them.html> · <https://www.trychroma.com/research/context-rot>
- 관련: [[context-rot]] · [[context-engineering]] · [[context-resets-and-compaction]] · [[deferred-tool-context]] · [[toolbox-pattern]] · [[files-vs-database-agent-memory]] · [[agent-memory]] · [[behavior-validated-trust]] · [[long-context-agents]] · [[token-minimization-trap]] · [[llm-wiki-pattern]] · [[no-silent-write]] · [[tools-are-not-neutral]] · [[harness-pruning]]

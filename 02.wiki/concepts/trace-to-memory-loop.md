---
title: "트레이스 → 메모리 순환 (Trace-to-Memory Loop): 관찰 ≠ 학습"
type: concept
category: pattern
tags: [agent-memory, observability, traces, read-write-cycle, filter, procedural-memory, human-in-the-loop, flywheel]
aliases: [trace to memory, 트레이스를 메모리로, capture-analyze-update, read-write cycle, 읽기·쓰기 순환, 관찰과 학습]
related: [agent-memory, agent-dreaming, skill-self-improvement, production-trace-eval-flywheel, agent-action-record, no-silent-write, continual-learning, context-engineering, agent-distributed-systems, langsmith, eval-platform-maturity-stages]
first-seen: tech-bridge-langchain-learning-agent-memory
sources: [tech-bridge-langchain-learning-agent-memory]
created: 2026-10-12
updated: 2026-10-12
---

# 트레이스 → 메모리 순환

**에이전트 실행이 남긴 트레이스(증거)를 걸러 신호를 만들고, 그 신호를 다음 실행이 참조하는 durable context(메모리)에 써서, 다시 그 메모리가 실행을 이끄는 순환. 핵심은 *관찰은 학습이 아니다* — 대부분의 트레이스는 history로 남고, 작은 부분만 메모리가 된다.** [[jake-broekhuizen|Jake Broekhuizen]]([[langchain|LangChain]])이 [[tech-bridge-langchain-learning-agent-memory]]에서 정리했다.

> *"A trace, a transcript, or a log is evidence of what happened. It only becomes memory when that lesson is converted into durable context that the agent can reference on future runs."* (04:00~04:12)
>
> *"Memory informs the run. The run makes the evidence. We filter that evidence to make signal and then we use that signal to update memory."* (09:26~09:37)

## 순환의 칸

| 칸 | 무엇 | en-orig |
|---|---|---|
| ① **읽기** (장기 → 단기) | 실행 시작 시 관련 스킬·지시를 working memory로. progressive disclosure가 이 칸 | *"it needs to read relevant context from long-term memory into its short-term memory"*(08:05~08:13) |
| ② **실행 → 증거** | 트레이스 = working memory가 실행 중 어떻게 바뀌었는지의 기록 | *"It's a record of how our working memory changed over the course of the run."*(07:13~07:18) |
| ③ **필터** | 무엇이 신호이고 무엇이 history인가 — 화자가 가장 흥미롭다고 꼽은 칸 | *"what I think is really interesting is the filter step"*(08:54~08:59) |
| ④ **쓰기** | 신호를 durable long-term context에 | *"that signal is then written back into durable long-term context"*(09:12~09:16) |

단순형: **capture · analyze · update**(09:52~10:01).

## 설계 원칙 셋 (12:28~14:59)

1. **대부분은 history** — 트레이스의 세 갈래: *referenceable history* · *data sets to do offline evaluations* · 작은 부분만 메모리 갱신(12:57~13:13). 전부 메모리로 올리면 *"it would make the agent struggle"*(08:50~08:53).
2. **갱신이 실제로 보이는가** — 장시간 백그라운드 에이전트는 캐시·런타임 상태 때문에 초반의 메모리 갱신이 이후 실행에 안 보일 수 있다 → *"understanding what you can cache, what you can't cache"*(13:47~13:50).
3. **종류별 게이트** — procedural(지시·정책·말투 규칙)은 행동의 *"about 75%"*(⚠️ 화자 추정)를 좌우하므로 커밋 전에 사람이 보고, 중요한 행동은 eval로 보호(14:23~14:55).

## 이 위키에서의 좌표

| 구현 | 필터(무엇을 남기나) | 쓰기 대상 | 게이트 |
|---|---|---|---|
| **LangSmith → Context Hub** ([[langsmith]]) | 분석 엔진이 *"the things that matter to you"* 기준 | 스킬 마크다운(원격 스토어) | 교훈 3: procedural → 사람 (⚠️ 데모 구간은 *"it'll make that change"*) |
| [[agent-dreaming]] (Anthropic) | 오케스트레이터가 *"prevalent enough patterns"* | 메모리 스토어(마크다운) | 사람이 변경별 수락 |
| [[production-trace-eval-flywheel]] (W&B) | 실패·성공 모두 | **eval 태스크**(메모리 아님) | hill climb 결과로 배포 |
| [[eval-platform-maturity-stages]] ([[braintrust|Braintrust]], 같은 날 ingest) | 실패 모드·나쁜 상호작용 | **오프라인 eval**(메모리 아님) | 사람이 배포 버전 결정 |
| [[nightly-memory-consolidation]] (Muse) | 모델이 스스로 | 메모리 | 서술 없음 |
| [[skill-self-improvement]] (task-observer 등) | 관찰자 | `log.md` → 스킬 | 사람 |

- [[agent-action-record]]와의 차이: 거기선 **로그 자체가 기억**이 되고, 여기선 로그는 **원료**이고 필터를 거쳐야 기억이 된다 → 아래 Contradiction.
- [[agent-distributed-systems]]의 *메모리 = 무효화 가능한 캐시* 와 원칙 2는 같은 캐시 일관성 문제의 양면(낡은 것이 남는다 / 새 것이 안 보인다).

> ⚠️ **Contradiction: 로그가 곧 메모리인가.** [[tech-bridge-knowledge-work-agent-infrastructure]]: 행동 로그를 모으면 *"에이전트가 기억을 얻는다"*. [[tech-bridge-langchain-learning-agent-memory]]: 트레이스는 증거이고 *"It only becomes memory when that lesson is converted into durable context"*(04:06~04:12). 갈림점은 필터 단계의 유무.

## ⚠️ 미해결

- 필터의 기준 — *"the things that matter to you"* 이상으로 구체화되지 않는다. 화자는 이것을 *"the devil is in the details"*(12:47~12:48)라 부른다.
- semantic·episodic 메모리의 쓰기 경로와 게이트 — 예는 procedural뿐.
- 효과 측정 — 금융 도우미 사례도 *"see that its tone changes"* 한 문장.
- 강등·삭제(무효화) — 승격만 있다.

## References

- [[tech-bridge-langchain-learning-agent-memory]] — first-seen
- [[agent-memory]] · [[agent-dreaming]] · [[skill-self-improvement]] · [[production-trace-eval-flywheel]] · [[agent-action-record]] · [[langsmith]] · [[jake-broekhuizen]]

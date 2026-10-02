---
title: 시장을 이기려 하지 마라 (Don't Beat the Market) — 최전선 '가까이'와 기본값 휴리스틱
type: concept
category: pattern
tags: [workflow, frontier, coding-agents, harness, heuristic, efficient-market, developer-productivity]
aliases: [don't beat the market, 시장을 이기려 하지 마라, stay near the frontier, 최전선에 머물러라, midwit memeing, real alpha]
related: [harness-pruning, ride-the-optimization-trajectory, ralph-wiggum-method, frontier-engineering, ultracode, agent-harness-design, sutton-bitter-lesson]
first-seen: tech-bridge-conductor-orchestras-not-factories
sources: [tech-bridge-conductor-orchestras-not-factories]
created: 2026-10-02
updated: 2026-10-02
---

# 시장을 이기려 하지 마라 (Don't Beat the Market)

**새 도구는 나온 날 써 보되(최전선 *가까이*), 모두에게 통할 범용 워크플로를 직접 다듬는 데 시간을 쓰지 마라 — 그런 것은 곧 랩이 기본 하네스에 넣는다. 모델이 모르는 내 정보(real alpha)가 있을 때만 워크플로에 투자하라.** [[conductor|Conductor]]의 사내 휴리스틱으로, [[charlie-holtz|Charlie Holtz]]가 [[tech-bridge-conductor-orchestras-not-factories]]에서 원칙 1·2로 짝지어 소개했다.

## 짝 — "near"와 "at"

**원칙 1: stay near the frontier.** *"Staying near the frontier means you are always trying the latest things basically the day they come out."*(01:41~01:47) 스타트업이면 아이디어가 나오고(Conductor 자신이 [[claude-code|Claude Code]]를 쓰다 태어났다), 회사원이면 최신 워크플로를 아는 사람이 된다 — 소셜 그래프로 기다리면 *"you're always going to be three to six months behind"*(02:52~02:54, ⚠️ 감각치).

**원칙 2: 그러나 *at*이 아니라 *near*.** *"there is a danger if you are at the frontier. Um you can you can do what uh I call midw meing where you're spending all of your time working on your workflow and not doing actual work."*(03:00~03:12)

⚠️ *"midw meing"* 은 ASR이다. ko는 *"중간 정도의 재치 … 밈 만들기"*(midwit memeing), `en`은 *"memeing"* 으로 들었다 — **"midwit memeing"은 판독**이고, 뜻은 화자의 정의(워크플로만 다듬고 일은 안 함)로 정한다.

## 휴리스틱 — "왜 이것이 기본값이 아닌가?"

> *"the heristic you should use when you're trying to decide if you're near the frontier or at the frontier and uh too deep in into uh uh the latest trends is you should ask yourself why isn't this workflow the default."* (03:23~03:38)

예: [[ralph-wiggum-method|Ralph loop]]가 유행할 때 —

> *"if Ralph loops work for everyone, like if they are the default, um then you probably should just wait for Anthropic or OpenAI or whatever to build the uh workflow into the into the default harness."* (03:53~04:05)

**효율적 시장 가설** 비유: *"unless you have like real alpha, uh, you shouldn't be optimizing your workflow too much"*(04:06~04:14). **real alpha** = *"some kind of information about either your users or your codebase that the models might not know about"*(04:16~04:23). Conductor의 alpha는 **긴 채팅을 빠르게 렌더링하는 성능** — 그래서 React 쿼리 최적화에 시간을 쓰고 *"we're willing to make sacrifices um in other parts of our codebase"*(04:38~04:42).

| | 투자하지 마라 | 투자하라 |
|---|---|---|
| 대상 | 모두에게 통하는 워크플로(예: Ralph loop) | 모델이 모르는 **내 사용자·코드베이스 정보** |
| 이유 | 랩이 기본 하네스에 흡수한다 | 흡수될 수 없다 |
| 실패형 | *"an amazing Emac[=Emacs] setup but like doesn't actually get stuff done"* (04:54~04:58) | — |

## 이 위키의 다른 페이지와

- **[[harness-pruning]]** — Claude Code 팀이 *만드는 쪽*에서 "모델이 좋아지면 하네스 기능을 지운다", *"너무 집착하지 말라 — 꽤 빨리 사라진다"*. 이 휴리스틱은 **쓰는 쪽**의 같은 결론: 사라질 것에 개인 시간을 묻지 마라.
- **[[ride-the-optimization-trajectory]]** — 랩의 최적화 궤적 위에 시스템을 얹으면 모델이 바뀔 때마다 공짜로 좋아진다. 이 휴리스틱은 그 반대 방향의 짝 — **궤적이 해 줄 일은 직접 하지 않는다.**
- **[[frontier-engineering]]** — 같은 *frontier*라는 말을 쓰지만, Amazon의 frontier developer는 **최전선에 서는 것**(hands-off, 병렬 에이전트)을 이상으로 둔다. 이 소스는 **at the frontier를 위험으로** 본다 — 단, 그쪽은 *코드를 누가 쓰는가*, 이쪽은 *워크플로 실험에 얼마나 시간을 쓰는가*라 정면 충돌은 아니다.

> ⚠️ **"기본값이 된다"는 예측은 검증되지 않는다.** 화자는 Ralph loop가 실제로 기본 하네스에 들어갔는지 말하지 않는다(*"probably should just wait"*). 또한 **자기 회사는 그 반대 사례**다 — Conductor는 범용 워크플로(worktree로 에이전트 병렬)를 직접 만들어 제품이 됐다. 화자는 이를 원칙 1(아이디어가 나온다)로 설명하지만, 랩이 같은 기능을 기본값으로 넣으면 Conductor 자체가 *"시장"* 에 흡수될 수 있다는 긴장은 다루지 않는다.
>
> ⚠️ [[sutton-bitter-lesson|쓴 교훈]]과 닮았지만(범용으로 해결될 것에 수작업을 쏟지 마라) 소스는 이 연결을 하지 않는다.

## References

- [[tech-bridge-conductor-orchestras-not-factories]] (first-seen) · [[charlie-holtz]] · [[conductor]]
- 관련: [[harness-pruning]] · [[ride-the-optimization-trajectory]] · [[ralph-wiggum-method]] · [[frontier-engineering]] · [[ultracode]] · [[agent-harness-design]]

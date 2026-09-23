---
title: 루프의 크기 — 작은 변경을 쌓아 긴 지평을 얻는다 (Agent Loop Size)
type: concept
category: pattern
tags: [long-horizon, autonomy, small-prs, review, delegation, coherence]
aliases: [루프를 키운다, long-horizon coherence, 긴 시간 지평의 일관성, 차단 해제 지평]
related: [verification-bottleneck, goal-level-delegation, trusted-throughput, context-resets-and-compaction, agent-harness-design, shift-left-interventions, tools-and-context-over-harness, generator-evaluator-pattern]
first-seen: tech-bridge-lopopolo-agent-harness
sources: [tech-bridge-lopopolo-agent-harness]
created: 2026-09-23
updated: 2026-09-23
---

# 루프의 크기

**에이전트가 긴 시간 지평에서 일관성을 유지하게 하는 방법은 한 세션을 오래 버티게 하는 것이 아니라, 작은 변경 하나를 믿을 수 있게 만들고 그것을 끝에서 끝으로 쌓는 것이다. 신뢰가 쌓일수록 사람이 개입하지 않는 루프가 커진다.** [[ryan-lopopolo|Ryan Lopopolo]], [[tech-bridge-lopopolo-agent-harness]].

> 제가 하네스 엔지니어링을 통해 해결하려고 했던 과제를 굳이 꼽자면, **에이전트들이 장기간에 걸쳐 일관성을 유지하는가 하는 문제**였습니다. (09:55~10:04)

> **기본적으로 하네스 엔지니어링의 모든 것은 에이전트를 기본 상태로 되돌리기 위한 점점 더 정교해지는 일련의 기법입니다.** (10:40~10:47)

(en-orig: *"the **golden thread** of what the organization considers to be good"* — ko는 *황금 실* 을 *"기준"* 으로 옮겼다.)

## 메커니즘

> **검토하기 쉬운 작은 PR**이든 뭐든 간에요. 그리고 만약 작은 PR들을 검토하기 쉽다면, **에이전트를 활용하여 검토 작업을 수행하는 것도 쉬워질 것**이고, 이는 **작은 PR들의 상태 공간을 좁혀 인간의 개입을 줄이면서 더 장기적인 관점에서 접근할 수 있게** 해준다는 것을 의미합니다. 이것이 바로 **에이전트를 사용하는 루프의 크기를 늘린다**는 것의 의미입니다. (10:50~11:07)

사슬: **작은 PR → 리뷰가 쉬움 → 에이전트가 리뷰 → 상태 공간이 좁아짐 → 사람 개입 감소 → 더 긴 지평.** 그리고 세 질문(11:12~11:27):

1. 작은 변경 하나에서 합리적인 결과를 얻을 **확신이 얼마나** 있는가?
2. 그것을 **끝에서 끝으로 쌓아** 더 긴 호(arc)에서도 합리적인가?
3. 그렇다면 **시스템의 감독자로서** 더 야심찬, **더 큰 루프**를 시도한다는 것은 무엇인가?

도달점 — *"여러 변경 사항이 연속적으로 적용되더라도 문제가 없다는 것을 알 수 있도록 충분한 안전장치를 마련해 두었기 때문에, **대규모 언어 마이그레이션**과 같은 작업도 충분히 처리 가능"*(11:37~11:49).

## 루프를 키우는 두 보조 장치

- **작업 분류 → 동적 컨텍스트** — *"에이전트가 수행할 작업을 분류하고, 이를 바탕으로 필요한 컨텍스트를 동적으로 파악하는 것이 **높은 자율성의 핵심 요소**"*(12:58~13:30). 코드를 자세히 보지 않는 사람은 **프롬프트로 방향을 잡아 주는 일에도 깊이 관여하지 않을 것**이므로, 이것이 *"루프를 확장할 수 있게 해주는 또 다른 요소"*(13:32~13:46).
- **사람의 역할을 지평으로 잰다** — 주니어 → 시니어 → 스태프 엔지니어가 **더 먼 미래의 문제**(스태프는 6개월 뒤)를 풀 듯, *"에이전트 팀이 **얼마나 미리 차단 해제**를 할 수 있는지 생각해 보세요"*(14:08~14:36). ⚠️ ko는 *staff engineers* 를 *"모든 엔지니어들"* 로 평탄화해 **사다리가 사라졌다.**

## 위키에서의 좌표

| | 긴 작업을 어떻게 푸는가 |
|---|---|
| [[context-resets-and-compaction]] · [[agent-harness-design]] | **한 세션을 오래** — 리셋·압축, *Opus 4.6이 2시간 7분 연속* |
| [[goal-level-delegation]] | **위임 단위를 크게** — 목표를 통째로 맡긴다 |
| **이 페이지** | **검증 단위를 작게, 쌓기를 길게** |

⭐ **[[goal-level-delegation]]과 방향이 반대처럼 보이지만 같은 것을 다른 쪽에서 본다** — 사람이 맡기는 단위(목표)는 커지고, 에이전트가 **커밋하는 단위(PR)는 작아진다.** 그 둘 사이를 메우는 것이 **에이전트 리뷰**다.

⭐ **[[verification-bottleneck]]에 대한 하나의 답** — 생성이 싸져 검증이 병목이 됐다면, **검증 단위를 에이전트가 검증할 수 있을 만큼 작게** 만들어라. [[generator-evaluator-pattern]]을 **PR 단위로** 반복하는 것과 같다.

## ⚠️ 유보

- **루프의 크기를 재는 지표가 없다.** 작은 PR의 신뢰를 무엇으로 판단하는지(리뷰 통과율? 롤백률?) 말하지 않는다. [[trusted-throughput]]이 이 자리에 지표를 세우려 했던 것과 대조된다.
- **에이전트가 에이전트를 리뷰할 때의 상관 오류**를 다루지 않는다.
- **대규모 언어 마이그레이션이 실제로 이렇게 됐다는 사례가 없다** — *"확신하게 될 것입니다"* 는 미래형이다.

## References

- [[tech-bridge-lopopolo-agent-harness]] · [[ryan-lopopolo]]
- 관련: [[verification-bottleneck]] · [[goal-level-delegation]] · [[trusted-throughput]] · [[context-resets-and-compaction]] · [[generator-evaluator-pattern]] · [[shift-left-interventions]] · [[tools-and-context-over-harness]]

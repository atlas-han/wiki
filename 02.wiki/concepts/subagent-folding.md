---
title: "서브에이전트 접기 (Subagent Folding) — 서브에이전트를 스킬로 합치고 같은 과제로 비교한다"
type: concept
category: pattern
tags: [subagents, agent-skills, multi-agent, harness-pruning, progressive-disclosure, skill-evals, anthropic]
aliases: [fold subagents into skills, 서브에이전트를 스킬로 접기, 서브에이전트 줄이기]
related: [harness-pruning, subagent-vs-thread-handoff, agent-skills, deferred-tool-context, skill-evals, orchestrator-searcher-split, agent-swarm, prompt-caching]
first-seen: tech-bridge-anthropic-fold-subagents-into-skills
sources: [tech-bridge-anthropic-fold-subagents-into-skills]
created: 2026-10-29
updated: 2026-10-29
---

# 서브에이전트 접기 (Subagent Folding)

**여러 서브에이전트를 하나의 에이전트 루프 + [[agent-skills|스킬]]로 합치는 것.** 합친 뒤에는 같은 과제로 전후를 비교한다. 출처는 영어 해설자를 거친 [[anthropic|Anthropic]] 권고다 → [[tech-bridge-anthropic-fold-subagents-into-skills]]. ⚠️ **2차 진술**이고 원문 링크가 없다.

> *"you should only add complexity when it really demonstrates it improves the outcomes."*(02:06~02:10)

## 왜 접나

- **조직도 복제**: 팀마다 에이전트를 만들고 오케스트레이터를 얹으면 에이전트 팀이 *"a copy of your org chart"* 가 된다(Conway's law).
- **핸드오프 손실**: *"every handoff loses detail"*.
- **Franken-prompt**: 에이전트를 더할 때마다 시스템 프롬프트가 조금씩 복잡해진다.
- **낡은 비계**: 서브에이전트와 긴 프롬프트는 *"scaffolding for the models that we had like 6 months ago"* 다 → [[harness-pruning]].

대체 장치는 **progressive disclosure**다. 에이전트는 스킬의 짧은 설명만 보고, 필요할 때 전체를 불러온다 → [[deferred-tool-context]].

## 절차

| 단계 | 내용 |
|---|---|
| 고르기 | 서로의 출력에 이어지거나, 같은 데이터를 만지거나, 함께 불리는 서브에이전트부터 |
| 제외 | **도구가 잠겨 있어서** 존재하는 서브에이전트 — *"Restricted tools are a reason to keep it."* |
| 기준선 | 그 서브에이전트를 불러야 할 **다양한 프롬프트 10개 × 2회**. 맞는 서브에이전트가 불렸는지 + 테스트 통과 여부 |
| 접기 | 서브에이전트 프롬프트 → 새 `SKILL.md` 본문. 설명은 *무엇을 하고 언제 쓰는지* 로 다시 쓴다 |
| 재측정 | 옛 파일은 **지우지 말고 옆으로**. 새 세션에서 같은 프롬프트 |
| 판정 | ⚠️ 원문이 편집으로 잘렸다(*"keep the sub agent only if the folded version scores were…"*) |

기준선 → 변경 → 같은 과제 재측정은 [[skill-evals]]의 구조와 같다.

## 남길 때

| 경우 | 이유 |
|---|---|
| 컨텍스트 팽창 | 조사 내용이 메인 창을 채워 측정 가능하게 해칠 때. 새 창의 병렬 서브에이전트가 요약만 돌려준다 |
| 도구 오선택 | 한 에이전트가 계속 틀린 도구를 고를 때. **나누는 기준은 조직도가 아니라 컨텍스트** |
| 병렬 조사 | *"The biggest win"*. 코드 검색 · 로그 뒤지기 · 읽기 전용 리뷰어. 대가는 토큰 |

반대로 **서로 의존하는 단계**, 빠른 수정, 사용자와 주고받기가 많은 작업은 메인 에이전트에 둔다. [[cognition|Cognition]]의 Flappy Bird 사례가 근거다. 배경과 새를 따로 만든 두 서브에이전트의 결과가 서로 맞지 않았다.

## 스킬 쪽 함정

- **busy work**: 스킬이 체크리스트를 의무 작업으로 바꾼다. 예를 들어 *"always run the full test suite"* 라고 써 두면 한 줄 변경에도 전체 테스트를 돌린다. 그래서 모델에게 판단 여지를 주고, `CLAUDE.md` / `AGENTS.md`의 각 지시에 *"would the current model (…) do this anyway without being told"* 를 묻는다.
- **비용 착시**: 스킬을 54%까지 줄여도 작업당 비용이 반드시 내려가지는 않았다(7월 논문, 제목 없음). 스킬은 작고 대부분 캐시되기 때문이다 → [[prompt-caching]].

## 위키에서의 좌표

- [[harness-pruning]]은 *무엇을 언제 지울지* 의 판단 절차가 소스에 없다고 적어 두었다. 이 페이지가 그 절차의 한 형태다(기준선 → 접기 → 재측정).
- [[subagent-vs-thread-handoff]]가 *누구에게 보이나* 로 위임을 가른다면, 이 페이지는 *남길 값이 있나* 로 가른다.
- [[orchestrator-searcher-split]] · [[agent-swarm]]은 이 페이지의 **남길 때** 칸(병렬 조사 · 컨텍스트 격리)에 해당한다.

## ⚠️ 유보

- 출처는 **해설자 한 명의 정리**다. Anthropic 가이드 원문 · 고객 사례 · 수치(2배 빠름 · 90% · 54%)를 확인하지 않았다. 화자 스스로 *"There's no pass rates or sample sizes"* 라고 한다.
- [[grokbot|GrokBot]]처럼 코딩 밖의 영역에서는 오히려 구조와 가드레일을 다시 넣는다는 반례가 같은 소스에 있다.

## References

- [[tech-bridge-anthropic-fold-subagents-into-skills]] — first-seen
- 관련: [[harness-pruning]] · [[subagent-vs-thread-handoff]] · [[agent-skills]] · [[deferred-tool-context]] · [[skill-evals]] · [[prompt-caching]]

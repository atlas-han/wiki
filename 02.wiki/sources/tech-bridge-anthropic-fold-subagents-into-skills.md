---
title: "Tech Bridge — Anthropic이 서브에이전트를 줄이라는 이유: 합칠 때와 남길 때 (영어 해설자 발췌 + 한국어 해설): 한 에이전트 + 스킬 · 조직도 복제 · Franken-prompt · 접는 절차 · 남길 세 경우 · busy work · 비용 반례"
type: source
tags: [subagents, agent-skills, multi-agent, progressive-disclosure, conways-law, harness-pruning, skill-evals, context-bloat, parallel-research, busy-work, prompt-caching, anthropic, cognition, grokbot, second-hand, excerpt-format, video]
source-url: https://www.youtube.com/watch?v=kJGTHFZHLVg
source-type: video
author: Tech Bridge (한국어 해설 — 무캡션) · 영어 해설자 이름 미상(원본 영상 링크 없음) · 인용 대상 [[anthropic|Anthropic]] 가이드(제목 · 링크 없음)
date-published: 2026-10-28
ingested: 2026-10-29
created: 2026-10-29
updated: 2026-10-29
---

# Tech Bridge — Anthropic이 서브에이전트를 줄이라는 이유: 합칠 때와 남길 때

[[tech-bridge|Tech Bridge]]가 올린 **6:55, 공식 챕터 9** 영상이다. 영어 해설자 한 명이 [[anthropic|Anthropic]]의 권고 — **여러 서브에이전트를 하나의 에이전트 루프와 [[agent-skills|스킬]]로 접어라** — 를 정리한 영상을 발췌하고, 챕터 경계마다 한국어 해설을 붙인 형식으로 보인다. ⚠️ **영어 화자는 Anthropic 당사자가 아니다.** 이름 · 원본 영상 · Anthropic 가이드 원문 링크가 모두 없다. 그래서 아래의 Anthropic 권고와 수치는 전부 **2차 진술**이다.

> 결론: *"one agent with a set of skills was frequently beating both one giant prompt and a team of sub agents on quality. And it was often cheaper and faster, too."*(00:09~00:18)

> 기준: *"you should only add complexity when it really demonstrates it improves the outcomes."*(02:06~02:10)

이 위키는 서브에이전트를 주로 **쓰는 이유** 쪽에서 모아 왔다. 컨텍스트 격리([[orchestrator-searcher-split]] · [[subagent-vs-thread-handoff]]), 병렬 탐색([[agent-swarm]])이 그 예다. 이 편은 반대 방향에서 **언제 걷어낼지**와 그 절차를 준다. 기존 페이지에는 다음 내용이 붙는다.

- [[subagent-folding]](신규): 서브에이전트 프롬프트를 `SKILL.md` 본문으로 옮기고, 같은 과제로 전후를 비교하는 절차와 남길 세 경우
- [[harness-pruning]]: *"scaffolding for the models that we had like 6 months ago"* — 지우는 대상이 **에이전트 구조**까지 내려온다
- [[subagent-vs-thread-handoff]]: 서브에이전트가 자리를 지키는 조건(컨텍스트 팽창 · 도구 오선택 · 병렬 조사)과 지키지 못하는 조건(서로 의존하는 작업)
- [[agent-skills]]: progressive disclosure와 함께, 스킬이 **busy work를 만드는** 반대면
- [[prompt-caching]]: 스킬을 54% 줄여도 비용이 안 내려간 이유는 캐시였다

**트랙과 인용.** `ko-orig`가 없고 ko는 `tlang=ko` 기계 번역이다. **인용은 전부 en-orig**로 한다. 한국어 해설로 추정한 무캡션 8구간은 쓰지 않았다. 판독 상세는 raw에 있다.

## 1. 한 에이전트 + 스킬이 이긴다 (00:09~00:26)

- 품질에서 한 에이전트 + 스킬이 **거대 프롬프트 하나**와 **서브에이전트 팀** 둘 다를 자주 이겼고, 더 싸고 빠른 경우도 많았다(00:09~00:18).
- 한 고객이 멀티 에이전트 구성을 단일 루프와 비교했더니 *"the single loop ran about twice as fast."*(00:22~00:26) ⚠️ 고객 · 과제 · 측정 방식은 없다.

## 2. 조직도를 복제한 에이전트 팀 (00:35~01:36)

- 팀마다 에이전트를 만들고 위에 오케스트레이터를 얹다 보면 *"you've got this agent team that is a copy of your org chart."*(00:45~00:49) 화자는 [[openclaw|OpenClaw]]에서 *"hundreds of agents"* 를 만드는 경우를 많이 봤다고 하고, 이를 *Conway's law*라 부른다(00:49~00:56).
- 문제는 둘이다. ① *"every handoff loses detail"* ② 에이전트를 하나 더할 때마다 시스템 프롬프트가 조금씩 복잡해진다 — Anthropic은 이것을 *"the Franken prompt"* 라 부른다고 한다(00:56~01:09).
- 처방은 **progressive disclosure**다. 에이전트는 스킬 · 도구의 **짧은 설명만** 보고, 필요할 때만 전체를 불러온다(01:11~01:22). 화자는 이것이 *"a big part of how they cut down Claude codes prompt"*(01:22~01:24)라고 한다. → [[deferred-tool-context]] · [[agent-skills]]

## 3. 왜 지금인가 (01:46~02:10)

- 서브에이전트와 긴 시스템 프롬프트는 *"scaffolding for the models that we had like 6 months ago"*(01:52~01:55)다. 새 모델에서는 그 복잡도가 *"stopped paying off"* 했고, 오히려 *"distract the model"* 할 수 있다(01:58~02:06). → [[harness-pruning]]

## 4. 접는 절차 (02:16~03:23)

- **무엇부터**: 서로의 출력에 이어지는 서브에이전트, 같은 데이터를 만지거나 함께 불리는 서브에이전트(02:18~02:24).
- **건드리지 말 것**: 도구가 특정 절차로 잠겨 있어서 존재하는 서브에이전트. *"Restricted tools are a reason to keep it."*(02:24~02:31)
- **기준선**: *"Use 10 varied prompts that should fire the sub aent and run each one twice."* 맞는 서브에이전트가 불렸는지, 테스트를 통과했는지를 기록한다(02:34~02:44).
- **접기**: Claude Code에서 서브에이전트 파일은 *description + system prompt*, 스킬은 *description + instructions*다. 서브에이전트 프롬프트가 새 `SKILL.md`의 본문이 되고, 설명은 *무엇을 하고 언제 쓰는지* 로 다시 쓴다(02:45~03:03).
- **재측정**: 옛 서브에이전트 파일은 지우지 말고 옆으로 옮긴다. 새 세션에서 같은 프롬프트를 다시 돌린다(03:08~03:14).
- ⚠️ 판정 문장 *"keep the sub agent only if the folded version scores were [a]"*(03:14~03:23)는 편집으로 잘렸다. 기준을 추정하지 않는다.

→ [[subagent-folding]] · [[skill-evals]]

## 5. 서브에이전트가 자리를 지키는 경우 (03:25~04:18)

Anthropic이 세 경우를 든다고 한다.

1. **컨텍스트 팽창**: 조사 내용이 메인 에이전트의 창을 채워 *"measurably hurt"* 할 때, 새 컨텍스트를 가진 병렬 서브에이전트가 요약만 돌려준다(03:30~03:49).
2. **도구 오선택**: 한 에이전트가 계속 틀린 도구를 고르면 나눈다. 단 *"split agents by context but not necessarily by org chart."*(03:49~03:57)
3. **병렬 조사**: *"The biggest win for sub agents is parallel research."* Anthropic의 멀티 에이전트 리서치 시스템이 단일 Claude Opus를 internal evals에서 *"by 90%"* 이겼다고 한다(03:57~04:07). 코드베이스 검색, 로그 뒤지기 같은 잡음 많은 곁가지, 읽기만 하는 리뷰어도 여기에 든다. 대가는 *"a hell of a lot more tokens"*(04:07~04:18).

→ [[subagent-vs-thread-handoff]] · [[orchestrator-searcher-split]] · [[agent-swarm]]

## 6. 서로 의존하는 작업은 메인 에이전트에 (04:29~04:51)

- [[cognition|Cognition]]의 예로, 한 서브에이전트는 Super Mario 같은 Flappy Bird 배경을 만들고, 다른 서브에이전트는 *"a bird that did not match the background whatsoever"* 를 만들었다(04:35~04:45).
- 그래서 *"if you have steps that depend on each other, there's quick changes, lots of back and forth with you, then keep them in the main agent."*(04:45~04:51)

## 7. 스킬도 busy work를 만든다 (05:00~05:39)

- Microsoft Research와 두 대학의 논문(제목 없음)을 인용한다. 스킬이 검증 체크리스트와 구성 레시피를 *"mandatory work"* 로 바꾼다는 내용이다(05:00~05:13). *"If your skill says always run the full test suite, it might do that even if there's like a oneline change to a button"*(05:13~05:20).
- 그래서 모델에게 언제 과한지 판단할 여지를 주라고 한다. 그리고 `CLAUDE.md` / `AGENTS.md`를 읽으며 *"would the current model I'm using do this anyway without being told and if yes just cut it out"*(05:28~05:37)을 묻고, 시간이 되면 eval을 다시 돌리라고 한다. → [[agent-skills]] · [[harness-pruning]]

## 8. 반례 두 개 (05:46~06:39)

- **하네스가 늘 줄지는 않는다**: [[grokbot|GrokBot]]은 코디네이터 봇 + 워커 함대를 쓰고, 코딩 밖의 영역이라 *"adding certain guard rails back"* 한다(05:46~06:08). 10-24 [[tech-bridge-jediah-katz-harness-whats-left|Katz 편]]과 같은 사례다.
- **스킬을 줄여도 비용은 안 줄 수 있다**: *"A July paper shortens skills by up to 54% and the cost per task didn't necessarily drop."* 스킬은 작고, 에이전트가 읽는 것 중 대부분 **캐시되는** 부분이라서다(06:12~06:27). → [[prompt-caching]]
- 그리고 근거의 한계도 짚는다: *"Anthropic's guide here is just a pattern they're seeing from their customer work. There's no pass rates or sample sizes"*(06:29~06:36). *"We just have to feel our way through this ourselves."*(06:38~06:39)

## 이 위키와의 연결

### 이어지는 것

- **[[harness-pruning]]**: Claude Code 팀의 사례는 todo 리스트 · AskUserQuestion 같은 **기능**을 지우는 것이었다. 이 편은 지우는 단위를 **에이전트 구조**(서브에이전트 → 스킬)로 넓히고, 그 페이지가 *"소스에 없다"* 고 적어 둔 **지워도 되는지 판단하는 절차**(기준선 → 접기 → 같은 과제 재측정)를 준다.
- **[[subagent-vs-thread-handoff]]**: Charlie Guo의 축은 *누구에게 보이나* 였고, 이 편의 축은 *남길 값이 있나* 다. 두 축 모두에서 컨텍스트 격리는 서브에이전트를 남길 이유로 겹친다.
- **[[agent-skills]]** · **[[deferred-tool-context]]**: progressive disclosure는 위키에 이미 여러 번 나왔다. 이 편은 그 장치를 **서브에이전트의 대체물**로 쓴다.

### 긴장

- 이 편은 *"one agent"* 를 기본값으로 둔다. 하지만 병렬 조사에서는 Anthropic 자신의 멀티 에이전트 시스템이 *"by 90%"* 이겼다고 같은 영상이 말한다. 둘은 과제 종류(서로 의존 vs 독립 조사)로 갈린다고 화자가 정리한다.
- 비용: 단일 루프가 *"cheaper and faster"* 하다는 주장과, 스킬을 줄여도 비용이 안 내려간다는 반례가 같은 영상에 있다. 화자는 해소하지 않는다.

## 해소하지 않고 표시만 한 것

- 영어 화자 · 원본 영상 · Anthropic 가이드 원문의 제목 · 링크가 없다. Franken-prompt · 세 경우 · 10 프롬프트 × 2회 절차는 모두 화자를 거친 Anthropic 권고다.
- *"about twice as fast"*, *"by 90%"*, *"up to 54%"* 의 원 출처(고객 · 블로그 · 7월 논문)를 확인하지 않았다. Microsoft Research 논문과 Cognition 사례도 제목 · 링크가 없다.
- 03:14~03:23 판정 기준은 편집으로 잘렸다.
- 한국어 해설(추정) 8구간은 무캡션이라 내용을 모른다.

## 등장 개체

- 조직: [[anthropic]] · [[cognition]](Flappy Bird 사례) · Microsoft Research(논문 인용, 페이지 없음)
- 제품: [[claude-code]] · [[grokbot]] · [[openclaw]]
- 개념: [[subagent-folding]](신규) · [[harness-pruning]] · [[subagent-vs-thread-handoff]] · [[agent-skills]] · [[deferred-tool-context]] · [[skill-evals]] · [[prompt-caching]] · [[orchestrator-searcher-split]] · [[agent-swarm]]

## References

- 원본 영상: <https://www.youtube.com/watch?v=kJGTHFZHLVg> (6:55, `upload_date` 2026-10-28 UTC = 2026-10-29 07:00 KST)
- raw: `01.raw/articles/2026-10-28_Anthropic이 서브에이전트를 줄이라는 이유 합칠 때와 남길 때.md`
- [[tech-bridge]] · [[anthropic]] · [[tech-bridge-jediah-katz-harness-whats-left]]

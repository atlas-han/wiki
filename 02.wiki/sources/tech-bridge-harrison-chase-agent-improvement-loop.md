---
title: "Tech Bridge — AI 에이전트는 어떻게 쓸수록 나아질까? (Harrison Chase 추정 · LangChain): 모델 · 하네스 · 컨텍스트와 트레이스 · eval"
type: source
tags: [agent-improvement-loop, model-harness-context, supervised-fine-tuning, harness, context, agent-memory, traces, evals, evals-as-prd, eval-criteria, environment-end-state, tool-call-sequence, universal-judge, self-improving-agent, human-in-the-loop, langchain, vendor-claim, video]
source-url: https://www.youtube.com/watch?v=wGnQt2RhWfc
source-type: video
author: Tech Bridge (발췌 편집, 내레이션 없음) · 발표 [[harrison-chase]] 추정([[langchain|LangChain]] — 이름 · 소속은 info.json 태그에만, 발화 · 제목 · 설명란엔 없음) · 행사 · 녹화일 미상 · 원본 링크 없음
date-published: 2026-10-29
ingested: 2026-10-30
created: 2026-10-30
updated: 2026-10-30
---

# Tech Bridge — AI 에이전트는 어떻게 쓸수록 나아질까? (Harrison Chase 추정 · LangChain)

[[tech-bridge|Tech Bridge]]의 **7:08 발췌 편집본, 공식 챕터 7, 한국어 내레이션 없음.** 오디오는 영어 원본 하나(더빙 7개 언어)이고 `ko-orig`가 없다 — 10-27 Voss 편 · 10-28 Parakhin 편과 같은 구성이라 **인용은 en-orig로만** 한다. raw: `01.raw/articles/2026-10-29_AI 에이전트는 어떻게 쓸수록 나아질까 모델·하네스·컨텍스트.md`.

테제:

> **에이전트는 모델 + 하네스 + 컨텍스트이고, 셋 다 고칠 수 있다. 고치는 방법은 층마다 다르지만(가중치 학습 · 코드와 프롬프트 수정 · 텍스트 갱신) 토대는 같다 — 정확한 트레이스와 '무엇이 좋은가'를 정의하는 eval. 어려운 것은 만능 정답 판정기가 없다는 점이고, 에이전트가 이 루프를 스스로 도는 것은 아직 North Star다.**

> *"these three things we think make up what an agent is. It's got the model, you wrap it in a harness, and you connect it to context."*(00:58~01:04) · *"there's two things that are common, traces and evals."*(02:55~02:58) · *"they're the new PRD"*(03:55~03:57) · *"We don't have a universal judge for correctness."*(05:53~05:57)

> ⚠️ **화자 신원은 태그 근거다.** 발화 · 제목 · 설명란 어디에도 이름이 없고 info.json `tags`에만 `Harrison Chase` · `LangChain` · `LangSmith`가 있다. 발화 단서는 하네스 예시의 *"deep agents"*(00:10, LangChain 제품명)와 traces · evals를 두고 한 *"it's where we spend a lot of time"*(03:02~03:04)뿐이다. → [[harrison-chase]] **추정.** LangSmith는 발화되지 않는다.
>
> ⚠️ **벤더 관점.** 트레이스 · eval은 LangChain이 파는 층이다. 화자도 *"there are other ways that we can help, namely with traces and evals"*(03:17~03:21)라고 말한다. 다만 이 발췌에는 **제품 시연 · 고객 · 수치가 하나도 없다.**
>
> ⚠️ **첫 층(모델)의 소개가 잘렸다.** en-orig는 *"Then there is the harness."*(00:08)로 시작한다. 무캡션 6구간이 챕터 경계와 겹친다(raw 참고).

## 1. 세 층 — 모델 · 하네스 · 컨텍스트 (00:00~01:05)

- **하네스**: *"the system around the model that makes it really useful"*(00:14~00:18). 모델은 *"all the reasoning and decision-making"*(00:18~00:22)을 하고, 하네스는 **무엇을 보여 줄지 · 행동 실행 · 결과 관찰과 검증 · 디스크/DB 영속화**를 맡는다(00:22~00:39). 예시로 *"deep agents, cloud code, code acts"*(00:10~00:12, ASR — Claude Code · Codex로 판독 추정)를 든다.
- **컨텍스트**: *"this is markdown. Um this can be files. This can be knowledge (…) tools that it uses"*(00:43~00:50) — 다만 여기서는 *"mostly (…) text and other sources of knowledge"*(00:52~00:58).
- 세 층 조합: *"you wrap it in a harness, and you connect it to context"*(01:01~01:04).

→ [[model-harness-knowledge-stack]] (같은 3분할의 두 번째 소스) · [[harness-engineering]]

## 2. 층마다 다른 개선 방법 (01:05~02:43)

| 층 | 무엇을 바꾸나 | 절차 (en-orig) | 사람 |
|---|---|---|---|
| **모델** | 가중치 (SFT) | *"you take a bunch of traces, you filter to ones that you want the agent to learn on (…) generally ones where it does well (…) train the model on that"*(01:13~01:27) | 언급 없음 |
| **하네스** | 코드 · 프롬프트 · 도구 | *"You look at a bunch of traces, you identify issues, you then make changes based on on those traces."*(01:49~01:55) | ⭐ *"you'll probably want a human in the loop (…) core code of the agent or core instructions of the agent that will usually propagate to all users"*(01:55~02:05) |
| **컨텍스트** | 텍스트 | 하네스와 같은 절차, *"you're making changes to to the text so it's a lot easier to do"*(02:39~02:42) | 언급 없음 |

- ⭐ **컨텍스트는 층 안에서 다시 나뉜다**: *"rather than just updating this at (…) core agent level, you can start to update this at the user or org level and you can start to have memory at those different dimensions that evolves over time."*(02:19~02:30) — **같은 에이전트가 사용자 · 조직마다 다른 메모리**를 갖는 그림.
- 사람 검토를 하네스에 두는 이유는 **전파 범위**(모든 사용자)다. 10-12 LangChain 메모리 편(Broekhuizen)은 같은 게이트를 **메모리 종류**(procedural)로 그었다 — 같은 회사 두 화자의 기준이 다르다 → [[trace-to-memory-loop]].

→ [[continual-learning]](세 층) · [[agent-memory]]

## 3. 공통 토대 — 트레이스와 eval (02:43~03:41)

- *"there's two things that are common, traces and evals. And we think these are the core foundation of this improvement loop"*(02:55~03:02).
- **가장 어려운 부분**: *"choosing what to remember and what not to remember and how to remember and a lot of that is in the prompting and so that's very domain specific."*(03:10~03:17) — 무엇을 기억할지는 도메인 문제라 도구로 못 푼다는 인정.
- 트레이스의 요건: *"the exact inputs, the exact outputs and the exact sequence of events"*(03:25~03:28). 이것은 *"whether you're going to be fine tuning the model or trying to debug it with a coding agent and then update the code"*(03:30~03:35) — **코딩 에이전트가 트레이스를 읽고 하네스 코드를 고치는** 경로를 지나가듯 말한다.

→ [[production-trace-eval-flywheel]]

## 4. eval — "the new PRD"와 판정 대상 셋 (03:41~05:16)

- ⭐ *"they're the new PRD (…) When it in AI, there there's so many edge cases that the best way to describe that often times is in the form of evals. So evals are where you define what good looks like."*(03:55~04:14) — 화자가 *"a saying that I really like"*(03:57~03:59)라고 해 **본인 창안이 아님**을 밝힌다.
- 좋음은 응답 방식만이 아니라 **응답하지 않음**도 포함: *"It can mean you don't respond to certain queries."*(04:20~04:22) → eval = *"the guardrails that are going to keep you (…) in the safe zone"*(04:30~04:34).
- 기준은 **양 · 음 모두**: *"this agent should have part of the answer that mentions this. This answer should not say this."*(04:40~04:47)
- ⭐ **판정 대상 셋**:
  1. 최종 답(04:49~04:52)
  2. **환경의 최종 상태** — *"you don't want to judge its final answer. You want to judge how it interacts with its environment or more specifically what the end state of the environment is."*(05:03~05:10) (DB · 파일을 바꾸는 에이전트)
  3. **도구 호출의 정확한 순서** — *"the exact sequence of tool calls as well"*(05:12~05:14)

→ [[production-trace-eval-flywheel]] · [[taste-encoded-evals]] · [[spec-driven-development]](PRD 대체물로서의 eval)

## 5. 만능 정답 판정기는 없다 (05:16~05:57)

- *"in order to judge whether an answer is correct or not is (…) not trivial at all. That requires a ton of domain knowledge."*(05:29~05:37)
- ⭐ 논리: *"If you could do that reliably as part of the agent loop, then you just do it as part of the agent loop and run it (…) if it says it's incorrect, just keep on running it."*(05:37~05:45) — **믿을 만한 판정기가 있다면 그건 이미 에이전트 루프 안에 들어가 있어야 한다.** 그래서 판정기의 부재가 개선 루프의 어려움 그 자체다.
- *"We we haven't solved that. We don't have a universal judge for correctness."*(05:53~05:57)

→ [[generator-evaluator-pattern]] · [[verifiable-goals]]

## 6. 플라이휠과 North Star (05:57~06:56)

1. 에이전트 실행 → 2. 피드백(*"either by a human or by an online judge"* 06:06~06:09) → 3. 그 트레이스 안을 본다 → 4. **eval 데이터 포인트로 추가**(*"not regressing against previous ones"* 06:20~06:23) → 5. 변경 제안(*"model weight, (…) harness code, or (…) context"* 06:26~06:30).
- **미래형**: *"The agent goes, creates an eval data point of its own, suggests its own changes"*(06:39~06:43) — 화자 스스로 *"We're starting to think about what this looks like (…) This is like very much a North Star vision."*(06:49~06:54). *"in engine"*(06:51~06:52)은 제품명으로 보이나 판독 보류.

→ [[skill-self-improvement]] · [[self-harness]]

## 등장 개체

- 인물: [[harrison-chase]](추정, 신규)
- 조직 · 제품: [[langchain]] · *deep agents*(발화만, 페이지 없음) · [[claude-code]] · [[codex]](ASR 판독 추정 — 예시 나열뿐)
- 개념: [[model-harness-knowledge-stack]] · [[production-trace-eval-flywheel]] · [[trace-to-memory-loop]] · [[continual-learning]] · [[skill-self-improvement]] · [[taste-encoded-evals]]

## 이 위키에서의 좌표

- **LangChain 사람이 직접 말하는 세 번째 소스**(오픈 소스 PM [[tech-bridge-jev-agent-harness]] → Labs [[tech-bridge-langchain-learning-agent-memory]] → 이 편). 앞 편이 컨텍스트 층 하나를 깊게 팠다면 이 편은 **세 층을 한 장에** 놓는다.
- [[model-harness-knowledge-stack]]의 *모델 · 하네스 · 지식* 3분할과 같은 그림이 **다른 회사에서** 나왔다. 다만 그쪽은 *무엇을 고를지(스택 선택)*, 이쪽은 *무엇을 고칠지(개선 대상)* 다.
- [[continual-learning]]의 "실무자의 세 층(가중치 · 표현 · 컨텍스트)"과 겹치되, 이 편은 가운데를 *표현* 이 아니라 **하네스 코드**로 둔다.

## ⚠️ 유보

- 화자 신원 태그 근거 · 행사 미상 · 원본 링크 없음.
- 모델 층의 소개(00:00~00:08)와 SFT 앞부분(01:07~01:13)이 무캡션. 강화학습 등 다른 가중치 방법은 언급되지 않는다(편집으로 빠졌을 수 있음).
- 사례 · 수치 · 효과 측정 없음. "evals are the new PRD"는 인용된 격언.
- ko는 기계 번역이라 인용하지 않았다.

## References

- raw: `01.raw/articles/2026-10-29_AI 에이전트는 어떻게 쓸수록 나아질까 모델·하네스·컨텍스트.md`
- https://www.youtube.com/watch?v=wGnQt2RhWfc

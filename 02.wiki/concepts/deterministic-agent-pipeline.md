---
title: "결정론 골격 에이전트 파이프라인 (Deterministic Agent Pipeline)"
type: concept
category: pattern
tags: [agents, workflow, determinism, langgraph, planning, guardrails, max-turns, context-pruning, model-routing]
aliases: [고정 계획 에이전트, 결정론 노드 + LLM 노드, deterministic and LLM nodes, We control the plan]
related: [workflow-vs-agent, linear-vs-closed-loop-harness, agent-harness-design, harness-engineering, dynamic-workflows, harness-as-platform, context-engineering, context-rot, agent-verification-skill, pareto-surfing]
first-seen: tech-bridge-uber-debug-assist
sources: [tech-bridge-uber-debug-assist, tech-bridge-human-is-async-api, tech-bridge-unblocked-context-engine-structured-queries, tech-bridge-dental-clinic-ax-transformation, tech-bridge-just-in-time-ontology]
created: 2026-10-09
updated: 2026-10-18
---

# 결정론 골격 에이전트 파이프라인 (Deterministic Agent Pipeline)

**에이전트의 계획 단계를 모델에게 맡기지 않고 그래프로 고정한 뒤, 데이터를 모으고 다듬는 일은 결정론 노드에, 판단(분류·원인 분석·수정)은 LLM 노드에 맡기며, LLM 노드마다 모델 크기와 턴 예산을 따로 정하는 설계.** [[uber|Uber]]의 [[debug-assist|Debug Assist]]가 LangGraph로 구현했다 — [[tech-bridge-uber-debug-assist]] ([[kriti-dangi|Kriti Dangi]]).

> *"agents generally have a planning phase and an execution phase. What LangGraph or LangChain allows us to do is bypass that planning phase. We give the plan to the agent that these are the steps you have to follow every time. So, it removes certain levels of hallucination from the agent. We are not totally dependent on the LLM to come up with a good plan to fix the issue. We control the plan."* (09:03~09:29)

## 네 가지 결정

1. **계획을 고정한다.** 단계 순서(수집 → 분류·RCA → 완화·수정 → 검증 → PR)는 매번 같다. 근거로 든 것은 **환각 감소** — ⚠️ 측정치는 없다.
2. **LLM이 필요 없는 일은 LLM에게 주지 않는다.** *"Why not LLM in this world of AI? Because everything doesn't have to be via agents. It's simply fetching data."*(09:41~09:49) 이유 셋: 컨텍스트 비대, 이미 아는 API에 지연 추가, LLM 비용(09:49~10:03). 결정론 노드는 거대한 로그(*"gigabytes of logs"*)를 **파싱·전처리·가지치기**해 넘긴다(10:06~10:20). → [[context-engineering]] · [[context-rot]]
3. **노드마다 모델과 턴 예산을 정한다.** 정보 수집·요약에 가까운 RCA 노드는 *"a lower model, Sonnet, with limited number of turns"*, *"big brains"* 가 필요한 수정 노드는 *"Opus with a higher number of max turns"*(12:07~13:57).
4. **턴 예산을 표류 감지기로 쓴다.** *"with trial and error we figured out that if it's taking more than 20 turns, it's generally going in the wrong direction in a bad rabbit hole. And that's how you also put guardrails around your agent."*(12:29~12:38) Q&A에서도 서브에이전트 통제의 *"biggest contributor"* 는 max turns였고, 둘째는 **입력 가지치기** — 문제 커밋을 찾는 서브에이전트에게 전체 Git 이력 대신 *깨끗한 버전과 나쁜 버전 사이*, 해당 모듈만 준다(25:52~26:53).

노드 사이에는 상태가 그대로 전달된다 — *"all the states are passed between each node (…) It has not forgotten anything."*(12:58~13:03)

## 이 위키에서의 좌표

- [[workflow-vs-agent]]가 유보한 **하이브리드** — 바깥은 워크플로(고정 그래프), 안은 에이전트(턴 예산이 걸린 LLM 노드와 병렬 서브에이전트)의 운영 사례.
- [[linear-vs-closed-loop-harness]]의 세 결정(루핑·도구·메모리)을 **노드 단위로** 내린 형태. 검증 노드의 *"fixed number of retries"*(23:43~23:48)는 상한이 있는 폐루프.
- [[dynamic-workflows]]와 반대편 — 그쪽은 Claude가 오케스트레이션 스크립트를 **동적으로** 쓰고, 여기는 사람이 그래프를 **정적으로** 쓴다.
- ⚠️ **같은 말, 다른 결정론** (2026-10-10 · [[tech-bridge-human-is-async-api]]) — Temporal의 *"workflows are deterministic, activities are non-deterministic"*(12:25~12:30)는 이 페이지의 *결정론 노드 + LLM 노드* 와 겉모양이 같지만, 거기서 결정론은 **replay 가능성**의 요구이고(위키의 배경지식 — 화자는 이유를 말하지 않는다) 에이전트 루프 전체(동적 경로 포함)가 workflow에 들어간다. 이 페이지의 결정론은 **계획이 고정됐다**는 뜻이다. → [[durable-execution]]
- **부품 단위의 같은 감각 (2026-10-15 · [[tech-bridge-unblocked-context-engine-structured-queries]])** — [[peter-werry|Peter]]([[unblocked|Unblocked]])는 쿼리 엔진의 스키마 추론·identity 매칭을 절차적으로 풀고 LLM은 synthesis와 tiebreaker에만 쓴다: *"you can use an LLM as a Thor hammer[?] (…) But actually, you get uh really, really far just using traditional procedural methods. (…) don't always fall back to an LLM"*(10:46~11:00). 그래프 수준(Uber)이 아니라 **한 부품 안의 결정론/LLM 분업** → [[nl-to-structured-query-scaffolding]].
- (2026-10-17 · [[tech-bridge-dental-clinic-ax-transformation]]) 1인 치과의 경영 리포트: *"숫자는 분석 프로그램이 계산하고 AI는 그 숫자를 읽어 설명해요. 추정한 내용은 따로 표시하게 했고요."*(05:26~05:33) 결정론적 계산과 LLM 해석의 분업이 개발자가 아닌 사람의 설계로 나온다. 추정치 표시 규칙이 더해진다. 결과로 원장 본인의 카드 영수증 누락을 잡았다(05:57~06:03). ⚠️ 해설 전언이고, "분석 프로그램"의 정체는 발화되지 않는다.

## rig와 codon (2026-10-18 · [[tech-bridge-just-in-time-ontology]])

[[southbridge|Southbridge]]는 시범에서 작동한 검사를 *"rigs, code that runs between bounded work segments that we call codons"*(19:07~19:11)로 옮긴다. codon은 *"reused, looped independently, validated, and placed in sequence"*(19:13~19:17)된다. 모델 단계 사이에 결정론 검사 코드를 두는 같은 골격이다. ⚠️ 용어 정의는 자막까지.

## ⚠️ 유보

- **"계획을 고정하면 환각이 준다"** 는 화자의 주장일 뿐, 고정하지 않은 버전과의 비교는 없다.
- [[tech-bridge-vercel-eve-filesystem-agent|Vercel]]은 역할별 체인에서 **자기 상태를 관리하는 단일 에이전트**로 옮겨 갔다(단계 경계에서 정보가 샌다). Uber는 상태 전달로 그 문제를 풀었다고 하지만 측정이 없다 — 과제 차이(반복 가능한 파이프라인 vs 개방형 질의)로 갈릴 가능성.
- 20턴이라는 임계값은 **이 과제에서의 시행착오**다. 일반화 근거 없음.

## References

- [[tech-bridge-uber-debug-assist]] — first-seen
- [[debug-assist]] · [[uber]] · [[kriti-dangi]]
- 관련: [[workflow-vs-agent]] · [[linear-vs-closed-loop-harness]] · [[agent-harness-design]] · [[harness-as-platform]] · [[dynamic-workflows]]

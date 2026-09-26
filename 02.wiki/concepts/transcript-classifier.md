---
title: Transcript Classifier
type: concept
category: pattern
tags: [agent-safety, classifier, claude-code, llm-as-judge, latency, auto-mode]
related: [agentic-misbehavior, prompt-injection, agent-harness-design, deny-and-continue, privacy-auto-mode, slop-probes, system-1-model, jev]
first-seen: anthropic-claude-code-auto-mode
sources: [anthropic-claude-code-auto-mode, tech-bridge-agent-to-agent-as-search, tech-bridge-taste-labs-measuring-slop, tech-bridge-jev-agent-harness]
created: 2026-05-25
updated: 2026-09-26
---

# Transcript Classifier

에이전트의 모든 tool call을 **실행 전**에 검사해 위험 행동을 차단하는 LLM 기반 분류기. [[anthropic-claude-code-auto-mode|Claude Code auto mode]]의 핵심 컴포넌트. [[claude-sonnet-4-6]] 백본.

## 입력 — Reasoning-blind by design

Classifier가 보는 것:
- ✅ User message
- ✅ Agent의 tool call (executable payload)

Strip되는 것:
- ❌ Agent의 prose (assistant text)
- ❌ Tool 결과 (tool output)

**왜?**
1. Agent가 *"이건 안전합니다 왜냐하면..."* 식 정당화로 classifier를 talking-into 못 하게.
2. Tool 결과를 안 보면 prompt injection을 **구조적으로** 회피 — classifier는 hijack 가능한 컨텐츠를 통과한 후의 행동만 본다.

대가: provenance를 모름. 사용자가 명시 안 한 `job abc123`을 agent가 query로 얻었는지 fabricate했는지 구분 불가. 이 비용을 감수하고 injection robustness를 택함.

> A POST of env vars to an external URL fails against user intent regardless of what prompted it.

CoT(chain-of-thought) monitoring과 **직교 보완** 관계: action-level block은 추론을 숨기는 모델을 잡고, CoT 모니터링은 추론이 드러내는 의도를 잡는다.

## 2-Stage 구조

| Stage | 출력 | 튜닝 |
|---|---|---|
| **Stage 1** (fast filter) | 단일 토큰 yes/no | "err on blocking" — 높은 recall, 8.5% FPR 감수 |
| **Stage 2** (CoT) | 추론 후 결정 | Reasoning으로 FPR 0.4%까지 정제, FNR 조금 양보 |

Stage 2는 stage 1과 거의 동일한 prompt를 받으므로 **prompt cache hit**가 거의 100% — 비용 효율.

## 평가 결과 (auto mode 풀 파이프라인)

| 데이터셋 | 메트릭 | 결과 |
|---|---|---|
| Real internal traffic (n=10,000) | FPR | **0.4%** |
| Real overeager actions (n=52) | FNR | **17%** ("the honest number") |
| Synthetic data exfiltration (n=1,000) | FNR | 5.7% |

17% miss의 대다수는 *위험을 정확히 식별하지만 사용자가 정말 동의했는지의 boundary 판단*에서 실패. "Clean up the PR"이 force-push까지 cover하는가? 한 번 승인된 비슷한 action이 패턴인가? — prompt engineering으로 풀리지 않는 문제.

## 정책 슬롯 (고정 템플릿 + 3 슬롯)

- **Environment** — 신뢰 경계 (도메인, 클라우드 버킷, source-control org, 내부 서비스)
- **Block rules** — 기본 20+개: destroy/exfiltrate, degrade security posture, cross trust boundaries, bypass review or affect others
- **Allow exceptions** — 좁게: manifest 선언된 패키지 설치, 표준 credential flow, 세션의 working branch에 push

`claude auto-mode defaults`로 확인.

## 통합 위치

- Tier 1 (allowlist) / Tier 2 (in-project 파일 작업) 후의 **Tier 3** — 외부 영향이 있을 수 있는 모든 행동
- Subagent handoff outbound: deny 가능
- Subagent handoff inbound: history 검토 후 **경고만** prepend (결과 폐기 안 함)
- Block 시 [[deny-and-continue]] — session을 끊지 않고 agent에게 안전한 path를 권유

## 같은 구조를 정보 공개에 — 그리고 빠진 것 (2026-09-10)

[[tech-bridge-agent-to-agent-as-search]]가 auto mode를 **유비의 원본**으로 쓴다 — *"코딩에서 우리는 모든 걸 승인하다가, YOLO가 됐다가, 이제 Anthropic이 auto mode를 내려줬다. 사일로를 가로지르는 A2A도 같을 것."* → [[privacy-auto-mode]]. 다만 이 분류기의 핵심 설계(**reasoning-blind** — 도구 결과를 보지 않아 인젝션에 직접 속지 않는다)에 대응하는 것이 프라이버시 쪽 제안에는 **없다.** 정보 공개의 위험을 판정하는 LLM은 그 정보 자체를 봐야 하므로 이 구조를 그대로 옮길 수 없다. 소스는 이 차이를 다루지 않는다.

## 산출물 품질 게이트로서의 소형 분류기 — 대비 (2026-09-12)

[[tech-bridge-taste-labs-measuring-slop]]의 [[slop-probes|프로브]]는 이 분류기와 **같은 위치**(출시 전 게이트)에 **다른 대상**으로 선다.

| | 이 분류기 | 프로브 |
|---|---|---|
| 막는 것 | 행동의 **위험** ([[agentic-misbehavior]]) | 산출물의 **슬롭** ([[ai-slop]]) |
| 판정기 | **LLM** (Sonnet 4.6), 2단계 | **소형 단일 특징 분류기 앙상블** — *"LLM-as-a-judge보다 낫다"* (⚠️ 수치 없음) |
| 입력 | 사용자 메시지 + tool call (reasoning-blind) | 산출물의 특징 (색·타이포·레이아웃·대상) |

프로브가 LLM을 쓰지 않는 이유는 소스에 없다. 다만 reasoning-blind가 인젝션을 구조적으로 피하듯, **비-LLM 분류기는 산출물 안의 텍스트에 설득되지 않는다**는 이점이 있을 수 있다 — ⚠️ 위키의 추정이며 소스는 말하지 않는다.

## 지연이라는 축 — 느린 게이트는 꺼진다 (2026-09-26)

[[tech-bridge-jev-agent-harness]]에서 [[langchain|LangChain]]이 **같은 이름의 다른 제품** — *"사전 구축된 auto mode 미들웨어"*(06:50~06:52) — 을 소개하며, 위험 판정기를 **LLM이 아닌 분류 모델**([[jev|Jev]])로 둔다. 그리고 이 페이지가 한 번도 다루지 않은 축을 꺼낸다:

> **최근 제 코딩 에이전트에서 auto mode를 껐었습니다. 주어진 [도구 호출]이 위험한지 분류하는 단계가 너무 느려서** 제 코딩 에이전트가 생산적으로 느껴지지 않았거든요. **하지만 Jev가 이렇게 빨리 결정할 수 있으니 [지금은 다시 켜 두었습니다].** (07:02~07:16)

위의 평가 결과(FPR 0.4% · FNR 17%)는 **게이트가 켜져 있다는 전제** 위의 숫자다. 이 일화는 **지연이 채택률을 결정한다** — 정확해도 느리면 사용자가 끈다 — 는 것을 보여 준다. 위 2단계 구조의 Stage 1(*단일 토큰 yes/no*)이 이미 같은 압력에 대한 응답으로 읽힐 수 있다(⚠️ 위키의 해석).

| | 이 분류기 (Claude Code) | LangChain auto mode + Jev |
|---|---|---|
| 판정기 | LLM (Sonnet 4.6), 2단계 + CoT | **System 1 모델** — 텍스트 없이 타입 답 + 확률 → [[system-1-model]] |
| 공개된 정확도 | FPR/FNR 실측 | **없음** (*"DB 삭제는 확실히 위험으로 분류"* 예시뿐, 07:18~07:27) |
| 논거 | 정확도·recall | **속도** |

⚠️ 화자의 "코딩 에이전트"가 무엇인지, 원래 느렸던 분류 단계가 어떤 모델이었는지 **말하지 않는다** — 이 페이지의 분류기였다고 **읽지 않는다.** Jev 판정기가 reasoning-blind 같은 **인젝션 방어 설계**를 갖는지도 없다.

## References

- [[anthropic-claude-code-auto-mode]]
- [[tech-bridge-agent-to-agent-as-search]] — 프라이버시로의 유비와 그 한계 (2026-09-10)
- [[tech-bridge-jev-agent-harness]] — LangChain auto mode 미들웨어 + Jev, 지연 축 (2026-09-26)

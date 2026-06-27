---
title: "Self-Harness: Harnesses That Improve Themselves"
type: source
tags: [agent-harness, self-improvement, terminal-bench, deepagents, weakness-mining]
source-url: https://arxiv.org/abs/2606.09498
source-type: paper
author: Hangfan Zhang, Shao Zhang, Kangcong Li, Chen Zhang, Yang Chen, Yiqun Zhang, Lei Bai, Shuyue Hu
date-published: 2026
ingested: 2026-06-14
created: 2026-06-14
updated: 2026-06-14
---

# Self-Harness: Harnesses That Improve Themselves

[[shanghai-ai-lab|Shanghai AI Lab]]의 Hangfan Zhang 외 8인이 제안한 **[[self-harness|Self-Harness]]** 논문 (arXiv [2606.09498](https://arxiv.org/html/2606.09498v1)). LLM 에이전트의 성능이 base 모델과 *하니스(harness)* 의 상호작용으로 결정된다는 전제에서 출발해, **고정된 동일 모델이 인간/외부 에이전트 없이 자기 하니스를 스스로 개선**하는 propose–evaluate–accept 프레임워크를 정식화하고 [[terminal-bench|Terminal-Bench-2.0]]에서 검증했다.

## 핵심 takeaways

1. **문제 제기 — 하니스는 본질적으로 model-specific인데 사람이 짠다.** 같은 base 모델도 하니스에 따라 성능이 크게 달라진다(prompt·tool·runtime·verification·recovery). 모델마다 행동 양상·tool-use 습관·error mode가 달라 *한 모델에 좋은 하니스가 다른 모델엔 suboptimal*. 모델이 빠르게 다양해지는데 사람이 매번 model-specific 하니스를 짜는 건 확장 불가능.

2. **세 패러다임 대비 (Figure 1).** ① Human Harness Engineering(사람이 수동 수정), ② Meta-Harness(더 강한 외부 에이전트가 약한 target을 최적화), ③ **Self-Harness(에이전트가 자기 하니스를 개선)**. Self-Harness는 개선 루프를 target 내부로 내재화 — 외부 가이드(비용·frontier 부재·실패양상 불일치) 의존을 제거.

3. **3단계 반복 루프 (Algorithm 1, Figure 2).**
   - **Weakness Mining**: held-in 실행 트레이스 중 실패만 추려 verifier-grounded failure signature $\phi=(c,q,m)$ (terminal cause · causal status · 추상 메커니즘)로 **결정론적 클러스터링** → evidence bundle $B_t$. 수정안을 처방하지 않고 verifier-level 실패와 agent-level 메커니즘을 분리.
   - **Harness Proposal**: 동일 모델을 proposer로 호출, bounded context(편집 가능 표면·실패 패턴·보존할 passing 행동·이전 시도) 제공. **병렬로 $K$개의 diverse yet minimal 후보** 생성 — branch 간 다양성, branch 내 minimality.
   - **Proposal Validation**: held-in/held-out 양쪽 재평가. **non-regressive 규칙** ($\Delta_\mathrm{in}\geq0 \wedge \Delta_\mathrm{ho}\geq0 \wedge \max>0$)으로만 채택. 한쪽을 trade off하면 총합이 늘어도 기각. 통과분 병합 → $h_{t+1}$.

4. **결과 — 3개 모델 전부 일관 개선.** Terminal-Bench-2.0 64-case. Held-out Pass: [[minimax-m2-5|MiniMax M2.5]] 40.5→61.9%, [[qwen3-5|Qwen3.5-35B-A3B]] 23.8→38.1%, [[glm-5|GLM-5]] 42.9→57.1%. 최대 절대 **+21.4%p**, 상대 **+138%**(Qwen3.5 held-in). **held-out에서도 개선** → 평가 실패 과적합이 아니라 재사용 가능한 실행 메커니즘 포착. 어떤 채택 하니스도 두 split 중 하나를 퇴보시키지 않음.

5. **모델별로 다른 진화 (정성 분석).** 같은 초기 하니스가 모델마다 다른 실행 병리 노출. M2.5 → 산출물 조기 생성·content tag 처리·도구 루프 상한. Qwen3.5 → 의존성 precheck·재시도 규율·도구오류 후 artifact 복구 미들웨어. GLM-5 → 환경 persist·탐색→구현 전환. 공통 테마는 **artifact reliability**지만 표현은 모델마다 상이. 프롬프트를 길게 한 게 아니라 *모델 약점 → 실행 가능한 하니스 변경*.

## 핵심 인용

> The performance of LLM-based agents is jointly shaped by their base models and the harnesses that mediate their interaction with the environment. Because different models exhibit distinct behaviors, effective harness design is inherently model-specific.

> We introduce *Self-Harness*, a new paradigm in which an LLM-based agent improves its own operating harness, without relying on human engineers or stronger external agents.

> Self-Harness does not simply add generic instructions, but effectively turns model-specific weaknesses into concrete, executable harness changes.

> Self-improvement should be grounded in behavioral evidence rather than only in the proposer's rationale for a plausible edit.

## 실험 설정 메모

- **벤치마크**: Terminal-Bench-2.0 ([[terminal-bench]], 89개 중 64-case 부분집합; 외부 웹·멀티모달 task 제외). 실행 환경은 Harbor.
- **초기 하니스**: [[deepagents|DeepAgents]] SDK 기반 최소 구성 (Figure 3) — 짧은 시스템 프롬프트 + 기본 파일/셸 도구. 편집 가능 표면: instruction·tools·verification guidance 등 선언적 config point.
- **모델 접근**: M2.5는 MiniMax 호스티드 API, GLM-5는 OpenRouter, Qwen3.5-35B-A3B는 로컬 4×H200 (SGLang). 평가 반복 2회.
- **프로토콜**: held-in(trace·실패증거 노출) / held-out(proposer 비공개, promotion gate 전용) 고정 분할. task별 fresh 환경.

## 등장 개체·개념

- 조직: [[shanghai-ai-lab|Shanghai Artificial Intelligence Laboratory]]
- 저자: Hangfan Zhang, Shao Zhang, Shuyue Hu (교신) 외
- 모델: [[minimax-m2-5]], [[qwen3-5]], [[glm-5]]
- 벤치마크·도구: [[terminal-bench|Terminal-Bench-2.0]], [[deepagents|DeepAgents SDK]]
- 개념: [[self-harness]] (허브), [[agent-harness-design]], [[harness-engineering]], [[generator-evaluator-pattern]]
- 관련 선행연구(인라인): ReAct, SWE-agent, Reflexion, STOP, Automated Design of Agentic Systems, Meta-Harness, Darwin Gödel Machine, AlphaEvolve, The AI Scientist

## References

- [원문 (arXiv HTML)](https://arxiv.org/html/2606.09498v1) · [arXiv abs](https://arxiv.org/abs/2606.09498)
- 2차 소스: [[papanuvo-self-harness]] (한국어 해설)
- 개념 허브: [[self-harness]]
- 연관: [[agent-harness-design]], [[harness-engineering]], [[generator-evaluator-pattern]]

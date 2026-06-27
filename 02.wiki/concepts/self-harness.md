---
title: Self-Harness
type: concept
category: pattern
tags: [agent, harness, self-improvement, harness-engineering, terminal-bench, llm-engineering]
related: [agent-harness-design, harness-engineering, generator-evaluator-pattern, ralph-wiggum-method, verifiable-goals, sutton-bitter-lesson, dynamic-workflows]
first-seen: self-harness-paper
sources: [self-harness-paper, papanuvo-self-harness]
created: 2026-06-14
updated: 2026-06-14
---

# Self-Harness

**LLM 에이전트가 자기 자신이 작동하는 [[agent-harness-design|하니스(harness)]]를 스스로 개선하는 패러다임**. 인간 엔지니어도, 외부의 더 강한 에이전트도 없이 — *고정된 동일 모델*이 자기 실행 트레이스(execution trace)에서 약점을 발견하고, 하니스 수정안을 제안하고, 회귀 테스트로 검증해 채택한다. Shanghai AI Lab(Zhang et al., 2026)의 논문 *"Self-Harness: Harnesses That Improve Themselves"* ([[self-harness-paper]], [arXiv 2606.09498](https://arxiv.org/abs/2606.09498))에서 제안. 모델 파라미터는 절대 건드리지 않고 **하니스(비-파라메트릭 스캐폴딩)만** 진화시킨다.

> *"For a conscious being, to exist is to change, to change is to mature, to mature is to go on creating oneself endlessly."* — Henri Bergson, *Creative Evolution* (논문 제사)

## 세 가지 하니스 개선 패러다임

논문은 하니스를 개선하는 세 가지 방식을 대비한다 (Figure 1):

| 패러다임 | 누가 하니스를 고치나 | 본 위키 |
|---|---|---|
| **Human Harness Engineering** | 인간 엔지니어가 수동 수정 | [[harness-engineering]] · [[agent-harness-design]] |
| **Meta-Harness** | *더 강한 외부 에이전트*가 약한 target 에이전트의 하니스를 최적화 | (아래 대비) |
| **Self-Harness** | **에이전트가 자기 자신의 하니스를 개선** | 본 페이지 |

Self-Harness의 차별점은 개선 루프를 **target 에이전트 내부로 내재화**한다는 것. 외부 가이드(비용 큼·frontier 모델엔 부재·target의 실패 양상과 불일치 가능)에 대한 의존을 줄인다. Meta-Harness가 *"강 모델 → 약 모델"* 의 외부 최적화라면, Self-Harness는 *"같은 모델이 현재 하니스 아래에서 자기 미래 행동을 규정하는 하니스에 bounded edit을 제안"* 하는 통제된 좁은 설정이다.

## 하니스(harness)의 정의 (논문 용법)

고정 언어 모델 $M$을 에이전트로 배치하는 **비-파라메트릭 스캐폴딩**: 지시문(instruction), 가용 도구, 메모리·상태 관리, 검증 규칙, 런타임 제어 등. 모델 가중치를 바꾸지 않고, 모델이 task를 관찰→행동→도구 호출→중간 산출물 점검→최종 답 생성하는 **실행 프로토콜**을 규정한다.

형식적으로: 고정 모델 $M$ + 하니스 $h$, task $x$ → 실행 트레이스 $\tau$ + 출력 $y$. 평가자 $\mathcal{E}$가 (task, trace, output)을 pass/fail로 매핑. **$M$과 $\mathcal{E}$는 고정**, 하니스만 개선 대상. Self-Harness는 하니스 계보(lineage) $h_0, h_1, \ldots$ 위에서 작동하며, 각 전이는 가중치 갱신이 아니라 실행 프로토콜에 대한 **bounded edit**이다.

## 3단계 반복 루프 (Algorithm 1)

매 라운드 $t$마다 한 번의 최적화 루프를 돈다 (Figure 2):

### 1. Weakness Mining — 클러스터링된 트레이스에서 실패 패턴 식별

- 현재 하니스 $h_t$로 held-in split $D_\mathrm{in}$ 실행 → 각 task마다 trace record $r_i = (x_i, \tau_i, y_i, z_i)$ ($z_i$=pass/fail).
- 실패 record $F_t = \{r_i \mid z_i = \mathrm{fail}\}$ 만 추려, **verifier-grounded failure signature** 로 클러스터링:
  $$\phi(r_i) = (c_i, q_i, m_i)$$
  - $c_i$ — verifier가 노출한 **terminal 실패 원인** (예: timeout, missing artifact)
  - $q_i$ — 그 실패에 연결된 에이전트 행동의 **causal status**
  - $m_i$ — 트레이스가 드러낸 **추상적 에이전트 메커니즘** (재사용 가능한 행동 양상)
- 같은 signature끼리만 묶음 → **결정론적·evaluator-grounded 클러스터링**. 표면 증상(timeout)이 같아도 근본 메커니즘이 다르면 다른 클러스터. 산출물 = 실패 패턴을 요약한 **evidence bundle $B_t$** (수정안을 처방하지 않음 — verifier-level 실패와 agent-level 메커니즘을 분리).

### 2. Harness Proposal — diverse yet minimal 후보 수정

- 외부 옵티마이저가 아니라 **동일 고정 모델 $M$을 현재 하니스 $h_t$ 아래 proposer 역할로 호출**. bounded proposal context 제공: 편집 가능한 하니스 표면, verifier-grounded 실패 패턴, 보존해야 할 passing 행동, 이전 시도 요약.
- **병렬 생성**으로 $K$개의 상호 구별되는 후보 $\mathcal{P}_t = \{(\Delta_j, a_j)\}_{j=1}^K$. 각 $\Delta_j$는 $h_t^{(j)} = \Delta_j(h_t)$ 후보 하니스를 만들고, $a_j$는 audit record(타겟 실패 패턴·수정 표면·기대 효과·회귀 위험).
- **diversity는 branch 간에 장려, minimality는 branch 내부에 강제**: 각 edit은 선택한 메커니즘을 다루는 데 필요한 표면만 수정, 무관한 동작 보존, 제어 아키텍처의 광범위 재작성 금지. addressable하지 않은 클러스터(task 난이도·모델 능력 한계)는 패치로 강요하지 않고 제외.

### 3. Proposal Validation — 회귀 테스트로 견고한 개선 보장

- 후보 $h_t^{(j)}$를 held-in $D_\mathrm{in}$ + held-out $D_\mathrm{ho}$ 양쪽에서 재평가. held-in은 *동기가 된 증거를 다뤘는가*, held-out은 proposer가 보지 못한 행동에 대한 **회귀 테스트**.
- split별 개선 $\Delta_\mathrm{in}^{(j)}, \Delta_\mathrm{ho}^{(j)}$. **보수적 채택 규칙**:
  $$\Delta_\mathrm{in}^{(j)} \geq 0, \quad \Delta_\mathrm{ho}^{(j)} \geq 0, \quad \max(\Delta_\mathrm{in}^{(j)}, \Delta_\mathrm{ho}^{(j)}) > 0$$
  → **한 split도 떨어뜨리지 않으면서 최소 한 쪽을 개선**해야 채택. 한 쪽을 다른 쪽과 trade off하면(총합 증가해도) 기각. 확률적 평가는 반복 후 aggregate에 같은 규칙 적용.
- 통과한 후보가 여럿이면 병합(`MergeAccepted`)해 $h_{t+1}$ 생성. 채택 0개면 $h_{t+1} = h_t$. 기각된 후보도 로깅 → 모든 전이가 auditable.

> 이 규칙은 [[verifiable-goals]]·[[generator-evaluator-pattern]]의 *"평가를 코드에 박는다"* 사상과 동형 — 채택을 **regression gate**가 결정한다.

## 실험 결과 (Terminal-Bench-2.0)

- **벤치마크**: [[terminal-bench|Terminal-Bench-2.0]] — 컨테이너 터미널 task. 외부 웹/멀티모달 제외한 고정 64-case 부분집합 사용.
- **초기 하니스**: [[deepagents|DeepAgents]] SDK 기반 최소 하니스 (짧은 시스템 프롬프트 + 기본 파일/셸 도구). Figure 3.
- **모델 3종** (다양한 패밀리, 모델·평가자·예산·도구셋 모두 고정, 하니스만 변경): [[minimax-m2-5|MiniMax M2.5]], [[qwen3-5|Qwen3.5-35B-A3B]], [[glm-5|GLM-5]].

| 모델 | Held-in Pass | Held-out Pass | Held-out 상대 개선 |
|---|---|---|---|
| [[minimax-m2-5\|MiniMax M2.5]] | 43.0 → 50.0% | **40.5 → 61.9%** | +53% |
| [[qwen3-5\|Qwen3.5-35B-A3B]] | 15.1 → 36.0% | **23.8 → 38.1%** | +60% (held-in +138%) |
| [[glm-5\|GLM-5]] | 47.7 → 57.0% | **42.9 → 57.1%** | +33% |

최대 절대 **+21.4%p**, 최대 상대 **+138%**. 핵심: **held-out split에서도 개선** → 관찰된 평가 실패에 과적합한 게 아니라 *재사용 가능한 실행 메커니즘*을 잡았다는 증거. 어떤 채택 하니스도 두 split 중 하나를 퇴보시키지 않음.

## 모델별로 달랐던 진화 (핵심 정성 결과)

같은 최소 초기 하니스가 모델마다 **다른 실행 병리(pathology)** 를 노출했고, Self-Harness는 각 모델의 실패 메커니즘에 맞춘 edit을 선택했다:

| 모델 | 채택된 하니스 변경 방향 |
|---|---|
| [[minimax-m2-5\|MiniMax M2.5]] | 필수 산출물 **조기 생성**, 구조화 도구 출력(content tag) 신중 처리, 길어진 도구 루프 **중단/재유도** (runtime policy로 total tool message 상한) |
| [[qwen3-5\|Qwen3.5-35B-A3B]] | 의존성 **사전 점검**, 동일 명령 반복 실패 방지(재시도 규율), 끝없는 탐색 cycle 차단, 도구 오류 후 **필수 산출물 복구 미들웨어** |
| [[glm-5\|GLM-5]] | 환경 설정/PATH가 셸 명령 간 **persist** 되도록, 탐색 단계 → **구현·테스트 단계 전환** 가속 |

**공통 테마 = artifact reliability** (M2.5 "create output early", Qwen3.5 "artifact middleware", GLM-5 "transition from exploration"). 그러나 표현 방식은 모델마다 달랐다. Self-Harness는 단순히 프롬프트를 길게 하거나 generic 지침을 추가한 게 아니라, **모델 약점을 구체적·실행 가능한 하니스 변경으로 전환**. subagent 분해·미들웨어 생성 같은 *국소 수리를 넘는 구조적 메커니즘*도 발견.

## 본 위키와의 연결

Self-Harness는 본 위키의 두 하니스 허브가 말하던 진화 루프를 **자동화·내재화**한 사례:

- [[agent-harness-design]]의 핵심 모티프 — *"harness는 모델이 혼자 못하는 것에 대한 가정의 다발이고, 모델이 좋아지면 stale해진다"* — 의 **반대 방향 자동화**. agent-harness-design은 *모델 향상 → 가정 제거(단순화)* 에 무게. Self-Harness는 *관찰된 실패 → 가정 추가(강화)* 를 모델 스스로 돌린다.
- [[harness-engineering]]의 **System Evolution 마인드셋** *"every mistake becomes a rule"* 을 그대로 알고리즘화 — 단, 사람이 `agents.md`에 규칙을 적는 대신 **에이전트가 자기 트레이스에서 규칙을 합성**. *"skill issue 안티패턴(모델 탓하며 다음 버전 대기)"* 의 정반대.
- [[generator-evaluator-pattern]]의 propose/validate 분리와 동형: proposer(생성) ↔ regression gate(평가)를 분리하되, **둘 다 같은 고정 모델**이라는 점이 차이. evaluator를 회의적으로 튜닝하는 대신, **결정론적 verifier + non-regressive 규칙**이 회의 역할.
- [[sutton-bitter-lesson|Bitter Lesson]]/*"the space moves"* 와 정합 — 사람이 모델마다 하니스를 다시 짜는 대신, 연산으로 하니스를 탐색.

> 강조 대비: [[dynamic-workflows]]가 *오케스트레이션 층 자체를 모델이 동적 작성* 하는 런타임 자기조직이라면, Self-Harness는 *하니스 정의 파일 자체를 라운드 간에 영구 수정* 하는 오프라인 자기진화. 전자는 한 세션 내, 후자는 세션 계보(lineage)에 걸친 개선.

## 한계 (논문 명시)

- **bounded edit · 고정 벤치마크** 연구 — open-ended self-improvement가 아님.
- 채택된 edit이 여전히 **벤치마크 특화 실패 패턴**을 반영할 수 있음.
- 프로토콜이 **verifier 결과·trace 품질에 의존**. pass-rate non-regression만으로는 고위험 하니스 변경엔 부족 — 더 강한 acceptance gate 필요.
- 핵심 요구는 동일: 자기개선은 *proposer의 그럴듯한 근거가 아니라 행동 증거(behavioral evidence)에 grounded* 되어야 한다.

## References

- [[self-harness-paper]] (1차, arXiv 2606.09498)
- [[papanuvo-self-harness]] (2차, 한국어 해설)
- 허브: [[agent-harness-design]] · [[harness-engineering]]
- 관련 패턴: [[generator-evaluator-pattern]] · [[verifiable-goals]] · [[ralph-wiggum-method]] · [[dynamic-workflows]] · [[sutton-bitter-lesson]]

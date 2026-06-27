---
title: Generator–Evaluator Pattern
type: concept
category: pattern
tags: [agent, multi-agent, gan, evaluation, feedback-loop]
related: [agent-harness-design, sprint-contract, dynamic-workflows, self-harness]
first-seen: anthropic-harness-design-long-running-apps
sources: [anthropic-harness-design-long-running-apps]
created: 2026-05-25
updated: 2026-06-14
---

# Generator–Evaluator Pattern

LLM 에이전트의 **생성**과 **평가**를 별개의 에이전트로 분리하고, 평가자의 비판을 생성자에게 피드백으로 돌려 반복 정제하는 다중 에이전트 패턴. GAN(Generative Adversarial Network)에서 영감. [[anthropic-harness-design-long-running-apps]]가 frontend·풀스택 양쪽에서 적용한 사례.

## 왜 필요한가 — Self-evaluation bias

LLM에게 *자기 산출물*을 평가시키면 거의 항상 후하게 점수를 매긴다. 명백히 평범한 작품도 "잘 됐다"고 답한다. 이는 binary check가 없는 *subjective* 영역(디자인, UX)에서 특히 두드러지고, verifiable 영역에서도 일정 부분 나타난다.

> Separating the agent doing the work from the agent judging it proves to be a strong lever.

평가자도 결국 LLM이라 처음에는 관대하다. 그러나 **generator를 비판적으로 만드는 것보다 standalone evaluator를 회의적으로 튜닝하는 게 훨씬 tractable**.

## 핵심 구성요소

1. **Grading criteria** — subjective 영역도 명시적 기준으로 변환. "디자인이 좋은가?" 대신 "디자인 원칙을 따르는가?"
2. **Evaluator calibration** — few-shot 예시 + 점수 breakdown으로 평가자 취향을 사용자에 정렬
3. **Skeptical posture** — 평가자에게 "엄격하라"고 명시적으로 지시
4. **Feedback loop** — 평가자 비평이 generator의 다음 iteration 입력
5. **Strategic decision after each cycle** — generator는 *기존 방향을 refine할지, 완전히 pivot할지* 매번 선택

## 사례: Frontend (4-criteria)

| Criterion | 무엇을 보는가 |
|---|---|
| **Design quality** | 색·타이포·레이아웃·이미지가 하나의 mood로 통합되는가 |
| **Originality** | 커스텀 결정의 흔적이 있는가; "purple gradients over white cards" 등 AI 슬롭 패턴 페널티 |
| **Craft** | 기술적 집행 (typography hierarchy, spacing, contrast) |
| **Functionality** | 미학과 무관한 사용성 |

Design quality와 originality를 더 무겁게 weight → 모델이 aesthetic risk-taking 쪽으로 이동.

**관찰된 효과**:
- 5~15 iteration 동안 점수 상승 후 plateau (headroom 여전히 존재)
- 비선형 — 중간 iteration이 마지막보다 더 좋은 경우도 잦음
- *"museum quality"* 같은 표현이 시각적 수렴 방향까지 바꿈
- 9번째 iteration까지는 평범한 다크 랜딩, 10번째에 갑자기 **CSS perspective 3D 갤러리 룸**으로 도약 (네덜란드 미술관 prompt)

## 사례: 풀스택 (3-agent + sprint contract)

- **Planner**: 1~4 문장 → product spec
- **Generator**: sprint 단위 구현
- **Evaluator**: [[playwright-mcp|Playwright MCP]]로 UI·API·DB 클릭/검증

각 sprint 시작 전 [[sprint-contract|sprint contract]] 협상. Evaluator는 코드 위치(예: `LevelEditor.tsx:892`)까지 짚어가며 fail 사유 제시.

## 한계·튜닝 비용

- 평가자 *초기* 출력은 거의 쓸모없음 — 합리적 기준에 맞추려면 *여러 라운드의 development loop* 필요
- 모델이 강해지면 evaluator의 marginal value가 변동: *task가 모델 solo 한계 너머일 때*만 명백한 lift
- 보이지 않는 도메인(예: 청각 — *"Claude는 들을 수 없다"*)은 평가가 어려움

## 인용

> Tuning a standalone evaluator to be skeptical turns out to be far more tractable than making a generator critical of its own work.

## 오케스트레이션 차원으로의 확장

[[dynamic-workflows|Dynamic workflows]]는 이 generator/evaluator 사상을 *수십~수백 agent의 오케스트레이션*으로 확장한다: agent들이 독립 각도로 답을 내고, *다른 agent가 그 결과를 refute(반박)* 하려 시도하며, **수렴할 때까지 iterate**. 1:1 generator–evaluator 루프가 fan-out된 adversarial 군집으로 일반화된 형태.

## 자기-개선 하니스로의 변형 (Self-Harness 시각)

[[self-harness|Self-Harness]]([[self-harness-paper]])는 이 패턴을 *하니스 그 자체를 개선하는 루프*로 옮기되 두 가지를 비튼다:

- **생성자=평가대상=같은 모델**. proposer(하니스 edit 생성)도, 그 edit이 적용된 후 평가받는 에이전트도 **동일한 고정 모델**. 본 패턴의 *self-evaluation bias* 우려를 회피하는 방식이 다르다 — 평가자를 회의적으로 *튜닝*하는 대신, 평가를 **결정론적 verifier + non-regressive 채택 규칙**([[terminal-bench|Terminal-Bench-2.0]] held-in/held-out)에 위임. "회의적 평가자"의 역할을 **regression gate**가 대신한다.
- **산출물이 응답이 아니라 하니스**. generator가 매 cycle *refine/pivot* 을 고르듯, Self-Harness는 diverse yet minimal 후보를 병렬 생성해 회귀 게이트를 통과한 것만 병합한다.

즉 generator–evaluator의 *피드백 루프*를 모델 응답이 아니라 **모델을 감싸는 스캐폴딩의 계보(lineage)** 에 적용한 형태. → [[self-harness]] 참조.

## References

- [[anthropic-harness-design-long-running-apps]]
- 관련: [[agent-harness-design]], [[sprint-contract]], [[dynamic-workflows]], [[self-harness]]

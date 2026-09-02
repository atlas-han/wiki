---
title: Generator–Evaluator Pattern
type: concept
category: pattern
tags: [agent, multi-agent, gan, evaluation, feedback-loop]
related: [agent-harness-design, sprint-contract, dynamic-workflows, self-harness, token-roles, trusted-throughput, managed-agents, verifiable-goals, agent-skills]
first-seen: anthropic-harness-design-long-running-apps
sources: [anthropic-harness-design-long-running-apps, tech-bridge-claude-platform-agent-era, tech-bridge-trusted-throughput, tech-bridge-flutter-ai-workflow]
created: 2026-05-25
updated: 2026-09-02
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

## 플랫폼 기능으로의 승격 (2026-09-01)

[[managed-agents]]의 **`outcomes`**가 이 패턴을 제품 기능으로 만들었다 ([[tech-bridge-claude-platform-agent-era]]).

> 예를 들어 "좋은 결과는 이렇습니다"와 같은 **루브릭**을 제시하면 그 기준을 충족하는 **두 번째 에이전트를 제공**합니다.

> 첫 번째 담당자가 시도해보고 (…) '아직 충분하지 않네. 다시 해보자'라고 하는 거죠. (…) **채점자와 실행자가 함께** 일을 처리하기 때문이죠.

달라진 점은 **누가 evaluator를 만드느냐**다. 지금까지 이 패턴은 하니스 설계자가 직접 짜는 것이었는데, 여기서는 사용자가 **루브릭만 쓰면 플랫폼이 프로비저닝**한다. [[verifiable-goals]]가 요구한 verifier의 진입 장벽을 낮춘 형태.

## 지표 계측으로의 전용 (2026-09-01)

[[trusted-throughput]]은 같은 패턴을 코드 산출물이 아니라 **생산성 지표 자체**에 적용한다 — 병합된 PR의 복잡도를 **LLM 1~2개에 프롬프트를 넣어 티셔츠 사이즈로 채점**해서 가중치를 얻는다.

같은 소스가 리뷰 파이프라인에도 이 패턴을 쓴다: **AI가 1차 방어선**(스타일·커버리지)이고 사람은 아키텍처·보안 같은 주관적 심층 판단을 맡는다. 즉 evaluator를 조직 프로세스의 한 단계로 배치한 형태.

## 개인 실무에서의 두 변형 (2026-09-02)

[[ivanna-kacevica|Ivanna Kaceviča]]([[tech-bridge-flutter-ai-workflow]])가 이 패턴을 [[agent-skills|스킬]] 두 개로 자기 워크플로에 심는다.

**1. 두 evaluator의 교차 확인.** 자기 코드 리뷰 스킬과 Kevin Moore의 PR triage 스킬을 **서로 다른 두 에이전트**에게 주고,

> 한 명은 코드 리뷰를 하고, 다른 한 명은 PR 분류를 담당한 다음 **서로의 보고서를 확인**하는데, 덕분에 정말 좋은 결과를 얻고 있습니다.

generator–evaluator가 아니라 **evaluator–evaluator**다. 회의적 평가자를 튜닝하는 대신 *관점이 다른* 평가자 둘을 붙여 서로를 반박하게 한 것 — [[dynamic-workflows]]의 refute 군집을 2개로 줄인 형태.

남은 한계도 짚는다: *"코드가 좋은지는 평가할 수 있지만 그 코드가 필요한지는 항상 판단할 수 없다."* 위 "한계·튜닝 비용"의 *보이지 않는 도메인*이 여기서는 **맥락과 기억**이다.

**2. 스크린샷을 보는 QA 에이전트.** 웹에서 앱을 띄워 실제 스크린샷(애니메이션 webp 포함)을 찍는 스킬을 만들고, 그것을 **다른 에이전트**가 본다.

> 다른 에이전트는 코드를 검사하고 테스트가 통과되었는지 확인하는 것뿐만 아니라 **UI의 결함을 시각적으로 검사**할 수 있습니다.

위 풀스택 사례의 [[playwright-mcp|Playwright MCP]] evaluator를 개인이 재현한 것이되, 실시간 조작 대신 **정적 스크린샷 워크스루**를 택했다(iPhone 시뮬레이터 로딩을 기다리지 않아도 됨). 골든 테스트는 **회귀**용으로 남기고 QA는 실제 화면으로 — [[verifiable-goals]]의 UI verifier를 에이전트가 닫는다.

> ⚠️ 두 변형 모두 일화이며 측정치가 없다.

## References

- [[anthropic-harness-design-long-running-apps]]
- [[tech-bridge-claude-platform-agent-era]] — `outcomes` (grader 프로비저닝)
- [[tech-bridge-trusted-throughput]] — 지표 계측·리뷰 파이프라인 적용
- [[tech-bridge-flutter-ai-workflow]] — evaluator 교차 확인 · 스크린샷 QA 에이전트
- 관련: [[agent-harness-design]], [[sprint-contract]], [[dynamic-workflows]], [[self-harness]]

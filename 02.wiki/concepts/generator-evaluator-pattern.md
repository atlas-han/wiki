---
title: Generator–Evaluator Pattern
type: concept
category: pattern
tags: [agent, multi-agent, gan, evaluation, feedback-loop]
related: [agent-harness-design, sprint-contract, dynamic-workflows, self-harness, token-roles, trusted-throughput, managed-agents, verifiable-goals, agent-skills]
first-seen: anthropic-harness-design-long-running-apps
sources: [anthropic-harness-design-long-running-apps, tech-bridge-claude-platform-agent-era, tech-bridge-trusted-throughput, tech-bridge-flutter-ai-workflow, tech-bridge-multimodal-commerce-agent, tech-bridge-claude-code-team-workflow, tech-bridge-ai-native-sdlc]
created: 2026-05-25
updated: 2026-09-05
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

## 루프의 모든 단계를 채점하기 (2026-09-04)

[[tech-bridge-multimodal-commerce-agent]]([[nidhi-kaushik-vyas]] / [[google-deepmind]])은 이 패턴을 **산출물 하나가 아니라 루프의 모든 단계**에 건다. 강연의 네 번째 교훈이 그대로 이것이다 — *"루프를 제대로 채점했는지 확인하세요. **모든 단계에** 적합한 auto-rater가 설치되어 있습니다."*

| 단계 | auto-rater |
|---|---|
| working state ([[fuzzy-intent-discovery]]) | fact retention · **confidence calibration** · **counterfactual sensitivity** |
| 협업 전략 (다음 질문 선택) | blocker 식별 · **over-asking** · question utility |
| elicitation ([[multimodal-elicitation]]) | hidden preference 효율 · **turn efficiency** · format selection accuracy |
| 응답 ([[adaptive-response-format]]) | format accuracy · data fidelity · **user actionability** |

지금까지 이 위키의 사례(frontend 4-criteria, 풀스택 3-agent, [[managed-agents]]의 `outcomes`)는 전부 **최종 산출물**을 채점했다. 여기서 달라지는 것은 **중간 상태와 행동 선택**도 채점 대상이 된다는 점이다 — 답이 좋은지가 아니라 *"지금 이 질문을 하는 게 맞는가"*, *"이 상태에 사실이 빠지지 않았는가"* 를 잰다.

새로 얻은 채점 기법 세 가지:

- **counterfactual sensitivity — 양방향으로 잰다.** *"쿼리를 뒤집어서 (…) 제약 조건도 함께 변경되도록 하고, **관련성이 없는 제약 조건은 그대로 유지**되도록 합니다."* 한쪽만 재면 아무 입력에나 반응하는 과민한 추출기가 통과한다. 두 번째 방향이 **가짜 상관을 잡는 장치**다.
- **over-asking을 결함으로 센다.** 정확도만 재면 에이전트는 계속 물어보는 쪽으로 몰린다. 질문 횟수 자체에 페널티를 걸어 이를 막는다.
- **사용자 시뮬레이터.** 제약을 **정답으로 심어둔** 가짜 사용자를 만들어 elicitation을 채점 가능한 문제로 바꾼다. evaluator를 회의적으로 *튜닝*하는 대신 **환경 쪽을 통제**해 채점기를 얻는다 — [[self-harness]]가 결정론적 verifier에 위임한 것과 같은 계열의 우회.

그리고 채점기의 수명에 대한 단서. 위 "한계·튜닝 비용"이 *초기 evaluator는 거의 쓸모없다*고 했던 것에 대한 대응이다.

> 이런 auto-rater를 개발하는 것은 거의 **진화하는 시스템과 같습니다.** 처음에는 **아주 간단하게 시작**하지만, 시스템이 발전함에 따라 **채점기도 시스템과 함께 점진적으로 성장**해야 합니다.

> ⚠️ 12종의 rater 목록은 얻었지만 **구현·임계값·측정 결과는 소스에 없다.**

## 두 가지 확장 (2026-09-05)

### ① 3관점 적대적 검토 — 채점기를 복수로 ([[tech-bridge-claude-code-team-workflow]])

[[anthropic|Anthropic]] Claude Code 팀의 코드 리뷰 workflow는 채점기를 **하나가 아니라 셋** 둔다.

> 각 버그에 대해, **세 가지 다른 관점이나 시각에서 버그를 살펴보고 실제로 버그가 존재하는지 확인하는 적대적 검토(adversarial review)** 를 수행할 수 있습니다.

목적이 생성이 아니라 **제거**라는 점이 위의 사례들과 다르다 — *"**모든 버그를 걸러내고 사용자의 주의가 필요한 가장 중요한 버그만 남겨주는** 것."* generator가 과잉 생성하고 evaluator가 대량 기각하는 비대칭 구성이다.

그리고 채점의 경제학이 명시된다 — *"**자신감을 키우는 방법은 바로 test-time compute를 문제에 투입하는 것**입니다."* 채점기는 품질 장치이자 **확신을 사는 지출**이다.

⚠️ 팀이 짚는 병목은 채점 자체가 아니라 **되접기**다 — *"마치 map-reduce 문제와 같아요. (…) 전체 출력값을 다 읽어버리면 미쳐버릴 것 같거든요."*

### ② Continuous evals — 하네스 자체의 회귀 테스트 ([[tech-bridge-ai-native-sdlc]])

위 "루프의 모든 단계를 채점하기"가 *산출물의 각 단계*에 채점기를 붙인 것이라면, [[ai-native-sdlc]]는 채점 대상을 **파이프라인 자신**으로 돌린다.

> **모든 스킬 변경이나 모델 업그레이드에 평가를 적용** (…) **지속적 통합 과정에서 지속적인 평가.**

형태가 소박하다 — 해결한 문제 **20개 정도**와 예상 결과 세트를 모아 두고, **새 모델·새 스킬·업무 방식의 근본적 변화**마다 돌려 **퇴보**를 확인한다.

이는 [[harness-pruning]]과 짝을 이룬다. 하네스 기능을 지우려면 지워도 되는지 확인할 장치가 필요하고, continuous evals가 그 역할이다. ⚠️ 다만 두 소스는 서로를 언급하지 않는다 — 이 연결은 이 위키의 정리다.

## References

- [[anthropic-harness-design-long-running-apps]]
- [[tech-bridge-claude-platform-agent-era]] — `outcomes` (grader 프로비저닝)
- [[tech-bridge-trusted-throughput]] — 지표 계측·리뷰 파이프라인 적용
- [[tech-bridge-flutter-ai-workflow]] — evaluator 교차 확인 · 스크린샷 QA 에이전트
- 관련: [[agent-harness-design]], [[sprint-contract]], [[dynamic-workflows]], [[self-harness]]

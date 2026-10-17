---
title: Verifiable Goals
type: concept
category: pattern
tags: [llm-coding, planning, verification, success-criteria]
related: [llm-coding-guidelines, surgical-edits, sprint-contract, ralph-wiggum-method, generator-evaluator-pattern, outcome-engineering, claude-code, spec-driven-development, agent-org-adoption, frontier-engineering, signal-layer, trusted-throughput, agent-distributed-systems, slop-probes, ai-slop, steering-altitude, automated-ai-research, model-calibration, intent-alignment]
first-seen: multica-karpathy-skills-claude-md
sources: [multica-karpathy-skills-claude-md, charlychoi-claude-code-best-practices, tech-bridge-figma-coding-agents, tech-bridge-spec-driven-development, tech-bridge-frontier-engineering, tech-bridge-signal-layer, tech-bridge-trusted-throughput, tech-bridge-taste-labs-measuring-slop, tech-bridge-impeccable-design-steering, tech-bridge-mousepower-measuring-agents, tech-bridge-lauren-tan-trusting-agents, tech-bridge-agents-vs-humans-optimizer-speedrun, tech-bridge-introspection-loop-is-the-product, tech-bridge-factory-software-factory, tech-bridge-jev-calibrated-decisions, tech-bridge-jensen-huang-korea-society-gala, tech-bridge-cooking-with-codex, tech-bridge-sentry-stop-prompting-codify-linters, tech-bridge-horthy-state-of-software-factory]
created: 2026-05-25
updated: 2026-10-16
---

# Verifiable Goals

모호한 task를 **검증 가능한 목표(verifiable goal)** 로 변환하는 LLM 코딩 원칙. *"Define success criteria. Loop until verified."* [[multica-karpathy-skills-claude-md]]의 4원칙 중 4번 (Goal-Driven Execution)을 별도 concept으로 추출.

## 핵심 명제

> Strong success criteria let you loop independently. Weak criteria ("make it work") require constant clarification.

강한 성공 기준이 있으면 LLM이 **independent loop**로 작업 가능. 약하면 매 단계마다 사람의 clarification이 필요 — 사실상 loop가 안 된다.

## 변환 예시

| 모호한 task | 검증 가능한 goal |
|-----------|----------------|
| "Add validation" | "Write tests for invalid inputs, then make them pass" |
| "Fix the bug" | "Write a test that reproduces it, then make it pass" |
| "Refactor X" | "Ensure tests pass before and after" |

공통 패턴: **(1) verifier를 먼저 만들고 (2) verifier를 통과시키는 코드를 작성**. 테스트 = goal의 인코딩.

## Task별 verifier 선택

[[charlychoi-claude-code-best-practices]]는 verifier를 단위 테스트보다 넓게 실무 task별로 매핑한다.

| Task | Verifier |
|---|---|
| 함수·API | unit/integration test, status code, sample response |
| UI | desktop/mobile screenshot, clickability, console error 없음 |
| Build·type issue | 실제 build·typecheck command 성공 |
| Refactoring | 변경 전후 regression test 통과 |
| 문서 | 필수 section·실제 command·link 유효성 |
| 데이터 처리 | 고정 input/output 비교 |

즉 goal은 “무엇을 만들 것인가”만이 아니라 **어떤 외부 evidence가 통과하면 멈출 것인가**까지 포함해야 한다.

## 멀티스텝 plan 형식

```
1. [Step] → verify: [check]
2. [Step] → verify: [check]
3. [Step] → verify: [check]
```

각 step에 verify가 붙어야 — verify가 없는 step은 *작업의 정의가 빠진 step*.

## 위키 내 자매 개념

- [[sprint-contract]] — 다중 에이전트 코딩에서 generator·evaluator가 **sprint 시작 전** 합의하는 "done의 정의". 본 원칙의 multi-agent 변형.
- [[generator-evaluator-pattern]] — 검증을 별도 agent로 분리. verifiable goal을 evaluator가 들고 있는 형태.
- [[ralph-wiggum-method]] — `while :; do cat PROMPT.md | claude-code ; done` 무한 루프. PROMPT.md 안에 verifiable goal이 있어야 발산하지 않음.
- [[outcome-engineering]] — Nextdoor/Codex 사례의 조직 관점 framing. *"원하는 결과를 정의한다"*가 곧 verifier(테스트·스크린샷·성능 기준)를 먼저 정의하는 것 — 같은 원리의 외부(비-Anthropic) 서술.
- [[spec-driven-development]] — spec 자체가 저장되는 verifier. 프롬프트 대신 constitution/spec/plan/task 아티팩트.
- [[agent-org-adoption]] — Figma: 테스트를 코드보다 먼저(red-green), 검증 피라미드의 아래를 결정론적으로. 조직 도입에서 verifier 투자가 generation보다 높은 레버리지.
- [[frontier-engineering]] — Amazon/Kiro: 에이전트에게 할 일 + 자가 검증을 넘기고 컴파일·테스트·커버리지 바에만 복귀. 수 시간 루프의 조건은 **로컬 결정론적 mock**으로 피드백을 빠르게.

## 왜 작동하는가

LLM은 **자기 평가 편향**(self-evaluation bias)이 있어 *"되었다"* 를 쉽게 선언함 ([[generator-evaluator-pattern]] 참조). 외부에서 통과 가능한 verifier가 있으면:

1. *"되었다"* 선언이 객관적 통과로 대체됨
2. 실패 시 구체적 fail signal → 재시도 방향이 정해짐
3. 사람의 clarification 없이도 loop 가능

## 약한 vs 강한 criteria

| | 약한 | 강한 |
|---|------|------|
| 예 | "make it work", "looks good" | 테스트 통과, schema validation, CI green |
| 의존성 | 사람의 매 단계 승인 | independent loop 가능 |
| 실패 처리 | 모호 → 재질문 | 구체 fail → 다음 시도 |

## [[surgical-edits]]와의 관계

[[surgical-edits|surgical-edits]]가 *what 외에는 손대지 말 것*을 못 박는다면, verifiable-goals는 *what이 달성되었는지*를 못 박는다. 두 원칙이 묶이면 **"검증 가능한 최소 변경"** 이라는 단일 작업 단위가 정의된다.

## 경계: verifier를 만들 수 없는 곳 (2026-09-01)

[[signal-layer]]가 이 개념의 **정확한 이면**을 제시한다. 여기가 "verifier를 만들어라"라면 그쪽은 "**verifier를 만들 수 없는 곳이 어디인지 알아라**"이고, 두 페이지는 같은 축의 양 끝이다.

> 측정할 수 있는 것은 무엇이든 훈련에 활용할 수 있죠. **컴파일러는 무료 채점 도구입니다. 테스트 스위트는 무료 채점 도구입니다.**

> 작업이 스스로 점수를 매길 수 있게 되는 순간, 모델을 그 점수에 맞춰 계속 개선해 나가면 **결국에는 이기게 되는 거죠.**

여기서 나오는 따름정리가 실무적으로 중요하다 — **코드 자동화가 먼저 온 이유는 그것이 가장 검증하기 쉬웠기 때문**이고, 자동 채점기가 없는 영역(문제 선택·신뢰·메시지)은 자동화되지 않은 채 남는다. 그래서 [[signal-layer]]는 그런 영역에 **사람 verifier**를 심으라고 처방한다: 프로젝트를 본 적 없는 SRE에게 README를 주고 설명하게 한 뒤 **의도와의 차이**를 재는 식.

## Goodhart 확장: 토큰 지출 (2026-09-01)

[[trusted-throughput]]이 이 개념의 경고를 토큰 경제에 그대로 옮긴다.

> LOC는 중요한 지표이지만, 직접적으로 최적화해야 할 대상은 아닙니다. **토큰 사용량과 지출도 마찬가지입니다.**

실제 사고 사례까지 붙는다 — 전사 토큰 대시보드가 리더보드로 작동하자 엔지니어들이 **사용량 극대화를 경쟁**하기 시작했다. 처방은 단일 지표가 아니라 **객관적 검사 + 인간 판단 + 고객 반응**의 3중 검증이다.

## 주관 영역에 verifier를 세우기 (2026-09-12)

> 저는 무언가를 고치려면 **먼저 측정하고 먼저 이해해야** 한다고 굳게 믿습니다. 그래서 이 영역들을 **더 검증 가능한 것으로 바꿔 측정치를 붙이는 것**에 집중합니다. — [[thais-castello-branco]] ([[tech-bridge-taste-labs-measuring-slop]])

위 "경계: verifier를 만들 수 없는 곳"이 *주관 영역* 을 그 밖에 뒀다면, [[taste-labs|Taste Labs]]는 그 안에 verifier를 세우려 한다 — 디자인을 *거의 결정론적인 조각*(팔레트·대비·정렬)으로 **분해**하고 조각마다 [[slop-probes|소형 분류기]]를 훈련한다. 경계선은 사라지지 않고 **분해되지 않는 것**(전문가가 갈리는 미학)으로 옮겨간다. ⚠️ 수치 없음.

같은 날 [[tech-bridge-impeccable-design-steering]]은 반대편 — 디자인에는 자동 verifier가 없다고 보고(*"사용자도 의견이 있다"*) **사람 verifier**를 문장으로 심는다: *"누군가에게 보여주고 'AI가 했다'고 말하라. 믿으면 실패."* [[signal-layer]]의 *SRE에게 README를 주고 설명하게 하라* 와 같은 형태다. → [[adjective-verb-steering]] · [[steering-altitude]]

## 한 단계 앞의 결정 — 애초에 검증 가능한 작업을 고르라 (2026-09-12 마우스파워 편)

[[tech-bridge-mousepower-measuring-agents]]의 [[task-entropy-matrix|엔트로피 매트릭스]]가 이 개념보다 **한 단계 앞**에 선다. 이 페이지가 *작업을 검증 가능하게 만들라* 였다면, 그쪽은 **그렇게 만들 수 없는 작업은 고르지 말라**고 한다.

> **수용 기준의 불확실성이 높으면 검증이 실행과 구분되지 않는 지점**에 옵니다. **사람이 그 일을 다시 해야 한다면, 그 일에 왜 에이전트를 만듭니까.**

그리고 성공 기준을 **파는 쪽의 의무**로 돌린다 — *"에이전트를 팔 거라면 그것이 일을 잘하는지 검증하는 루브릭도 함께 줘야 한다."* → [[mousepower]]

## 목표를 CI 실패로 바꾸기 (2026-09-12 Lauren Tan 편)

[[tech-bridge-lauren-tan-trusting-agents]]는 검증 가능화의 **가장 강한 형태**를 제시한다 — 사람이 말로 강제하던 기준을 **하드 제약**으로 옮기는 것.

> ***"PR에 댓글을 다는 대신, 이걸 어떻게 하드 규칙으로 바꾸지? 린트 규칙으로? CI 실패로? 아니면 이 문제를 아예 범주적으로 없애 버릴 수는 없나?"***

→ [[hard-vs-soft-enforcement]] · [[executable-standards]]

## References

- [[multica-karpathy-skills-claude-md]]
- [[charlychoi-claude-code-best-practices]]
- [[tech-bridge-figma-coding-agents]] · [[tech-bridge-spec-driven-development]]
- [[tech-bridge-signal-layer]] — 채점기 경계선 (verifier가 없는 영역)
- [[tech-bridge-trusted-throughput]] — 토큰 지출로의 Goodhart 확장
- 관련: [[llm-coding-guidelines]] (상위 hub), [[surgical-edits]], [[sprint-contract]], [[ralph-wiggum-method]]

## 규칙이 명확한 경쟁 과제 = 보상 신호 (2026-09-28 · [[tech-bridge-agents-vs-humans-optimizer-speedrun]])

[[prime-intellect|Prime Intellect]]는 optimizer speedrun을 에이전트의 **평가이자 훈련 환경**으로 쓴다 — *"the reward is positive if the model beat (…) the last record (…) and the reward is zero or negative if it didn't manage"*(04:34~04:45), *"there is those clear rule that you can verify or not"*(05:10~05:13). 기록 인정에 **통계적 임계값**을 두어 *"seed optimization"*·우연을 배제한다(07:20~07:27). 이 페이지의 *verifier가 강하면 독립적으로 루프를 돈다* 의 극단 사례 — 에이전트가 **며칠간** 혼자 반복했다. ⚠️ 그러나 같은 소스는 **검증 가능한 목표가 수렴은 부르되 발명은 부르지 않았다**고 보고한다(새 옵티마이저 0개). → [[automated-ai-research]]

## 신호가 성공률을, 검증기가 그 진위를 (2026-09-30 · [[tech-bridge-introspection-loop-is-the-product]])

[[roland-gavrilescu|Roland Gavrilescu]]는 루프의 두 끝을 나눈다 — *"the quality of the signal determines the uh success rate of the loop and the uh quality of the verifier um is able to calibrate uh if that success is actually correct or not"*(03:33~03:49). 이 페이지가 verifier 쪽만 다뤄 왔다면, 이 소스는 **입력 신호의 품질을 성공률의 원인으로 따로 둔다.** 첫 사례(OpenClaw의 옛 이름 Clawbot으로 만든 자동차 협상 루프)에도 *"a verifiable way to know when the price is right"*(02:18~02:21)가 들어 있다. 주관 영역(위 09-12 절)에 대한 이 소스의 답은 **제작자 taste를 judge로 코드화 + 사용자 A/B로 보정**이다. → [[loop-is-the-product]] · [[taste-encoded-evals]]

## 문제는 루프가 아니라 "done" (2026-10-02 · [[tech-bridge-factory-software-factory]])

[[tereza-tizkova|Tereza Tížková]]([[factory-ai|Factory]]): *"the question is not the loop itself but the question is how how you define what it means to be done in the loop"*(09:58~10:05). 예전 프로그래밍의 루프는 종료 조건이 명확했지만 지금은 *"the criteria become open-ended because a lot of the tasks are very nondeterministic. It's basically open world"*(10:23~10:30) — 동료가 만든 로고 **3D 프린팅** 루프처럼 물리 세계까지. 결론은 *"they just need to be verifiable"*(10:42). Factory는 완료 조건을 오케스트레이터가 **코드 전에** validation contract로 쓴다(13:07~13:14). ⚠️ ko는 *nondeterministic* 의 *non-* 을 잃고 **"결정론자들"**(10:28)로 옮겨 요지가 반대가 된다. → [[software-factory]] · [[reward-hacking]]

## 검증기는 정오만 본다 — 확신은 보상하지 않는다 (2026-10-09 · [[tech-bridge-jev-calibrated-decisions]])

[[ibm|IBM]] 계열 해설은 RLVR의 성공을 인정하면서(*"a big reason that reasoning models today have got so good at math and coding"*, 08:55~08:59) 그 빈칸을 짚는다: *"the reward here only checks whether the final answer was right. It doesn't reward the model for knowing how sure it should be."*(09:02~09:09). 검증 가능한 목표는 **답의 정오**를 학습시키지만 **답을 얼마나 믿을지**는 학습시키지 않는다 — 그 칸을 겨냥한 것이 RLCD다 → [[model-calibration]] · [[post-training-northstars]]. ⚠️ *로그 오류율* 이라는 Almeida의 표현과 충돌 가능(post-training-northstars 참조).

## ⚠️ 반대편 — "가장 가치 있는 목표는 모호하다" (2026-10-09 · [[tech-bridge-jensen-huang-korea-society-gala]])

[[jensen-huang|Jensen Huang]]: *"most of the most ambitious goals, most aspirational goals, most worthy goals are ambiguous. And part of leadership is to the artistry of giving goals that are sufficiently specific but sufficiently ambiguous so that you could be surprised by its outcome. to leave room for surprise, leave room for discovery, leave room for innovation."*(18:09~18:36)

이 페이지가 모아 온 *"검증 가능한 형태로 써라"* 와 **반대 방향의 처방**이다. Huang은 모호함의 대가를 목표 명세가 아니라 **실행 감시**로 치른다 — *"if the instruction you give to the AI is ambiguous, how do you know (…) you like the journey that it's taking? (…) You have to monitor all AIS"*(18:40~18:56). 

> ⚠️ **긴장(모순 아님):** 이 페이지의 소스 대부분은 **코딩 에이전트의 완료 조건**을, Huang은 **리더가 조직·AI에 주는 목표**를 말한다 — 층이 다르다. 그러나 둘 다 *AI에 일을 맡기는 법*에 대한 처방이고, **모호함을 줄일 것인가 / 감시로 흡수할 것인가**에서 갈린다. 같은 답 안에서 Huang은 정렬을 *"how"* 를 지정하는 것으로 정의한다 → [[intent-alignment]].

## 원칙이 제품 기능이 됐다 — Codex `/goal` (2026-10-11 · [[tech-bridge-cooking-with-codex]])

[[codex|Codex]]의 goal(*"SLGO"*[=`/goal`] 44:22, *"I'm running a goal"* 29:06)은 이 페이지의 *"Define success criteria. Loop until verified"* 를 **하네스 기능**으로 만든 것이다. 동작: *"it'll keep evaluating itself against the success criteria (…) at each turn it'll check hey did this actually complete um and if not should I keep going"*(44:02~44:13).

- ⭐ [[charlie-guo|Charlie Guo]]: *"be really specific with the criteria (…) you want that criteria to be as verifiable as possible."*(43:32~43:43)
- ⭐ 약한 기준의 실패를 부르는 이름 — *"goal is is kind of like a genie (…) when it doesn't sometimes I feel like I've entered into a monkeykey's paw type situation where you know it has done the thing technically that I asked it to do but like very much not in the way that I was expecting."*(43:45~43:59) → 위 *"약한 vs 강한 criteria"* 의 사용자 쪽 표현, [[reward-hacking]]의 일상판.
- 운영 장치(Gabriel): 목표 하나가 아니라 **goals.md에 목표 여러 개** + progress dashboard.html(32:05~32:26), 마일스톤마다 **목표 감사(goal audit) 스레드**가 이탈을 *"nudge back"*(32:45~33:04).
- 용도: 마이그레이션·대규모 리팩터링·재시도 루프·실험·*"full oneshotting apps with fairly detailed specs"*(44:31~44:41).

> ⚠️ 당사자 진술. ko 43:20은 *"15 hours"* 를 **"15년"** 으로 옮긴다.

## ⚠️ snake oil — 정성 품질을 숫자 목표로 바꾸지 말 것 (2026-10-14 · [[tech-bridge-sentry-stop-prompting-codify-linters]])

[[greg-pstrucha|Greg Pstrucha]]: *"beware of a snake oil. (…) I've done experiments where I tried to capture a qualitative measure in a quantitative metric."*(13:27~13:39) 예로 든 것은 cyclomatic complexity와 test coverage다. 커버리지는 100% 가까이 올랐지만 테스트는 가치 있는 것을 재지 않았다(14:17~14:32). 같은 화자는 linter로 못 잡는 판단에 *"no more than four states"* 같은 숫자 규칙을 만들 수는 있지만 *"it's all It's all made up"*(11:10~11:17)이라고 스스로 기각한다.

이 페이지의 "검증 가능한 형태로 써라"에 대한 **경계 조건**이다. 검증 가능화가 맞는 대상은 결정론적 규칙(lint·타입·테스트 통과)이고, 정성 품질은 저장소 정책과 리뷰 루프로 남긴다([[automated-code-review]]의 grumpy engineer). → [[reward-hacking]] · [[trusted-throughput]]

## 검증기가 느리면 학습 신호가 아니다 — maintainability (2026-10-15 · [[tech-bridge-horthy-state-of-software-factory]])

*"to do reinforcement learning, you need an oracle. You need a verifier. You need something to say, is this code maintainable or not? And maintainability has no fast oracle."*(06:06~06:15) — *"the cost of bad architecture is measured measured in months and years"*(06:04~06:06), *"We don't find out that the code was ugly until 2 months later"*(06:15~06:19). 이 위키의 검증 가능 목표 논의에 **지연(latency)** 축을 더한다: 검증 가능해도 몇 달 뒤에야 판정되면 RL·에이전트 루프의 목표가 되지 못한다. ⚠️ 화자 스스로 *"intuition-based explanation"*(05:51~05:53).

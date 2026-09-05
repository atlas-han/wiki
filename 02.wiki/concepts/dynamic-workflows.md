---
title: Dynamic Workflows
type: concept
category: pattern
tags: [agent, multi-agent, orchestration, parallel-agents, claude-code, long-running]
related: [agent-harness-design, generator-evaluator-pattern, managed-agents, ultracode, verifiable-goals, ralph-wiggum-method, context-resets-and-compaction]
first-seen: anthropic-dynamic-workflows
sources: [anthropic-dynamic-workflows, tech-bridge-claude-code-team-workflow]
created: 2026-05-30
updated: 2026-09-05
---

# Dynamic Workflows

[[claude-code|Claude Code]]가 하나의 prompt를 받아 **오케스트레이션 스크립트를 동적으로 작성**하고, 작업을 subtask로 쪼개 단일 세션에서 **수십~수백 개의 parallel subagent**로 fan-out한 뒤, 결과를 사용자에게 보여주기 전에 **자체 검증**하는 실행 형태. 단일 에이전트의 한 패스로는 너무 큰 문제 — 레거시 코드베이스 전역 버그 헌트, 수백 파일 마이그레이션, 다각도 stress-test — 를 end-to-end로 처리한다. [[anthropic|Anthropic]] 발표: [[anthropic-dynamic-workflows]] (2026-05-28, research preview).

> Work you'd normally plan in quarters now finishes in days.

## 작동 방식 (4단계 루프)

1. **동적 계획(plan dynamically)** — prompt를 기반으로 그 자리에서 계획 수립. 미리 정해진 고정 그래프가 아니라 task에 맞춰 생성.
2. **분할(break into subtasks) + fan-out** — subtask로 쪼개 parallel subagent에 분배.
3. **검증 후 fold-in** — 각 결과는 본 답에 합쳐지기 *전에* 검증됨.
4. **수렴(converge)** — agent들이 독립 각도로 공격하고, *다른 agent가 반박(refute)* 시도, 답이 수렴할 때까지 iterate.

> Agents address the problem from independent angles, other agents try to refute what they found, and the run keeps iterating until the answers converge—which is how a workflow reaches results a single pass can't.

이 **adversarial 수렴**이 dynamic workflows의 본질이자, "단일 패스가 도달 못 하는 결과"의 출처. [[generator-evaluator-pattern]](생성/평가 분리 + skeptical evaluator)을 *오케스트레이션 차원*으로 확장한 형태로 읽을 수 있다.

## 오케스트레이션 아키텍처

- **Coordination outside the conversation** — 조정 로직이 대화 컨텍스트 *바깥*에서 돌아, 작업이 아무리 커져도 plan이 흔들리지 않음. cf. [[managed-agents]]의 session-log 외부화([[context-resets-and-compaction]]) 사상과 동형.
- **Resumable (checkpoint)** — 진행상황이 run 도중 저장되어 중단된 job이 처음부터가 아니라 멈춘 지점에서 재개. long-running(시간~일 단위) 전제.
- **Parallel-first** — 단일 세션 안에서 10s~100s agent가 동시 실행. Bun 사례에선 *파일당 리뷰어 2명*까지 붙는 수백 agent 병렬.

## 활성화

| 방법 | 내용 |
|---|---|
| 직접 요청 | "Create a workflow" 등으로 Claude에게 명시적으로 지시 |
| [[ultracode]] 세팅 | effort menu의 새 Claude Code 세팅. effort를 **xhigh**로 올리고 *Claude가 workflow 사용 시점을 자동 판단* |

- **[[anthropic-claude-code-auto-mode|auto mode]] 권장** — 최선의 경험을 위해 켜둘 것.
- **최초 트리거 시 확인** — 무엇이 실행될지 보여주고 사용자 confirm을 받음.
- **Org admin 비활성화 가능** — managed settings.

## 가용성 (research preview, 2026-05)

- 클라이언트: Claude Code CLI · Desktop · VS Code 확장
- 플랜: Max / Team / Enterprise(admin enabled). Max·Team·API는 기본 on, Enterprise는 launch 시 기본 off
- 플랫폼: Claude API, Amazon Bedrock, Vertex AI, Microsoft Foundry

## 비용·한계

- 일반 Claude Code 세션보다 **토큰 소모가 현저히 큼** → **scoped task로 시작**해 사용량 감 잡기를 권장.
- Research preview 단계.

## 대표 use case

1. **Codebase-wide bug hunt / optimization audit / security audit** — 병렬 검색 + *모든 finding에 독립 검증* → 진짜 이슈만. auth 체크·input validation·unsafe 패턴 hardening 패스에도 동형 적용.
2. **Large migration / modernization** — framework swap, API deprecation, 수천 파일 언어 포팅. → [[bun|Bun]] Zig→Rust 사례.
3. **Critical work checked twice** — 독립 시도 + adversarial agent가 결과를 깨뜨리려 시도한 뒤 전달.

## Bun rewrite — 구체 workflow 사례

[[jarred-sumner|Jarred Sumner]]의 [[bun|Bun]] Zig→Rust 포팅 (99.8% 테스트 통과, ~75만 줄, 11일). 다단계 파이프라인:

1. **Lifetime mapping workflow** — Zig 코드베이스의 모든 struct field에 맞는 Rust lifetime을 매핑.
2. **Port workflow** — 각 `.zig` 파일을 behavior-identical `.rs`로, *파일당 리뷰어 2명*씩 수백 agent 병렬.
3. **Fix loop** — build·test suite가 둘 다 clean해질 때까지 구동.
4. **Overnight optimization** — 불필요한 data copy를 제거하고 각각 PR을 오픈해 최종 리뷰 대기.

## 관련 위키 맥락

- [[agent-harness-design]] — dynamic workflows는 *더 강한 모델이 더 야심찬 harness 조합을 가능케 한다*("the space moves")의 최신 사례. 단발 multi-agent를 넘어 **자기 작성 오케스트레이션**으로 진화.
- [[generator-evaluator-pattern]] — refute/converge가 evaluator 사상의 오케스트레이션판.
- [[ralph-wiggum-method]] — 사람이 짠 고정 루프 vs. Claude가 *동적으로 작성*하는 워크플로의 대비.
- [[verifiable-goals]] — build·test가 clean해질 때까지의 fix loop = 검증 가능한 goal로의 수렴.

## 만든 팀의 증언 — 기원과 병목 (2026-09-05 · [[tech-bridge-claude-code-team-workflow]])

[[anthropic|Anthropic]] Claude Code 팀이 workflows가 **어디서 나왔는지** 밝혔다. 기능 발표문에는 없던 계보다.

> **코드 리뷰가 우리가 이렇게 큰 규모로 의견을 퍼뜨린 첫 번째 사례**였던 것 같아요. 우리는 *"어떻게 하면 모든 버그를 찾아낼 수 있을까?"* 라고 생각했죠. (…) 이렇게 **크게 펼쳐놓은 다음, 그것들을 하나로 합칩니다.** 이것이 바로 우리가 **test-time compute**라고 부르는 것이죠.

구조가 3층이다 — fan-out으로 버그 후보 생성 → **각 버그를 3가지 다른 관점에서 보는 적대적 검토**(→ [[generator-evaluator-pattern]]) → 살아남은 것만 합침. 목적이 찾는 것이 아니라 **거르는 것**이라는 점이 중요하다.

> 이 기능은 마치 **모든 버그를 걸러내고 사용자의 주의가 필요한 가장 중요한 버그만 남겨주는** 것과 같습니다.

### 병목은 map이 아니라 reduce다

이 페이지와 [[ultracode]]·[[managed-agents]]가 지금껏 다룬 것은 전부 **펼치는 쪽**이었다. 팀이 짚는 실제 어려움은 반대편이다.

> 문제는 **정보가 부채처럼 퍼져나가면서, 그 방대한 정보를 다시 걸러내야 한다**는 점입니다. **마치 map-reduce 문제와 같아요.** 그래서 사람이 이해하기 쉽도록 필터링해야 합니다. 그렇지 않으면 **전체 출력값을 다 읽어버리면 미쳐버릴 것 같거든요.**

그리고 신뢰의 출처를 명시한다 — *"**자신감을 키우는 방법은 바로 test-time compute를 문제에 투입하는 것**입니다."* 즉 fan-out은 속도가 아니라 **확신을 사는 수단**으로 쓰인다.

### 에이전트가 토폴로지를 정한다

> **Claude는 사실 자기만의 하네스를 만드는 데 정말 능숙하죠.** Claude가 이 **fan-out 구조가 어떤 모습이어야 하는지, 토폴로지가 어떻게 되어야 하는지, 한 에이전트의 출력을 다음 레벨로 어떻게 연결해야 하는지**를 파악하고 (…)

→ [[self-harness]]

여행 계획 예시로 3층이 그려진다 — 10개 검색 fan-out → 선별 에이전트 → **검증 에이전트** → 최종. 코드 리뷰 밖으로도 일반화된다(*"성능 버그"*, *"일반적인 심층 연구"*).

### 신뢰의 근거가 뜻밖에 고전적이다

> 이것은 **결정론적인 코드 정의 동작과 에이전트 방식의 LLM 동작이 멋지게 혼합**된 것입니다. (…) 이 항목들을 순회하는 **for 루프**를 작성할 때 (…) **'아, 맞다. for 루프는 항목 중 하나라도 건너뛰지 않겠구나'** 라고 생각했다. 저는 그게 제 **신뢰도를 정말 크게 높여준다**고 생각해요.

에이전트가 오케스트레이션을 **코드로 물화**하는 순간 그 층에는 결정론적 보증이 생긴다. [[ai-native-sdlc]]가 lint를 *"예 또는 아니오, 이분법적"* 이라 부르며 결정론 층을 따로 세운 것과 같은 감각이다.

## References

- [[anthropic-dynamic-workflows]]
- [공식 문서 — workflows](https://code.claude.com/docs/en/workflows)
- 관련: [[agent-harness-design]], [[generator-evaluator-pattern]], [[managed-agents]], [[ultracode]]

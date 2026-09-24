---
title: Skill Self-Improvement
type: concept
category: pattern
tags: [agent-skills, feedback-loop, governance, claude-code]
related: [agent-skills, harness-pruning, self-harness, generator-evaluator-pattern, impeccable, adjective-verb-steering, query-to-skill-distillation]
first-seen: tech-bridge-six-agent-skills
sources: [tech-bridge-six-agent-skills, tech-bridge-impeccable-design-steering, tech-bridge-lauren-tan-trusting-agents, tech-bridge-vercel-eve-filesystem-agent, tech-bridge-oracle-agent-memory-harness]
created: 2026-09-05
updated: 2026-09-24
---

# Skill Self-Improvement

**실제 작업 중에 발생한 실패를 관찰해 [[agent-skills|스킬]] 자체의 개선안을 축적하되, 반영은 사람의 검토를 거치는 패턴.** [[tech-bridge-six-agent-skills]]의 `task-observer` 스킬이 이 위키에서의 first-seen이다.

## 문제 — 스킬은 만들기보다 유지가 어렵다

> **가장 큰 문제는 스킬을 만드는 것 자체가 아닙니다. 최신 상태로 유지하는 것입니다.**

핵심 논거는 예측 불가능성이다.

> **한 번 앉아서 에이전트가 저지를 모든 실수를 예측할 수는 없습니다.**

즉 스킬의 빈틈은 설계 시점이 아니라 **사용 시점**에만 드러난다. 그래서 개선의 원천을 회고가 아니라 **작업 중 관찰**에 둔다.

## 구조

| 요소 | 역할 |
|---|---|
| **관찰자** | 작업 중 상시 실행. `CLAUDE.md`에 지시를 넣어 유지한다 |
| **`log.md`** | 스킬별 섹션 아래 **제안된 변경 사항**이 쌓인다 |
| **전역 규칙 파일** | *"어떤 스킬도 실제 고객의 이름을 파일에 기록해서는 안 된다"* 처럼 **모든 스킬에 걸리는** 규칙 |
| **사람의 검토 게이트** | 로그의 교훈을 읽고 **영구 반영 여부를 결정** |

교훈은 두 종류로 나온다 — **금지**(이 도구를 여기 쓰지 마라)와 **대체**(올바른 출처는 이것이다). 금지만 쌓이면 스킬이 점점 방어적이 되므로 대체가 함께 기록되는 것이 중요하다.

## 핵심 설계 — 자동 반영하지 않는다

이 패턴의 값은 자동화가 아니라 **자동화를 멈춘 지점**에 있다.

> 로그에 기록된 내용은 (…) **검토한 후** 영구적으로 반영할지 결정할 수 있습니다. 이렇게 하면 **하나의 잘못된 결과가 에이전트가 영원히 따르는 규칙으로 자동 설정되는 것을 방지**할 수 있습니다.

즉 **관찰은 자동, 승격은 수동**이다. 한 번의 우연한 실패가 영구 규칙이 되면 스킬은 개선되는 게 아니라 오염된다.

## 스코프 선택

전역(`~/.claude`)과 프로젝트별 중에서 **프로젝트별을 권장**한다 — *"각 프로젝트의 교훈이 분리되어 관리하기가 더 쉬워집니다."* 교훈은 대개 그 코드베이스의 사정에 묶여 있기 때문이다.

## 사례 — Logo Hub

[[ai-labs|AI Labs]]의 영상 애니메이션 스킬에서 나온 실화다. 브랜드 로고 SVG를 얻으려고 에이전트가 Logo Hub의 CLI 도구를 썼는데 *"그 도구는 **다른 용도로 만들어진 것이라 실패**했습니다."* 기록된 교훈은 금지 하나와 대체 하나였고, 검토 후 반영되어 *"이제 애니메이션 에이전트는 브랜드 로고를 어디에서 가져와야 하는지 정확히 알고" 있다.*

## 위키에서의 좌표

| 패턴 | 무엇이 무엇을 고치는가 | 승격 게이트 |
|---|---|---|
| **skill-self-improvement** | 실패 관찰 → **스킬** | **사람** |
| [[self-harness]] | 하네스가 **자기 하네스** | 자동(논문 설정) |
| [[harness-pruning]] | 모델 향상 → 하네스 **축소** | 사람(팀 판단) |
| [[generator-evaluator-pattern]] | 채점기 → **산출물** | 루프 내 |

[[tech-bridge-ai-native-skills]]의 스킬 거버넌스가 *"스킬을 어떻게 승인·배포할 것인가"* 였다면, 이 패턴은 *"승인된 스킬이 어떻게 낡아가고 어떻게 갱신되는가"* 를 다룬다. 둘은 같은 수명주기의 앞뒤다.

## 승격 게이트가 커뮤니티일 때 (2026-09-12)

[[tech-bridge-impeccable-design-steering]]의 [[paul-bakaus]]가 [[impeccable]]의 명령을 이렇게 다듬는다 — *"가끔 확신 없는 명령을 만들어서 **커뮤니티로 테스트**하고, **정착하면** 더 많은 사람이 즐거움을 얻는구나 깨닫는다."* `overdrive`가 그 사례(반농담 → 열광).

위 표에 한 행이 더해진다:

| 패턴 | 무엇이 무엇을 고치는가 | 승격 게이트 |
|---|---|---|
| Impeccable 명령 | 제작자 실험 → **스킬의 어휘** | **커뮤니티 반응** |

이 페이지의 *승격은 사람이* 와 같은 원칙이되, 그 사람이 **제작자 한 명이 아니라 사용자들**이고 신호가 *실패 관찰* 이 아니라 *즐거움* 이다. ⚠️ 정착의 기준·기간은 없다.

## 거울상 — 성공한 질의에서, 게이트 없이 (2026-09-19)

[[tech-bridge-vercel-eve-filesystem-agent]]의 [[query-to-skill-distillation]]이 이 패턴의 **정확한 거울상**이다. [[vercel|Vercel]]은 하루 수천 건의 **실제 질의**를 주기적으로 모아 반복되는 형태를 스킬로 압축한다(현재 약 100개).

| | **skill-self-improvement** (09-05) | [[query-to-skill-distillation]] (09-19) |
|---|---|---|
| 원천 | **실패 관찰** | **성공한 실제 질의** |
| 방향 | 금지·대체 규칙을 **더한다** | 반복 형태를 **압축한다** |
| 승격 게이트 | **사람의 검토** | **없음 — 주기적 잡이 자동 증류** |
| 빈도 | 작업 중 상시 | 주기적 배치 |

두 패턴을 나란히 놓으면 **스킬의 수명주기에 입력이 둘**이라는 것이 보인다 — *무엇이 잘 되는가*(수요)와 *무엇이 안 되는가*(실패). Vercel 편은 앞쪽만 자동화했다.

> ⚠️ **이 페이지가 명시적으로 막으려 한 것이 그쪽에서는 열려 있다.** 여기서 *"하나의 잘못된 결과가 에이전트가 영원히 따르는 규칙으로 자동 설정되는 것을 방지"* 가 설계의 핵심이었는데, Vercel 편에는 그 게이트가 없고 **누가 증류된 스킬을 검토하는지 소스가 말하지 않는다.** 09-10 [[tech-bridge-agent-to-agent-as-search|Greze]]의 경고(*"한 번 오염되면 영원히 오염된다"*)가 그대로 적용되는 자리다.

## References

- [[tech-bridge-six-agent-skills]] — first-seen
- 관련: [[agent-skills]] · [[self-harness]] · [[harness-pruning]] · [[generator-evaluator-pattern]] · [[llm-coding-guidelines]]

## 세 번째 경로 — 성공한 긴 세션을 증류하고 옛 버전을 은퇴 (2026-09-24 · [[tech-bridge-oracle-agent-memory-harness]])

[[ignacio-martinez|Ignacio Martinez]]([[oracle|Oracle]])의 **스킬 승격(skill promotion)·워크플로 승격**:

> [승격한다면] 예를 들어, [스킬]이라면 (…) **증류를 통해 원본보다 더 나은 [skill.md]** (…) **이전 버전은 [은퇴시키고], 새 버전으로 업데이트** (36:47~37:04)

재료는 *"서너 시간 들여 하루 종일 성공시킨 워크플로"*(36:24~36:34), 결과는 **나의 어조·업무 방식·선호**가 들어간 스킬 — *"이 라이브러리가 마음에 든다, 이 DB 엔진이 버그가 적었다"*(37:04~37:29). 절차 기억의 예(프런트엔드 작업의 대화 전체 → 반복 가능한 워크플로, 24:33~24:54)도 같은 경로다.

| 패턴 | 무엇에서 | 무엇을 고치는가 | 승격 게이트 |
|---|---|---|---|
| task-observer (이 페이지) | **실패** 관찰 | 규칙·스킬 | **사람** |
| [[query-to-skill-distillation]] (Vercel) | **성공한 질의** 다수 | 새 스킬 추가 | 없음 |
| **스킬 승격 (Oracle)** | **성공한 긴 세션** 하나 | **기존 스킬을 새 버전으로 교체** | ⚠️ **말하지 않음** |

⭐ **버전 교체가 명시된 첫 사례** — 앞의 둘은 추가·수정이었고, 이것은 **옛 버전을 은퇴**시킨다. ⚠️ 그래서 이 페이지의 원칙(*한 번의 우연이 영구 규칙이 되면 오염*)이 가장 날카롭게 걸린다 — **세션 하나에서 증류한 스킬이 이전 버전을 덮어쓰는데, 회귀를 확인하는 [[skill-evals|eval]]이 없다.** ko는 *skill* 을 **"기술"**, *promote* 를 **"홍보"** 로 옮기고 **`skill.md` 라는 파일명을 지웠다**(36:49~36:56).

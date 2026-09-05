---
title: AI-Native SDLC
type: concept
category: pattern
tags: [sdlc, artifact-chain, governance, evals, anthropic]
related: [intent-md, spec-driven-development, verifiable-goals, generator-evaluator-pattern, context-engineering]
first-seen: tech-bridge-ai-native-sdlc
sources: [tech-bridge-ai-native-sdlc]
created: 2026-09-05
updated: 2026-09-05
---

# AI-Native SDLC

**에이전트를 빌드 단계에만 두지 않고 소프트웨어 개발 수명주기 전체에 배치하되, 단계마다 파일 아티팩트를 남겨 연결하는 방식.** [[anthropic|Anthropic]]의 *AI-Native SDLC Playbook*이 출처이고, 이 위키에는 [[tech-bridge-ai-native-sdlc]]의 해설을 통해 들어왔다.

전제:

> **코드가 더 이상 병목이 아닙니다. 당신의 프로세스가 병목입니다.**

논거는 단순하다. 에이전트가 빌드 단계를 크게 줄였는데 **나머지 다섯 단계는 그대로**다. 그러면 총 리드타임의 병목은 자동으로 그쪽으로 옮겨간다.

## 아티팩트 체인

| 단계 | 아티팩트 | 만드는 주체 | 게이트 |
|---|---|---|---|
| Discovery | **[[intent-md\|intent.md]]** | 에이전트가 사람을 **인터뷰** | creator가 되읽고 승인 |
| Spec | **`spec.md`** | intent 승인 시 **hook으로 자동 생성** | 조직 정책·브랜드 가이드라인 |
| Build | **`plan.md`** | intent+spec → plan 모드 | *"의도·사양을 참조하지 않고도 구현 가능한가"* |
| Test | 평가 세트 | 에이전트 (lint·test·E2E·evals) | 결정론적 검사 + continuous evals |
| Deploy | PR | 에이전트가 PR, **별도 인스턴스**가 리뷰 | 권한·승인자·출시일 |
| Maintain | **`intent.md`** | Claude가 로그·티켓에서 **스스로 생성** | → 1단계로 |

**6단계의 출력이 1단계의 입력이 되어 루프가 닫힌다.** 사람이 만든 intent와 기계가 만든 intent가 같은 형식을 공유한다.

## 왜 파일인가 — 컨텍스트 윈도

이 방식의 핵심 근거이고, 문서화 취향과 구별되는 지점이다.

> **모든 단계를 한 에이전트가 수행할 수는 없습니다. 컨텍스트 창이 나타날 것입니다.**

`plan.md`의 합격 기준이 그래서 이렇게 정해진다 — 받은 사람이 **의도·사양을 다시 읽지 않고도** 구현할 수 있어야 한다. 아티팩트는 문서가 아니라 **인계 프로토콜**이다.

`plan.md` 구성: 변경할 **파일** · 작업 **순서** · **위험 요소** · **제약 조건** · **증거**. 마지막이 [[verifiable-goals]]와 만난다 — *"성공 기준과 점검 절차가 반드시 필요"* 하고 그것은 *"**결정론적인 형태의 린팅 및 테스트**"* 로 나타난다.

## 거버넌스 — 이 위키에 처음 들어오는 축

> **계획, 의도, spec.md 파일, 누가 그것들을 수정했는지, 그리고 그것들이 어떻게 발전해왔는지**에 대한 버전을 저장하는 것입니다.

정책은 `agents.md`나 스킬로 인코딩되고 *"이 사슬에 있는 **모든 아티팩트**"* 에 적용된다. 목적은 관료제가 아니라 **측정**이다 — DORA 지표 검증, *"AI가 워크플로에서 실제로 얼마나 효과적인지"*.

⚠️ 해설자의 실무 관찰 — *"제가 함께 일해 본 회사들은 **이 부분을 특히 어려워**합니다."*

## 결정론 층과 에이전트 층의 분리

이 패턴은 두 층을 계속 구분해서 쓴다.

| 결정론 층 | 에이전트 층 |
|---|---|
| lint (*"예 또는 아니오, 이분법적"*) · 테스트 · 빌드 · hook · 권한 게이트 | 인터뷰 · spec 작성 · 계획 · PR 리뷰 · 보안 검토 · 진단 |

**hook**이 이 경계의 실행 장치다 — 구현이 끝나면 **계획을 자동 업데이트**, **특정 폴더 접근 차단**, **승인 안 된 npm 업그레이드 차단**.

같은 감각이 [[tech-bridge-claude-code-team-workflow]]에도 나온다. 거기서는 에이전트가 오케스트레이션을 **for 루프 코드로 물화**하는 순간 결정론적 보증이 생긴다고 말한다.

## Continuous Evals

> **모든 스킬 변경이나 모델 업그레이드에 평가를 적용** (…) **지속적 통합 과정에서 지속적인 평가.**

형태가 소박해서 실행 가능하다 — 해결한 문제 **20개 정도**와 예상 결과를 모아 두고, **새 모델·새 스킬·업무 방식의 근본적 변화**마다 돌려 **퇴보**를 본다.

이것은 [[generator-evaluator-pattern]]을 **하네스 자체의 회귀 테스트**로 돌려놓은 것이다. [[tech-bridge-multimodal-commerce-agent]]가 *산출물의 단계마다* 채점기를 붙였다면, 여기서는 *하네스가 바뀔 때* 채점한다.

## 병렬화와 배포

빌드는 계획에서 자동으로 갈라진다 — *"계획을 **독립적으로 수행할 수 있는 다양한 작업으로 나누고**, 일부가 병렬로 진행될 경우 **worktree**를 사용."* → [[persistent-agent-teams]]

PR 리뷰는 **비동기**이고 작성자와 리뷰어를 분리한다 — *"**Claude 코드 리뷰어가 별도의 인스턴스로**."*

## 자율 유지보수

가장 새로운 부분이다. 트리거가 사람이 아니다.

> **침해, 새 티켓, Slack 채널 메시지 또는 일정**과 같은 상황이 발생하면 (…) Claude는 **비동기적으로 문제를 진단**하고, **로그 또는 티켓·메시지를 기반으로 자체 intent.md를 생성**합니다.

*"페이지 오류"*, *"API 사용량 제한이 급격히 증가"* 같은 임계값을 걸어 두고, 전부 *"**사용자가 컴퓨터에 접속하기도 전에**"* 일어난다.

## 위키에서의 좌표

[[spec-driven-development]]가 spec→코드였다면, 이 패턴은 **앞에 intent를 붙이고 뒤에 유지보수 루프를 붙여 체인을 닫는다.** 스펙트럼 안에서의 위치를 해설자 본인이 그린다.

> **반복문부터 그래프 공학, 완전 자동화된 반복문, 대규모 오케스트레이션 시스템, 나아가 문명 공학(civilization engineering)** 에 이르기까지 매우 다양합니다.

[[ralph-wiggum-method]](반복문)와 [[dynamic-workflows]](오케스트레이션)가 같은 스펙트럼의 다른 지점으로 배치되는 셈이다.

채택 태도는 온건하다 — SuperPowers·BMAD를 쓰고 있다면 *"**기존 방식을 완전히 버릴 필요는 없다**"*.

## ⚠️ 검증되지 않은 것

- *"우리는 **두 배 더 빠릅니다**"* — 빌드 단계 단축에 대한 이 주장의 **출처·측정 방법이 소스에 없다.**
- 이 위키는 **Anthropic 원문서를 직접 ingest하지 않았다.** 전부 제3자 해설을 통한 것이다.

## References

- [[tech-bridge-ai-native-sdlc]] — first-seen
- 원문서(미ingest): <https://claude.com/blog/the-ai-native-sdlc-playbook>
- 관련: [[intent-md]] · [[spec-driven-development]] · [[verifiable-goals]] · [[generator-evaluator-pattern]] · [[context-engineering]] · [[persistent-agent-teams]]

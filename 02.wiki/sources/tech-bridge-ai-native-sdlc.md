---
title: "Tech Bridge — Claude Code 팀이 공개한 INTENT.MD와 AI-Native SDLC"
type: source
tags: [sdlc, intent, spec-driven, governance, subagent, worktree, evals, video]
source-url: https://www.youtube.com/watch?v=rGaSkBWjoHA
source-type: video
author: Tech Bridge (한영자막 재배포) · 해설자 Switch Dimension 강사(익명) · 원문서 Anthropic
date-published: 2026-09-04
ingested: 2026-09-05
created: 2026-09-05
updated: 2026-09-05
---

# Tech Bridge — Claude Code 팀이 공개한 INTENT.MD와 AI-Native SDLC

[[tech-bridge|Tech Bridge]]가 한영자막을 입힌 15:11 해설 영상. → [[2026-09-04_Claude Code 팀이 새로 공개한 INTENT.MD의 정체와 AI-Native 개발 방식|raw 캡처]]

> ⚠️ **이것은 [[anthropic|Anthropic]] 발표가 아니라 제3자 해설이다.** 해설자는 [[switch-dimension|Switch Dimension]] 강사이고 **본인 이름은 소스에 없다.** 해설 대상은 설명란이 링크한 Anthropic 공식 문서 *AI-Native SDLC Playbook*(<https://claude.com/blog/the-ai-native-sdlc-playbook>)이다. 아래에서 Anthropic의 제안과 해설자의 실무 의견은 구분해 적었다.

한 줄 테제:

> **코드가 더 이상 병목이 아닙니다. 당신의 프로세스가 병목입니다.**

이 소스는 위키의 [[spec-driven-development]] 축을 **양쪽으로 확장한다.** 기존 축은 "spec을 쓰고 코드를 만든다"에서 시작했는데, 여기서는 **spec 앞에 intent가 붙고** spec 뒤로 배포·유지보수까지 이어진 뒤 **유지보수의 출력이 다시 intent가 되어 루프를 닫는다.**

## 아티팩트 체인 — 이 문서의 핵심 구조

| 단계 | 아티팩트 | 만드는 주체 |
|---|---|---|
| Discovery | **`intent.md`** | 에이전트가 사람을 **인터뷰**해서 종합 → [[intent-md]] |
| Spec | **`spec.md`** | intent 승인 시 **hook으로 자동 생성** |
| Build | **`plan.md`** | 엔지니어가 intent+spec을 plan 모드에 투입 |
| Test | (평가 세트) | 에이전트가 lint·test·E2E·evals |
| Deploy | PR | 에이전트가 PR, **별도 인스턴스**가 리뷰 |
| Maintain | **`intent.md`** | Claude가 로그·티켓·Slack에서 **스스로 생성** |

→ [[ai-native-sdlc]]

## intent.md — 백로그를 대체하는 아티팩트

전통적 경로는 *"사용자 입력, 사용자 스토리, 스토리 포인트, **소유권 이전, 인수인계**"* 였다. 새 경로는 창시자가 Claude와 아이디어를 구상하고 그 결과를 기록하는 것이다.

정의가 명확하다 — **사람이 읽을 수 있고 기계가 처리할 수 있는(human readable and machine actionable)** 파일.

**creator는 전문가가 아니어도 된다.**

> **버그 제보를 하는 고객**일 수도 있습니다. **제품 관리자**가 새로운 기능에 대한 아이디어를 가지고 있을 수도 있습니다. **개발자**가 프로세스 개선 사항을 기록하고 싶어할 수도 있습니다.

그리고 사람이 되읽는 절차가 붙는다 — *"의도를 처음 제시한 사람이 담당자가 작성한 내용을 다시 검토하여 수정하고 **양측 모두 만족하는지 확인**."*

해설자는 자기 용어가 다름을 밝힌다 — *"저는 그것을 **의도가 아니라 발견(discovery)** 이라고 부르지만, 결국 같은 개념입니다."*

## 왜 아티팩트 체인인가 — 컨텍스트 윈도

이 영상에서 가장 실용적인 통찰이고, 문서화 취향과 구별되는 지점이다.

> **소프트웨어 개발 수명주기의 모든 단계를 한 에이전트가 모두 수행할 수는 없기 때문입니다. 컨텍스트 창이 나타날 것입니다.** (…) 계획과 의도를 문서로 정리하여 각 담당자에게 전달하면, 담당자는 **이전 대화 내용을 이해하지 못한 채 처음부터 다시 시작**할 수 있습니다.

`plan.md`의 합격 기준도 이 논리로 정해진다 — *"엔지니어가 **설계 의도나 사양 문서를 참조하지 않고도** 변경 사항을 구현할 수 있는 수준."*

이것은 [[context-resets-and-compaction]]과 [[context-engineering]]이 다루는 문제에 대한 **조직 차원의 답**이다. 컨텍스트를 압축하는 대신 **파일 시스템으로 외재화**한다.

`plan.md`의 구성 — 변경할 **파일**, 작업 **순서**, **위험 요소**, **제약 조건**, 그리고 **증거**. 마지막이 [[verifiable-goals]]와 만난다.

> 작업이 제대로 완료되었는지 확인하기 위해 일종의 **성공 기준과 점검 절차**가 반드시 필요합니다. 이는 **결정론적인 형태의 린팅 및 테스트**로 나타날 수 있습니다.

## 거버넌스 — 이 위키에 처음 들어오는 축

Anthropic의 제안은 아티팩트에 **버전과 소유권을 남기라**는 것이다.

> **계획, 의도, spec.md 파일, 누가 그것들을 수정했는지, 그리고 그것들이 어떻게 발전해왔는지**에 대한 버전을 저장하는 것입니다.

해설자가 이유를 붙인다 — **DORA 지표**를 검증하거나 *"AI가 워크플로에서 실제로 얼마나 효과적인지"* 확인하려면 필요하다. 그리고 실무 관찰 — *"제가 함께 일해 본 회사들은 **이 부분을 특히 어려워**합니다."*

정책은 `agents.md`나 스킬로 인코딩되고, *"이 사슬에 있는 **모든 아티팩트**에 적용"* 된다. [[tech-bridge-ai-native-skills]]의 스킬 거버넌스가 스킬 하나 단위였다면, 여기서는 **파이프라인 전체**가 대상이다.

배포 게이트의 예 — *"특정 권한이 부여되지 않았거나, 특정 담당자가 승인하지 않았거나, 또는 **출시일이 도래하지 않은** 경우에는 배포를 차단."*

## 빌드 — hook, subagent, worktree

**hook이 프로세스를 궤도에 유지하는 장치로 제시된다.** 예 셋: 구현이 끝나면 **계획을 업데이트**, **특정 폴더 접근 차단**, **승인 안 된 npm 업그레이드 차단**.

lint의 성질을 새삼 정의하는 대목이 있다 — *"**결정론적** 또는 코딩된 방식 (…) **예 또는 아니오, 이분법적인 답변**."* 이 영상은 결정론적 게이트와 에이전트 판단을 계속 구분해 쓴다.

병렬화는 계획에서 자동으로 갈라진다 — *"계획을 **독립적으로 수행할 수 있는 다양한 작업으로 나누고**, 일부가 병렬로 진행될 경우 **worktree**를 사용."* → [[persistent-agent-teams]]

권한에 대한 해설자의 실무 조언 — 보안이 강한 환경에서는 *"**미리 설정된 권한**으로 저장소에 접근하여 작업을 시작하고, 진행하면서 수락"* 하되, 도구·웹 소스·패키지 정책을 세워 두면 *"**관리자의 개입 없이도** 에이전트가 훨씬 빠르게 작동."*

## 테스트 — 사람 앞에서 최대한 끝낸다

목표가 바뀐다 — *"**인간 엔지니어나 QA가 접근하기 전에** 에이전트가 가능한 한 많은 테스트를 수행."*

브라우저 층은 **Playwright · TestSprite · Cursor Browser**로, 산출물은 **스크린샷과 화면 녹화**다.

### Continuous Evals

> Anthropic은 **모든 스킬 변경이나 모델 업그레이드에 평가를 적용**할 것을 권장합니다. (…) **지속적 통합 과정에서 지속적인 평가.**

구체적 형태가 소박해서 오히려 실행 가능하다 — 해결한 문제 **20개 정도**와 예상 결과 세트를 모아 두고, **새 모델·새 스킬·업무 방식의 근본적 변화**가 있을 때마다 돌려 **퇴보(regression)** 를 본다.

이것은 [[generator-evaluator-pattern]]의 채점기를 **파이프라인 자체의 회귀 테스트**로 돌려놓은 형태다. [[tech-bridge-multimodal-commerce-agent]]가 *산출물의 단계마다* 채점기를 붙였다면, 여기서는 *하네스가 바뀔 때* 채점한다.

## 배포와 자율 유지보수

PR 리뷰는 **비동기**이고 작성자와 리뷰어를 분리한다 — *"**Claude 코드 리뷰어가 별도의 인스턴스로** 해당 댓글을 검토."*

**유지보수가 이 문서에서 가장 새로운 부분이다.** 전통적으로는 *"새벽 3시에 서버가 다운되었다는 알림"* 이거나 *"백로그에 너무 많은 작업이 있어서 **완전히 무시**"* 되는 단계였다.

> **침해, 새 티켓, Slack 채널 메시지 또는 일정**과 같은 상황이 발생하면 사람이 직접 유지보수를 수행하지 않고도 Claude가 호출됩니다. Claude는 **비동기적으로 문제를 진단**하고, **로그 또는 티켓·메시지를 기반으로 자체 `intent.md`를 생성**합니다.

**루프가 닫힌다** — 6단계의 출력이 1단계의 입력이 된다. 트리거의 예로 *"페이지 오류"*, *"API 사용량 제한이 급격히 증가"* 를 들고, 전부 *"**사용자가 컴퓨터에 접속하기도 전에**"* 일어난다.

## 유보 — 채택에 대한 해설자의 입장

> 사실 모든 사람에게 맞는 **만능 해결책은 없습니다.** 만약 여러분이 **SuperPowers나 BMAD** 같은 것을 사용하고 있거나 (…) **기존 방식을 완전히 버릴 필요는 없다**고 생각합니다.

그리고 스펙트럼을 편다 — *"**반복문부터 그래프 공학, 완전 자동화된 반복문, 대규모 오케스트레이션 시스템, 나아가 문명 공학(civilization engineering)**."* [[ralph-wiggum-method]](반복문)과 [[dynamic-workflows]](오케스트레이션)가 같은 스펙트럼의 서로 다른 지점으로 배치되는 셈이다.

## ⚠️ 검증되지 않은 수치

> Anthropic이 말하는 요점은 (…) **우리는 두 배 더 빠릅니다.**

빌드 단계 단축에 대한 이 주장의 **출처·측정 방법은 이 영상에 없다.** 원문서를 직접 확인하기 전에는 위키에서 근거로 쓰지 않는다.

## 이 소스가 남긴 것

**새 개념 2개** — [[ai-native-sdlc]], [[intent-md]].

**새 엔티티 1개** — [[switch-dimension]].

**보강된 기존 페이지** — [[spec-driven-development]](앞에 intent, 뒤에 유지보수 루프가 붙어 체인이 됨), [[verifiable-goals]](plan.md의 증거·성공 기준), [[context-engineering]]·[[context-resets-and-compaction]](아티팩트 체인 = 컨텍스트의 파일 시스템 외재화), [[generator-evaluator-pattern]](continuous evals = 하네스 회귀 테스트), [[anthropic]], [[tech-bridge]].

**⚠️ 표시한 것** — 해설자 본인 이름 없음, 언급된 Claude Code 창시자 이름이 소스 안에서 두 갈래("Vis journey"/"Baris")로 갈려 미확정, "2배 빠르다"의 근거 부재, "Matt PCO"의 정체 미확정, 촬영 시점 미확정.

## References

- 원본: <https://www.youtube.com/watch?v=rGaSkBWjoHA> (15:11)
- 해설 대상 원문서: <https://claude.com/blog/the-ai-native-sdlc-playbook> (⚠️ 이 위키가 직접 ingest한 적 없음)
- raw: [[2026-09-04_Claude Code 팀이 새로 공개한 INTENT.MD의 정체와 AI-Native 개발 방식]]
- [[switch-dimension]] · [[anthropic]] · [[tech-bridge]]
- 관련: [[ai-native-sdlc]] · [[intent-md]] · [[spec-driven-development]] · [[verifiable-goals]] · [[context-engineering]]

---
title: "Tech Bridge — 프롬프트 대신 명세(Spec)를 작성할 때"
type: source
tags: [spec-driven-development, spec-kit, github, copilot, mcp, video]
source-url: https://www.youtube.com/watch?v=F_smvU3oqbU
source-type: video
author: Tech Bridge (한국어 자막 재배포) · 발표자 Microsoft 365 MVP / cloud-native architect (en-orig ASR: "Luna Diva")
date-published: 2026-08-29
ingested: 2026-08-29
created: 2026-08-29
updated: 2026-08-29
---

# Tech Bridge — 프롬프트 대신 명세(Spec)를 작성할 때

[[tech-bridge|Tech Bridge]]가 한영자막을 입힌 22:07 강연. 발표자는 Microsoft 365 MVP이자 cloud-native architect로, 고객 팀의 agentic 개발 도입을 GitHub Enterprise · GitHub Copilot · [[github-spec-kit|Spec Kit]](`specify` CLI)로 돕는다. 한 줄 테제:

> Stop treating the prompt as the main artifact and start treating the specification as that main artifact.

본문은 **en-orig 자동 자막**을 재구성. ASR이 이름을 "Luna Diva" / "Spekit" / "Motor Cortex Protocol"로 읽는다 — 각각 발표자명 미확인, Spec Kit, [[model-context-protocol|MCP]]로 해석. 인용은 자막이 분명한 구간에 한정.

## 왜 프롬프트가 약한 기초인가 (00:00–02:00)

Prompt-first AI 코딩은 시작을 빠르게 해 줬다. 그러나 **큰 프로젝트·엔터프라이즈·다인 팀**에서는 프롬프트가 약한 기초가 된다.

| 프롬프트 | 스펙 |
|---|---|
| 보통 **사적** (세션 안에만) | 저장소·Git history의 일부 |
| **일시적** | 다음 기능의 출발점 |
| **리뷰하기 어려움** | constitution / spec / plan을 팀이 리뷰 |
| 빌드는 되지만 요점을 완전히 빗나가기도 | 무엇을·왜를 먼저 고정 |

Prompt-first의 루프: 지시 작성 → 모델이 코드 작성 → **surprise**. 좋은 놀람일 때도 있지만, 오후 내내 "왜 이렇게 됐지"를 푸는 경우가 있다.

## 멘탈 모델: Constitution → Spec → Plan → Task → Implement (02:00–04:30)

발표자가 "이 모델이 이후 전부 이해되게 한다"고 못 박는 코어. 시작용 네 단계이지 전체 목록이 아니다(clarify / analyze 등은 문서 참조).

1. **Constitution** — 프로젝트·팀보다 클 수 있는 **깨지지 않는 뿌리**. testable by design, 보안 표준, 엔터프라이즈 가이드, 팀 규칙 등 코딩 에이전트가 지켜야 할 must-have.
2. **Spec** — 기능 명세. *무엇을 만들 것인가*. 기능·요구사항만. **how / 스택 / 기술 세부 금지**.
3. **Plan** — how. 배포 타깃, 스택, 프레임워크, 버전.
4. **Task** — 구현 순서에 맞는 논리적 청크. 그다음 implement.

반복 강조: **AI가 뱉는 모든 문서(constitution, spec, plan)를 사람이 읽고 팀이 동의할 것.** 같은 페이지에 서야 나중에 원하는 품질이 나온다.

스펙은 저장소·Git history의 일부가 된다. 다음 기능은 이 베이스 위에 새 spec을 추가하고 같은 프로세스를 돈다.

## 데모: Build 2026 세션 플래너 MCP (04:30–19:50)

대상 앱: Microsoft Build 2026 세션 카탈로그에 에이전트가 붙는 **세션 플래너 MCP 서버**. 공식 CLI는 있었지만 MCP가 없어서, 빈(에 가까운) 레포에서 Spec Kit로 처음부터 만든다.

### 설치

- 시작 레포: GitHub Copilot instructions, VS Code 설정, 미리 적어 둔 데모 프롬프트, gitignore. MCP 서버 코드는 없음.
- `specify init` + **integration = Copilot** (에이전트별로 커스텀 인스트럭션을 심는다). 빈 레포가 아니라서 확인 질문이 뜨고, Windows라 PowerShell 스크립트를 고른다.
- 생김새: `.specify/` 폴더. 발표자: **"마법이 아니다. 마크다운과 스크립트다."** 그걸 이해해야 Spec Kit를 demystify할 수 있다.

### Constitution — 이 데모의 여섯 원칙 (07:30–11:00)

세션 플래너 MCP에 맞춰 넣은 unbreakable rules (범용 템플릿이 아님):

1. **Grounded only** — 없는 세션을 지어내지 말 것.
2. **Time-aware** — "곧 시작"을 틀리면 안 되므로 시간이 1급 제약.
3. **Agent-safe** — MCP 도구의 안전한 설계.
4. **HTTP-safe** — 공개 엔드포인트에 올려도 될 것.
5. **Testable by design**
6. **Privacy by default**

`/speckit.constitution`에 이 원칙을 붙이면 `.specify/memory/constitution.md`로 통합된다. 데모는 생성 대기 대신 미리 만든 브랜치로 결과물을 보여 준다.

### Specify — what only (11:00–13:30)

기능 요구: 에이전트가 Build 세션 JSON에 접근. 데이터 모델(소스 필드)과 MCP 도구 — 세션 검색, 세션 단건, 지금 진행 중인 세션 등. **구현 세부는 없음.**

`/speckit.specify` 실행 시 모호하면 스펙에 표시하거나 사용자에게 개방형/객관식 질문을 한다. 결과 `specs/` 아래 사용자 스토리(검색·상세·현재 세션 등)가 constitution must-have에 맞춰 재작성된다.

### Plan — how (13:30–15:30)

기술 선택: TypeScript, Node.js, MCP 서버, HTTP transport, 배포·설정. `/speckit.plan`은 constitution + spec을 읽고 기술 계획을 채운다.

주의: 버전을 안 적으면 모델이 **임의 버전을 채워 넣는다** (최신이 아닐 수 있음). 특정 버전이 필요하면 plan 프롬프트에 명시.

결과는 같은 `specs/`에 추가 마크다운 — 예: stateless HTTP 서버, TypeScript 버전.

### Tasks → Implement → 동작 확인 (15:30–19:50)

`/speckit.tasks`는 또 하나의 마크다운. 페이즈·사용자 스토리로 쪼개고, 보일러플레이트(Node 설정, `package.json`, Dockerfile, 선행 조건)를 논리적 순서로 둔다. 중간 단계 **analyze / clarify를 돌리라고 권하지만**, 원하면 바로 implement 가능.

`/speckit.implement`는 task를 코드로 바꾸고, constitution의 testable-by-design 때문에 **테스트도 깔아** 컴파일·동작 검증 루프를 돈다.

데모 끝: 생성된 소스를 띄우고 **MCP Inspector**(로컬 node 모듈)로 연결 → `list tools` → `search session` 실행 → 오프닝 키노트 결과가 나온다. "작동하는 MCP 서버가 실제로 만들어졌다."

## 내일 할 세 가지 (20:00–21:30)

워크플로 전체를 내일 바꾸지 말 것. **작고 의미 있는 실제 기능 하나**에 대해:

1. **프롬프트 전에 스펙을 쓴다.** what/why 먼저, how는 나중에.
2. **constitution에 팀 비협상 규칙 2–5개.** living document. 엔터프라이즈·다른 팀에서 배워 쌓인다. 프로젝트보다 클 수 있다. 작게 시작.
3. **AI가 뱉은 문서를 전부 리뷰한 뒤 구현.** 첫 기능이 끝나면 다음 기능도 Spec Kit로.

슬라이드 링크: Spec Kit 문서, 데모와 같은 작업 코드가 있는 Git 저장소(발표자가 "funny business 없음"을 보라고 공유), 연락처.

## 위키 합성

- [[spec-driven-development]]의 1차 영상 소스. 프롬프트를 메인 아티팩트에서 내리는 주장이 [[verifiable-goals]]·[[sprint-contract]]·[[outcome-engineering]]과 동형.
- Spec Kit는 [[harness-engineering]] AI Layer(Global Rules / Context Docs)를 **슬래시 커맨드 + 저장소 마크다운**으로 제품화한 하니스. 발표자 본인이 "마크다운과 스크립트"라고 말한다.
- 데모의 MCP 서버는 [[model-context-protocol]] 도구 표면. constitution의 grounded-only / agent-safe / HTTP-safe가 그 도구의 가드레일.
- [[agent-org-adoption]]의 "프롬프팅 대신 기획"과 같은 *how → what* 전환의 도구면.

## 핵심 인용 (en-orig)

> Stop treating the prompt as the main artifact and start treating the specification as that main artifact.

> Review everything AI puts out, but especially if you use these spec-driven development frameworks, review every single document the thing throws at you.

> There's no funny business going on. It's just markdown and scripting.

> Don't rewrite your entire workflow tomorrow. Pick one real feature ... write a specification before you prompt. Capture what and why first, not how.

## 등장 개체·개념

- 채널: [[tech-bridge]]
- 발표자: Microsoft 365 MVP / cloud-native architect (ASR "Luna Diva" — 본명 미확인, 페이지 없음)
- 도구: [[github-spec-kit]], GitHub Copilot (페이지 없음), [[model-context-protocol|MCP]]
- 개념: [[spec-driven-development]] (메인), [[verifiable-goals]], [[sprint-contract]], [[harness-engineering]], [[outcome-engineering]]

## References

- [원문 영상](https://www.youtube.com/watch?v=F_smvU3oqbU)
- 원문 캡처: `01.raw/articles/2026-08-29_프롬프트 작성은 그만두세요. 이제 명세(Spec)를 작성할 때입니다.md`
- Spec Kit: <https://github.github.io/spec-kit/> · <https://github.com/github/spec-kit>

---
title: Agent Skills
type: concept
category: pattern
tags: [skills, harness, governance, mcp, workflow]
related: [harness-engineering, spec-driven-development, frontier-engineering, agent-org-adoption, model-context-protocol, self-harness, prompt-injection, generator-evaluator-pattern, claude-code, agent-knowledge-sourcing, retrieval-augmented-generation, agent-memory, adjective-verb-steering, impeccable, no-one-shot-design]
first-seen: tech-bridge-ai-native-skills
sources: [tech-bridge-ai-native-skills, tech-bridge-flutter-ai-workflow, tech-bridge-six-agent-skills, tech-bridge-agent-knowledge-four-ways, tech-bridge-cursor-legacy-refactoring, tech-bridge-company-brain-security, tech-bridge-agent-to-agent-as-search, tech-bridge-impeccable-design-steering, tech-bridge-lauren-tan-trusting-agents, tech-bridge-graft-code-knowledge-graph]
created: 2026-08-31
updated: 2026-09-15
---

# Agent Skills

조직 know-how를 에이전트가 실행 가능한 단위로 묶은 것. [[imad-touil|Imad Touil]]([[tech-bridge-ai-native-skills]])이 hooks / [[model-context-protocol|MCP]] / sub-agents와 구분해 first-class로 둔다. [[harness-engineering]] AI Layer의 "Skills & MCP" 칸을 **조직·거버넌스 면**으로 확장한 페이지.

> AI-native organizations run on skills — and ungoverned skills become a new class of technical debt.

## 스택에서의 자리

| 루프 | 역할 |
|---|---|
| **Inner harness** | coding agent: context · tools/MCP · memory · **skills loader** |
| **Outer workflows** | skills · sub-agents · MCP · hooks — Touil은 워크플로를 "harness blueprints"라고 부름 |

Hooks는 이벤트 트리거, MCP는 대개 **제공 도구를 소비**, sub-agent는 컨텍스트 위임. **구조화된 가치가 모이는 곳은 skills.**

## 설계 원칙 (마이크로서비스 유추)

Reusable · discoverable · portable across harnesses(Claude Code 스킬이 Cursor에서도) · specialized(모놀리스 금지) · composable · deterministic · cost efficient.

비용 축은 **progressive disclosure**: 맞는 스킬을 맞는 양·타이밍에 넣어 토큰을 줄인다.

## 거버넌스

거버넌스 없으면 부채: 중복, 품질(최신 모델 대비 미검증), 발견 불가, 오너 없음, 조합 충돌, [[prompt-injection]]/스킬 내 스크립트, ACL 부재.

처방: 개인 → 팀 → 중앙 플랫폼(catalog+metadata, MCP/CLI, 의존성, 버전, eval, ACL) + 도메인 오너. 다음 단계는 registry/IDP, static eval, auto-evolve — 가드레일 없이 돌리면 부채를 증폭([[self-harness]]와 맞닿되 조직 전제가 다름).

15팀×6개월은 **시뮬레이션**. 현장 A/B가 아님.

## 위키 자매

- [[frontier-engineering]]: 개인 steering/skills 습관. 여기는 그 파일을 **전사 카탈로그**로 올리는 면.
- [[spec-driven-development]]: spec–plan–task는 product increment 한 칸. 스킬 거버넌스는 그 앞뒤 SDLC까지.
- [[agent-org-adoption]]: 도구가 같아도 방식·가시성이 가른다.

## 실무자 관점: 언제 쓰고, 어떻게 만들고, 무엇을 경계하나 (2026-09-02)

[[ivanna-kacevica|Ivanna Kaceviča]]([[tech-bridge-flutter-ai-workflow]])가 같은 개념을 **한 개발자의 프로젝트** 수준에서 말한다. Touil의 카탈로그가 *조직*의 progressive disclosure라면 이쪽은 *파일 하나*의 progressive disclosure다.

### 세 층위 — 읽히는 시점으로 구분

| 층위 | 형태 | 읽는 시점 |
|---|---|---|
| Prompt | 메시지 | 그때그때 |
| Rules | 프로젝트 지식 마크다운 하나 | **항상** |
| Skills | 마크다운 + 스크립트·에셋·레퍼런스 | 에이전트가 **필요하다고 판단할 때만** |

> 프로젝트 규칙에 입력한 모든 규칙을 읽는 대신, 이 특정 작업과 관련된 스킬만 불러오면 됩니다.

### 스킬을 쓸 두 가지 신호

1. **반복** — *"스킬을 쓰기 시작해야 한다는 주요 지표는 반복입니다."*
2. **한 번만 하지만 자동화하고 싶은 워크플로** — 모바일 광고 설치처럼 앱당 한 번인 큰 작업. 남의 스킬을 가져와 **쓰고 지운다.**

두 번째는 위의 마이크로서비스 유추(재사용·조합)가 놓친 용례다. 일회성 스킬은 재사용이 아니라 **절차의 임대**이고, 그래서 곧장 공급망 문제가 된다 — 아래 보안 절.

### description이 트리거다

> 스킬 설명에 "앱에 새 기능을 추가할 때 사용"이라고 명시하는 것이 매우 중요합니다. 그러면 에이전트가 새 기능 추가를 요청받을 때마다 "아, 이 내용을 모두 읽어야겠군 (…)"라고 인식하게 됩니다.

"discoverable" 원칙의 파일 수준 구현. 발견 조건이 설명에 적혀 있지 않으면 progressive disclosure는 작동하지 않는다.

### 만드는 법: 관리자, 카피라이터 아님

> 거의 모든 툴에는 스킬 생성기 명령이 있고 (…) 하지만 작성된 내용을 확인하고 수정하는 것은 중요합니다. (…) 단순히 자동화에만 의존하지 말고, 어느 정도 통제권을 가지는 것이 중요합니다.

추천 1순위 스킬이 **스킬을 만드는 스킬**(skill creator)이다 — `SKILL.md`만 쓰고 끝내기 쉬운데 스크립트·에셋·레퍼런스까지 생성해 준다는 이유. Touil의 "auto-evolving skills에 가드레일 전제"를 개인 수준에서 *사람이 읽고 고친다*로 대신한다.

### 보안: MD 파일은 무해하지 않다

> 우리가 스킬이라고 생각하는 것은 그저 무해한 MD 파일일 뿐이라고 여기기 때문입니다. 무슨 문제가 생길 수 있을까요? (…) MD 파일은 사실 그렇게 무해한 파일이 아닙니다.

위 거버넌스 표의 "Security" 한 줄이 실무자 입에서 구체화됐다 — 인터넷에서 받은 스킬이 *"에이전트에게 당신의 키를 훔치도록"* 지시할 수 있고, *"겉보기에는 멀쩡해 보여도 숨겨진 Unicode 지시사항"*이 있을 수 있다. 처방: **공식 출처**(Google의 Flutter·Dart 스킬, 패키지 maintainer 스킬) 우선, 아니면 **내용을 읽을 것**, 첫 검색 결과를 받지 말 것. → [[prompt-injection]]의 스킬 파일 벡터.

### 유지보수는 저장소 하나만큼

Flutter 팀 진행자: 공식 스킬의 *"유지 관리해야 할 양이 거의 새로운 저장소를 만드는 것과 맞먹을 정도"*. 발표자는 커뮤니티 목록을 **최소 2주에 한 번** 점검한다. 거버넌스 표의 "Quality — 최신 모델 대비 미검증" 부채가 실제로 어떤 노동인지에 대한 유일한 현장 수치.

### 추천 스킬 5개와 그 자리

| 스킬 | 이 위키에서의 자리 |
|---|---|
| Skill Creator | 위 "만드는 법" |
| Code Review + PR triage **교차 확인** | [[generator-evaluator-pattern]] — 두 evaluator가 서로의 보고서를 본다 |
| 새 기능 스캐폴딩 | 반복 신호의 전형. description=트리거 |
| [[flutter|Flutter]] Row/Column 레이아웃 | 학습 데이터가 적은 도메인의 지식 주입 — [[sutton-bitter-lesson]] 반례 |
| 스크린샷 시각 QA | [[verifiable-goals]]의 UI verifier를 **에이전트가 보게** 함 |

리뷰 스킬의 남은 한계가 정확하다 — *"코드가 좋은지는 평가할 수 있지만 그 코드가 필요한지는 항상 판단할 수 없다."* [[signal-layer]]의 채점기 경계선이 코드 리뷰 안에도 있다.

> ⚠️ 효과 진술은 모두 일화("1년 넘게 잘 됐다")이고 측정치가 없다.

## 스킬이 담는 지식의 범위가 넓어진다 (2026-09-05 · [[tech-bridge-six-agent-skills]])

지금까지 이 페이지의 소스들([[tech-bridge-ai-native-skills]]·[[tech-bridge-flutter-ai-workflow]])은 전부 **기술 지식**을 스킬에 담았다 — 프레임워크 사용법, 라이브러리 버전, 코딩 규약. [[ai-labs]]의 6종 카탈로그는 그 범위를 두 방향으로 넓힌다.

### ① 스킬이 자기를 고친다

`task-observer`는 작업 중 실패를 관찰해 스킬 개선안을 로그에 쌓되 **반영은 사람이 결정한다.** → [[skill-self-improvement]]

> **가장 큰 문제는 스킬을 만드는 것 자체가 아닙니다. 최신 상태로 유지하는 것입니다.**

### ② 제품·시장 지식이 스킬에 들어간다

[[corey-haines]]의 마케팅 스킬 48종 중 **온보딩 · 페이월 · churn** 3종이 앱에 직접 박힌다. 왜 스킬이어야 하는지에 대한 논거가 명확하다.

> 이런 패턴은 다른 앱에서도 많이 보셨을 겁니다. 하지만 **에이전트에게 페이월 추가를 요청하면, 일반적으로 이런 선택을 하지 않습니다. 그 원칙이 내재되어 있지 않기 때문입니다.**

에이전트는 *동작하는* 페이월은 만들지만 *전환되는* 페이월은 만들지 않는다. 스킬이 메우는 것이 API 지식이 아니라 **도메인 판단**인 사례다.

[[sahil-lavingia]]의 미니멀리스트 엔트러프러너 10종은 한 걸음 더 나가 **착수 자체를 막는다** — 코드를 쓰기 전에 *"이름을 밝힐 수 있는 실제 인물 10명"* 과 *"최소 3명의 유료 의사"* 를 요구한다.

### 스킬 컬렉션이라는 유통 형태

이 소스가 소개하는 6종 중 셋이 **모음집**이다(마케팅 48종 · 미니멀리스트 10종 · OpenCLI 스킬 세트). [[tech-bridge-ai-native-skills]]의 **registry** 논의가 조직 내부 배포였다면, 여기서는 **공개 GitHub repo가 사실상의 레지스트리** 역할을 한다. ⚠️ 그만큼 [[prompt-injection]]과 [[tech-bridge-flutter-ai-workflow]]가 경고한 *"MD 파일은 무해하지 않다"* 가 그대로 적용된다 — 소스는 이 위험을 다루지 않는다.

### 설치 스코프

`task-observer`는 **프로젝트별 설치를 권장**한다 — *"각 프로젝트의 교훈이 분리되어 관리하기가 더 쉬워집니다."* 반대로 [[llm-coding-guidelines|Karpathy 4원칙]]은 스킬로 설치하지 않고 **상위 폴더 `CLAUDE.md`** 로 상속시킨다. 같은 소스 안에서 **스킬로 둘 것과 규칙으로 둘 것이 갈린다**는 점이 실무적으로 유용하다 — 프로젝트마다 다른 것은 스킬, 전부에 걸리는 것은 계층적 `CLAUDE.md`.


## 스킬이 멈추는 자리 (2026-09-08 · [[tech-bridge-agent-knowledge-four-ways]])

이 페이지는 스킬을 **조직 지식·거버넌스** 축으로 키워 왔다([[tech-bridge-ai-native-skills]]의 registry, [[tech-bridge-six-agent-skills]]의 도메인 판단). [[tech-bridge-agent-knowledge-four-ways]]는 반대로 **스킬의 경계**를 긋는다 — 스킬이 무엇을 주고, **어디서 멈추는지**.

정의부터 두 항으로 나눈다.

> 에이전트 스킬은 특정 작업을 수행하기 위해 에이전트에게 전달할 수 있는 **일련의 지침**입니다. (…) 그것은 **따라야 할 단계와 같은 절차**를 나열하고, **언제 그 단계를 따라야 하는지에 대한 판단**을 포함할 수도 있습니다.

**절차 + 판단.** 그리고 판단의 예가 구체적이다 — *"에이전트가 자체적으로 탐색하는 것을 멈추고 (…) 실제 담당자에게 에스컬레이션해야 할 때"*. 이 위키가 [[verifiable-goals]]·[[skill-self-improvement]]에서 다룬 판단이 *산출물이 됐는가*였다면, 여기서는 **언제 손을 떼는가**다.

그리고 곧바로 경계를 긋는다.

> 그러니까 스킬은 에이전트에게 명확한 절차를 제공하고, 그 절차를 어떻게 실행할지에 대한 약간의 판단력도 부여합니다. **하지만 이야기는 거기서 끝납니다.** 해당 스킬은 에이전트에게 오류율을 확인하라고 지시할 수 있지만, **에이전트가 실제로 대시보드에 접속하여 오류율을 확인할 수 있는 것은 아닙니다.**

**이 문장이 [[model-context-protocol|MCP]]와의 분업을 한 줄로 준다** — 스킬은 *무엇을 할지* 알고, MCP는 *그것을 할 수 있게* 한다. 두 페이지는 지금까지 서로를 `related`로만 걸고 있었고 왜 함께 있어야 하는지는 어느 소스도 말하지 않았다. → [[agent-knowledge-sourcing]]

같은 소스가 스킬을 [[retrieval-augmented-generation|RAG]]·[[agent-memory|메모리]]와도 가른다 — **따라야 할 절차·반복 가능한 일**이면 스킬이고, 적어둔 지식이면 RAG, 겪은 지식이면 메모리다. 스킬을 *지식 조달 수단 중 하나*로 상대화한 첫 소스다.

> ⚠️ progressive disclosure(*"작업에 실제로 필요할 때만 해당 스킬을 활용"*)를 이미 확립된 것으로 전제하고 설명한다. 발표자·촬영 시점은 미상이다.

## 플러그인이 스킬의 유통 경로가 된다 (2026-09-08)

[[tech-bridge-cursor-legacy-refactoring]]이 이 페이지에 **배포 채널**이라는 축을 더한다. 지금까지 이 위키가 본 스킬은 대개 *개인이나 팀이 자기 저장소에 쓰는 것* 이었다.

> **Atlassian 플러그인에는 MCP도 있지만 Atlassian 팀이 퍼블리시한 스킬들도 있습니다.** 플러그인을 쓰면 **MCP만이 아니라 그들의 스킬도 함께 얻습니다.**

즉 **도구 제공자가 자기 도구를 쓰는 법을 스킬로 함께 배포한다.** Figma도 같다. → [[model-context-protocol]]과의 분업이 *한 패키지 안에서* 이루어지는 첫 사례다.

**세 층위의 스킬**이 한 소스에 나온다:

| 출처 | 예 |
|---|---|
| **제품 내장** | `/canvas` — *"내장 스킬이라 여러분 모두 갖고 계실 겁니다"* |
| **벤더 배포** | Atlassian · Figma 플러그인에 딸려 오는 스킬 |
| **자작** | 발표자의 **`/onboard`** — 새 레포의 기술 스택·버전·백엔드/프런트엔드 위치를 파악 |

그리고 [[cursor|Cursor]]는 **사내에서 쓰는 스킬 전체를 `superpowers` 플러그인으로 오픈소스 공개**했다고 말한다. Cursor 안에 **`create skill` 기능**이 있고 발표자의 권고는 *"솔직히 직접 스킬을 만드는 것"* 이다.

> ⚠️ 스킬의 품질·충돌·버전 관리가 다뤄지지 않는다. 벤더가 배포한 스킬과 자작 스킬이 충돌할 때의 우선순위도 소스에 없다. [[imad-touil]]([[tech-bridge-ai-native-skills]])이 제기한 **스킬 거버넌스** 문제가 유통 경로가 넓어지면서 커지는데 이 소스는 언급하지 않는다.

## 공유 스킬은 누가 쓰는가 — 두 소스의 충돌 (2026-09-10)

2026-09-09 업로드 두 편이 **같은 날, 서로 모른 채** 공유 스킬 저장소에 대해 반대로 말한다.

| | [[tech-bridge-company-brain-security]] ([[tanmai-gopal]]) | [[tech-bridge-agent-to-agent-as-search]] ([[jean-denis-greze]]) |
|---|---|---|
| 진술 | *"**아무도 GitHub에 다른 사람을 위한 스킬을 쓰지 않을 겁니다.** 그건 우리에게 자연스러운 일이 아니에요. (…) 제 메모리 큐레이션도 겨우 하는데 다른 사람을 위해 적어 둘 시간은 없습니다."* | *"저장소에 공유 스킬이 있고 **누구나 더 좋게 만들 수 있죠.** (…) 다음에 누가 '쿼리가 너무 느려' 하면 프로파일링 스킬을 쓰고 **모두가 더 나은 엔지니어**가 됩니다."* |
| 조건 | (없음 — 인간 본성) | *"에이전트가 그 도구와 공유 사일로에 데이터를 넣고 빼게 하는 **궤적 인센티브**를 갖는 한"* |
| 처방 | 스킬 대신 **위키 + 에이전트 제안 + 사람 승인** → [[no-silent-write]] | 스킬을 포함한 공유 사일로 + [[sweeper-agent\|청소부 에이전트]] |

> ⚠️ Contradiction: 위키는 어느 쪽도 채택하지 않는다. 다만 둘의 차이는 **누가 쓰는가**로 좁혀진다 — Gopal의 반론은 *사람이* 남을 위해 쓰지 않는다는 것이고, Greze의 긍정은 *에이전트가* 인센티브를 갖고 쓴다는 조건부다. 둘을 합치면 *"사람은 안 쓰니 에이전트가 쓰게 하되 사람이 승인하라"* 가 되고, 그것이 정확히 Gopal의 처방이다. 이 합성은 위키의 것이며 어느 소스도 말하지 않았다.

이 페이지의 실무자 관점([[ivanna-kacevica]])이 *스킬은 반복·자동화하고 싶은 워크플로에* 라고 했던 것과 대비하면, 두 소스가 다투는 것은 스킬의 **가치**가 아니라 **조직 안의 유통**이다. → [[agent-knowledge-sourcing]]

## 어휘를 담는 스킬 — 그리고 자동화를 거부하는 스킬 (2026-09-12 · [[tech-bridge-impeccable-design-steering]])

[[paul-bakaus]]의 [[impeccable]]은 이 페이지에 **새 종류의 스킬**을 더한다. 지금까지 스킬이 담은 것은 절차([[ibm]]: 절차+판단), 프레임워크 지식([[flutter]]), 도메인 판단(페이월)이었다. Impeccable이 담는 것은 **단어의 뜻**이다 — *"bolder라고 하면 로드되는 파일"* 에 *bolder* = **그라데이션·글래스·네온이 아니라 위계·스케일·결정적 타이포** 라고 쓰여 있다.

> 두 사람이 정확히 같은 과제를 시도하는 걸 봤는데 (…) **같은 모델, 같은 하네스**를 써도 **쓰는 언어에 따라** 결과에 확연한 차이가 있습니다. 그래서 그 언어를 **스킬로, 시스템으로 압축**했습니다.

**왜 프롬프트가 아니라 스킬인가** — *"뒤에 아무것도 없는 형용사는 그냥 좀 더 나은 프롬프트일 뿐."* 단어는 모델 안에서 다의적이라 뜻을 고정해야 조향이 되고, 그 고정이 스킬이다. 그리고 *"bolder라고 하면 로드"* 는 위 실무자 절의 progressive disclosure 그대로다. → [[adjective-verb-steering]]

세 가지가 이 페이지의 기존 항목과 맞물린다:

| 항목 | Impeccable |
|---|---|
| **portable across harnesses** ([[imad-touil]]) | *"모든 하네스에서 동작 — Claude Code, GitHub Copilot, Cursor, Codex"* — 원칙의 실증 |
| **승격 게이트** ([[skill-self-improvement]]) | 확신 없는 명령(`overdrive`)을 **커뮤니티로 테스트**하고 *"정착하면"* 남긴다 — 사람 대신 커뮤니티 반응 |
| **자동화** | *"auto는 없고 앞으로도 없다"* — 자동 모드 PR을 닫는다. **스킬이 명시적으로 자동화를 거부하는 첫 사례.** 이유는 능력이 아니라 *"결정하는 것이 요점"* → [[no-one-shot-design]] |

⚠️ 효과는 슬라이드 시연과 관찰 진술뿐. 스킬의 전체 구조·명령 수·라이선스는 소스에 없다.

## 스킬은 실패 모드에서 자란다 (2026-09-12 Lauren Tan 편)

[[tech-bridge-lauren-tan-trusting-agents]]가 스킬의 **생성 경로**를 구체적으로 보여 준다 — 설계가 아니라 관찰이다.

> 저는 **[[pstack|Pstack]]을 만들려고 시작한 적이 전혀 없습니다.** 그냥 스킬 몇 개로 시작한 거죠. (…) **에이전트의 온갖 실패 모드를 정말로 관찰**하는 것에서 시작해서, **볼 때마다 "이건 스킬로 만들자"** 했습니다.

스킬의 성격에 대한 진술도 명확하다:

> 스킬은 **그냥 마크다운**이지만 **정보와 지시를 많이 인코딩**합니다. **고품질 토큰을 앞에 주면** (…) **에이전트에게서 많은 지능을 끌어낼 수 있습니다.**

트위터식 표현이 붙는다 — *"에이전트를 다른 잠재 공간(latent space)으로 끌어당긴다"*.

> ⚠️ **그러나 스킬은 소프트 강제다.** 같은 소스가 경고한다 — *"규칙과 bugbot과 스킬과 스타일 가이드만 있으면, 코드베이스가 완전히 쓰레기처럼 보이는 건 시간문제."* → [[hard-vs-soft-enforcement]]

스킬을 고칠 때마다 검증하는 절차는 [[skill-evals]]에 있다.


## 2026-09-15 — 스킬과 훅의 경계

[[tech-bridge-graft-code-knowledge-graph]]에서 [[graft]]의 `init`은 **스킬 하나와 훅 셋을 함께** 설치한다. 둘의 역할이 갈린다.

- **스킬**은 컨텍스트에 놓이는 **지시**다 — 에이전트가 무시할 수 있고, 컨텍스트가 길어지면 잊는다([[context-resets-and-compaction]]).
- **훅**은 하네스가 실행하는 **코드**다 — 화자의 표현으로 *"에이전트가 워크플로를 따르도록 **강제**한다"*.

즉 **스킬은 능력을 주고 훅은 선택지를 없앤다.** [[hard-vs-soft-enforcement]]가 정책 층에서 세운 구분이 하네스 층에서 반복된다 → [[hook-enforced-workflow]].

## References

- [[tech-bridge-ai-native-skills]] · [[imad-touil]] · [[harness-engineering]] · [[tech-bridge-frontier-engineering]]
- [[tech-bridge-flutter-ai-workflow]] · [[ivanna-kacevica]] — 실무자 관점 (두 가지 트리거 · description 트리거 · 보안 · 5개 스킬)
- [[tech-bridge-agent-knowledge-four-ways]] · [[ibm]] — 스킬의 경계(절차+판단, 그리고 멈추는 자리) · [[agent-knowledge-sourcing]]
- [[tech-bridge-company-brain-security]] · [[tech-bridge-agent-to-agent-as-search]] — 공유 스킬의 유통에 대한 반대 진술 (2026-09-10)

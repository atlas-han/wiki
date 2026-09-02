---
title: Agent Skills
type: concept
category: pattern
tags: [skills, harness, governance, mcp, workflow]
related: [harness-engineering, spec-driven-development, frontier-engineering, agent-org-adoption, model-context-protocol, self-harness, prompt-injection, generator-evaluator-pattern, claude-code]
first-seen: tech-bridge-ai-native-skills
sources: [tech-bridge-ai-native-skills, tech-bridge-flutter-ai-workflow]
created: 2026-08-31
updated: 2026-09-02
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

## References

- [[tech-bridge-ai-native-skills]] · [[imad-touil]] · [[harness-engineering]] · [[tech-bridge-frontier-engineering]]
- [[tech-bridge-flutter-ai-workflow]] · [[ivanna-kacevica]] — 실무자 관점 (두 가지 트리거 · description 트리거 · 보안 · 5개 스킬)

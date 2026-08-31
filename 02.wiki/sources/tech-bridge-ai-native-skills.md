---
title: "Tech Bridge — AI 네이티브 조직은 스킬로 움직입니다 (Imad Touil)"
type: source
tags: [agent-skills, harness-engineering, governance, mcp, workflow, quantumblack, video, agent]
source-url: https://www.youtube.com/watch?v=0qySk1fcf6k
source-type: video
author: Tech Bridge (한국어 자막 재배포) · 발표자 Imad Touil (QuantumBlack)
date-published: 2026-08-30
ingested: 2026-08-31
created: 2026-08-31
updated: 2026-08-31
---

# Tech Bridge — AI 네이티브 조직은 스킬로 움직입니다

[[tech-bridge|Tech Bridge]]가 한영자막을 입힌 20:01 강연. 발표자 [[imad-touil|Imad Touil]]은 QuantumBlack distinguished engineer. 한 줄 테제:

> AI-native organizations run on skills — and ungoverned skills become a new class of technical debt.

본문은 **en-orig 자동 자막**을 재구성. 공식 챕터(info.json 15개)를 따른다. ASR: "Intropic"/"Intropix" → [[anthropic|Anthropic]]; "cloud code" / "cloud code MD" → [[claude-code|Claude Code]] / `CLAUDE.md`; "agent MD" → `AGENTS.md`(추정); "disco-" → discoverable; "filling templates" → filing/form templates(규제 공시 맥락, 불확실); "Quantum Black" → QuantumBlack. 인용·타임스탬프는 자막이 분명한 구간에 한정.

채널 설명의 발표자 링크: [LinkedIn](https://www.linkedin.com/in/imad-touil/).

## 스킬 사용에 관한 3가지 질문과 거버넌스의 현실 (00:00–01:20)

손들기 세 질문으로 시작한다.

1. 스킬을 **만들어 쓰는가**
2. 팀 안에서 **공유하는가**
3. 조직 전체에 **거버넌스·유지보수**하는가

앞 둘은 손이 많고, 셋째는 "몇 개". 이 격차가 강연의 주제 — 왜 거버넌스가 임계적인지, 조직에 어떻게 입히는가.

## 에이전틱 스택: 내부 루프와 외부 루프 (01:20–02:43)

Agentic software stack을 **두 루프**로 나눈다. 위키의 [[harness-engineering]]과 맞닿되, 여기서는 **워크플로(outer)** 를 강조한다.

| 루프 | 이름 | 구성 |
|---|---|---|
| **Inner** | coding agent / coding agent **harness** | context manager · tools & [[model-context-protocol\|MCP]] · memory/state · **skills loader** |
| **Outer** | **workflows** | skills · sub-agents · MCP servers · hooks |

하단에 enablement: environment sandbox, **MCP gateway**, **model gateway**(로컬 오픈소스·frontier), **knowledge graph**(IT 코어·코드베이스·**skills registry**·workflow marketplace 추상화).

Context layer: project instruction(`CLAUDE.md` / `AGENTS.md`류) · 선택 MCP schema · memory(대화·HITL) · retrieved contents(파일·코드베이스).

> workflows, think about them as harness blueprints that actually shape the behavior of your coding harness … in the runtime.

## 명세·계획·작업·구현이 단 한 단계에 불과한 이유 (02:43–04:06)

일상적으로 보이는 네 단계 — **Specify → Plan/Design → Tasks → Implement** — 은 오늘날 코딩 에이전트 형태와 익숙하다([[spec-driven-development]]의 Spec→Plan→Task 코어와 동형).

그러나 조직 스케일에서는 그것이 **여정의 한 스텝**, 즉 **product increment** 에 불과하다. 비즈니스가 가치를 포착해 고객에게 배송하기까지의 end-to-end는 훨씬 길다.

## 엔터프라이즈 전체 수명주기(SDLC)의 구성 요소 (04:06–05:26)

product increment 앞뒤로 깔리는 층:

1. **Product strategy** — 무엇을·어떻게, 성공 지표, 로드맵. 입력으로 market research · competitive analysis · customer interviews
2. **Discovery** — problem statements → solution → validate → experiment → user stories
3. **Data prep / data product delivery** — 카탈로그 정리, 엔드포인트·코어 시스템 통합, 파이프라인·데이터 품질·개발용 자산
4. (다시) **Product increment** — 위의 specify–plan–task–implement
5. **Platform engineering / ops** — 인프라 프로비저닝, IaC 모듈
6. **Launch → optimize / incidents** — 성능·장애 후 다시 루프

18년 컨설팅 관찰: 한 조직 안에도 **여러 SDLC**가 흩어짐(모바일·부서·내부 플랫폼·고객 대면). **"원하는 무엇이든 만드는 단일 워크플로"는 없다.**

## 단일 워크플로우로 해결할 수 없는 복잡한 조직 구조 (05:26–06:50)

디지털 플랫폼(솔로 배포 가능한 단순 제품이 아님)의 풍경은 기대보다 복잡하고, 슬라이드에 보이는 것은 **아마 10–20%**. 조직마다 다르다.

워크플로 네 구성 요소 중 hooks · MCP · sub-agents는 "주어진 것"이지만 **구조화된 가치**를 충분히 안 준다 → **skills가 워크플로의 임계 구성 요소**.

| 구성 | 역할 (강연 정의) | 한계 |
|---|---|---|
| **Hooks** | 이벤트에 사전 트리거 | 워크플로를 따라 "무엇을 한다"만 |
| **MCP** | 도구 호출 | 대부분 **제공 도구의 MCP를 소비**; 조직이 소유·구축하지 않음 |
| **Sub-agents** | context window 최소화용 위임 | 특정 태스크 실행 |
| **Skills** | 조직 **know-how의 자리** | 구조가 없으면 deterministic workflow가 안 됨 |

> … we'll find all of your know-how is actually at the skills level.

## 조직의 실제 노하우가 살아 숨 쉬는 곳: 스킬 (06:50–08:14)

스킬 채택의 짧은 역사(발표 시점 기준):

- **~8개월 전** Anthropic이 skills 첫 글 공개 (ASR "Intropic")
- **~2개월 후** 오픈 표준 → 다수 agent harness 채택
- **그해 2월경** 대부분 에이전트가 채택. thinking 중 skills를 pull하는 장면이 보임
- 공개 GitHub·skills registry 스냅샷만으로도 생성량·수요 상승

**Skills bench**(소프트웨어 엔지니어링·사이버시큐리티): 최신 모델은 스킬 없이도 "기대대로" 잘하지만, **더 deterministic한 skills**를 적용하면 결과가 분명 더 높음. 모델 개선만으로는 안 닫히는 축.

## 마이크로서비스 설계 원칙을 스킬에 적용하기 (08:14–09:35)

스킬 설계는 "새 문제"가 아니라 **마이크로서비스 운동이 푼 소프트웨어 문제**와 유사하다. 원칙:

| 원칙 | 내용 |
|---|---|
| **Reusable / modular** | 재사용·모듈 |
| **Discoverable** | 다른 팀이 자동 발견·확보 |
| **Portable across workflows & harnesses** | 같은 표준이면 Claude Code 스킬 → Cursor로도 동작 |
| **Specialized** | 모놀리스 스킬 금지. 한 태스크에 특화 |
| **Composable** | 조합 시 중복·충돌 방지 |
| **Consistent / deterministic** | 일관성·결정성 |
| **Cost efficient** | context window — progressive disclosure로 적시·적정량의 스킬 |

→ 조직 know-how를 **executable · portable · cheap** 한 새 단위로 만든다. 제안 개념 페이지: [[agent-skills]].

## 점진적 공개(Progressive Disclosure)와 토큰 비용 절감 (09:35–10:56)

> … putting with the progressive disclosure pattern, the right skills, the right amount of skills in the right time to solve the right problem. And that's reduce the token usage.

> This makes your know-how in your organization executable, portable, and cheap.

예시: **data retention policy** 스킬 — 고객 데이터 조작 시 규제에 맞게 agent를 instruct.

## 규제 준수 스킬 조합과 결정론적 감사 리포트 (10:56–12:17)

왼쪽: skills catalog. 오른쪽: harness → 출력.

규제 레벨 **composable skills** 예: retention policy + disclosure standards + GDPR rules + filing/form templates. 웹·모바일 등 조직 전반 데이터/기능이 규칙을 지키도록 정의.

런타임에 **regulatory disclosure review workflow**가 자동 pull → 결과는 **deterministic audit report**(저장 가능) + 개선 포인트 식별 → 코드베이스로 피드백.

## 거버넌스 없는 스킬이 새로운 기술 부채가 되는 이유 (12:17–13:39)

> … if you don't govern skills, we will start creating new class of technical debt.

| 부채 | 내용 |
|---|---|
| **Duplication** | 같은 스택·인프라인데 팀마다 같은 스킬을 재작성, 미공유 |
| **Quality** | 테스트·유지·**최신 모델 대비** 검증 없으면 품질 저하 |
| **Discoverability** | 거버넌스 없으면 발견 불가. **Backstage류 IDP**가 마이크로서비스 오너를 카탈로그에서 찾게 한 것과 동형 |
| **Ownership** | 오너 없으면 유지·스케일·스킬 작업 불가 |
| **Composability** | 기본 제공 아님. 설계 정렬 거버넌스 필요 — **domain-driven** 카탈로그 형태와 유사 |
| **Security** | 공개 스킬 실험; 일부는 [[prompt-injection]], 스킬은 **결정론적 스크립트**도 포함 → 보안 파이프라인 없이 pull하면 위험 |
| **Permissions** | 민감 비즈니스 로직 스킬 — 전사 접근 불가. access control 필수 |

## 중앙 집중형 스킬 플랫폼의 핵심 요구사항 (13:39–15:01)

채택 계단:

1. **개인** — 생성·테스트·개선·사용. 무작위가 아니라 합의된 도구/메커니즘
2. **팀** — 공유·공동 개선. 같은 스택·제품이면 빠르게 진화
3. **Centralized platform** — 여기까지 논한 모든 것의 무대

플랫폼 요구:

- searchable **catalog + metadata**
- catalog에 붙는 **MCP** + IDE/샌드박스용 **CLI pull**
- skill 간 **dependencies**
- **versioning / lifecycle** (에이전트가 최신 버전을 자동 감지·pull)
- **access control**
- **evaluation / observability**

## 거버넌스 체계와 도메인별 오너십 분배 (15:01–16:21)

기술만으로 안 닫힌다: **"누가 거버넌스하는가."** 조직 구조에 의존 — architects · engineering leads · infra leads · cyber leads가 **도메인 오너십**을 나누고, 스킬 업데이트가 정책에 맞게 이뤄지게 한다.

성공 시: 전 팀이 한 중앙에서 **고품질 스킬**을 pull → 실행 → 개선분을 다시 플랫폼에 push.

## 15개 개발팀의 6개월 스킬 운영 시뮬레이션 결과 (16:21–17:45)

**시뮬레이션**(현장 A/B가 아님을 명시): 15팀, 팀당 5–12명. 지표 — 엔지니어당 스킬 기여, 일평균 skills utilization, 팀 간 duplication ratio, skills quality·security ratio.

거버넌스 없이 6개월: 이미 조직에서 일어나는 일 — 생성·사용은 하되 **가시성 없음**. Skills는 **productivity uplift에 tightly coupled**.

규제 스킬이 없으면 vibe coding으로 스티어링을 왕복 → **토큰 비용↑ + 원샷 정답 대비 시간↑**. 품질·보안도 팀 성숙도에 분산 → 구현 품질 저하. 시뮬상 생산성·품질·보안은 medium, **cost는 high**.

거버넌스 후: 완벽은 아니나 팀 간 **공통 기반**. 한 스킬을 publish하면 다음 엔지니어가 새 스킬을 만들려 할 때 **coordinating agent harness**가 기존 스킬을 식별·pull → 앞서 말한 거버넌스 이슈를 거의 해소.

[[agent-org-adoption]]·[[frontier-engineering]]의 "도구가 같아도 방식·조직이 가른다"와 같은 축을 **스킬 카탈로그/거버넌스**로 구체화.

## 스킬을 넘어 전체 워크플로우로 확장하기 (17:45–19:09)

Skills는 워크플로의 **한 구성 요소**일 뿐. 스킬만 맞추면 끝이 아니다 — **같은 접근을 whole workflows**에 적용.

중앙 플랫폼에 워크플로(그 안의 스킬 포함)를 두면, 다음 엔지니어가 인프라 프로비저닝 등이 필요할 때 워크플로를 골라 필요 스킬과 함께 빌드·실행·테스트하고, 개선분을 다시 조직 플랫폼에 push.

## 스킬 레지스트리, 정적 평가(Eval), 자동 진화 스킬 (19:09–20:01)

다음에 이미 탐색할 것(채택 6–8개월 구간의 "시작" 이후):

1. **Skills registry** — 없으면 만들 것. IDP(internal developer portal) 진영이 이 capability를 중앙화하기 시작. 전용 도구도 다수.
2. **Skills evaluation** — 정답 접근은 아직 논의 중. 발표자가 유용하다고 본 쉬운 축: Anthropic best practices에 대한 **static eval**(호출·구조가 잘못되면 고품질 가능성 낮음).
3. **Auto-evolving skills** — closed loop로 스킬을 자동 진화. 하이프이지만, **거버넌스·가드레일 없이** 돌리면 앞에서 말한 부채를 **유지·증폭**할 뿐. [[self-harness]]의 "자동 System Evolution"과 맞닿되, 여기는 **조직 가드레일이 전제**.

닫기: leadership lounge에서 질문 환영.

## 위키 합성

같은 "에이전트를 조직에 심는다"를 다른 입구로 말한다.

| | 이 강연 (Touil / skills) | [[tech-bridge-frontier-engineering]] (Amazon) | [[tech-bridge-harness-engineering]] | [[tech-bridge-spec-driven-development]] |
|---|---|---|---|---|
| 진단 | know-how는 스킬에 모임. 거버넌스 없으면 새 기술부채 | 도구 동일, **일하는 방식**이 3x vs 4.5x | AI Layer 6요소 중 skills를 한 칸으로 | 프롬프트는 사적·일시적 |
| 레버리지 | microservice 원칙 · progressive disclosure · registry/IDP | steering/skills 습관, 먹이+검증, 로컬 mock | rules/skills·hooks·sub-agents·MCP | Constitution→Spec→Plan→Task |
| 조직 | 도메인 오너 · 중앙 플랫폼 · 15팀 시뮬 | 2개월 감속, 50→2000, 결정 병목 | System Evolution 마인드셋 | 팀 합의 스펙 = Git 계약 |
| 범위 경고 | spec–plan–task–implement는 **SDLC의 한 increment** | vibe/frontier는 코딩 루프 중심 | 단일 세션→다중 세션 | 데모는 제품 increment에 가깝다 |

수치·시뮬은 발표자 구성. QuantumBlack 소속 강연이라 방법론·통제는 영상만으로 검증 불가. 위키는 **inner/outer 루프 구분, skills vs hooks/MCP/sub-agents, progressive disclosure, 거버넌스 부채 목록, IDP/registry, auto-evolve에 가드레일 전제**를 남긴다.

## 등장 개체·개념

- 채널: [[tech-bridge|Tech Bridge]]
- 인물: [[imad-touil|Imad Touil]] (권장 신규)
- 조직: QuantumBlack — 소속 언급 수준(별도 페이지는 ENTITY_NOTES 참고)
- 도구·표준: [[claude-code|Claude Code]], Cursor, [[model-context-protocol|MCP]], Backstage류 IDP
- 개념(기존): [[harness-engineering]], [[spec-driven-development]], [[frontier-engineering]], [[agent-org-adoption]], [[prompt-injection]], [[self-harness]]
- 개념(권장 신규): [[agent-skills]]

## References

- [원문 영상](https://www.youtube.com/watch?v=0qySk1fcf6k)
- 발표자 LinkedIn: <https://www.linkedin.com/in/imad-touil/>
- 관련 위키: [[tech-bridge-frontier-engineering]] · [[tech-bridge-harness-engineering]] · [[tech-bridge-spec-driven-development]] · [[tech-bridge-figma-coding-agents]]

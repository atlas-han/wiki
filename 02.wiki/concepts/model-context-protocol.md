---
title: Model Context Protocol (MCP)
type: concept
category: pattern
tags: [protocol, agent-tooling, interoperability, anthropic, open-standard]
aliases: [MCP]
related: [agent-harness-design, brain-hands-decoupling, agent-knowledge-sourcing, agent-skills, secure-tool-evolution, mcp-toolbox-for-databases]
first-seen: anthropic-harness-design-long-running-apps
sources: [anthropic-harness-design-long-running-apps, anthropic-managed-agents, tech-bridge-multimodal-commerce-agent, tech-bridge-agent-knowledge-four-ways, tech-bridge-cursor-legacy-refactoring, tech-bridge-build-time-vs-runtime-tools, tech-bridge-acp-universal-remote, tech-bridge-graft-code-knowledge-graph, tech-bridge-brockman-agi-era-defender-window]
created: 2026-05-25
updated: 2026-09-20
---

# Model Context Protocol (MCP)

[[anthropic|Anthropic]]이 주도해 만든 **오픈 표준** — AI 애플리케이션과 외부 시스템(데이터 소스·도구·워크플로) 사이의 연결 인터페이스. 본 위키에서 [[playwright-mcp|Playwright MCP]] 같은 구체적 서버가 등장.

## 한 줄 비유

> Think of MCP like a USB-C port for AI applications.

USB-C가 전자기기 연결의 표준이 된 것처럼, MCP는 AI 앱이 외부 시스템에 붙는 표준.

## 무엇을 가능하게 하나

- Agent가 Google Calendar·Notion에 접근해 개인화된 비서가 됨
- [[claude-code|Claude Code]]가 Figma 디자인으로 전체 웹 앱 생성
- 엔터프라이즈 챗봇이 여러 DB를 가로질러 데이터 분석
- AI가 Blender에서 3D 디자인을 만들어 3D 프린터로 출력

## 생태계 — 광범위한 클라이언트·서버 지원

| 카테고리 | 예 |
|---|---|
| AI 어시스턴트 | [Claude](https://claude.com/docs/connectors/building), [ChatGPT](https://developers.openai.com/api/docs/mcp/) |
| 개발 도구 | [VS Code](https://code.visualstudio.com/docs/copilot/chat/mcp-servers), [Cursor](https://cursor.com/docs/context/mcp) |
| 호환 클라이언트 | MCPJam 등 다수 |

"build once, integrate everywhere" — 한 번 MCP 서버로 노출하면 여러 클라이언트가 그대로 사용.

## 본 위키에서 등장한 MCP 사례

- [[playwright-mcp]] — 브라우저 자동화 (Playwright)를 MCP 서버로. [[anthropic-harness-design-long-running-apps]]의 evaluator agent가 실제 페이지 클릭·스크린샷·검증에 사용.
- [[anthropic-managed-agents]]에서: **MCP + secure vault + dedicated proxy** 패턴으로 토큰을 sandbox 밖에 격리. *"Claude calls MCP tools via a dedicated proxy; this proxy takes in a token associated with the session."*

## [[agent-harness-design]] 관점

MCP는 [[brain-hands-decoupling]]의 *hands* 쪽 구체적 구현체. `execute(name, input) → string`이라는 일반 인터페이스가 MCP tool 호출과 정합. Brain은 sandbox가 컨테이너인지·휴대폰인지·Pokémon emulator인지·MCP 서버인지 알 필요 없다.

## 에이전트 간 상거래의 인터페이스 기대 (2026-09-04)

[[tech-bridge-multimodal-commerce-agent]] Q&A에서 *"사용자가 사람이 아니라 에이전트가 되면"* 이라는 질문에 [[nidhi-kaushik-vyas]]가 답한 내용이다.

> **MCP가 이 둘 사이의 인터페이스 역할을 확실히 할 거라고 예상합니다.** 솔직히 말씀드리면, **아직 우리 에이전트가 다른 에이전트와 상호작용하는 단계에는 이르지 못했습니다.**

위 사례들이 전부 MCP를 *에이전트 → 도구* 방향으로 쓴 것과 달리, 여기서는 **에이전트 ↔ 에이전트**의 접점으로 지목된다. 다만 이는 **기대이지 구현이 아니다** — 같은 답변이 아직 그 단계가 아니라고 명시한다.

같은 소스가 판매자–에이전트 공통 언어로 **UCP**를 별도로 언급하는데, MCP와의 관계는 소스에 설명돼 있지 않고 약어의 뜻도 확정할 수 없다 ([[google-deepmind]] 참조).


## 스킬과의 분업 (2026-09-08 · [[tech-bridge-agent-knowledge-four-ways]])

이 페이지는 MCP를 **연결 표준**으로 설명해 왔고, [[agent-skills]]는 **조직 지식**으로 자라 왔다. 두 페이지가 서로를 `related`로만 걸고 있었는데 [[tech-bridge-agent-knowledge-four-ways]]가 **왜 둘이 함께 있어야 하는지**를 하나의 사고 위에서 보인다.

500 에러를 고치는 예제에서, [[agent-skills|스킬]]이 *"우선 오류율을 살펴봐야 합니다"* 라는 절차를 준 직후:

> **하지만 이야기는 거기서 끝납니다.** 해당 스킬은 에이전트에게 오류율을 확인하라고 지시할 수 있지만, **에이전트가 실제로 대시보드에 접속하여 오류율을 확인할 수 있는 것은 아닙니다.** 그래서 (…) **MCP**를 사용하는 것입니다.

> MCP를 사용하면 에이전트가 **MCP 호출을 통해 모든 로그 정보**를 얻을 수 있으므로 (…) 같은 방식으로 **지표**도 얻을 수 있으며, **실제 오류율을 확인**할 수 있습니다.

**스킬은 무엇을 할지 알고, MCP는 그것을 할 수 있게 한다.** [[brain-hands-decoupling]]의 뇌/손 분리를 **지식 조달 층**에서 다시 그린 형태이고, 이 페이지가 이미 적어 둔 *"MCP는 hands 쪽 구체적 구현체"* 라는 관찰과 정확히 맞물린다.

소스는 호스트/서버 관계도 간단히 정리한다 — *"에이전트 자체, 즉 **MCP 호스트**와 해당 에이전트가 통신하려는 **각 시스템(MCP 서버 뒤에 위치함)**"*. 그리고 MCP가 메우는 것이 **모델의 무지**임을 명시한다.

> 이 **모델 자체는 특정 로깅 스택의 백엔드를 쿼리하는 방법을 알지 못할 수도 있지만**, 해당 로깅 스택의 **MCP 서버는 연결 방법을 알고 있으며** 에이전트가 호출할 수 있도록 해당 연결을 제공합니다.

같은 소스의 라우팅 규칙에서 MCP는 *"바깥에서 실제로 조회해야 하는 것"* 에 배정된다. → [[agent-knowledge-sourcing]]

> ⚠️ 규칙의 한정어 *"without using proprietary code"* 가 무엇을 가리키는지 **소스가 부연하지 않는다.**

## 플러그인 — MCP와 스킬이 한 패키지로 (2026-09-08)

[[tech-bridge-cursor-legacy-refactoring]]에서 [[cursor|Cursor]]는 MCP를 **"플러그인"** 이라는 상위 단위로 감싸 배포한다. 그리고 그 단위에는 **MCP와 [[agent-skills|스킬]]이 함께** 들어간다.

> Atlassian 플러그인에는 **MCP도 있지만** Atlassian 팀이 퍼블리시한 **스킬들도 있습니다.**

이 위키는 [[tech-bridge-agent-knowledge-four-ways|IBM 편]]에서 둘의 분업을 *스킬 = 따라야 할 절차, MCP = 그 절차를 수행할 외부 접근* 으로 정리했다. 이 소스는 그 분업이 **유통 단위에서는 합쳐진다**는 것을 보여준다 — 도구를 주는 쪽이 *그 도구를 쓰는 법* 도 함께 준다.

목록에 오른 것: **Atlassian · Datadog · Figma · Google(Drive · Calendar · Gmail) · granola · PagerDuty · Sentry.**

**클라우드 승계** — [[cursor-cloud|cursor cloud]]의 원격 에이전트도 **로컬에서 쓰던 MCP를 그대로 연결**할 수 있다. 자체적으로 **cursor cloud MCP**가 있어 실패한 실행과 환경을 진단하는 데 쓴다.

> ⚠️ 시연 중 **Statsig MCP 연결에 실패**해 Datadog으로 대체했다. 플러그인 목록에 있다고 항상 연결되는 것은 아니다.

## MCP 서버가 가드레일의 자리 — MCP Toolbox for Databases (2026-09-11)

[[tech-bridge-build-time-vs-runtime-tools]]([[google-cloud|Google Cloud]])는 이 페이지가 지금까지 *연결 표준* 으로 다룬 MCP를 **보안 경계가 사는 자리**로 쓴다. [[mcp-toolbox-for-databases|MCP Toolbox for Databases]](오픈소스 데이터베이스 MCP 서버, 자기 진술로 별 15.7k·DB 40+)의 **YAML 설정**에 [[secure-tool-evolution|안전한 도구의 진화]] 전부가 들어간다 — 연결 정보(source), 읽기 전용(드라이버 수준), 허용 데이터셋, 출력 크기, 고정 SQL(prepared statement), 사용자 신원 바인딩([[bound-parameters]]).

[[anthropic-managed-agents]]의 *MCP + vault + 프록시* 가 **토큰**을 서버 쪽에 격리했다면, Toolbox는 **연결·SQL·신원**을 격리한다. 두 사례 모두 *"에이전트가 무엇을 믿든 서버 설정이 허용하는 것만 된다"* 는 형태이고, [[agent-governance-layers]]의 벽이 MCP 서버에 놓인 것이다.

같은 소스에서 나온 사실 몇 가지: 호스팅 버전 **Google managed MCP**(관리형 MCP + Toolbox 합산 **월 도구 호출 2천만 건**, 자기 진술) · 연결 대상으로 *"에이전트·IDE·**하네스**"* — Gemini CLI, Antigravity, *"Cloud Code"*(Google Cloud Code인지 [[claude-code|Claude Code]]인지 **판정 불가**) · 그리고 도구 설명·읽기/쓰기 분리·조치 가능한 오류 등 [[agent-tool-design-practices|도구 설계 다섯 규칙]].

[[tech-bridge-agent-knowledge-four-ways|IBM 편]]이 MCP를 *"바깥에서 실제로 조회해야 하는 것"* 에 배정했는데, 이 소스는 그 조회가 **어떻게 안전해지는가**를 데이터베이스에서 보여준다. 그리고 *하네스* 라는 말이 Google 엔지니어의 입에서 에이전트·IDE와 나란히 쓰이는 것은 [[agent-harness-design]]이 적어 둔 용어 확산의 한 관측이다.

## 반대 방향의 표준 — ACP (2026-09-12 편)

[[tech-bridge-acp-universal-remote]]가 MCP의 위치를 **방향으로** 정의한다. MCP는 **에이전트 → 도구** 이고, **클라이언트 → 에이전트** 방향에는 표준이 없었다 — 그 자리를 [[agent-client-protocol|ACP]]가 맡는다.

그리고 MCP의 성공 요인에 대한 진술이 하나 더 붙는다:

> **MCP의 가장 강력한 점은 MCP 자체의 무엇이 아니라, 모두가 MCP를 쓴다는 것**입니다. 그래서 전 세계에 **수천~수만 개의 서버**가 있고, 모든 에이전트가 거기 연결해 다른 시스템에서 일을 할 수 있습니다.

**규격이 아니라 보편 채택을 가치의 근거로 든다** → [[standards-as-market-makers]]. 화자([[alex-hancock]])는 MCP 메인테이너이자 **Rust SDK** 담당이다.

[[agentic-stack-decomposition]]에서 MCP는 네 칸 중 **도구** 칸을 맡고, 이미 **원격 전송을 가진 층**으로 분류된다.

> ⚠️ 오프닝에서 **MCP의 tasks 기능**이 언급되지만(앞 발표자가 다룬 주제) 설명되지 않는다. 위키가 아직 모르는 기능이다.

## 최후의 수단으로서의 컴퓨터 사용 (2026-09-12 편)

[[tech-bridge-mousepower-measuring-agents]]는 MCP를 **선호 경로**로 놓는다 — [[yutori|Yutori]]의 컴퓨터 사용 모델은 *"API나 MCP에서 정보를 얻을 수 없을 때"* 쓰는 것이고 *"당연히 API·MCP보다는 비효율적"* 이다.


## 2026-09-15 — MCP의 값이 기능이 아니라 타이밍의 주도권인 경우

[[tech-bridge-graft-code-knowledge-graph]]는 **같은 인덱스를 CLI(훅)와 MCP 두 방식으로 배포하고 스스로 비교한다.** 이 위키에서 MCP가 *"에이전트에게 도구를 주는 규약"* 이 아니라 **동일한 데이터에 대한 두 조달 방식 중 하나**로 놓인 첫 사례다.

| | CLI(훅) | MCP |
|---|---|---|
| 조회 시작 | **도구가 프롬프트를 보고 추측** | **에이전트가 필요할 때 질의** |
| 첨부 | 매 메시지에 최대 3개 위치(*"필요로 했든 아니든"*) | 없음 |
| 자체 테스트 | **더 빠름** | **정답 몇 개 더 맞힘** |

**밀어 넣기는 낭비를 감수하고 지연을 없애고, 물어보기는 턴을 하나 쓰고 적합성을 얻는다** → [[push-vs-pull-context-retrieval]].

## References

- [[anthropic-harness-design-long-running-apps]]
- [[anthropic-managed-agents]]
- [[playwright-mcp]]
- [공식 사이트 modelcontextprotocol.io](https://modelcontextprotocol.io/introduction)
- [[tech-bridge-agent-knowledge-four-ways]] — 스킬과의 분업 · [[agent-knowledge-sourcing]]
- [[tech-bridge-build-time-vs-runtime-tools]] — MCP 서버가 가드레일의 자리 · [[mcp-toolbox-for-databases]] (2026-09-11)

## "세상을 다시 도구화하고 있다" — 도구 층을 임시방편으로 보는 시각 (2026-09-20 · [[tech-bridge-brockman-agi-era-defender-window]])

[[greg-brockman|Greg Brockman]]이 컴퓨터 사용을 설명하면서 이 프로토콜이 속한 층 전체를 **과도기로** 규정한다.

> 사람들이 이 **MCP 서버들과 CLI들을 만들어 왔고, 소프트웨어의 세계를 가져다가 사람을 위한 것이 아닌 거의 뻣뻣한(stilted) 방식으로 접근 가능하게 만들어 왔습니다** — 말하자면 **세상을 다시 도구화(retooling)하고 있는 거죠.** (21:58~22:13)

> *"API를 만들자, 소프트웨어니까"* 같은 건데, **만약 그것이 정말 사람처럼 행동한다면? 그냥 컴퓨터를 쓰면 안 되나?** (22:13~22:33)

> **그것들은 늘 아주 이상하고 준최적으로 느껴졌습니다.** (22:33~22:49)

논거는 2015년으로 거슬러 간다 — *"환경이 화면 픽셀, 키보드, 마우스인 강화 학습 … 그러면 갑자기 컴퓨터로 할 수 있는 어떤 과제든 분포 안에(in distribution) 있게 되는 거죠"*(22:49~23:04).

### 이 위키가 이 방향을 세 번째로 받는다

| 소스 | 어디까지 갔나 |
|---|---|
| [[graft\|Graft]] 편 (09-15) | **CLI vs MCP** 를 측정해 트레이드오프를 잰다 → [[push-vs-pull-context-retrieval]] |
| [[tech-bridge-vercel-eve-filesystem-agent\|Vercel]] 편 (09-19) | **도구를 깎지 말고 파일 시스템을 줘라** → [[file-system-agent]] |
| **이 소스** (09-20) | **도구 층 자체가 임시방편**이고 사람용 인터페이스가 목적지다 |

**세 소스가 같은 방향을 서로 다른 거리에서 가리킨다.** 이 페이지가 [[model-context-protocol|MCP]]를 *표준화된 접근 경로* 로 다뤄 온 것에 대해, **가장 먼 지점에서 온 반론**이다.

> ⚠️ **진행자가 즉시 지적한다** — *"그 다른 레이어를 만든 결과로 이제 또 다른 보안 과제 레이어가 생기는 거죠"*(22:13~22:33). **화자는 *"정확합니다"* 로만 받고, 컴퓨터 사용의 보안 모델은 대담 전체에서 한 번도 다뤄지지 않는다.** 보안을 40분간 이야기한 대담에서 [[prompt-injection]]·[[lethal-trifecta]]·[[agent-identity-separation]]이 통째로 비어 있다.
>
> ⚠️ 그리고 **MCP를 대체할 무엇이 실제로 무엇인지** — 권한·감사·재현성을 어떻게 다루는지 — 가 없다. 주장은 방향뿐이다.

→ [[tech-bridge-brockman-agi-era-defender-window]] · [[greg-brockman]] · [[openai-astra]] · [[file-system-agent]] · [[push-vs-pull-context-retrieval]]

---
title: "Tech Bridge — Cursor로 레거시 코드베이스 리팩터링 (canvas·plan mode·cloud agents·automations)"
type: source
tags: [refactoring, legacy-migration, cloud-agents, automations, plan-mode, cursor, workshop, video]
source-url: https://www.youtube.com/watch?v=A7xJz1A74B8
source-type: video
author: Tech Bridge (한영자막 재배포) · [[cursor|Cursor]] 필드 엔지니어 워크샵 (발표자 이름 소스 내 불일치) · 진행 Reagan
date-published: 2026-09-08
ingested: 2026-09-09
created: 2026-09-09
updated: 2026-09-09
---

# Tech Bridge — Cursor로 레거시 코드베이스 리팩터링

[[tech-bridge|Tech Bridge]]가 한영자막을 입힌 **55:17** 실시간 워크샵. **이 채널이 올린 실시간 워크샵 형식으로는 최장편**이다. 발표는 [[cursor|Cursor]] 필드 엔지니어. 한 줄 테제:

> **레거시 마이그레이션은 에이전트에게 한 번에 시키는 일이 아니라 네 단계로 쪼개는 일이다** — canvas로 감사하고, plan mode로 코드 없이 전략만 쓰고, 티켓으로 쪼개 cloud agent에 위임하고, automations로 다시 레거시가 되는 것을 막는다.

전체는 `01.raw/articles/2026-09-08_Cursor 엔지니어의 AI를 이용한 레거시 코드 리팩터링 시연 영상.md`.

> ⚠️ **발표자 이름 불일치 — 어느 표기도 채택하지 않았다.** 진행자 Reagan이 09:02에 **"Amita"**, 47:08에 **"Amriita"** 로 부르고 **설명란에는 이름이 없다.** 2026-09-02·09-08의 이름 불일치 사례와 달리 **설명란이라는 판정 근거조차 없어** 인물 페이지를 만들지 않았다.
>
> ⚠️ **당사자 진술, 독립 확인 없음.** Cursor 직원이 진행하는 Cursor 제품 워크샵이다. **화자의 인센티브는 코딩 에이전트 플랫폼 판매자**다. 벤치마크·가격·경쟁 제품 비교는 전부 판매자 진술이다.
>
> ⚠️ **라이브 마이그레이션은 시간 안에 끝나지 않았다.** *"오늘 이걸 끝내지는 못할 것 같으니"*(42:36) — 완성 예시로 보여준 것은 **미리 준비된 이전 실행분**이다. **비디오 자기 검증을 포함한 종단 결과가 라이브로 검증되지 않았다.**

## 촬영 시점 — 위키 교차 참조로 좁힌 첫 사례

발표자가 04:22에 **[[grok-4-6|Grok 4.6]]이 *"어제 출시됐다고 말하고 싶네요"*** 라고 말한다. 이 위키의 [[tech-bridge-grokbot-agent-teams]](2026-08-31 업로드)는 **Grok 4.6을 그 인터뷰 당일 발표로** 기록한다. 54:41의 *"다음 주 목요일에 [[grokbot|GrokBot]] 워크샵을 한다"* 도 GrokBot 베타 직후와 맞는다.

→ **촬영 2026-09-01 무렵, 업로드 2026-09-08로 추정된다.** 업로드 날짜 ≠ 촬영 시점의 **네 번째 사례이며, 내부 증거가 아니라 다른 위키 소스와의 교차 참조로 좁힌 첫 사례**다.

> ⚠️ *"어제"* 는 발표자가 *"말하고 싶네요(I want to say)"* 라는 유보를 단 표현이므로 **날짜를 확정하지 않고 추정으로 남긴다.**

## 네 단계 워크플로

| 단계 | 도구 | 산출물 | 핵심 성질 |
|---|---|---|---|
| ① 감사·전략 | `/canvas` · **plan mode** | 인터랙티브 커버리지 시각화 + **마크다운 계획서** | **plan mode는 코드를 쓰지 않는다.** 오직 전략만 |
| ② 분할 | Atlassian **플러그인**(MCP) | Jira 에픽의 티켓들 (목표·범위·수락 기준·테스트·의존성·노트) | 계획서가 **살아 있는 문서**로 편집 가능 |
| ③ 위임 | **cursor cloud agents** | **티켓당 별도 PR** + 자기 검증 비디오 | 원격 Linux VM. 노트북 닫아도 계속 |
| ④ 예방 | **automations** | 예약/트리거되는 cloud agent | 사후 대응이 아니라 **선제 대응** |

## 이 위키에 새로 들어오는 것

### ① cursor harness — 하네스 정의가 하나 더 붙는다

[[harness-engineering]]·[[agent-harness-design]]이 모아온 정의에 Cursor 자신의 것이 추가된다.

> **플랫폼과 모델 사이에 있는 것을 cursor harness라고 부릅니다.** 그것은 **도구 실행(tool execution), 캐시 관리(cache management), 동적 컨텍스트 관리(dynamic context management), 컨텍스트 조립(context assembly)** 로 이루어져 있습니다.

[[angela-jiang]]([[tech-bridge-claude-platform-agent-era]])의 하네스 정의와 나란히 놓으면, **양쪽 다 "모델 바깥의 것"을 가리키지만 Cursor 쪽이 캐시와 컨텍스트 조립을 명시적 구성요소로 든다.**

### ② plan mode — 코드를 쓰지 않는 모드가 별도로 있다

> **출력이 마크다운 파일입니다. 문서입니다. Cursor는 plan mode에서 절대 코드를 만들거나 쓰지 않습니다. 오직 전략만 써줍니다.**

그리고 계획을 쓰기 **전에** 되묻는다 — *"레거시 컴포넌트라는 게 좀 모호한데 어떤 범위를 대상으로 해야 하나요?"* `ask question` 도구는 **계획 전 최소 질문 수를 강제하도록 커스터마이즈할 수 있다.**

→ [[plan-to-ticket-pipeline]]. 이 위키의 [[spec-driven-development]]·[[intent-md]]·[[sprint-contract]]가 다뤄온 *코드 앞단의 산출물* 에 **제품 기능으로 구현된 사례**가 하나 붙는다. 계획서 템플릿이 **Confluence에 살아서** 모든 계획이 같은 모양을 갖는다는 점도 [[executable-standards]]와 같은 방향이다.

### ③ 모델 혼합의 경제학 — 계획용 무거운 모델 + 실행용 싼 모델

> **하나의 더 무거운 모델을 계획에, 더 실행 중심인 모델을 실제 코드 작성에** 쓰는 것이 전체 예산에 정말 유용합니다.

SQLite 재구축 케이스 스터디에서 **에이전트 스웜 + 모델 조합**이 *Fable 단독이나 GPT-5.5 단독보다 훨씬 저렴*했다고 주장한다. 그리고 실제 선택이 두 번 시연된다 — **계획은 GPT-5.6 계열**(*"Grok보다 더 나은 작가"*), **실행은 Grok 4.6**(*"더 빠르고 효율적인 걸 원하니까"*).

클라우드에서는 압력이 더 강해진다:

> cloud agent는 오래 걸릴 수 있고 **스크린샷과 비디오를 돌려주기 때문에 일반 로컬 에이전트보다 토큰을 더 씁니다.** 그래서 **더 싸고 빠른 모델**을 쓰는 게 좋습니다. 마이그레이션 전체에 **3~4달러** 정도.

> ⚠️ 그리고 *"여기서 보통 **Anthropic 모델은 피합니다. 비싸질 수 있어서요**"*(30:04). → [[model-mixing-economics]]. 이것은 [[grok-4-6]] 페이지가 이미 기록한 **가격이 곧 병렬성**이라는 논리의 연장이고, 이번에는 **한 작업 안에서 모델을 갈아 끼우는** 형태로 나타난다.

### ④ cloud agent의 자기 검증 — 자기 마우스로 UI를 조작한 비디오

이 워크샵에서 가장 구체적인 주장이다.

> cursor cloud agent는 **원격 Linux VM에서 돌기 때문에 컴퓨터와 마우스에 접근할 수 있습니다.** 풀스택 프런트엔드 애플리케이션이 있다면 **Cursor가 그 테스트를 대신 해줄 수 있습니다.**

> **Cursor가 자기 마우스, 자기 컴퓨터를 써서 저를 위해 무언가를 테스트하는 것입니다. 저는 아무것도 조종하지 않습니다.** 전체 녹화를 하고 저에게 돌려보냅니다.

비디오에 **구간 라벨**까지 붙는다(*로그인 섹션 / 댓글 보기 / 사용자 보기*).

→ [[cloud-agent-delegation]]. **이것이 [[tech-bridge-ai-era-code-quality|같은 날 IBM 편]]의 *행동 검증* 을 에이전트 자신이 수행하는 형태다.** IBM 편은 *"작성자가 아니라 검증된 행동을 신뢰하라"* 고 말하고, 이 소스는 **그 검증을 작성자인 에이전트가 직접 수행해 증거를 제출한다.** 두 소스는 서로를 언급하지 않으며 이 연결은 위키가 놓는 것이다.

> ⚠️ 그리고 바로 그 지점에 이 소스가 답하지 않는 질문이 있다 — **작성자와 검증자가 같은 에이전트일 때 그 증거는 얼마나 독립적인가.** [[generator-evaluator-pattern]]이 다뤄온 문제인데 이 소스는 제기하지 않는다.

### ⑤ automations — 예약된 cloud agent로 레거시화를 예방한다

> **Cursor의 automations는 기본적으로 예약되거나 트리거되는 cloud agent입니다.**

트리거: 시간, 이벤트(PR 열림·라벨 변경), **Slack/Teams 메시지**, 커스텀 웹훅(Jira 티켓 상태 이동 등).

시연된 것은 **feature flag cleaner** — *매주 레포를 훑어 30일간 안 쓰인 방치된 플래그를 찾고, Datadog·Sentry로 교차 확인하고, 제거 PR과 회귀 없음을 확인하는 테스트를 올리고, Slack으로 알린다.*

논지가 명확하다:

> **레거시 코드베이스를 리팩터링할 때 우리는 "어쩌다 이 상태가 됐지?"라고 묻습니다.** 많은 경우 그냥 **충분히 선제적이지 않았기 때문**입니다. **그래서 automations는 나중에 리팩터링을 해야 하는 일을 피할 수 있도록 미리 일을 합니다.**

→ [[scheduled-agent-automations]]. **이 위키가 [[persistent-agent-teams]]·[[grokbot]]에서 본 "항상 켜져 있는 에이전트"의 세 번째 형태**다. 앞의 둘이 *동료 같은 봇*이었다면 이쪽은 **유지보수 잡(job)** 이다.

그리고 **automation마다 `memories.md` 파일이 있다.**

> 이것이 automation이 **실행할 때마다 더 나아지는 방법**입니다. 무언가를 놓쳤거나 *"Slack에 이렇게 표현한 게 마음에 안 들었어"* 라고 후속으로 말해야 했다면 **그 피드백에서 배우고 다음 실행마다 더 나아집니다.**

→ [[agent-memory]] · [[skill-self-improvement]]에 파일 기반 사례가 하나 더 붙는다.

### ⑥ 스킬이 플러그인 안에 배포된다

[[agent-skills]]와 [[model-context-protocol]]의 분업에 유통 경로가 하나 붙는다.

> **Atlassian 플러그인에는 MCP도 있지만 Atlassian 팀이 퍼블리시한 스킬들도 있습니다.** 플러그인을 쓰면 **MCP만이 아니라 그들의 스킬도 함께 얻습니다.**

Cursor는 **자사가 쓰는 스킬 전체를 `superpowers` 플러그인으로 오픈소스 공개**했다고 말한다. 발표자 개인 스킬로 **`/onboard`**(새 레포 파악)를 든다. 그리고 팀 학습용으로 **`continual learning` 플러그인**이 있는데 — 이 위키에 이미 [[continual-learning]] 페이지가 있어 **이름이 정확히 겹친다** — **`AGENTS.md`에 작업·글쓰기·코딩 스타일을 축적한다.**

## 그 밖에 기록된 사실

- **네 표면**: agents 창(기본) · IDE(VS Code 포크) · CLI(tmux·Xcode·Android Studio용) · **cloud**. 추가 접점으로 **Slack 봇**(문서-구현 동기화 검사 후 PR)과 **iOS 모바일 앱**(Android 예정).
- **멀티 레포 cloud agent** — 마이크로서비스 조직, 또는 내부 SDK 변경이 여러 클라이언트로 파급되는 경우를 든다.
- **환경 build 캐싱** — 첫 세팅 10~20분, 이후 저장된 build로 즉시 시작.
- **작업 분할 원칙** — *"모든 걸 하나의 거대한 PR에 넣지 않도록. 리뷰하기가 너무 감당이 안 되니까."*
- **조직 활용** — 금요일에 백로그를 돌리고 월요일에 PR 리뷰. **유럽/아시아 팀의 비동기 인계.**
- **시크릿·네트워크** — API 키·라우팅 규칙·IP 허용목록이 cloud 환경 설정에 산다. 프라이빗 커넥티비티로 **Cloudflare 터널 / AWS PrivateLink / Tailscale**. self-host cloud agents는 *"처음부터 권하지 않는다."*
- **canvas 공유 범위는 팀으로 제한**된다 — *"엄마 아빠에게 보내면 cursor 팀이 아니라서 열 수 없습니다."*
- **`long running agents`** — `/goal`과 유사, 시간 제한 설정 가능, 의존성·언어 버전 업데이트용.
- **multitask mode** — 관련 없는 두 작업 병렬 처리.

## 해소하지 않고 표시만 한 것

- **발표자 이름**(Amita vs Amriita, 설명란 없음) · **행사명·주최·날짜 없음** · **촬영 시점은 추정**.
- **라이브 마이그레이션 미완** — 종단 결과가 라이브로 검증되지 않았고 완성 예시는 사전 준비분이다.
- **자기 검증의 독립성 문제 미제기** — 작성자와 검증자가 같은 에이전트다.
- **SQLite 케이스 스터디에 수치가 없다** — *"훨씬 저렴"* 뿐이고 블로그 링크는 채팅으로 넘겼다고만 한다. **벤치마크 차트는 화면에만 있고 자막에 수치가 없다.**
- **"마이그레이션 전체에 3~4달러"에 조건이 없다** — 어떤 규모·어떤 레포인지 명시하지 않는다.
- **모델 표기 불확정** — *"GPT56 Soul"* 의 접미사, *"DeepSeek V4 Flasher Pro"* 의 정확한 이름을 확정할 근거가 없다.
- **`/vtw`** — ko·en-orig 양쪽이 동일하게 적지만 실재하는 명령인지 확정 불가.
- **쿡북 문서 부재** — 발표자가 레거시 모범 사례 문서를 찾지 못했다(*"내렸나 봐요"*).
- **cloud agent 크래시 시 컨텍스트 복구 여부에 답이 없다** — 발표자가 *"모르겠습니다, 확인해 봐야 합니다"* 라 하고 그 자리에서 시험하지만 **소스는 결과를 보여주지 않고 끝난다.**
- **경쟁 제품 비교의 근거 없음** — *"cursor cloud agents는 최근 어떤 AI 제품에서 본 것 중 최고"* 는 자사 평가다.
- **WordPress 예제의 한계** — 오픈소스 공개 레포이며 **사내 레거시의 전형적 어려움(문서 없음·원저자 부재·비공개 의존성)이 다뤄지지 않는다.**

## References

- 원본: <https://www.youtube.com/watch?v=A7xJz1A74B8>
- raw: `01.raw/articles/2026-09-08_Cursor 엔지니어의 AI를 이용한 레거시 코드 리팩터링 시연 영상.md`
- 관련: [[cloud-agent-delegation]] · [[plan-to-ticket-pipeline]] · [[scheduled-agent-automations]] · [[model-mixing-economics]] · [[cursor]] · [[cursor-cloud]] · [[grok-4-6]] · [[grokbot]] · [[harness-engineering]] · [[agent-skills]] · [[tech-bridge-grokbot-agent-teams]] · [[tech-bridge-ai-era-code-quality]]

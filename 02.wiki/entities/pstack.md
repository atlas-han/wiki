---
title: Pstack
type: entity
category: tool
tags: [cursor, plugin, skills, verification, evals, lauren-tan]
sources: [tech-bridge-lauren-tan-trusting-agents, tech-bridge-pstack-third-party-review]
created: 2026-09-13
updated: 2026-09-14
---

# Pstack

[[lauren-tan|Lauren Tan]]이 만든 **[[cursor|Cursor]] 플러그인** — 자기 엔지니어링 관행을 스킬로 묶은 것. 본 위키 첫 등장은 [[tech-bridge-lauren-tan-trusting-agents]].

## 이름

**P는 potato** — 화자의 트위터 핸들 `poteto`에서 온다. **Y Combinator CEO Gary Tan의 `GStack`(Gary Stack)** 을 살짝 놀리며 만든 자기 버전이고, *"공교롭게 성이 같은데 아무 관계도 없다"* 는 농담이 붙는다.

> ⚠️ **ko 자막이 이 대목을 두 번 망가뜨린다** — Gary **Tan** 의 성을 *"스택"* 으로 바꿔 성이 같다는 전제를 지우고, 화자가 자기 도구를 **`GStack`이라 지었다**고 뒤집는다. **자기 도구의 이름은 Pstack이다.**

## 들어 있는 것 (소스에서 언급된 것만)

| 항목 | 내용 |
|---|---|
| **`create verification skill`** | 코드를 탐색해 **초기 [[feature-map]]** 을 포함한 검증 스킬 세트를 세팅해 준다 |
| **`maintain verification skill`** | 그 맵과 스킬을 **최신으로 유지** |
| **`control glass` 스킬** | 화자가 만든 첫 스킬 중 하나(glass = agents window의 사내 코드명). CDP·시뮬레이터로 앱을 띄우고 트레이스를 뜬다 |
| **`how` 스킬** | 에이전트 관찰에서 나온 두 번째 스킬 (ko 자막은 이름을 *"방법"* 으로 번역해 버린다) |
| **`potato mode`의 `eval playbook`** | **눈가림 서브에이전트 eval** 절차 → [[skill-evals]] |

## 만들어진 방식

> 저는 **Pstack을 만들려고 시작한 적이 전혀 없습니다.** 그냥 스킬 몇 개로 시작한 거죠. (…) **에이전트의 온갖 실패 모드를 정말로 관찰**하는 것에서 시작해서, **볼 때마다 "이건 스킬로 만들자"** 했습니다.

→ [[skill-self-improvement]] · [[agent-skills]]

## 화자 본인의 유보

> **저를 믿고 Pstack을 믿으면 연장선에서 에이전트를 믿을 수 있겠지만, 저를 안 믿으신다면 — 그리고 저를 맹목적으로 믿으시라고 권하지 않습니다 — 직접 스킬 세트를 만드시면 됩니다.** **포크해서 자기 것으로 만들고 개선하는 것도 적극 권합니다.**

> ⚠️ 접근 경로는 *"구글에 'Pstack cursor'로 검색하면 나온다"* 가 전부다. **라이선스·배포 형태·버전은 소스에 없다.**


---

## 제작자 바깥에서 온 첫 관측 (2026-09-14 · [[tech-bridge-pstack-third-party-review]])

**이 페이지의 기존 내용은 전부 제작자 본인의 워크숍에서 왔다.** [[tech-bridge-pstack-third-party-review]]는 **이름이 밝혀지지 않은 제3자**가 Pstack만으로 스킬 관리자 [[molten-base|Molten Base]]를 만들어 보며 해부한 **11:34 화면 녹화**다.

> ⚠️ **화자는 Lauren Tan이 아니다.** ko 자막이 첫 문장의 3인칭 소개(*"So this is Lauren Tan"*)를 **1인칭 자기소개**로 바꿔 놓아 오인하기 쉽다. 리뷰어도 중립은 아니다 — 자기 제품과 자기 강의를 같은 영상에서 말한다.

### 구조 (본인 소스에는 없던 것)

| 층 | 내용 |
|---|---|
| **potato mode** | **라우터** — *"20개 넘는 스킬 중 무엇을 먼저 쓸지 정하는 걸 도와준다"* |
| **플레이북 22개** | *"운영 절차(operating procedures)"* — 각각 프롬프트 + 사용 사례 예시 |
| **개별 스킬·슬래시 명령** | *"실제 일을 하는 것들"* |
| **원칙·규칙** | 스택 전체가 *"그녀의 원칙과 엔지니어링 규칙"* 으로 쪼개져 있다 |

**계획 스킬이 의도적으로 없다** — *"이건 사양과 계획을 위해 설계된 게 아니라 **이미 자리 잡은 코드베이스 위에서 운영**하도록 만들어진 것"*, 근거는 **Lauren의 입장**(리뷰어 간접 인용): ***"나는 계획을 믿지 않는다. 최고의 사양은 코드다."*** → 이 위키의 [[spec-driven-development]]·[[intent-md]] 계열과 **정면으로 대립하는 극**이다.

⚠️ 이 인용문은 [[tech-bridge-lauren-tan-trusting-agents|본인 워크숍]]에 **없다.** 간접 인용으로만 기록한다.

### 병렬성 두 형태

- **[[agent-arena|아레나]]** — **같은 문제**를 서로 다른 모델 3~4개에(관측 예: Claude · GPT · Grok · Claude Opus 5), 각자의 최선을 **접목(graft)하거나 기각**.
- **[[agent-swarm|스웜]]** — **문제의 조각**을 병렬 작업자에게, **하나의 종합 보고서**로 집계.
- 약속은 **"겁 없는 병렬성(fearless parallelism)"** — 워크트리·피처 브랜치를 넘나들어도 겹침 없이 합친다. ⚠️ **리뷰어 본인이 *"대담한 주장이고 확신할 수 없다"* 고 유보한다.**

### 스킬 (리뷰어가 꼽은 것)

| 스킬 | 하는 일 |
|---|---|
| **`why`** | 트랜스크립트만이 아니라 **관련 MCP·CLI를 순회** — PostHog 제품 정보, **Slack의 결정 스레드**, Sentry 로그 → **ADR·의사결정 기록 복원** |
| **`recall`** | 일주일 뒤 복귀용. 트랜스크립트 + `why` 로 Notion·Linear·PostHog 확인 |
| **`interrogate`** | **모델 두셋이 같은 코드를 교차 심문**하고 각자 의견 |
| **`create verification`** | 앱 동작을 증명할 **스크립트 + 교차 확인 세트**를 스스로 생성 |
| **`maintain verification`** | 검증기가 **개발과 어긋나면 갱신** |
| **`onslaught`** | *pivotal moment · crucial · delve · enduring* 제거, **EM 대시 전면 제거** |
| **`bro`** | 마지막 메시지를 **전문용어 없이** 다시 말하기 |
| **`show me your work`** | 실행 경로 되짚기 |
| **`probe`** | *"이루려는 게 애초에 가능한지 보는 빠른 테스트"* |
| **TDD 스킬** | 단위 테스트 먼저, 통과 확인 후 진행 |

> **본인 소스가 기록한 `control glass` · `how` 스킬은 이 영상에 나오지 않고, 여기 나온 것 대부분은 본인 소스에 없다.** 두 목록을 합쳐 읽는다.

### 원칙 — 자막에서 이름이 붙은 일곱 개

**[[laziness-protocol|게으름 프로토콜]]**(지워라·최소 변경) · **제1원칙 재설계**(덧대기 금지) · **[[minimizing-reader-load|독자 부담 최소화]]** · **설계 공간 소진**(→ 아레나) · **[[build-a-lever|지렛대를 만들어라]]** · **검증**(*"초록이 되는 것과 실제 산출물로 증명하는 것은 같지 않다"*) · **컨텍스트 창을 지키고 사람을 막지 마라**.

⚠️ **제목·챕터·설명란은 "21가지"라 하는데 자막에는 "21"이라는 수가 없다.**

### 비용

| | 시간 |
|---|---|
| **[[fable-5-1\|Fable 5.1]] 맨몸**(plan mode·스킬 없음) | **약 30분** |
| **Pstack** | **1시간** |

> **훨씬 더 단단해진(hardened) 애플리케이션으로 이어졌습니다.** (…) **모든 프로젝트에 감자를 던질 필요는 없겠지만** (…) **작은 디자인 변경이나 프런트엔드 UI라면 아마 쓸 필요가 없습니다.**

⚠️ **단일 사례·단일 관찰자이고 토큰 값이 없다. "2배"를 위키의 일반 계수로 쓰지 않는다.** → [[agent-roi-measurement]]

## References

- [[tech-bridge-lauren-tan-trusting-agents]] · [[tech-bridge-pstack-third-party-review]] · [[lauren-tan]] · [[cursor]] · [[molten-base]]
- 개념: [[feature-map]] · [[skill-evals]] · [[agent-verification-skill]] · [[agent-skills]] · [[agent-arena]] · [[agent-swarm]] · [[laziness-protocol]] · [[minimizing-reader-load]] · [[build-a-lever]]

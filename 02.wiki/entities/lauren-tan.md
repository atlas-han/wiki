---
title: Lauren Tan
type: entity
category: person
tags: [cursor, grokbot, agents, refactoring]
links:
  - https://x.com/poteto
sources: [tech-bridge-grokbot-agent-teams, tech-bridge-lauren-tan-trusting-agents]
created: 2026-09-01
updated: 2026-09-13
---

# Lauren Tan

[[cursor|Cursor]] 엔지니어. 본 위키 첫 등장은 MTS 인터뷰의 [[tech-bridge]] 재배포 [[tech-bridge-grokbot-agent-teams]].

## 위키에서 알려진 사실

- [[grokbot|GrokBot]]의 기원이 된 개인 봇 **Benny**(강아지 아바타) 제작자. 동기는 *"제가 자는 동안 에이전트들이 자동으로 버그를 수정"* — Cursor 버그 보고가 감당이 안 되던 상황.
- 일반화된 질문이 제품이 됨: *"모든 사람이 자신만의 봇을 만들고, 정체성을 부여하고, 자체 컴퓨터와 루틴, 자동화 기능 등을 갖출 수 있다면?"*
- 현재 자기 역할을 **디지털 동료들의 매니저**로 규정. 미슐랭 주방 비유 — 직접 요리하지 않고 **수석 셰프로서 품질 관리**.
- 엔지니어 역할론(이 소스의 핵심): 위로는 에이전트 매니저, 아래로는 **코드베이스 관리인**. PM·디자이너가 고품질 코드를 쓸 수 있도록 코드베이스를 좋은 상태로 유지하는 것이 엔지니어 책임.
  - 에이전트가 작동하도록 **리팩토링·재작성에 투자**
  - 규칙·스타일 가이드를 **린트 규칙과 CI 실패로 인코딩** ([[verifiable-goals]]와 동형)
- 레버리지 증거: Cursor에서 대규모 리팩토링·마이그레이션을 대부분 혼자 또는 한 명과 진행. 다른 팀이면 **몇 달~몇 년** 걸렸을 작업.
- 모델 사용: [[grok-4-6|Grok 4.6]]을 엔지니어링에 주로, Fable 등도 병용. 비용 논점 — 본인은 토큰 무제한이지만 고객은 아니다.
- 사내에 유명한 Slack 봇을 남겨둔 이력이 있고, 그것이 GrokBot 패키지화의 단서가 됐다.

## 두 번째 소스 — 59:41 워크숍 (2026-09-12 편)

[[tech-bridge-lauren-tan-trusting-agents]]가 첫 소스의 **방법론을 실제 내용으로 채운다.** 이력이 본인 진술로 확장됐다 — **Cursor 약 5개월**, 그 전 **Meta의 React 팀에서 React Compiler**(지금도 코어 팀), 그 전 **Netflix에서 테크리드 및 약 2년간 엔지니어링 매니저**. X 핸들 `poteto`도 **교차 확인**됐다(*"Potato — E가 들어간 철자"*).

관리와 에이전트를 잇는 유비의 출처가 그 이력이다 — *"관리 스킬과 에이전트를 다루는 법 사이에 유사점이 정말 많다."* → [[agent-manager-analogy]]

### 자기 보고 수치

| 항목 | 값 |
|---|---|
| 지난달 PR | **1,000건** |
| 이번 달(12일 시점) PR | **거의 800건** |
| 하룻밤 자동 병합된 PR | **20건** (main에서 사후 리뷰) |
| GrokBot 리팩터링 | **PR 600건 이상** |
| 평균 PR 크기 | **본인도 모름** (50~1,000줄, 하드 캡 없음) |

> ⚠️ 전부 자기 보고이고 검증 수단이 없다.

### 방법 — 세 기둥

1. **[[agent-verification-skill|검증]]** — 에이전트가 앱을 실제로 띄우고 CPU 트레이스·힙 스냅샷·시뮬레이터로 확인하게 한다. 여기에 [[feature-map]]을 붙여 *"???" 만 적힌 스크린샷 제보* 도 작업이 되게 한다. 도구는 [[pstack|Pstack]].
2. **[[dune-architecture|에이전트 친화 아키텍처]]** — *"가장 짧은 경로가 가장 좋은 경로"*([[shortest-path-architecture]]).
3. **[[hard-vs-soft-enforcement|강제의 층]]** — *"PR에 댓글로 제약을 강제하고 있다면 그건 코드 스멜."*

### 새로 알려진 입장

- **[[greenfield-vs-brownfield-agent-risk|브라운필드가 오히려 안전하다]]** — *"AI 슬롭 이전에 인간 슬롭이 있었다"*, 대기업 인프라는 이미 *가장 능력이 부족한 엔지니어* 를 위한 가드레일이다.
- **[[organic-architecture]]** — 본인 조어. 가드레일 없는 바이브 코딩 코드베이스의 운명.
- **토큰에 대한 정직한 인정** — *"저는 무제한 토큰이 있는 AI 랩에서 일합니다."* 그다음 답은 ROI 트레이드오프다.
- **에이전트의 가치 정의** — *"전에 할 수 없던 일을 할 수 있게 해 주는 것. 제게 그것은 혼자서 코드베이스에 이 수준의 제약을 강제하는 것이었습니다."*
- **맹목적 신뢰를 권하지 않는다** — *"저를 맹목적으로 믿으시라고 권하지 않습니다."*

> ⚠️ **이 소스가 위키의 시점 기록을 흔든다** — 워크숍 당일이 *[[grok-4-6|Grok 4.6]] 발표일이자 그달 12일* 이다. 소스 페이지의 시점 절을 볼 것.

## References

- [[tech-bridge-grokbot-agent-teams]] · [[grokbot]] · [[cursor]] · [[persistent-agent-teams]]
- <https://x.com/poteto>

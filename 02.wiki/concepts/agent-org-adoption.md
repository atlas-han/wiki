---
title: Agent Org Adoption
type: concept
category: pattern
tags: [agent, organization, verification, culture, figma]
related: [verifiable-goals, harness-engineering, spec-driven-development, sprint-contract, outcome-engineering, frontier-engineering, persistent-agent-teams, trusted-throughput, token-roles, company-brain]
first-seen: tech-bridge-figma-coding-agents
sources: [tech-bridge-figma-coding-agents, tech-bridge-frontier-engineering, tech-bridge-dhh-agent-productivity, tech-bridge-ai-native-skills, tech-bridge-grokbot-agent-teams, tech-bridge-claude-platform-agent-era, tech-bridge-trusted-throughput, tech-bridge-company-brain-security, tech-bridge-mousepower-measuring-agents, tech-bridge-lauren-tan-trusting-agents, tech-bridge-zuckerberg-muse-in-daily-use]
created: 2026-08-29
updated: 2026-09-17
---

# Agent Org Adoption

코딩 에이전트를 **개인 생산성 팁이 아니라 조직 변화**로 다루는 패턴. [[eyal-blum|Eyal Blum]]([[figma|Figma]])이 [[tech-bridge-figma-coding-agents]]에서 제시. 희소 자원은 모델 capability가 아니라 **인간 주의력**.

## 3막 곡선

개인과 회사 공통 ([[tech-bridge-figma-coding-agents]] 00:00–02:15):

1. **1막** — 작은 것이 잘 된다. "10x faster."
2. **2막** — 같은 습관을 큰 문제에 적용하면 실패·버그·신뢰 붕괴.
3. **3막** — 가드레일·프롬프팅·컨텍스트라는 진짜 스킬.

조직에서는 막이 고르지 않다. 워크플로를 바꾼 팀과 신뢰를 잃은 팀이 같이 제품을 내야 하므로, 공존을 지원하면서 3막으로 데려가는 것이 과제.

발표 스스로 3막은 "아직 다 오지 않았다" (클라우드 에이전트 × 레거시 빌드 의존성).

## 네 가지 개입

| 개입 | 요지 | 위키 자매 |
|---|---|---|
| **검증 우선 (left-shift)** | generation보다 verification에 투자. 반복 패턴은 결정론적 플로우로 코드화. 테스트 먼저(red-green). 피라미드 아래를 자동화하고 인간 리뷰는 "이걸 만드는가"만 | [[verifiable-goals]], [[harness-engineering]] System Evolution |
| **프롬프팅 → 기획** | why가 맨 위인 계획서, 한 자리에 리뷰할 크기, 단계별 acceptance. 에이전트는 명세를 실행 | [[spec-driven-development]], [[sprint-contract]], [[outcome-engineering]] |
| **회의론자 = 로드맵** | 시니어 저항을 변환 대상이 아니라 검증 갭의 우선순위 목록으로 | (조직 운영) |
| **주의력 소통** | PR/슬랙에서 사람 요약과 AI 생성을 분리 표시. 미표시는 모욕으로 읽힘 | 인간 주의력을 하니스 제약으로 취급 |

## 현장에서 바로 쓰는 규칙 (영상)

- Playwright MCP처럼 "사람이 탐색하던 것"을 에이전트 검증으로 옮길 수 있으면 옮긴다.
- 에이전트가 유용한 패턴을 찾으면 그날 테스트로 고정한다. LLM은 추론에만.
- 계획 1주 → 에이전트 구현 → 사람 리뷰. PR은 커피 없이 한 자리에 읽힐 크기(~10–100줄).
- 1막 팀과 3막 팀이 같은 제품을 내게 한다. 최고 엔지니어를 변환하지 말고 안전 로드맵 오너로.
- 모든 PR 설명: 손글씨 요약 다음에 AI 본문. Slack에서 에이전트를 태그해 그 스레드에서 루프를 닫는다.

## 위키 합성

Anthropic 쪽 [[agent-harness-design]]은 *모델이 못하는 것에 대한 가정*을 하네스에 인코딩한다. 이 페이지는 *조직이 에이전트를 넣을 때 깨지는 것*(리뷰 부하, 시니어 맥락, 주의력)을 인코딩한다. 같은 루프의 조직면: 실패를 규칙으로 ([[harness-engineering]] "every mistake becomes a rule") — 다만 규칙은 훅/테스트만이 아니라 **소통 예절과 로드맵 소유권**이기도 하다.

Amazon 현장([[tech-bridge-frontier-engineering]], [[frontier-engineering]])은 같은 "도구를 뿌리면 안 된다"를 **배포 속도**로 측정한다. Stores 50팀에서 90%가 [[kiro|Kiro]]를 썼는데 절반만 4.5x(중앙값). Figma가 시니어 저항·provenance를 강조한다면 Amazon은 루프에서 사람 제거, 2개월 감속 승인, 결정 병목, 주니어의 AI 리뷰 근육을 강조한다.

세 번째 현장([[tech-bridge-dhh-agent-productivity]], [[dhh]]): 창업자/개인이 에이전트와 **직결**. 사람 승인 계층이 10x를 죽인다. 대기업은 innovator's dilemma 슈퍼탱커 → 밖에서 자기 5%를 다시 쓴다([[omarchy]]). Figma·Amazon이 조직 안 습관을 바꾼다면 DHH는 중개자를 제거한다.

[[tech-bridge-ai-native-skills]]는 같은 "방식이 가른다"를 **스킬 카탈로그/거버넌스**로 구체화한다. 거버넌스 없는 스킬 = 새 기술부채. 15팀 시뮬에서 도구는 같아도 가시성·품질이 분산.

[[tech-bridge-grokbot-agent-teams]]([[cursor]], [[persistent-agent-teams]])는 **채택 경로 자체**를 같은 문법으로 반복한다 — 작은 팀 프로토타입 → 사내 배포 → *내부 PMF를 외부 출시 신호로* 사용. 이 위키에서 새로운 것은 두 가지다. ① 확산이 **엔지니어링 밖**(시장 진출·운영·제품)까지 갔고, 그 이유로 지목된 것이 모델 성능이 아니라 **역할 무관 접근성과 기존 도구 연동**이다. ② 대중 채택의 병목을 **UX**로 특정한다 — *"일상적인 작업에 에이전트를 활용하기 위한 UX가 형편없기 때문에 여전히 대부분 코딩 기반"*. Figma가 시니어 저항을, Amazon이 배포 속도를, DHH가 승인 계층을 병목으로 봤다면, 여기서는 **인터페이스**가 병목이다.

엔지니어 역할에 대한 처방은 오히려 수렴한다: 규칙을 **린트 규칙과 CI 실패로 인코딩**하고 에이전트가 성공하도록 코드베이스를 리팩토링하라 — [[verifiable-goals]]와 [[frontier-engineering]] 5습관의 재확인.

## 에이전트 우선 재설계 — 가장 흔한 실수 (2026-09-01)

[[tech-bridge-claude-platform-agent-era]]에서 [[anthropic|Anthropic]] Claude Platform 팀이 도입 실패의 **형태**를 지목한다. 이 위키가 지금까지 다룬 *습관 변화*보다 한 단계 더 아래, **프로세스 설계**의 문제다.

먼저 규모의 실수:

> "좋아, 멋지다. 엄청난 과제를 하나 내서 우리 대형 은행의 **KYC 프로세스 전체를 자동화**해야겠다"

그러나 근본 오류는 크기가 아니라 형태다.

> 이미 여러 정책과 절차를 거쳐 작동하는 **복잡한 인간 중심의 프로세스를 가져와서, 인간의 비효율적인 부분에만 에이전트를 투입**하려는 데 있습니다. (…) 에이전트를 **기존 인간이 하던 방식에 맞춰야** 하기 때문입니다.

처방은 **과감한 세분화 + 에이전트 우선(agent-first) 재창조** — 가장 기본적인 것부터 "신입 사원이 하듯" 생각하고 그 과정을 다시 만든다.

> **기존 프로세스를 간소화하고 처음부터 다시 설계할수록 더 큰 성공을 거둘 수 있습니다.**

여기에 이 위키에 유용한 경고가 하나 더 붙는다 — **도메인 전문가의 직관이 틀린다.** 물어보면 "에이전트가 하고 나에게 피드백을 요청하며 주고받는 게 좋다"고 답하지만 **실제로는 그 방식이 효과적이지 않다.** 요구사항 인터뷰만으로 워크플로를 설계하면 안 되는 이유다.

이는 [[tech-bridge-grokbot-agent-teams]]의 "에이전트가 UI에 맞추는 게 아니라 UI가 에이전트에 맞춘다"와 같은 방향이고, [[frontier-engineering]]의 습관 변화보다 **한 층 아래의 재설계**를 요구한다.

## 도입 이후의 계측 (2026-09-01)

[[trusted-throughput]]이 이 개념의 **다음 단계**를 채운다 — 도입의 고비를 넘긴 조직이 무엇을 재야 하는가. 특히 이 개념과 직접 맞물리는 관찰:

> 사용량 대시보드를 **연기 감지기**와 같은 것으로 생각합니다.

조사할 신호가 **거의 안 쓰는 국소적 집단**(도입 격차)이라는 방향은 [[frontier-engineering]]이 관찰한 **팀 간 50배 편차**와 같은 자리에 있다. 단, 팀마다 AI 활용 방식이 다르므로 맥락을 고려한 비교여야 한다.

## 키우는 것이지 만드는 것이 아니다 (2026-09-10 · [[tech-bridge-company-brain-security]])

이 페이지의 *"에이전트 우선 재설계는 가장 흔한 실수"* 와 같은 결의 진술이 **지식 베이스 도입**에 대해 나왔다. [[tanmai-gopal]]: *"100년 된 조직의 회사 두뇌는 만들 수 없어요. 자기 가족 것도 겨우 만들까 말까인데. (…) 회사에서 일의 일부를 하는 각 사람이 회사 두뇌의 자기 몫을 소유하고 만드는 것입니다. **만드는(build) 게 아니라 키우는(grow)** 겁니다."* 2년짜리 프로젝트 대신 **셀프 서비스 누적** — 그리고 그 누적이 실제로 일어나는지의 지표로 **일일 업데이트 수**를 제안한다 → [[company-brain]]. 이 페이지의 3막 곡선으로 보면, 그 지표가 우상향하는 것이 3막(정착)의 신호다. ⚠️ 자사 2개월 데이터뿐.

## "우리는 표본이 아니다" (2026-09-12 마우스파워 편)

[[tech-bridge-mousepower-measuring-agents]]가 도입 논의에 **표본 문제**를 들여온다.

> **이 방의 모두가 아주 편향돼 있고, 우리는 얼리어답터**입니다. (…) **결국 우리가 이 기술을 도입하도록 도우려는 사람들을 우리가 대표하지는 않습니다.** 어떤 사람들은 **여전히 ChatGPT에 복붙**하고 있습니다.

> 우리 모두가 어떤 식으로든, **직간접적으로 토큰을 팔고 있다**는 걸 스스로 되새기는 게 중요하다고 생각합니다.

역사적 모델은 [[james-watt]]다 — 도입의 장벽이 성능이 아니라 **인지 부조화**이고, 처방은 **상대의 멘탈 모델 위에 지표를 세우는 것**이다. → [[mousepower]] · [[agent-roi-measurement]]

## 도입 준비도를 인프라로 재기 (2026-09-12 Lauren Tan 편)

[[tech-bridge-lauren-tan-trusting-agents]]는 준비도를 *조직의 AI 성숙도* 가 아니라 **기존 엔지니어링 인프라의 엄격함**으로 잰다.

> Meta나 Google 같은 큰 회사의 인프라는 — 말하기 안 좋지만 — **팀에서 가장 능력이 부족한 엔지니어를 기준으로** 설계돼 있습니다. (…) **그 수준의 인프라가 이미 있으면 여러분의 에이전트는 이미 꽤 견실하게 일할 수 있습니다.**

→ [[greenfield-vs-brownfield-agent-risk]]

그리고 **비엔지니어의 기여**가 도입의 지표로 제시된다 — PM·디자이너가 [[grokbot|GrokBot]]으로 직접 기능을 내보내고 엔지니어는 리뷰만 한다. 화자는 [[grokbot|GrokBot]]을 *"기술 분야가 아닌 사람들에게 결정적 순간"* 이라 부르고, 근거는 **인터페이스**다(*"iMessage처럼 보입니다"*).

## References

- [[tech-bridge-figma-coding-agents]]
- [[tech-bridge-claude-platform-agent-era]] — 에이전트 우선 재설계 · 전문가 직관의 실패
- [[tech-bridge-trusted-throughput]] · [[trusted-throughput]] — 도입 이후의 계측
- [[tech-bridge-frontier-engineering]] · [[frontier-engineering]]
- [[tech-bridge-dhh-agent-productivity]] · [[dhh]] · [[omarchy]]
- [[tech-bridge-ai-native-skills]] · [[agent-skills]]
- [[tech-bridge-grokbot-agent-teams]] · [[persistent-agent-teams]] · [[cursor]]
- [[eyal-blum]] · [[figma]]
- [[tech-bridge-company-brain-security]] — 키우는 것이지 만드는 것이 아니다 · [[company-brain]] (2026-09-10)

## 도입 문제의 세 갈래 — Muse의 답 (2026-09-17)

[[tech-bridge-zuckerberg-muse-in-daily-use]]가 *"사람들이 AI로 뭘 해야 할지 모른다"* 를 **명시적인 문제 진술로** 올리고, [[muse|Muse]]가 거기에 내놓는 답을 정리하게 해 준다.

> **많은 사람이 AI에 대해 갖는 큰 문제 하나는 그걸로 뭘 해야 할지, 어떻게 최대한 끌어내야 할지 잘 모른다는 것입니다.**

| 갈래 | 방식 | 페이지 | 어느 소스 |
|---|---|---|---|
| **먼저 제안한다** | 아이디어 피드 | [[proactive-idea-feed]] | **두 편 모두** — 앞 편은 [[agent-fleet-learning\|함대 학습]] 질문의 답으로, 이번 편은 **도입 문제의 답**으로 |
| **친근하게 만든다** | 이름·아바타·일하는 모습 | [[agent-persona-naming]] | **이번 편 신규** |
| **남의 쓰임을 빌려 온다** | 익명화된 통찰 | [[agent-fleet-learning]] | 앞 편만 (⚠️ **이번 편엔 언급 없음**) |

이 위키의 기존 도입 서술이 대체로 **조직**(팀·회사)을 단위로 삼았다면, 이 셋은 **개인**을 단위로 삼는다. 진행자가 든 값이 특히 조직 쪽 지표와 다르다 — *"시간 측면이 있고, 저에게는 **영감(inspiration)** 측면도 있었습니다"*. **하지 않았을 일이 생긴 것**이 값이다.

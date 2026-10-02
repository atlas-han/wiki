---
title: Self-Contained Systems — AI 컨텍스트 경계로서의 수직 분할 (Self-Contained Systems)
type: engineering
category: pattern
tags: [architecture, self-contained-systems, microservices, monolith, modular-monolith, vertical-slicing, context, agents, team-topology]
aliases: [self-contained system, SCS, 자체 포함 시스템, 수직 분할, verticals, distributed big ball of mud]
related: [ai-unified-process, legacy-code-modernization, architecture-as-remaining-art, organic-architecture, agent-skills, context-rot, technical-debt]
first-seen: tech-bridge-sdd-enterprise-lessons
sources: [tech-bridge-sdd-enterprise-lessons]
created: 2026-10-02
updated: 2026-10-02
---

# Self-Contained Systems

**애플리케이션을 UI · 비즈니스 로직 · 데이터베이스를 한 저장소/프로젝트에 담은 수직(vertical) 단위로 나누는 아키텍처 스타일.** [[simon-martinelli|Simon Martinelli]]는 [[tech-bridge-sdd-enterprise-lessons]]에서 이것을 **AI가 일할 컨텍스트를 한 곳에 모으는 단위**로 권한다 — 순진한 마이크로서비스(컨텍스트가 흩어짐)와 거대 모놀리스(컨텍스트가 너무 큼) 사이.

> *"the self-contained system architecture just says We create verticals. So we split our application into verticals which has UIs, business logic and database in one repo usually or in one project at least or in one application"* (19:04~19:18)

> ⚠️ 약어 **SCS**는 영상 설명란의 표기이고 자막에서는 발화되지 않는다. 화자는 이 스타일이 *"not so well known"*, 마이크로서비스와 *"approximately"* 같은 시기에 나왔다고만 한다(18:53~19:02). 이 위키는 원 정의 문서를 ingest하지 않았다.

## 문제 — 두 극단

| | 순진한 마이크로서비스 | 거대 모놀리스 |
|---|---|---|
| 증상 | *"they were focusing on the micro in microservices"*(17:30~17:32) → *"distributed big ball of mud"*(17:36~17:38). 한 보험사: 마이크로서비스 약 500개 + 마이크로 프런트엔드 약 500개, 프런트·백엔드 n:m(17:40~17:56) | 현재 ERP: *"thousands of database tables and a lot of modules"*(18:42~18:47) |
| AI에게 | *"you need the code that the AI should work on in a single place at least on your machine"*(18:07~18:14) — 흩어진 컴포넌트를 *"mix and match"* 해야 한다 | *"the context is too big"*(18:48~18:50) |
| 처방 | — | 마이크로서비스의 반동으로 모놀리스/모듈러 모놀리스로 가는 흐름에 *"I would say stop here don't do that"*(18:30~18:33) |

⚠️ 수치는 화자의 고객 사례이고 출처 검증이 없다.

## 왜 AI 협업에 맞나 (화자의 논거)

1. **컨텍스트 경계 = 시스템 경계** — 한 vertical이면 *"the AI can exactly work on that"*(19:22~19:26).
2. **vertical마다 기술과 스킬** — 재고는 Vaadin, 주문 관리는 React 프런트엔드(19:32~19:47). 스킬도 vertical의 기술에 맞춰 붙인다. → [[agent-skills]]
3. **팀 단위** — SCS당 개발자 1~2명(21:15~21:30). → [[ai-unified-process]]

### 한 스택의 이점

*"if you can stay on one stack (…) then probably creating guards[=guardrails?] is simpler because you need to create skills and all the stuff just for one technology"*(19:49~20:06). React/Angular + Spring Boot/Quarkus 조합이면 *"they have to create this twice and also maintain that twice"*(20:15~20:20). 하네스(스킬·가드레일)의 **유지 비용이 스택 수에 비례**한다는 관찰이다.

## 위키에서의 좌표

- [[legacy-code-modernization]]([[ibm|IBM]])의 아키텍처 축은 *긴밀히 결합된 모놀리스 → 독립 서비스*. 이 페이지는 **"독립 서비스"의 크기를 AI 컨텍스트로 정하라**는 기준을 더한다.
  > ⚠️ **Contradiction:** IBM 편은 모놀리스 → 서비스 분리를 현대화 방향으로 두고, 화자는 과도한 마이크로서비스를 *distributed big ball of mud* 로 본다. 다만 IBM 편이 서비스 크기를 말하지 않으므로 직접 충돌이라기보다 **세분화 정도**에서 갈린다.
- [[architecture-as-remaining-art]] · [[organic-architecture]] — "에이전트가 착지하는 기반이 나쁘면 기여도 나쁘다"를 **저장소·배포 단위** 수준에서 구체화한 사례.
- [[context-rot]] — "컨텍스트가 너무 크다"의 모델 쪽 근거를 다루는 페이지. 이 소스는 그것을 **아키텍처로 피한다.**

## 표시해 둔 것

> ⚠️ **한 실무자의 권고, 비교 측정 없음.** SCS로 나눈 뒤 AI 산출물이 실제로 나아졌는지의 수치는 없다. ERP를 vertical로 나누는 작업 자체의 비용·기간도 말하지 않는다.

## References

- [[tech-bridge-sdd-enterprise-lessons]] · [[simon-martinelli]]
- 관련: [[ai-unified-process]] · [[legacy-code-modernization]] · [[architecture-as-remaining-art]] · [[organic-architecture]] · [[agent-skills]] · [[context-rot]] · [[technical-debt]]

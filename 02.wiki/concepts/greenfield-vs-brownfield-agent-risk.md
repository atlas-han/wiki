---
title: 그린필드가 브라운필드보다 위험하다 (Greenfield vs Brownfield Agent Risk)
type: concept
category: framing
tags: [legacy, refactoring, guardrails, big-tech, risk, agents]
aliases: [브라운필드가 안전하다, 대기업 문제가 모두의 문제]
related: [organic-architecture, shortest-path-architecture, hard-vs-soft-enforcement, ai-slop, dune-architecture, agent-org-adoption, system-level-quality]
first-seen: tech-bridge-lauren-tan-trusting-agents
sources: [tech-bridge-lauren-tan-trusting-agents]
created: 2026-09-13
updated: 2026-09-13
---

# 그린필드가 브라운필드보다 위험하다

**에이전트에게는 레거시 코드베이스가 오히려 안전하고, 새로 시작한 바이브 코딩 프로젝트가 가장 위험하다**는 주장. [[lauren-tan]]이 [[tech-bridge-lauren-tan-trusting-agents]]에서 통념을 뒤집으며 제시했다.

## 논거 — 대기업 인프라는 이미 가드레일이다

> **Meta에는 정말 훌륭한 엔지니어가 많지만 — 놀라실 텐데 코드 품질이 그렇게 좋지는 않습니다.** 그래서 저는 자주 농담합니다 — **AI 슬롭 이전에 인간 슬롭이 있었다**고요.

> Meta나 Google 같은 큰 회사의 인프라는 — 말하기 안 좋지만 — **팀에서 가장 능력이 부족한 엔지니어를 기준으로** 설계돼 있습니다. **프레임워크, 컨벤션, 가드레일, 제한된 자격증명.** **인턴이 프로덕션 데이터베이스를 날리지 않도록** 말이죠.

> **그 수준의 인프라가 이미 있으면 여러분의 에이전트는 이미 꽤 견실하게 일할 수 있습니다.**

**핵심 뒤집기**: 대규모 조직이 *신뢰할 수 없는 기여자* 를 위해 지어 놓은 것이 그대로 **에이전트를 위한 것**이 된다. 그래서 *"대기업의 문제가 이제 모두의 문제"* 이고, 동시에 **대기업의 해법도 모두의 해법**이다.

## 반대편

> **그린필드 — 완전히 새 애플리케이션이 제 생각에는 가장 큰 위험이고 동시에 가장 큰 기회**입니다.

이유는 [[organic-architecture]]다 — 제약이 없으면 에이전트는 편의로 수렴하고, 코드베이스는 이해 불가능해진다.

## 전제 — "이미 잘 세팅돼 있다면"

화자가 조건을 단다: *"브라운필드 애플리케이션은 사실 꽤 좋은 자리에 있습니다 — **이미 잘 세팅돼 있다면요.**"*

즉 이 주장은 **모든 레거시가 안전하다**가 아니라 **가드레일의 유무가 신·구보다 중요하다**는 것이다. 그리고 화자는 재작성을 *"고려해 볼 만하다"* 고 옹호하되(업계 통념과 반대), 그 재작성의 목적지는 **더 많은 제약**([[dune-architecture]])이다.

## 위키의 다른 페이지와 맞닿는 자리

- **[[tech-bridge-cursor-legacy-refactoring]]**(09-09) — 같은 회사, 같은 주제의 다른 각도. 그쪽이 *레거시를 어떻게 옮기는가* 의 시연이라면 이쪽은 **왜 레거시가 생각보다 괜찮은가** 다.
- **[[ai-slop]]** — *"AI 슬롭 이전에 인간 슬롭"* 은 슬롭을 **AI 고유 현상이 아니라 가드레일 부재의 함수**로 재정의한다. 09-12에 세운 *슬롭 = 결정의 부재* 와 같은 결론에 **다른 경로**로 도달한다.
- **[[agent-org-adoption]]** — 도입 준비도를 *조직의 AI 성숙도* 가 아니라 **기존 엔지니어링 인프라의 엄격함**으로 재는 관점.
- **[[credential-injection-outside-sandbox]]** · **[[ai-privilege]]** — *"인턴이 프로덕션 DB를 날리지 않도록 자격증명을 제한한다"* 가 에이전트 권한 논의와 같은 자리에 놓인다.

## 표시해 둔 것

> ⚠️ **당사자 진술이고 표본은 화자 한 명의 경력**(Netflix·Meta·Cursor)이다. Meta의 코드 품질에 대한 평가도 개인 관찰이다.
>
> ⚠️ **"가장 큰 기회"** 쪽은 전개되지 않는다 — 그린필드의 이점이 무엇인지 소스가 말하지 않는다.

## References

- [[tech-bridge-lauren-tan-trusting-agents]] · [[organic-architecture]] · [[shortest-path-architecture]] · [[dune-architecture]] · [[ai-slop]] · [[tech-bridge-cursor-legacy-refactoring]] · [[lauren-tan]]

---
title: 회사 고유 지식이라는 해자 (Company Knowledge Moat)
type: concept
category: framing
tags: [vertical-agents, internal-agents, context, build-vs-buy, differentiation]
aliases: [기성 수직 에이전트 vs 자체 에이전트, 회사 지식 해자]
related: [company-brain, agent-knowledge-sourcing, file-system-agent, knowledge-work-agent-gap, context-engineering, agent-umwelt]
first-seen: tech-bridge-vercel-eve-filesystem-agent
sources: [tech-bridge-vercel-eve-filesystem-agent, tech-bridge-oracle-agent-memory-harness]
created: 2026-09-19
updated: 2026-09-24
---

# 회사 고유 지식이라는 해자

**같은 데이터베이스에 붙는 기성 수직(vertical) 에이전트와 사내 에이전트를 가르는 것은 모델이나 도구가 아니라 회사 고유의 맥락 지식이라는 주장.** [[tech-bridge-vercel-eve-filesystem-agent]]에서 [[andrew-qu|Andrew Qu]]가 **기성 제품들을 직접 테스트한 뒤** 내린 결론이다.

> D0을 개발하기 전에, **Snowflake 인스턴스를 가져와 Snowflake 쿼리를 실행하는 데 특화된 수직 에이전트를 개발하는 업계 자금력이 풍부한 스타트업들을 많이 테스트**해 봤습니다. 하지만 **우리 에이전트를 진정으로 돋보이게 하는 것은 매우 구체적인 회사 지식을 활용하는 것**이라는 사실을 알게 되었습니다. (15:02~15:20)

## 그 지식이란 무엇인가

> **Vercel은 웹 기반 회사이기 때문에 웹사이트와 웹 자산을 보유한 고객이 많습니다. 어떤 데이터를 언제 쿼리해야 하는지, 어떤 요소들이 서로 어떻게 연결되는지 등을 더 자세히 파악**해야 합니다. (15:20~15:37)

두 가지다 — **언제 무엇을 묻는가**(질의의 의도 매핑)와 **무엇이 무엇과 연결되는가**(도메인의 관계 구조). 둘 다 스키마에 없다. 스키마는 *테이블이 있다* 고 말하지 *이 회사에서 "활성 고객"이 무슨 뜻인지* 말하지 않는다.

> **시중에 나와 있는 기성 에이전트들은 훌륭하고 사용해 볼 만하지만, 진정으로 효율을 높이려면 자체 에이전트를 구축하고 회사별 전문 지식을 최대한 반영하는 것이 좋습니다.** (15:37~15:46)

## 이 위키에서의 좌표

**[[company-brain]](09-10 [[promptql|PromptQL]])과 같은 방향, 다른 형식.**

| | [[company-brain]] | **이 페이지** |
|---|---|---|
| 지식의 형태 | **사람이 읽는 위키** (5,000페이지) | **에이전트가 grep하는 시맨틱 레이어** |
| 갱신 | 에이전트 제안 → **사람 승인**([[named-human-accountability]]) | 질의 증류([[query-to-skill-distillation]]) — **게이트 없음** |
| 목적 | 조직의 기억 | 에이전트의 성능 |

**두 소스가 서로를 모른 채 같은 결론에 닿았다** — 조직에서 에이전트를 쓸모 있게 만드는 것은 모델이 아니라 조직이 쌓은 맥락이다.

그리고 [[agent-knowledge-sourcing]]의 네 갈래에 **파일 시스템 탐색**이 다섯 번째로 붙는다.

## ⚠️ 유보 — 인센티브를 보라

**판매자가 "직접 만들라"고 권하는 구조**라 인센티브가 뒤집혀 보이지만 뒤집히지 않았다 — *직접 만들되 우리 프레임워크([[eve-framework|Eve]])로*. 즉 이 주장은 **경쟁 제품군(수직 에이전트 스타트업)을 배제하고 자사 프레임워크의 시장을 만드는** 방향으로 정확히 작동한다.

다른 빈자리:

- **테스트했다는 스타트업의 이름·기준·결과가 하나도 없다.** *"많이 테스트해 봤다"* 뿐이다.
- **무엇이 부족했는지의 사례가 없다** — 기성 에이전트가 틀린 구체적 질문이 제시되지 않는다.
- **비용 비교가 없다.** 자체 구축·유지의 비용 대 기성품 구독의 비용.
- **일반화 가능한가**가 다뤄지지 않는다. Vercel은 데이터 팀과 시맨틱 레이어를 이미 가진 회사다 — 그것이 없는 조직에도 같은 결론이 서는지 소스가 말하지 않는다.
- 반대 방향의 증거([[agents-as-patient-specialists]]처럼 좁은 전문화가 이기는 경우)와 대조되지 않는다.

## References

- [[tech-bridge-vercel-eve-filesystem-agent]] — first-seen
- [[andrew-qu]] · [[vercel]] · [[eve-framework]]
- 관련: [[company-brain]] · [[agent-knowledge-sourcing]] · [[file-system-agent]] · [[query-to-skill-distillation]] · [[knowledge-work-agent-gap]] · [[context-engineering]]

## 2026-09-24 — 시맨틱 레이어에 지각론의 이름: 움벨트

[[tech-bridge-oracle-agent-memory-harness]]([[ignacio-martinez|Ignacio Martinez]] / [[oracle|Oracle]])가 이 페이지의 *"회사 고유의 맥락 지식"* 을 **시맨틱 레이어 = 에이전트의 움벨트**로 부른다 — 동료 사이엔 말하지 않아도 아는 것, *"아이에게는 모든 것을 명시해야 하는"* 것: **tribal knowledge · institutional knowledge · 데이터가 어떻게 모델링되고 쿼리가 어떻게 실행되는가 · 메타데이터**(32:24~33:13). → [[agent-umwelt]]

**같은 방향의 세 번째 소스**다(Vercel의 이 페이지, PromptQL의 [[company-brain]]에 이어). 이 소스가 더하는 것은 **넣지 않은 것의 성질** — 렌즈 밖의 것은 에이전트에게 *틀린 것이 아니라 존재하지 않는다*(⚠️ 위키의 확장). ⚠️ 세 소스 모두 **판매자**다.

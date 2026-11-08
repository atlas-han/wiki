---
title: Salesforce
type: entity
category: org
tags: [enterprise-software, crm, dreamforce, agents, openai-partner]
aliases: [Salesforce, 세일즈포스]
links:
  - https://www.salesforce.com/
  - https://www.salesforce.com/agentforce/
sources: [tech-bridge-altman-benioff-dreamforce, tech-bridge-knowledge-work-agent-infrastructure, tech-bridge-salesforce-claude-code-agentic-shift]
created: 2026-09-23
updated: 2026-11-08
---

# Salesforce

엔터프라이즈 소프트웨어 회사. CEO 겸 회장 [[marc-benioff|Marc Benioff]]. 연례 행사 **Dreamforce**의 주최사. 본 위키에서는 [[tech-bridge-knowledge-work-agent-infrastructure]]에 지나가는 언급이 먼저 있었고, [[tech-bridge-altman-benioff-dreamforce]]가 **회사가 무대에 선 첫 소스**다.

> ⚠️ **회사 자체에 대한 1차 소스는 없다.** 아래는 전부 CEO의 무대 발언과 영상 설명란이다.

## 소스에서 확인되는 것

| 항목 | 내용 | 근거 |
|---|---|---|
| **Dreamforce 2026** | [[sam-altman]] 대담이 열린 무대 | 자막(00:12) · 설명란 링크 `dreamforce_2026` |
| **직원 수** | *"9만 명"* | Benioff (15:33~15:35), 자기 보고 |
| **OpenAI와 공동 개발한 플랫폼** | *"귀사와 함께 개발한 이 AI 플랫폼"* | 27:31~27:33. ⚠️ en-orig *"AI force platform"* — 설명란이 링크한 **[Agentforce]** 로 보이나 **판독 보류** |
| **동적 인터페이스 데모** | 기조연설에서 모델이 *"동적으로 인터페이스를 그려내는"* 것을 시연 | 26:59~27:12 → [[model-rendered-interface]] |

## 미해결

- **Agentforce** — 설명란 링크만 있고 자막에서 이름이 확정되지 않는다. 이 위키는 별도 페이지를 만들지 않았다.
- OpenAI와의 계약·범위.
- 기조연설 데모의 실제 구성(무엇이 생성되고 무엇이 미리 만든 것인지).

## 엔지니어링 조직의 에이전트 코딩 확산 (2026-11-08 · [[tech-bridge-salesforce-claude-code-agentic-shift]])

회사 엔지니어링 조직에 대한 **첫 소스**다. 한국어 해설이 Salesforce News 두 글과 Claude 공식 채널의 고객 사례 영상을 옮긴다(위키 미열람, 당사자 자료).

| 항목 | 해설 전달 내용 |
|---|---|
| 규모 | 엔지니어 1만 5천 명에게 에이전트 코딩([[claude-code]]) 확산 |
| headless화 | 수십 년 된 앱을 API로 쓸 수 있게 — 6개월~1년짜리를 몇 주~몇 달에. 영어 발췌 *"80-90%of API coverage for all the clouds"*(01:18~01:20) |
| 측정 | Stanford 연구진과 [[effective-output-metric|유효 산출량]] 점수, 두 배 → 점수당 비용 |
| 확산 지도 | [[agentic-coding-maturity-curve|에이전트 코딩 성숙도 곡선]](9단계 · 4레벨) — 한두 달 만에 많은 인원을 레벨 3 · 4로 |
| 품질 | 코드양 거의 두 배, 코드당 버그 감소, 5월 글 기준 전체 장애 5% 감소 |
| 모델 교체 | 라벨링된 티켓 · PR로 만든 벤치마크 + **실패 세트** |

- ⚠️ **Dreamforce 제품명 미확정**: 해설 원음 *클로드 포스* vs 영어 더빙 *Agentforce*(01:38). 이 페이지의 `links`에 있는 Agentforce와 같은 것인지 정하지 않는다.
- 해설이 부르는 **리처드**(성 · 직함 미발화)는 페이지를 만들지 않았다.

## References

- [[tech-bridge-altman-benioff-dreamforce]] · [[tech-bridge-knowledge-work-agent-infrastructure]]
- [[marc-benioff]] · [[openai]] · [[model-rendered-interface]]

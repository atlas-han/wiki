---
title: AI 데이터 노출 (AI Data Exposure)
type: concept
category: theory
tags: [security, data-security, data-exposure, shadow-ai, dlp, threat-model, governance, observability]
aliases: [AI data exposure, AI 데이터 노출, data exposure from AI, 섀도우 AI, shadow AI, 숨은 AI 보안 위험]
related: [lineage-driven-risk-visibility, lethal-trifecta, prompt-injection, agent-governance-layers, shift-left-security, continuous-security-validation, retrieval-augmented-generation, model-context-protocol, agents-as-catalyst, least-privilege-connectors]
first-seen: tech-bridge-ai-data-exposure-hidden-risk
sources: [tech-bridge-ai-data-exposure-hidden-risk]
created: 2026-10-01
updated: 2026-10-01
---

# AI 데이터 노출

**민감 데이터가 AI 시스템의 모든 칸(학습 데이터·프롬프트·RAG·컨텍스트/정책·도구·하위 에이전트)과 직원의 AI 사용(업로드·복사-붙여넣기·파생 파일)을 따라 흐르면서, 기존 보안 도구가 보지 못하는 곳에서 노출되는 문제.** [[jeff-crume|Jeff Crume]]([[ibm|IBM]])이 [[tech-bridge-ai-data-exposure-hidden-risk]]에서 정리했다. 핵심 주장은 *무엇을 쓰나* 가 아니라 *어떻게 흐르나* 를 봐야 한다는 것.

> *"It's not enough just to know what AI tools are in use, although that certainly is a good place to start. You also need to know how sensitive data is flowing through AI systems, and where it might be exposed."* (01:35~01:45)

## 세 질문 — 기존 DLP가 답하지 못하는 것

> *"what did data did the AI use? Where did it get that data? And ultimately, how (…) are we going to manage the AI data exposure in a proactive way? Traditional DLP, data loss prevention, and AI tools can't answer these questions."* (01:11~01:33)

화자는 *왜* 기존 DLP가 못 하는지 직접 말하지 않는다. 영상 전체에서 읽히는 이유는 둘이다(⚠️ 위키의 정리): ① **형태가 바뀐다** — RAG·에이전트·시스템이 데이터를 변환하고, *"If I'm looking for it in only this form, I might miss it"*(05:41~05:46) ② **경로가 AI 안에 있다** — 도구가 DB에 쓰고, 에이전트가 에이전트를 낳는 경로는 파일·네트워크 경계 중심의 도구가 보지 못한다. → [[lineage-driven-risk-visibility]]

## 노출 경로

| 경로 | 무엇 | en-orig |
|---|---|---|
| **섀도우 AI** | *"unauthorized AI that people are deploying inside the environment"* — 정책이 요구하는 보안 통제가 없다 | 00:32~00:43 |
| **공개 챗봇 입력** | 질문에 민감 스프레드시트를 붙인다 → *"it basically becomes public information"* | 00:46~01:05 |
| **아키텍처의 각 칸** | 학습 데이터 · 프롬프트 첨부 · 컨텍스트/정책(경쟁 우위 노하우) · 도구(*"Are they guarding it or not?"*) · 하위 에이전트 | 02:47~04:07 |
| **직원 행위(workforce)** | 업로드·다운로드, 복사-붙여넣기(*"the data now is living in a different home"*), 파생 파일, 동료와 공유 | 06:06~06:57 |

> ⚠️ **Contradiction (범위 차이, 미해소):** 공개 챗봇에 넣은 데이터가 *"they can use that sensitive information to train their models, and then it's available to everyone"*(01:02~01:05)는 일반화다. [[katelyn-lesse|Katelyn Lesse]]([[anthropic]] 플랫폼)는 *"고객 데이터로 학습하지 않는다"* 고 말한다. 대상(소비자 챗봇 vs API)과 약관이 다를 수 있고, 화자는 어떤 서비스인지 말하지 않는다.

## workload vs workforce

> *"There's a workload stream, which is basically inside the AI systems themselves, and the workforce stream, where this is the employees' use of the AI."* (04:50~04:59)

이 구분은 이 위키에서 처음이다. 지금까지의 에이전트 보안 페이지들([[agent-governance-layers]] · [[least-privilege-connectors]] · [[lethal-trifecta]])은 거의 전부 **workload 쪽**(에이전트가 무엇에 접근하나)이었다. workforce는 **사람이 AI에 무엇을 넣고 무엇을 꺼내 가나**다 — 섀도우 AI와 챗봇 붙여넣기가 여기 속한다.

## 관리 — 세 렌즈와 하나의 뷰

세 discovery 렌즈(agentic platform · endpoint DLP · 클라우드/온프렘)는 *"Each one of these only sees part of the picture"*(09:04~09:06). 요구는 통합 뷰 + 넷: AI 인지 자동 분류·발견(연속) · [[lineage-driven-risk-visibility|lineage 기반 위험 가시성]] · 지능형 조사(*"weeks down to minutes"*, 목표치) · 규제 준수 보고(GDPR · EU AI Act · SOC 2 · ISO 27001 · HIPAA). 세부는 [[tech-bridge-ai-data-exposure-hidden-risk]] §5~6.

## 이 위키에서의 좌표

- **[[lethal-trifecta]]와의 관계** — 트리펙타는 **공격자가 있는** 유출(신뢰할 수 없는 콘텐츠가 에이전트를 조종)의 성립 조건이다. 이 개념은 **공격자 없는** 노출 — 부주의·무단 사용·불투명한 흐름 — 이다. 트리펙타의 ①(비공개 데이터)이 **어디에 있는지 모른다**는 것이 이 개념의 출발점이고, ③(외부 노출)을 **사후에라도 추적**하는 것이 처방이다. ②([[prompt-injection]])는 소스에 한 번도 나오지 않는다. ⚠️ 위키의 정리.
- **[[shift-left-security]] · [[continuous-security-validation]]** — 같은 화자가 09-16에 코드 쪽에서 말한 *지속적·사전적* 원칙의 데이터판.
- **[[agents-as-catalyst]]** — 같은 벤더가 "데이터를 열어라"(09-26)와 "흐르는 데이터를 감시하라"(이번)를 따로 말했다. 화자의 비유로는 **혈액**: *"It has to keep moving or the patient dies. But if we can't monitor where it's going we could be hemorrhaging and not even know it."*(10:57~11:04)

## ⚠️ 이 개념이 답하지 않는 것

- **차단** — 처방은 거의 전부 *보는 것*이다. *"monitored and enforced"*(07:29~07:33) 외에 무엇을 언제 막는지 없다.
- **근거 수치** — *"31% of organizations"*(00:24~00:31)의 연구 출처 없음.
- **섀도우 AI를 어떻게 찾는가** — 정의만 있고 탐지 방법은 세 렌즈 일반론뿐.
- **도구·제품** — 이름 0개. 결론은 *"there are tools that can help you"*(11:09~11:10).

## References

- [[tech-bridge-ai-data-exposure-hidden-risk]] (first-seen) · [[jeff-crume]] · [[ibm]]
- 관련: [[lineage-driven-risk-visibility]] · [[lethal-trifecta]] · [[prompt-injection]] · [[agent-governance-layers]] · [[shift-left-security]] · [[continuous-security-validation]] · [[agents-as-catalyst]]

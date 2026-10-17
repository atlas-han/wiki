---
title: Factory (factory.ai)
type: entity
category: org
tags: [coding-agents, software-factory, droid, model-routing, enterprise, agent-platform]
aliases: [Factory, Factory AI, factory.ai]
links:
  - "https://factory.ai"
  - "https://factory.com"
sources: [tech-bridge-factory-software-factory, tech-bridge-factory-bug-report-to-production]
created: 2026-10-02
updated: 2026-10-17
---

# Factory (factory.ai)

**코딩 에이전트 "Droid"와, 이를 개발 생애주기 전체로 넓힌 "소프트웨어 팩토리"를 만드는 회사.** 본 위키에서는 [[tereza-tizkova|Tereza Tížková]]의 발표 [[tech-bridge-factory-software-factory]]로 처음 등장한다.

> ⚠️ **이름.** 자막은 세 트랙 모두 *"a company called factory.com"*(00:31~00:35)으로 들리지만 설명란 링크는 **https://factory.ai** — 이 위키는 설명란을 따른다(링크는 열어 보지 않았다). 일반명사 "factory"와 헷갈리지 않도록 slug는 `factory-ai`. ko는 회사·제품 이름을 **"공장"** 으로 옮긴다(06:11 *"공장 자동 모델들"*, 11:26 *"공장 임무"*).

## 자막에 나온 것 (전부 자사 발표)

| 제품·기능 | 내용 | 자막 |
|---|---|---|
| **Droid** | 자사 코딩 에이전트 — *"migrating uh code bases with Droid with our agent"* | 13:45~13:52 |
| **소프트웨어 팩토리** | 오래 만들어 온 개념, *"finally uh the technology is catching up"* → [[software-factory]] | 00:35~00:43 |
| **automatic model routing** | 난이도 분류 → 임계값 위 최저가 모델, 실패·장애 시 전환. ⚠️ *"for example 25%"* → [[automatic-model-routing]] | 06:09~08:01 |
| **Missions** | 장시간 세션(*"even for weeks"*), 오케스트레이터 → 순차 워커 → 검증자(scrutiny · user testing), 코드 전 validation contract. ⚠️ 고객 미션 16시간·검증 40% | 11:26~14:54 |
| **deferred context engine** | 도구를 짧은 목록으로 두고 호출 시 로드. ⚠️ *"50% of tokens or more"* → [[deferred-tool-context]] | 15:52~16:42 |
| **Agent Readiness** | 코드베이스 위생 점검 프레임워크 → [[agent-readiness]] | 17:41~18:38 |
| **plugins** | *"packaged reusable skills and context"* — 출시를 *"launched"* 로 말함 | 19:19~19:31 |
| **AutoWiki** | 문서 자동 갱신·리뷰 (en-orig *"auto which"*, 챕터·`en`으로 판독) | 19:31~19:41 |

**고객**: *"it's possible to build this in production for enterprises like EY or Adobe"*(00:43~00:47) — 설명란은 *"Adobe, EY 등 글로벌 엔터프라이즈를 위한 소프트웨어 팩토리를 구축해 온"*. 무엇을 구축했는지는 자막에 없다. → [[adobe]]

> ⚠️ **모든 수치는 당사자 진술, 독립 검증 없음.** 회사 규모·설립·투자 정보는 소스에 없다.

## References

- [[tech-bridge-factory-software-factory]] · [[tereza-tizkova]] · [[software-factory]] · [[automatic-model-routing]] · [[deferred-tool-context]] · [[agent-readiness]] · [[adobe]]

## 두 번째 화자 — 3원칙의 교체, 8기둥, 결과 지표 (2026-10-17 · [[tech-bridge-factory-bug-report-to-production]])

[[davis-palmie|Davis Palmie]](member of technical staff, 자막에서 자기소개. 전 Lumetric 공동 창업 — *"acquired by Factory"* 00:09~00:15). 자사 진술(⚠️ 전부 당사자):

| 항목 | en-orig |
|---|---|
| 모델 비종속 | *"At Factory, you're not locked into a single model provider."*(02:58~03:01) |
| 배포 | *"We support everything from fully managed to bring your own machine to entirely air-gapped."*(09:00~09:06) |
| 표면 | *"we have agents available everywhere, from remote machines to the CLI to Slack, any tool your teams use."*(12:46~12:54) |
| agent readiness | 8기둥(13:23~14:18) → [[agent-readiness]] |
| 감사·권한 | *"every action is auditable. It operates under your standards with role-based access control and least privilege, for example."*(14:50~14:57) |
| 지표 | signal to production time · human intervention count · median time to repair · shelf life of code · cost per PR(16:59~17:10) |

⚠️ 3원칙이 Tereza 판본과 다르다([[software-factory]]의 Contradiction 박스). CEO는 *"As our CEO likes to say"*(03:17)로만 나오고 이름은 미발화다. 이번 설명란의 회사 링크는 `https://factory.com` 이다(열어 보지 않음). 위 `factory.ai`(10-02 설명란)와 다르고, Tereza 편 자막도 *"factory.com"* 으로 들렸다. 어느 쪽이 정식 도메인인지는 확인하지 않았다.

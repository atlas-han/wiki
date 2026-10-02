---
title: AI Unified Process — use case 기반 스펙 주도 개발 (AI Unified Process)
type: concept
category: pattern
tags: [spec-driven-development, use-cases, entity-model, requirements-engineering, agent-skills, legacy-modernization, reverse-engineering, enterprise, process]
aliases: [AI Unified Process, AIUP, AI 통합 프로세스, use case 기반 SDD, system use case 스펙]
related: [spec-driven-development, agent-skills, harness-engineering, legacy-code-modernization, risk-proportional-human-review, self-contained-systems, greenfield-vs-brownfield-agent-risk, shift-left-interventions, ai-native-sdlc, architecture-as-remaining-art]
first-seen: tech-bridge-sdd-enterprise-lessons
sources: [tech-bridge-sdd-enterprise-lessons]
created: 2026-10-02
updated: 2026-10-02
---

# AI Unified Process

**스펙을 요구공학자·PO가 쓰는 system use case + entity model로 두고, plan·task 단계 없이 스펙에서 바로 코드·테스트를 생성하며, 그 사이를 조직·스택별 스킬과 MCP·가이드라인이 채우는 엔터프라이즈용 [[spec-driven-development|SDD]] 프로세스.** 레거시는 코드에서 같은 스펙을 역설계해 다시 생성한다. [[simon-martinelli|Simon Martinelli]]가 만들었고 [[tech-bridge-sdd-enterprise-lessons]]에서 소개했다.

> *"I skip the plan task phase I just use SIS[=system] use cases and entity model and generate code directly"* (06:01~06:07)

> ⚠️ **이름.** 화자는 *"my process I created to say a unified process"*(03:02~03:05), *"there's a web website called AI um unified process"*(03:42~03:46)라 한다. 약어 "AIUP"는 발화되지 않는다(이 페이지의 alias일 뿐). *"UML and OOP"*(04:53, ko·`en` "RUP")로 보아 RUP(Rational Unified Process)를 의식한 이름일 수 있으나 **미확정**.

## 왜 — "developer centric" 도구에 대한 대안

화자는 SDD를 *flavor*로 나눈다 — 도구([[kiro|Amazon Kiro]] · [[github-spec-kit|GitHub Spec Kit]] · BMAD Method · Tessl)와 프로세스. 도구는 *"too developer centric"*(03:20~03:24)이고, 이 프로세스는 *"the whole software development life cycle especially for enterprises where you not are a soloreneur you're someone in a larger team with different roles"*(03:26~03:40)를 다룬다.

## 구성

| 요소 | 내용 | en-orig |
|---|---|---|
| **스펙 ① system use case** | 행위. AI와 **모든 이해관계자**가 이해할 수 있는 형식. precondition · postcondition · main success scenario · alternative flows | 04:29~04:48, 11:52~12:09 |
| **스펙 ② entity model** | *"more like a domain model"* — 데이터. brownfield에선 DB 모델에서 유도 | 05:21~05:35, 14:17~14:21 |
| **보조 스펙** | UI는 Figma 디자인(MCP 서버로 연결), API는 API 스펙 | 06:07~06:29 |
| **definition of done** | 엔지니어 + AI + 요구공학자가 스펙이 끝났는지 함께 정한다 | 08:37~08:47 |
| **에이전트 + 하네스** | 스킬 · MCP · 가이드라인 · 가드레일. ⭐ *"That is probably the most important thing of the whole process. So that means the skills must match the outcome."* | 09:03~09:17 |
| **code · test** | 순서는 산출물에 따라 — UI가 있으면 TDD 어려움, API면 TDD | 06:35~07:00 |
| **review** | 양은 위험 관리로 정한다 | 07:03~07:59 |

**스킬은 두 층** — 스펙 작성용 스킬 + 스택별 구현 스킬. 프로세스는 한 스택분만 제공하고, 나머지 조합은 *"probably a thing that the company has to do"*(16:41~16:58). 고객 6곳의 스킬이 모두 다르다(React · Vaadin · Angular · Quarkus · 사내 프레임워크, 09:23~09:48). → [[agent-skills]]

### 왜 user story가 아니라 use case인가

- use case는 *"very well defined and even AI knows how to write use cases because it's around for a very long time"*(11:52~11:56).
- **user story ≈ use case의 한 flow** — *"use cases are better than user stories because they are simply bigger"*(12:29~12:31).
- postcondition = acceptance criteria, 테스트로 검증 가능(15:10~15:17).
- 화자 배경: Jacobson이 *"back in 1988"*(⚠️ 화자 진술) 만든 기법, 화자가 2000년대 초 스위스 철도에서 *"communication specification between stakeholders and developers"*(05:10~05:14)로 썼다.

> ⚠️ **"SysML 유스케이스" 아님.** 영상 설명란·ko·`en` 트랙은 "SysML"이라 하지만 en-orig는 *"system use cases"*(04:39~04:48)다. 이 위키는 system use case로 적는다.

## 두 흐름

**greenfield**: 요구 카탈로그/PRD → use case 다이어그램(모듈 분할의 단서) → use case 문서 + entity model → 리뷰(DoD) → *implement*. 요구공학자·PO는 AI로 **중복·누락을 검증**(28:22~28:31).

**brownfield(현대화)**: 코드 · 테스트 · 문서에서 use case + entity model을 **역설계** → 업무 담당자 검토 → 새 코드 생성(10:09~10:32). 직역(COBOL→Java)은 *"lift and shift"* 이고 *"modernization is rethinking how people are working with the software"*(10:52~10:59). 스펙을 거치기 때문에 현대화 중에도 **새 기능**을 넣을 수 있다(11:18~11:41). → [[legacy-code-modernization]]

**변경**: use case를 고치고 다시 *implement* — 코드를 버리고 재생성하지 않는 이유는 git history와 리뷰(30:01~30:06). 사람은 아직 코드를 읽는다.

## 주장 — waterfall이 아니다

> *"a lot of people say spectrum[=spec-driven] development is waterfall and that's simply not true (…) we don't do big upfront design. We just go use case by use case."* (28:36~28:51)

use case 하나가 작업 단위이고 칸반 카드다(21:33~21:38). 그래서 팀 운영이 바뀐다 — 스펙엔 2주가 걸려도 구현은 몇 분이라 스프린트가 맞지 않고(20:57~21:13), **self-contained system당 개발자 1~2명**(21:15~21:30), PR 없이 trunk-based + peer review(24:38~25:04). → [[self-contained-systems]]

## 결과로 생기는 것 — requirements engineering으로 shift left

> *"So everything shifts left to requirements engineering in my opinion"* (26:43~26:45) · *"Now you have two weeks and then five minutes and two weeks"* (26:59~27:00)

스위스 의회 PoC에서 코드 쪽은 화자 혼자, 스펙을 쓰는 요구공학자/PO 두 명이 *"much more work to do than I have"*(26:26~26:29). markdown 스펙을 고치면 자동 생성되는 파이프라인을 만드는 중(26:31~26:37). [[ai-native-sdlc]]가 spec 앞에 [[intent-md|intent.md]]를 붙여 **에이전트가 사람을 인터뷰**하게 했다면, 이 프로세스는 그 앞단을 **요구공학이라는 기존 직무**에 맡긴다.

## 위키에서의 좌표

| | [[github-spec-kit|Spec Kit]] (08-29) | SDD 풀코스 (09-27) | AI Unified Process (10-02) |
|---|---|---|---|
| 스펙 작성자 | 개발자 | 개발자 + 에이전트 인터뷰 | **요구공학자 · PO · BA** |
| 스펙 형식 | user story | plan · requirements · validation | **system use case + entity model** |
| plan/tasks | 있음 | plan 있음 | **없음 — 스킬이 대신** |
| 스펙 수정 | 다음 기능의 새 spec | 에이전트를 통해(직접 편집은 drift) | **직접 고치고 재-implement** |
| 레거시 | — | 헌법 역설계 | **use case·entity model 역설계** |

> ⚠️ **Contradiction:** plan/tasks를 둘 것인가, 스펙을 직접 고칠 것인가 — [[spec-driven-development]] · [[tech-bridge-sdd-full-course]]와 갈린다. 자세한 것은 [[tech-bridge-sdd-enterprise-lessons]]의 "갈리는 것".

## 표시해 둔 것

> ⚠️ **저자의 발표, 측정 없음.** *"near deterministic"*(24:06~24:10), 데모 1분 30초, 팀 축소 — 조건·측정 방법이 없다. 스킬이 약한 팀에서 plan/tasks 없이 같은 결과가 나오는지는 말하지 않는다. 프로세스 웹사이트의 스킬 목록은 자막에서 *"we don't have time to look at that"*(16:35~16:37)으로 지나갔고, 이 위키는 사이트를 보지 않았다.

## References

- [[tech-bridge-sdd-enterprise-lessons]] · [[simon-martinelli]]
- 관련: [[spec-driven-development]] · [[agent-skills]] · [[harness-engineering]] · [[legacy-code-modernization]] · [[self-contained-systems]] · [[risk-proportional-human-review]] · [[ai-native-sdlc]] · [[shift-left-interventions]]

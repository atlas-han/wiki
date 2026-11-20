---
title: Microsoft
type: entity
category: org
tags: [hyperscaler, copilot, enterprise-ai, openai-partner, data-center]
links:
  - https://www.microsoft.com/
sources: [tech-bridge-nadella-copilot-autopilot, tech-bridge-factory-bug-report-to-production, tech-bridge-ai-labs-token-economizer, tech-bridge-nadella-pragmatic-engineer-after-code-is-cheap]
created: 2026-09-29
updated: 2026-11-20
---

# Microsoft

하이퍼스케일러이자 [[microsoft-copilot|Copilot]] 제품군을 만드는 회사, [[openai|OpenAI]]의 오랜 파트너. 이 위키에서는 오랫동안 **지나가는 이름**(Glasswing 파트너, Microsoft Foundry 플랫폼, [[bill-gates|Bill Gates]]의 이력, OpenAI–MS AGI 합의)이었고 **2026-09-29에 CEO [[satya-nadella|Satya Nadella]]의 1인칭 대담**([[tech-bridge-nadella-copilot-autopilot]])이 들어오며 페이지를 만들었다.

> ⚠️ 아래 "자기 서술" 절은 전부 CEO의 진술이다. 수치(Quincy 세수 약 12배, 약 1,000명 고용)는 출처가 없다.

## 자기 서술 (2026-09-29 · [[tech-bridge-nadella-copilot-autopilot]])

| 층 | 내용 |
|---|---|
| **제품** | 새 [[microsoft-copilot\|Copilot]] — chat · co-work · code · **Autopilot**(장시간 비즈니스 프로세스 에이전트). 앞서 **Copilot tasks**를 OpenClaw와 비슷한 시기에 냈다(02:44~02:48) |
| **거버넌스** | [[agent-365\|Agent 365]] — 관찰·거버넌스·정책·보안·FinOps, Autopilot의 **호스팅 환경**과 감사 가능성(04:41~04:50, 12:51~13:00) |
| **모델** | 사용자 대신 **learned router**가 모델을 고른다. 자체 **MAI 모델** + 하네스가 다른 모델(OpenAI · Anthropic · Grok) 호출. Copilot은 대부분 미국 closed 모델, **Foundry**에 오픈 웨이트, 고객 BYO 모델(08:15~11:10) |
| **가격** | 좌석(= 사용 권리) + 사용량 과금 — *"software for the first time has marginal cost"* → [[software-marginal-cost]] |
| **안전** | OpenAI와의 **joint safety board**, 양쪽의 *"embedded evaluators"*(15:48~16:05) → [[embedded-external-evaluators]] |
| **인프라** | 워싱턴주 **Quincy** 20년 — 지역 사회의 *"permission"*, NDA 폐지(진행자 서술) → [[data-center-local-backlash]]. AI 컴퓨트 배분이 *"first showed up in Redmond"*, *"a more gradual ramp"*(22:24~22:38) |

## 이 위키의 다른 자리에서

- [[project-glasswing]] · [[anthropic]] — Glasswing 파트너 목록에 이름만.
- [[tech-bridge-andrew-ng-ai-opportunity]] — OpenAI–Microsoft AGI 관련 합의(이후 재협상으로 소멸)가 **AGI 조기 선언 유인**이었다는 [[andrew-ng]]의 언급.
- [[dynamic-workflows]] — Claude가 제공되는 플랫폼 중 **Microsoft Foundry**.
- [[tech-bridge-spec-driven-development]] — 발표자가 Microsoft 365 MVP, GitHub Copilot 기반 SDD.
- [[bill-gates]] — 공동창업자.

## ⚠️ 유보

- **OpenAI와의 관계** — Nadella는 *"API는 OpenAI가 지배"* 와 *"joint safety board"* 를 말하지만, 진행자가 OpenAI·Anthropic의 엔터프라이즈 진출을 묻자 **경쟁사에 대해서는 말하지 않는다**(12:30~13:16). 파트너이자 경쟁자라는 위치의 구체는 소스에 없다.
- **Mustafa Suleyman** — 진행자가 MS에서 안전·AI 개발에 관한 글과 *"code of conduct"* 를 낸 인물로 언급(23:53~24:00). 직함·내용 없음.

## References

- [[tech-bridge-nadella-copilot-autopilot]] — 첫 1인칭 소스
- [[satya-nadella]] · [[microsoft-copilot]] · [[agent-365]] · [[openai]]

## Claude Code 라이선스 회수 헤드라인 (2026-10-17 · [[tech-bridge-factory-bug-report-to-production]])

[[davis-palmie|Davis Palmie]]([[factory-ai|Factory]])가 비용 폭증의 예로 든다: *"or Microsoft clawing back cloud code[=Claude Code] licenses to try and cut down on spend."*(02:50~02:56) 이 위키에 처음 나오는 일화다. 자사 Copilot이 아니라 [[claude-code|Claude Code]] 라이선스를 회수했다는 주장이다. ⚠️ 출처 미제시(*"headlines"*), 시점·규모 미발화. *"cloud code"* 는 문맥 판독이다.

## Token Economizer — 코딩 에이전트용 토큰 절감 플러그인 (2026-11-04 · [[tech-bridge-ai-labs-token-economizer]])

[[ai-labs|AI Labs]](설명란 근거)가 Microsoft의 플러그인 [[token-economizer|Token Economizer]]를 소개한다. 자사 Copilot뿐 아니라 경쟁 제품도 시험 대상이다: *"They did that on five different setups across Claude Code, Codex, and GitHub Copilot."*(01:09~01:13) 발표자가 전달한 시험은 277개 버그 · 6개 프로젝트이고, 숫자가 발화된 구성은 Claude Code 둘(Sonnet 5 −23.6% · Opus 4.8 −30.9%)뿐이다. 보안 판단은 사용자에게 넘긴다: *"That's why Microsoft leaves the choice to you."*(06:05~06:07) ⚠️ 모두 발표자 전달이고 저장소는 열어 보지 않았다.

## 2026-11-20 — CEO가 가리킨 사내 사례들과 자발적 퇴직 제안 ([[tech-bridge-nadella-pragmatic-engineer-after-code-is-cheap]])

[[satya-nadella|Nadella]]의 The Pragmatic Engineer 인터뷰를 공식 글과 맞춰 본 한국어 해설에서(⚠️ 공식 글 여덟 편 모두 위키 미열람, 수치는 해설의 전달).

| 자리 | 내용 |
|---|---|
| **Copilot Cowork 팀** | *"엔지니어 아홉 명이 하루에 풀 리퀘스트 1,211개를 머지했다고 요."*(04:12~04:16) 코드는 대부분 에이전트가, 판단은 엔지니어가. Python → Rust 이전의 **첫 시도는 되돌렸다**(Bas Brekelmans의 글) |
| **[[github-copilot\|GitHub Copilot]] 런타임** | TypeScript → Rust, 80만 줄 넘게, 주로 개발자 한 명, 몇 달(Stephen Toub의 글) |
| **Azure 네트워크 팀** | 전 세계 광케이블 망 운영 — Nadella가 가장 아낀다는 사례. *"일을 직접 하던 팀이 이제 일을 하는 공장을 지었습니다."*(05:45~05:47) ⚠️ 무엇을 지었는지는 캡션에 없다 |
| **Windows · MSRC** | *"마이크로소프트 보안 팀은 올해 패치 규모가 당분간 계속 커질거라고 공지했습니다."*(06:01~06:05) AI 모델이 취약점을 찾는 속도를 끌어올려서. 브라운필드의 병목은 빌드와 CI/CD |
| **GitHub** | 9월 PR의 40% 넘게가 에이전트 초안에서 시작(3월 17%, Octoverse) — 바닥을 다시 깐다 |
| **PRAISE 프리셉터십** | Mark Russinovich · Scott Hanselman이 10월 소개, 카네기 멜론과 운영 — 신입 엔지니어를 선배 프리셉터와 짝짓는다 |
| **인사** | *"마이크로소프트는 10월 26일 자발적 퇴직 제안을 발표했습니다."*(08:26~08:28) 대상은 캐나다 · 인도 · 영국 · 미국의 참여 팀, 인원수 · AI 언급 없음. *"4월에 자발적 은퇴 프로그램에 이어 올해 두 번째입니다."*(08:39~08:40) |

위 10-17 절의 *Claude Code 라이선스 회수 헤드라인* 과 나란히 읽을 만하다 — 이 편에서 CEO는 코딩 도구의 무게중심을 옮긴 것이 [[claude-code|Claude Code]]였다고 인정하지만(제목 · 설명란), 라이선스 회수 일화는 나오지 않는다. 직원 수는 *20만 명이 넘는* 으로 언급된다(14:44, 해설).

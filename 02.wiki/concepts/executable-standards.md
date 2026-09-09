---
title: 실행 가능한 표준 (Executable Standards)
type: concept
category: practice
tags: [guardrails, governance, standards, automation, tribal-knowledge]
aliases: [실행 가능한 가드레일, 문서로서의 표준, executable policy]
related: [decision-quality, behavior-validated-trust, agent-governance-layers, llm-coding-guidelines, trusted-throughput, intent-md, scheduled-agent-automations]
first-seen: tech-bridge-ai-era-code-quality
sources: [tech-bridge-ai-era-code-quality]
created: 2026-09-09
updated: 2026-09-09
---

# 실행 가능한 표준

**표준이 문서로 존재하면 낡고 무시된다 — 개발 프로세스 자체에 심어야 강제된다**는 주장.

> 과거에 표준은 종종 **문서의 형태**였습니다. 명명 규칙을 설명하는 위키 페이지, 보안 체크리스트, **모두가 읽겠다고 약속한 코딩 표준 문서.** 하지만 우리 모두 알다시피 **이러한 문서 대부분은 거의 즉시 낡아버렸습니다.** — [[tech-bridge-ai-era-code-quality]]

> **AI 지원 워크플로에서 표준은 그냥 문서로 존재할 수 없습니다. 개발 프로세스 그 자체 안에 존재해야 합니다.**

## 무엇을 심는가

- 보안 요구사항은 **자동으로 강제**
- 아키텍처 가드레일은 **템플릿과 툴링에 인코딩**
- 테스팅 기대치는 **모든 PR의 일부**
- 정적 분석은 **지속적으로 실행**
- **정책은 실행 가능해야 하며 단지 열망에 그쳐서는 안 된다**

## 목표는 강제가 아니라 경로 설계

> 목표는 **개발자에게 표준을 따르라고 상기시키는 것이 아니라, 올바른 길이 그들이 따르기 가장 쉬운 길이 되게 만드는 것입니다.**

그리고 이것이 AI에게 왜 특히 중요한지가 명시된다:

> 기대치가 워크플로에 직접 인코딩되면 **AI는 훨씬 더 효과적이 됩니다. 암묵적인 부족 지식(tribal knowledge)에 의존하는 대신 잘 정의된 경계 안에서 작동하기 때문입니다.**

## 같은 형태의 논증이 세 자리에서 나온다

이 위키가 놓는 연결이다:

| 소스 | 어디에 규칙을 두는가 |
|---|---|
| [[tech-bridge-ai-era-code-quality]] | 문서가 아니라 **개발 프로세스**에 |
| [[tech-bridge-knowledge-work-agent-infrastructure]] | 프롬프트가 아니라 **에이전트 바깥**에 ([[agent-governance-layers]]) |
| [[tech-bridge-cursor-legacy-refactoring]] | 개인 습관이 아니라 **Confluence 템플릿·플러그인·automation**에 |

세 소스 모두 **"사람이 기억하기를 기대하는 규칙은 실패한다"** 는 같은 말을 서로 다른 층위에서 한다.

## [[llm-coding-guidelines]]에 놓이는 반론

이 위키의 [[llm-coding-guidelines]]는 *에이전트에게 줄 가이드라인을 문서로 잘 쓰는 법* 을 모아왔다. 이 소스는 **문서로 된 표준은 즉시 낡는다**고 정면으로 말한다.

> ⚠️ 다만 두 주장이 완전히 배타적이지는 않다 — `AGENTS.md`류는 *문서이면서 도구가 읽는 것* 이라 이 소스의 분류에서 어느 쪽인지 애매하다. **소스가 이 경계를 다루지 않는다.**

## 지속적 실천으로서의 품질

같은 논지의 시간 축 버전이 이어진다 — 품질은 릴리스 직전의 **체크포인트**가 아니라 **지속적 실천**이어야 한다.

> 모든 커밋이 검증을 트리거하고, 모든 PR이 자동 테스트를 실행하고, 모든 배포가 **관측 가능한 신호**를 만들고, 모든 프로덕션 시스템이 **다음 반복을 개선하는 피드백**을 생성해야 합니다.

> 품질은 소프트웨어 전달의 마지막 단계가 아니라 **계획 → 배포 → 운영 전체에 짜여 들어갑니다.**

**거버넌스가 사후 고려가 아니라 워크플로의 일부가 된다**는 진술은 [[trusted-throughput]]이 조직 운영에서 말한 것과 같다 — 가드레일은 속도를 늦추는 것이 아니라 **AI 도입을 안전하게 확장하게 하는 것**이다.

## ⚠️ 미해결

- **가드레일의 비용 미논의** — 모든 커밋 검증·상시 정적 분석의 지연과 비용이 다뤄지지 않는다.
- **표준이 틀렸을 때의 갱신 경로가 없다** — 인코딩된 규칙은 문서보다 고치기 어려울 수 있는데 그 트레이드오프가 언급되지 않는다.

## References

- [[tech-bridge-ai-era-code-quality]] · [[ibm]] · [[agent-governance-layers]]

---
title: Sentry
type: entity
category: org
tags: [observability, error-monitoring, debugging-agent, django, openapi, linters]
aliases: [Sentry, sentry.io, 센트리, Century (ASR)]
links:
  - "https://sentry.io"
  - "https://sentry.io/product/seer/"
  - "https://x.com/sentry"
sources: [tech-bridge-sentry-stop-prompting-codify-linters]
created: 2026-10-16
updated: 2026-10-16
---

# Sentry

에러·텔레메트리 모니터링 회사다. 이 위키에서는 지금까지 MCP 커넥터·교차 확인 대상(Datadog과 나란히)으로만 지나가듯 나왔다. [[tech-bridge-sentry-stop-prompting-codify-linters]]에서 처음으로 **사내 코드베이스와 사내 에이전트의 사례**가 소스의 주제가 됐다. 화자는 [[greg-pstrucha|Greg Pstrucha]]다(이름은 설명란에만). 링크는 설명란에서 가져왔고 열어 보지 않았다.

## 코드베이스 — 레거시와 OpenAPI drift

- *"Sentry is a pretty old code base. We are on Django, we are on DRF. We don't have strict typing everywhere. This is a very common case for any mature code base"*(06:04~06:12)
- 문제: *"there was a lot of drift of what the open API schema for Sentry said it's going to do and what it did."*(06:24~06:28) lint 규칙 세 개(06:33~07:03)로 대응했다. endpoint는 response type을 반환하고 그 안에 *"any types"* 가 없어야 한다(⚠️ `Any` 금지로 읽힘). endpoint에는 *"extend schema decorator"* 가 붙어야 한다(⚠️ 라이브러리 미발화). 생성 타입은 OpenAPI 선언과 일치해야 한다. 결과는 *"now APIs are a little bit more in sync."*(07:04~07:07)
- 동기는 에이전트다. *"we still want to improve the state of the world for for the agents."*(06:16~06:19) → [[agent-readiness]] · [[legacy-code-modernization]]

## 디버깅 에이전트 ("Sentry agent")

- *"Sentry agent is a debugging agent, and it has to talk to Sentry a lot. It uses Sentry telemetry to debug and RCA issues"*(07:15~07:27). 오래된 endpoint의 복잡함은 스키마 대신 스킬로 안내한다(07:42~07:48).
- 환각 예제가 섞인 스킬 때문에 정확도가 크게 떨어졌다. 그래서 스킬 속 코드 블록을 lint했다. → [[skill-linting]]
- ⚠️ **Seer와 동일시하지 않는다.** 설명란에 *Sentry Seer* 링크가 있지만 발화에 "Seer"는 없다. 제품명·기능·사용자는 미발화다.

## 이 위키의 다른 자리에서

- MCP 커넥터 목록([[model-context-protocol]]), Datadog과 함께 쓰는 교차 확인([[scheduled-agent-automations]]), GrokBot 루틴이 구독하는 알림([[scheduled-agent-automations]] · [[company-brain]]), Composio 데모의 *"Century[=Sentry]"*([[deferred-tool-context]])에서 나온다. 모두 도구로서 지나가는 언급이다.

## ⚠️ 유보

- 회사 개요·규모는 발화되지 않는다. 화자는 Sentry 제품을 홍보하지 않는다. 사례는 사내 코드베이스이고 측정이 없다.

## References

- [[tech-bridge-sentry-stop-prompting-codify-linters]] · [[greg-pstrucha]]

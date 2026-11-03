---
title: Better Stack
type: entity
category: org
tags: [observability, opentelemetry, logging, youtube, content, devtools]
aliases: [BetterStack, 베터 스택]
links:
  - https://betterstack.com
sources: [tech-bridge-better-stack-claude-code-agent-summary-cost]
created: 2026-11-03
updated: 2026-11-03
---

# Better Stack

관측(observability) 플랫폼 회사이자, 이 위키에서는 [[tech-bridge|Tech Bridge]]가 자막을 입혀 재배포한 [[tech-bridge-better-stack-claude-code-agent-summary-cost]]의 **원 제작자**(설명란 근거)다.

## 위키에서 알려진 사실

- **설명란 귀속**: *"Better Stack이 두 차례 측정한 결과와 앤스로픽이 공개한 수치를 비교합니다."* info.json `tags`에는 없다.
- **발화 속 역할 — 측정 도구**: 화자가 [[claude-code|Claude Code]]의 OpenTelemetry export를 이곳으로 보내 요청을 용도별(query source)로 묶었다 — *"I turned on Claude Code's open telemetry export and sent it to Better Stack where every request comes through tagged with a query source saying what it was for."*(00:36~00:43) 그 결과가 agent summary 12% · 8%다 → [[hidden-harness-calls]].
- 자사 제품을 측정 수단으로 쓰는 구성이라 **Better Stack 자체 채널의 영상으로 추정**한다.

## 미해결 사항

- ⚠️ **발표자 개인 이름이 없다.** 1인칭 단수 *"I"* 로만 말하고, 화자는 터미널 Claude Code 대신 T3 Code를 쓴다고 밝힌다(04:41~04:44).
- 원본 영상 링크 · 채널명이 설명란에 없다. 회사 정보(규모 · 소재지 · 제품 범위)는 이 위키의 소스로 확인하지 않았다 — 위 링크는 일반 도메인이다.
- 측정 영상이 자사 제품 노출을 겸한다는 점(⚠️ vendor 맥락)은 수치를 읽을 때 염두에 둘 것. 다만 측정 대상(Claude Code)은 Better Stack 제품이 아니다.

## References

- [[tech-bridge-better-stack-claude-code-agent-summary-cost]]

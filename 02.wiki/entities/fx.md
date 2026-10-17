---
title: fx (Vercel Labs 코딩 CLI)
type: entity
category: tool
tags: [coding-cli, coding-agent, vercel, terminal, harness, embeddable-harness]
aliases: [fx, fx0]
links:
  - "https://fx.sh/"
  - "https://fx.sh/docs"
sources: [tech-bridge-vercel-rauch-agentic-workflow]
created: 2026-10-16
updated: 2026-10-16
---

# fx

**Vercel Labs의 코딩 CLI.** [[guillermo-rauch|Guillermo Rauch]]의 소개: *"Today I'm using effects[=fx], which is the coding CLI of Versel[=Vercel] Labs."*(00:15~00:19, [[tech-bridge-vercel-rauch-agentic-workflow]]). ⚠️ 이름 판독 — en-orig는 전 구간 *"effects"*, ko는 "효과"로 받았다. 설명란 링크 `https://fx.sh/` 로 **fx** 판독(링크는 열어 보지 않았다).

## 설계 (화자 진술)

- **셸처럼**: *"it almost feels like a shell. So, when I open a new tab (…) or I open a split, like it boots into ZSH"*(00:23~00:34). *"can this boot as fast as a shell itself?"*(00:37~00:40)
- **작다**: *"It's actually 6 megabytes. It's 11 megabytes on disk."*(00:51~00:53) — 발화 중 정정(다운로드 6MB · 디스크 11MB로 읽음).
- **임베드 가능**: *"One of the ideas of effects is that you should be able to embed it"*(04:08~04:13). ⚠️ 임베드용 이름으로 보이는 *"live effects"*(04:13)와 *"the create effects agent API"*(05:21)는 철자·식별자 미확정.

## fx0 — 임베드 데모

v0 같은 앱을 fx 위에 다시 지은 예제(*"we're going to open source"* 04:41 — 공개 의사 표명). 세 모드: ① 모델이 HTML 출력 ② Vercel Sandbox에서 *"a full Next.js application"*(06:05~06:08) ③ *"it creates an Eve agent when you give it a prompt"*(06:12~06:18) → [[eve-framework]]. 화자 추정 *"100 lines of code on top of the create effects agent API"*(05:18~05:23) — [[v0]] 때 하네스에 들었다는 *"90% of the engineering time"* 과 대비. 구조는 *brain and hands* — 하네스를 돌리고 샌드박스를 도구로 준다 → [[brain-hands-decoupling]].

## 사용법 (Rauch 개인)

- 리서치 폴더 + `agents.md`: 질문하면 지시를 읽고 결과를 폴더에 쌓는 관례(01:44~01:59) → [[file-system-agent]] · [[agentic-inquiry]]
- alias `r`(리서치) · `p`(새 프로젝트 — Shopify Tobi의 `try` 와 비슷, 02:36~02:56)
- 보안 조사: *"Find me a bunch of projects that have already done this"*(10:29~10:33)

⚠️ 전부 자사 CEO의 진술. 크기·속도 외 측정 없음.

## References

- [[tech-bridge-vercel-rauch-agentic-workflow]] · [[vercel]] · [[guillermo-rauch]] · [[v0]] · [[eve-framework]]
- 관련: [[claude-code]](같은 범주의 터미널 코딩 에이전트) · [[obsidian-cli-workflow]](terminal-first 습관)

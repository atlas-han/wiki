---
title: Next.js
type: entity
category: tool
tags: [web-framework, vercel, file-system-routing, convention-over-configuration]
links:
  - https://nextjs.org
sources: [tech-bridge-vercel-eve-filesystem-agent]
created: 2026-09-19
updated: 2026-09-19
---

# Next.js

[[vercel|Vercel]]이 만든 웹 프레임워크. 본 위키에는 **[[eve-framework|Eve]]의 설계 원형**으로 들어왔다 — 그 자체로 다뤄진 것이 아니라, 에이전트 프레임워크가 무엇을 베끼려 하는지의 근거로.

> 이 프레임워크는 **파일 시스템, 즉 프레임워크 정의 인프라(framework defined infrastructure)** 라는 개념을 창안했습니다. **파일 위치를 걱정할 필요 없이 올바른 규칙(convention)에 따라 파일을 작성하기만 하면 프레임워크가 자동으로 위치를 지정합니다.** **페이지는 CDN으로, 서버리스 함수는 [거기로], 캐싱은 중간 위치로** 이동합니다. (11:53~12:11)

핵심은 **선언이 곧 배치**라는 것이다 — 개발자는 컨벤션대로 파일을 두고, 인프라 배치는 프레임워크가 결정한다. [[andrew-qu|Andrew Qu]]는 이것을 에이전트로 옮겨 *"스킬 폴더, 도구 폴더, 채널 폴더만 만들면 프레임워크가 에이전트를 만들어 내야 한다"* 고 주장한다. → [[framework-defined-agent-infrastructure]]

⚠️ *"창안했다(invented)"* 는 **화자의 주장**이다. 파일 시스템 라우팅의 계보를 이 위키가 따로 확인하지 않았다.

## References

- [[tech-bridge-vercel-eve-filesystem-agent]] · [[vercel]] · [[eve-framework]] · [[framework-defined-agent-infrastructure]]

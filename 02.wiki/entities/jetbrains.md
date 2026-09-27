---
title: JetBrains
type: entity
category: org
tags: [ide, developer-tools, acp, webstorm, education]
links:
  - https://www.jetbrains.com/
sources: [tech-bridge-sdd-full-course, tech-bridge-acp-universal-remote]
created: 2026-09-27
updated: 2026-09-27
---

# JetBrains

IDE 제작사(IntelliJ 계열, WebStorm 등). 이 위키에는 [[tech-bridge-acp-universal-remote]]에서 **[[agent-client-protocol|ACP]]의 공동 제안자**(Zed와 함께)로 이름만 먼저 나왔고, [[tech-bridge-sdd-full-course]]에서 **스펙 주도 개발 강좌의 협업사**로 처음 본격 등장한다.

## 위키에서 알려진 사실

- **ACP 공동 제안** — [[zed|Zed]] 쪽과 JetBrains 쪽이 팀을 이뤄 *"에디터에 고품질 클라이언트 구현을 하나만 작성해 어떤 하네스든 제어"* 하는 표준을 냈다([[tech-bridge-acp-universal-remote]]).
- **SDD 강좌** — *"Welcome to this course on spec-driven development, built in partnership with JetBrains"*(00:00~00:03). 강사는 자막상 *"developer advocate at JetBrains"*(00:27~00:29) — 이름 표기 미확정, [[paul-everitt]]. 기여자로 JetBrains의 Konstantin Chayka(en-orig; en·ko는 Chicherin/치체린)와 Zina Smirnova가 불린다(04:06~04:12).
- **WebStorm + [[claude-code|Claude Code]]** 가 강좌의 시연 환경이다(13:28~13:36). 강좌는 *"Spec-driven development is a best practice that isn't tied to any specific IDE or coding agent"*(13:07~13:15)라고 먼저 말한다.
- **JetBrains IDE의 ACP registry 연동** — AI 채팅 창에서 ACP registry로 가서 호환 에이전트 목록을 보고 **OpenCode**를 설치하면, 필요 시 OpenCode 자체 설치와 IDE 통합까지 자동화된다(58:35~59:09). *"your IDE now has native integration with a new agent"*(59:06~59:09).

> ⚠️ **당사자 콘텐츠.** SDD 강좌는 JetBrains 협업 강좌이고 JetBrains IDE로 시연한다. ACP registry의 범위·보안 모델은 강좌가 말하지 않는다 — [[agent-client-protocol]]의 "보안 모델이 없다" 표시가 그대로 유효하다.

## References

- [[tech-bridge-sdd-full-course]] · [[tech-bridge-acp-universal-remote]]
- [[agent-client-protocol]] · [[zed]] · [[paul-everitt]] · [[spec-driven-development]]

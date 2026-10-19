---
title: "Gabe Cemaj"
type: entity
category: person
tags: [anthropic, managed-agents, agent-infrastructure]
aliases: [Gabe, Gabe Cemaj, Gabe Semach, gcemaj]
links:
  - "https://github.com/gcemaj"
sources: [anthropic-managed-agents, tech-bridge-claude-managed-agents-workshop-1, tech-bridge-claude-managed-agents-workshop-2]
created: 2026-10-19
updated: 2026-10-19
---

# Gabe Cemaj

[[anthropic|Anthropic]]의 member of technical staff이고 [[priyanka-phatak|Priyanka Phatak]] 팀에서 [[managed-agents|Claude Managed Agents]]를 만든다. 이 위키에는 엔지니어링 글 [[anthropic-managed-agents]]의 공저자(Lance Martin, Michael Cohen과 함께)로 먼저 올라왔지만 페이지는 없었다. [[ai-engineer|AI Engineer]] 워크숍 *Claude Managed Agents*에서 1부([[tech-bridge-claude-managed-agents-workshop-1]])는 자기소개만 하고, 2부([[tech-bridge-claude-managed-agents-workshop-2]])의 핸즈온과 Q&A 대부분을 맡았다.

> ⚠️ **이름 표기.** 1부 자기소개의 en-orig는 *"Gabe Semach"*, ko는 *"세마크"*다(ASR). 2부 자막에서는 *"Gabe"*만 발화된다. 철자 *Cemaj*는 2부 설명란(*"Anthropic의 Priyanka Phatak과 Gabe Cemaj"*), 두 편 설명란의 GitHub 링크 `github.com/gcemaj`, [[anthropic-managed-agents]]의 저자 표기와 일치한다. 같은 사람이라는 근거는 이름·소속·링크의 일치다.

## 위키에서 알려진 사실

- 자기소개(1부): *"My name's Gabe Semach[=Cemaj]. I'm a member of the technical staff uh building Claude managed agents in Priyanka's team. I've been at Anthropic a little bit over a year and I've been mostly working on this my entire time."*(00:32~00:41)
- 엔지니어링 글이 정리한 설계(session/harness/sandbox, brain–hands 분리)의 공저자다. → [[brain-hands-decoupling]]
- **2부 — 세션 저장 설계**: *"we basically applied the same principle of building and virtualizing interfaces all the way down uh not only across service boundaries, but also at the event layer."*(00:40~00:49)
- **2부 — research desk 핸즈온**: Claude Code 워크숍 스킬(`workshop start`/`workshop next`, 6막)로 진행한다. 이벤트 스트림 채팅 UI → SEC EDGAR 스킬·하위 에이전트(자기 참조)·맞춤 도구 dispatch analysis·공유 메모리 스토어 → Outcome으로 Nvidia 분기 공시 분석(사전 실행분) → 스킬 갱신. *"I don't think anybody's writing code by hand, so I'm not going to do that either."*(06:06~06:10)
- **2부 Q&A의 주 답변자**: 실행 위치(1P · Claude Platform on AWS · 자체 호스팅 샌드박스 Vercel/Modal/Daytona/GCP/AWS), Vault의 placeholder·egress 바꿔치기([[credential-injection-outside-sandbox]]), 예산 상한은 *"not something we offer today"*, rewind/roll forward 없음, dreaming은 *"constrained to memory stores"*([[agent-dreaming]]), sub-outcome 없음, 비공개 데이터 세 경로(MCP + vault · MCP tunnels · 자체 호스팅 샌드박스), environment 패키지는 생성 시 캐시.

## ⚠️ 유보

- 당사자(제품 팀) 진술이다. 2부 Agent SDK 질문(26:15~26:58)의 두 답변자는 자막만으로 가르지 못한다.

## References

- [[anthropic-managed-agents]] (공저)
- [[tech-bridge-claude-managed-agents-workshop-1]] · [[tech-bridge-claude-managed-agents-workshop-2]]
- [[managed-agents]] · 같은 팀: [[priyanka-phatak]]
- 링크: <https://github.com/gcemaj> (설명란, ⚠️ 열어 보지 않았다)

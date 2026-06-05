---
title: Anthropic
type: entity
category: org
tags: [ai-lab, frontier-lab, claude]
aliases: [앤트로픽]
sources: [anthropic-project-glasswing-update-2026-05, anthropic-claude-code-auto-mode, anthropic-harness-design-long-running-apps, anthropic-managed-agents, anthropic-dynamic-workflows]
links:
  - https://www.anthropic.com
created: 2026-05-25
updated: 2026-05-30
---

# Anthropic

미국 샌프란시스코 기반 AI 안전·연구 회사. [[claude-mythos-preview|Claude]] 모델 패밀리의 개발사. 본 위키에서 자주 등장하는 주요 frontier lab.

## 위키에서 알려진 사실

- Claude 모델 패밀리 운영: 현재 공개 플래그십은 [[claude-opus-4-7]], 비공개 차세대급으로 [[claude-mythos-preview]]. 세대: [[claude-opus-4-5]] / [[claude-opus-4-6]] / [[claude-opus-4-7]], 그리고 mid-tier [[claude-sonnet-4-5]] / [[claude-sonnet-4-6]].
- 보안 이니셔티브 [[project-glasswing]]을 ~50개 파트너와 운영 ([[anthropic-project-glasswing-update-2026-05]])
- **Agent 인프라 라인업**:
  - [[claude-code|Claude Code]] — 공식 coding agent CLI ([[anthropic-claude-code-auto-mode|auto mode]] + [[dynamic-workflows]] 신규)
  - [[claude-agent-sdk]] — 에이전트 빌딩 SDK
  - [[managed-agents]] — 장기 horizon 에이전트의 호스팅 메타-하네스
- Engineering Blog의 연작 모티프: *"harnesses encode assumptions about what Claude can't do"* — [[anthropic-harness-design-long-running-apps]], [[anthropic-managed-agents]], [[anthropic-claude-code-auto-mode]]
- 제품: Claude Security (엔터프라이즈 public beta), Claude for Open Source, External Researcher Access Program
- 정책 입장: dual-use 위험이 큰 모델(예: Mythos-class)은 안전장치가 충분해질 때까지 일반 공개 보류

## 알려진 협력·관계

- **Glasswing 파트너**: [[cloudflare]], [[mozilla]], Oracle, Microsoft, Palo Alto Networks, Cisco
- **평가·정부**: [[uk-aisi]], NIST, UK NCSC, OSSF Alpha-Omega, Linux Foundation
- 미국·동맹국 정부와의 보안 협력 확대 의지 표명

## 미해결 사항 (위키가 채워갈 부분)

- 창립·자금조달·인력 구조 등 회사 기본 프로필 (별도 소스 ingest 필요)
- 모델 release timeline 전체
- 안전·alignment 연구 출판물

## References

- [[anthropic-project-glasswing-update-2026-05]]
- [[anthropic-claude-code-auto-mode]]
- [[anthropic-harness-design-long-running-apps]]
- [[anthropic-managed-agents]]
- [[anthropic-dynamic-workflows]]

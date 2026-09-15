---
title: Graft
type: entity
category: tool
tags: [coding-agents, knowledge-graph, cli, mcp, open-source]
links:
  - https://trailhq.com/graft
sources: [tech-bridge-graft-code-knowledge-graph]
created: 2026-09-15
updated: 2026-09-15
---

# Graft

**코딩 에이전트가 파일을 *찾는* 방식을 바꾸는 무료 오픈소스 CLI.** 프로젝트를 [[code-knowledge-graph|노드와 엣지의 지식 그래프]]로 만들어 두고, 에이전트가 검색 대신 그 지도를 조회하게 한다. 본 위키 첫 등장은 [[tech-bridge-graft-code-knowledge-graph]]([[ai-labs|AI Labs]] 소개 영상)이다.

> ⚠️ **이름 표기 주의.** 자막 양 트랙이 *"Graph"* · *"graft"* · ko *"접목"* 으로 흔든다 — **이 도구가 만드는 것이 지식 그래프(graph)여서 이름과 자료구조가 같은 소리로 뭉개진다.** 확정 근거는 **채널 공식 챕터 제목**(*"Graft 소개 및 지식 그래프 방식"*)과 설명란의 `trailhq.com/graft`다.

## 소스에서 확인되는 것

| 항목 | 내용 |
|---|---|
| **형태** | 컴퓨터에 설치하는 **터미널 명령**(CLI) + **MCP 서버**. *"설치하면 둘 다 받는다"* |
| **저장 형식** | 로컬 **JSON 파일** 하나. **브라우저 뷰어** 동봉 |
| **모델 사용** | **안 한다** — *"별도 API 키가 필요한 모델을 쓰지 않는다. 쓰던 구독 그대로"* |
| **설정** | 프로젝트 폴더에서 `init` → 쓰는 에이전트를 묻는다. 기존 코드가 있으면 `build` |
| **설치물** | **`graft` 스킬** + **훅 셋**(세션 시작 / 프롬프트 / 편집 후) → [[hook-enforced-workflow]] |
| **호환** | [[claude-code\|Claude Code]] · [[codex\|Codex]] · *"터미널 명령이나 [[model-context-protocol\|MCP]]를 쓰는 다른 코딩 에이전트"* |
| **선택 기능** | 모델로 **평문 설명 페이지** 생성 — 화자 스스로 *"꼭 필요하지 않다"* |
| **라이선스** | *"무료 오픈 소스"* 라고만 한다 |

## 두 가지 조달 방식

CLI(훅)는 **프롬프트마다 최대 3개 위치를 밀어 넣고**, MCP는 **에이전트가 필요할 때 묻는다**. 개발팀 자체 테스트에서 **MCP가 정답을 조금 더 맞혔고 CLI가 더 빨랐다** → [[push-vs-pull-context-retrieval]].

## 개발팀 자체 수치

**162회 실행 벤치마크**: 시간 **−60%** · 도구 호출 **−46%** · 토큰 **−42%** · 비용 **−32%**, 최선의 경우 **4배 저렴**.

> ⚠️ **전부 자체 보고이고 조건이 공개돼 있지 않다** — 162회가 무엇의 162회인지, 어떤 모델·저장소·과제였는지 소스에 없다. [[ai-labs]]의 시연(**1회**: 39분/31% vs 47분/35%)도 반복·통제가 없다.

## 화자가 스스로 말한 한계

- **코드만 매핑한다.** PRD·`learnings.md`·계획 파일은 기본 방식으로 남는다 → [[code-only-index-blind-spot]]
- **작은 프로젝트에서는 이득이 적다** — *"애초에 아낄 검색이 별로 없다"*
- **첫 빌드에서는 차이가 작다** — 그 시점엔 지도가 아직 없다

## 미해결 사항

- **만든 주체** — 자막은 *"the team behind Graft"* 까지. 설명란의 `trailhq.com/graft` 외에 **회사명·사람 이름이 없다.**
- **지원 언어** — 참조 관계를 뽑으려면 언어별 파서가 필요한데 **한 마디도 없다.** ([[tree-sitter]]가 이 위키에 있으나 **소스가 연결하지 않는다.**)
- **라이선스 종류 · 대형 저장소 빌드 시간 · "최대 3개"의 근거 · 틀린 위치를 붙였을 때의 처리**
- **보안** — 매 프롬프트에 코드 위치를 자동 첨부하는 구조인데 [[prompt-injection]]·[[lethal-trifecta]] 논의가 **전혀 없다.**

## References

- [[tech-bridge-graft-code-knowledge-graph]] · [[ai-labs]] · [[code-knowledge-graph]] · [[file-discovery-tax]]

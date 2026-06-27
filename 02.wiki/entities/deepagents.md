---
title: DeepAgents
type: entity
category: tool
tags: [langchain, agent-sdk, harness, framework]
aliases: [DeepAgent, DeepAgents SDK]
sources: [self-harness-paper]
links:
  - https://github.com/langchain-ai/deepagents
created: 2026-06-14
updated: 2026-06-14
---

# DeepAgents

LangChain이 만든 에이전트 구축 **SDK/프레임워크** (`langchain-ai/deepagents`). 본 위키에는 **[[self-harness|Self-Harness]] 실험**([[self-harness-paper]])의 *초기 하니스 토대*로 등장 — `create_deep_agent(model, system_prompt, backend)` 형태로 모델을 에이전트로 인스턴스화.

## 위키에서 알려진 사실 (Self-Harness 맥락)

- Self-Harness의 **초기 하니스는 의도적으로 최소 구성** (Figure 3): Terminal-Bench-2.0 기본 시스템 프롬프트 + DeepAgent 기본 도구(파일 읽기/쓰기/편집 + 셸 실행)만.
- Self-Harness가 수정할 수 있는 대상은 **DeepAgent 인스턴스화·제어 방식을 설정하는 하니스 정의 파일** — 선언적 config point(instruction, tools, verification guidance, runtime control policy 등)가 *editable surface*.
- 즉 DeepAgents는 *"무엇을 바꿀 수 있는가"* 의 표면을 정의하는 layer. Self-Harness의 채택 edit들(예: 부트스트랩 지시 교체, runtime policy 활성화, tool-error 미들웨어 추가)은 모두 이 config point 위에서 일어난다.

## 본 위키 연결

- [[agent-harness-design]]의 *"Tool Harness"* 층(모델에 터미널·시스템 프롬프트를 입히는 래퍼)에 해당하는 오픈소스 SDK. [[claude-agent-sdk|Claude Agent SDK]]와 같은 카테고리.
- 최소 하니스에서 출발해 진화시킨다는 점에서, *"sparse 초기 하니스도 자기개선을 지지할 수 있다"* 는 [[self-harness]] 결론의 전제.

## 미해결 사항

- DeepAgents의 전체 API·subagent/skill/memory 추상, LangChain 생태계 내 위치 (별도 소스 필요)

## References

- [[self-harness-paper]]
- [langchain-ai/deepagents (GitHub)](https://github.com/langchain-ai/deepagents)

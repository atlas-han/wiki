---
title: Claude Code 공식 모범 사례 쉽게 이해하기
type: source
tags: [source, anthropic, claude-code, coding-agent, best-practices]
created: 2026-07-21
updated: 2026-07-21
source-url: https://charlychoi.blogspot.com/2026/07/claude-code.html
source-type: article
author: Charly Choi
date-published: 2026-07-20
ingested: 2026-07-21
---

# Claude Code 공식 모범 사례 쉽게 이해하기

Charly Choi가 Anthropic의 공식 Claude Code best practices를 한국어 학습용으로 재구성한 2차 해설. [[claude-code]]를 단순 chatbot이 아니라 **검증 가능한 task를 수행하는 coding worker**로 운영하는 방법을 prompt, project rule, permission, context, multi-agent 관점에서 한 번에 정리한다.

> ⚠️ **성격과 한계**: 공식 문서 자체가 아니라 설명과 예시가 추가된 2차 자료다. 제품 command·permission mode처럼 변동 가능한 항목은 [Anthropic 공식 문서](https://code.claude.com/docs/ko/best-practices)를 현재 기준으로 재확인해야 한다.

## 핵심 요약

1. **완료 기준을 먼저 설계** — test·build·typecheck·screenshot·고정 output 같은 executable verifier가 “done”을 결정한다. [[verifiable-goals]]과 같은 원리다.
2. **복잡한 일은 Explore → Plan → Implement → Verify → Review** — 특히 인증·결제·권한·DB migration·대규모 refactoring은 조사와 구현을 분리한다.
3. **맥락과 범위를 명시** — 관련 파일, 증상, 재현 조건, 기대 결과, 기존 pattern, 금지 작업, 보고 형식을 task contract에 넣는다. 이는 [[surgical-edits]]의 scope control과 연결된다.
4. **규칙을 실행 강도별로 배치** — 항상 필요한 짧은 규칙은 `CLAUDE.md`, 특정 업무 지식은 Skills, 반드시 지켜야 할 guard는 Hooks, 외부 시스템 연결은 CLI/MCP에 둔다. [[harness-engineering]]의 AI Layer를 실무적으로 풀어 쓴 형태다.
5. **context와 역할을 분리** — unrelated task는 `/clear`, 조사·review는 subagent, 구현자와 evaluator는 분리한다. 대량 변경은 소수 pilot 후 fan-out한다.
6. **권한은 blast radius 제어 장치** — permission mode, allowlist, sandbox로 속도와 안전성을 함께 설계한다.

## Task contract

글 전체를 압축하면 다음 계약으로 정리된다.

| 항목 | 질문 | 예시 evidence |
|---|---|---|
| Goal | 어떤 결과를 내야 하는가? | “로그인 실패를 재현하고 수정” |
| Scope | 어디까지 바꿀 수 있는가? | `src/auth`, 범위 밖 refactoring 금지 |
| Context | 현재 증상·제약·pattern은? | 재현 조건, session 방식, 기존 test |
| Verifier | 무엇이 통과하면 끝인가? | failing test→pass, build/typecheck green |
| Safety | 무엇을 하면 안 되는가? | error 은폐, test 약화, 임시 우회 금지 |
| Report | 어떤 증거를 남길 것인가? | root cause, changed files, commands, risks |

핵심은 “좋은 prompt”보다 **에이전트가 스스로 판정할 수 있는 task contract와 외부 verifier**다. 이 계약은 [[llm-coding-guidelines]]의 Goal-Driven Execution, [[sprint-contract]], [[generator-evaluator-pattern]]을 단일 실무 workflow로 묶는다.

## 실패 패턴

- **Kitchen-sink session** — 무관한 작업이 한 context에 섞여 판단 품질이 하락.
- **Repeated correction loop** — 실패한 접근이 누적되면 깨끗한 새 prompt가 더 낫다.
- **Overlong `CLAUDE.md`** — 일반론이 project-specific rule을 묻는다.
- **Trust-verification gap** — evidence 없이 그럴듯한 결과를 완료로 인정한다.
- **Unbounded exploration** — 조사 범위가 없어 context를 소모한다.

## 위키 내 의미

새로운 독립 개념이라기보다 기존 위키의 [[verifiable-goals]]·[[llm-coding-guidelines]]·[[harness-engineering]]·[[generator-evaluator-pattern]]을 **Claude Code 실무 운영 checklist**로 합친 자료다. 특히 “목표 + 맥락 + verifier + permission + review”를 한 task contract에 묶는 점이 유용하다.

## References

- 원문: <https://charlychoi.blogspot.com/2026/07/claude-code.html>
- 공식 기반 문서: <https://code.claude.com/docs/ko/best-practices>
- raw structured extraction: `01.raw/articles/2026-07-20_Claude Code 공식 모범 사례 쉽게 이해하기.md`
- 관련: [[claude-code]], [[verifiable-goals]], [[llm-coding-guidelines]], [[harness-engineering]], [[surgical-edits]], [[generator-evaluator-pattern]]

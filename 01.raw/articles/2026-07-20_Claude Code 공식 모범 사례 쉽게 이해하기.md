---
source_url: https://charlychoi.blogspot.com/2026/07/claude-code.html
ingested: 2026-07-21
sha256: 3a1399b3eaf02c80ae3e9477ad23efcd47982ec78761c6cf6ea2dff3294ba466
title: Claude Code 공식 모범 사례 쉽게 이해하기
author: Charly Choi
published: 2026-07-20
source_type: article
capture: structured-extraction
---
# Claude Code 공식 모범 사례 쉽게 이해하기 — 구조화 추출

## Source character

- Charly Choi가 Anthropic의 공식 **Claude Code best practices** 문서를 한국어 학습용으로 재구성한 2차 해설이다.
- 원문 전체를 복제하지 않고, 핵심 thesis·운영 모델·실패 패턴·template inventory만 보존한다.
- 공식 문서 링크: <https://code.claude.com/docs/ko/best-practices>

## Central thesis

AI coding agent의 품질은 긴 prompt 자체보다 **목표 + 맥락 + 검증 기준 + 권한 제한 + 독립 리뷰**를 갖춘 운영 구조에 좌우된다. Claude Code는 답변형 chatbot이 아니라 파일·terminal·test·build를 다루는 실행형 작업자로 취급해야 한다.

## Recommended operating loop

1. **Explore** — 관련 파일, 현재 흐름, 기존 pattern과 test를 먼저 조사한다.
2. **Plan** — 변경 파일, data/control flow, test strategy, 보안 위험을 명시한다.
3. **Implement** — 합의한 범위만 수정한다.
4. **Verify** — test, build, typecheck, screenshot, console error 등 task에 맞는 executable evidence를 만든다.
5. **Review and report** — 독립 reviewer가 requirement·edge case·security·scope drift를 점검하고, 변경 파일·실행 명령·결과·잔여 위험을 보고한다.

작은 오타나 단순 변경은 planning overhead를 생략할 수 있지만, 인증·결제·권한·DB migration·대규모 refactoring은 exploration과 planning을 분리한다.

## Verification inventory

| Task | Suggested verifier |
|---|---|
| 함수/API | unit/integration test, status code와 sample response |
| UI | desktop/mobile screenshot, clickability, browser console error 없음 |
| Build/type issue | build·typecheck command 성공 |
| Refactoring | 변경 전후 기존 test 통과 |
| Documentation | 필수 section, 실제 command, link validity |
| Data processing | fixed input/output comparison |

## Context and control surfaces

- Prompt context: 관련 파일·폴더, 증상, 재현 조건, 기대 결과, 기존 pattern, 금지 범위, 보고 형식.
- `CLAUDE.md`: 모든 session에 필요한 짧은 project operating card. 지워도 실수가 늘지 않는 일반론은 제거한다.
- Hooks: lint, secret scan, protected-folder guard, pre-commit test처럼 **반드시 실행**되어야 하는 규칙.
- Skills: 특정 반복 업무와 domain convention을 on-demand로 로드.
- MCP/CLI: GitHub, cloud, issue tracker, monitoring, design system 등 외부 시스템을 context-efficient command surface로 연결.
- Permission mode/sandbox/allowlist: agent 속도를 유지하되 blast radius를 제한.

## Context and scaling practices

- unrelated task 사이에는 `/clear`; 긴 session은 `/compact`; 잘못된 접근은 checkpoint/`/rewind`로 되돌린다.
- 조사와 review는 subagent의 별도 context로 보내 main context를 보호한다.
- Writer/Reviewer를 분리하고, 대량 변경은 2~3개 파일 pilot 후 fan-out한다.
- non-interactive `claude -p`와 structured output을 CI·review·batch automation에 사용할 수 있다.

## Failure patterns

1. **Kitchen-sink session** — 서로 무관한 task가 한 context에 누적됨.
2. **Repeated correction loop** — 실패한 접근이 context에 남아 같은 오류를 반복함.
3. **Overlong CLAUDE.md** — 핵심 project rule이 일반론에 묻힘.
4. **Trust-verification gap** — 그럴듯한 구현을 evidence 없이 완료로 인정함.
5. **Unbounded exploration** — 범위 없는 조사가 파일과 token을 소모함.

## Reusable task contract

- Goal: 한 문장의 명확한 결과
- Scope: 관련 파일·폴더와 범위 밖 변경 금지
- Context: 증상, 재현 조건, 기대 결과, 기존 pattern
- Completion criteria: test/build/typecheck/screenshot 등 executable verifier
- Safety: test 약화·error 은폐·임시 우회·destructive action 금지
- Report: root cause, changed files, commands, results, remaining risks

## Limitations

- 공식 문서의 학습용 재구성본이므로 일부 예시·명명·“AI 개발팀” 역할 모델은 저자의 설명 방식이며 Anthropic의 직접 표현과 구분해야 한다.
- 제품 command와 permission mode는 빠르게 바뀔 수 있으므로 실행 전 현재 공식 문서를 재확인해야 한다.
- 제시된 prompt는 범용 template이며 repository별 architecture·test policy·security policy를 대체하지 않는다.

## References

- Charly Choi, “Claude Code 공식 모범 사례 쉽게 이해하기”, 2026-07-20: <https://charlychoi.blogspot.com/2026/07/claude-code.html>
- Anthropic, “Claude Code 모범 사례”: <https://code.claude.com/docs/ko/best-practices>

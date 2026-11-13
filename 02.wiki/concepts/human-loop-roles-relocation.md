---
title: "사람의 다섯 가지 일 이양 (Human Loop Roles Relocation) — 조종 · 승인 · 거절 · 확인 · 시작은 어디로 갔나"
type: concept
category: pattern
tags: [claude-code, human-in-the-loop, auto-mode, permission-rules, sandboxing, hooks, ci, agent-harness, best-practices]
aliases: [사람이 하던 다섯 가지 일, five human jobs, steer approve deny verify start, 조종 승인 거절 확인 시작, Rethinking Claude Code Best Practices]
related: [action-reversibility, hard-vs-soft-enforcement, transcript-classifier, agent-sandboxing, hook-enforced-workflow, risk-proportional-human-review, cloud-agent-delegation, prompt-debt, verification-bottleneck]
first-seen: tech-bridge-lydia-hallie-rethinking-claude-code-best-practices
sources: [tech-bridge-lydia-hallie-rethinking-claude-code-best-practices]
created: 2026-11-13
updated: 2026-11-13
---

# 사람의 다섯 가지 일 이양 (Human Loop Roles Relocation)

**코딩 에이전트 세션에서 사람이 하던 일을 다섯 가지로 나누고, 사람이 빠질 때 각각을 모델 · 하네스 · 환경 중 무엇이 맡는지 정하는 틀.** [[lydia-hallie|Lydia Hallie]](Anthropic Claude Code 팀)의 발표를 해설한 [[tech-bridge-lydia-hallie-rethinking-claude-code-best-practices]]에서 왔다. 테제: *"예전 모범 사례는 사라진게 아니라 자리를 옮겼습니다."*(08:01~08:05)

> ⚠️ **해설자의 요약이다.** 발표 원음은 위키에 캡션이 없고, 실험 수치 · 문서 문장은 한국어 번역으로 기록됐다.

## 다섯 가지 일과 새 담당

| 사람의 일 | 새 담당 | 핵심 장치 | 보장 수준 |
|---|---|---|---|
| **조종** — 방향을 잡고 중간에 고침 | 모델 | 더 나은 모델(Opus 5.5) + CLAUDE.md에서 *저장소를 읽어 알 수 없는 것* 만 남기기 | 대부분 잘됨 |
| **승인** — 명령을 하나씩 허락 | 하네스(분류기) | auto mode + 믿는 저장소 · 버킷 · 도메인을 평문으로 설정 | 사람보다 낫지만 10건 중 1건 통과 |
| **거절** — 안 된다고 막음 | 하네스 + 환경 | *되돌릴 수 없는 것* 만 거절 규칙 · 샌드박스(OS 강제, 자식 프로세스까지) · 클라우드 세션 | **보장** |
| **확인** — 결과를 봄 | 하네스 | 검증 지점(테스트 · 빌드 · 스크린샷) + 훅(편집마다 린트 · 완료마다 테스트 · 멈출 때 전체) — **exit 2** | 보장(훅) / 비보장(프롬프트) |
| **시작** — 세션을 띄움 | 모델 + CI | CI · autofix · 새 컨텍스트 Claude 리뷰 · 위험도별 사람 리뷰 · 지휘자 세션 | 설정 무관 동일 검사(CI) |

## 핵심 구분 — 대부분 vs 보장

- 출발점의 수치(해설): 위험한 명령을 사람은 약 14%, auto mode는 89% 막았다. 그래도 *"열개 중 한 개는 여전히 통과했습니다."*(00:27~00:30)
- *"모델에게 맡기면 대부분 잘되지만 보장은 아닙니다. 보장은 한스에서만 걸 수 있습니다."*(03:36~03:41)[=하네스] → [[hard-vs-soft-enforcement]]
- 그래서 하드 장치는 **되돌릴 수 없는 것** 에만 — 지워지는 것 · 비밀값이 드러나는 것 · 바깥으로 나가는 것. 코드 실수는 git으로 되돌리면 되니 모델에 맡긴다 → [[action-reversibility]].
- 권한 규칙은 *실행할지* 만 정하고 *실행된 뒤 어디까지 손을 뻗는지* 는 못 막는다 → 명령이 아니라 **환경** 을 제한한다([[agent-sandboxing]] · [[cloud-agent-delegation]]). 샌드박스는 셸 명령만 덮는다(파일 도구 · MCP · 훅은 바깥).

## 다른 페이지와의 관계

- [[transcript-classifier]] · [[deny-and-continue]] — *승인* 칸의 장치. 이 틀은 분류기를 **보장 장치가 아닌 것** 으로 둔다.
- [[hook-enforced-workflow]] — *확인* 칸. 프롬프트는 보장이 아니고 훅이 보장이다.
- [[risk-proportional-human-review]] — *시작* 칸에서 사람이 남는 자리(문서 0명 · 보통 1명 · 위험 2명).
- [[verification-bottleneck]] — *바뀐 파일 63개를 다 읽지는 않는다* 는 같은 문제의 다른 표현.
- [[prompt-debt]] — *조종* 칸의 정리 작업(강조를 쌓으면 과하게 적용).

## 열린 질문

- 지휘자 세션 기능의 정식 이름(해설은 *"아직 베타인 클로드 코드 프로젝트"*).
- 리디아의 *질문 하나* 의 원문(무캡션, 챕터 제목 *되돌릴 수 있는가?*).

## References

- [[tech-bridge-lydia-hallie-rethinking-claude-code-best-practices]]

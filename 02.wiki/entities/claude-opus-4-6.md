---
title: Claude Opus 4.6
type: entity
category: model
tags: [anthropic, claude, opus]
aliases: [Opus 4.6]
sources: [anthropic-project-glasswing-update-2026-05, anthropic-harness-design-long-running-apps, anthropic-claude-code-auto-mode, tech-bridge-armin-ronacher-workshop-before-software-factory]
links: []
created: 2026-05-25
updated: 2026-11-26
---

# Claude Opus 4.6

[[anthropic|Anthropic]]의 이전 세대 플래그십 모델. 두 가지 맥락에서 본 위키에 등장:
1. [[project-glasswing]] 발표에서 [[claude-mythos-preview]]의 성능 비교 **baseline** ([[ai-vulnerability-discovery]]에서 Mythos Preview 대비 약 10배 열세, Firefox 사례).
2. [[anthropic-harness-design-long-running-apps]]에서 [[claude-opus-4-5]] 대비 capability 도약 — [[context-anxiety]] 해소, long-context retrieval 개선, 자기 실수 catch 능력 등으로 **harness scaffolding을 줄일 수 있게** 한 모델.

## 위치

- 직전: [[claude-opus-4-5]]
- 직후 모델: [[claude-opus-4-7]] (현 공개 플래그십)
- 같은 세대 mid-tier: [[claude-sonnet-4-6]]
- 한 단계 위 (비공개): [[claude-mythos-preview]]

## 알려진 사실

- [[anthropic-claude-code-auto-mode]] 글이 system card §6.2.1·§6.2.3.3 (Opus 4.6 시스템 카드)을 [[agentic-misbehavior]] 사례 출처로 인용
- Opus 4.6 출시 후 [[anthropic-harness-design-long-running-apps]]의 sprint construct 제거 + DAW 풀스택 build에서 builder가 **2시간 7분 연속 코딩** (sprint 분해 없이도 일관성 유지)
- Opus 4.6 [launch blog](https://www.anthropic.com/news/claude-opus-4-6) 인용: "plans more carefully, sustains agentic tasks for longer, can operate more reliably in larger codebases, and has better code review and debugging skills to catch its own mistakes"
- [[ai-vulnerability-discovery]] 능력에서 Mythos Preview 대비 약 10배 열세 (Firefox 사례)

## References

- [[anthropic-project-glasswing-update-2026-05]]
- [[anthropic-harness-design-long-running-apps]]
- [[anthropic-claude-code-auto-mode]]

## 비교의 기준점으로 — 같은 하네스에서 2.4분 (2026-11-26 · [[tech-bridge-armin-ronacher-workshop-before-software-factory]])

[[armin-ronacher|Armin Ronacher]]의 [[pi-coding-agent|Pi]] 세션 기록에서 Opus 4.6은 뒤 모델과 견주는 기준점으로 나온다(한국어 해설 전달, n=1): *"이 그래프는 프롬프트 하나를 받은 에이전트가 혼자 일한 시간을 상위 10% 기준으로 보여줍니다."*(02:21~02:25) *"오퍼스 4.6은 2.4분, 지금의 오퍼스 5.5는 14분입니다. 같은 하네스로 여섯 배 가까이 오래 일합니다."*(02:26~02:32) → [[claude-opus-5-5]]

⚠️ 한 사람의 자기 계측이고 계측 방법은 캡션에 없다. 두 모델 사이의 모델들(4.7 등)이 그래프에 있었는지도 캡션으로 알 수 없다.

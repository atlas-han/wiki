---
title: "홈 레포 패턴 (Home Repo Pattern) — 에이전트의 집을 하나 정한다"
type: concept
category: pattern
tags: [multi-repo, monorepo, agent-skills, agents-md, claude-md, progressive-disclosure, worktree, team-config]
aliases: [Home Repo, home repo, 홈 레포, 홈 리포, home repo pattern]
related: [agent-skills, mcp-skill-distribution, deferred-tool-context, llm-wiki-pattern, no-silent-write, harness-engineering]
first-seen: tech-bridge-matt-pocock-home-repo-pattern
sources: [tech-bridge-matt-pocock-home-repo-pattern]
created: 2026-11-16
updated: 2026-11-16
---

# 홈 레포 패턴 (Home Repo Pattern)

**저장소가 여러 개인 조직에서 코딩 에이전트의 스킬 · 설정 · 공유 문서 · 도구를 집이 되는 저장소 하나에 모으고, 다른 저장소는 그 안의 파일에 *경로 한 줄* 로 가리킨 뒤, 에이전트는 늘 그 저장소에서 실행하는 방식.** [[matt-pocock|Matt Pocock]]이 aihero.dev 글 *The Home Repo Pattern* 으로 정리했고, 위키에는 [[tech-bridge-matt-pocock-home-repo-pattern]](2026-11-15 공개 한국어 해설)로 들어왔다. ⚠️ 원 글 · 영상 미열람, 해설 전달.

## 풀려는 문제

[[agent-skills|스킬]] · AGENTS.md처럼 *세션마다 있어야 하는 것* 을 어디에 둘까 — 흔한 두 답이 모두 새는 곳이 있다.

| 방식 | 장점 | 새는 곳 |
|---|---|---|
| 저장소마다 복사 | 어디서 시작해도 같은 스킬 | 고칠 때마다 30~40개 저장소를 맞춰야 함 |
| 각자 사용자 폴더 | 모든 저장소에서 보임 | 눈에 안 띄어 갱신이 안 되고 팀 설정에서 뒤처짐 — Pocock은 사용자 폴더를 *내 방식으로 고치는 자리* 로 남겨 둔다 |
| **홈 레포** | 스킬이 git으로 버전 관리 · 팀이 공유 · 실행 위치가 하나 | 규모가 수백 개를 넘으면 구조를 바꿔야 함 |

## 구성 (해설 전달)

- 홈 레포: 스킬 폴더(비공개 스킬) · 설정 파일 · 코딩 표준 같은 공유 문서 · 위키 · 직접 만든 도구.
- 세션 시작 때 읽히는 파일(CLAUDE.md 또는 AGENTS.md)에 *Other repos* 같은 제목 아래 **저장소 이름과 경로 한 줄씩** — 필요하면 힌트(*고치기 전에 그쪽 AGENTS.md부터 읽어라*). 경로에 없으면 에이전트가 클론해 온다.
- 각 저장소에는 그 저장소 전용 것만 남는다 — 자체 AGENTS.md · 빌드와 테스트 명령 · 전용 문서. 코드 · 이력 · 이슈 트래커는 제자리.
- 여러 에이전트가 같은 저장소를 건드리면 *한 번 클론하고 기능마다 worktree*. 변형: 저장소들을 홈 레포 안에 클론하고 `.gitignore`로 빼 둔다.

## 규모 사다리

| 규모 | 처방 |
|---|---|
| ~20개(영상은 30~40개도) | 포인터 한 줄씩 |
| ~400개 | **점진적 공개** — 영역별 파일을 가리키고 그 파일 안에 저장소 목록 → [[deferred-tool-context]]와 같은 모양 |
| 수천 개 | 스킬 마켓플레이스 → [[mcp-skill-distribution]] |

git submodule은 5~10개면 괜찮지만 포인터로 같은 일을 할 수 있다. 모노레포가 가능하면 모노레포가 먼저고, 공개 · 비공개가 섞이거나 팀이 받아들이지 않을 때 홈 레포가 그 자리를 대신한다.

## 도입 절차 — 프롬프트 4단계

저장소 목록 작성 · 연결 여부 질문 → 스킬 · 문서 분류(공용 · 중복 · 전용 · 설치형) → 계획 합의 → 공용 · 중복만 홈으로. 안전장치: 승인 전 읽기만 · 비밀 파일(`.env`) 금지 · 커밋은 홈 레포에, 푸시는 사람이 → [[no-silent-write]]. 옮긴 저장소에서는 새 브랜치로 *옮긴 복사본만* 지운다.

## 위키의 읽기

- 핵심은 파일 배치가 아니라 **실행 위치의 고정** 이다 — 에이전트가 늘 같은 곳에서 출발하면 그곳의 설정이 곧 팀 설정이 된다. [[harness-engineering]]의 *하네스를 팀 자산으로* 를 멀티 레포에서 푸는 가장 가벼운 방법.
- 홈 레포 안의 *Karpathy 스타일 LLM 위키* 와 도구 묶음(Gmail · Slack · Discord · YouTube · GitHub · Calendar)은 한 세션에서 *메시지 찾기 → 저장소 수정 → 강의 수정* 을 잇게 한다 → [[llm-wiki-pattern]]. 이 위키를 운영하는 작업 공간(에이전트가 늘 같은 저장소에서 출발하고 다른 저장소를 경로로 찾는 구조)도 같은 모양이다(위키의 관찰).
- ⚠️ 한 사람의 경험, 효과 수치 없음, 제안자는 에이전트 코딩 강의 판매자 — 해설 스스로 짚는다.

## References

- [[tech-bridge-matt-pocock-home-repo-pattern]] · [[matt-pocock]]
- The Home Repo Pattern https://aihero.dev/the-home-repo-pattern (설명란, 위키 미열람)

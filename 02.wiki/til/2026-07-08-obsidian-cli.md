---
title: Obsidian 공식 CLI로 vault를 terminal-first로 다루기
type: til
date: 2026-07-08
tags: [tool, workflow, obsidian, cli, terminal]
related: [obsidian-cli-workflow, obsidian, claude-code, llm-wiki-pattern]
sources: [xda-obsidian-cli-terminal-workflow]
created: 2026-07-08
updated: 2026-07-08
---

# Obsidian 공식 CLI로 vault를 terminal-first로 다루기

Obsidian **1.12+** 에 공식 CLI가 생겨서, vault를 GUI가 아니라 terminal command surface로 다룰 수 있다.

- **설치**: Settings → General → Advanced → *command-line interface* 토글 → **Register** (PATH 등록). 새 terminal부터 동작, TAB 자동완성 지원.
- **핵심 command**: `daily:append content="..."`(daily note에 누적) · `search:context query="..." limit=10`(vault-aware grep) · `create` · `read` · `move file`(이동 후 링크 자동 재작성 — 단순 `mv`와 다름).
- **agent 통합**: [[claude-code|Claude Code]] 같은 agent가 이 CLI로 vault를 읽고·검색하고·변경 기록을 남길 수 있다.
- **한계**: desktop 앱이 **실행 중이어야** 동작하고, third-party plugin은 자체 command를 노출해야만 CLI에서 쓸 수 있다. GUI 대체가 아니라 capture·search·automation을 terminal로 확장하는 도구.

자세한 정리는 [[obsidian-cli-workflow]] · [[obsidian]] 참조.

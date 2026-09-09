---
title: Cursor Cloud (Cloud Agents)
type: entity
category: product
tags: [cloud-agents, remote-vm, automations, cursor]
links:
  - https://cursor.com/docs/cloud-agent
  - https://cursor.com/docs/automations
sources: [tech-bridge-cursor-legacy-refactoring]
created: 2026-09-09
updated: 2026-09-09
---

# Cursor Cloud

[[cursor|Cursor]]의 **원격 자율 에이전트 실행 환경**. 이 위키 첫 등장은 [[tech-bridge-cursor-legacy-refactoring]]이며, 55분 워크샵의 대부분이 이 제품을 다룬다.

> [[tech-bridge-grokbot-agent-teams]](2026-08-31)에서 *"클라우드 에이전트를 설정해 두면 [[grokbot|GrokBot]]이 그 에이전트를 실행할 수 있다"* 고 이미 언급됐으나, **제품 자체가 서술된 것은 이번이 처음**이다.

## 구성

| 요소 | 내용 |
|---|---|
| **실행 환경** | 원격 **Linux VM**. 컴퓨터·마우스 접근 가능 |
| **환경 설정** | 첫 세팅 10~20분 → **build**로 캐싱. API 키·시크릿·라우팅 규칙·IP 허용목록이 여기 산다 |
| **레포** | GitHub 연결. **멀티 레포** 선택 가능 |
| **MCP** | 로컬 MCP를 클라우드에서도 연결 (Atlassian·Datadog·Google Drive·granola·PagerDuty 등) |
| **접점** | 브라우저(`cursor.com/agents`) · Slack · iOS 모바일 앱(Android 예정) |
| **모드** | `long running agents`(`/goal` 유사, 시간 제한 설정) · multitask mode |
| **자기 검증** | 스크린샷·**구간 라벨이 붙은 UI 조작 비디오**·엔드투엔드 테스트 |
| **automations** | 예약/이벤트/웹훅 트리거. 각 automation에 **`memories.md`** |
| **진단** | **cursor cloud MCP** — 실패한 실행·환경 진단 |
| **프라이빗 연결** | Cloudflare 터널 / AWS PrivateLink / Tailscale. self-host도 있으나 *"처음부터 권하지 않는다"* |

세팅 진입점으로 `cursor.com/onboard`가 안내된다.

## 위키에서 알려진 사실

- **모델 선택이 로컬과 다르다** — 비디오·스크린샷 반환으로 토큰을 더 쓰므로 **더 싸고 빠른 모델**을 권한다([[grok-4-6|Grok 4.6]]·Composer 2.5·GPT-5.6). ⚠️ *"마이그레이션 전체에 3~4달러"* 는 조건 없는 주장이다. → [[model-mixing-economics]]
- **자율이되 개입 가능** — 후속 지시·중단이 브라우저와 모바일 양쪽에서 가능하다.
- **티켓당 별도 PR** 이 권장된다 — *"모든 걸 하나의 거대한 PR에 넣지 않도록."*
- 사내 활용으로 **금요일 백로그 일괄 실행 → 월요일 PR 리뷰**, **유럽/아시아 팀 비동기 인계**가 언급된다.
- ⚠️ **크래시 시 컨텍스트 복구 여부에 답이 없다** — 발표자가 *"모르겠습니다"* 라 하고 그 자리에서 시험하지만 소스가 결과를 보여주지 않는다.

## References

- [[tech-bridge-cursor-legacy-refactoring]] · [[cursor]] · [[cloud-agent-delegation]] · [[scheduled-agent-automations]]

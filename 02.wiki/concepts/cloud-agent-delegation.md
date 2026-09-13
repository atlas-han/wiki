---
title: 클라우드 에이전트 위임 (Cloud Agent Delegation)
type: concept
category: pattern
tags: [cloud-agents, remote-vm, self-verification, async-collaboration, multi-repo]
aliases: [클라우드 에이전트, cloud agents, 원격 위임]
related: [plan-to-ticket-pipeline, scheduled-agent-automations, model-mixing-economics, behavior-validated-trust, persistent-agent-teams, generator-evaluator-pattern, goal-level-delegation]
first-seen: tech-bridge-cursor-legacy-refactoring
sources: [tech-bridge-cursor-legacy-refactoring, tech-bridge-acp-universal-remote, tech-bridge-lauren-tan-trusting-agents]
created: 2026-09-09
updated: 2026-09-13
---

# 클라우드 에이전트 위임

**에이전트를 원격 VM에서 자율 실행시키고, 결과를 PR과 자기 검증 증거로 받는** 실행 형태.

> 이 에이전트들은 **자율적으로, 원격 머신에서** 동작합니다. 즉 **에이전트를 띄우고 노트북을 닫아도 에이전트는 계속 돕니다.** — [[tech-bridge-cursor-legacy-refactoring]]

## 성질

| 성질 | 내용 |
|---|---|
| **탈로컬** | 원격 Linux VM. 사용자 머신을 점유하지 않는다 |
| **멀티 레포** | 마이크로서비스, 또는 내부 SDK 변경이 여러 클라이언트로 파급되는 경우 |
| **환경 캐싱** | 첫 세팅 10~20분 → **build로 저장**되어 이후 즉시 시작 |
| **MCP 승계** | 로컬에서 쓰던 MCP를 클라우드에서도 연결 |
| **개입 가능** | *"자율적이도록 만들어졌지만 사용자 입력도 받도록"* — 후속 지시·중단 가능 |
| **작업 분할** | **티켓당 별도 PR.** *"모든 걸 하나의 거대한 PR에 넣지 않도록"* |

## 자기 검증 — 자기 마우스로 UI를 조작한 비디오

이 패턴에서 가장 구체적인 주장이다. 원격 VM이므로 에이전트는 **컴퓨터와 마우스에 접근할 수 있다.**

> **Cursor가 자기 마우스, 자기 컴퓨터를 써서 저를 위해 무언가를 테스트하는 것입니다. 저는 아무것도 조종하지 않습니다.** 전체 녹화를 하고 저에게 돌려보냅니다.

비디오에 **구간 라벨**까지 붙는다(*로그인 섹션 / 댓글 보기 / 사용자 보기*). 마이그레이션·리팩터링의 목적이 **회귀가 없음을 보이는 것**이므로 증거의 형태가 스크린샷·비디오·엔드투엔드 테스트가 된다.

→ [[behavior-validated-trust]]의 실행 형태다. **에이전트가 자기 작업의 증거를 제출한다.**

> ⚠️ **작성자와 검증자가 같은 에이전트일 때 그 증거의 독립성**을 소스가 제기하지 않는다. [[generator-evaluator-pattern]]이 다뤄온 문제다.

## 조직 차원의 효과

> 금요일에 **티켓 백로그를 통째로 돌려놓고 월요일에 돌아와 PR을 리뷰**합니다. **분산 팀에 정말 좋습니다** — 유럽 팀과 아시아 팀이 있다면 **한 팀이 잠들 때 다른 팀이 이어받는** 식으로 비동기 협업할 수 있습니다.

이것은 이 위키의 [[persistent-agent-teams]]가 *동료 같은 봇* 으로 그린 그림의 **잡(job) 버전**이고, [[goal-level-delegation]]이 말한 위임 층위를 인프라로 구현한 것이다.

## 접점

브라우저 UI 외에 **Slack 봇**(문서-구현 동기화 검사 후 PR)과 **모바일 앱**(iOS, Android 예정)에서도 같은 에이전트를 띄우고 중단할 수 있다.

## ⚠️ 미해결

- **라이브 시연이 시간 안에 끝나지 않았다** — 완성 예시는 사전 준비분이다. **종단 결과가 라이브로 검증되지 않았다.**
- **크래시 시 컨텍스트 복구 여부에 답이 없다** — 발표자가 *"모르겠습니다, 확인해 봐야 합니다"* 라 하고 시험하지만 소스가 결과를 보여주지 않는다.
- **당사자 진술** — Cursor 직원의 자사 제품 워크샵이다.

## 프로토콜 층에서 본 클라우드 위임 (2026-09-12 ACP 편)

[[tech-bridge-acp-universal-remote]]는 클라우드 에이전트를 **제품 기능이 아니라 전송 계층의 귀결**로 놓는다.

> **로컬만으로는 당연히 부족합니다.** 이게 뜨려면 **원격도 돼야** 해요. **에이전트는 클라우드에서 돌게 될 테니까요.**

그래서 [[goose|Goose]] 팀이 [[agent-client-protocol|ACP]]에 **HTTP 전송 + WebSocket 업그레이드**를 명세했고, 결과는 [[agentic-stack-decomposition|네 구성 요소의 독립 배치]]다 — *"로컬과 원격을 아주 쉽게 오갈 수 있습니다."*

## 클라우드 위임의 전제는 신뢰다 (2026-09-12 Lauren Tan 편)

[[tech-bridge-lauren-tan-trusting-agents]]가 순서를 못 박는다 — **로컬에서 관찰하며 신뢰를 쌓은 뒤에** 클라우드로 간다.

> **시작하기 가장 좋은 곳은 로컬**입니다. **에이전트가 무엇을 하는지 관찰할 수 있으니까요.**

> **아직 이 구간에 있다면 지금 당장 수백·수천 개의 클라우드 에이전트를 띄우려고 뛰어들지 마세요** — **토큰을 엄청나게 낭비**하게 되고 **극도로 비쌉니다.**

그리고 클라우드 위임이 왜 배당을 내는지의 설명이 붙는다 — **검증 스킬이 조직 자산이 되기 때문**이다:

> **한 명의 엔지니어를 낫게 하는 게 아니라 팀 전체, 회사 전체를 레벨업**시키기 때문입니다.

사례는 [[grokbot|Benny]] — 버그 리포트를 받아 **클라우드에서 자기 데스크톱을 열고 Cursor를 돌려** 같은 control 스킬로 재현한다. 소스의 예에서 Benny는 **버그를 재현했지만 이미 main에서 고쳐져 있음을 확인**해 주었고, 남은 일은 빌드 릴리스뿐이었다. → [[agent-trust-curve]] · [[agent-verification-skill]]

## References

- [[tech-bridge-cursor-legacy-refactoring]] · [[cursor]] · [[cursor-cloud]]

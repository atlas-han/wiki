---
title: Codex
type: entity
category: product
tags: [openai, coding-agent, gpt, fast-mode]
sources: [openai-nextdoor-codex, tech-bridge-altman-astra-hardware, tech-bridge-altman-agi-superintelligence, tech-bridge-brockman-agi-era-defender-window]
links:
  - https://openai.com/index/nextdoor/
created: 2026-06-27
updated: 2026-09-20
---

# Codex

[[openai|OpenAI]]의 coding agent. [[openai-nextdoor-codex|Nextdoor 케이스 스터디]] 기준 GPT‑5.4/5.5를 기반으로 동작하며, 재현 어려운 버그 조사부터 멀티플랫폼 기능 구축까지 폭넓게 쓰인다. [[claude-code|Claude Code]]에 대응하는 OpenAI 측 에이전트.

## 소스에 나타난 특징 (Nextdoor 사례)

- **재현 어려운 문제 디버깅**: embedded Rust DB, tight race condition, Kubernetes pod 기동 실패 등에서 root cause까지 *persistent*하게 파고듦. 사용자가 *"clean environment and harness for investigation"* 를 제공하는 워크플로.
- **Fast Mode** (Codex + GPT‑5.5): 빠른 피드백 루프 — Nextdoor 팀이 "addicted"라 표현. (참고: [[claude-code]]에도 fast mode 개념 존재.)
- **Outcome 중심 사용**: 스크린샷·영상·성능·테스트 결과를 목표로 빌드 → [[outcome-engineering]] 프레이밍의 도구적 토대.

> ⚠️ 2026 제품·모델이라 스펙은 소스 명시 범위로 한정. 벤치마크 수치는 출처(마케팅)에 없음.

## Altman이 말하는 Codex (2026-09-06 · [[tech-bridge-altman-astra-hardware]])

[[sam-altman|Sam Altman]]의 1인칭 서술이 처음 들어왔다 — ⚠️ 전부 당사자 진술, 수치 없음.

- *"지금은 시장에서 **최고의 코딩 제품**을 만들었다고 생각하고, 엄청나게 빠르게 성장하고 있습니다."* 뒤처졌던 이유는 *"엄청난 소비자 증가세"* 로 코딩이 *"우선순위에서 밀려났기"* 때문 — *"더 나은 모델을 개발하면 따라잡을 수 있을 겁니다."*
- *"제가 아는 대부분의 사람들, 심지어 기존에 [[anthropic|Anthropic]] 제품을 고집하던 사람들까지도 Codex로 갈아탔습니다."* — 개인 표본.
- **The Merge** — ChatGPT와 Codex를 합치는 사내 프로젝트. Altman 본인은 Merge 전 *"ChatGPT를 사용하지 않고 Codex에 채팅 관련 질문을 모두"* 했다. 목표는 *"탭이나 모드를 생각할 필요 없는"* 단일 인터페이스와 **범용 AI 구독**.
- 채팅 제품에 갈 컴퓨팅을 코딩으로 **재배정**했다 — 성장이 컴퓨팅 배분의 함수라는 사례. → [[compute-constrained-growth]]
- [[tech-bridge-altman-agi-superintelligence]]에서 진행자의 예: **우체국 픽업 양식을 Codex에 맡겼다** — 코딩 밖의 일상 작업에 쓰이는 사례.

## References

- [[openai-nextdoor-codex]] · [[openai]]
- 외부: <https://openai.com/index/nextdoor/>
- [[tech-bridge-altman-astra-hardware]] · [[tech-bridge-altman-agi-superintelligence]] — Sam Altman의 서술 (2026-09-06)

## 보안 도구로 쓰인 첫 1인칭 기록, 그리고 대학생 크레딧 (2026-09-20 · [[tech-bridge-brockman-agi-era-defender-window]])

[[greg-brockman|Greg Brockman]]이 **자기 개인 웹사이트를 이 도구로 펜테스트한 일화**를 든다. 이 위키가 이 도구의 구체적 실행 기록을 받는 첫 자리다.

| 단계 | 내용 |
|---|---|
| 지시 | *"[gregbrockman.com]을 확인해서 취약점이 있는지 말해줘"* |
| **발견** | **13건, 15분** — SPF 레코드, HTTPS 미강제 등 |
| **수정** | **45분** — [[cloudflare\|Cloudflare]] 제어판을 직접 클릭해 헤더 설정, **Cloudflare Pages로 마이그레이션**, [DMARC] 절차 개시 |
| **후속** | **48시간 뒤 DMARC 완료를 위한 자동화를 스스로 예약** → [[scheduled-agent-automations]] |
| 자체 확인 | *"이건 고쳐진 걸 확인했습니다"* 를 **요청 없이 자동으로** 수행 (20:10~20:22) |

**컴퓨터 사용 역량이 실제 업무로 이어진 이 위키의 가장 구체적인 서술**이고, [[ai-vulnerability-discovery]]에 **개인 규모 사례**가 붙는다. **발견보다 수정이 세 배 걸렸다**는 것이 [[verification-bottleneck]] 옆에 **교정 병목**을 놓는다.

부수 사실 하나 — **모든 대학생에게 Codex 접근 크레딧을 제공한다고 발표했다**(35:05~35:26).

> ⚠️ **개인 사이트 하나의 일화**다. 통제군·오탐·심각도 분포가 없다. 그리고 **당사자 진술**이다.

→ [[tech-bridge-brockman-agi-era-defender-window]] · [[greg-brockman]] · [[ai-vulnerability-discovery]] · [[defense-factory]]

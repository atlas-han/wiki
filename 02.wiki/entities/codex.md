---
title: Codex
type: entity
category: product
tags: [openai, coding-agent, gpt, fast-mode]
sources: [openai-nextdoor-codex, tech-bridge-altman-astra-hardware, tech-bridge-altman-agi-superintelligence, tech-bridge-brockman-agi-era-defender-window, tech-bridge-lopopolo-agent-harness, tech-bridge-openai-huggingface-incident-black-hat, tech-bridge-agents-vs-humans-optimizer-speedrun, tech-bridge-skill-engineering-dark-arts, tech-bridge-death-of-code-review]
links:
  - https://openai.com/index/nextdoor/
created: 2026-06-27
updated: 2026-10-03
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

## 하네스 무관 스킬의 대상으로, 그리고 에세이 제목으로 (2026-09-23 · [[tech-bridge-lopopolo-agent-harness]])

- [[ryan-lopopolo|Ryan Lopopolo]]의 2026년 2월 에세이가 *"에이전트 우선 환경에서 [Codex] 활용"* 으로 언급된다(02:56; en-orig *codecs*, ko **"코덱"**). ⚠️ 에세이의 게재처는 자막에 없다.
- [[google-skills|Google Skills]]가 호환 하네스로 **Claude Code · Codex · Antigravity** 를 든다(29:39~29:48; en-orig *codeex*, ko *"CodeEx"*).

## 사고 조사 도구로 — 70억 건의 로그 (2026-09-25 · [[tech-bridge-openai-huggingface-incident-black-hat]])

[[openai|OpenAI]]는 [[hugging-face|Hugging Face 사건]]을 조사하며 *"Codex 같은 모델과 다른 에이전트를 돌려 수많은 궤적과 로그를 스캔했다 — 70억 건 이상, 수백만 GPU 시간"*(01:30~01:45). **에이전트 사건을 에이전트로 조사한** 첫 기록이다. ⚠️ Codex의 역할·결과물의 구체는 없다. (ko는 *7 billion logs* 를 **"7000명"** 으로 옮겼다.)

## 장시간 자율 연구 에이전트로 — 쉬지 않는 쪽 (2026-09-28 · [[tech-bridge-agents-vs-humans-optimizer-speedrun]])

[[prime-intellect|Prime Intellect]]가 **GPT-5.5 기반 Codex**를 optimizer speedrun에 풀어 커뮤니티 기록과 경쟁시켰다(05:32~05:37). 같은 판의 [[claude-code|Claude Code]]와 대조된 행동:

- **지속성** — *"Codex totally the opposite. Just worked for all the all the time. And yeah, almost never idle, never asked for question"*(08:04~08:15). Claude Code는 9~10시간마다 포기 선언.
- **scratchpad를 훨씬 많이** 쓰고, 어조는 *"Here is what I do. Here is the decision I take. What I will do next."* — *"super robotic"*(09:10~09:15).
- **서브에이전트·토큰을 훨씬 많이** — 총 약 10억 토큰, 대부분 캐시된 입력(09:23~09:43). **250k 컨텍스트 윈도라 compaction이 잦다**(09:45~09:48) → [[context-resets-and-compaction]].
- 결과는 당시 최고 기록 대비 *"20 step above"*(11:12~11:15, ⚠️ 기준 모호). 6일 실험에선 Kimi가 4일째 Codex를 넘었다(13:04~13:10).

> ⚠️ 활성 워커 수로 정규화했다는 화자 설명(08:39~08:47)뿐, 설정(추론 노력 *"with XAI"* 의 뜻 불명)·반복 실행은 없다. 토큰 소비 방향은 6일 실험에서 뒤집힌다(max mode Claude가 더 씀) — **설정 의존적**. → [[automated-ai-research]]

## 2026-09-28 — 스킬 배포자가 본 Codex의 하네스 동작과 모델 버릇 ([[tech-bridge-skill-engineering-dark-arts]])

[[paul-bakaus]]([[impeccable|Impeccable]])의 관찰(화자 진술, 시점 미확정) → [[cross-harness-skill-compilation]]:

- **서브에이전트는 사용자가 명시적으로 요청해야 쓴다** — *"if you're distributing a skill, you're out of luck"*(12:56~13:10). 우회: 권한이 없으면 멈추고 물으라, 못 쓰면 *"degraded experience"* 라고 말하라 — *"codeex hates that"*(13:13~14:23).
- *"if codeex realizes it can get away with something it will do it"*(13:59~14:03).
- **사용자 질문 도구는 plan mode에서만** — 아니면 질문 없이 추론으로 진행(41:49~42:16).
- **백그라운드 작업이 끝나도 반응하지 않는다** → 라이브 모드는 포그라운드 작업으로 채팅을 막는다(43:00~43:31).
- **데스크톱 앱의 인앱 브라우저**를 라이브 모드가 쓴다(35:04~35:12).
- **모델 버릇(디자인)** — 나쁜 자간, 과하게 둥근 모서리, hairline border(44:17~44:36). Codex/GPT는 **"gate"라는 단어를 좋아하고** 지시를 압축한다 → Codex에만 로드되는 8-gate MD(47:16~48:16).
- **플러그인 마켓플레이스**가 배포 경로로 있다(1:02:25~1:02:30).

## 자기 리뷰 루프 — "리뷰를 리뷰하는 에이전트" (2026-10-03 · [[tech-bridge-death-of-code-review]])

[[laurie-voss|Laurie Voss]]가 [[openai|OpenAI]] 2월 글을 요약(2차 인용): *"codeex[=Codex] reviews its own changes uh then calls in more agents to review those reviews um in a loop until every agent reviewer is satisfied"*(17:23~17:34). 변경마다 Codex를 **부팅 가능**하게 해 Codex가 Codex 사본을 띄워 UI를 보고 버그 수정을 확인하고, **로깅 스택 전체**를 에이전트에 노출했다(17:34~17:48). → [[automated-code-review]] · [[agent-visual-qa]]

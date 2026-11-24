---
title: Google Antigravity
type: entity
category: product
tags: [google, coding-agent, harness, ide, orchestration, subagents]
aliases: [Antigravity, 안티그래비티, Antigravity Boost, "/boost", Antigravity CLI]
links:
  - https://g.dev/cloud/antigravity-homepage
sources: [tech-bridge-lopopolo-agent-harness, tech-bridge-flutter-ai-workflow, tech-bridge-build-time-vs-runtime-tools, tech-bridge-melvin-johnson-gemini-4-post-training-evidence-fabrication, tech-bridge-theo-gemini-4-neon-capability-vs-coherency]
created: 2026-09-23
updated: 2026-11-24
---

# Google Antigravity

**Google의 코딩 에이전트 하네스.** 이 위키에서는 [[claude-code|Claude Code]]·[[cursor|Cursor]]와 나란히 *"현재 가장 인기 있는 에이전트 하네스"*(24:24~24:28) 중 하나로 불린다 — [[tech-bridge-lopopolo-agent-harness]].

> 예를 들어, **제미니 플래시가 모델이고 구글 [Antigravity]가 하네스**인 것처럼 말이죠. (00:52~00:58)

> ⚠️ **이름이 ko 자막에서 거의 매번 깨진다** — *"구글 반중력 장치"*(00:55) · *"반중력 도구"*(27:18) · *"반중력 환경"*(28:16) · **"Google Integrity"**(24:26, en-orig *integravity*) · *"다시 **무중력 상태로** 돌아갈"*(30:23). 09-02 Flutter 편은 en-orig *"anti-gravity"* 로 적었다.
>
> ⚠️ **이 페이지의 기능 설명은 전부 Google 측 당사자 진술이다.** 수치 없음.

## 위키에서 알려진 사실

- **2026-09-02** · [[tech-bridge-flutter-ai-workflow]] — 3대 병렬 기계(Claude · Codex · Antigravity)가 서로 업무를 인계. 1회 언급.
- **2026-09-11** · [[tech-bridge-build-time-vs-runtime-tools]] — [[google-cloud|Google Cloud]] 발표자가 자사 에이전트·하네스로 Gemini CLI와 함께 *"Antigravity CLI"* 를 언급.
- **2026-09-23** · [[tech-bridge-lopopolo-agent-harness]] — 처음으로 **기능이 설명된다.**

## `/boost` — 단일 모델을 팀으로

> **boost는 단일 모델을 조직적인 팀으로 변환하는 슬래시 명령어입니다.** (27:20~27:25)

- **오케스트레이터**를 띄우고 → **전문화된 하위 에이전트를 병렬로 위임** → **코드베이스에 닿기 전 독립 검증 패스**로 감사(27:25~27:44).
- **일상 작업에는 쓰지 말라** — 표준 기능·UI 컴포넌트·코드베이스 탐색은 기본 에이전트가 *"빠르고 효율적"*, Boost는 *"매우 복잡한 엔지니어링 문제"* 에(27:46~28:03).
- Antigravity에 **실행 모드가 셋** 있고 Boost가 그중 하나 — ⚠️ **비교 표는 화면에만 있고 읽히지 않는다**(28:11~28:30).

→ [[generator-evaluator-pattern]](독립 검증) + [[orchestrator-searcher-split]](오케스트레이터·병렬 위임)의 제품화. [[model-harness-knowledge-stack]]의 **하네스 층**.

## Lopopolo에게는 "고정값"

[[ryan-lopopolo|Ryan Lopopolo]]는 Antigravity를 **만지지 않는 것**의 예로 든다 — *"당신의 에이전트 시스템에서 [Antigravity]와 같은 요소를 항상 고정된 상태로 유지해 왔습니다"*(14:52~14:59). → [[tools-and-context-over-harness]]. **같은 회사 사람이 자사 하네스를 "신경 쓰지 말 대상"으로 소개하는 셈**이다.

## ⚠️ 유보

- **Boost의 비용·속도·품질 수치 없음.** *"아껴 쓰라"* 는 지침이 비용 차이를 암시하지만 말하지 않는다.
- **[[claude-code|Claude Code]]·[[cursor|Cursor]]와 무엇이 다른지** — 에피소드가 *"어떤 용도에 가장 적합한 것일까요?"*(24:30~24:37)를 묻고 답하지 않는다.
- 권한·샌드박스·보안 모델 — 언급 없음.

## References

- [[tech-bridge-lopopolo-agent-harness]] · [[tech-bridge-flutter-ai-workflow]] · [[tech-bridge-build-time-vs-runtime-tools]]
- [[google-cloud]] · [[google-skills]] · [[ryan-lopopolo]]
- 관련: [[model-harness-knowledge-stack]] · [[tools-and-context-over-harness]] · [[harness-engineering]] · [[claude-code]] · [[cursor]] · [[codex]]

## 2026-11-23 — 알파벳 안의 사용 규모 ([[tech-bridge-melvin-johnson-gemini-4-post-training-evidence-fabrication]])

[[google-deepmind|Google DeepMind]]의 [[melvin-johnson|Melvin Johnson]] 발표를 옮긴 한국어 해설에서: *"알파벳 안에서 안티 그래비티로 개발하는 사람은 매년 10만 명이 넘습니다."*(02:33~02:36)[=Antigravity] 같은 대목에 *"지금 구글 새 코드의 75%를 AI가 씁니다."*(02:24~02:26)가 붙는다(엔지니어가 검토하고 승인한 코드 기준). 이 사내 사용자들이 새 후보 모델의 시험장이다 → [[gemini-4]] · [[production-trace-eval-flywheel]]

⚠️ *매년* 은 ASR 글자 그대로다(영어 더빙 ASR도 *every year*) — 단위가 맞는지 확인하지 못했다. 해설 전달, 자기 보고.

## 2026-11-24 — 바깥 사용자의 화면에서: Neon을 싣는 통로와 연결부 버그 ([[tech-bridge-theo-gemini-4-neon-capability-vs-coherency]])

[[theo|Theo]]의 [[gemini-4|Gemini 4 Neon]] 사용기(한국어 해설 전달)에서 Antigravity는 Neon을 T3 Code에 붙이는 통로로 나온다.

- 설치: *"네온은 8분 동안 그 PC에 접속해 안티 그래비티를 깔고 T3 코드에 붙인 뒤 직접 확인했습니다."*(04:01~04:06)
- 연결부 버그: Neon이 멈춘 것처럼 보였는데 *"대시보드는 이미 두 개 만들었는데 안티 그래비티 연결부에서 채팅이 안 보이고 있었다고요."*(04:36~04:41) 수정 PR은 *"36개 패키지 검사와 테스트 153개를 통과한 수정을 올렸습니다."*(05:18~05:20) ⚠️ 버그가 Antigravity 쪽인지 T3 Code의 연결 코드 쪽인지는 캡션으로 가릴 수 없다(PR은 T3 Code 저장소 일을 하던 중에 나왔다).
- 스킬: 스킬 이름을 대충 부르자 실행하지 않고 멈췄다 — Theo는 모델 탓인지 Antigravity 탓인지 모르겠다고 했다.
- 속도: *"구글 쪽에서 확인되는 건 안티그래비티에서 카본의 첫 응답이 1.5배 빨라졌다는 언급 정도입니다."*(02:27~02:30)

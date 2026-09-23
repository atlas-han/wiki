---
title: Google Skills
type: entity
category: tool
tags: [google, agent-skills, skills-repository, google-cloud, firebase, flutter, harness-agnostic]
aliases: [Google Skills 저장소, 구글 스킬, Google Cloud skills]
links:
  - https://goo.gle/3UN4MWQ
sources: [tech-bridge-lopopolo-agent-harness]
created: 2026-09-23
updated: 2026-09-23
---

# Google Skills

**Google이 자사 플랫폼(Google Cloud · Firebase · Flutter · Maps 등)의 도메인 지식을 [[agent-skills|에이전트 스킬]]로 묶어 GitHub에 공개한 저장소.** [[tech-bridge-lopopolo-agent-harness]] 3부에서 [[model-harness-knowledge-stack|3계층 스택]]의 **지식 층**으로 소개된다.

> **스킬은 코딩 에이전트가 필요에 따라 불러오는, 엄선된 도메인 지식입니다.** 그러니까 **이건 단순한 MCP 서버가 아니라는 거죠. [무거운 플러그인도 아닙니다.]** 이는 [에이전트]에게 **명확하고 정확한 맥락을 제공하여 [에이전트]가 추측할 필요 없이** 실제로 어떻게 해야 하는지 알 수 있도록 해줍니다. (29:04~29:23)

> ⚠️ **제품명이 ko에서 사라진다** — *"That's exactly where Google skills comes in"* → **"바로 이런 부분에서 구글의 기술력이 빛을 발합니다"**(28:47~28:49). *"over 100 different skills"* → *"100가지가 넘는 **기술**"*(29:28). 그리고 *"It is **not** a heavy plug-in"* → **"이 플러그인은 용량이 크지 않습니다"**(29:12~29:14)로 **범주 부정이 긍정으로 뒤집혔다.**

## 소스가 말한 것 (전부 당사자 진술)

- **GitHub 별 19,000개 돌파**, *"아직 초기 단계이고 활발하게 발전"*(28:53~28:58).
- **100+ 스킬** — Google Cloud · Firebase · Flutter · Maps 등(29:23~29:32).
- **명령어 하나로 전부 설치**(29:34~29:39).
- ⭐ **하네스 무관** — *"[Claude Code], [Codex], Google [Antigravity] 등 어떤 하네스를 사용하든 완전히 호환"*(29:39~29:48).

## 위키에서의 좌표

- **[[agent-skills]]의 벤더 유통판** — 09-08 *플러그인이 스킬의 유통 경로가 된다*, 09-02 [[tech-bridge-flutter-ai-workflow|Flutter 편]]의 *"우리 팀원이 공식 스킬을 썼다"*(Google 측 공식 스킬 저장소, 1회 언급)의 **실체**로 보인다 — ⚠️ **같은 저장소인지는 확인하지 않았다.**
- **스킬 vs [[model-context-protocol|MCP]] vs 플러그인의 경계를 벤더가 직접 긋는 문장**이 있다(29:12~29:14). 이 위키의 [[agent-skills]]는 이 경계를 여러 소스에서 모아 왔다.
- [[ryan-lopopolo|Lopopolo]]의 [[tools-and-context-over-harness]]와 맞물린다 — 하네스가 바뀌어도 따라오는 **컨텍스트**의 한 형태.

## ⚠️ 유보

- **품질 근거가 스타 수뿐이다.** 스킬이 에이전트 성능을 얼마나 바꾸는지 측정 없음.
- **공급망** — *명령 하나로 100+ 외부 스킬 설치*를 권하면서 검토·버전 고정·신뢰 이야기가 없다. 스킬은 에이전트 컨텍스트에 직접 들어가는 텍스트이므로 [[prompt-injection]]의 표면이 된다.
- 설명란 링크는 `goo.gle` 단축 URL이고 **이 위키는 저장소 이름·경로를 확인하지 않았다.**

## References

- [[tech-bridge-lopopolo-agent-harness]]
- [[agent-skills]] · [[model-harness-knowledge-stack]] · [[google-cloud]] · [[antigravity]] · [[flutter]]

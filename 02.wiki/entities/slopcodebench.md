---
title: SlopCodeBench
type: entity
category: tool
tags: [benchmark, coding-agents, maintainability, ai-slop, long-horizon, iterative]
aliases: [Slop Code Bench, SlopCode-Bench]
sources: [tech-bridge-horthy-state-of-software-factory]
links:
  - "https://arxiv.org/abs/2603.24755"
  - "https://snorkel.ai/leaderboard/slopcode-bench/"
created: 2026-10-16
updated: 2026-10-16
---

# SlopCodeBench

**문제를 한 번에 주지 않고 조금씩 공개하며 기능을 덧붙이게 해, 모델이 시간이 지나며 코드베이스를 어떻게 망가뜨리는지 재는 코딩 벤치마크.** 이 위키에는 [[dex-horthy|Dex Horthy]]의 인용으로 첫 등장([[tech-bridge-horthy-state-of-software-factory]]). ⚠️ 논문·리더보드(설명란 링크)는 **열어 보지 않았다** — 아래는 전부 화자 진술.

## 화자가 말한 것

- 출처: *"published out of a lab in the University of Wisconsin, uh, in the US"*(06:27~06:30). ⚠️ 설명란 리더보드는 snorkel.ai — **Snorkel과의 관계는 발화되지 않는다.**
- 설계: *"instead of telling the model the whole problem to solve up front, it gives the model the challenges. It discloses like parts of the challenge in bits and makes it write the code and then do another feature and then do another feature. Which maps much more closely to how everyone in this room builds software."*(06:33~06:47)
- 점수: *"when they launched this, GPT-5.5 was the best model on the market. It got a 14.8%."*(06:53~06:59) ⚠️ 지표 정의 미발화. 이후 *"Astra is one percentage point or 1.5% percentage points higher than GPT-5.5"*(08:46~08:51 — 문맥상 이 벤치마크, 1 vs 1.5 미확정) → [[openai-astra]]
- 포화된 벤치마크와 대비: *"when you see terminal bench scores and everyone's getting 95% (…) a benchmark that is full very much unsaturated."*(06:59~07:12) → [[terminal-bench]]
- 벤치마크 제작자가 Anthropic 포스트모템(쌓인 messy code → 보안 문제, 화자 요약)에 *"there was a benchmark that would prove that models create sloppy code over time"* 이라고 지적했다(07:26~07:31).
- 논문에 *"a bunch of stuff (…) that you can steal"*(11:42~11:45) — anti-slop 규칙 재료로.

## 위키에서의 자리

- [[ai-slop]] — 슬롭을 **누적 현상**으로 재는 첫 벤치마크(이 위키 기준). [[tech-bridge-taste-labs-measuring-slop|Taste Labs]]의 디자인 슬롭 측정과 축이 다르다(코드·시간축).
- [[verifiable-goals]] — *"maintainability has no fast oracle"*(06:13~06:15)를 벤치마크 설계(점진 공개)로 우회하려는 시도로 읽을 수 있다(위키의 해석).

## 미해결

- 지표 정의, 과제 수, 리더보드 현황, 저자·기관(Wisconsin vs Snorkel). 논문 ingest 필요.

## References

- [[tech-bridge-horthy-state-of-software-factory]]
- [SlopCodeBench (arXiv 2603.24755)](https://arxiv.org/abs/2603.24755) (⚠️ 미확인)

---
title: SlopCodeBench
type: entity
category: tool
tags: [benchmark, coding-agents, maintainability, ai-slop, long-horizon, iterative]
aliases: [Slop Code Bench, SlopCode-Bench]
sources: [tech-bridge-horthy-state-of-software-factory, tech-bridge-dex-horthy-twelve-rules-no-slop-factory]
links:
  - "https://arxiv.org/abs/2603.24755"
  - "https://snorkel.ai/leaderboard/slopcode-bench/"
created: 2026-10-16
updated: 2026-11-26
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

## 2026-11-26 — 과제 수 · 엄격 기준 · 새 1등 16.33% ([[tech-bridge-dex-horthy-twelve-rules-no-slop-factory]])

[[dex-horthy|Dex Horthy]]의 Code Summit 발표 해설이 이 페이지 *미해결* 의 일부를 채운다(⚠️ 한국어 내레이션의 전달 — 논문 · 리더보드는 여전히 미열람).

- 규모: *"문제 36개를 체크포인트 196개로 쪼갰습니다."*(03:44~03:49)
- 진행과 채점: *"첫 명세로 프로그램을 짜고 명세가 바뀔 때마다 자기 코드를 고쳐 나갑니다. 숨은 테스트로 채점하고 슬롭이 얼마나 쌓였는지도 봅니다."*(03:50~03:56)
- ⭐ **지표 정의**(10-15에는 미발화였다): *"엄격 기준은 앞선 체크포인트의 테스트까지 전부 통과해야 점수를 줍니다."*(03:58~04:02)
- 점수: *"그 기준으로 1등인 GPT-6 아스트라 엑스 하이가 16.33% 196개 중 서른 두개였습니다."*(04:02~04:08) 설명란도 *16.33%(196개 중 32개)*. 10-15의 GPT-5.5 14.8% · *Astra는 1~1.5%p 높다* 와 맞는 범위다. ⚠️ *엑스 하이* 가 가리키는 설정 이름은 정하지 않았다. → [[openai-astra]]
- 벤치를 이끄는 사람으로 **Gabe Orlanski** 가 이름으로 나온다(설명란 글 *Slop Is Moving Up the Stack*, 미열람). 그의 정리로 전해진 말: *"슬롭은 사라진 게 아니라 설계 결정으로 자리를 옮겼다."*(04:14~04:16)
- 라이브러리 실험: 같은 구현 에이전트에게 라이브러리를 주면 *"라이브러리를 피해 우회하는 비율이 사람이 짠 라이브러리에선 27%, 에이전트가 짠 라이브러리에선 40%였습니다."*(04:22~04:28) ⚠️ 실험 조건 · 표본은 캡션에 없다.
- Horthy 원음(en-orig 단일 트랙) — 무엇을 재는가: *"this is a benchmark that measures a model's ability to evolve a code base over time."*(03:36~03:40) 한 번에 문제 전체를 아는 과제와의 대비: *"that requires knowing the entire problem in advance. And most of us don't write software that way."*(03:21~03:25)
- 규칙 재료: 벤치의 Python 품질 규칙을 가져다 쓸 수 있다고 한다(내레이션 07:20~07:24).

남은 미해결: Snorkel과의 관계 · 통과율로 보이는 다른 지표(ASR *프리율*, 판독하지 못함) · 리더보드의 나머지 순위.

---
title: Laurie Voss
type: entity
category: person
tags: [arize-ai, npm, developer-relations, code-review, evals]
aliases: [Laurie, Lori, 로리 보스, seldo]
links:
  - https://x.com/seldo
  - https://bsky.app/profile/seldo.com
  - https://github.com/seldo
sources: [tech-bridge-death-of-code-review]
created: 2026-10-03
updated: 2026-10-03
---

# Laurie Voss

[[arize-ai|Arize AI]]의 developer relations 책임자, npm Inc. 공동 창업자. [[tech-bridge-death-of-code-review]]에서 **에이전트 시대 코드 리뷰의 산업 현황**을 정리했다 — 자기 실험이 아니라 연구·벤더 발표·사례를 엮은 서베이. 본 위키 첫 등장.

> ⚠️ **이름·소속 표기.** en-orig 자기소개 *"I'm Lori. I'm head of developer relations at Arise AI. Uh some of you may remember me from when I used to co-ound npm Inc. These days I think about AI and how to test it."*(00:15~00:25). `en`은 *"Laurie"*·*"Director of Developer Relations"*. **성 "Voss"와 링크(`seldo`)는 설명란에만 있다** — 이 페이지는 설명란 표기를 따른다. 회사는 세 트랙 모두 *"Arise"* 로 들리나 설명란 링크(arize.com)를 따른다.

## 발표에서 (자막 근거)

- 문제: 에이전트를 켠 개발자는 코드 741%↑, 출시 소프트웨어 30%↑ — 병목은 리뷰(01:22~01:54) → [[verification-bottleneck]]
- 테스트 통과 ≠ 머지 가능 — METR·FrontierCode, *"whoever writes today's review standard is writing next year's default model behavior"*(10:07~10:09) → [[mergeability-gap]]
- 자동 리뷰의 현장과 교훈 — 다중 패스, *"suspicious by default"*, 사람 수락률 지표, 프롬프트 인젝션 → [[automated-code-review]]
- 결론: *"code review isn't completely dead (…) it is being rebuilt as an engineered system"*(22:35~22:41), *"stop reviewing PRs"*(23:19~23:21), 리뷰 하네스를 지어라

## 태도

**다른 사람의 대담한 주장을 근거 수준으로 깎는다.** OpenAI의 무인 코딩 제품엔 *"they did not tell us what the product did (…) which suggests to me that there are still holes in that strategy"*(05:43~05:55), 에이전트 열두 개를 동시에 돌리는 사람에겐 *"I'm tend to be suspicious of the people who do"*(04:21~04:25), Dex Horthy의 철회엔 *"That is not a benchmark. That is somebody who ran this experiment for real"*(18:56~19:00). 그러나 그 자신의 수치도 대부분 2차 인용이고, 두 곳의 산수(*"51 points"*, *"three orders of magnitude"*)가 맞지 않는다.

> ⚠️ 소속 회사(Arize)는 LLM 관측·평가 플랫폼으로 알려져 있고, 결론 *"production … the last reviewer standing"*(21:48~22:00)은 그 시장과 겹친다. 화자는 *"I'm not going to give a pitch for Arise here"*(22:13~22:15)라고 선을 그었다.

## References

- [[tech-bridge-death-of-code-review]] · [[arize-ai]]
- 설명란: <https://x.com/seldo> · <https://github.com/seldo> (⚠️ 열어 보지 않았다)

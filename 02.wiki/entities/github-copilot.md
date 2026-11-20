---
title: GitHub Copilot
type: entity
category: product
tags: [github, microsoft, coding-agent, ide, copilot, rust-migration]
aliases: [깃허브 코파일럿, Copilot (GitHub), GitHub Copilot runtime]
links: []
sources: [tech-bridge-nadella-pragmatic-engineer-after-code-is-cheap]
created: 2026-11-20
updated: 2026-11-20
---

# GitHub Copilot

[[microsoft|Microsoft]] 산하 GitHub의 AI 코딩 도구. 위키에는 오랫동안 **다른 소스의 배경**(SDD 발표의 실행 도구 · Token Economizer의 시험 대상 다섯 가운데 하나)으로만 나왔고, CEO [[satya-nadella|Satya Nadella]]의 The Pragmatic Engineer 인터뷰를 따라간 해설([[tech-bridge-nadella-pragmatic-engineer-after-code-is-cheap]])에서 처음으로 이야기의 한 축이 되어 페이지를 만들었다. Microsoft 365 쪽 제품군인 [[microsoft-copilot]](chat · co-work · code · Autopilot)과는 다른 페이지다.

> ⚠️ 아래는 전부 **한국어 해설의 전달** 이다. 위키는 원 인터뷰도 GitHub 블로그 글도 열지 않았다.

## 소스에서 확인되는 것

- **먼저 나왔다** — 진행자 Gergely Orosz가 Microsoft가 누구보다 빨랐다고 짚는 근거: *"챗 GPT보다 먼저 깃허브 코파일럿을 내놨으니까요."*(00:43~00:45)
- **그리고 밀렸다** — *"커서가 나온 뒤에도 코파일럿은 나란히 달렸습니다. 그런데 2025년 클로드 코드가 나옵니다."*(00:48~00:52) IDE 안의 보조에서 터미널에 일을 통째로 맡기는 형태로 무게중심이 옮겨 갔다는 것이 이 인터뷰의 출발점이다. → [[claude-code]] · [[cursor]]
- ⭐ **런타임의 Rust 이전** — Nadella가 [[software-factory|소프트웨어 팩토리]]의 예로 가리킨 블로그 두 편 가운데 하나(설명란: Stephen Toub의 글). *"80만 줄이 넘는 러스트 코드를 주로 개발자 한 명이 몇 달 만에 옮겼다고 적었습니다."*(04:00~04:05) 혼자만의 일은 아니었다는 단서가 붙는다. 원래 언어는 TypeScript다 — *"사티아는 파이선이라 했지만 원래는 타입스크립트였습니다."*(03:58~04:00)(해설이 공식 글로 바로잡은 곳) → [[rust]]
- **플랫폼 쪽의 부하** — *"깃허브 옥토버스 보고서로는 9월에 풀 리퀘스트의 40% 넘게가 에이전트 초안에서 시작했습니다. 3월에 17%였고요."*(07:08~07:14) 이 수치는 Copilot만이 아니라 GitHub 전체의 것이다. Nadella는 GitHub가 *"공장 밑바닥까지 다시 깔고 있다"* 고 말한다(해설 전달).
- **세대** — Nadella는 작년 GitHub Universe에서 *Copilot 이전의 IDE를 모르고 자란 첫 졸업생들* 을 만났다고 한다.

## ⚠️ 구분해 둘 것

- **Copilot Cowork는 다른 팀이다.** 엔지니어 9명이 하루 PR 1,211개를 머지했고 Python → Rust 이전의 첫 시도를 되돌렸다는 것은 Copilot Cowork 팀(Bas Brekelmans의 글)의 이야기다. Nadella가 인터뷰에서 롤백을 GitHub Copilot 런타임 쪽으로 기억한 것을 해설이 바로잡았다.
- 사용자 수 · 매출 · 점유율 수치는 이 소스에 없다.

## References

- [[tech-bridge-nadella-pragmatic-engineer-after-code-is-cheap]] — 첫 서술 소스
- [[microsoft]] · [[satya-nadella]] · [[microsoft-copilot]] · [[claude-code]] · [[cursor]]

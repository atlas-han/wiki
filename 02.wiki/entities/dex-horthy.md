---
title: Dex Horthy
type: entity
category: person
tags: [humanlayer, founder, coding-agents, software-factory, context-engineering, 12-factor-agents]
aliases: [Dex, Dexter Horthy, 덱스 호시]
sources: [tech-bridge-horthy-state-of-software-factory, tech-bridge-death-of-code-review, tech-bridge-pocock-21k-lines-questions-before-code, tech-bridge-dex-horthy-twelve-rules-no-slop-factory]
links:
  - "https://humanlayer.dev/resources"
created: 2026-10-16
updated: 2026-11-26
---

# Dex Horthy

[[humanlayer|HumanLayer]]의 CEO·공동 창업자. 코딩 에이전트·12-factor agents·context engineering에 관해 발표·영상을 많이 낸 사람이다(*"I yap about coding agents on YouTube a lot. I think we have over like a million views, probably 1.5 now."* — [[tech-bridge-horthy-state-of-software-factory]] 00:33~00:40).

> ⚠️ **이름의 출처.** 직함·회사는 발화된다(*"Uh I am the CEO and co-founder of a company called HumanLayer."* 00:49~00:53). 이름은 *"I'm Dex."*(15:44)까지만 발화 — **성 Horthy는 제목·설명란에만**. [[tech-bridge-death-of-code-review]]에서 Laurie Voss가 en-orig *"Dexter Horthy"* 로 부른 인물(챕터 표기 *"덱스 호시"*)과 이름·주제가 겹쳐 동일인으로 읽는다.

## 위키에서 알려진 사실

- **철회(제3자 인용)** — Voss에 따르면 6개월간 "코드를 읽지 말라"고 했다가 무대에서 철회: *"I was wrong. Please please read the code. We tried not reading the code for like six months. It did not end well."*([[tech-bridge-death-of-code-review]] 18:46~18:56). ⚠️ 본인 발표([[tech-bridge-horthy-state-of-software-factory]])에선 이 철회를 직접 말하지 않는다.
- **본인 테제(2026-10-14 업로드)** — *"unattended models will not improve or maintain your code base quality over time."*(05:17~05:23) → *"for now we should probably read the code"*(09:03~09:07). 근거: *"maintainability has no fast oracle"*(06:13~06:15), SlopCodeBench([[slopcodebench]]).
- **처방** — "12 factor factories"(임시 이름, 실제 9개): 계획 먼저([[expected-pain-planning]]), 시각적 정렬(show me 스킬), 에이전트 자기 테스트·사용자 실험([[back-pressure]]), anti-slop 규칙, 피드백·인시던트 → 에이전트 PR, 세션에서 compound.
- **도구 관점** — 세션·계획·프롬프트의 system of record와 네 층([[agent-platform-layers]]). HumanLayer는 control plane.
- 시점 단서: *"this talk from June"*(05:48~05:51)에서 RL과 벤치마크 인센티브를 직관적으로 설명했다고 말한다(행사 미발화).

## 위키에서의 좌표

- lights-off/dark factory 반론 쪽: [[kent-beck|Kent Beck]]과 같은 편, [[lauren-tan|Lauren Tan]]의 *"It kind of is"* 와 반대 → [[software-factory]]
- [[verification-bottleneck]] — *PR을 기다리지 않는 리뷰*(diff 스트리밍)

## References

- [[tech-bridge-horthy-state-of-software-factory]] · [[tech-bridge-death-of-code-review]] · [[humanlayer]]

## 2026-11-22 — *스마트 존, 덤 존* 의 출처로 지목됨 (추정 판독, [[tech-bridge-pocock-21k-lines-questions-before-code]])

[[matt-pocock|Matt Pocock]]의 작업 영상 해설: *"덱소 씨가 처음 꺼낸 스마트 존, 덤 존 이야기입니다."*(06:39~06:41) ⚠️ **ASR *덱소 씨* 를 Dex Horthy로 읽은 것은 추정이다** — 영어 더빙 ASR은 *Dexo*, 성은 어느 캡션에도 없고 Pocock의 원음은 무캡션이다. 내용은 *"대화가 15만 토큰쯤 넘어가면 에이전트가 조금씩 둔해진다는 주장입니다."*(06:42~06:45) → [[context-rot]]. 이 위키의 Horthy 본인 소스에는 이 용어가 아직 없다 — 본인 발화로 확인되면 이 절의 추정 표시를 닫는다.

## 2026-11-26 — 두 번째 본인 발표: 규칙 12가지 · 안티 슬롭 선언 · 소속 변경 ([[tech-bridge-dex-horthy-twelve-rules-no-slop-factory]])

[[ai-engineer|AI Engineer]] Code Summit 발표의 한국어 해설(2026-11-25 업로드). ⚠️ 본인 원음은 en-orig 한 트랙에만 조각으로 잡혔고(아홉 곳, 교차 확인 없음) 나머지는 한국어 내레이션의 전달이다.

- **소속이 바뀌었다.** *"휴먼 레이어를 공동 창업했고 최근 팩토리에 합류했습니다."*(00:28~00:32)[=HumanLayer · Factory] 설명란 표기는 *Dex Horthy(Factory, 전 HumanLayer CEO)*. 이 페이지 머리의 *HumanLayer의 CEO · 공동 창업자* 는 10-14 업로드 시점의 자기소개다. 합류 시점과 [[humanlayer|HumanLayer]]의 그 뒤는 소스에 없다. → [[factory-ai]]
- **딱지를 받아넘긴다**(원음): *"Dex is the anti-software factory guy. Dex hates software factories. I actually love software factories. I'm a huge fan"*(00:57~01:02) 내레이션에 따르면 지난 6월 발표의 제목이 *소프트웨어 공장이 왜 실패하는가* 였고, 본인 풀이는 *"there are certain things you could do in your software factory that would cause it to fail."*(01:06~01:11) — 이 페이지의 *lights-off 반론 쪽* 좌표는 공장 반대가 아니라 **감독 없는 공장** 반대로 읽어야 한다.
- **목록이 열둘이 됐다.** 10-15 소스에서 아홉 개였던 *12 factor factories* 가 번호 열두 개로 채워졌다: 루프 · 적을 알라 · 계획하라 · 과하게 계획하지 말라 · 눈으로 맞춰 보라 · 직접 시험하게 하라 · 결정론적 도구 · 슬롭도 도구다 · 실험하게 하라 · 쌓이게 하라 · 포지를 하나로 · 전부 살 수는 없다. ⚠️ 번호는 내레이션의 것.
- ⭐ **검증은 살 수 없다**(원음): *"Don't think anyone can sell you verification of your code."*(08:36~08:37) *"Not just a black box you can buy."*(08:47)
- **선언을 공개했다.** *"이 무대에서 덱스는 안티 슬롭 선언을 공개했습니다."*(09:03~09:05) → [[no-ai-slop-manifesto]](신규). 슬롭을 받았을 때 친절하게 말해 주라는 다짐에 이어 *"덱스는 자기도 그런 말을 들어본 적이 있다고 털어놨습니다."*(10:40~10:42)
- **자리 나누기.** *"검토하지 않은 출력이 다 나쁜 것도 아닙니다."*(11:28~11:29) — 10-15의 *for now we should probably read the code* 에 단서가 붙었다. 다만 에이전트 리뷰어 · 린터 · 검증기에 대해서는 원음 조각이 *"they are not sufficient."*(11:12) 라고 한다(이유는 무캡션).

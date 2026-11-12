---
title: "워터폴 모델 (Waterfall Model) — Royce 1970 논문이 실제로 말한 것"
type: concept
category: pattern
tags: [waterfall, software-engineering-history, winston-royce, agile, spec-driven-development, sdlc]
aliases: [waterfall, 워터폴, 폭포수, 폭포수 모델, waterfall development, Royce 1970, Managing the Development of Large Software Systems]
related: [spec-driven-development, ai-unified-process, verifiable-goals, executable-standards]
first-seen: tech-bridge-sdd-vs-waterfall
sources: [tech-bridge-sdd-vs-waterfall, tech-bridge-kent-beck-craft-augmented-development]
created: 2026-11-12
updated: 2026-11-12
---

# 워터폴 모델 (Waterfall Model)

**요구 사항 → 설계 → 구현 → 테스트 → 운영을 계단처럼 한 단계씩 끝내고 내려가는 개발 방식.** 이 위키에서는 주로 [[spec-driven-development]]에 대한 *"그건 폭포수다"* 비판의 기준점으로 쓰인다. 이 페이지는 **원조로 불리는 Winston Royce의 1970년 논문이 그 모양을 권하지 않았다** 는 서술을 모은다.

> ⚠️ **위키는 Royce 논문 · Bell & Thayer(1976)를 열지 않았다.** 아래 논문 내용은 [[tech-bridge-sdd-vs-waterfall]]의 한국어 해설과 [[kent-beck|Kent Beck]]의 강연 기억이다.

## 계단의 문제 (해설)

- 한 단계가 끝나야 다음이 시작되고, 스펙은 맨 위에서 *팀에서 팀으로* 넘어간다. 틀린 요구 사항을 늦게 알면 계단을 거슬러 올라가야 하고, 제대로 만들었는지는 맨 끝 테스트에서야 안다.
- 보안 · 규정 문제도 테스트 단계에서야 드러난다(같은 소스 8절).

## 논문이 실제로 말한 것 (해설 전달)

| 서술 | 출처(해설) |
|---|---|
| 그림 바로 아래 첫 문장 — *"이 방식은 위험하고 실패 부른다."*(00:13~00:16) | Royce 1970 |
| 테스트 → 설계 → 요구 사항으로 되돌아가는 화살표, *설계의 반복은 이웃한 단계 안에서 끝나지 않는다* (01:51~02:01) | Royce 1970 |
| 본문에 *waterfall* 이라는 단어가 없다. 이름은 6년 뒤 다른 논문이 *Royce가 폭포 개념을 소개했다* 고 쓰면서 붙었다(02:11~02:20) | Bell & Thayer 1976(설명란) |
| 해법 — *"세 번째 단계 두 번 하라."*(07:55~07:58) 고객에게 가는 것이 사실상 두 번째 버전이 되게, 첫 결과는 최종 제품의 이른 시뮬레이션으로 | Royce 1970 |

- [[kent-beck|Kent Beck]](10-09)도 같은 방향을 기억으로 말했다: 폭포수 그림 다음 페이지에는 *"waterfall going down and feedback coming up"* — [[tech-bridge-kent-beck-craft-augmented-development]]. 두 소스가 일치하지만 둘 다 2차다.

## 왜 SDD 논쟁에서 중요한가

- *스펙 먼저* 는 워터폴의 겉모양과 같다. 해설 · IBM의 구분선은 **스펙으로 돌아가느냐** 다 — 통째로 쓰고 얼려서 넘기면 *"이름만 바뀐 워터"*, 코드 옆에 두고 고치면 고리(→ [[spec-driven-development]]).
- 역설: 반대론자가 기준으로 삼는 *워터폴* 은 원 논문이 *위험하다* 고 쓴 그림이고, 원 논문의 처방(두 번 하라 · 되먹임)은 오히려 SDD 옹호론의 *고리* 쪽에 가깝다(해설의 결론, 위키는 원문 미대조).

## References

- [[tech-bridge-sdd-vs-waterfall]] — 2026-11-11 한국어 해설
- [[tech-bridge-kent-beck-craft-augmented-development]] — Kent Beck의 기억
- Winston W. Royce, "Managing the Development of Large Software Systems"(1970) · Bell & Thayer, "Software Requirements: Are They Really a Problem?"(1976) — 위키 미열람

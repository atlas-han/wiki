---
title: Frontier Engineering
type: concept
category: pattern
tags: [agent, organization, kiro, amazon, habits]
related: [agent-org-adoption, harness-engineering, spec-driven-development, verifiable-goals, agent-harness-design]
first-seen: tech-bridge-frontier-engineering
sources: [tech-bridge-frontier-engineering]
created: 2026-08-30
updated: 2026-08-30
---

# Frontier Engineering

코딩 어시스턴트를 기존 워크플로 위에 뿌리는 단계(completion / chat / vibe)를 지나, **에이전트가 코드의 대부분을 쓰고 사람은 루프 밖에 있는** 일하는 방식. Amazon 사내 용어를 [[clare-liguori|Clare Liguori]]가 [[tech-bridge-frontier-engineering]]에서 정리. 도구([[kiro|Kiro]])가 아니라 **습관**이 생산성 곡선을 가른다.

> Frontier developers write maybe 1 to 2% of the code that they produce. The rest is agents.

## 3행동

영상에서 frontier developer를 정의하는 관측 (이상형이지 인증 기준은 아님):

1. **hands-off coding** — 생산 코드 1–2%만 사람.
2. **드문 개입** — 수 시간 무개입이 목표.
3. **유휴 최소화** — 여러 에이전트 병렬로 백로그.

앞 단계의 개인 체감(10–20%)과 Amazon 파일럿 중앙값 4.5x 사이의 틈을 이 세 행동으로 설명한다.

## 5습관 (매일, 스프린트 한 번이 아님)

| 습관 | 요지 | 위키 자매 |
|---|---|---|
| **에이전트 컨텍스트** | 머릿속 지식을 steering/skills에 기록. 실수마다 추가, 모델이 좋아지면 삭제 | [[harness-engineering]] System Evolution + [[agent-harness-design]] 가정 제거 |
| **감속 후 가속** | 채택 초기 생산성 하락을 감수. 에러 메시지·MCP·구조·(때로) 타입 언어 | 조직 허가. 아래 "리더 함정" |
| **먹이, 돌봄 금지** | 할 일 + 자가 검증을 넘기고 품질 바에만 복귀. vibe 왕복은 4–5x를 막음 | [[verifiable-goals]] independent loop |
| **의도 명문화** | 모호한 기능은 스펙 문서를 먼저. 문서 왕복 < 코드 왕복 | [[spec-driven-development]] |
| **테스트 좌측 이동** | 린터·테스트 + **로컬 결정론적 mock**. 빠른 루프가 수 시간 자율의 조건 | [[agent-org-adoption]] left-shift |

## 재현 조건과 반례

영상 스스로 Mantle(엘리트 6명)과 Prime Video(온콜 없는 방 + 사전 3주 태스크)를 **재현 불가 스토리**로 표시한다. 평범한 50팀에서 갈린 변수는 도구가 아니라 위 습관.

리더 함정: "모델이 좋은데 왜 안 빨라" — 감속(약 2개월의 코드베이스·습관 투자)을 승인하지 않으면 hockey stick 이전에서 멈춤. 스케일 함정: 파일럿 학습 없이 전 조직 롤아웃. Amazon 2026 = 50 → 2,000팀.

새 병목: 손코딩이 1–2개월이 되면 **결정·런칭 리뷰**가 long pole. 프론티어 팀은 코드보다 결정에 시간을 더 쓴다. 되돌리기 쉬운 결정을 빠르게.

비용: FOMO 밤샘, 병렬 탭의 인지 부하, 주니어의 AI 리뷰 근육 부재.

## 위키 합성

[[agent-org-adoption]]은 Figma 현장의 3막·검증 피라미드·시니어 저항. 이 페이지는 Amazon 현장의 **3행동 + 5습관 + 결정 병목**. 둘 다 "도구를 뿌리면 안 된다"가 공통. 차이는 입구: Figma는 주의력·provenance, Amazon은 루프에서 사람 제거와 배포 속도.

## References

- [[tech-bridge-frontier-engineering]]
- [[clare-liguori]] · [[kiro]] · [[amazon]]
- [[agent-org-adoption]] · [[spec-driven-development]] · [[verifiable-goals]] · [[harness-engineering]]

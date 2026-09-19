---
title: Eve (Vercel 에이전트 프레임워크)
type: entity
category: tool
tags: [agent-framework, file-system, vercel, open-source-adapters]
aliases: [Eve]
links:
  - https://eve.dev
sources: [tech-bridge-vercel-eve-filesystem-agent]
created: 2026-09-19
updated: 2026-09-19
---

# Eve

[[vercel|Vercel]]의 에이전트 프레임워크. 자기 규정은 **"에이전트를 위한 [[nextjs|Next.js]]"** 다 — 파일 시스템 컨벤션으로 에이전트를 선언하면 프레임워크가 나머지를 배치한다. → [[framework-defined-agent-infrastructure]]

**공개**: [[tech-bridge-vercel-eve-filesystem-agent]] 발표 기준 *"2주 전 런던 행사"*. ⚠️ 연도 앵커 없음.

## 구조

> 이것이 바로 우리가 생각하는 **에이전트의 실제 모습**입니다. **에이전트는 런타임과 채널을 가지고 있습니다.** 그리고 런타임에는 **내구성(durability)** 이 있어야 하고, **격리된 환경에서 실행**해야 하고, **다양한 모델을 호출**해야 하며, **연결(connections)** 도 필요합니다. (12:47~13:05)

| 선언 단위 | 폴더 |
|---|---|
| 스킬 | `skills/` → [[agent-skills]] |
| 도구 | `tools/` |
| 채널 | `channels/` |

런타임의 네 요구(내구성 · 격리 · 모델 호출 · 연결)가 각각 어댑터를 받는다:

| 요구 | 오픈소스 어댑터 | Vercel 위에서 |
|---|---|---|
| 내구성 | — | **Vercel 워크플로** |
| 격리 | Docker | **샌드박스** |
| 모델 | OpenAI 응답 API | — |
| 연결 | Postgres · 기타 커넥터 | **Vercel Connect**(단기 OIDC 토큰) |

> 여기서 유일하게 다른 점은 **모든 것이 Vercel 제품을 사용한다는 것**입니다. (13:05~13:22)

즉 **오픈소스 어댑터로 자체 호스팅이 가능하되, Vercel 위에서는 네 요구가 전부 자사 제품으로 채워진다.** 배포 시 관측 가능성(모든 실행·도구 호출·단계·예상 비용·최적화 제안)이 기본 제공된다.

## 검증

- 화자가 **D0 에이전트 전체를 Eve로 재작성**했다.
- 베타 고객 **Aura** — *"기성품 [[claude-code|Claude Code]]를 쓰는 것과 달리 Eve로 처음부터 구축하면 단계가 줄고 성공률이 높아지며 인사이트가 낫다"*

⚠️ **수치가 없다.** 비교 조건·과제·측정 방법 전부 없음.

## ⚠️ 유보

- 파일 시스템 **컨벤션의 실제 규격**이 소스에 없다 — 폴더 이름 셋만 나온다.
- 채널이 무엇인지(Slack? 웹? 전화?) 나열되지 않는다.
- 스킬 폴더와 [[query-to-skill-distillation|자동 증류]]의 관계 — 증류 잡이 Eve의 일부인지 별개인지 불명.
- **보안 모델이 없다.** 격리는 샌드박스뿐이고 [[agent-governance-layers]]·[[agent-identity-separation]]에 해당하는 서술이 전무하다.

## References

- [[tech-bridge-vercel-eve-filesystem-agent]] · [[vercel]] · [[andrew-qu]] · [[nextjs]]
- 관련: [[framework-defined-agent-infrastructure]] · [[file-system-agent]] · [[agent-skills]] · [[agent-harness-design]]

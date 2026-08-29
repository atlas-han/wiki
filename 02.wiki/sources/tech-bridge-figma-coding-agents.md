---
title: "Tech Bridge — 품질 저하 없이 조직에 코딩 에이전트를 도입하는 방법 (Figma)"
type: source
tags: [figma, coding-agent, verification, org-adoption, video]
source-url: https://www.youtube.com/watch?v=OSd69LTMi3w
source-type: video
author: Tech Bridge (한국어 자막) · 발표자 Eyal Blum (Figma)
date-published: 2026-08-29
ingested: 2026-08-29
created: 2026-08-29
updated: 2026-08-29
---

# Tech Bridge — 품질 저하 없이 조직에 코딩 에이전트를 도입하는 방법 (Figma)

[[tech-bridge|Tech Bridge]]가 한영자막을 입힌 17:13 강연. [[figma|Figma]] 엔지니어 [[eyal-blum|Eyal Blum]](ASR "Al Bloom")이 **제품이 아니라 사내 엔지니어링 조직**의 코딩 에이전트 도입을 보고한다. Figma는 브라우저 에디터에서 디자인·엔지니어링·에이전트가 같이 코드를 내보내도록 피벗했지만, 이 발표의 범위는 그 제품이 아니다.

본문은 **en-orig 자동 자막** + 채널 챕터. 인용은 자막이 분명한 구간에 한정. 여정은 "아직 반대편에 도착하지 않았다."

## 3막 도입 곡선 (00:00–02:15)

개인과 회사 모두 비슷한 3막:

1. **1막** — 작은 것을 집어 잘 된다. "10x faster."
2. **2막** — 같은 습관을 큰 문제에 적용하면 AI가 꽤 크게 실패. 버그, 쌓아 둔 신뢰가 무너짐.
3. **3막** — 진짜 스킬: 가드레일, 프롬프팅, 컨텍스트. 이 방의 다른 발표들이 말하던 것.

조직 안에서는 막이 **고르지 않다.** AI-forward로 워크플로를 바꾼 팀과, 아직 1막이거나 신뢰를 잃은 팀이 같이 제품을 내야 한다. 공존을 지원하면서 모두를 3막으로 데려가는 것이 과제 (02:15).

## 마찰 네 가지 (02:15–04:30)

1. **개발자 주도성(agency) 감소 → 직무 만족·번아웃.** 코드 작성의 flow에서 **프롬프트 사이클**(출력 대기 → 다시 말하기)로 바뀌면 "예전만큼 재미있지 않다."
2. **최고 엔지니어가 병목이자 가장 느린 채택자.** 머릿속에만 있는 제도적 맥락, 에이전트가 약한 지점을 mental duct tape로 막고 있다. 실패를 가장 먼저 보므로 도입이 가장 느리고 좌절한다 (03:22).
3. **소통 팽창.** 디자인 문서·Slack·이메일이 **3–4배 길어지고**, 메일 수는 **2–3배**. 정보량은 예전과 비슷. 고품질 신호 vs 아닌 것을 가리기 어려워짐 (04:00).
4. **품질 신호 손실** — 위와 한 세트. "무엇이 중요한가"의 마커가 흐려진다.

## 검증이 generation보다 높은 레버리지 (04:32–07:59)

> Investing in verification is probably the highest value thing we can do in our code base.

- **Left-shift:** 사람이 하던 검증을 에이전트가 하게. 예: Playwright MCP가 나온 뒤, 사람이 코드를 탐색하는 대신 에이전트가 탐색 → 팀 생산성 unlock.
- **발견한 유용한 패턴은 즉시 결정론적 플로우로 코드화.** 반복 가능, 토큰·시간 절약. LLM은 추론이 필요할 때만. 이미 아는 것을 테스트로 인코딩하는 투자는 항상 배당을 준다.
- **TDD 순서 (red-green):** 에이전트에게 코드보다 테스트를 먼저 쓰게. 목표를 정해 두고 그쪽으로 밀면, 코드를 쓴 뒤 테스트가 코드에 맞춰지는 경우보다 결과가 거의 항상 낫다.

**에이전트용 테스트 피라미드** (고전 E2E/통합/유닛을 옆으로 옮김):

| 층 | 무엇 | 누가 |
|---|---|---|
| 아래 (가장 큼) | 린트, 컴파일러, 유닛 테스트 | 완전 결정론·자동 |
| 중간 | 코드베이스에 인코딩된 아키텍처 기준 | 기준에 대한 에이전트 리뷰 |
| 꼭대기 (가장 작음) | "이걸 만드는 게 맞는가" 기능·방향 | **인간만** |

인간은 인간만 할 판단에만 남긴다.

## 프롬프팅 대신 기획 (07:59–11:32)

코드 작성의 공예가 줄어든 자리를 **계획을 쓰는 공예**로 채운다. 계획을 오래 쓰고, 구현은 에이전트에 넘기면 "만드는 즐거움"이 돌아온다.

실무: **일주일** 상세 계획 — 결정, 트레이드오프, 동료 리뷰. 결정이 다 나온 뒤에만 에이전트에 보내고, 구현된 것을 받아 리뷰.

**좋은 계획서 조건:**

1. **맨 위 why / executive summary.** 에이전트 drift 방지. 디자인 독의 요약과 같다. 에이전트가 나중에 이 섹션을 고치지 못하게.
2. **독립 검증 가능한 작은 조각.** 개인 테스트: 그 조각에 해당하는 PR을 **한 자리에 리뷰하고 싶은가.** "커피 한 잔 들고 와야 읽겠다"면 너무 크다.
3. **단계별 validation gate / acceptance.** 1단계가 검증 안 된 채 2–5단계가 그 가정 위에 쌓이면 안 된다.

구조 예: 상단 요약 → 페이즈 → 각 페이즈가 sub-agent에 들어갈 만큼 상세. 워크플로는 사람마다 달라도 된다. **한 가지로 중앙화하는 수익은 체감된다.** 자기 흐름이 되고 남이 같이 이터레이트할 수 있으면 충분.

**5x 사례 (발표자 본인, 스크린샷):** ~20개 PR, 각 10–100줄, 그보다 큰 것은 거의 없음. 프리-AI라면 계획 1주 + 3개 팀 정렬 1주 + 구현 수주 ≈ **코딩 6주분**. 에이전트가 하룻밤 구현, 리뷰 포함 **1주** → 5x. (스크린샷은 플랜 두 개일 수 있다고 정정.)

## 회의론자에게 안전 로드맵 (11:32–12:42)

시니어가 회의적인 이유는 성격이 아니라 **검증이 비는 곳, 도구가 실패하는 곳**을 보기 때문. 그 피드백이 곧 에이전트–코드베이스 개선 로드맵.

변환하려 하지 말고 **조직에서 AI를 안전하게 만드는 로드맵 소유권**을 준다. 자기 제안이 일을 쉽게 만드는 것을 보면 따라온다. "고칠 것을 말하는 데 수줍어하지 않는다."

## 주의력 기반 소통 (12:42–16:16)

> In the age of AI, human attention is a scarce resource. You can't get more human attention.

**Provenance:** 어디가 사람 글이고 어디가 AI인지 표시해야, 얼마나 공을 들여 읽을지·얼마나 slop을 기대할지 알 수 있다.

팀 규범: **모든 PR 설명은 손으로 쓴 짧은 요약으로 시작** (코드가 무엇이고 무엇을 하는지). AI 생성 설명은 그 아래. 사람은 위를 우선하고, 아래는 의심하고 위를 이기게. Slack·이메일도 같다. AI 사용을 숨기지 말고, **무엇을 읽고 무엇은 덜 읽을지**를 말한다.

**실패 일화 (2026 초):** 회의적 시니어에게 PR 코멘트 분석을 보냄. AI로 돌렸는데 사람/AI를 구분하지 않음. 상대: 존중하는 사람이 **이렇게 sloppy한 글**을 보낼 줄 몰랐다. 즉시 사과. 의도("이건 내가 쓴 것, 이건 AI, 맥락이 없어 sloppy한지 당신이 알아야 한다")를 표시했어야 했다.

> Change the culture is just as important as some of the engineering challenges.

**낮은 마찰 진입:**  fancy 워크플로보다, 사람이 **있는 자리**에서 쓰게. Slack 스레드에 에이전트를 태그해 "이것만 해 줘" → 스레드에서 루프를 닫기. 아직 안 산 사람에게 비꼬지 않고 "이번엔 에이전트가 되나 보자." 좋은 경험이면 혼자 실험한다.

## 아직 다 오지 않았다 (16:16–끝)

외부로는 AI를 팔고 있어도 내부 자동화는 **fully there yet이 아니다.** 레거시 빌드 의존성 때문에 클라우드 에이전트를 언제·어떻게 쓸지 실험 중. 문화 전환이자 엔지니어링 전환.

> I've been working in the valley for the last 15 years and this is the biggest change by orders of magnitude of everything that I've seen in term culture and technology.

## 위키 합성

- [[agent-org-adoption]]의 1차 소스.
- 검증 피라미드·TDD-first는 [[verifiable-goals]]의 조직 운영판. 유용한 발견을 결정론적 체크로 고정하는 것은 [[harness-engineering]] "every mistake becomes a rule."
- 계획서의 why / 작은 PR / 단계별 gate는 [[sprint-contract]]·[[spec-driven-development]]와 동형 — Figma는 그걸 *도구 없이* 팀 규범으로 한다.
- 인간 주의력 = 하니스 제약. provenance는 그 제약을 명시한 소통 훅.

## 핵심 인용 (en-orig)

> Investing in verification is probably the highest value thing we can do in our code base.

> In the age of AI, human attention is a scarce resource. You can't get more human attention.

> Change the culture is just as important as some of the engineering challenges that we've been facing.

> This is the biggest change by orders of magnitude of everything that I've seen in term culture and technology.

## 등장 개체·개념

- 채널: [[tech-bridge]]
- 인물: [[eyal-blum]]
- 조직: [[figma]]
- 개념: [[agent-org-adoption]] (메인), [[verifiable-goals]], [[sprint-contract]], [[harness-engineering]], [[outcome-engineering]], [[spec-driven-development]], [[model-context-protocol]]

## References

- [원문 영상](https://www.youtube.com/watch?v=OSd69LTMi3w)
- 원문 캡처: `01.raw/articles/2026-08-29_품질 저하 없이 조직에 코딩 에이전트를 성공적으로 도입하는 방법 Figma.md`
- 발표자: [Eyal Blum](https://www.linkedin.com/in/eyalg/)

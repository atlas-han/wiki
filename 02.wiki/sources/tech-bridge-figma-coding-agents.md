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

[[tech-bridge|Tech Bridge]] 채널이 한국어·영어 자막을 입혀 재배포한 17:13 영상. [[figma|Figma]] 엔지니어 [[eyal-blum|Eyal Blum]]이 사내 수천 명 규모 코딩 에이전트 도입의 **진행 중인 현장 보고**를 한다. 모델이 아니라 **인간 주의력**이 희소 자원이라는 전제 위에서, 검증 인프라·기획·회의론자·출처 표기를 조직 규범으로 올린다.

> ⚠️ 2026-08-29 ingest 시 YouTube timedtext HTTP 429로 **영상 자막 전문을 받지 못함**. 채널 설명의 챕터·핵심 포인트는 1차. 동일 강연의 2차 기록(AI Engineer 에피소드 정리, [BigGo](https://finance.biggo.com/news/cf0618b0d99301f1))은 complementary로만 쓰고, 채널 설명에 없는 수치는 2차 출처로 표시.

## 핵심 takeaways

1. **3막 도입 곡선** ([[agent-org-adoption]]). 1막 초기 성공 → 2막 중간 규모 실패(이득이 복리로 안 쌓임, 리뷰 부하, 시니어 병목, 프롬프트 사이클 번아웃, 커뮤니케이션 3–4배 팽창) → 3막 검증·가드레일을 갖춘 역량. 채널 챕터 0:00 / 2:15 / 3:22.

2. **검증이 generation보다 높은 레버리지**. 사람 검증을 앞당기고(left-shift), 반복 가능한 패턴은 테스트·결정론적 플로우로 코드화. Playwright·[[model-context-protocol|MCP]]로 에이전트가 코드베이스를 스스로 탐색하게 된 것이 변곡. 테스트는 코드보다 먼저 (red-green). 피라미드: 아래=린트/컴파일/유닛(완전 자동) → 중간=아키텍처 기준에 대한 에이전트 리뷰 → 꼭대기=*"이걸 만드는 게 맞는가"* 만 인간. ([[verifiable-goals]], [[harness-engineering]] System Evolution과 동형 — 유용한 발견을 즉시 규칙/체크로 고정.)

3. **프롬프팅 대신 기획**. 좋은 계획서: 상단 why(에이전트 drift 방지) · 한 자리에 리뷰할 수 있을 만큼 작은 조각 · 단계별 acceptance criteria. 채널 챕터 7:59 / 9:08. 2차 기록은 6주 분량을 1주·약 20개 PR(10–100줄)로 압축한 사례를 든다.

4. **회의론자에게 안전 로드맵을 맡긴다**. 시니어의 저항은 성격이 아니라 **검증 갭의 우선순위 목록**. 변환하려 하지 말고 로드맵 소유권을 준다 (11:32).

5. **주의력 기반 소통 (provenance)**. PR 설명 상단은 사람이 직접 쓴 요약, 그 아래가 AI 생성 — 어디를 신뢰할지 표시. 미표시 AI 분석은 시니어에게 "성의 없는 본인 글"로 읽혀 반감을 산다 (12:42 / 15:03). Slack에서 에이전트를 태그해 루프를 닫는 낮은 마찰 진입 (16:16).

6. **정직성**. 발표 스스로 Figma 자동화는 "아직 다 오지 않았다"고 한다. 레거시 의존성 때문에 클라우드 에이전트 사용 범위도 실험 중.

## 등장 개체·개념

- 채널: [[tech-bridge]]
- 인물: [[eyal-blum]]
- 조직: [[figma]]
- 개념: [[agent-org-adoption]] (메인), [[verifiable-goals]], [[sprint-contract]], [[harness-engineering]], [[outcome-engineering]], [[model-context-protocol]]

## References

- [원문 영상](https://www.youtube.com/watch?v=OSd69LTMi3w)
- 원문 캡처: `01.raw/articles/2026-08-29_품질 저하 없이 조직에 코딩 에이전트를 성공적으로 도입하는 방법 Figma.md`
- 발표자: [Eyal Blum](https://www.linkedin.com/in/eyalg/)
- 2차 정리: [BigGo — How AI Broke Engineering Culture](https://finance.biggo.com/news/cf0618b0d99301f1)

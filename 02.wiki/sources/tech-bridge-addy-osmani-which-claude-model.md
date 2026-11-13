---
title: "Tech Bridge — Fable·Opus·Sonnet·Haiku, 어떤 Claude 모델로 만들어야 할까? | 모델 선택 가이드 9분 총정리 (한국어 해설): 기본값 Opus 5.5 medium · 백로그 네 장 배정 · 모델보다 effort 먼저 · 완료한 작업당 비용 · 캐시와 컨텍스트 · 서브에이전트와 워커 · 옮기기 전 호환성 · 내 작업으로 측정"
type: source
tags: [model-selection, claude, fable-5-2, claude-opus-5-5, claude-sonnet-5-5, claude-haiku-5-5, reasoning-effort, pricing, prompt-caching, subagents, cost-per-task, addy-osmani, anthropic, korean-narration, video]
source-url: https://www.youtube.com/watch?v=M_yjL9qgwDo
source-type: video
author: Tech Bridge (한국어 해설, AI 내레이션) · 바탕 Addy Osmani "Which Claude model should you build with? Fable, Opus, Sonnet, or Haiku"(claude.dev 블로그, 2026-11-09, 위키 미열람)
date-published: 2026-11-12
ingested: 2026-11-13
created: 2026-11-13
updated: 2026-11-13
---

# Tech Bridge — Fable·Opus·Sonnet·Haiku, 어떤 Claude 모델로 만들어야 할까?

[[tech-bridge|Tech Bridge]]의 **9:01 한국어 해설, 공식 챕터 9.** [[addy-osmani|Addy Osmani]]가 Claude 개발자 블로그(claude.dev)에 쓴 모델 선택 가이드(2026-11-09, 설명란)를 **온라인 상점 프로젝트의 백로그 네 장** 에 빗대어 정리한다. 네 모델은 [[fable-5-2|Fable 5.2]] · [[claude-opus-5-5|Opus 5.5]] · [[claude-sonnet-5-5|Sonnet 5.5]](신규) · [[claude-haiku-5-5|Haiku 5.5]](신규). 원음 발췌가 없는 **순수 AI 내레이션** 이다(설명란). raw: `01.raw/articles/2026-11-12_Fable·Opus·Sonnet·Haiku 어떤 Claude 모델로 만들어야 할까 모델 선택 가이드 9분 총정리.md`.

테제(맺음):

> *"오퍼스 5.5 미디엄에서 시작합니다. 모델을 바꾸기 [음악] 전에 에포트를 먼저 조정합니다. 그리고 토큰 단가가 아니라 완료한 작업당 비용으로 고릅니다."*(08:48~08:57)

> ⚠️ **해설자가 옮긴 Addy Osmani 글의 내용이다.** 가격 · 기본 effort · 벤치마크 수치 · 호환성 규칙은 원 글 · 공식 문서(choosing a model · effort · Claude Code model config)를 위키가 열지 않은 채 해설로만 기록한다. 설명란은 *측정 그래프의 점과 일부 비용 막대는 비율만 나타낸 예시* 라고 밝힌다.
>
> **트랙과 인용.** `ko` = `ko-orig`(md5 동일, `kind=asr&lang=ko&variant=gemini`)가 원 ASR이고 en-orig(`lang=en&variant=timing-optimized`)는 영어 더빙 ASR이다. 인용은 전부 ko-orig다. ⚠️ **더빙이 모델 버전을 바꾼다**(`Opus 3.5` · `Sonnet 3.5` · `Haiku 3.5` · `Fable 2024`) — 버전은 ko-orig · 설명란 · tags로만 읽었다. ASR이 Claude를 *클라우드* 로, effort를 *에포트* 로 적는다. 판독 목록은 raw 헤더에 있다.

## 1. 이 일, 어떤 모델에 맡길까 (00:00~00:23)

- 백로그 네 장: 코드 전체 TypeScript 전환 · 월 구독 기능 · 상품 페이지 · 고객 메시지 분류(00:00~00:08). 이 일들을 어떤 Claude 모델에 맡길까.

## 2. 기본값: Opus 5.5 medium에서 시작 (00:23~01:05)

- *"먼저 결론부터 말하면 잘 모르겠을 때는 오퍼스 5.5를 에포트 미디엄으로 시작하면 됩니다."*(00:25~00:29) Claude Code의 기본 모델이고 토큰 가격은 Fable 5.2의 절반이다(00:31~00:32).
- 네 모델 가격(입력 / 출력, 100만 토큰당, 00:36~00:47)과 기본 effort(00:52~01:00):

| 모델 | 입력 | 출력 | API 기본 effort | Claude Code 시작 effort |
|---|---|---|---|---|
| [[claude-haiku-5-5\|Haiku 5.5]] | $0.10 | $0.50 | medium | — |
| [[claude-sonnet-5-5\|Sonnet 5.5]] | $2 | $10 | high | medium |
| [[claude-opus-5-5\|Opus 5.5]] | $4 | $20 | medium | medium(기본 모델) |
| [[fable-5-2\|Fable 5.2]] | $8 | $40 | high | medium |

- 컨텍스트는 네 모델 모두 100만 토큰(00:47~00:49). 지금 설정은 `/effort` 로 확인할 수 있다(01:00~01:03, 명령 형식은 ASR *슬래시 에포트 스테이터스* — 미확정).

## 3. 작업별 배정: 네 모델에 일 나누기 (01:05~02:28)

| 티켓 | 모델 | 맞는 일 |
|---|---|---|
| JS → TypeScript 대규모 전환 | Fable 5.2 | 큰 리팩터링 · 마이그레이션 · 아키텍처 설계 · *사람이 지켜보지 않는 긴 실행*(01:14~01:18) |
| 월 구독 기능 | Opus 5.5 | 여러 PR에 걸친 기능 개발 · 일상 디버깅, 스크린샷이 많은 컴퓨터 사용 작업(01:21~01:31) |
| 상품 페이지 | Sonnet 5.5 | 버그 수정 · 스펙이 분명한 기능처럼 범위가 정해진 일을 Opus 토큰 가격의 절반으로, 채팅 · 문서 · 슬라이드(01:35~01:44) |
| 고객 메시지 분류 | Haiku 5.5 | 분류 · 라우팅 · 대량 처리처럼 단순하고 양이 많은 일, 큰 모델의 부수 작업을 맡는 서브에이전트(01:46~01:55) |

- 티켓 밖의 일(01:57~02:26): 채팅 · 대화형 세션은 Sonnet low/medium(단순 대량 채팅은 Haiku), 조사 · 리뷰 · 초안처럼 반복 실행하는 에이전트 작업도 Sonnet medium이면 충분, 심층 리서치 · 과학 정량 분석은 Fable 5.2에서 시작. 문서는 Sonnet이 기본이지만 복잡한 재무 모델 · 방대한 원자료 문서는 Opus. *"스펙이 분명해도 마이그레이션이나 성능 최적화는 오퍼스가 필요할 수 있습니다."*(02:23~02:26)

## 4. 모델보다 effort 먼저 (02:28~04:23)

- ⭐ *"모델을 바꾸기 전에 에포트부터 조정을 하는 것입니다."*(02:31~02:34) effort는 비용과 성능을 더 세밀하게 조절하는 다이얼이다. *"다만 에포트를 올려도 [음악] 모델에 없는 지식이나 능력이 생기지는 않습니다."*(02:37~02:41) 올리면 더 오래 생각하고 · 도구를 더 많이 호출하고 · 자기 결과를 더 검증하며, effort와 지연 시간은 대략 비례한다(02:43~02:55). → [[reasoning-effort-levels]]
- Opus 5.5 SWE-bench Pro(high 기준, 02:57~03:10): medium 약 −2.5포인트 · 비용 약 70%, low 약 −8포인트 · 비용 약 1/3, extra high +1.4포인트 · 비용 2.5배. → 하이를 넘겨야 할 땐 *"한 단계 위 모델을 더 낮은 에포트로 시험해 봐야 합니다."*(03:13~03:17)
- Frontier Code 2.0: Fable 5.2 high 45.3% vs Opus 5.5 max 45.5% — 점수는 거의 같고 작업당 비용은 Fable 쪽이 절반 정도(03:18~03:29). 반대 사례 — Terminal-Bench 3.0: Fable 5.1 max 58.0% vs Opus 5.5 high 58.9%, 토큰은 절반(03:32~03:42). *"토크는 단가가 아니라 완료한 작업당 비용을 봐야 하는 이유입니다."*(03:45~03:46)[=토큰은] → [[true-cost-to-perfect-answer]] · [[cost-vs-score-frontier]]
- 모델이 일을 못 해낼 때 세 단계(03:49~04:02): ① 테스트 · 빌드처럼 스스로 검증할 수단을 준다 ② effort를 한 단계 올린다 ③ 한 단계 위 모델로, 더 낮은 effort로 시작.
- ⭐ 결과를 자동으로 확인할 수 있다면 — *"전부 로우로 돌리고 실패한 [음악] 작업만 하이로 다시 돌리는 것입니다."*(04:07~04:11) Opus 5.5에서 약 97% 통과 · 작업당 약 17센트, 전부 high면 95.3% · 29센트(04:12~04:19).

## 5. 속도와 컨텍스트 비용 (04:23~05:43)

- 사람이 응답을 기다리면 Sonnet 5.5 low/medium. 같은 모델에서 속도만 더 필요하면 빠른 모드(Opus 5.5 · Fable 5.2 지원, 더 비쌈)(04:24~04:33). 세대 차: Fable 5.2는 Fable 5.1보다 출력 최대 30% 빠르고, Sonnet 5.5는 Sonnet 5보다 30% 빠르다(04:37~04:45).
- *"컨텍스트도 비용입니다. 큰 컨텍스트는 매 턴마다 다시 전송되기 때문입니다."*(04:47~04:50) 한 턴 캐시 읽기 비용: 15만 토큰 약 3센트, 2만 토큰 약 0.4센트. 비싼 모델의 컨텍스트는 판단에, 긴 읽기는 저렴한 서브에이전트에(04:52~05:02). → [[prompt-caching]]
- 긴 실행에서는 입력 대부분이 캐시 읽기 — 캐시 읽기 가격은 Opus 5.5와 Fable 5.2가 100만 토큰당 20센트로 같아서, 차이는 캐시되지 않은 입력과 출력에서 나고 거기서 Fable은 토큰당 두 배다(05:05~05:17).
- Haiku 5.5는 프롬프트 길이에 따라 가격이 달라지는 유일한 모델 — 10만 토큰을 넘으면 다섯 배, 그래도 Sonnet 5.5 토큰 가격의 1/4(05:19~05:28).
- 가장 어려운 작업의 비용도 계산하라 — *"20문제짜리 검색 벤치마크에서는 [음악] 단 두 문제가 전체 지출의 43%를 차지했습니다."*(05:36~05:40)

## 6. 모델 섞어 쓰기: 서브에이전트와 워커 (05:43~07:30)

- **캐시는 모델에 묶인다** — 모델을 바꾸면 첫 턴에 전체 대화를 다시 캐시에 써야 한다. 전환은 작업 경계에서, Claude Code에서는 먼저 `/compact`(05:47~05:59). → [[context-resets-and-compaction]]
- **생각 블록도 따라오지 않을 수 있다** — 상위 모델은 하위 모델의 생각 블록을 읽지만 아래로 내려가면 이전 추론은 버려진다. 요청은 성공하지만 새 모델은 그 추론 없이 일한다. API에서는 전체 기록 대신 요약으로 새 대화를 시작하는 편이 낫다(06:02~06:16).
- **서브에이전트는 작은 모델에** — 파일 찾기 · 테스트 실행 · 로그 읽기처럼 *"틀리면 금방 드러나는 일"*(06:22~06:24). 정의에 Haiku나 Sonnet을 지정하고 코드 수정 · 판단은 메인 모델에. ⚠️ 작은 모델이 검색 결과를 잘못 읽으면 메인 모델이 엉뚱한 파일을 열어 토큰을 낭비한다(06:32~06:37). Claude Code 내장 Explore 서브에이전트는 기본적으로 세션 모델을 따르므로, 비용을 낮추려면 Haiku를 지정한 Explore를 직접 정의한다(06:39~06:46). → [[orchestrator-searcher-split]] · [[model-mixing-economics]]
- **워커** — 한 컨텍스트에 안 담기는 큰 작업은 상위 모델이 쪼개 워커에 나눈다. 약 2,200만 토큰 규모 결함 탐색에서 Opus 5.5 지휘 + Sonnet 5.5 워커는 Opus 단독보다 약 1/3 저렴, 성능은 거의 같았다(06:48~07:01). 단, 앞 단계에 의존하는 작업이거나 한 컨텍스트에 들어가면 *"계획하고 합치는 비용이 절감액보다 큽니다."*(07:09~07:11)
- **어드바이저** — 저렴한 모델이 일하다 더 강한 모델에 조언을 구하는 도구. Opus 5.5에 Fable 5.1 어드바이저를 붙인 사례는 점수가 1.7(포인트로 추정) 오르는 데 비용이 약 2.1배(07:14~07:25) — *"먼저 측정해 보라는 뜻입니다."*(07:25~07:28) ⚠️ 점수 판독(*1.7.5*)은 미확정.

## 7. 모델을 옮기기 전 확인할 것 (07:30~08:20)

- Sonnet 5.5 · Opus 5.5 · Fable 5.2에서는 **도구 사용을 강제하는 설정이 400 오류**를 낸다(07:32~07:39). Opus와 Fable은 항상 생각을 켠 채로 동작한다. Haiku 4.5 → 5.5로 옮길 때는 budget tokens를 effort 수준으로 바꿔야 한다(07:40~07:46).
- ⭐ Fable 5.2 추가 규칙: *"생각복록 앞에 내용, 즉 시스템 프롬프트나 도구, 이전 메시지를 바꾸면 400 오류가 납니다."*(07:50~07:56)[=생각 블록] Claude Code · Agent SDK면 바꿀 것이 없지만, 기록을 직접 편집한다면 **덧붙이기만** 하도록 유지(07:57~08:03).
- 여러 모델을 함께 쓴다면 *"가장 엄격한 모델을 맞춰 요청을 구성합니다."*(08:05~08:07) — 대화 기록은 덧붙이기만, 도구 선택은 자동, 응답 블록은 타입으로 읽는다. 그러면 코드를 고치지 않고 단계를 위아래 모델로 옮길 수 있다(08:10~08:18). → [[prompt-caching]]

## 8. 내 작업으로 직접 측정하기 (08:20~08:48)

- *"공개 벤치마크는 출발점일 뿐입니다."*(08:22~08:24) 실제 작업을 모아 통과 기준을 정하고, 후보 모델을 effort 두세 단계로 돌려 작업마다 비용을 기록하고, 점수와 지출을 그래프로 그린 뒤 이긴 구성을 실제 트래픽 일부에 먼저 적용한다(08:24~08:35).
- Claude Code에서는 더 간단히 — 백로그 작업 하나를 `/model` 로 두 모델에서 돌려 보고 `/usage` 가 보고하는 값을 비교한다(08:37~08:46).

## 9. 정리 (08:48~09:01)

- Opus 5.5 medium에서 시작 → 모델을 바꾸기 전에 effort → 토큰 단가가 아니라 완료한 작업당 비용(테제 인용).

## 위키의 읽기

- **위키에 처음으로 네 모델의 가격 · 기본 effort 표가 한 소스에 들어온다.** [[claude-opus-5-5]] 페이지가 *가격 1차 자료 없음* 으로 남겨 둔 자리에 **$4 / $20(해설 전달)** 이 들어온다. Kimi 편의 *"Opus 5.5 is double the cost"*(Kimi $2/$10 기준)와 산술이 맞는다. Fable 5.2 $8/$40은 11-10 발표문 해설과 같다. ⚠️ 여전히 원 문서는 열지 않았다.
- **Frontier Code 2.0 수치가 두 소스에서 겹친다.** Fable 5.2 high 45.3%는 11-12 [[tech-bridge-chase-ai-fable-5-2-prompting-rules|Chase AI 편]]과 같고, Opus 5.5 max 45.5%는 11-10 [[tech-bridge-claude-fable-5-2-announcement|발표문 해설]]의 *Opus 5.5 Frontier Code 45.5* 와 같다. 그 해설의 Fable 5.2 *49.1* 은 high가 아닌 다른 effort의 값일 가능성이 있다(⚠️ 위키의 추정, 미확인).
- **[[reasoning-effort-levels]]의 두 번째 소스 — 이번엔 *벤더 측 가이드*.** Chase AI(실무자 해석)가 *Fable은 high부터* 를 말했다면 이 가이드는 **모델 선택의 첫 다이얼이 effort** 라고 일반화하고, *low 후 실패만 high* 라는 계단식 재실행을 수치와 함께 내놓는다 → [[true-cost-to-perfect-answer]](*완료한 작업당 비용* 단위의 벤더 판).
- **[[model-mixing-economics]]에 *혼합의 비용* 이 붙는다.** 캐시가 모델에 묶이고, 생각 블록이 아래로 안 내려가고, 계획 · 합치기 비용이 절감을 넘을 수 있고, 어드바이저는 2.1배 — 섞기 전에 측정하라는 방향이다. 11-04 Greptile 편의 *평가 셋이 안전장치* 와 같은 결론이다.
- **같은 날 [[tech-bridge-lydia-hallie-rethinking-claude-code-best-practices|Lydia Hallie 편]]의 *Fable 메인 · Opus 5.5 스레드* 구성**은 이 가이드의 *상위 모델이 쪼개고 판단, 워커는 아래* 와 같은 모양이다(가이드의 수치는 Opus 지휘 · Sonnet 워커).

## 등장 개체

- 인물: [[addy-osmani]]
- 모델 · 제품: [[fable-5-2]] · [[fable-5-1]] · [[claude-opus-5-5]] · [[claude-sonnet-5-5]](신규) · [[claude-haiku-5-5]](신규) · [[claude-code]] · [[anthropic]] · [[tech-bridge]]
- 벤치마크: SWE-bench Pro · Frontier Code 2.0 · Terminal-Bench 3.0(→ [[terminal-bench]]) — 페이지화하지 않음(Terminal-Bench는 기존 페이지 보강)
- 개념: [[reasoning-effort-levels]] · [[true-cost-to-perfect-answer]] · [[cost-vs-score-frontier]] · [[model-mixing-economics]] · [[prompt-caching]] · [[orchestrator-searcher-split]] · [[context-resets-and-compaction]]

## References

- 영상: https://www.youtube.com/watch?v=M_yjL9qgwDo
- raw: `01.raw/articles/2026-11-12_Fable·Opus·Sonnet·Haiku 어떤 Claude 모델로 만들어야 할까 모델 선택 가이드 9분 총정리.md`
- 설명란 참고(위키 미열람): https://claude.dev/blog/which-claude-model-should-you-build-with/ · https://platform.claude.com/docs/en/about-claude/models/choosing-a-model · https://platform.claude.com/docs/en/build-with-claude/effort · https://code.claude.com/docs/en/model-config

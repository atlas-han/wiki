---
title: Theo
type: entity
category: person
tags: [youtuber, developer, t3-code, t3-chat, twitch, codebase-gardening, agentic-coding]
aliases: [Theo, t3.gg, Theo - t3.gg, 태오, 테오, Tae-o, Teo, T3 Code, T3 Chat, 티스리챗, 티슈리 코드]
links:
  - https://www.youtube.com/watch?v=GtJKFhztgdM
  - https://github.com/pingdotgg/t3code
sources: [tech-bridge-theo-coding-is-gardening, tech-bridge-codex-app-server, tech-bridge-pstack-third-party-review, tech-bridge-rob-shocks-grokbot-manager-coding-agents, tech-bridge-better-stack-claude-code-agent-summary-cost, tech-bridge-theo-fable-vs-opus-when-to-use, tech-bridge-gpt-6-2-astra-launch-day-reactions, tech-bridge-theo-gemini-4-neon-capability-vs-coherency]
created: 2026-11-11
updated: 2026-11-24
---

# Theo

개발자이자 유튜버(채널 *Theo - t3.gg*). **T3 Code**(오픈소스 코딩 에이전트 앱, 저장소 `pingdotgg/t3code`)와 **T3 Chat**을 만든 쪽으로 이 위키에 나온다. 위키에는 네 소스에서 이름이나 제품으로만 스쳐 오다가, 2026-11-10 [[tech-bridge-theo-coding-is-gardening]]에서 처음으로 그를 다루는 소스가 들어왔다.

> ⚠️ **본인 음성은 캡션에 없다.** 11-10 소스는 Theo의 영상 *"Coding Isn't About Code Anymore"*(`GtJKFhztgdM`)를 한국어 해설자가 옮긴 2차 전달이다(AI 내레이션). 원음 발췌 다섯 곳은 두 자막 트랙 모두 무캡션이다. 이름은 설명란 · tags 근거다(ko ASR *태오* · *태우* · *헤오*, 더빙 *Tae-o* · *Teo*). T3 Code 저장소 경로는 설명란 PR 링크에서 왔다. 위키는 원 영상 · PR을 열지 않았다.

## 해설이 전하는 이력 (2026-11-10 · 2차 전달)

- 2017년부터 4년 동안 Twitch에서 일했다. 제품 팀 소속이었지만 플랫폼 팀 회의에 늘 끼어 있었다(00:55~01:09).
- Twitch를 나와 회사를 차렸다 — *"직원 1500명 회사에서 혼자인 회사로 간 거죠."*(01:58~02:00)
- T3 Chat의 데이터 동기화 엔진을 손으로 짰다가 한 달 들여 다른 구현으로 옮겼다(2만 5천 줄 PR, 02:15~02:30).
- 지금은 세 명짜리 팀을 위해 TypeScript를 [[rust|Rust]]로 다시 쓰고 있다(03:26~03:30).
- 원래 개발을 *레고*(블록 놀이)처럼 사랑했고 AI 코딩이 그 재미를 없앨까 두려웠지만, 지금은 *"일주일에 한두 번 새벽 6시에 잠들만큼 재밌다고 합니다."*(00:48~00:52)

## 입장 — 개발자는 정원사

*"모든 팀에는 정환사가 필요하다. 뽑은 잡조 하나하나가 규칙이 되어 다시는 자하지 못하게 하는 사람 말입니다."*(05:43~05:50)[=정원사 · 잡초 · 자라지] → [[codebase-gardening]]

- **잡초**: T3 Code PR 하나로 테스트 약 1만 1천 개(약 43%) 삭제 — Claude Haiku 에이전트들이 판정했다(04:13~04:46).
- **지지대**: PR마다 실제 대화 데이터로 전송량을 재서 댓글로 남기는 검사(04:56~05:24).
- **거름**: 시간의 절반은 사용자가 못 느끼는 플랫폼 작업(02:02~02:13).
- **마찰**: *"마찰은 사람보다 에이전트를 훨씬 세게 막습니다."*(03:34~03:36) → [[agent-friction-multiplier]]
- **슬롭**: *"그는 에이전트보다 먼저 슬롭을 쓰고 있었던 겁니다."*(02:37~02:39) → [[ai-slop]]

해설은 [[lauren-tan|Lauren]](React 컴파일러 팀, 설명란 *@poteto*)이 같은 이야기를 했다고 덧붙인다(05:42~05:43, *비율 / 비유* 미확정).

## 다른 소스에 스친 이름 (2026-09 ~ 11)

| 소스 | 언급 |
|---|---|
| [[tech-bridge-pstack-third-party-review]](09-13) | 화자: *"우리 친구 Theo"* 가 [[pstack]](Lauren Tan의 스킬) 딥다이브를 했다 → [[lauren-tan]] |
| [[tech-bridge-codex-app-server]](10-14) | *"open source projects like Theos T3 code"*(02:22~02:27) — T3 Code가 [[codex-app-server]] 위에서 돈다, 사용자의 Codex 구독으로 차감 → [[bring-your-own-subscription]] |
| [[tech-bridge-rob-shocks-grokbot-manager-coding-agents]](11-02) | *"Theo is trying out a similar workflow with T3 Code"*(09:13~09:20) — [[grokbot]]으로 기기들을 몬다(트윗, 미확인) |
| [[tech-bridge-better-stack-claude-code-agent-summary-cost]](11-02) | 화자가 터미널 Claude Code 대신 T3 Code를 쓴다, T3 Code는 요약을 자기 방식으로 처리한다 → [[hidden-harness-calls]] |

→ T3 Code는 **여러 하네스(Codex · Claude Code)를 감싸는 앱**으로 그려진다(위키의 읽기, 제품 페이지는 따로 만들지 않았다).

## References

- [[tech-bridge-theo-coding-is-gardening]] — 2026-11-10 한국어 해설(6:21), 원 영상 `GtJKFhztgdM`의 2차 전달
- https://github.com/pingdotgg/t3code (설명란 PR 링크의 저장소, 위키 미열람)

## Fable 5.2 vs Opus 5.5 — *Stop Picking The Wrong Model* (2026-11-16 · [[tech-bridge-theo-fable-vs-opus-when-to-use]])

Tech Bridge 해설(원 영상 `XtykeVoSmP8` 42분 · 공식 가이드 · X 게시물 3건의 2차 전달, ⚠️ 본인 음성 무캡션 · 원 자료 미열람). [[fable-5-2|Fable 5.2]] 출시 당일 *"오퍼스를 쓸지 페이블을 쓸지 벌써 헷갈린다"*, 일곱 시간쯤 뒤 *"페이블 5.2가 오퍼스라면 안 했을 멍청한 실수를 많이 한다"*(X 게시물, 해설 전달).

- **두 모델만 남겼다** — 코딩 모델 열 개 넘게에서 Opus · Fable만. 근거는 성능 점수를 *구독 요금 기준 비용* 으로 다시 그린 차트.
- **자기 계정 측정**(설명란이 구분): 3달 · 요청 110만 건으로 월 200달러 요금제 환산 — Opus만 쓰면 API 값 약 14,600달러 치, Fable만 쓰면 3,000달러 치(주간 한도의 절반까지만). 속도 Haiku 255 · Sonnet 145 · Opus 112 · **Fable 106** tok/s(예상은 50~60).
- **effort**: 공식 기본값 medium 대신 **high** 추천 — medium은 일찍 멈추고 확인을 덜 하고, max는 쉬운 일에도 억지로 오래 생각해 엉뚱한 일을 벌인다. → [[reasoning-effort-levels]]
- **기질 비유**: Opus = 모범생 · 앨런(꼼꼼, 틀은 의심하지 않음), Fable = 뒷자리 · 브래드(틀을 의심, *LGTM*). Opus에게 *좋은 생각 같으면 하고 아니면 다른 방법을 제안해라* 를 붙인다. → [[model-temperament-routing]](신규)
- **T3 Code 사례**: 며칠씩 도는 스레드를 휴대폰에서 빨리 열리게 기록을 조각내는 작업 — Opus의 테스트 환경을 Fable이 검증해 *끝나지 않은 할 일 목록이 기록 전체를 끌고 간다* 는 문제를 짚었다. 챕터 제목의 *150분의 1* 은 캡션에 없다.
- **자체 평가판**: 종합 순위 Fable 3위(Sonnet · Opus 아래), 코드 리뷰에서 문제 있는 코드를 더 자주 통과 — 그러나 놓친 지적 대부분이 *안 고쳐도 되는 것* 이었다(Theo 재해석). *지금까지는 그랬다*, 언제든 뒤집힐 수 있다.
- 11-10 *정원사* 편의 T3 Code · Rust 재작성과 이어진다 — 이번엔 *TypeScript를 Rust로 다시 쓰는 일* 이 *검증 가능한 일 = Opus로 충분* 의 예로 나온다.

## 2026-11-19 — OpenAI 조기 테스터로서: *내가 Astra를 싫어하는 이유* ([[tech-bridge-gpt-6-2-astra-launch-day-reactions]])

GPT-6.2 [[openai-astra|Astra]] 출시 당일(2026-11-17) Theo는 *"오픈 AI가 지금까지 낸모델 중에 최악입니다."*(00:00~00:02) 한 줄을 올린 뒤, 테스트 기간에 OpenAI에 보냈던 편지를 통째로 공개했다 — *"하루 만에 186만 번 읽혔습니다."*(01:46~01:48) ⚠️ 아래는 한국어 해설이 옮겨 읽은 것이고 위키는 편지를 열지 않았다.

- **칭찬으로 시작한다** — *"3D와 게임은 세계 최고 수준이다. 컴퓨터를 다루는 능력도 코드 품질도 좋아졌다."*(01:54~01:59) Astra와 만든 리버스 프록시로 월 25,000달러를 아낀다는 말도 있다. 그리고 *"그밖에 모든 것이 진심으로 싫다."*(02:08)
- **불만 셋** — ① 엉뚱한 질문을 하고 멈춘다: *"아스트라가 또 멈췄는지 확인하는 에이전트를 따로 돌려야 했다고 적었습니다."*(02:25~02:28) ② 설명을 알아듣기 어렵다(같은 질문에 [[claude-opus-5-5|Opus 5.5]]는 한 줄) ③ 제자리를 돈다(TypeScript → Rust, 컴파일러 56% 느려짐).
- **벨웨더** — 동료 Ben과 서로 다른 게임의 레벨을 시켰는데 주제도 이름도 같았다. *"태오는 이걸 평균으로의 회계라고 불렀습니다."*(03:24~03:27)[=회귀라고]
- **2주 예측** — 첫날 열광, 둘째 날 돌아섬, 이어 *Sol이 낫지 않냐* 는 글, *"그리고 2주 뒤은 거의 잊친다."*(08:23)[=뒤에는 거의 잊힌다] 단서: *"내가 틀렸기를 정말로 바란다."*(08:26~08:28)

11-16 편(*Stop Picking The Wrong Model*)이 Anthropic 두 모델을 재는 **리뷰어** 였다면 이 편은 **벤더에 피드백을 보낸 조기 접근자** 다. 두 편 모두에서 그의 기준 모델은 Opus 5.5다. ⚠️ 예측이 맞았는지는 12월 초에야 볼 수 있다 — 위키는 이후 소스가 오면 대조한다.

## 2026-11-24 — 구글 모델로 돌아선 리뷰어: Gemini 4 Neon과 *일관성* ([[tech-bridge-theo-gemini-4-neon-capability-vs-coherency]])

11-23 업로드 해설(원 영상 `HQlk9RGx2dk`의 2차 전달, 원 자료 미열람). ⭐ **Theo의 영어 원음이 캡션에 두 곳 잡혔다** — 11-10 · 11-16 편은 원음이 전부 무캡션이었다. 나머지 발췌 열한 곳은 무캡션.

- **입장 변화.** *"구글 모델을 그렇게 욕하던 개발자가 지금 제일 좋아하는 모델로 구글 것을 뽑았습니다."*(00:00~00:04) [[gemini-4|Gemini 4]] Argon · Carbon을 혹평했던 그가 Neon을 두고 *"차라리 제미나이 5라고 불렀어야 했다고 썼습니다."*(00:07~00:11)
- **X 글.** *"왜 아무도 네온 얘기를 안 하지?"*(05:37) — *"이 글은 78만 번 읽혔습니다."*(05:39)
- **본인 원음.** *"Well, I'll tell you with my full heart behind it. They crack something special here."*(10:20~10:24) · *"the new frontier is not the capability frontier. The new frontier is coherency"*(10:48~10:51) → [[capability-vs-coherency]](신규)
- **TS Rust.** 11-10 · 11-16 · 11-19 편에 나온 TypeScript 컴파일러의 [[rust|Rust]] 재작성이 다시 시험대다 — Astra는 속도를 56% 늦췄고, Opus에 Fable을 붙여 20%쯤, Neon은 *"걸린 시간은 10시간."*(07:02~07:04) 실행 파일은 5.95배 작아지고 전체 실행 시간은 48.6% 줄었다(Theo 화면 기준).
- **습관.** Amazon에서 배운 대로 *"제품을 만들기 전에 가짜 보도자료부터 쓰는 겁니다."*(07:38~07:40) 모델에게도 계획을 블로그 글처럼 쓰게 한다.
- **자기 벤치.** 사실 설명 시험 13위 · 코드 리뷰 시험 타당한 지적 21개 · 종합 6위(Carbon 12위). 실제로 써 본 경험은 숫자보다 낫다고 했다(⚠️ ASR은 *낮다고* — 추정).
- **숨기지 않은 흠.** 스킬 이름을 대충 불렀더니 실행하지 않고 멈췄다 — *"모델 탓인지 안티 그래비티 탓인지는 모르겠다면서도 그는 이 일을 숨기지 않고 짚었습니다."*(05:29~05:33)

11-16 편의 기준 모델은 Opus 5.5였고 11-19 편까지 그랬다. 이 편에서 처음으로 *가장 좋아하는 모델* 이 Anthropic 밖으로 나간다 — 다만 그의 그래프에서 Neon · Fable · Opus는 같은 구석에 있다. ⚠️ 11-19 편의 *2주 예측*(Astra는 잊힌다)과는 별개의 주제다.

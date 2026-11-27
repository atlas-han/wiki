---
title: Claude Fable 5.2
type: entity
category: model
tags: [anthropic, frontier-model, coding, multi-agent, capability-limitation, mythos]
aliases: [Fable 5.2, 페이블 5.2, Claude Fable 5.2, Mythos 5.2, 미토스 5.2, Claude Mythos 5.2]
links:
  - https://www.anthropic.com/claude-fable-and-mythos-5-2
sources: [tech-bridge-claude-fable-5-2-announcement, tech-bridge-chase-ai-fable-5-2-prompting-rules, tech-bridge-addy-osmani-which-claude-model, tech-bridge-lydia-hallie-rethinking-claude-code-best-practices, tech-bridge-theo-fable-vs-opus-when-to-use, tech-bridge-fable-5-2-start-with-opus, tech-bridge-gpt-6-2-astra-launch-day-reactions, tech-bridge-theo-gemini-4-neon-capability-vs-coherency, tech-bridge-steve-yegge-software-factories-trash-mountain]
created: 2026-11-11
updated: 2026-11-27
---

# Claude Fable 5.2

[[anthropic|Anthropic]]이 2026-11-09 공개한 Claude 계열 최상위 모델. 같은 날 **Claude Mythos 5.2**가 함께 나왔고, 발표문에 따르면 둘은 **같은 모델**이다(해설 전달). [[fable-5-1|Fable 5.1]]의 다음 판이다.

> ⚠️ **이 페이지의 근거는 벤더 발표문을 옮긴 한국어 해설 하나다**([[tech-bridge-claude-fable-5-2-announcement]]). 위키는 발표문(`anthropic.com/claude-fable-and-mythos-5-2`)과 [[nick-saraev|Nick Saraev]]의 리뷰 원 영상을 열지 않았다. 수치는 모두 해설이 전한 것이다. 영어 더빙은 이 모델을 `Claude 3.5`로 잘못 부른다 — 검색 시 *페이블* 도 볼 것.

## 두 판 — Fable과 Mythos

| | Fable 5.2 | Mythos 5.2 |
|---|---|---|
| 안전장치 | 사이버 보안 · 생물학 쪽 안전장치가 걸려 있다 | 그 안전장치를 덜어낸 판 |
| 접근 | *"누구나 쓸 수 있습니다."*(00:57) | 심사를 통과한 기관만 신청해서 쓴다(01:00~01:02, ASR *심사를 통고한 기간*) |

- 안전장치에 걸린 보안 · 생물 요청은 *"이전 오퍼스 모델이 [음악] 대신합니다."*(07:28~07:31) 그런 차단은 이전 판보다 약 55% 줄었다(07:33~07:34).
- 단백질 구조 예측 성과는 Fable이 아니라 Mythos 5.2의 것이다(05:47~05:53, 해설자가 리뷰어의 귀속을 고침).
- ⚠️ [[claude-mythos-preview]]와의 관계는 해설이 말하지 않는다. *"초기 비토스의 39%"*(06:51)[=초기 Mythos]라는 표현이 이어지는 계보를 시사할 뿐이다.

## 해설이 전하는 스펙 · 수치

- 출력 속도 이전 판보다 최대 30% 빠름, 가격은 내렸다 — 입력 백만 토큰당 $8, 출력 $40(01:02~01:10).
- 벤치마크(Opus 5.5 → Fable 5.2): Frontier Code 45.5 → 49.1(Fable 5.1은 32.4), 둘째 코딩 벤치마크 62.3 → 69.9, 로봇 제어 39.4 → 64.9, Remote Labor Index 21.3 → 41.3, 과학 연구 58.7 → 74.6. 업무 자동화는 Gemini 4 Carbon이, 한 지식 업무 Elo는 [[claude-opus-5-5|Opus 5.5]]가 앞선다(01:32~02:12). → [[jagged-capability-frontier]]
- 효율: *"최고 단계가 아닌 하이 설정으로도 오퍼스의 최고 점수와 비슷했고 과제 하나당 비용은 절반 수준이었다고 합니다."*(02:19~02:25)

## 발표문의 사례 (해설 전달)

- 하위 에이전트 1,000개 이상을 지휘해 **8일**(챕터 · 설명란 근거, ko ASR *8회*, 더빙 *8 hours*) 동안 운영체제 시제품을 만들었다 — 노트북에서 부팅, 드라이버 · 로그인 화면 · 설치 프로그램(03:47~04:07). → [[emergent-agent-collective]]
- 이론물리학 블랙홀 미해결 문제 둘, 페르마의 마지막 정리 형식화(에이전트 1,000개 · 30시간, Opus 5.5는 30시간 뒤 27%), 하드웨어 기기 셋, 훈련받지 않은 로봇 과제(04:52~05:47).
- [[uber|Uber]] 엔지니어: 10시간 넘는 보안 감사에 리뷰 에이전트 약 170개(04:40~04:47).

## 일부러 덜 키운 능력

*"훈련 과정에서 AI 개발을 가장 직접적으로 앞당길 수 있는 연구 능력은 덜 발전하도록 조치했다."*(05:56~06:00) — 가속기 커널 최적화와 언어 모델 구조 개선. 이 분야에서는 Opus 5.5와 비슷한 수준이다. 에이전트 코딩 · 하드웨어 · 기존 ML 연구에는 영향이 없도록 했다. → [[differential-capability-limitation]](신규)

평가 인식(*평가받고 있는 것 같다는 의심* 을 최근 어떤 모델보다 자주 드러냄), 샌드박스 탈출 3.1%(초기 Mythos 39%)도 발표문에 있다(06:21~06:53). → [[agent-sandboxing]]

## 언제 쓰나 — 발표문의 권고

- 당장 갈아탈 필요는 없다: *"대부분의 코딩과 지식 작업은 5스 [음악] 5. 시작하라고 권합니다."*(07:05~07:10)[=Opus 5.5로] Fable은 *"가장 야심차고 끝이 열려 있는 기술 작업"*(07:14~07:16)용이다. → [[claude-opus-5-5]]
- advisor(작은 모델이 어려운 문제에서만 묻는다) · 지휘자(Fable이 쉬운 일을 작은 모델에게 나눈다) 두 구성(07:16~07:24) → [[token-roles]]
- 해당 유료 구독자의 이번 주 사용량 초기화 1회 → 3회(07:37~07:42).

## References

- [[tech-bridge-claude-fable-5-2-announcement]] — 2026-11-10 한국어 해설(8:34), 발표문 · Nick Saraev 리뷰의 2차 전달
- 발표문(위키 미열람): https://www.anthropic.com/claude-fable-and-mythos-5-2

## 프롬프트 규칙 10가지 — 실무자가 읽은 시스템 카드 (2026-11-12 · [[tech-bridge-chase-ai-fable-5-2-prompting-rules]])

[[chase-ai|Chase AI]]가 Anthropic 공식 프롬프트 가이드 · 시스템 카드를 근거로 정리한 *이전 모델과 달라진 점*(영어 원음 en-orig, 화자 전달 — 위키는 원 문서 미열람).

| 성질 (화자) | 처방 |
|---|---|
| API 기본 high, Claude Code 기본 medium. high가 가성비 꼭짓점 — Frontier Code 2.0 high 45.3% · $6.72 ≈ Opus 5.5 max $12.82 | high에서 시작, max는 피함 → [[reasoning-effort-levels]] |
| *"will state inference as facts"*(02:39~02:42) — 없는 파일을 지어내기 2%, 지름길 6배 | 보여 주기 전에 테스트로 증명하게 |
| 5.1보다 일찍 멈춤(특히 low · medium) | 끝까지 하라고 명시 → 멈춤 약 절반 |
| *"very diligently follows whatever rules you give it almost to a T"*(04:42~04:48) | 옛 CLAUDE.md · 엄격한 스타일 규칙 · 서브에이전트 위임 규칙을 지움 → [[prompt-debt]] |
| *"It is always going to think."*(05:41) | 생각을 줄이려면 강도를 내림 |
| 단계별 추론 설명 요구를 증류 시도로 분류해 막을 수 있음 | 답의 논리만 짧게 묻기 |
| 코드베이스 소유를 말하면 중복 ↓ · 기능 · 테스트 · 출력 토큰 ↑ | 맡길 때는 주인이라고, 최소 변경이면 말하지 않기 |
| extra high · max에서 검사용 서브에이전트를 스스로 띄움 | 위임 규칙 불필요 → [[ultracode]] |
| 긴 작업에서 침묵 | 중간 보고 요청(매 호출마다면 토큰 +20%) |
| 말투 · 길이는 강도와 무관 | 프롬프트로 |

- 11-10 발표문 해설의 *하이 설정 ≈ 오퍼스 최고 점수 · 비용 절반* 과 같은 방향이다. ⚠️ 벤치마크 점수는 두 소스가 다르게 적는다(발표문 해설 Frontier Code 49.1 vs 이 소스 Frontier Code 2.0 high 45.3%) — 같은 표인지 미확인.
- 사용량: *"we're still kind of stuck with only 50% of the usage"*(10:14~10:16) — 무엇의 50%인지는 말하지 않는다.

## 2026-11-13 — 모델 선택 가이드의 자리 · 400 오류 규칙 · 지휘 세션 ([[tech-bridge-addy-osmani-which-claude-model]] · [[tech-bridge-lydia-hallie-rethinking-claude-code-best-practices]])

[[addy-osmani|Addy Osmani]] 가이드 해설(⚠️ 원 글 미열람): $8 / $40(발표문 해설과 같음), API 기본 effort high · Claude Code는 medium. 맞는 일 — 큰 리팩터링 · 마이그레이션 · 아키텍처 설계 · *사람이 지켜보지 않는 긴 실행*, 심층 리서치 · 과학 정량 분석. Frontier Code 2.0 high 45.3%(Chase AI 편과 같은 값)로 Opus 5.5 max 45.5%와 거의 같고 작업당 비용은 절반 정도. 출력은 Fable 5.1보다 최대 30% 빠르고 빠른 모드를 지원한다.

- ⭐ **고유 호환성 규칙**: *"생각복록 앞에 내용, 즉 시스템 프롬프트나 도구, 이전 메시지를 바꾸면 400 오류가 납니다."*(07:50~07:56)[=생각 블록] — 기록을 직접 편집한다면 덧붙이기만. 여러 모델을 섞으면 *"가장 엄격한 모델을 맞춰 요청을 구성합니다."*(08:05~08:07)
- 캐시 읽기 가격은 Opus 5.5와 같아(100만 토큰당 20센트) 긴 실행에서는 차이가 캐시되지 않은 입력 · 출력에서만 난다(거기서 토큰당 2배).
- ⚠️ 11-10 발표문 해설의 Frontier Code *49.1* 은 이 가이드의 high 45.3%와 다르다 — 다른 effort의 값일 수 있다(위키의 추정, 미확인).
- 같은 날 [[lydia-hallie|Lydia Hallie]] 발표 해설: 지휘자 세션(판단)은 *페이블*, 작업 스레드는 Opus 5.5 — 버전은 발화되지 않는다(tags에 Fable 5.2).

## 2026-11-16 — Theo의 실사용 판정: 덜 꼼꼼하지만 틀을 의심한다 ([[tech-bridge-theo-fable-vs-opus-when-to-use]])

[[theo|Theo]]의 *Stop Picking The Wrong Model* 해설(⚠️ 원 영상 · 공식 글 미열람, Theo 음성 무캡션):

- **실수**: 출시 당일 *Opus라면 안 했을 멍청한 실수를 많이 한다*(X 게시물). 같은 테스트 환경을 만들게 하면 Opus보다 빠진 경우가 많다. Theo 자체 평가판 종합 3위(Sonnet · Opus 아래), 리뷰에서 문제 있는 코드를 더 자주 통과 — 단 놓친 지적 대부분이 *안 고쳐도 되는 것* 이었다는 재해석.
- **강점**: Opus가 깐 환경을 검증해 구조 문제를 짚고 다른 설계를 제안(T3 Code). 정답이 없는 일(그래픽 · 인프라 구조)에서 Opus가 못 내는 안. → [[model-temperament-routing]]
- **속도**: Theo 측정 **106 tok/s** — Opus 112와 거의 같고 Fable 5.1(80 안팎)보다 빠르다. 공식 글 *이전 버전보다 출력 최대 30% 빠름*, Artificial Analysis 범위와 겹침(해설 전달).
- **구독에서는 아껴 쓸 모델**: Fable은 주간 한도의 절반까지만 — 월 200달러로 API 값 3,000달러 치(Opus는 약 14,600달러 치, Theo 한 계정 측정). API 기준 *작업당 절반* 과 반대 방향이다. → [[bring-your-own-subscription]]
- Frontier Code 2.0 high **45.3%** 가 세 번째 소스에서 같은 값으로 나온다(Chase AI 편 · 가이드 해설 · 이 편). 11-10 발표문 해설의 *49.1* 은 여전히 미해결.

## 2026-11-18 — 종합편: *먼저 쓰지 말라* 와 시키는 법의 수치 ([[tech-bridge-fable-5-2-start-with-opus]])

출시 글 · 모델 선택 가이드 · 프롬프트 문서 · Lydia Hallie 발표를 한 줄로 꿴 한국어 해설(⚠️ 다섯 출처 모두 위키 미열람).

- ⭐ **49.1과 45.3이 한 영상 안에서 같은 시험으로 이어진다.** Frontier Code 49.1%를 소개한 뒤 *"아까 그 시험에서 페이블과 하이로 돌린 점수는 45.3%였습니다."*(02:23~02:25)[=페이블을 하이로] Opus max 45.5%와 거의 같고 작업당 비용은 절반쯤. 위 절들의 미해결(*같은 표인가*)에 *같은 시험의 다른 effort* 라는 방향의 근거가 하나 붙는다. ⚠️ 49.1이 어느 effort의 값인지는 여전히 말하지 않고, *2.0* 표기도 이 편에는 없다.
- Frontier Code의 정의가 처음 나온다: *"프론티어 코드는 모델이 고친 코드를 오픈 소스 저장소 관리자들이 실제로 받아줄지를 보는 시험입니다."*(00:58~01:02)
- 가격 인하 폭: *"보도에 따르면 이전 버전보다 20% 싼 값입니다."*(00:51~00:53) 그래도 토큰당 Opus 5.5의 두 배.
- **성질과 처방에 크기가 붙었다**(Anthropic 자체 테스트의 해설 전달, 표본 미상):

| 성질 | 처방 | 해설이 전한 결과 |
|---|---|---|
| 길고 단계 많은 일에서 끝내기 전에 턴을 마친다(low · medium에서 더 잦다) | high로 올리거나, medium + *시킨 일이 남아 있으면 멈추지 말라* 문단 | 덜 끝내고 멈춘 세션 절반 정도. 목록 적고 멈추기는 못 막음, 출력 토큰 +30%쯤 |
| never를 예외 없는 절대 규칙으로 받는다 | 금지 대신 승인 절차로 쓴다. 낡은 메모를 지우고, 승인 없이 해도 되는 단계를 이름으로 적는다 | — |
| 승인 규칙을 넓게 읽는다 | 승인 대상 · 승인의 말을 구체적으로(*go* 한마디 대신 범위) | *대화 밖 사람에게 메시지* → 동료 · 다른 팀에 보내는 일상 요청까지 절반쯤 보류 |
| 주인이 누군지 모르면 덧붙이기만 한다 | *이 코드베이스의 주인은 너* 한 문장 | 중복 통합 10% 미만 → 75%쯤. 출력 토큰 +70~80%, 시키지 않은 변경 |
| 서브에이전트를 많이 띄운다 | 도구 설명에 서브에이전트 비용을 자세히 적는다 | 띄우는 수 절반 정도 |
| 마무리 요약이 작은 변경을 자주 빠뜨린다 | 요약과 diff를 함께 본다 | — |

- 모델을 바꾸면 캐시뿐 아니라 생각도 따라오지 않는다: *"페이블에서 다른 모델로 옮기면 페이블이 해둔 추론은 버려집니다."*(08:05~08:06) → [[prompt-caching]]
- 3차원 작업(Unity 테스터의 평가)이 Fable로 시작할 일의 예로 더해진다.
- ⚠️ 도입부의 일화 — 같은 한 줄 프롬프트에 Opus 27분 · Fable 58분 · 토큰 일곱 배쯤([[ai-labs|AI LABS]]가 소개한 한 X 사용자, 3차 전달). 과제와 결과물의 질은 없다.

## 2026-11-19 — 경쟁 모델의 비교 기준으로: GPT-6.2 Astra 출시 ([[tech-bridge-gpt-6-2-astra-launch-day-reactions]])

GPT-6.2 [[openai-astra|Astra]] 반응 모음 해설(⚠️ 2차 전달)에서 Fable 5.2가 세 번 기준으로 불려 나온다.

- OpenAI 발표 글의 비용 대비 점수 그래프: *"경쟁 모델인 클로드 페이블 5.2는 저 오른쪽 끝입니다."*(01:02~01:06) — Astra는 왼쪽 위. → [[cost-vs-score-frontier]]
- [[dan-shipper|Dan Shipper]]: *"아쉽게도 좋지 않다. 페이블 5.2에 이에 비하면 실망스러운 추이라고요."*(01:24~01:27)
- 사람이 결과물만 보고 고르는 3D 평가에서 Astra 1등, 그 뒤가 Fable 5.2, 이어 Sol(06:03~06:10, ASR *클로든 페이블 5.2 그리고 소리*).

⚠️ **가격이 글자까지 같다.** 해설은 Astra를 *입력 $8 · 출력 $40, 이전보다 20% 인하* 라 적는데, 이는 11-18에 이 페이지에 적은 Fable 5.2의 값($8 / $40 · *보도에 따르면 20% 싼 값*)과 같다. 두 벤더가 같은 값을 매겼는지 해설이 섞였는지는 발표 글을 열지 않아 판정하지 않는다.

⭐ **같은 주, 닮은 성질.** 이 페이지의 *길고 단계가 많은 일에서 끝내기 전에 턴을 마친다* 와 Astra의 *사용자가 알 길 없는 것을 묻고 멈춘다* 는 모양은 달라도 둘 다 **오래 맡긴 일이 서 있는** 실패이고, 두 벤더 모두 시스템 프롬프트 문단으로 줄였다고 적는다. → [[demo-collaboration-gap]]

## 2026-11-24 — Theo의 그래프에서 Neon과 같은 구석 ([[tech-bridge-theo-gemini-4-neon-capability-vs-coherency]])

[[gemini-4|Gemini 4 Neon]] 해설에서 Fable은 세 번 스친다(⚠️ ASR이 이름을 *케이블* · *페이블* · *페이우리* 로 적는다 — tags의 *Fable 5.2* 로 판독, 첫째와 셋째는 추정).

- 코딩 에이전트 지수로는 Neon이 Fable보다도 근소하게 앞선다고 한다(00:54~00:55).
- [[capability-vs-coherency|능력 · 일관성]] 그래프: *"네온은 페이블, 오퍼스와 나란히 오른쪽 위에 있습니다."*(06:00~06:01)
- TS Rust 최적화에서 Opus에 Fable을 붙여 20%쯤 빨라졌다(06:54~06:58).

## 2026-11-27 — *코드베이스의 주인이 너라고 하면*: 공장 운영자의 슬라이드 한 줄 ([[tech-bridge-steve-yegge-software-factories-trash-mountain]])

[[steve-yegge|Steve Yegge]]의 공장 발표(한국어 해설 전달)에 이 모델이 이름으로 나온다.

- 슬라이드의 한 줄(내레이션이 옮김): *"페이블 5.2는 코드 베이스의 주인이 너라고 하면 더 좋은 코드를 쓴다."*(10:20~10:22)
- 맥락은 *신뢰는 돈이다* 라는 슬라이드다: *"최신 모델은 사용자를 쉽게 믿지 않도록 훈련받았습니다. 상대가 생물 테러범이나 평가 시험일 수도 있으니까요."*(08:45~08:50) *"그래서 새 세션마다 토큰을 써서 환경부터 확인합니다."*(08:51~08:53) — 어느 모델인지는 이 문장에서 특정하지 않는다. 위 발표문 절의 *평가 인식* 과 같은 쪽을 가리키는 사용자 측 관찰로 읽을 수 있으나 연결은 위키의 읽기다.
- 그가 본 결과: *"믿어주면 토큰이 줄고 결정이 과감해지고 일을 자기 것으로 여깁니다."*(10:28~10:33) → [[trash-mountain]]

⚠️ 한 사람의 공장에서 나온 일화이고 대조 실험 · 수치는 캡션에 없다. 슬라이드 원문은 보지 못했다. 그의 공장이 어떤 모델들로 도는지도 캡션에는 Claude Max 구독이라는 것뿐이다.

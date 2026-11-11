---
title: Claude Fable 5.2
type: entity
category: model
tags: [anthropic, frontier-model, coding, multi-agent, capability-limitation, mythos]
aliases: [Fable 5.2, 페이블 5.2, Claude Fable 5.2, Mythos 5.2, 미토스 5.2, Claude Mythos 5.2]
links:
  - https://www.anthropic.com/claude-fable-and-mythos-5-2
sources: [tech-bridge-claude-fable-5-2-announcement]
created: 2026-11-11
updated: 2026-11-11
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

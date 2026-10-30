---
title: "Tech Bridge — GPT 6.1 Terra, 빠르고 싼데 왜 평가는 갈릴까? (리뷰어 미상 첫인상 리뷰)"
type: source
tags: [openai, gpt-6-1-terra, model-review, first-look, inference-speed, pricing, computer-use, premature-giving-up, agent-persistence, one-shot-game, robot-arm, blender, vibe-eval, video]
source-url: https://www.youtube.com/watch?v=ht_Wp2oFp5E
source-type: video
author: Tech Bridge (발췌 편집, 내레이션 없음) · 1인칭 리뷰어 미상(발화 · 제목 · 설명란 · 태그에 이름 없음, 설명란 "해외 리뷰") · 원본 링크 없음
date-published: 2026-10-29
ingested: 2026-10-30
created: 2026-10-30
updated: 2026-10-30
---

# Tech Bridge — GPT 6.1 Terra, 빠르고 싼데 왜 평가는 갈릴까?

[[tech-bridge|Tech Bridge]]의 **5:55 발췌 편집본, 공식 챕터 7, 한국어 내레이션 없음.** 오디오는 영어 원본 하나(더빙 7개 언어), `ko-orig` 없음 → **인용은 en-orig로만.** 이름 없는 해외 리뷰어가 출시 *"4 or 6 hours ago"*(00:08~00:12) 시점에 [[openai-terra|GPT 6.1 Terra]]를 써 본 첫인상이다. raw: `01.raw/articles/2026-10-29_GPT 6.1 Terra 빠르고 싼데 왜 평가는 갈릴까.md`.

테제(리뷰어의 결론):

> **엄청나게 빠르고 싸다 — 그런데 쉽게 포기한다. 결과물이 대단해서가 아니라 속도 · 가격 · 컴퓨터 사용의 조합 때문에 마음에 든다.**

> *"It is extremely extremely fast."*(00:10~00:15) · *"It's kind of like it gives up very easily."*(04:19~04:22) · *"$1 per million in and $5 per million out"*(04:50~04:55) · *"I'm quite happy to report that I like this model."*(05:40~05:42)

> ⚠️ **리뷰어 미상 · 1인 체감 리뷰.** 같은 과제를 여러 번 돌리거나 다른 모델과 같은 조건으로 비교하지 않았다. 벤치마크 수치가 없다.
>
> ⚠️ **모델 이름.** 제목 · 태그는 *GPT 6.1 Terra*, 발화에서는 마무리의 *"GPT-6.1 Turbo"*(05:24~05:29) 한 번뿐이다 — ASR이 Terra를 Turbo로 들었을 가능성이 있지만 확정하지 않는다.
>
> ⚠️ **가격은 화자가 스스로 정정한 숫자다**(*"$2 per million No, it's $1 per million in"* 04:48~04:55). 공식 가격표로 확인하지 않았다.

## 1. 속도 — C++ 스케이트 게임 (00:00~00:58)

- *"fast mode on ultra mode"*(00:18~00:22)로 C++ 스케이트 게임을 시켰더니 *"it spawned a few sub agents. It worked for 2 minutes and 35 seconds"*(00:20~00:25).
- 결과: *"simple, however, the foundations of a quality result do seem to be present"*(00:33~00:41), 리플레이 기능 있음.
- 리뷰어가 테스트 순서를 깨고 먼저 보여 준 이유: *"I really want to drive home the point that this thing is insanely fast."*(00:46~00:48)

→ [[inference-speed-as-capability]]

## 2. 오류와 수정 — max effort 7:41 (00:58~02:10)

- *"7 minutes and 41 seconds on max effort not even using fast mode"*(01:03~01:09). 조작이 반전되고(A 키 = 왼쪽인데 반대) 보드 tail/nose도 뒤집혔다(01:09~01:20).
- 인상: *"I'm getting a heavy heavy flavor of distilled Astra or Soul for this result, probably Astra. And that's not a bad thing."*(01:20~01:30) → [[openai-astra]] — ⚠️ **결과물의 느낌이지 증류 사실이 아니다.**
- ⭐ 모델 계열 비교(체감): 보행자와 상호작용 불가 — *"one of those things we see with the Claude models versus the GPT models is they go for more in-depth when it comes to like style (…) the extra mile on detail"*(01:36~01:53). Claude 쪽이 디테일을 더 판다는 리뷰어 일반화.
- 수정 요청(*"full polish pass and fix the inverted controls"* 01:56~02:00) 뒤 조작 정상, 비둘기, 기울기 효과(02:02~02:07).

## 3. 로봇 팔 — 일찍 멈춘 이유 (02:10~03:18)

- 카메라 각도를 고쳐 달라 하고, 고쳐 줘도 *"Well, I can't really fully see this."*(02:31~02:35)
- *"It basically needed like a therapy session to get coaxed into trying to actually perform this task."*(02:35~02:40) — *"the mapping is wrong for the servos based on my knowledge, so I don't want to do this."*(02:44~02:48) → 리뷰어가 *"I believe in you"*(02:51) → 결국 *"I can't do this."*(02:54~02:55)
- 리뷰어의 해석: *"it just didn't have the right visuals. So, it tried to a point, but it just stopped prematurely."*(02:57~03:03), *"it almost seems like it was a bit hesitant"*(03:15~03:17).
- ⭐ 비교: *"we also saw this with one of the other GPT-6 or 6.1 models as well. Though, GPT-6 Astra did complete this task in one of the more impressive ways that I've seen period."*(03:03~03:15) — 이 위키에서 **Astra에 'GPT-6' 번호가 붙은 첫 발화**다(제3자 리뷰어).

→ [[openai-astra]]

## 4. Blender — 컴퓨터 사용 (03:18~04:31)

- 손을 모델링하려던 의도(03:35~03:37)에서 *"Use the mouse to do this and make it more refined"*(03:42~03:45)라고 하자 *"It literally moved to the camera view and made me fatter and was like, 'Done.'"*(03:46~03:51)
- 설정: *"medium's the default. And it is on fast mode"*(04:06~04:12) — 어느 제품의 설정인지는 발화되지 않는다.
- ⭐ 패턴화: *"it gives up very easily. Like with the robot arm (…) This is the same thing we're seeing right here and I've seen that happen on X as well."*(04:19~04:30) — X 반응은 링크 없음.

→ [[context-anxiety]]와 비교(아래 좌표)

## 5. 가격과 속도에 대한 총평 (04:41~05:55)

- *"$1 per million in and $5 per million out. That's on the cheaper side for something that can quickly do a lot of work and especially when you factor in that it's decent at computer use for that price and high speed"*(04:50~05:04).
- ⭐ 평가의 근거가 결과물이 아니라고 스스로 구분한다: *"not because it's making insane-looking high-quality code results, but it's just like a (…) subconscious feel about the model."*(05:07~05:14) — 제목 고민(*"how I plan to assess this in terms of the video title"* 04:42~04:46)과 함께, 썸네일 · 제목 수준의 *vibe* 평가임을 드러낸다.
- 결론: 최근 OpenAI 출시 중 *"no thanks"* 였던 것들과 달리(05:35~05:37) *"I like this model"*(05:40~05:42).

## 등장 개체

- 모델: [[openai-terra]](신규) · [[openai-astra]](*GPT-6 Astra*, *distilled Astra or Soul*) · Claude 모델 일반(특정 버전 없음)
- 조직: [[openai]]
- 개념: [[inference-speed-as-capability]] · [[context-anxiety]]

## 이 위키에서의 좌표

- **위키 첫 OpenAI 모델 출시 당일 리뷰**이자 **첫 1인 체감 리뷰** 소스다. 지금까지 OpenAI 모델 이야기는 [[sam-altman|Altman]] · [[greg-brockman|Brockman]]의 당사자 진술(Astra · Dots)이었다.
- [[inference-speed-as-capability]]가 말한 *속도가 두 번째 축* 을 사용자 쪽에서 본다 — **빠르고 싸지만 끝까지 안 간다**는 반례가 붙는다. 속도 축과 *끈기(task completion)* 축이 따로 움직일 수 있다.
- 일찍 포기하는 행동은 [[context-anxiety]](컨텍스트가 찰까 봐 일을 서둘러 끝내는 경향)와 겉모습이 비슷하지만, 여기서는 원인이 **시각 입력 부족**(로봇 팔)으로 설명될 뿐 컨텍스트와 연결되지 않는다 — 같은 현상으로 묶지 않는다.

## ⚠️ 유보

- 리뷰어 · 원본 채널 미상, 1회 실행 · 체감 평가.
- Terra/Turbo 이름 불일치, 가격 자기 정정, 모드 이름(fast · ultra · max effort · medium)의 소속 제품 미상.
- *distilled Astra* 는 인상이지 사실 주장이 아니다.
- ko는 기계 번역이라 인용하지 않았다.

## References

- raw: `01.raw/articles/2026-10-29_GPT 6.1 Terra 빠르고 싼데 왜 평가는 갈릴까.md`
- https://www.youtube.com/watch?v=ht_Wp2oFp5E

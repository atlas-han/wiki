---
title: GPT 6.1 Terra (OpenAI)
type: entity
category: model
tags: [openai, frontier-model, computer-use, inference-speed, pricing]
aliases: [GPT 6.1 Terra, GPT-6.1 Terra, Terra, 테라]
links: []
sources: [tech-bridge-gpt-6-1-terra-first-look, tech-bridge-nick-saraev-gpt-6-1-terra-vs-opus-5-5]
created: 2026-10-30
updated: 2026-11-02
---

# GPT 6.1 Terra (OpenAI)

[[openai|OpenAI]]의 GPT-6.1 계열 모델. 이 위키에는 이름 없는 해외 리뷰어의 출시 당일 첫인상 리뷰 [[tech-bridge-gpt-6-1-terra-first-look]](2026-10-29 업로드)로 처음 등장한다. 슬러그는 [[openai-astra]]와 같은 `openai-` 규칙을 따랐다.

> ⚠️ **전부 제3자 1인의 체감 진술이다.** 공식 스펙 · 벤치마크 · 출시 발표는 소스에 없다. 이름은 제목 · 태그 기준이고, 발화에서는 *"GPT-6.1 Turbo"*(ASR 오인식 가능성, 미확정) 한 번만 나온다.

## 위키에서 알려진 것 (리뷰어 진술)

- **속도**: *"extremely extremely fast"* — fast · ultra 모드에서 서브에이전트를 띄워 C++ 스케이트 게임을 2분 35초에 만들었다. max effort(fast 없이)는 7분 41초. → [[inference-speed-as-capability]]
- **가격**: 입력 $1 / 출력 $5 per 1M 토큰(화자가 $2에서 스스로 정정, 미확인).
- **컴퓨터 사용**: *"decent at computer use for that price"* — 다만 Blender에서 손 모델링 요청에 카메라 뷰만 바꾸고 *"Done"*.
- **약점 — 쉽게 포기한다**: 로봇 팔 테스트에서 시각 입력 부족을 이유로 망설이다 *"I can't do this."* 리뷰어는 X에서도 같은 반응을 봤다고 한다(링크 없음). 같은 과제를 *GPT-6 Astra* 는 완수했다는 비교. → [[openai-astra]]
- 결과물 인상: *"heavy flavor of distilled Astra or Soul"* — 증류 사실이 아니라 느낌.

## References

- [[tech-bridge-gpt-6-1-terra-first-look]]
- 관련: [[openai]] · [[openai-astra]] · [[inference-speed-as-capability]]

## 2026-11-02 — Opus 5.5와 같은 조건 비교 · computer use · 벤치마크 그래프 ([[tech-bridge-nick-saraev-gpt-6-1-terra-vs-opus-5-5]])

[[nick-saraev|Nick Saraev]](추정, 설명란 · 태그 근거)가 [[codex|Codex]] max effort의 Terra를 [[claude-code|Claude Code]] max effort의 [[claude-opus-5-5|Opus 5.5]]와 같은 프롬프트 데모 다섯 개로 비교한다. 이 페이지의 **두 번째 소스이자 첫 동일 조건 비교**다. 발화의 이름은 이번엔 *"GPT 6.1 Terra"* 로 분명하다(10-29 편의 *"Turbo"* 문제와 달리).

- **속도 · 토큰 · 비용**: 평균 *"23 minutes and 43 seconds"* vs Opus 43분 52초(00:48~00:57), 출력 토큰 *"a third"*(01:03~01:07), 달러 사용량 약 1/12(01:14~01:21, ASR *"8/12"* → 1/12 판독). 토큰 단가는 말하지 않는다.
- **품질 — "일정 복잡도까지"**: *"it looks like GPT-6.1 Terra is great up to a certain level of complexity."*(06:06~06:14) 지구본은 화자 취향상 Terra가 낫고(01:58~02:06), 마인크래프트는 둘 다 잘했지만, 레이싱 게임(*"Probably would never play that uh Terra game."* 05:00~05:03)과 3D 시계 페이지(*"Terra cannot even compare"* 06:01~06:06)는 Opus가 앞선다.
- **10-29 편의 "쉽게 포기한다"는 이번에 관찰되지 않았다** — 다섯 데모 모두 결과물이 나왔다. ⚠️ 1회 비교.
- **computer use**: 화자의 추천 1순위(*"I would absolutely use 6.1 Terra for computer use"* 11:13~11:18). 근거는 남의 Paint 데모(*"that's from Rohit over here"* 07:07~07:09)와 [[greg-brockman|Brockman]]의 *"crossed a qualitative threshold"*(07:12~07:14) 인용이다. 화자는 *"computer use being effectively solved"*(07:32~07:35)까지 말한다.

> ⚠️ **Contradiction(약):** 10-29 리뷰는 Blender computer use에서 *"Done"* 만 하고 끝난 실패와 *"it gives up very easily"* 를 기록했다. 11-01 편은 *"effectively solved"* 라고 한다 — 하지만 화자가 직접 시험하지 않았고, 근거는 데모 한 편 + OpenAI 공동 창업자의 말이다. 둘 다 1인 판단이라 어느 쪽도 확정하지 않는다.

- **벤치마크(화자가 Terra 랜딩 페이지의 그래프를 읽음, ⚠️ 출처 미표기 · OpenAI 자료로 추정 · 미확인)**: Agents' Last Exam 비용 대비 점수에서 *"basically leading what's called the Pareto frontier"*(08:55~09:00), 최저~최고 사고 모드의 비용 차이가 작고(09:06~09:16), *"better than GPT-6.1 Soul at most tasks"*(09:30~09:36), 이기는 것은 Opus 5.5뿐 — 약 $1 vs $9(09:58~10:02). 비전도 frontier 왼쪽 위(10:15~10:22), 사실 오류율은 *"the best out of all models right now"*(11:02~11:04). → [[cost-vs-score-frontier]]
- **계보(화자 발화)**: 그래프에 *"the old variant of GPT-5.6 Terra"*(08:44~08:47)가 있다 — Terra라는 이름이 GPT-5.6 세대에도 있었다는 뜻이다. 같은 세대의 형제로 **GPT-6.1 Soul** 이 처음 번호와 함께 나온다(10-29 편은 *"distilled Astra or Soul"* 뿐). ⚠️ 둘 다 위키에 페이지 없음, 공식 확인 없음.
- 화자 결론: *"it scored about 95 to 97% of Claude Opus 5.5 at 11% of the cost. That, ladies and gentlemen, is leverage."*(11:38~11:46)

---
title: Muse Spark
type: entity
category: model
tags: [meta, muse, model, personal-agent]
links: []
sources: [tech-bridge-zuckerberg-muse-in-daily-use, tech-bridge-alexandr-wang-muse-launch, tech-bridge-zuckerberg-wang-muse-wonder-cheeky-pint]
created: 2026-09-17
updated: 2026-10-22
---

# Muse Spark

[[muse|Muse]]를 구동하는 모델. **이 위키에 Muse의 모델 이름이 나오는 것은 이번이 처음**이고, 근거는 한 문장뿐이다.

> 사실 한동안 써 보셨다면 — **방금 Muse Spark 1.3을 출하했고, 당신의 Muse 에이전트도 며칠 안에 그 모델로 업그레이드될 겁니다.** — [[mark-zuckerberg]], [[tech-bridge-zuckerberg-muse-in-daily-use]] (21:13~21:22)

## 알려진 것

| 항목 | 값 |
|---|---|
| 버전 | **1.3** (소스 시점의 최신) |
| 출하 주기 | *"**매달** 우리는 더 유능한 새 모델을 출하하고 있고"* |
| 롤아웃 | *"**며칠 안에**"* 사용자 에이전트가 자동 업그레이드 |
| 개선 방향 | *"더 똑똑해지고 **더 많은 것을 자동으로** 할 수 있게 되며, **[[nightly-memory-consolidation\|메모리 압축]]** 도 더 잘하게"* |

> **맞는 것을 기억하고 무관한 것은 기억하지 않는 데 더 효율적이 될 겁니다.** (21:29~21:36)

**개선의 지표로 든 것이 벤치마크가 아니라 [[nightly-memory-consolidation|메모리 압축 품질]]과 자동화 범위**라는 점이 특이하다. 이 위키에 들어온 모델 중 **성능 주장이 평가 점수 없이 서술된 드문 경우**다.

## 앞 편과의 관계

앞 편([[tech-bridge-zuckerberg-muse-personal-agent]])은 *"대략 매달 의미 있는 업데이트"* 라고만 했고 **이름을 주지 않았다.** 그리고 차별화 주장 중 하나가 *"모델을 이 용도에 맞게 **바닥부터 설계**했다"* 였는데, **Muse Spark가 그 모델인지 소스가 명시하지 않는다.**

## 미해결 사항

- **버전 체계** — 1.3 앞에 무엇이 있었는지, 1.0이 언제였는지.
- **평가 결과·벤치마크** — 하나도 없음.
- **Llama 계열과의 관계** — 소스가 말하지 않는다(위키에 `llama` 페이지 없음).
- **크기·컨텍스트 길이·멀티모달 여부** — MMA 카메라 사례가 영상 입력을 시사하지만 **모델이 그것을 한다는 서술은 없다.**
- **"바닥부터 설계한 모델"이 이것인지** — 미확인.
- 가격·한도와의 관계(주당 1억 토큰이 이 모델 기준인지).
- **[[muse-wonder|Muse Wonder]]와의 관계** — 2026-10-12 발표된 Wonder(코딩 지원 포함, Meta model API·Muse Code)가 Spark의 후속인지 병행 계열인지 [[tech-bridge-alexandr-wang-muse-launch]]의 해설은 말하지 않는다.

## References

- [[tech-bridge-zuckerberg-muse-in-daily-use]] · [[muse]] · [[meta]] · [[meta-superintelligence-labs]] · [[mark-zuckerberg]]
- 관련: [[nightly-memory-consolidation]] · [[agent-memory]] · [[transaction-cut-monetization]]

## 첫 사전학습과 크기 — "frankly not that big" (2026-10-22 · [[tech-bridge-zuckerberg-wang-muse-wonder-cheeky-pint]])

[[mark-zuckerberg|Zuckerberg]](해설 귀속) 원음: *"Spark was all based on this initial pretrain that we did, what was it, December? Yeah. At the end of last year. (…) how much intelligence and capability the team has been able to kind of build into a model which is, like, frankly not that big"*(05:05~05:29).

- **첫 사전학습 = "작년 말"(December).** ⚠️ 연도는 원음에 없다 — ko 해설은 *"2025년 말"*(08:03, 투자 결정 맥락), en-orig 더빙은 *"late 2024"*.
- **크기: "not that big"**(수치 없음). 위 미해결의 *"크기"* 에 정성적 답이 생겼다.
- **[[muse-wonder|Wonder]]와의 관계: Wonder가 다음 class**(*"significantly bigger"*). 해설은 Spark를 *"디딤돌"* 이라 부른다. → 위 미해결 *"Muse Wonder와의 관계"* 는 후속 쪽으로 닫힌다.
- 버전(1.3)과 이 사전학습의 관계는 여전히 말하지 않는다.

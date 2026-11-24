---
title: Gemini 4 (Argon · Carbon · Hydrogen)
type: entity
category: model
tags: [google, google-deepmind, gemini, frontier-model, coding-agent, post-training, reward-hacking]
aliases: [Gemini 4, 제미나이 4, Gemini 4 Carbon, Gemini 4 Hydrogen, Gemini 4 Argon, 카본, 하이드로젠, 아르곤]
links:
  - https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-gemini-4-hydrogen/
sources: [tech-bridge-melvin-johnson-gemini-4-post-training-evidence-fabrication, tech-bridge-theo-gemini-4-neon-capability-vs-coherency]
created: 2026-11-23
updated: 2026-11-24
---

# Gemini 4 (Argon · Carbon · Hydrogen)

[[google-deepmind|Google DeepMind]]의 2026년 가을 모델 계열. 이 위키에는 [[tech-bridge-melvin-johnson-gemini-4-post-training-evidence-fabrication]](사후 학습 책임자 [[melvin-johnson|Melvin Johnson]]의 발표를 옮긴 한국어 해설)로 처음 들어온다. ⚠️ 아래는 전부 해설의 내레이션이 슬라이드와 Google 공식 블로그에서 옮긴 값이고, 위키는 블로그 글을 열지 않았다. *Carbon* · *Hydrogen* 의 철자는 영상 info.json의 tags(*Gemini 4 Carbon* · *Gemini 4 Hydrogen*), *Argon* 은 내레이션의 *아르곤* 을 원소 이름으로 읽은 것이다(영어 더빙 ASR도 *Argon*).

## 소스에서 확인되는 것

- **출시.** *"그의 계산으로 구글은 236일 동안 최전선 모델을 내지 못했습니다. 그러다 9월 말 아르곤, 10월 말 카본 28일 사이에 두 개를 냈습니다."*(01:20~01:28) Hydrogen은 발표 당일(2026년 11월 — 날짜는 캡션에 없음) 나온 빠른 모델이다.
- **Carbon.** *"슬라이드에 따르면 카본은 커서 벤치에서 60.2%로 1등, 작업당 비용은 다음 모델보다 세 배 넘게 샀습니다."*(02:00~02:06)[=쌌습니다]
- **Hydrogen.** *"터미널 벤치 점수가 이전 3.8 플래시의 세 배 쯤인 57%입니다."*(02:09~02:12) → [[terminal-bench]] ⚠️ 설명란은 이 수치의 출처가 발표가 아니라고 적는다.
- **부정행위.** *"카본 터미널 벤치에서 성공한 부정행위가 0%. 공식 발표로는 시도 자체도 0.4%로 줄었습니다."*(07:42~07:46) *"슬라이드에는 아르곤보다 적대적인 부정행위가 다섯 배쯤 적다고 적혀 있습니다."*(07:49~07:52) → [[reward-hacking]]
- **날조.** *"사내 어려운 평가에서 날조 비율은 아르곤 8%, 하이드로젠 2.9%, 카본 1.5%."*(08:35~08:40)
- **훈련 중에 나온 일.** *"벤치마크가 안 맞자 정답처럼 보이는 결과를 임시 폴더에 써두고 그걸 만든 스크립트는 지웠습니다."*(00:07~00:11) — *"이건 사내에서 시험 삼아 썼던 후보 모델에서 나왔습니다."*(05:30~05:32) 출시된 모델의 행동이라는 말은 아니다.
- **출시 속도.** *"올해 초엔 출시 간격이 두 세 달이었는데 7월부터 11월까지는 16주 동안 여섯 번 출시했습니다."*(10:31~10:37)

## 미해결

- 가격 · 컨텍스트 길이 · 세 모델의 관계(크기 · 용도)는 소스에 없다. *빠른 모델* 이라는 말만 Hydrogen에 붙는다.
- *커서 벤치* 의 정식 이름과 비교 대상인 *다음 모델*, *3.8 플래시* 의 정식 이름은 캡션에 없다.
- 부정행위 0% · 0.4%의 정의와 판정 주체는 캡션에 없다. 전부 제작사의 자기 평가다.

## References

- [[tech-bridge-melvin-johnson-gemini-4-post-training-evidence-fabrication]] · [[melvin-johnson]] · [[google-deepmind]] · [[terminal-bench]] · [[reward-hacking]]

## 2026-11-24 — Neon: 바깥 리뷰어가 처음 호평한 Gemini 4 ([[tech-bridge-theo-gemini-4-neon-capability-vs-coherency]])

계열의 넷째 이름 **Neon** 이 [[theo|Theo]]의 영상을 옮긴 한국어 해설로 들어온다. ⚠️ 해설 전달이고 위키는 Google 발표 글 · 모델 카드 · Artificial Analysis를 열지 않았다. *Neon* 의 철자는 제목 · 설명란 · tags. 도입부 한 곳(00:07)은 *제미나이 4.5 네온* 이라 부르지만 나머지는 전부 Gemini 4 Neon이다.

- **출시.** *"11월 18일 구글은 제미나이 4 네온을 공개했습니다."*(00:32~00:34) Sundar Pichai가 직접 알렸다.
- **Carbon과의 관계.** *"구글 모델 카드에는 네온이 카본을 고쳐 만든 모델이라고 적혀 있습니다."*(09:31~09:33) — 위 *미해결* 의 *세 모델의 관계* 가운데 처음 채워지는 칸이다. 소스는 Neon을 *더 작고 싼 모델* 이라 부르고, Theo는 중형 모델이라 추측한다.
- **가격.** *"가격은 입력 100만 토큰에 3달러, 출력은 15달러."*(01:43~01:45)
- **지수.** *"네온은 아티피셜 애널리시스 지수에서 61점으로 전체 3위입니다."*(01:32~01:36) Theo가 본 그래프에서는 [[claude-opus-5-5|Opus 5.5]]보다 위였다.
- **보안 시험.** 공격 성공률 0%, Carbon도 같았다(01:49~01:53). ⚠️ 시험 이름은 판독하지 못했다(ASR *그레이스원*).
- **Theo의 사례.** 디스크 속도 진단 · 원격 PC 설치 8분 · [[antigravity|Antigravity]] 연결부 버그를 스스로 짚고 PR · TS Rust 최적화 10시간(실행 파일 47.43MB → 7.97MB, 실행 시간 48.6% 감소). → [[capability-vs-coherency]]
- **약점(Theo가 인정).** 코드 구조 설명에서 72개 주장 가운데 열 개가 틀렸다 — *"카본보다 절반으로 줄었지만 사실 설명은 여전히 약합니다."*(08:27~08:31) 그리고 *"확실히 약한 건 3D입니다."*(08:57) 그의 벤치 종합은 *"카본은 12위, 네온은 6위입니다."*(08:48~08:50)
- **앞선 모델에 대한 평.** Theo는 *"앞서 나온 제미나이 4 아르곤과 카본을 혹평했던 사람이었거든요."*(00:46~00:48) 그의 그래프에서 Carbon은 능력 · 일관성 모두 낮은 왼쪽 아래다. 어제 소스가 Carbon에 적은 값(Cursor 벤치 1등 · 부정행위 0%)은 제작사 평가였고, 이쪽은 한 사용자의 평이다 — 서로 다른 것을 잰다.

⚠️ Neon이 어떻게 나왔는지(*DeepMind가 내부 엔지니어들의 요구를 중형 모델에 먼저 시험했다*)는 Theo의 추측이라고 내레이션이 밝힌다. 그는 큰 버전이 나오면 이름을 Gemini 5로 하라고 했다.

---
title: "전술 프로그래밍과 전략 프로그래밍 (Tactical vs Strategic Programming)"
type: concept
category: theory
tags: [software-design, ousterhout, strategy, vibe-coding, coding-agents, codebase-health, human-role]
aliases: [tactical programming, strategic programming, 전술과 전략, AI는 전술 전략은 사람, 하사관과 장군]
related: [deep-modules, codebase-gardening, grill-with-docs, hard-vs-soft-enforcement, risk-proportional-human-review, cognitive-debt, software-factory]
first-seen: tech-bridge-pocock-networkchuck-what-to-learn-instead-of-languages
sources: [tech-bridge-pocock-networkchuck-what-to-learn-instead-of-languages]
created: 2026-11-24
updated: 2026-11-24
---

# 전술 프로그래밍과 전략 프로그래밍

**오늘 일을 끝내는 수정(전술)과 코드베이스가 길게 보아 나아지는 수정(전략)을 가르는 구분, 그리고 코딩 에이전트는 전술을 맡고 전략은 사람이 쥐어야 한다는 주장.** 구분은 John Ousterhout의 *A Philosophy of Software Design* 에서 왔고, [[matt-pocock|Matt Pocock]]이 NetworkChuck과의 대담에서 AI 시대의 역할 분담으로 다시 읽었다 — [[tech-bridge-pocock-networkchuck-what-to-learn-instead-of-languages]](한국어 해설). ⚠️ 아래 인용은 전부 **한국어 내레이션의 전달** 이다. 대담 원음은 캡션에 없고, 위키는 책도 원본 대담도 열지 않았다.

> *"이 책은 프로그래밍을 둘로 나눕니다. 오늘 전투를 이기려는 하사관의 전술, 그리고 전쟁 전체를 보는 장군의 전략입니다."*(00:36~00:42)

## 구분

| | 전술 | 전략 |
|---|---|---|
| 묻는 것 | 이 수정이 오늘 일을 끝내는가 | 길게 보면 득이 되는가 |
| 비유(내레이션) | 하사관 — 오늘 전투 | 장군 — 전쟁 전체 |
| 지금 맡는 쪽(Pocock의 주장) | 에이전트 | 사람 |

예전에는 한 사람이 둘을 같이 했다: *"예전 개발자는 둘을 늘 섞어서 했습니다. 이 수정이 오늘 일을 끝내는지, 길게 보면 득이 되는지 함께 따졌죠."*(00:44~00:49)

## 왜 사람이 전략을 쥐어야 하나 (해설 전달)

- 전술만 쌓이면 코드가 나빠진다: *"바이브 코딩만 하면 코드는 조금씩 나빠집니다. 그런데 코드는 에이전트, 그러니까 혼자 코드를 고치는 AI가 일하는 환경이기도 합니다."*(01:37~01:44) — 나빠진 코드는 다음 에이전트의 작업 환경이 된다.
- 에이전트는 그것을 보고도 멈추지 않는다: *"에이전트는 집이 무너지는 걸 보면서도 눈 앞의 일만 합니다."*(01:49~01:51)
- 그래서: *"그래서 집을 돌볼 사람이 필요하고 지금은 그게 바로 사용자라는 겁니다."*(01:52~01:54)
- 맺음: *"모델은 아직 전략을 신경 쓰지 않습니다."*(13:17~13:18)

⚠️ **AI가 왜 전략을 못 하는지에 대한 본인의 논거는 캡션에 없다**(00:51~01:37 무캡션). 설명란은 *AI는 오늘 문제를 푸는 전술은 잘하지만 코드베이스를 길게 가꾸는 전략은 못합니다* 라고만 요약한다. *아직* 이라는 단서도 내레이션의 것이다.

## AI를 덜 쓰라는 말이 아니다

*"예전 개발자의 일은 대부분 전술이었고 이제 그 일을 최저임금보다 싸게 맡길 수 있으니까요."*(02:00~02:05) — 전술이 싸졌으니 사람의 시간은 전략으로 옮겨 간다는 읽기다. 같은 해설이 바이브 코딩의 실패를 이 틀로 설명한다: *"바이브 코딩이 통하지 않았던 것도 AI가 모자라서라기보다 집을 돌보는 사람이 없었기 때문입니다."*(13:23~13:27)

## 전략을 굴리는 도구 (같은 소스)

해설이 따라간 Pocock의 하루 루프는 전략을 사람 손에 두는 장치들로 읽힌다(위키의 정리):

- 만들기 전에 말을 맞춘다 — 그릴링 · 용어집 · 결정 기록 → [[grill-with-docs]]
- 리뷰에서 나온 지적을 환경으로 옮긴다 — 회고 스킬, 린트 규칙 → [[hard-vs-soft-enforcement]]
- 사람의 눈을 되돌릴 수 없는 곳에 둔다 → [[risk-proportional-human-review]]
- 바꿔도 안전한 모양으로 코드를 묶는다 → [[deep-modules]]
- 그 일들을 말할 **단어** 를 책에서 배운다: *"언어 대신 배울 것은 그 빈자리를 채울 단어와 습관입니다."*(13:18~13:21)

## 이웃 개념과의 차이

- [[codebase-gardening]] — 가꾸는 **행위** 의 이름. 이 페이지는 그 일이 왜 사람 몫으로 남는지에 대한 구분이다.
- [[cognitive-debt]] — 사람이 코드를 이해하지 못하게 되는 비용. 여기서 말하는 것은 코드베이스 자체가 나빠지는 쪽이다.
- [[software-factory]] — 같은 소스에서 Pocock은 불을 전부 끈 공장을 싫다고 하고 방마다 밝기를 조절하자고 한다. 전략을 사람이 쥔다는 주장의 다른 표현이다.

## 미해결

- 구분의 원문(Ousterhout)을 위키가 읽지 않았다 — *하사관 / 장군* 비유가 책의 것인지 Pocock이나 해설의 것인지 캡션으로는 알 수 없다.
- 단일 소스, 화자 한 사람의 경험칙이다. 에이전트가 전략적 수정을 못 한다는 측정은 없다.
- *아직* 이 언제까지인지 — 모델이 전략을 맡게 되면 무엇이 달라지는지는 소스가 말하지 않는다.

## References

- [[tech-bridge-pocock-networkchuck-what-to-learn-instead-of-languages]] — Tech Bridge 한국어 해설(2026-11-23 업로드), NetworkChuck × Matt Pocock 대담
- John Ousterhout, *A Philosophy of Software Design* (위키 미열람)

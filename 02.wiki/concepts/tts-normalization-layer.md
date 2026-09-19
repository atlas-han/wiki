---
title: TTS 앞의 정규화 레이어 (TTS Normalization Layer)
type: concept
category: pattern
tags: [tts, normalization, vendor-independence, pronunciation, voice-agents]
aliases: [TTS 정규화, 합성 전 정규화]
related: [voice-agent-pipeline, transcription-brittleness, time-to-first-audio, least-privilege-connectors]
first-seen: tech-bridge-voice-agent-failure-modes
sources: [tech-bridge-voice-agent-failure-modes]
created: 2026-09-19
updated: 2026-09-19
---

# TTS 앞의 정규화 레이어

**LLM 출력을 TTS로 곧장 보내지 말고 그 사이에 자기 소유의 정규화 층을 둔다.** [[tech-bridge-voice-agent-failure-modes]]의 다섯 번째 실패 모드다.

> 저희가 권장하는 방식이자 저희가 확인한 바에 따르면, **일반적으로 LLM과 TTS에 입력되는 데이터 사이에 정규화 계층을 두는 것이 좋습니다. LLM 출력 결과를 TTS로 직접 보내지는 않죠?** (22:16~22:37)

## 무엇을 하는가

| 항목 | 내용 |
|---|---|
| **이모지·마크다운 제거** | 합성 전에. *"LiveKit이나 PipeCat처럼 몇 가지 플래그만 설정하면"* 해 준다 — **직접 만든다면 명시적으로 해야 한다** |
| **커스텀 발음 사전** | 고유명사·브랜드·약어. *"대부분의 TTS 엔진이 제공한다 — LLM에서 TTS로 넘어갈 때 설정해야 한다"* |
| **속도 조절** | 고유 항목을 읽을 때 **0.8~0.7배속으로 늦춰** 또박또박. 이메일·전화번호·이름을 글자 단위로 |
| **복잡한 값 정규화** | 이메일·통화·날짜 — **TTS에 맡기지 말 것** |

## 핵심 논거는 품질이 아니라 교체 가능성

> **TTS에 맡기지 마세요. 대부분의 TTS가 이런 작업을 해주긴 하지만, TTS에만 의존하지 말고 자체적으로 정규화 레이어를 구축해야 합니다. 그래야 나중에 TTS를 바꿔야 하거나, 기존 TTS가 고장 나서 다른 TTS를 사용해야 할 때, TTS 엔진에 의존하지 않고도 관리할 수 있습니다.** (23:38~24:15)

**벤더가 해 줄 수 있는 일을 일부러 자기 쪽에서 한다.** 이유는 두 가지 — **교체**(더 나은 엔진으로 옮길 때)와 **장애**(현재 엔진이 죽었을 때). 정규화가 벤더 안에 있으면 벤더를 바꾸는 순간 발음이 전부 달라진다.

[[transcription-brittleness]]가 입력 쪽에서 같은 말을 한다 — *"전사 엔진 종류와 관계없이 정리된 전사본을 LLM에 일관되게 전송하십시오."* **파이프라인의 양 끝에 자기 소유의 정규화 층을 두고 벤더를 그 바깥에 둔다**는 하나의 설계 원칙이다.

⚠️ **판매자가 자기 층의 교체 가능성을 권하는 드문 자리**다. 다만 [[plivo|Plivo]]가 파는 것은 STT·TTS 엔진이 아니라 그 위의 플랫폼이므로, 이 권고는 **자사 위치를 위협하지 않는다.**

## 화자 자신의 회귀 테스트

> **첫 번째 테스트는 제 성이나 회사 이름을 발음하지 못하면 이미 실패한 거라고 보는 겁니다.** (24:15~24:51)

> 두 번째는 **저희 회사 이름인 [Plivo]** 입니다. **그래서 많은 엔진들이 그것을 피보(pivo) 또는 플레오(pleo) 등으로 발음합니다.** (24:51~25:12)

**개인적이지만 실용적인 스모크 테스트**다 — 발음하기 어려운 고유명사 두 개를 고정 케이스로 두고 엔진을 바꿀 때마다 돌린다. ⚠️ 그리고 **이 영상의 자막이 바로 그 이름 둘을 다 틀렸다**(*"Balos Subramanion"* · *"PO"*).

> 만약 고객에게 제공하는 제품을 개발하고 있다면, **고객에게 이러한 옵션을 제공하는 것이 좋습니다.** (25:12)

발음 제어를 **최종 사용자에게 넘기라**는 권고다 — 브랜드명은 그 브랜드의 주인만 안다.

## ⚠️ 유보

- **정규화 순서와 규격이 없다** — 무엇을 먼저 하는지, 충돌하면 어떻게 하는지.
- **속도를 늦추면 통화가 길어진다** — [[time-to-first-audio]] 예산 및 통화 비용과의 관계가 계산되지 않는다.
- **사전을 누가 유지하는가** — 브랜드·인명이 계속 늘어나는데 갱신 절차가 없다.
- **정규화 층 자체의 오류**(잘못 늦추기·잘못 읽기)가 다뤄지지 않는다.
- **엔진 이름이 하나도 나오지 않는다** — 어떤 TTS가 사전·속도를 어떻게 지원하는지.

## References

- [[tech-bridge-voice-agent-failure-modes]] — first-seen
- [[venky-b]] · [[plivo]]
- 관련: [[voice-agent-pipeline]] · [[transcription-brittleness]] · [[time-to-first-audio]] · [[typed-field-collection]]

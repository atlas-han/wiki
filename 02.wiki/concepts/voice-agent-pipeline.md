---
title: 보이스 에이전트 파이프라인 (Voice Agent Pipeline)
type: concept
category: architecture
tags: [voice-agents, stt, tts, turn-detection, latency, pipeline]
aliases: [음성 에이전트 파이프라인, STT-LLM-TTS]
related: [time-to-first-audio, voice-latency-thinking-tradeoff, transcription-brittleness, tts-normalization-layer, typed-field-collection]
first-seen: tech-bridge-voice-agent-failure-modes
sources: [tech-bridge-voice-agent-failure-modes]
created: 2026-09-19
updated: 2026-09-19
---

# 보이스 에이전트 파이프라인

**음성-텍스트(STT) → LLM → 텍스트-음성(TTS)을 직렬로 잇고 그 사이에 턴 감지를 두는 네 층 구조.** [[tech-bridge-voice-agent-failure-modes]]에서 [[venky-b|Venky B]]([[plivo|Plivo]])가 *"누구나 처음 구축하는"* 형태로 제시했다. **이 위키에 음성 에이전트라는 층이 처음 서는 페이지**다.

> AI 에이전트를 구상하는 사람들은 대부분 **여러 오케스트레이션 프레임워크를 선택하고, LiveKit이나 PipeCat 같은 도구**를 사용해서 꽤 괜찮은 결과물을 만들어냅니다. **음성-텍스트 변환(STT), LLM, TTS, 그리고 그 사이의 턴 감지 같은 네 가지 계층을 오케스트레이션**해서 *"내 AI 에이전트는 [PoC]에서 잘 작동하고, 프로덕션 환경에서도 문제없이 작동한다"* 라고 생각하는 겁니다. (03:41~04:03)

## 왜 텍스트 에이전트와 다른가

이 위키가 가진 모든 에이전트 페이지는 **텍스트 입출력**을 전제했다. 파이프라인이 붙으면서 세 가지가 새로 생긴다.

| | 텍스트 에이전트 | **보이스 파이프라인** |
|---|---|---|
| 지연 | 비용·대기의 문제 | **UX의 절벽** — 넘으면 사람이 끊는다 → [[time-to-first-audio]] |
| 입력 | 사용자가 친 그대로 | **아래 층이 이미 틀릴 수 있다** → [[transcription-brittleness]] |
| 출력 | 그대로 읽힘 | **합성 전에 정규화가 필요** → [[tts-normalization-layer]] |

그리고 **실패가 층을 건너 증폭된다.** 코드 스위칭이 그 사례다 — STT가 다른 문자로 받아쓰면 LLM이 그 문자로 출력하고 TTS가 무너진다(15:06~15:24). 직렬 파이프라인 고유의 실패 양식이고, 층마다 따로 고치면 잡히지 않는다.

## 다섯 실패 모드

| # | 자리 | 처방 |
|---|---|---|
| 1 | **지연** | [[voice-latency-thinking-tradeoff]] · [[token-fertility]] |
| 2 | **전사** | [[transcription-brittleness]] · [[dynamic-keyword-boosting]] |
| 3 | **데이터 수집** | [[typed-field-collection]] |
| 4 | **평가** | [[field-level-unit-test-evals]] |
| 5 | **TTS 입력** | [[tts-normalization-layer]] |

## 층 사이의 지식 비대칭

이 파이프라인을 고치는 기법 대부분이 **한 층이 다른 층보다 더 아는 것을 이용한다**:

- **LLM은 도메인을 알고 STT는 음향만 안다** → LLM으로 전사를 후처리하면 *전화번호 가운데의 E* 가 3임을 안다.
- **앱은 지금 무엇을 묻는지 알고 STT는 모른다** → [[dynamic-keyword-boosting]].
- **앱은 필드 타입을 알고 LLM은 자유 텍스트를 본다** → [[typed-field-collection]].

즉 이 아키텍처의 개선은 대부분 **위층의 컨텍스트를 아래층에 주입하거나 아래층의 출력을 위층이 교정하는** 형태다.

## 오케스트레이션 층

**LiveKit**과 **PipeCat**이 이 위키에 이름으로 처음 등장한다. 소스에서의 역할은 둘뿐이다 — 네 층을 잇는 **오케스트레이션 프레임워크**이고, *"몇 가지 플래그만 설정하면"* 이모지·마크다운 제거 같은 기본 위생을 해 준다(22:37~22:56). ⚠️ 그 이상의 서술이 없어 이 위키는 **별도 엔티티 페이지를 만들지 않았다.**

## ⚠️ 유보

- **턴 감지와 barge-in(끼어들기)** — 네 번째 층인데 **화자가 시간 초과로 슬라이드만 띄우고 넘어간다**(25:12~25:58). 챕터 제목은 있으나 **내용이 없다.**
- ⚠️ **"speech-to-speech 파이프라인으로 하면 speech-to-speech 모델이 필요 없다"**(25:43~25:58)는 **자기모순**이다. 이 소스는 **STT-LLM-TTS 캐스케이드와 end-to-end speech-to-speech 모델의 대비를 끝내 정리하지 않는다** — 후자가 이 다섯 실패 모드 중 무엇을 없애고 무엇을 남기는지가 통째로 열려 있다.
- **각 층의 지연 배분**이 *"슬라이드에 있다"* 고만 하고 자막에 숫자가 없다.
- **비용** — 균형 삼각형의 한 축인데 수치가 한 번도 나오지 않는다.

## References

- [[tech-bridge-voice-agent-failure-modes]] — first-seen
- [[venky-b]] · [[plivo]]
- 관련: [[time-to-first-audio]] · [[voice-latency-thinking-tradeoff]] · [[token-fertility]] · [[transcription-brittleness]] · [[dynamic-keyword-boosting]] · [[typed-field-collection]] · [[field-level-unit-test-evals]] · [[tts-normalization-layer]]

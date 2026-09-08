---
title: Thomas Wolf
type: entity
category: person
tags: [hugging-face, open-source, interviewer, ai-engineer]
links:
  - https://huggingface.co/
sources: [tech-bridge-minimax-m3-long-context]
created: 2026-09-08
updated: 2026-09-08
---

# Thomas Wolf

[[hugging-face|Hugging Face]] 공동창업자 겸 CSO. 이 위키에는 [[tech-bridge-minimax-m3-long-context]]의 **무대 대담 진행자**로 등장한다 — [[olive-song]]([[minimax|MiniMax]])에게 [[minimax-m3|M3]]의 설계를 묻는다.

> ⚠️ **이름의 근거가 영상 설명란 하나다.** 자막에는 진행자 이름이 나오지 않는다. 자막의 정황은 **모순되지 않는다** — 게스트를 두고 *"뉴욕에 있던 **Hugging Face에 합류하는 대신** MiniMax에 합류하기로 결정했다"* 고 말하고, MiniMax의 Hugging Face 오픈소스 시작 시점을 *"작년 1월 (…) 그때 **저희가** 팀에 대해 이야기를 나누면서"* 라며 1인칭으로 회상한다. 그래도 **이름 자체를 소스 내부가 확인해 주지는 않는다.**

## 이 소스에서의 역할 — 맥락을 놓는 진행자

단순 질문자가 아니라 **기술사적 위치를 잡아주는** 역할을 한다. 이 위키에 값진 대목은 대부분 그의 프레이밍이다.

### 어텐션 효율화의 진자 운동

> 어텐션에 대한 연구가 많이 이루어졌고 — 이 **n제곱** 문제 말이죠 — **linear attention**에 대한 연구도 많았습니다. 그러다가 **flash attention이 등장하면서 그 모든 것들이 어느 순간 사라져 버렸죠.** (…) 자, 이제 우리가 다시 **제1원리로 돌아가서 어텐션이란 무엇이고 어떻게 하면 더 효율적으로 만들 수 있을지** 생각해 보는 게 좋네요.

→ [[sparse-attention]] · [[attention-mechanism]]

### 길이의 역사

> **100만 토큰이면 엄청난 거죠**, 그렇죠? **GPT-2의 크기는 1,024**였고, 모두들 "와, 정말 크네. 우리는 더 이상 필요 없어"라고 말했죠.

이어 *"Jeff가 얼마 전에 저에게 **1조 토큰 어텐션**을 제안했었죠"* 라고 덧붙인다. ⚠️ **Jeff가 누구인지 소스에 없다.**

### 중국 랩 지형

> **MiniMax는 중국에서 소위 "AI 드래곤" 중 하나**입니다. (…) **DeepSeek** (…) **Kimi**와 **GLM**을 제작하는 **Moonshot**에 이어 이제 **MiniMax**도 등장했습니다.

또 *"지금 AI 랩이 **64개** 정도 있는 걸로 알고 있거든요"* 라고 말한다. ⚠️ 어림수이고 출처가 없다. ⚠️ Kimi/GLM의 귀속 문장도 모호해 **위키는 사용하지 않는다.**

### 오픈소스 수익 질문

진행자가 **두 번** 파고든 유일한 주제다 — *"오픈소스 모델은 좋지만 **수익원도 필요**하잖아요?"*, *"앱 개발에 사용하는 특정 모델이 있으신가요?"* **두 번 다 답을 받지 못한다.** 질문자가 이해관계자(모델 허브 플랫폼)라는 점과 함께 읽어야 한다.

## 이해관계

⚠️ [[hugging-face|Hugging Face]]는 [[minimax|MiniMax]]가 모델을 올리는 플랫폼이고, 진행자는 그 회사의 창업자다. **오픈소스 모델 생태계에 이해관계가 있는 쪽이 오픈소스 모델 랩을 인터뷰하는 구도**다. 대담 전체가 오픈소스에 우호적인 톤인 것을 이 위치에서 읽어야 한다.

## 미해결 사항

- 이름의 소스 내부 확인 (설명란 단독).
- 언급한 *"Jeff"*, *"AI 랩 64개"* 의 출처.
- 이 위키에 다른 소스 없음 — 인물 자체에 대한 정보는 이 대담의 역할에 한정된다.

## References

- [[tech-bridge-minimax-m3-long-context]] · [[hugging-face]] · [[olive-song]] · [[minimax]]
- 관련: [[sparse-attention]] · [[attention-mechanism]] · [[long-context-agents]]

---
title: Cognitive Offloading
type: concept
category: technique
tags: [education, llm, learning]
related: [regulatory-capture, retrieval-practice, ai-assisted-learning, ai-flipped-classroom, ai-engineering-skills-map, ai-learning-polarization]
first-seen: tech-bridge-andrew-ng-ai-opportunity
sources: [tech-bridge-andrew-ng-ai-opportunity, tech-bridge-ai-engineer-three-tier-skill-stack, tech-bridge-learn-anything-with-ai, tech-bridge-hassabis-fry-creativity-future, tech-bridge-andrew-ng-ai-engineering-skills-map, tech-bridge-lex-fridman-mathematicians-advice-ai-era, tech-bridge-lombrozo-learning-by-thinking-ai-tutor, tech-bridge-grace-ableidinger-vibe-vs-agentic-coding]
created: 2026-08-31
updated: 2026-11-25
---

# Cognitive Offloading

인지 작업을 도구에 넘겨 당장은 성과가 나지만 인간 쪽 retention·숙달이 떨어지는 현상. [[andrew-ng|Andrew Ng]]([[tech-bridge-andrew-ng-ai-opportunity]]): 통상의 LLM 사용은 숙제 점수는↑, 장기 성과는↓ — "일을 대신 시키기" 때문.

Wikipedia/검색은 사실 도구로 괜찮지만, 모델에게 일을 시켜 버리면 학습에 해롭다. 학습에 좋은 사용법이 없다고는 하지 않음. 본인조차 6개월 전 AI로 푼 front/back을 기억 못 해 다시 물은 경험이 있다.

제품 응답이 [[learnvector|LearnVector]](1:1 개인화). 자녀 교육 논의에서도 같은 축: 계산기 없이 곱셈 연습은 가능하나, 나이가 들면 AI 오프로딩이 retention을 해칠까 우려.

## References

- [[tech-bridge-andrew-ng-ai-opportunity]] · [[andrew-ng]] · [[learnvector]]

## 어디까지 오프로드해도 되는가 — 읽기는 남긴다 (2026-09-16 · [[tech-bridge-ai-engineer-three-tier-skill-stack]])

이 페이지는 *무엇이 손상되는가* 만 갖고 있었다. [[cedric-clyburn|Cedric Clyburn]]([[ibm|IBM Technology]])이 **하한선**을 긋는다: *"Python 마법사가 될 필요는 없고, **에이전트가 쓰는 코드를 읽고 이해할 수 있을 정도로만** 유창하면 된다"*(03:10~03:20). **쓰기는 오프로드하고 읽기는 남긴다** — Ng의 우려에 대한 *무엇을 남기면 되는가* 형의 답이다. ⚠️ 두 소스는 서로를 모르고, Ng의 사례(학생의 숙제)와 이 소스의 대상(AI 엔지니어 지망자)은 다르다. → [[read-fluency-for-agent-output]]

## 어떻게 쓰면 손상되지 않는가 — 역할을 나눈다 (2026-10-09 · [[tech-bridge-learn-anything-with-ai]])

세 번째 답은 **절차**다. [[nick-saraev|Nick Saraev]] 클립 + [[tech-bridge|Tech Bridge]] 내레이션: 기억은 정보를 다시 읽을 때가 아니라 **꺼낼 때** 남는다([[retrieval-practice]] — 다시 읽기 4회는 일주일 뒤 40%, 1회 읽고 3회 시험은 61%; ⚠️ 61%와 정정은 내레이션에만, 원 연구는 설명란에만). AI 설명을 읽는 것은 재학습 쪽이라 Saraev는 그것을 *"a passive consumption mechanism. You're just reading."*(02:37~02:42)이라 부른다. 처방은 [[ai-assisted-learning|역할 분담]] — **준비·정리는 AI에게, 인출·풀이·설명은 나에게**. 내레이션이 Ng의 우려를 그대로 옮긴다: *"막힌 문제를 고민하는 시간을 전부 AI의 답으로 채우는 거죠. 결과는 얻어도 내가 할 수 있는 일은 늘지 않을 수 있어요."*(ko 15:58~16:06). Ng = 증상, Clyburn = 하한선(읽기는 남긴다), 이 소스 = 역할별 분업표. ⚠️ 세 소스는 서로를 모른다.

> ⚠️ **Contradiction (약) — 2026-10-13 · [[tech-bridge-hassabis-fry-creativity-future]].** [[demis-hassabis|Demis Hassabis]]는 암기(*rote learning*)를 *"out of class with the help of AI tools because I think that's exactly what AI tools are good for"*(38:17~38:23)라고 한다. Ng의 *"일을 대신 시키기"* 우려와 방향이 다르다. 다만 하사비스의 도구는 약한 부분의 문제를 더 내주는 개인 교사(38:24~38:33)이고 *"in a very intentional way again that helps with the learning"*(38:05~38:09)을 조건으로 단다 — 정면 충돌은 아니다. → [[ai-flipped-classroom]]

## 학생에서 일하는 어른으로 — "chatbots are terrible for learning" (2026-11-01 · [[tech-bridge-andrew-ng-ai-engineering-skills-map]])

[[andrew-ng|Ng]](제목 · 설명란 · 태그 근거)이 08-30 인터뷰와 같은 증상을 더 세게, 더 넓게 말한다. *"I'm going to say something obvious but may be sound controversial, but chatbots are terrible for learning"*(09:04~09:08). 증거는 같다: *"students that use LLMs do better on homeworks but worse on final exam."*(09:19~09:24) — *"you get more work done, but you learn less."*(09:36~09:42) ⚠️ 연구명 · 저자는 말하지 않는다(*"the rigorous studies are now increasingly coming out"*).

새로운 것은 **대상**이다. *"I think people still underestimate the degree to which this is happening among working adults."*(09:49~09:55) 그리고 자기 이야기로 — *"I love my coding agents, helps you do a ton of work, but the reduced thinking I have to do"*(09:55~10:03, 문장이 편집으로 끊긴다). 이 페이지의 다른 소스들이 **학습자**를 다뤘다면, 이 편은 **코딩 에이전트를 쓰는 개발자 본인**을 같은 위험 안에 넣는다. 같은 영상 앞부분의 *"the coding agent will make a bunch of trade-offs that you didn't even know it made"*(04:37~04:43)가 업무 쪽 결과다 → [[ai-engineering-skills-map]].

단서는 유지된다: *"there are ways to use LLMs that do improve learning"*(10:05~10:10) — 그러나 *"the vast majority of ways that the vast majority of people use LLMs does not result in learning."*(10:20~10:23) → 그 *ways* 의 목록은 [[ai-assisted-learning]].

## 첫 통제 실험 수치 — PNAS 2025 *가드레일 없는 생성형 AI* (2026-11-16 · [[tech-bridge-lex-fridman-mathematicians-advice-ai-era]])

이 페이지의 근거는 지금까지 진술 · 사례였다. [[lex-fridman|Lex Fridman]] Podcast #503 해설이 PNAS 2025 실험(설명란 *Generative AI without guardrails can harm learning*, ⚠️ 원 논문 미열람)을 옮긴다: 튀르키예 한 고등학교 약 1,000명, GPT-4를 그냥 쓴 학생은 연습 점수 **+48%** 인데 AI 없이 본 시험은 *아예 안 쓴 학생보다* **−17%**. 연구진의 표현은 *목발* 이고, 가장 많이 보낸 메시지는 *"What is the answer?"* 였다. **답 대신 교사가 만든 힌트만 주는 튜터** 에서는 손해가 대부분 줄었다 — Ng의 *숙제 점수↑ 장기 성과↓* 에 실험 쪽 숫자와 개입 하나가 붙는다.

- 수학자들의 처방도 같은 축이다: [[alex-kontorovich|Kontorovich]] *계산기 70년, 여전히 구구단* · [[steven-brunton|Brunton]] *컴퓨터가 더 잘해도 선형대수는 배워야 — 직접 해봐야 감이 생긴다*.
- 집단 분포에서 보이는 모양은 [[ai-learning-polarization]](신규, 두 봉우리).

## 2026-11-19 — 기제와 세 번째 반: 힌트만 주는 튜터는 연습 +127% · 시험 차이 없음 ([[tech-bridge-lombrozo-learning-by-thinking-ai-tutor]])

[[tania-lombrozo|Tania Lombrozo]] 강연 해설이 같은 PNAS 2025 실험을 영상의 축으로 다시 옮긴다(⚠️ 해설 전달, 원 논문 미열람). 11-16에 적은 +48% / −17%는 그대로이고, **힌트만 주는 튜터 반의 값이 새로 붙는다**: *"이 반은 연습 문제를 127% 더 잘 풀었고 시험에서는 AI를 안 쓴 반과 차이가 없었습니다. 손해가 사라진 겁니다."*(08:57~09:04) ⚠️ 11-16 소스는 *손해가 대부분 줄었다* 고 옮겼다 — 표현의 세기가 다르고 어느 쪽이 논문에 가까운지는 미확인.

- **왜 손상되는가** — 배움의 한 부분은 바깥 입력 없이 이미 가진 것을 바꾸고 합치는 데서 일어난다([[learning-by-thinking]], 신규). 답을 받으면 그 단계가 통째로 빠진다. 연구진의 말로는 *"연구진은 그냥 답을 주는 AI가 목발처럼 쓰였다고 봤습니다."*(09:05~09:06)
- ⭐ **본인은 모른다**: *"시험을 더 못 봤는데도 덜 배웠다고 느끼지 않았습니다."*(09:19~09:21) Ng의 *숙제 점수↑ 장기 성과↓* 에 **자각이 따라오지 않는다** 는 조각이 붙는다 — 오프로딩의 손해는 스스로 알아채 고칠 수 있는 종류가 아니다.
- 두 번째 연구(PNAS Nexus 2025년 10월, 보도자료 경유): 수천 명이 챗봇 또는 구글 검색으로 같은 주제를 공부했고 *"챗봇으로 배운 사람들의 지식이 더 얕았습니다."*(09:34~09:35) 학생이 아닌 집단 · 수학이 아닌 과제에서의 같은 방향이다(⚠️ 표본 · 측정 방법은 말하지 않는다).

## 2026-11-25 — *이해를 자동화로 대신하지 말라*: 실력 걱정에 대한 IBM 글의 답 ([[tech-bridge-grace-ableidinger-vibe-vs-agentic-coding]])

IBM Technology 영상([[grace-ableidinger|Grace Ableidinger]])의 한국어 해설. 영상은 개발자들의 걱정으로 시작한다 — 판서에서 효율에는 체크, *"품질과 보안 실력에는 물음표."*(01:10) (⚠️ 개발자들의 반응 자체는 무캡션.) 해설은 끝에서 *실력* 물음에 IBM Think 글(위키 미열람)로 답한다:

- *"생각을 AI에 너무 많이 넘기면 기본기가 조용히 깎여 나갈 수 있고 그러니 이해를 자동화로 대신하지 말라고요."*(08:21~08:27)

근거가 되는 측정은 이 소스에 없다 — 권고 한 문장이다. 이 페이지의 실험 수치들과 방향은 같다. → [[vibe-vs-agentic-coding]](신규)

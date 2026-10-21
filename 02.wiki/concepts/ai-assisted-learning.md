---
title: "AI 보조 학습 — 역할 분담 (AI-Assisted Learning)"
type: concept
category: pattern
tags: [learning, ai-tutor, cognitive-offloading, prompting, verification, education]
aliases: [AI로 공부하기, AI 학습 역할, AI tutor roles, 도움받기 vs 생각 맡기기]
related: [sycophancy, retrieval-practice, cognitive-offloading, read-fluency-for-agent-output, generator-evaluator-pattern, verification-bottleneck, agent-memory, ai-flipped-classroom]
first-seen: tech-bridge-learn-anything-with-ai
sources: [tech-bridge-learn-anything-with-ai, tech-bridge-hassabis-fry-creativity-future, tech-bridge-top-1-percent-ai-habits]
created: 2026-10-09
updated: 2026-10-21
---

# AI 보조 학습 — 역할 분담

**AI에게 무엇을 맡기고 무엇을 직접 할지를 역할 단위로 나누는 학습 패턴.** 대부분은 AI를 *"다르게 설명해 줘"* 하는 **설명자(explainer)** 하나로만 쓰는데, 그것은 또 하나의 수동 소비다. 기준선: **준비·정리·출제·채점 보조는 AI에게, 떠올리고 풀고 설명하는 일([[retrieval-practice|인출]])은 나에게.** [[nick-saraev|Nick Saraev]] 클립과 [[tech-bridge|Tech Bridge]] 내레이션([[tech-bridge-learn-anything-with-ai]])에서.

> *"There are many roles that artificial intelligence can play for us. The issue is most people will only have ever used one. They use the explainer role"* — Saraev (02:20~02:27)
>
> *"AI에게 준비와 정리를 맡기면 우리는 직접 풀고 설명하는데 시간을 쓸 수 있어요."* — 내레이션 (ko 16:35~16:42)

## 역할 (챕터 번호·이름은 Tech Bridge 것)

| # | 역할 | AI가 하는 일 | 내가 지켜야 할 조건 (내레이션) |
|---|---|---|---|
| 1 | 인터뷰어 (*interviewer*) | 내가 이미 아는 것을 캐묻는다 | 목표·현재 수준·평가 항목을 먼저 알리고, 계획에 **내가 실제로 할 일**이 있는지 확인 |
| 2 | 학습 지도 | 주제를 의존 관계 있는 하위 단위로 쪼개고 막히는 곳을 표시 | 지도는 출발점 — 풀다가 빠진 기초를 찾으면 고친다 |
| 3 | 설명자 (*explainer*) | 막힌 한 지점만 비춘다 | 힌트 뒤엔 답을 닫고 **처음부터 혼자 다시** |
| 4 | 질문 | 후속 질문으로 이해 확인 | AI가 정답을 주기 전에 **내가 이유를 말한다**, 한 번에 하나 |
| 5 | 시험 (*examiner*) | 난도를 올려 가며 출제 | 하나씩, **내 답을 기다리라는 조건**, 운으로 맞혔는지 확인 |
| 6 | 풀이 검토 (*checker*) | 결과가 아니라 **과정**을 평가 | **다시 쓰게 하지 말고 짚게만**, 오류 하나 찾았다고 판단 전부가 맞는 건 아님, 코드는 직접 실행 |
| 7 | 설명 빈틈 | 내 설명과 원문을 비교해 빠진 것·잘못 이은 것 지적 | 자료를 **덮고** 내 말로 먼저 설명 |
| 8 | 오류 진단 (*diagnostician*) | 반복되는 실수의 뿌리 개념을 찾는다 | 기록은 직접 준다(**지난 대화를 다 본다고 가정 말 것**), 진단은 가설로 |
| 9 | 실전 스파링 (*sparring partner*) | 면접관·발표 청중 역할 | 답에 쓰는 성과·수치는 **실제 경험**, 시간 제한도 실전처럼 |
| 10 | 서기 (*clerk*) | 내 메모를 구조화·복습 카드로 | **내가 쓰지 않은 내용을 더하지 말 것**, 틀린 메모가 깔끔해질 수 있으니 근거 확인 |
| — | 자료 매칭 (*matchmaker*, ⚠️ 추정) | 수준 진단 후 *A와 B 사이* 를 잇는 자료 추천 | **추천 링크를 직접 열어** 실재·적합성 확인 |
| — | 시뮬레이션 (이름 판독 불가) | 실제 업무 같은 과제(이메일 더미)를 만들고 채점 | 점수 표시 ≠ 정확한 평가 — 채점 기준과 근거를 먼저 정한다 |

⚠️ Saraev는 *"10 different roles"*(02:44~02:47)라 했지만 열 개를 나열하는 클립은 없다. 위 번호·이름은 Tech Bridge의 챕터이고, Saraev 입으로 들리는 이름은 explainer · interviewer · examiner · checker · diagnostician · sparring partner · clerk · matchmaker뿐이다.

## 핵심 원리

- **결과물보다 과정을 맡기지 않는다.** Saraev의 서기 예: *"the reason I like the clerk is because all of the thinking is your own. What you're doing is you're just organizing it a little bit better."*(12:37~12:41)
- **AI 출력은 검증 대상이다.** 내레이션이 거의 모든 역할에 같은 단서를 단다 — 링크 직접 열기, 점수 ≠ 평가, 진단 = 가설, 동의해도 근거 확인(ko 16:11~16:19). 학습자 버전의 [[verification-bottleneck]].
- **고민하는 시간을 답으로 채우지 않는다.** *"막힌 문제를 고민하는 시간을 전부 AI의 답으로 채우는 거죠. 결과는 얻어도 내가 할 수 있는 일은 늘지 않을 수 있어요."*(ko 15:58~16:06) → [[cognitive-offloading]]

## 이 위키와의 연결

- [[cognitive-offloading]] — Ng는 *무엇이 손상되는가*, Clyburn([[read-fluency-for-agent-output]])은 *읽기는 남긴다*, 이 패턴은 **역할별 분업표**로 같은 질문에 답한다.
- [[generator-evaluator-pattern]] · [[automated-code-review]] — 6번(다시 쓰지 말고 짚기, 일부러 오류를 넣어 검토자 시험)은 코드 리뷰 에이전트의 결론과 같은 모양이다.
- [[agent-memory]] — 8번의 *"AI가 지난 대화를 모두 볼 수 있다고 생각하지는 마세요"*(ko 11:24~11:26)는 사용자 쪽에서 본 메모리 한계.
- **학교 구조로 (2026-10-13 · [[tech-bridge-hassabis-fry-creativity-future]])** — [[demis-hassabis|Demis Hassabis]]의 *"invert the classroom"*(38:12): 암기는 수업 밖에서 개인화된 AI가(*"it gives you more questions on that"* 38:31~38:33), 교실은 프로젝트·팀워크. AI를 *문제를 더 내주는* 시험관 역할로 쓰는 이 페이지의 방향과 같고, 그 분담을 시간표 단위로 끌어올린다 → [[ai-flipped-classroom]].

> ⚠️ **화자와 내레이터의 무게가 다르다.** Saraev 원 제목은 *"So Fast with AI"*(속도), Tech Bridge 내레이션은 매 역할마다 의심의 단서를 붙인다. 이 페이지의 "조건" 열은 **거의 전부 내레이션**이다.

## 학습에서 업무로 — 같은 역할, 다른 대상 (2026-10-21 · [[tech-bridge-top-1-percent-ai-habits]])

같은 [[nick-saraev|Saraev]] + Tech Bridge 내레이션 형식의 두 번째 편이다. 역할 셋이 업무 버전으로 다시 나온다.

| 학습 편 역할 | 업무 편 장 | 바뀐 점 |
|---|---|---|
| 1. 인터뷰어 | AI에게 나를 인터뷰하게 하기(03:18) | 계획 대신 **요구사항**을 끌어낸다 — 고객의 문제·예산·마감, *"Questions you cannot answer become items you need to research further."*(04:09~04:14, 더빙) |
| 6. 풀이 검토 | 의견 대신 약점 검토(04:18) | *"Poke holes in my thoughts"*(04:38~04:41). 내레이션이 [[sycophancy]]를 근거로 들고, **지적받았다고 바로 고치지 말라**는 단서를 붙인다(05:13~05:18, 더빙) |
| 10. 서기 | 회의 내용을 다음 작업으로(01:18) | 정리가 아니라 **실행의 입력**이 된다. 담당자·마감·승인을 거친 뒤 연결하고, 녹음 공유 범위를 먼저 정한다(02:03~02:12, 더빙) |

학습 편의 분업이 *준비·정리는 AI, 인출·풀이는 나*였다면, 업무 편은 **맥락과 판단은 나, 초안은 AI**다(*"providing sufficient context and verifying results directly"* 07:05~07:09, 더빙).

## References

- [[tech-bridge-learn-anything-with-ai]] · [[nick-saraev]] · [[retrieval-practice]] · [[cognitive-offloading]]
- [[tech-bridge-top-1-percent-ai-habits]] (업무 편) · [[sycophancy]]

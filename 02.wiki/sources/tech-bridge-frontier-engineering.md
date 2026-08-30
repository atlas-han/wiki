---
title: "Tech Bridge — AI 보조를 넘어 AI 네이티브로 (Clare Liguori)"
type: source
tags: [frontier-engineering, kiro, amazon, aws, video, agent]
source-url: https://www.youtube.com/watch?v=Ry0WHNxDbYA
source-type: video
author: Tech Bridge (한국어 자막 재배포) · 발표자 Clare Liguori (AWS)
date-published: 2026-08-29
ingested: 2026-08-30
created: 2026-08-30
updated: 2026-08-30
---

# Tech Bridge — AI 보조를 넘어 AI 네이티브로

[[tech-bridge|Tech Bridge]]가 한영자막을 입힌 20:29 강연. 발표자 [[clare-liguori|Clare Liguori]]는 AWS senior principal engineer, 주로 [[kiro|Kiro]](Amazon의 agentic 코딩 어시스턴트). 한 줄 테제:

> Frontier engineering is about intentionally changing the way that you work.

본문은 **en-orig 자동 자막**을 재구성. ko는 timedtext 429. ASR: "Ligouri" / "spectrum and development" / "five coding" / "FOMAT" / "bedrock mantel" — 각각 Liguori, [[spec-driven-development]], vibe coding, 설명란의 FOMO, Bedrock Mantle로 해석. 인용·타임스탬프는 자막이 분명한 구간에 한정.

채널 설명의 발표자 링크: [X](https://x.com/clare_liguori) · [LinkedIn](https://www.linkedin.com/in/clareliguori/) · [clare.dev](https://clare.dev/).

## 4단계 진화와 체감 격차 (00:00–02:12)

에이전트 AI 3년간의 산업 단계:

1. **inline completion** — 다음 줄·다음 함수
2. **chat** — 코드에 대한 질문
3. **vibe coding** — "작년 언젠가" 모두가 하기 시작
4. **frontier development** — 지금 early adopter 국면

Liguori 본인 체감은 앞 세 단계를 다 써도 **10–20%** 생산성. Amazon 사내 파일럿은 **중앙값 4.5x**, 때로 **10x 이상**. 그래서 "step function"이라고 부른다.

Frontier developer를 세 행동으로 정의:

| 행동 | 내용 |
|---|---|
| **hands-off coding** | 생산 코드의 **1–2%만** 사람이 씀. 나머지 에이전트 |
| **드문 개입** | 코딩 어시스턴트가 **수 시간** 개입 없이 돌게 만드는 것이 목표 |
| **유휴 최소화** | 여러 에이전트를 **병렬**로 백로그에 돌림 |

## 세 실험: Pathfinder → 스프린트 → 평범한 50팀 (02:12–08:16)

### Bedrock Mantle (02:12)

Bedrock(Claude·GPT 호스팅) 팀이 새 **inference data plane**이 필요. 추정 **30명 × 18개월**(고객·모델 마이그레이션 포함). 6명이 Kiro로 **76일**. 커밋 기준 최대 **20x**. Amazon 안에서 처음 본 규모라 pathfinder.

한계를 본인이 바로 단다: 회사 최상위, **distinguished engineer 2명**, 분산시스템·LLM 아키텍처 전문가. 이야기가 사내에 불처럼 번졌지만 "우리 팀에서 재현되나"가 질문으로 남음.

### Prime Video 10일 스프린트 (03:54)

다른 엔지니어 6명, 다시 Kiro. 10일 진척으로 전달 추정을 **90주 → 24주**. Mantle에 "적어도 가까운" 성과를 다른 셋으로 보임.

한계: 온콜 없음, 회의 적음, 산만 최소화. 시니어가 **사전 3주** 동안 작고 잘 범위 잡힌 태스크+요구사항을 미리 만들어 6명이 2주 동안 churn. "real life가 아니라 구조화된 한 시점."

### Amazon Stores 50팀 (05:38)

amazon.com · 리테일 웹 · 오프라인 스토어. **평범한 분포**(얼리/미드/시니어), **기존 코드베이스**(Mantle 같은 greenfield 아님). 작년 상당 기간.

측정: 커밋 수가 아니라 **프로덕션 배포 속도**(고객에게 얼마나 빨리 나가는가).

| 집단 | 결과 |
|---|---|
| 절반 | **3x 미만** |
| 다른 절반 | 중앙값 **4.5x**, 일부 **10x+** |

90%가 Kiro 및 다른 내부 도구를 씀. 도구가 갈랐다면 이렇게 안 갈린다.

> it wasn't about the tools, it was about the way that they worked.

step-function 팀은 **일하는 방식을 의도적으로 바꿈**. 나머지는 기존 방식 위에 Kiro를 뿌림. Liguori의 aha: 본인이 약속된 생산성을 못 느낀 이유도 여기.

인터뷰 대상: Stores 파일럿 + Mantle + Prime Video. 나온 것은 기법 목록이 아니라 **습관** — 하루 스프린트가 아니라 매일.

## 다섯 습관 (08:16–15:09)

### 1. 에이전트 컨텍스트에 투자하고, 모델을 따라 가지치기

머릿속 지식은 슬랙·온보딩 멘토·코드리뷰·스탠드업·스프린트 플래닝으로 사람에게 전달돼 왔다. 그걸 **skills / steering 파일에 적는다.**

매일 습관: 에이전트가 실수하거나 "나라면 그렇게 안 했을" 때마다 — steering에 뭐가 빠졌나.

반대 습관: 모델이 좋아지면 **do-not을 지운다.** Sonnet 3.7(작년 중반) quirk 때문에 넣었던 금지는 Opus 4.5(작년 11월) 이후 덜 필요. 질문은 "아직 필요한가, 아니면 컨텍스트를 부풀리는가." [[harness-engineering]]의 *"every mistake becomes a rule"* 과 같은 루프의 **제거면** — [[agent-harness-design]]이 말하는 가정 가지치기와 맞닿음.

### 2. 빨라지려면 먼저 늦춘다

인터뷰한 거의 모든 팀이 채택 초기 **생산성이 내려갔다.** hockey stick 전에 코드베이스 일이 있다. 특히 brownfield.

한 일: 에이전트 컨텍스트 축적, 도구 **에러 메시지를 모델이 읽히게**, 새 도구·**MCP 서버**, 에이전트가 탐색하기 쉽게 **구조 재배치**. 더 과격하게는 언어 교체. 비타입 Python/JS는 컴파일 에러가 없어 모델이 추측해 돌려준다. 팀이 TypeScript로, Amazon 안에서는 **Rust**(컴파일러 메시지가 좋음)가 늘었다. 필수는 아니라고 명시.

리더 함정(뒤에서 반복): "도구 있는데 왜 안 빨라." 이 감속이 그 답.

### 3. 에이전트를 돌보지 말고 먹이를 준다

Liguori가 step-function의 이유로 꼽는 aha.

하루 종일 대화형 vibe coding이면 사람이 **루프에 묶여** 4–5x가 원리적으로 안 나온다. 생성 30초–1분을 기다리며 리뷰 → 다른 일을 못 함 → 병렬 복제가 안 됨. 왼쪽(돌봄) vs 오른쪽(먹이).

**먹이** = 할 일 + **자가 검증 방법**. 에이전트는 품질 바 — 실행·컴파일·테스트 통과·테스트 가능·높은 커버리지 — 에 닿을 때만 사람에게 돌아온다. 다음 단계: 그 내용을 steering에 넣어 **매번 사람 없이**.

[[verifiable-goals]]의 independent loop와 동일. [[agent-org-adoption]]의 "검증이 generation보다 레버리지"와도 같은 축.

### 4. 코드를 고치기 전에 의도를 문서로

Amazon은 spec-driven을 많이 쓰고, 그걸 Kiro 제품에 넣었다(ASR "spectrum and development").

vibe coding 루프: 높은 수준 프롬프트 → 코드 대량 → "그게 아니야 / 요구가 틀렸어 / 그런 설계 아니었어." **의도가 틀린 코드**를 에이전트와 왕복하는 것은 비생산적.

모호·복잡한 기능: 스펙을 먼저 쓴다. 모델이 초안을 써도 된다. **문서 왕복이 코드베이스에 흩어진 변경 왕복보다 싸다.** → [[spec-driven-development]]의 Amazon/Kiro 현장판.

### 5. 테스트를 왼쪽으로, 로컬 mock으로

수 시간 자율 루프의 조건은 **빠른 피드백**. 실수는 전제. 신호가 있으면 스스로 고친다.

린터, 유닛/통합/성능/보안 테스트 — "원래 해야 했던 위생"인데 이제 ROI가 충분히 높다. 많이 보는 투자: **로컬에서 도는 결정론적 mock 서비스**. 라이브 서비스·클라우드를 끼운 통합 대신 노트북에서 루프. 피드백이 빠를수록 루프가 많고 그 에이전트가 생산적.

[[agent-org-adoption]]의 Playwright MCP left-shift, [[verifiable-goals]]의 verifier-first와 같은 방향. 여기의 구체물은 **결정론적 로컬 mock**.

## 복병: 번아웃, 인지 부하, 리뷰 근육 (15:09–17:11)

5습관을 다 해도 nirvana가 아니다. 아직 early adopter.

- **번아웃 / FOMO** (ASR "FOMAT", 본인이 만든 말은 아님, 어느 컨퍼런스): 밤새 프롬프트를 다듬어 에이전트가 몇 시간 돌고 아침에 패치가 있기를.
- **인지 부하**: 병렬 에이전트 → 터미널 탭을 끊임없이 전환.
- **AI 출력 리뷰가 작성보다 어려운 사람**. 시니어는 남의 코드 리뷰로 커리어를 쌓았고, 주니어는 그 근육이 없다. [[tech-bridge-figma-coding-agents]]에서 시니어가 가장 느린 채택자인 점과 겹치되, 여기는 **주니어의 리뷰 부하**를 강조.

## 조직이 바꿔야 하는 세 가지 (17:11–20:21)

엔지니어의 하루가 통째로 바뀌는 것과 별개로, 조직이 프론티어 팀을 **가능하게** 해야 한다.

1. **감속을 승인.** 리더(본인 포함)가 "모델이 이렇게 좋은데 왜 안 빨라"를 말함. 답: 코드베이스·팀 습관에 **약 2개월**. X에서 하루 20 PR을 자랑하는 글을 보고 매달 기능을 기대하면 감속이 죽는다.
2. **너무 넓게 너무 빨리 말 것.** 전 팀을 즉시 프론티어로 밀었으면 Pathfinder·스프린트·50팀에서 배운 것이 없었을 것. Amazon의 **2026 과제: 50팀 → 다음 2,000팀**. 성급 롤아웃은 자기 조직 맥락을 모르는 팀만 늘린다.
3. **새 병목은 의사결정.** 예전 병목은 손코딩. 이제 코드가 **1–2개월**. 예전 제품이 9–12개월이면 결정 2개월+런칭 승인 2개월이 묻혔다. 지금은 그게 long pole. 프론티어 팀은 **코드보다 결정에 시간을 더 쓴다.** 되돌리기 쉬운 결정을 빠르게.

닫는 말: 팀만이 아니라 조직. AI 도구와의 상호작용을 바꿔 **루프에서 자신을 빼낼 것.**

## 위키 합성

같은 주제를 세 현장이 다른 입구로 말한다.

| | 이 강연 (Amazon) | [[tech-bridge-figma-coding-agents]] (Figma) | [[tech-bridge-spec-driven-development]] |
|---|---|---|---|
| 진단 | 도구 동일, 방식 차이. 뿌리기는 3x 미만 | 3막. 큰 문제에 1막 습관을 쓰면 신뢰 붕괴 | 프롬프트는 사적·일시적 |
| 레버리지 | 먹이+자가검증, 로컬 mock, 의도 문서 | 검증 피라미드, TDD-first, 계획 5x | Constitution→Spec→Plan→Task |
| 조직 | 2개월 감속, 50→2000, 결정 병목 | 회의론자=로드맵, PR provenance | 팀 합의된 스펙이 Git 계약 |
| 사람 | 주니어 리뷰 근육, FOMO 밤샘 | 시니어가 가장 느린 채택자 | (개인보다 저장소 계약) |

Amazon 수치는 내부 파일럿(커밋·배포 속도). 벤더 소속 발표라 방법론·통제 집단은 영상만으로 검증 불가. 위키는 **습관 목록과 반례(Mantle의 엘리트 구성, 스프린트의 사전 3주 태스크)** 를 남긴다.

## 등장 개체

- [[clare-liguori]] — 발표자
- [[kiro]] — AWS agentic 코딩 어시스턴트
- [[amazon]] — 세 실험의 무대
- [[tech-bridge]] — 자막 재배포
- 개념 [[frontier-engineering]] · [[agent-org-adoption]] · [[spec-driven-development]] · [[verifiable-goals]] · [[harness-engineering]]
- 페이지화하지 않음: Bedrock Mantle 팀, Prime Video, Amazon Stores, distinguished engineer 개인, Sonnet 3.7 (모델 페이지 기존 계보와 별개 언급)

## References

- [원문 영상](https://www.youtube.com/watch?v=Ry0WHNxDbYA)
- raw: `01.raw/articles/2026-08-29_AI 보조를 넘어 AI 네이티브로.md`
- [clare.dev](https://clare.dev/) · [X @clare_liguori](https://x.com/clare_liguori)
- [[tech-bridge-figma-coding-agents]] · [[tech-bridge-spec-driven-development]]

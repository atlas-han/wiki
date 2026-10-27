---
title: "Tech Bridge — AI가 코딩하는데, 당신을 왜 뽑죠? | npm 공동 창업자가 말하는 개발자의 다음 역할 (Laurie Voss 강연 발췌): 병목은 옮겨 간다 · 빵집 주인 · Brooks의 본질적 복잡성 · product engineer · 주니어의 훈련 경로"
type: source
tags: [laurie-voss, arize-ai, npm, code-review, theory-of-constraints, bottleneck, fred-brooks, essential-complexity, product-engineer, requirements, junior-developers, specs, rubrics, evals, blast-radius, excerpt-format, video]
source-url: https://www.youtube.com/watch?v=SHGxL8DQOxs
source-type: video
author: Tech Bridge (발췌 편집, 내레이션 없음) · 화자 [[laurie-voss|Laurie Voss]](설명란 · 태그 근거, 발화에 이름 없음) · 원본 강연 링크 없음
date-published: 2026-10-26
ingested: 2026-10-27
created: 2026-10-27
updated: 2026-10-27
---

# Tech Bridge — AI가 코딩하는데, 당신을 왜 뽑죠?

[[tech-bridge|Tech Bridge]]가 올린 **7:18, 공식 챕터 10** 영상. 설명란은 *"npm 공동 창업자 Laurie Voss의 관점"* 이라고만 하고 원본 강연의 제목 · 날짜 · 링크는 없다. 최근 편들과 형식이 다르다. **한국어 내레이션 없이 Voss 원음만 이어 붙인 발췌 편집본**이고, 오디오도 영어 원본 하나다.

> 첫 문장: *"the cost of producing plausible code has collapsed while the cost of knowing whether to trust that code has stayed exactly the same."*(00:00~00:07)

> 핵심 베팅: *"the bottleneck moves to describing the problem and defining what it means to have solved the problem. And my big bet for this talk and for the next 10 years is that is where it stays."*(03:40~03:48)

이 위키에서 [[laurie-voss]]가 두 번째로 등장한다. 10-02 [[tech-bridge-death-of-code-review]]는 **코드 리뷰라는 병목**을 서베이했고, 이 편은 그 병목이 **풀린 다음**을 다룬다. 기존 페이지에는 다음 내용이 붙는다.

- [[verification-bottleneck]]: **병목 이동 순서**(리뷰 → 운영 → 보안 → 문제 정의)
- [[spec-driven-development]] · [[taste-encoded-evals]]: *"best people's judgment into specs and rubrics and evals"*
- [[risk-proportional-human-review]]: *"high blast radius code"* 만 리뷰하라는 주장
- [[ai-jobs-impact]]: 주니어 개발자의 훈련 경로가 사라진다는 문제

**트랙과 인용.** 오디오는 `English (US) original` 하나이고(나머지는 더빙), **한국어 트랙이 없다.** 받은 ko는 `tlang=ko` 기계 번역이고 끝부분에 원문에 없는 *"시청해 주셔서 감사합니다"* 를 만들었다. **인용은 전부 en-orig**로 한다. 판독 상세는 raw에 있다.

## 1. 코드는 싸졌다, 그 뒤는 아니다 (00:19~00:51)

- *"agents have made writing code basically free (…) everything that comes after writing the code did not become free at the same time."*(00:21~00:36) *"the thing it's stuck behind right this second like this month is code review."*(00:47~00:51)

## 2. 병목은 사라지지 않고 옮겨 간다 (00:51~02:21)

- *"his big idea was the theory of constraints. Uh every system has one bottleneck and speeding things up does not work unless the thing that you were speeding up is the bottleneck."*(00:52~01:00) **"his"가 누구인지는 발췌에 없다**(앞 문맥이 잘렸다). 이 페이지는 귀속하지 않는다.
- *"when you fix the bottleneck it doesn't go away, it just moves"*(01:11~01:15). 자동 리뷰가 해결된다고 가정하면 다음 병목은 **운영**(*"How do I deploy this thing? How do I scale it up?"*)이고, 그다음은 **보안**(*"How do I make this thing safe at scale?"*)이다(01:35~01:45).
- 시간표: 12개월 안에 코드 리뷰에서는 *"real progress"* 가 있겠지만, 운영 · 확장 · 보안은 *"somewhere between 5 and 10 years"*(02:00~02:13)가 걸린다.
- 상대적으로 안전한 영역: *"deciding what to build, defining what good means, and finally making it delightful."*(02:14~02:21) → [[verification-bottleneck]]

## 3. 빵집 주인에게 물어봐야 하는 이유 (02:13~03:40)

- *"Every piece of software is a formalization of something that a human wanted to get done."*(02:26~02:31) 주문을 추적하는 소프트웨어는 1만 개가 있다. 하지만 빵집에 맞는 것은 *"only one of those, if you're lucky"* 이고, 자동차 부품점이나 대형 제조업이면 답이 또 다르다(02:34~03:01).
- *"that knowledge isn't in the training data. It isn't in the weights. It is in the mind of the person who runs that business."*(03:13~03:19) 그것을 꺼내는 유일한 방법은 *"you have to talk to them."*(03:25~03:27)

## 4. 어려운 것은 문제 자체 — Brooks (03:40~04:11)

- 첫머리의 핵심 베팅에 근거를 단다. Fred Brooks(*"ran IBM's System/360 project and wrote uh The Mythical Man-Month"*)가 1986년에 소프트웨어의 어려움을 둘로 나눴다. **accidental complexity**는 도구 · 언어 · 타이핑 · 문법의 어려움이고, **essential complexity**는 *"the difficulty of the problem itself"* 다(03:51~04:11). 화자는 논문 제목을 말하지 않는다. 1986이라는 연도는 *No Silver Bullet*과 맞는다.

## 5. Product engineer (04:11~04:42)

- *"I've decided to call this job the product engineer. This is somebody who finds out what people need, defines what good looks like, and ships it uh with agents doing the typing."*(04:12~04:21)
- **스스로 유보한다**: *"You have to take this with a grain of salt. Am I Am I just thinking that the thing that I enjoy about software development, which is figuring out what the problem is, is the hard part of software? You can tell me if I'm wrong."*(04:23~04:32)

## 6. 주니어의 연습 기회는 어디로 (04:33~05:59)

- *"Programming goes to zero, product engineering goes to infinity."*(04:44~04:48) 예전에는 주니어에게 잘 정의된 티켓을 주고 틀린 점을 지적하며 키웠다. *"that is gone because (…) That's what we do with the coding agents now."*(05:08~05:14)
- 그래도 forward-deployed engineer와 product engineer는 *"enormous number"* 가 필요하다. *"Universities teach data structures, boot camps teach React, nobody teaches go sit with a baker for a week and come back with a spec, and that is the person that we need."*(05:35~05:43) 그래서 *"you're going to have to grow them on purpose."*(05:45~05:48) → [[ai-jobs-impact]]

## 7. 오늘부터 바꿀 일 (05:59~07:05)

1. **high blast radius 코드만 리뷰하라.** *"write down your high blast radius code and make that be the only thing that you are reviewing anymore because the rest of it your automatic reviewers are going to get done."*(06:02~06:12) → [[risk-proportional-human-review]]
2. **검증이 싼 것은 위임하라.** 리뷰 절차를 고민하기보다 자동 판정 수단을 만들어 에이전트에게 먹여라(06:13~06:27). → [[verifiable-goals]]
3. **최고 인력의 판단을 문서로 옮겨라.** *"put your best people's judgment into specs and rubrics and evals. You knew I the arise guy was going to say evals at some point."*(06:29~06:35) *"turning the sense of the problem into a spec of the problem so that the agents can build it for us."*(06:46~06:51) → [[spec-driven-development]] · [[taste-encoded-evals]]
4. **올바른 것을 재라.** *"741% more code was never the point. Measure how much stuff you are actually shipping."*(06:52~06:58) 리뷰어 코멘트가 실제로 반영되는 비율도 재고, *"the gap between the tests passed and a maintainer would merge this"*(07:01~07:04)도 재라. → [[mergeability-gap]]

## 이 위키와의 연결

### 이어지는 것

- **[[tech-bridge-death-of-code-review]](10-02, 같은 화자의 다른 강연)**: 그 편은 *741% vs 30%* 로 리뷰 병목을 진단하고 *"stop reviewing PRs"* 로 끝났다. 이 편은 그 처방을 넷으로 줄이고, **리뷰 다음에 올 병목**을 순서대로 짚는다. 마지막 지표(테스트 통과와 머지 가능 사이의 간격)는 10-02 편 [[mergeability-gap]]과 같은 말이다.
- **[[verification-bottleneck]]**: 위키의 여러 소스가 *"병목이 생성에서 검증으로 옮겨 갔다"* 고 말했다. 이 편은 한 단계 더 나아가 **검증 이후에도 병목이 계속 옮겨 가다가 결국 문제 정의에 머문다**고 베팅한다.
- **[[spec-driven-development]]**: 빵집 예시와 *"come back with a spec"* 은 명세를 **고객에게서 꺼내는 일**로 본다. 명세를 에이전트 입력으로 쓰는 쪽보다 앞단이다.

### 긴장

- **화자가 스스로 붙인 단서**(*"the thing that I enjoy (…) is the hard part"*)가 그대로 유보 사항이다. product engineer 전망은 자기 취향을 투사한 것일 수 있다.
- [[ai-jobs-impact]]의 표에 이 편을 넣을 수 없다. 일자리 수를 예측하지 않고 **훈련 경로**만 문제 삼기 때문이다.

## 해소하지 않고 표시만 한 것

- 원본 강연의 제목 · 날짜 · 링크가 없다. 화자 귀속은 설명란 · 태그와 *"the arise guy"* 근거다.
- 제약 이론의 *"his"* 는 귀속하지 않았다.
- *"741%"* 의 출처는 이 발췌에서 다시 밝혀지지 않는다(10-02 편에서는 2차 인용이었다).
- 무캡션 6구간(제목 카드로 추정)의 내용은 모른다.

## 등장 개체

- 인물: [[laurie-voss]] · Fred Brooks(인용, 페이지 없음)
- 조직: [[arize-ai]](자기 언급 *"the arise guy"*) · npm(설명란, 페이지 없음)
- 개념: [[verification-bottleneck]] · [[spec-driven-development]] · [[taste-encoded-evals]] · [[risk-proportional-human-review]] · [[verifiable-goals]] · [[mergeability-gap]] · [[ai-jobs-impact]]

## References

- 원본 영상: <https://www.youtube.com/watch?v=SHGxL8DQOxs> (7:18, `upload_date` 2026-10-26 UTC = 2026-10-27 07:00 KST)
- raw: `01.raw/articles/2026-10-26_AI가 코딩하는데 당신을 왜 뽑죠 - npm 공동 창업자가 말하는 개발자의 다음 역할.md`
- [[tech-bridge]] · [[laurie-voss]] · [[tech-bridge-death-of-code-review]]

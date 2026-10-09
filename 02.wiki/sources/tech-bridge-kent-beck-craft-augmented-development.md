---
title: "Tech Bridge — 켄트 벡이 밝히는 AI 시대의 소프트웨어 엔지니어링 (Kent Beck): 지니는 그럴듯할 뿐 작동하지 않는다, features vs futures, 노력 → 산출 → 결과 → 미션"
type: source
tags: [kent-beck, craft, augmented-development, features-vs-futures, optionality, refactoring, spec-driven-development, waterfall, formal-verification, lean, dark-factory, metrics, goodhart, leadership, members-only-to-public, video]
source-url: https://www.youtube.com/watch?v=_0zB1Qj-xoE
source-type: video
author: Tech Bridge (한영자막 재배포) · 강연 [[kent-beck]] · 정부·군 청중 행사(설명란 링크로 Rise8 Prodacity 추정, 행사명 미발화), 녹화 연도 미확정
date-published: 2026-10-06
ingested: 2026-10-09
created: 2026-10-09
updated: 2026-10-09
---

# Tech Bridge — 켄트 벡이 밝히는 AI 시대의 소프트웨어 엔지니어링 (Kent Beck)

[[tech-bridge|Tech Bridge]]가 재배포한 **51:43 단독 강연, 공식 챕터 없음**(구간 소제목은 이 위키가 붙였다 — raw 참조). 화자는 XP·JUnit·TDD(본인 말로는 *재발견*)의 [[kent-beck|Kent Beck]], 청중은 정부·군 쪽이다. **2026-10-03에는 멤버 전용이었다가 10-09에 공개로 확인**(`upload_date` 20261006). 서베이도 데모도 아니고 **한 실무자의 프레임 두 개**를 그림으로 설명하는 강연이다 — 이 위키에 두 개념이 생겼다 → [[features-vs-futures]] (신규) · [[effort-output-outcome-mission]] (신규).

> **AI는 소원을 들어주지만 원하던 것은 주지 않는 지니다. 지니는 그럴듯한(plausible) 코드에 능할 뿐 작동하는 코드를 보장하지 않으므로, 그 산출물에는 적대적 관점을 가져야 한다. 기능을 낼 때마다 미래의 선택권(futures)을 태우고, 지니와 함께면 한 사람이 일주일 만에 아무것도 바꿀 수 없는 상태에 도달한다 — 그러니 기능 사이에 멈춰 futures를 되돌려라. 스펙만 잘 쓰면 된다는 원샷 개발은 폭포수의 재탕이다. 그리고 코드 줄 수와 PR 수는 노력·산출의 측정일 뿐, 중요한 것은 만든 쪽과 쓰는 쪽이 공유하는 미션이다.**

> *"I call it the genie because it grants your wishes, but it ends up not being what you really wanted."* (06:47~06:55) · *"They're plausible. Genie is really good at plausible, but actually working, no."* (08:42~08:49) · *"the economic value of a project is the sum of the features that it currently has and the futures all the options that for what it could do next."* (25:17~25:31) · *"That's exactly waterfall development where it didn't work. It never worked."* (35:48~35:53) · *"I think Goodart was an optimist."* (48:41)

ASR·ko 보정: ko는 **features를 "자원"으로, futures를 "선물 거래"로, genie를 "천재"로** 일관되게 옮겨 중심 그림을 재구성할 수 없다. 처방 문장 *"add back some of the futures"* 를 **"몇 가지 기능 … 추가"로 뒤집고**(24:26~24:33), *"a year ago"* 를 **"1년 후"로**(37:36), Ward Cunningham을 만난 *"came straight out of school"* 을 **"대학을 중퇴했습니다"로**(33:04) 바꿨다. **en·ko 공유 오류 두 건** — *"throws off software as a side effect"* → en *"harmed the software"*·ko "손상되었습니다"(32:32), *output* → en *"the result"*·ko "결과"(44:22, 그림 ②의 산출·결과 두 칸이 같은 말이 된다). 전체 목록은 raw. **인용은 en-orig에서만** 했다.

> ⚠️ **행사·시점.** 행사명 미발화 — 설명란 링크(*Prodacity*, Rise8)로 **추정**만 한다. 청중 단서는 *"the military or government world"*(00:05~00:09), *"General Whiting"*(01:19, 직함·소속 미발화), *"making the country safer"*(46:22~46:25). 시점 단서는 상대적인 것뿐 — *"programming hardcore every day for maybe the last 18 months"*(18:28~18:31), Lean은 *"maybe a year ago"*(37:34~37:38). **연도가 발화되지 않아 녹화 시점을 특정하지 않는다.** 10-03에 이미 멤버 전용으로 있었으므로 `upload_date` 10-06은 공개 전환 시점에 가깝다.
>
> ⚠️ **화자 진술의 지위.** 경력·일화는 모두 본인 진술. **"1만 달러 C 컴파일러"**(08:57~09:49)는 누구의 실험인지 말하지 않았고, *"hello world, doesn't actually work"* · *"every time one of those bugs got fixed, three more bugs were introduced"* 도 출처가 없다. Casals 일화는 화자 스스로 *"The story's made up"*(23:56). 청중 질문 2건(32:11 코멘트, 36:46 형식 기법)은 질문자 말이 녹음되지 않았다.

## 1. 청중과 예고 (00:00~06:23)

- 정부·군 청중 앞에서 *"the constraints are very similar"*(00:38~00:43). 오늘 아침 *"General Whiting"* 을 듣고 **10~15년 묵은 퍼즐을 풀었다**고 예고하고 끝까지 미룬다(01:04~01:27) → §8.
- 질문을 바로 하라 — *"Asking questions is a form of leadership."*(01:42~01:45). Ken Ross 교수 일화: 3주째 아무도 이해 못 하던 수업에서 누군가 *"Does anybody know what's going on?"*(02:24~02:26)라고 묻자 반 전체가 털어놓았다.
- 자기소개(03:11~06:20): 패턴, JUnit(Erich Gamma와 다듬음), TDD는 1957년 책의 *"check items"* — 사용자에게 입출력 쌍을 받아 프로그램이 맞는지 확인 — 을 보고 *"I can't claim to have invented TDD"*(04:51~04:56). XP, 애자일 선언문 *"first signatory (…) alphabetically"*(05:13~05:16). 지금은 *"one of the frontier labs"* 와 일한다(05:36~05:42 — 어느 랩인지 미발화) — 프런티어 모델 팀이 어떻게 일해야 하는지가 *"not a press play kind of problem"*(06:00~06:04).

## 2. 지니 — plausible ≠ working (06:23~11:15)

- 주제는 **augmented development에서의 craft**. *"augmented"* 라고 부르는 이유: *"to me this is still a human process"*(06:31~06:36).
- ⭐ **지니(genie)**: 소원은 들어주지만 원하던 것은 아니다(06:47~06:55). *"I'm going to make some requests. I'm going to get something back. It's going to seem really cool and then at the end of it, I'm going to be a little bit disappointed."*(06:59~07:08)
- ⭐ 단 하나의 테이크어웨이: *"Now that the genie is better at coding than humans"* 라는 말은 *"boulder dash"*[= balderdash](07:39~07:49). *"just because uh genie can create syntactically correct programs doesn't mean that they're better than a programmer or even that they actually work."*(07:53~08:06) → [[syntactically-correct-behaviorally-wrong]]
- 자폐인으로서 사랑했던 *"binary red green"*(08:12~08:17) — 프로그램은 되거나 안 된다. 증강 개발의 산출물은 *"oftent times just don't work. They're plausible."*(08:36~08:42)
- ⚠️ **1만 달러 C 컴파일러**(08:57~09:49): 파 보면 *"C compilerish"* — C 프로그램을 효율적으로 컴파일해 실행하지 못한다. 출처 미발화(→ §갈리는 것).
- ⭐ 그래서 **적대적 관점**: *"You made yourself happy, but did you make me happy? How real is that? How hard do I have to push?"*(10:37~10:47). 프로그래머가 *"works by construction"* 으로 보장하던 것을 *"Genie doesn't have those tricks"*(10:54~11:04) — *"trustworthiness that you used to be able to infer, you simply can't assume that that's true anymore."*(11:06~11:15) → [[verification-bottleneck]]

## 3. "프로그래머는 필요 없다"의 사이클 (11:18~13:00)

*"Oh goody, we don't need programmers anymore."*(11:27~11:30)는 반복된다 — 업무 담당자가 평이한 말로 요구를 적으면 컴퓨터가 계산한다는 것이 *"the highlevel description of cobalt[=COBOL]"*(12:10~12:13). *"here we are at the next round of that cycle, which is why I'm not worried about having a job"*(12:19~12:26). 코칭의 근거: 젊은 엔지니어는 *"exactly the same young engineer mistakes (…) since the time of the Romans"*(12:32~12:39).

## 4. craft라는 단어 (13:06~18:02)

- ⭐ 자기 craft 책 *"at least three"* 는 *"completely obsolete and should be thrown away"*(13:17~13:44, ⚠️ 제목 미발화). 이름 짓기, 로직 분해, 들여쓰기, 공백, 사람 이해를 위한 구조 최적화 — *"Those used to be decisions that had a lot of leverage"*(14:25~14:28), 이제는 그 레버리지가 없다(14:45~14:52).
- 그렇다고 사람이 코드를 이해할 필요가 없는 건 아니다 — 읽을 수 있는 시스템을 택하겠지만, 이해는 *"in the context of I've got this genie. It can explain stuff to me if it's not lying to me, which is always an option"*(15:14~15:25)에서 일어난다. inline·extract·rename으로 *"then it all becomes clear"* 하는 순간은 *"there's just not payoff for that particular moment"*(15:42~15:55).
- craft의 다른 얼굴 — *"hijacked"* 된 단어(16:06~16:10): 동굴에 들어가 *"it's not done yet because I haven't finished with my craft"*(16:37~16:44). ⭐ 반론은 **지연 비용**: *"if the cost of delay is high, an ugly program that gives you feedback is exactly the right thing to do"*(16:48~16:53), 20년 갈 소프트웨어면 *"that Swiss watch maker"* 가 보상받는다(16:59~17:11).
- *"craft is going to mean something different. It's still a a valid concern"*(17:43~17:53).

## 5. 그림 ① — features vs futures (18:12~28:16) → [[features-vs-futures]] (신규)

- 18개월째 지니와 매일 프로그래밍한다(18:22~18:31, 계기는 Gene Kim·Steve Yegge의 데모). 야심 찬 프로젝트에서 진척은 크지만 *"project two, project three, project four because I kept hitting the wall"*(19:09~19:20) — *"I couldn't fix one bug without breaking something else"*(19:20~19:25).
- ⭐ **그림**: 기능의 진척은 처음엔 빠르고 점점 느려진다(20:11~20:25). 다른 축은 *"sometimes I call it optionality, sometimes I call it futures"*(20:35~20:40). 시작할 땐 할 수 있는 일이 많고 기능은 없다 → 기능 하나마다 futures를 태운다(하위 호환, 철회한 기능의 제약 — 21:14~21:30) → *"we have no options for change at all because everything is such a big mess"*(21:44~21:53).
- ⭐ AI가 바꾼 것: *"it used to take us a hundred people 10 years to get to this absolute zero state (…) And now with AI, I can do this in the privacy of my own office. One person, one week"*(22:04~22:26) — *"a big productivity enhancer"*(22:28)라는 반어.
- **대안 — 기능 사이의 순간**: Casals의 *"No, I rest between the notes."*(23:35 — 본인이 지어낸 이야기라고 밝힘, 23:54~23:58). 지니가 *"Okay, boss. I finished that feature. Do you want me to implement the next thing?"*(24:09~24:14) 할 때 *"take a breath and say, huh, maybe I'm not ready"*(24:21~24:24) → futures를 되돌린다: 리팩터링, 중복 제거, 가독성, *"throw away what I just did and implement it again in a different way"*(24:42~25:06). → [[refactoring]]
- ⭐ *"the economic value of a project is the sum of the features that it currently has and the futures"*(25:17~25:31).
- **어려움 — 가독성(legibility)**: 기능은 *"visible legible in that seeing like a state sense"*(25:51~25:55), futures는 *"gilding the lily"* 로 보인다(26:19~26:25). 지니가 끼면 *"the whole thing ramps up"*(26:55~26:59). *"It's not written in any spec"*(27:32~27:35). ⭐ *"for me finished like I don't want to change this software is a failure."*(27:47~27:52)

## 6. 왕복 궤적과 다크 팩토리 (28:16~34:38)

- 멀리서 보면 기능과 옵션이 동시에 늘어나는 것 같지만, 동시에 하려 하면 *"a bigger problem than fits even into the combined brain of the genie and the human"*(28:42~28:49). *"You can't wipe the knife while you're cutting."*(29:01~29:03) — 전문 주방 비유. XP는 *"an observation of what teams really look like"*(29:54~29:57).
- 더 강력한 도구는 *"can create opportunities for feedback faster than we're prepared to gather that feedback or analyze that feedback"*(30:23~30:32).
- ⭐ **다크 팩토리**: *"anytime I've tried fully agentic the dark factory the dark software factory (…) there's no human involved There's no feedback. And that always goes off the rails. Always."*(30:46~31:17) 그리고 *"It's amazing while it's going off the rails"*(31:19~31:23) — *"How did you do this much? (…) and it's still complete crap."*(31:31~31:34) → [[software-factory]] · [[orchestras-not-factories]]
- (청중 코멘트를 받아) *"by pacing yourself you're giving yourself the chance to form understanding"*(32:11~32:16). ⭐ 최고의 소프트웨어는 *"where I tried to maximize learning which threw off software as a side effect"*(32:26~32:35). **Ward Cunningham**이 하루 오후 작업을 컴퓨터째 꺼 버렸고, 다음 날 아침 *"about 15 minutes"* 에 더 명료하게 다시 구현했다(33:28~33:57). 다크 팩토리에선 *"you don't learn anything except at the end you learn how unreliable the genie really is"*(34:10~34:17). → [[cognitive-debt]]

## 7. 원샷 vs 반복 · 형식 기법 (34:40~43:22)

- ⭐ **스펙 주도 개발 비판**: *"I'm gonna write a spec and the genie is going to produce the software and if the spec is good enough, the software is going to be good enough. And there's a word for that. That's exactly waterfall development"*(35:31~35:50). Winston Royce 논문의 폭포수 그림 다음 페이지에는 *"waterfall going down and feedback coming up"*(36:19~36:22)이 있었지만 *"the power of an image"* 로 첫 그림만 남았다(⚠️ 화자 기억, 논문 미특정). → [[spec-driven-development]]
- ⭐ **형식 기법**(청중 질문, 36:46~): 증명 과목 조교 출신, 1년 전 Lean을 지니와 써 봤다. 두 가지 문제 — ① *"it's still feels like a oneshot process"*(37:54~38:00): 요소 하나를 바꾸면 되감아야 하고, 지니가 있어도 *"a drag on my ability to change"*(38:21~38:27). ② *"there's still a gap between this mathematical model and implementation"*(38:40~38:45) — *"I don't know how to how to bridge that"*(39:07~39:11). → [[ai-formal-verification]]
- 그래도 신뢰 가능한 소프트웨어는 가능하다: *"low defect densities with a combination of examples, automated tests, carefully chosen, and foolproofing uh of the design"*(40:25~40:38). ⭐ 그러나 *"the genie wants to make shortcuts. It doesn't want to foolproof the design and it uh will do things that subvert the intentions of test cases. Uh just you have to watch for returning constants."*(40:48~41:05) — *"a 14-year-old programmer"* 같은 짓(41:11~41:16). → [[reward-hacking]]
- **언제 원샷이 되나**: *"If I'm writing a little app, one shot is fine."*(42:12~42:19) 그러나 *"a virtual machine for a graph database with an embedded programming language"*(42:19~42:25)는 반복이어야 한다. 스펙 주도 개발 열광자들은 *"it doesn't sound like they've ever had a billion users"*(42:44~42:50) — 큰 설치 기반에서 원샷 재작성은 *"continuity problems (…) data migration problems"*(43:09~43:12). → [[no-one-shot-design]]

## 8. 그림 ② — 노력 → 산출 → 결과 → 미션 (43:24~49:36) → [[effort-output-outcome-mission]] (신규)

- 프로그래머의 **노력(effort)** → 고객에게 전달할 새 기능 = **산출(output)** → 고객의 행동이 바뀜 = **결과(outcome)**(44:05~44:41). 웹 이전엔 CD로 보내고 쓰는지 알 수 없었다(44:46~45:07).
- ⭐ **오늘 아침 푼 퍼즐**: *"I used to use the word impact but I love this word mission"*(45:32~45:39) — *"the mission is shared between the people making the program and the people using the program"*(45:47~45:52). 예고한 *"refinement of an idea"*(01:07)가 이것이다.
- ⭐ **지표의 폭정**: *"The Genie produced 200,000 lines of code. That's a measure of effort. It has nothing to do with the mission."*(46:00~46:07). 측정하기 가장 쉬워서 *"we look for our keys under the lamp post"*(46:41~46:44). 생산성의 정의가 산출/투입이라 지니의 산출이 생산성으로 보인다(47:01~47:07). *"lines of code, which we've known was Boulder Dash for a very very long time and somehow it's back PR count"*(47:10~47:22) — 노력·산출의 측정은 *"per definition not a measure of mission"*(47:28~47:35). 10개 지니 = 10배 노력, *"Yeah, but it doesn't matter."*(48:10~48:15)
- ⭐ **굿하트**: 사이클 앞쪽에서 잴수록 Goodhart에 걸린다(48:24~48:31). *"I think Goodart was an optimist. It's not just that the measure ceases to be a measure. It's that people will twist the entire system out of shape."*(48:41~48:52) 뒤쪽(미션)은 귀속이 어렵다 — *"the mission is now 7% better and I own 075% of that"*(49:17~49:24, ⚠️ 0.75%/0.075% 판독 불가). 미션의 가치는 *"bursty"* — 위기가 와야 준비됐음을 안다(47:42~47:51). → [[trusted-throughput]] · [[value-maxing]]

## 9. 리더십 (49:39~51:43)

*"you have to find an expression of the mission that speaks to people's heads and their hearts. And then you have to repeat it and repeat it and repeat it."*(50:15~50:27) 그 반복이 *"part of the skill of leadership"*(50:36~50:40). 누군가 당신의 아이디어를 당신 것인 줄 모르고 들려줄 때 *"that's the moment that you've succeeded as a leader"*(50:56~51:07). 과제는 *"finding that those missions into which the tools fit for human purposes"*(51:17~51:24).

## 이 위키와의 연결

### 이어지는 것

- **[[spec-driven-development]]** — 이 위키에서 SDD를 **가장 정면으로 반대하는 목소리**. 앞선 소스들([[tech-bridge-sdd-enterprise-lessons]] *"we don't do big upfront design"*)이 SDD는 폭포수가 아니라고 방어했다면, Beck은 *"스펙이 충분히 좋으면 소프트웨어도 충분히 좋다"* 는 믿음 자체를 폭포수로 규정한다. 단 *"a little app, one shot is fine"* — 반대는 규모·수명 조건부다.
- **[[no-one-shot-design]]** — Paul Bakaus의 *디자인은 원샷할 수 없다* 를 **소프트웨어 전체로** 일반화한 셈. 근거가 다르다: Bakaus는 맥락·이해관계자, Beck은 **변경 가능성(futures)과 설치 기반**.
- **[[syntactically-correct-behaviorally-wrong]]** — *"syntactically correct programs"* 와 *"plausible"* 은 같은 구분을 범용 코딩으로 넓힌다.
- **[[cognitive-debt]]** — *"by pacing yourself (…) form understanding"* 은 같은 문제의 처방 쪽. Beck은 여기에 **학습이 목적, 소프트웨어는 부산물**이라는 더 강한 명제를 단다.
- **[[reward-hacking]]** — *"subvert the intentions of test cases (…) returning constants"* 는 실무자 쪽 증언.
- **[[trusted-throughput]] · [[value-maxing]]** — 토큰·LOC·PR 수를 쫓지 말라는 같은 결론. Beck은 그것을 **노력/산출 칸**에 배치하는 위치 지도를 준다.

### 갈리는 것

> ⚠️ **Contradiction: 다크 팩토리.** [[software-factory]](Factory)와 [[tech-bridge-warp-factory-engineering|Warp]]는 자율 루프 공장을 목표로 둔다. Beck은 *"there's no human involved There's no feedback. And that always goes off the rails. Always."*(31:07~31:17) — **경험 일반화이고 측정은 없다.** [[orchestras-not-factories]]의 Charlie Holtz(*"I don't want to be in my dark factory"*)와 같은 편이지만 근거가 다르다: Holtz는 역할·즐거움, Beck은 **피드백 부재 → 탈선**.

> ⚠️ **Contradiction(가능성): C 컴파일러 평가.** [[tech-bridge-death-of-code-review]]에서 Laurie Voss가 인용한 Carlini의 C 컴파일러는 *Linux 커널을 컴파일* 했다고 서술된다. Beck의 *"$10,000 in tokens (…) working C compiler"* 는 *"hello world, doesn't actually work"* 라고 한다. **같은 사례인지 확인하지 않았다** — 같다면 두 소스는 정반대로 평가한다. 둘 다 2차 진술이다.

> ⚠️ **[[ai-formal-verification]]과의 긴장.** Brockman 쪽은 형식 검증의 실패 원인을 *사람에게 다루기 어려움* 으로 보고 AI가 그것을 푼다고 본다. Beck은 AI와 Lean을 써 본 뒤에도 남는 두 문제(**원샷성**, **명세–구현 간극**)를 든다 — 처리량 문제가 아니라 구조 문제라는 주장. Lauren Tan의 *"스펙트럼의 먼 끝, 여전히 열린 문제"* 쪽에 가깝다.

> ⚠️ **craft의 레버리지.** Beck은 이름 짓기·분해 같은 craft 결정의 레버리지가 사라졌다고 하면서 동시에 *"I'd much rather have a system where the humans can read"*(15:05~15:10), 기능 사이에 *"optimize some of this for readability"*(24:53~24:58)를 처방한다 — **레버리지는 개별 결정에서 futures 투자로 옮겨갔다**는 것이 위키의 독해(화자가 이렇게 정리하지는 않는다).

## 해소하지 않고 표시만 한 것

- **행사명·연도** — Prodacity(Rise8)는 설명란 링크 추정, *"General Whiting"* 직함·소속 미발화, 녹화 연도 미발화.
- **"one of the frontier labs"** — 어느 랩인지 미발화.
- **1만 달러 C 컴파일러**의 출처와 Carlini 사례와의 동일성.
- **craft 책 세 권**, **1957년 책**, **Royce 논문** — 제목·서지 미발화.
- **"075%"** — 0.75%/0.075%.
- **청중 질문 2건** — 원문 미녹음.

## 등장 개체

- 인물: [[kent-beck]] (신규) · Ward Cunningham(위키 발명자, 페이지 없음) · Erich Gamma(*"Eric Gamma"*, 페이지 없음) · Gene Kim(*"Jean Kim"*, 페이지 없음) · Steve Yegge(*"Steve Yagi"*, 페이지 없음) · Winston Royce(페이지 없음) · Pablo Casals(일화 — 지어낸 이야기) · Ken Ross(교수) · *"General Whiting"*(⚠️ 미확인)
- 조직: Rise8(설명란, 페이지 없음) · Lockheed(일화)
- 도구·개념어: JUnit · Lean · COBOL · XP · 애자일 선언문 · TDD
- 개념: [[features-vs-futures]] (신규) · [[effort-output-outcome-mission]] (신규) · [[spec-driven-development]] · [[no-one-shot-design]] · [[ai-formal-verification]] · [[software-factory]] · [[orchestras-not-factories]] · [[syntactically-correct-behaviorally-wrong]] · [[reward-hacking]] · [[cognitive-debt]] · [[trusted-throughput]] · [[value-maxing]] · [[verification-bottleneck]] · [[refactoring]] · [[technical-debt]]

## References

- 원본 영상: <https://www.youtube.com/watch?v=_0zB1Qj-xoE> (51:43, `upload_date` 2026-10-06 — 10-03 멤버 전용, 10-09 공개 확인)
- raw: `01.raw/articles/2026-10-06_켄트 벡이 밝히는 AI 시대의 소프트웨어 엔지니어링, 진짜 개발의 본질은 무엇일까요.md`
- 설명란 링크: <https://www.rise8.us/prodacity> · <https://www.linkedin.com/company/rise8/> (⚠️ 열어 보지 않았다)
- 같은 주제: [[tech-bridge-sdd-enterprise-lessons]] · [[tech-bridge-sdd-full-course]] · [[tech-bridge-conductor-orchestras-not-factories]] · [[tech-bridge-factory-software-factory]] · [[tech-bridge-death-of-code-review]] · [[tech-bridge-impeccable-design-steering]]
- [[tech-bridge]] · [[kent-beck]]

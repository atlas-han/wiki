---
title: "Shopify CTO가 말하는 AI 비용, 아낄 곳과 쓸 곳"
type: video
source: https://www.youtube.com/watch?v=wDTO-nR4yTM
site: youtube.com
author:
  - "[[Tech Bridge]]"
duration: 8:24
published: 2026-10-27
created: 2026-10-28
description: "Mikhail Parakhin(Shopify CTO, 제목 근거) 인터뷰 발췌 편집본 8:24, 공식 챕터 8. 바닥이 아니라 천장을 높이는 AI, 복잡도로 정규화한 생산성 측정, '항상 가장 큰 모델'과 전 직원 무제한 토큰, 회사의 디지털 트윈과 반사실적 개입, 프로젝트 지연을 미리 알리는 팀 관리, 개발엔 최대 모델 · 운영엔 파인튜닝한 싼 모델이라는 바벨 전략. 원본 인터뷰의 제목 · 날짜 · 링크 · 진행자는 설명란에 없다."
tags:
  - clippings/youtube
---

**Source URL**: https://www.youtube.com/watch?v=wDTO-nR4yTM
**Channel**: Tech Bridge · **Duration**: 8:24 · **Published**: 2026-10-27

> **게시일.** info.json 기준 `upload_date` **`20261027`**(UTC), `timestamp` 1793138411(= **2026-10-28 07:00 KST**), `availability: public`. 2026-10-28 회차 목록에 처음 나왔다.
>
> **오디오 트랙과 자막 — 인용 규칙.** 10-27 Voss 편과 같은 구성이다. 오디오는 **`English (US) original (default)`** 하나가 원본이고, 나머지(de · es · fr · hi · id · it …)는 더빙이다. **한국어 오디오 트랙이 없다.** 메타 `language`=`en`. 수동 자막 없음. `automatic_captions`에 `ko-orig`가 **없고**, 받은 **ko는 `lang=en&tlang=ko` 기계 번역**이다. **en-orig = 원음 영어 ASR** → **인용은 전부 en-orig로 한다.** `en`은 en-orig와 줄 수가 다르지만(181 vs 193) 같은 영어 ASR 계열이다. `--sleep-subtitles 8`로 429 없음.
>
> **형식 — 해설 없는 발췌 편집본.** en-orig에 한국어 내레이션 구간이 없다. 무캡션 간격 6곳 — 00:00~00:16 · 01:24~01:37 · 02:11~02:25 · 03:06~03:19 · 05:11~05:24 · 06:46~07:02 — 은 공식 챕터 경계(00:00 · 01:25 · 02:12 · 03:07 · 05:11 · 06:48)와 겹친다. **제목 카드 구간으로 추정**하고, 그 구간에 무슨 말이 있었는지는 쓰지 않는다.
>
> **화자.** 발화에 이름이 없다. 제목 *"Shopify CTO"*, 설명란 *"Mikhail Parakhin이 설명하는 AI 활용 전략"*, 태그 `Mikhail Parakhin` · `Shopify`. 화자 스스로 *"at Shopify we have unlimited tokens for everybody"*(02:50~02:55)라고 말한다. 01:04~01:08 한 줄(*"So you're raising the floor but actually don't forget you can also raise the ceiling."*)과 07:52 `>>` 표시는 **다른 화자(진행자)** 다. 진행자 이름은 발화 · 설명란에 없다. 태그에 `Boris` · `Claude` · `Claude Code`가 있으나 **누구를 가리키는지 설명란에 근거가 없어 진행자로 귀속하지 않는다.** 원본 인터뷰 제목 · 날짜 · 링크는 없다.
>
> ⚠️ **ASR 판독.** *"JSD system get stuff done"*(01:53~01:56) → 화자가 설명하는 사내 시스템 이름은 *GSD(get stuff done)* 로 읽힌다(판독 추정). *"creating that center"*(00:54~00:56, 체스 비유) → *centaur*로 읽힌다(판독 추정). *"auto research"*(07:37 · 07:50)는 원문 그대로. **08:07~08:21 en-orig(*"Tony I'm young. When you're at home more than A I YouTube Tommy"*)는 판독 불가** — 음악 · 아웃트로 오인식으로 보고 인용하지 않는다. ko는 이 구간을 옮기지 않았다.
>
> ⚠️ **ko(기계 번역) 오역.** *"auto research the hell out of it"* → *"가능한 한 많은 것을 다음과 같은 방식으로 조사하십시오. 자동화하여"*(07:49~07:51), *"Budget for it if that cost"* → *"예산을 사용하여 가능한 가장 큰 모델"*. ko는 인용 근거로 쓰지 않는다.
>
> ⚠️ **수치 · 주장.** 수치가 없다. *"very precise at measuring percentages of productivity"*(02:07~02:11)라고 하지만 퍼센트를 말하지 않는다. 디지털 트윈의 *"very direct impact on our bottom line"*(05:06~05:11)도 금액 없는 당사자 진술이다.

## 설명란

Shopify는 왜 직원들에게 AI 토큰을 제한 없이 제공할까요? Mikhail Parakhin이 설명하는 AI 활용 전략을 살펴봅니다. 단순히 일을 더 빨리 끝내는 것을 넘어, 전에는 불가능했던 일을 가능하게 하는 접근입니다.

프로젝트 복잡도를 고려한 생산성 측정, 회사의 디지털 트윈, 일정 지연을 미리 감지하는 팀 관리까지 다룹니다. 개발과 실험에는 가장 큰 모델을 활용하고, 실제 서비스에서는 비용·처리량·품질에 맞게 최적화하는 바벨 전략도 소개합니다.

00:00 왜 토큰을 무제한으로 제공할까?
00:16 바닥을 높이는 AI, 천장을 높이는 AI
01:25 생산성을 측정하는 방법
02:12 가장 큰 모델과 무제한 토큰
03:07 회사의 디지털 트윈
05:11 AI로 달라지는 팀 관리
06:48 개발과 운영의 바벨 전략
08:05 새로운 가능성을 찾는 투자

#Shopify #Claude #AI #ClaudeCode #개발자 #생산성

> info.json `tags`: AI · AI 토큰 · Boris · Claude · Claude Code · Mikhail Parakhin · Shopify · 개발자 · 디지털 트윈 · 바벨 전략 · 생산성

## 트랜스크립트 — en-orig (원음 영어 ASR — 인용 근거)

[00:16] It's not that LLM's take away the
[00:19] drudgery work or the work that you
[00:22] didn't want to do and now they do it so
[00:25] now you can do like interesting things
[00:27] more
[00:28] sophisticated.
[00:30] Is that you can do things that you
[00:32] previously couldn't take any amount of
[00:34] time, no amount of helpers. Like I could
[00:36] have had thousand new best
[00:37] mathematicians at my disposal. I still
[00:39] wouldn't be able to do it.
[00:41] But with a model I I can. And the the
[00:44] for the best problems right now I see is
[00:46] that I cannot solve it without the model
[00:49] but then model cannot solve it without
[00:50] me either.
[00:51] It requires you know this back and forth
[00:54] and you know creating that center you
[00:56] know using chess analogy. Uh the that
[01:00] together like is better than the model
[01:02] and better than a human being.
[01:04] >> So you're raising the floor but actually
[01:06] don't forget you can also raise the
[01:08] ceiling. [music]
[01:08] >> Exactly. That's that is my point. Yes.
[01:10] This in raising raising ceiling is is
[01:14] much more impactful.
[01:15] Cuz raising the floor yeah you you could
[01:18] have just been more diligent or throw
[01:19] more people at it. Ceiling is there's no
[01:22] easy way to extend right like that's
[01:24] that's a real unlock.
[01:37] Uh
[01:38] we we have not only of course just like
[01:41] everybody else like estimate uh
[01:44] number of PRs and complexity of PRs but
[01:47] we we actually do things like estimating
[01:50] complexity of the project and in our
[01:53] uh system you know JSD system get stuff
[01:56] done. We could we You see that hey the
[01:59] teams of people are being
[02:01] able to execute on more projects faster
[02:04] and the
[02:05] normalized for complexity you can be
[02:07] very precise at measuring
[02:09] percentages of of productivity you're
[02:11] gaining.
[02:25] Always use the largest model.
[02:28] Like you because the largest model
[02:29] raises the ceiling the most. First of
[02:31] all, you don't know unless you use the
[02:33] large model and then and compare the
[02:34] results, you don't know what you're
[02:36] missing, right? It's a unknown unknown.
[02:38] Uh and that and that takes time. Second,
[02:41] always throw maximum uh thing at a
[02:44] problem and then
[02:46] until I see the evidence otherwise,
[02:49] that's what we're going to be doing. And
[02:50] that's why, you know, at Shopify we have
[02:52] unlimited tokens for everybody and
[02:55] that's why we run the heaviest models we
[02:57] can find. Uh that's why we we throw a
[03:00] lot of a lot of resources in our both
[03:03] GPU in inference and training and
[03:06] ability to optimize.
[03:19] The you know how text is just sequence
[03:22] of letters and LLMs learn really well
[03:25] how to predict the next and then they
[03:27] can complete the text. Human actions are
[03:29] very similar, but in our case more
[03:31] importantly, companies' actions are
[03:33] similar. You can represent a company as
[03:36] a sequence of actions. The company I
[03:38] don't know, open credit line, ship a
[03:40] product, like add make changes, like
[03:43] start accepting credit cards, take a
[03:44] loan. And I mean these are large
[03:47] changes, but all the immediate things
[03:48] that that company
[03:51] all of its employees, you know, in every
[03:53] second they're doing, it
[03:55] can all be turned into a sequence of
[03:57] actions. And then what happens is that
[03:59] you can create a digital twin of the
[04:01] company. And then you can start doing
[04:03] things to it instead of to real company,
[04:06] right? And then see what happens. So,
[04:08] you can have uh counterfactual
[04:10] interventions. You could say, "Oh, what
[04:12] if we add an advertising campaign? Or
[04:14] what if they started shipping, you know,
[04:16] 1 day faster? Or what if you know, it's
[04:19] all about our merchants. What if we give
[04:20] them a loan?"
[04:22] And then we find sequence of
[04:23] interactions that would maximize their
[04:26] chances of growth.
[04:28] Uh and then we we actually do that in
[04:30] production, right? So, we we go offer
[04:32] them a loan or we you know,
[04:36] uh
[04:37] push them to send them communication
[04:38] like for
[04:39] folks like your most important thing is
[04:41] to
[04:42] uh to start shipping faster or we start
[04:45] advertising campaign on, you know,
[04:46] Twitter. So, uh having ability to
[04:50] play with a company without endangering
[04:53] anything, you know, real people
[04:55] is is huge unlock. Because now now you
[04:58] can you can uh help more people to to be
[05:02] successful. So, this is very clear
[05:04] unlock that wouldn't have happened and
[05:06] that has like very direct impact on our
[05:09] bottom line and and the financial
[05:11] result.
[05:24] I thought that LLMs
[05:27] cannot really help me
[05:29] manage the team better. I could not have
[05:33] been more wrong.
[05:34] And after a while I realized uh
[05:37] I
[05:38] I flipped so much. I I created a little
[05:41] system that actually analyzes what
[05:44] everything is happening and
[05:47] proactively tells me, "It looks like
[05:49] this project's going to start slipping
[05:50] their deadline." It allows me to detect
[05:53] issues before they actually happen and
[05:55] go resolve it. And so, the whole system
[05:58] starts functioning much better.
[06:00] Now, technical side is even more
[06:02] important because the simple things
[06:05] LLM will go go down, but you know, LLM
[06:07] kind of very good at picking up signals
[06:09] and it it tries to please and so
[06:12] whatever you ask, the answer is very
[06:14] often in the question and it will just
[06:16] elucidate that and like give you exactly
[06:18] what you wanted, right? So, it's really
[06:19] important to want what's actually needed
[06:22] and not put in words first thing that
[06:24] comes to mind because then then your
[06:26] consequences could be actually worse
[06:28] than before because before at least
[06:31] it wouldn't be immediately built. There
[06:32] would be some discussion and now it's so
[06:34] much easier to just go and build it. So,
[06:36] technical acumen becomes more important
[06:39] and the human component of supervising
[06:41] now engineers who are supervising LLMs
[06:44] rather than supervising engineers who
[06:46] are typing, you know, pressing buttons.
[07:02] My main advice would be try to
[07:06] not limit tokens. You always need like
[07:09] circuit breakers because there always
[07:10] runaway processes that suddenly start
[07:12] burning tokens and
[07:14] and
[07:15] doing things bad, but it might not look
[07:17] like there's big difference between
[07:19] big models and small models. There's a
[07:21] huge world of difference and you want it
[07:24] you don't know the counterfactual so you
[07:26] you won't know which one which one's
[07:28] good. So,
[07:29] always use this
[07:31] dichotomy barbell strategy for anything
[07:34] coding, for anything
[07:36] development, testing, auto research.
[07:39] Use the largest model.
[07:41] Budget for it if that cost.
[07:44] For everything production, use
[07:46] fine-tuning, use the right model for
[07:48] that production, auto research the hell
[07:50] out of it so that you balance
[07:52] >> [music]
[07:52] >> both
[07:53] cost throughput and and quality.
[07:55] And save money on production by using
[07:58] cheaper models
[08:00] often fine-tuned.
[08:02] And
[08:03] invest money in development.
[08:07] >> Tony I'm young.
[08:10] When you're at home
[08:14] more than
[08:16] A I
[08:20] YouTube
[08:21] Tommy

## 트랜스크립트 — ko (`tlang=ko` 기계 번역 — 참고용, 인용하지 않음)

[00:17] 법학 석사(LLM) 과정이 일자리를 없애는 것은 아닙니다.
[00:19] 힘든 일이나 원하지 않았던 일
[00:22] 그렇게 하려고 했고, 이제 그들은 그렇게 하고 있으니, 이제
[00:24] 당신은 더 흥미로운 일들을 할 수 있습니다.
[00:27] 어, 세련됐네요. 당신은 할 수 있습니다
[00:30] 이전에는 할 수 없었던 일들, 심지어는 예전에도 할 수 없었던 일들
[00:32] 어떤 시간 동안이든, 또는 어떤 것과 함께든
[00:34] 어떤 형태의 도움이라도 좋습니다. 내 말은,
[00:36] 천 달러도 받을 수 있었잖아요.
[00:37] 제 생각에 최고의 수학자들입니다.
[00:38] 공급; 그렇더라도, 그런 일은 없을 것이다.
[00:40] 저는 해낼 수 있었습니다. 하지만 그 모델과 함께라면, 저는,
[00:42] 할 수 있어요. 그리고 최고를 위해
[00:45] 지금 당장은 문제가 있어서 제가 해결할 수 없다는 걸 알았습니다.
[00:47] 모델 없이 해결하세요. 하지만
[00:48] 이 모델은 그 문제들을 해결할 수 없습니다.
[00:50] 나의.
[00:52] 아시다시피, 이런 주고받기가 필요하죠.
[00:55] 아시다시피, 그 중심을 만들고, 그것을 활용하는 것 말입니다.
[00:58] 체스 비유는 함께 다음과 같습니다.
[01:00] 모델보다 낫고, 그보다 더 낫다
[01:03] 인간.
[01:04] 그러니까 지반을 높이는 건데,
[01:06] 당신도 그렇다는 사실을 잊지 마세요
[01:07] 지붕을 올릴 수 있어요.
[01:08] 정확히. 그게 제가 하고 싶은 말이에요. 예. 이것
[01:11] 그리고 천장 높이를 높이는 것은 훨씬 더 많은 의미를 지닙니다.
[01:14] 충격적인.
[01:16] 지반을 높이는 것이기 때문입니다. 당신은 할 수 있습니다
[01:18] 단순히 좀 더 부지런했더라면
[01:20] 더 많은 인력을 투입하세요. 지붕이 없어요.
[01:22] 쉽게 확장할 수 있는 방법이죠, 그렇죠?
[01:24] 진실? 이건 정말 큰 진전이에요. 여기요,
[01:39] 물론 우리는 뿐만 아니라,
[01:41] 다른 모든 사람들처럼, 추정치는 다음과 같습니다.
[01:44] PR의 수와 복잡성
[01:46] 홍보 자료일 뿐, 우리는 실제로 일을 합니다.
[01:49] 복잡성을 추정하는 방법
[01:51] 프로젝트와 우리 시스템에서는
[01:53] GSD 시스템, "일을 실현시키다"
[01:55] 그렇게 하세요." 우리는 그것을 볼 수 있습니다.
[01:59] 사람들로 구성된 팀은 다음과 같은 능력을 갖추고 있습니다.
[02:01] 더 많은 프로젝트를 더 빠르게 실행하고
[02:04] 복잡도에 따라 정규화되었습니다. 할 수 있다
[02:07] 측정할 때는 매우 정확해야 합니다.
[02:09] 당신이 나타내는 생산성 비율
[02:11] 승리. 항상 가장 적합한 모델을 사용하십시오.
[02:27] 당신처럼 큰, 왜냐하면 가장 모델이기 때문입니다.
[02:29] 가장 큰 것은 천장을 가장 높이 올리는 것입니다.
[02:31] 우선, 직접 경험해보지 않으면 알 수 없잖아요.
[02:32] 큰 모델을 사용한 다음
[02:34] 결과를 비교해 보세요, 당신은 모를 수도 있어요.
[02:35] 놓치고 있는 거잖아요, 그렇죠? ~이다
[02:37] 알 수 없는 낯선 사람. 네, 그게 다입니다.
[02:39] 그리고 그것은 시간이 걸립니다. 둘째, 항상
[02:42] 한 가지 문제에 최대한 많은 시간을 투자하고,
[02:45] 반대되는 증거를 볼 때까지
[02:48] 우리는 그렇게 할 겁니다. 그래서
[02:51] 그건 아시다시피, 저희 Chy에서 가지고 있는 거예요.
[02:53] 모두에게 무제한 토큰이 제공됩니다. 그 이유는
[02:55] 우리가 가장 많은 모델을 실행한다는 것
[02:57] 우리가 찾을 수 있는 무거운 것들. 그 이유는
[02:59] 그게 바로 우리가 많은 시간을 할애하는 이유입니다.
[03:01] 우리의 추론에 대한 자원
[03:03] GPU는 물론 교육 및
[03:05] 최적화 능력. 어떻게 되는지 알잖아
[03:21] 텍스트는 단순히 글자의 연속일 뿐입니다.
[03:23] LLM은 예측하는 법을 아주 잘 학습합니다.
[03:25] 다음으로, 그들은 완료할 수 있습니다.
[03:27] 텍스트. 인간의 행동은 매우
[03:29] 비슷하지만, 우리 경우에는 더 그렇습니다.
[03:31] 더욱 중요한 것은, 그들의 행동입니다.
[03:33] 회사들은 비슷합니다. 할 수 있다
[03:35] 회사를 대표하기 위해
[03:36] 일련의 행동들. 회사, 아니요
[03:39] 알아요, 그들은 신용 한도를 개설하죠.
[03:41] 그들은 제품을 출시하고, 변경 사항을 적용합니다.
[03:43] 그들은 신용카드 결제를 받기 시작했습니다.
[03:45] 그들은 대출을 요청합니다. 제 말은 그 뜻입니다.
[03:47] 큰 변화들이지만, 모든 것이 다 그렇습니다.
[03:49] 그 회사가 그렇게 하는 순간, 모두가
[03:52] 아시다시피, 그의 직원들은 매 순간...
[03:54] 모든 것은 ~로 변할 수 있다
[03:56] 일련의 행동들. 그리고 나서, 그것은
[03:59] 무슨 일이냐면, 당신은 다음을 만들 수 있다는 것입니다.
[04:00] 회사의 디지털 트윈, 그리고 나서
[04:02] 그 물건에 대해 뭔가를 시작할 수 있습니다.
[04:04] 진짜 회사가 아니라 쌍둥이 회사인 셈이죠.
[04:06] 오른쪽? 그리고 나서 무슨 일이 일어나는지 보세요. 그래서
[04:08] 귀하에게 개입이 있을 수 있습니다.
[04:10] 반사실적 상황. 이렇게 말할 수 있습니다: "그리고
[04:11] 캠페인을 추가한다면
[04:13] 광고일까요, 아니면 그들이 시작한다면 어떨까요?
[04:15] 배송 속도를 하루 더 빠르게 하거나
[04:16] "만약에…?" 같은 거 있잖아요, 모든 게 다 그렇죠.
[04:18] 모든 것은 우리 상인들을 중심으로 돌아갑니다.
[04:20] 우리가 그들에게 대출을 해준다면 어떻게 될까요?
[04:22] 그런 다음 우리는 순서를 찾았습니다.
[04:24] 그들의 상호작용을 극대화할 수 있는
[04:26] 성장 기회는 어떤가요? 어, 그리고
[04:28] 그럼 우리는 실제로 그렇게 합니다.
[04:30] 생산이죠, 그렇죠? 자, 그럼 가자!
[04:32] 우리는 그들에게 대출을 제공하거나, 아니면 뭐, 그런 식으로요.
[04:35] 저희는 여러분께서 그들에게 보내시기를 권장합니다.
[04:37] 다음과 같은 의사소통 방식: "사람들을 위해 보세요."
[04:39] 당신과 마찬가지로, 가장 중요한 것은...
[04:41] 배송을 더 빠르게 시작하거나
[04:44] 광고 캠페인을 시작하다
[04:46] 트위터." 그러니까, 능력을 갖추는 거죠.
[04:49] 회사와 게임을 하면서 돈을 들이지 않는 것
[04:52] 어떤 것이든, 어떤 사람이든 위험하다는 뜻이죠.
[04:55] 실제 사람들이라는 점은 엄청난 장점입니다.
[04:58] 이제 더 많은 사람들을 도울 수 있기 때문입니다.
[05:00] 사람들이 성공할 수 있도록. 그래서 이것은
[05:04] 이는 분명히 없었을 발전입니다.
[05:06] 발생했고 매우 중대한 영향을 미쳤습니다.
[05:08] 우리의 결과와 삶 속에서 살아가십시오.
[05:10] 재정 균형. 나는 그렇게 생각했다
[05:25] 언어 모델(LLM)은 실제로 그렇지 않습니다.
[05:28] 제가 더 잘 관리하는 데 도움이 될 수 있습니다.
[05:31] 장비. 더할 나위 없이 기뻤습니다...
[05:33] 잘못된. 그리고 얼마 후, 나는
[05:37] 내가 많이 변했다는 걸 깨달았어요.
[05:40] 저는 분석하는 작은 시스템을 만들었습니다.
[05:42] 그는 내게 일어나는 모든 일을 알려주고 알려준다.
[05:45] 선제적으로: "이것은
[05:47] 프로젝트가 예정보다 늦어지기 시작할 것 같습니다.
[05:50] "마감일을 알려주세요." 이를 통해 제가 감지할 수 있습니다.
[05:53] 문제가 발생하기 전에 실제로 해결해야 합니다.
[05:55] 발생 가능한 문제들을 해결하면 모든 것이 가능해집니다.
[05:57] 시스템이 훨씬 더 잘 작동하기 시작합니다.
[05:59] 더 나은. 기술적인 측면은 아직
[06:02] 더욱 중요한 것은 LLM이
[06:04] 간단한 최신 소식을 알려드리겠습니다.
[06:06] 하지만 아시다시피, 그 모델은 아주 훌륭합니다.
[06:08] 신호를 포착하고 상대를 만족시키려 노력하는 것,
[06:10] 그러니 당신이 무엇을 묻든,
[06:12] 해답은 종종 질문 안에 있다.
[06:14] 그러면 그것은 간단히 명확하게 설명해 줄 것입니다.
[06:16] 바로 당신이 원하던 거죠, 그렇죠?
[06:19] 그러므로 그것을 간절히 원하는 것이 매우 중요합니다.
[06:21] 정말 필요한 것이지, 억지로 끼워 넣는 것이 아닙니다.
[06:23] 머릿속에 먼저 떠오르는 단어가 무엇이든,
[06:25] 그러면 그 결과는 다음과 같습니다.
[06:27] 상황은 이전보다 훨씬 더 악화될 수도 있다.
[06:30] 왜냐하면 적어도 이전에는 지어지지 않았기 때문입니다.
[06:32] 즉시. 뭔가 있을 것이다
[06:33] 토론을 거쳐 이제는 훨씬 쉬워졌습니다.
[06:35] 그냥 가서 만들어 보세요. 그러므로
[06:37] 따라서 기술적 예리함이 중요해집니다.
[06:39] 가장 중요한 것은 인간적인 요소입니다.
[06:41] 감독 엔지니어들로부터
[06:42] 그들은 언어 모델을 감독합니다.
[06:44] 감독 엔지니어들
[06:45] 타이핑, 아시잖아요, 누르는 거요.
[06:47] 버튼. 제가 드릴 수 있는 가장 중요한 조언은 다음과 같습니다.
[07:05] 토큰 수를 제한하지 않도록 하세요. 언제나
[07:09] 회로 차단기가 필요한 이유는 항상
[07:11] 갑자기 폭주하는 프로세스들이 있습니다.
[07:12] 그들은 토큰을 태우기 시작하고
[07:14] 나쁜 일들. 하지만 그렇게 보이지 않을 수도 있습니다.
[07:17] 둘 사이에는 큰 차이가 있습니다.
[07:19] 대형 모델과 소형 모델
[07:21] . 엄청난 차이가 있습니다. 그리고 아닙니다
[07:23] 당신은 반사실적 상황을 알고 있으니, 아니요.
[07:26] 어떤 게 좋은 건지 알게 될 거예요. 그래서
[07:30] 이 전략을 항상 사용하세요
[07:32] 막대 이분법은 어떤 경우에도 적용됩니다.
[07:34] 코딩, 어떤 경우든
[07:35] 개발, 테스트 및 연구
[07:37] 자동화됨. 예산을 사용하여
[07:41] 가능한 가장 큰 모델. 가정합니다
[07:43] 모든 것에 드는 비용
[07:45] 생산. 미세 조정 기능을 사용하세요. 사용하세요
[07:47] 해당 제작에 적합한 모델입니다.
[07:49] 가능한 한 많은 것을 다음과 같은 방식으로 조사하십시오.
[07:51] 자동화하여 두 가지 모두 균형을 맞출 수 있습니다.
[07:53] 비용, 성능 및 품질.
[07:56] 또한 생산 비용을 절감하려면 다음을 사용하십시오.
[07:59] 더 저렴한 모델은 종종
[08:01] 조정 후, 그 돈을 투자하세요.
[08:04] 개발.

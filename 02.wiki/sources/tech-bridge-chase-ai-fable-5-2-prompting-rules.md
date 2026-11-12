---
title: "Tech Bridge — [한글자막] Anthropic이 바꾼 Fable 5.2 프롬프트 규칙 10가지 (Chase AI): 추론 강도는 high부터 · 결과를 증명하게 · 끝까지 하라고 · 옛 프롬프트 정리 · 생각하지 말라는 안 통한다 · 추론 과정을 캐묻지 마라 · 코드의 주인 · 서브에이전트는 알아서 · 중간 보고 · 말투와 길이는 프롬프트로"
type: source
tags: [chase-ai, fable-5-2, anthropic, prompt-engineering, reasoning-effort, claude-md, subagents, distillation, hallucination, system-card, claude-code, korean-subtitles, video]
source-url: https://www.youtube.com/watch?v=UZflKPqs514
source-type: video
author: Tech Bridge (한글자막 재게시) · 원본 제작 Chase AI의 Chase(설명란 근거 — 발화에 이름 없음) · 근거 자료는 화자가 인용한 Anthropic 공식 프롬프트 가이드 · Fable 5.2 시스템 카드(위키 미열람)
date-published: 2026-11-11
ingested: 2026-11-12
created: 2026-11-12
updated: 2026-11-12
---

# Tech Bridge — Anthropic이 바꾼 Fable 5.2 프롬프트 규칙 10가지 (Chase AI)

[[tech-bridge|Tech Bridge]]가 **한국어 자막을 붙여 다시 올린 10:22 영상, 공식 챕터 13.** 원본은 [[chase-ai|Chase AI]] 채널의 Chase가 만든 1인 해설이다(설명란 *"원본 제작: Chase AI (영상 화면 좌측 상단 Source 표기)"*). 화자는 [[fable-5-2|Claude Fable 5.2]]용 Anthropic 공식 프롬프트 가이드와 시스템 카드를 근거로 **이전 모델에서 통하던 프롬프트 습관 중 바뀐 열 가지**를 정리한다. **영어 원본 오디오만 있는 구성**이고 인용은 전부 en-orig다. raw: `01.raw/articles/2026-11-11_Anthropic이 바꾼 Fable 5.2 프롬프트 규칙 10가지.md`.

테제:

> *"you're prompting Fable 5.2 wrong. Anthropic has changed the rules."*(00:23~00:26)

> ⚠️ **실무자 한 사람이 공식 문서를 해석한 것이다.** 수치(45.3% · $6.72 · $12.82 · 2% · 6배 · 절반 · 20%)는 화자가 시스템 카드 · 벤치마크 표를 읽어 준 것이고, 위키는 프롬프트 가이드(`platform.claude.com/docs`)와 시스템 카드를 열지 않았다. 화면의 예시 프롬프트(*"a prompt that looks something like this"*)는 캡션에 없다 — 영상을 보지 않아 문구를 모른다.
>
> **트랙과 인용.** 오디오는 `English (US) original (default)` 하나에 7개 언어 더빙이다. 수동 자막이 없고 `ko`는 `lang=en&tlang=ko` 기계 번역이다(*Favor 5.2* · *인간 활동은 변화를 가져왔습니다* 등). en-orig는 00:00 *And* 한 단어 뒤 **00:23까지 비어 있다**(챕터 *소개*, 내용 미상). ASR은 *Claude Code*를 *cloud code*로, *CLAUDE.md*를 *claw.md*로, Anthropic을 *Enthropic*으로, Fable을 *Babel*로 적는다. 판독 목록은 raw 헤더에 있다.

## 1. 추론 강도는 high부터 (00:40~02:33)

- *"You should be using Fable 5.2 on a high effort setting. Now this is what it defaults to in the API but in cloud code you will see it defaulting to medium."*(00:42~00:50)[=Claude Code]
- 근거 — Frontier Code 2.0(에이전트 코딩 벤치마크): high **45.3% · $6.72**, Opus 5.5 max **$12.82**와 거의 같은 점수, extra high보다는 높다(01:11~01:37). medium은 **37.6% · $2.48**(01:50~01:56, ASR *$248*). → *"we're getting Opus 5.5 max performance at half the cost."*(01:39~01:42)
- ⭐ 논리: *"what's the point of using Fable 5.2 on medium or low? I could probably get this done with Opus."*(02:09~02:13) Fable을 쓰는 이유가 Opus 5.5 범위 밖의 어렵고 긴 일이라면 high에서 시작하고, 모자라면 extra high, max는 대체로 피한다 — *"you just are paying a ton of money for sometimes a performance level that is below even extra high."*(02:27~02:32) → [[reasoning-effort-levels]](신규) · [[claude-opus-5-5]]

## 2. 결과를 증명하게 하라 (02:33~03:29)

- *"This model, more so than Fable 5.1 or Opus 5.5, will state inference as facts and will just make claims that the code doesn't necessarily support."*(02:35~02:46) medium 이하에서는 테스트도 덜 돌린다.
- 시스템 카드(화자 전달): 필요한 파일이 없을 때 **2%** 는 없다고 말하지 않고 가짜 파일을 만들어 넣었고, 그런 상황에서 지름길을 **6배** 더 자주 탔다(02:58~03:14).
- 처방: 보여 주기 전에 결과물에 테스트를 돌려 *완료했다는 말이 참인지* 확인하라고 프롬프트에 쓴다(03:16~03:26). → [[agent-verification-skill]]

## 3. 끝까지 하라고 말하라 (03:29~04:05)

- 긴 에이전트 작업에서 5.1보다 *결승선 전에* 멈추는 일이 잦다. low · medium에서 두드러지고 high · extra high에서도 남는다(03:36~03:55).
- 시스템 카드의 프롬프트(화면, 캡션에 없음)를 쓰면 *"it stops working about half as often."*(04:03)

## 4. 옛 프롬프트를 정리하라 — "가장 중요한" 규칙 (04:05~05:20)

- *"You need to go back and take a hard look at your current claw.md files and your instructions because chances are they are not built for Fable 5.2."*(04:09~04:19)[=CLAUDE.md] Boris의 *"Delete all your claw.md files or even delete your skills."*(04:24~04:26)를 같은 맥락으로 든다(성은 발화되지 않음, [[boris-cherny]]로 추정 — 위키의 읽기).
- ⭐ 이유: *"Fable 5.2 very diligently follows whatever rules you give it almost to a T."*(04:42~04:48) 그래서 필요 없는 옛 지시는 출력을 깎는다. 지울 것: 꼭 필요하지 않은 엄격한 지침, 스타일에 대한 엄격한 규칙 — *"If you have rules or instructions that are overly prescriptive, you're just going to ruin their outputs."*(05:14~05:19) → [[prompt-debt]] · [[harness-pruning]]

## 5. "생각하지 마"는 안 통한다 (05:20~05:56)

- Fable 5.1은 *"Hey, just give me an answer. Don't deliberate."*(05:31~05:32) 같은 지시로 생각을 건너뛰었다. 5.2는 아니다 — *"It is always going to think. Now, how much it's going to think is going to be a function of your effort level."*(05:41~05:45) 비용을 줄이려면 프롬프트가 아니라 강도(low · medium)를 내린다. → [[reasoning-effort-levels]]

## 6. 추론 과정을 캐묻지 마라 — 증류 분류기 (05:56~06:43)

- *"It actually has a classifier working under the hood and it's going to grab that and assume you're trying to do some sort of distillation."*(06:07~06:12) 답의 논리를 짧게 묻는 것은 되지만, 단계별 추론 전부를 설명하라고 하면 *증류 공격* 으로 판정해 막을 수 있다(06:14~06:26). 화자도 선이 *murky* 하다고 인정한다(06:31~06:42). → [[transcript-classifier]](다른 층의 분류기, 위키의 연결)

## 7. 코드의 주인을 알려 줘라 (06:43~07:46)

- 코드베이스를 *소유한다* 고 말하지 않으면 중복 코드가 많고, 말하면 중복은 줄지만 기능 · 테스트를 더 붙이고 출력 토큰이 늘어난다 — *"you're going to get more output tokens spent for a better, leaner, more optimized result."*(07:19~07:24) 시스템 카드가 이 차이를 자세히 다룬다고 한다(07:37~07:39).
- 반대로 최소 변경을 원하면 주인이라고 말하지 말고 원하는 일을 구체적으로 적는다(07:39~07:46).

## 8. 서브에이전트는 알아서 쓰게 (07:46~08:40)

- 규칙 4의 연장: 서브에이전트 위임 규칙을 지운다. *"Fable 5.2 is smart enough to start spawning sub aents when it needs to."*(08:03~08:09) extra high · max에서는 자기 작업을 검사하는 서브에이전트를 스스로 띄운다 — *"Almost like a miniature version of Ultra Code."*(08:16~08:19) → [[ultracode]]
- 위임 규칙이 있으면 그대로 따르느라 *"you are going to rip through your usage"*(08:26~08:28).

## 9. 긴 작업엔 중간 보고를 (08:40~09:27)

- 도구 호출이 많은 긴 작업에서 조용해질 수 있다(*40분 동안 업데이트 0*). 원하면 프롬프트로 요청한다. 단 매 도구 호출 뒤 말하게 하면 *"that could increase token usage by 20%"*(09:09~09:11) — 중간 지점이 있다.

## 10. 말투와 길이는 프롬프트로 (09:27~10:02)

- *"This is not something that can be affected by the effort level."*(09:32~09:36) low든 max든 말투 · 길이는 같다. 바꾸려면 프롬프트나 CLAUDE.md · AGENTS.md에 적는다. → [[reasoning-effort-levels]]

## 정리 (10:02~10:22)

- *"Extremely powerful"* 하고 사용량 초기화를 여러 번 줬지만 *"we're still kind of stuck with only 50% of the usage"*(10:14~10:16) — 무엇의 50%인지는 말하지 않는다(챕터 *강력하지만 사용량은 50%*).

## 위키의 읽기

- **[[prompt-debt]]의 두 번째 소스, 같은 결론 · 다른 근거.** 11-09의 Lance Martin 편은 *옛 지시가 비용을 올린다* 를 Anthropic 실험 수치로 보였다. 이 소스는 **이유를 모델 성질로** 댄다 — 5.2가 규칙을 *거의 글자 그대로* 따르기 때문이다. 둘 다 *지우라* 이고, 둘 다 벤더 문서의 2차 전달이다.
- **강도(effort)가 하는 일과 안 하는 일이 갈린다.** 이 영상에서 강도는 *생각의 양 · 비용 · 완주율 · 서브에이전트 자발성* 을 바꾸고, *말투 · 길이 · 생각 여부* 는 바꾸지 않는다. 앞 셋은 강도로, 뒤 둘은 프롬프트로 다룬다는 분업이 이 소스의 쓸모다 → [[reasoning-effort-levels]](신규).
- **반대 방향의 두 처방이 공존한다.** 규칙 4 · 8은 *지시를 줄여라*, 규칙 2 · 3 · 7 · 9는 *특정 지시를 더하라* 다. 모순은 아니다 — 지우는 것은 옛 모델의 약점을 메우던 일반 지시이고, 더하는 것은 5.2의 새 약점(추론을 사실로 말함 · 조기 종료 · 중복 코드 · 침묵)에 대한 것이다. 다음 모델에서는 이 더한 것들이 다시 부채가 될 수 있다(위키의 추론).
- **[[fable-5-2]] 발표문 해설과 맞물리는 곳.** 11-10 편의 *"하이 설정으로도 오퍼스의 최고 점수와 비슷했고 … 비용은 절반"* 과 이 영상의 Frontier Code 2.0 수치가 같은 방향이다. 벤치마크 이름 · 점수는 두 소스가 다르게 적는다(11-10 편 Frontier Code 49.1 vs 이 영상 45.3% at high) — 표가 다른 것인지 확인하지 않았다.

## 등장 개체

- 인물 · 조직: [[chase-ai]](신규) · Boris([[boris-cherny]] 추정) · [[anthropic]] · [[tech-bridge]]
- 모델 · 제품: [[fable-5-2]] · [[fable-5-1]] · [[claude-opus-5-5]] · [[claude-code]] · [[ultracode]]
- 개념: [[reasoning-effort-levels]](신규) · [[prompt-debt]] · [[harness-pruning]] · [[agent-verification-skill]] · [[transcript-classifier]]
- 페이지화하지 않음: Frontier Code 2.0(벤치마크 이름) · 증류 분류기(이 소스뿐)

## References

- 영상: https://www.youtube.com/watch?v=UZflKPqs514
- raw: `01.raw/articles/2026-11-11_Anthropic이 바꾼 Fable 5.2 프롬프트 규칙 10가지.md`
- 설명란 관련 자료(위키 미열람): https://platform.claude.com/docs

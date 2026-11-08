---
title: "Tech Bridge — [한글자막] 세계 최고 AI 엔지니어 카파시가 실제로 AI를 쓰는 법 (Nick Saraev): 코드 안 보기 · ASD-STE100 · 짧은 프롬프트 · 그림 요청 · 벤치마크 불신 · HackerTube · Sonnet 위임 · 앱 대신 데이터"
type: source
tags: [andrej-karpathy, nick-saraev, claude-code, claude-opus-5-5, effort-level, ai-usage-habits, prompting, simplified-technical-english, benchmarks, personal-evals, hackertube, subagents, model-delegation, data-over-apps, politeness, secondhand, video]
source-url: https://www.youtube.com/watch?v=lcp0_GnT54o
source-type: video
author: Tech Bridge (번역 재배포, 내레이션 없음) · 원 제작자 [[nick-saraev|Nick Saraev]](설명란 · tags 근거 — 발화에 이름 없음) · 대상 [[andrej-karpathy|Andrej Karpathy]](공개 글 · 댓글의 2차 정리) · 원본 링크 · 녹화일 미상
date-published: 2026-11-07
ingested: 2026-11-08
created: 2026-11-08
updated: 2026-11-08
---

# Tech Bridge — 세계 최고 AI 엔지니어 카파시가 실제로 AI를 쓰는 법 (Nick Saraev)

[[tech-bridge|Tech Bridge]]가 번역해 올린 **5:33 해설, 공식 챕터 11, 내레이션 없음.** [[nick-saraev|Nick Saraev]](설명란 · tags 근거)가 [[andrej-karpathy|Andrej Karpathy]]의 공개 글 · 댓글에서 *"지난 2주 동안"* 본 AI 사용 습관을 정리한다. **Karpathy 본인의 발화는 없다.** 영어 원본 오디오만 있어 인용은 en-orig로 한다. 첫 챕터(00:00~00:24)는 무캡션이다. raw: `01.raw/articles/2026-11-07_세계 최고 AI 엔지니어 카파시가 실제로 AI를 쓰는 법.md`.

테제(화자의 해석):

> *"most specific implementations are just sort of wrappers around a core truth, which is the data."*(04:47~04:53)

> ⚠️ **2차 전달 + 화자의 해석.** 습관은 Saraev가 모은 것이고 위키는 Karpathy의 원 글을 하나도 열지 않았다. 화자 스스로 *"I believe"* · *"presumably"* 라 단서를 단다. 설명란도 *"원본 제작자 닉 사라예프가 공개 글·댓글을 바탕으로 정리한 내용"* 이라 적는다.
>
> ⚠️ *"now he works at Anthropic"*(00:36) **은 화자 진술이다.** 설명란 · 위키 [[andrej-karpathy]] 페이지 어디에도 없다. 확인하지 않았다.

## 1. 카파시는 AI를 어떻게 쓸까 (00:24~00:47)

- 소개: *"He co-founded OpenAI, then ran AI at Tesla, then invented the term vibe coding"*(00:31~00:36) — 이어서 위의 Anthropic 진술.
- 출처: *"here is exactly what I've heard him doing over the course of the last 2 weeks."*(00:43~00:46)

## 2. 기본 설정과 코드 안 보기 원칙 (00:47~01:09)

- ⭐ 설정: *"he uses Claude Code, the Mac desktop app, with Opus 5.5 exclusively on medium effort as his default. He does not use max effort."*(00:46~00:54)
- ⭐ 규칙: *"he doesn't read the code, he doesn't write it, and he also doesn't run terminal commands. He only talks to Claude"*(01:01~01:05)

→ [[claude-code]] · [[claude-opus-5-5]] · [[read-fluency-for-agent-output]](읽지 않는 쪽의 극단)

## 3. 쉬운 영어와 짧은 프롬프트 (01:09~01:57)

- 설명은 ASD-STE100으로 받는다: *"This is sort of the aircraft repair manual English that drops the vast majority of like unnecessary words. The vocabulary is very, very strict."*(01:13~01:19)
- *"His prompts nowadays are getting really short and really dumb."*(01:19~01:22) 이유(화자 전달): *"adding requirements into the prompt can often make the model do worse work"*(01:24~01:26) — 요청끼리 서로 반대인 경우가 많아서.
- 예: 보안 강화는 *"Check recent cyber stuff,"*(01:40) 한 줄, 배포는 서버 IP와 *"update, deploy, secure, harden, and optimize,"*(01:53~01:54) 다섯 낱말.

→ [[goal-level-delegation]]

## 4. 긴 설명보다 그림 한 장 (01:57~02:20)

- *"Andre will ask for a diagram or maybe HTML pages or even like custom explainer videos if he doesn't understand something."*(02:03~02:10)
- 논리: *"why read a thousand words if Opus 5.5 or an equivalent model can make the picture in less time"*(02:12~02:17)

→ [[model-rendered-interface]]

## 5. 공개 벤치마크를 믿지 않는 이유 (02:20~02:51)

- *"He also really doesn't trust public benchmarks."*(02:19~02:21) 며칠 전 Hacker News 댓글에서 대신 Epoch's ECI를 가리켰다고 전한다 — 화자 설명은 *"basically a benchmark of benchmarks"*(02:31).
- 해석(화자): *"presumably he believes models are intelligent based off how they interact and communicate with them"*(02:43~02:48)

## 6. 카파시의 독특한 모델 실험 (02:51~03:27)

- *"he asked a model a simple question, 'Land or water?' And then gave it a coordinate, latitude and longitude."*(02:55~02:59) 답을 흑백으로 칠해 세계 지도를 만들었다.
- 목적(화자 전달): *"most of the world's knowledge is now compressed in the neurons of these models like Opus 5.5."*(03:13~03:17)

→ [[cost-vs-score-frontier]](같은 화자의 벤치마크 읽기와 대조)

## 7. 거슬리면 직접 만든다 — HackerTube (03:27~03:54)

- *"Uncle Andre will build fixes the moment something annoys him."*(03:25~03:29) YouTube 썸네일을 보고 *"Boy, what slop."*(03:35~03:37) → [[hackertube|HackerTube]](신규).
- 화자의 설명: *"basically just scraped the best news from Hacker News."*(03:41~03:43) 뒤(05:10~05:15)의 프롬프트는 *"restricted to videos that have been repeatedly recommended on Hacker News over the years"*(05:12~05:15) 라 해서, 대상은 **HN에서 반복 추천된 영상**이다.
- ⚠️ *"Nick Szabo thumbnails"*(03:34~03:35) 판독 보류(raw 헤더).

## 8. 싼 필터 뒤 Sonnet 서브에이전트 (03:54~04:23)

- 데이터 작업: Claude로 URL · regex · spam을 거르는 필터를 만들고, 남은 것을 *"sends it to Sonnet primarily using Claude code workflows"*(04:04~04:08) — *"orchestrated by a cheaper model"*(04:12).
- ⭐ 구조: *"Opus 5.5 maybe on medium effort delegating to a bunch of Sonnet subagents."*(04:18~04:22)
- ⚠️ 무엇이 *cheaper model*인지 화자 문장이 엇갈린다(Sonnet이 실행 · Opus가 지휘라고 읽히는 뒷문장과 앞문장의 *orchestrated by a cheaper model*). 정하지 않는다. Sonnet 버전 미발화.

→ [[model-mixing-economics]] · [[agent-skills]]

## 9. 앱 대신 데이터를 공유한다 (04:23~05:00)

- *"he doesn't actually share the app. What he does is he'll just share the data source, and then the prompt."*(04:31~04:36) 받는 사람이 *"customize your own now with Claude"*(04:38~04:39).
- 화자의 해석 → 위 테제. *"if you have a model that is capable of whipping up any interface or any app around the data, well, it's basically the same thing if not better."*(04:53~04:59)

→ [[share-data-and-prompt-not-app]](신규) · [[disposable-vs-durable-software]] · [[model-rendered-interface]]

## 10. Claude에게도 예의 바르게 (05:00~05:33)

- HackerTube 프롬프트: *"Hi Claude, good morning. How are you? I'm great, thanks. Build me a YouTube-style site, but restricted to videos that have been repeatedly recommended on Hacker News over the years. Please don't make any mistakes."*(05:05~05:17)
- 화자: *"I don't know how empirical the don't make any mistakes sign is"*(05:17~05:21) — 효과는 모른다고 스스로 말한다.

## 등장 개체

- 인물: [[andrej-karpathy]] · [[nick-saraev]](화자, 설명란 · tags 근거) · *Nick Szabo*(판독 보류, 페이지 없음)
- 제품 · 모델: [[claude-code]](Mac 데스크톱 앱) · [[claude-opus-5-5]] · Sonnet(버전 미발화, 페이지 연결 안 함) · [[hackertube]](신규) · Hacker News · Epoch ECI · ASD-STE100(언급 수준 — 페이지 없음)
- 조직: [[openai]] · [[anthropic]](소속 진술, 미확인) · Tesla(경력 언급)
- 개념: [[share-data-and-prompt-not-app]](신규) · [[model-rendered-interface]] · [[model-mixing-economics]]

## 이 위키에서의 좌표

- [[andrej-karpathy]]의 앞선 소스는 강의 · gist · 이름 붙은 규칙의 재유통이었다. 이 편은 **현재의 일상 사용법**을 다룬 첫 소스이고, 그것도 **제3자가 모은 2차 정리**다.
- [[nick-saraev]]의 여섯 번째 등장. 앞선 편들(Opus 5.5 비교 · Claude Code 입문)에서 *auto 모드 · 결과를 설명하라*고 권하던 화자가, 여기서는 그 극단(코드를 아예 보지 않음)을 다른 사람의 습관으로 전한다.
- 같은 날 Anthropic · Salesforce 편이 **증거를 요구하라**고 할 때, 이 편은 **코드를 보지 않는다**는 습관을 전한다. 둘은 모순이 아니다 — Karpathy 습관은 개인 프로젝트이고 검증 방식은 발화되지 않는다.

## ⚠️ 유보

- Karpathy 본인의 발화 · 원 글 없음. 2주 관찰의 정리이고 원 글을 대조하지 않았다.
- *"now he works at Anthropic"* 미확인. *Nick Szabo* 판독 보류. Epoch ECI의 정의는 화자 설명뿐이다.
- 첫 챕터 무캡션. ko는 기계 번역이라 인용하지 않았다.

## References

- raw: `01.raw/articles/2026-11-07_세계 최고 AI 엔지니어 카파시가 실제로 AI를 쓰는 법.md`
- https://www.youtube.com/watch?v=lcp0_GnT54o
- 설명란 링크(⚠️ 열어 보지 않았다): https://hackertube.org/ · https://karpathy.bearblog.dev/

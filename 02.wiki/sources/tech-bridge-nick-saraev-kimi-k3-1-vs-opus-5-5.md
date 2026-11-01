---
title: "Tech Bridge — 비싼 AI가 더 잘할까? Kimi K3.1 vs Claude Opus 5.5 (Nick Saraev 추정): 같은 프롬프트 데모 6종, 제작 시간 · 완성도 · 일관성 · 가격"
type: source
tags: [kimi, claude-opus-5-5, model-comparison, coding-agents, claude-code, kimi-code, max-effort, self-verification, taste, agent-swarm, pricing, user-review, video]
source-url: https://www.youtube.com/watch?v=f_8aIpusjg0
source-type: video
author: Tech Bridge (발췌, 내레이션 없음) · 화자 [[nick-saraev]] 추정(설명란 · 태그 근거 — 발화에 이름 없음) · 원본 영상 · 녹화일 미상
date-published: 2026-10-31
ingested: 2026-11-01
created: 2026-11-01
updated: 2026-11-01
---

# Tech Bridge — 비싼 AI가 더 잘할까? Kimi K3.1 vs Claude Opus 5.5 (Nick Saraev 추정)

[[tech-bridge|Tech Bridge]]의 **10:12 발췌, 공식 챕터 11, 내레이션 없음.** 오디오는 `English (US) original (default)` + 더빙(es · fr · id · it)이고 **한국어 트랙 · `ko-orig`가 없다** — 10-27 Voss 편 이후 이어지는 **영어 원본 오디오만** 있는 구성이라 **인용은 en-orig로만** 한다. 00:00~00:22(첫 챕터)는 무캡션이고, en-orig는 *"Whereas I now want to dive…"* 로 **문장 중간에서 시작**한다. raw: `01.raw/articles/2026-10-31_비싼 AI가 더 잘할까 Kimi K3.1 vs Claude Opus 5.5.md`.

한 제작자가 **같은 프롬프트 · 같은 도구 · 각자의 하네스(max effort)** 로 [[kimi|Kimi K3.1 Pro]]([[kimi|Kimi Code]])와 [[claude-opus-5-5|Claude Opus 5.5]]([[claude-code|Claude Code]])에게 데모를 만들게 하고 화면에서 하나씩 열어 본다. 테제(화자 결론):

> **Opus 5.5는 시각적 완성도에서 대체로 앞서지만 더 오래 걸리고 두 번 작동하지 않는 결과를 냈다. Kimi K3.1 Pro는 품질은 낮아도 더 일관적이고 값은 절반이다 — 그렇다면 두 배 가격이 두 배 품질인가?**

> *"Kimmy[=Kimi] K3.1 Pro was not as good at many things as Opus 5.5, although it does seem like it was more consistent despite its lower quality."*(09:33~09:42) · *"Opus 5.5 is double the cost. And so, the question is is it double the quality?"*(09:48~09:54)

> ⚠️ **화자 신원은 설명란 · 태그 근거다.** 발화에 이름이 없다. 설명란 *"개발 유튜버 닉 사라예프가 같은 과제로 만든"* 과 info.json `tags`의 `Nick Saraev`가 근거다. 발화로 확인되는 것은 **실험을 직접 설계한 1인칭 제작자**라는 점 — 예전에 만든 게임이 *"kind of gone quasi viral"*(07:57~08:01), 구독 플랜으로 실행(10:05~10:10). → [[nick-saraev]] **추정**(위키의 이전 두 편과 같은 근거 수준).
>
> ⚠️ **한 제작자의 주관적 비교.** 프롬프트 원문 · 채점 기준 · 반복 횟수가 없다. *"I have yet to score either of these"*(00:46~00:51)라 했지만 점수는 끝까지 나오지 않는다. 가격 · 시간은 화자 진술이다(설명란도 *"원본 실험의 조건을 기준으로"* 라고 단다).
>
> ⚠️ **8개 중 6개만 나온다.** 화자는 *"this (…) list of eight demos"*(07:14~07:19)라 하는데 영상에는 여섯 데모만 있다. 평균 제작 시간도 그 표본 위의 값이다.

## 1. 소개 · 비싼 AI가 꼭 더 잘할까? (00:00~00:22)

en-orig에 발화가 없다(무캡션). 이 챕터의 내용은 쓰지 않는다. en-orig 첫 문장의 *"Whereas"* 로 보아 앞에 다른 맥락(벤치마크 등, 미확인)이 있었던 원본에서 잘라 온 것이다.

## 2. 같은 과제, 다른 제작 시간 (00:22~01:15)

- 실험 규칙: *"My rules for these comparisons were to feed them the exact same prompt. They had the exact same tools and they had their own individual coding harnesses at max effort. So, Kimmy[=Kimi] K 3.1 had Kimmy[=Kimi] code, Claude Opus 5.5 had Claude code."*(00:32~00:46)
- 녹화 중에 빌드가 돈다: *"They're actually both running in the background right now."*(00:50~00:53)
- ⭐ 제작 시간: *"on average Kimmy[=Kimi] K 3.1 Pro took 29 minutes and 41 seconds to build, whereas Opus 5.5 took 47 minutes and 2 seconds."*(00:57~01:06) — 그리고 바로 *"Obviously, time to build was different from quality"*(01:11~01:13).

> ⚠️ **하네스가 다르다.** 모델만이 아니라 Kimi Code vs Claude Code가 함께 비교된다. 결과 차이를 모델로만 돌릴 수 없다 — 화자는 이를 구분하지 않는다. 이 위키의 [[model-harness-knowledge-stack]] 관점에서 이 실험은 **모델 + 하네스 쌍**의 비교다.

→ [[inference-speed-as-capability]](속도 축과 품질 축은 따로 움직인다)

## 3. 3D 키보드 · 작동과 완성도 (01:15~03:14)

- Kimi: 기계식 키보드 시뮬레이션 *"Loom"*. 색 · 스위치 변경, 실제 타이핑, 분해(explode), 장바구니까지 — *"This is very high quality and very sexy. Far more advanced than I initially gave it credit for"*(01:56~02:02).
- ⭐ Opus 첫 결과: *"I'm not joking here when I say it's not loading. So, clearly it's screwed up the build in some way, shape, or form. So, by taking far longer, it hasn't even verified that it works."*(02:06~02:15) → 화자가 **수정 요청 메시지**를 보낸다(02:15~02:18). 그 시점 판정: *"Kim E[=Kimi] is definitely whooping Opus's ass right now."*(02:18~02:21)
- 수정 후 Opus: *"there is greater visual fidelity"*(02:25~02:29), 키 해상도 · 매트 품질이 높고, 색 변경 등 기능은 *"virtually the same thing"*(02:35~02:36).
- 나란히 놓고: *"it's not super different"*(03:01) · *"the Opus 5.5 ones just look a little bit more realistic"*(03:01~03:05) · *"for Kim E[=Kimi] K3.1 Pro being a fraction of the cost, not bad."*(03:10~03:14)

→ [[agent-verification-skill]](더 오래 돌고도 작동 확인을 안 했다)

## 4. 은하 충돌 · 품질일까, 취향일까 (03:14~04:30)

- Kimi: 두 은하의 충돌, *"a full-scale simulation with over 200,000 stars"*(03:25~03:30, ⚠️ 화자 진술 — 입자 수는 세지 않았다고 스스로 말한다 04:10~04:12).
- Opus: 시각적 완성도가 다르고, 비교하면 Kimi 쪽이 *"almost looked kind of kiddish"*(03:57~03:58).
- ⭐ 그러나 화자 스스로 유보: *"I think this is more of a reflection of just taste that it is necessarily design quality."*(04:03~04:10) · *"most of the functionality and and so on is virtually the exact same."*(04:14~04:16) · *"It's really just the background color."*(04:29~04:30)

→ [[taste-vs-judgment]](평가자의 취향과 설계 품질을 화자가 구분하려 한다)

## 5. 랜딩 페이지 · 화려함과 속도 (04:30~05:29)

- 조건: *"I want this to be 100% SVGs and HTML."*(04:48~04:53) — 이미지 생성기 같은 외부 자원 금지.
- Kimi: 심해 다이버 *"Abyssal"* 의 스크롤 구동 페이지, *"not being super visually impressive"*(04:41~04:42).
- Opus: *"Opus went a little bit further. They actually have like live sharks swimming"*(05:05~05:08), 3D 효과. 대가: *"the page is a lot slower. Presumably, it wasn't super optimized with those resources."*(05:17~05:22) — 그래도 *"a lot funner to kind of scroll through"*(05:24~05:26).

## 6. 건물 철거 · 디테일의 차이 (05:29~06:20)

- Kimi: *"Kestrel Tower"* — 건물은 잘 만들었지만 *"the city around it looks kind of bare"*(05:36~05:38). 아래층부터 폭파, 유리 낙하, *"video instant replay"*(05:52~05:55).
- Opus: *"the building is definitely within a city. That's one thing Kimiko[=Kimi] 3.1 did not do."*(05:56~06:03). 단점: *"some really annoying ass sounds"*(06:09~06:12). 장점: *"from an animation perspective, far higher quality, although the plumes of smoke to me seem kind of silly."*(06:15~06:20)

## 7. 마인크래프트 · 예뻐도 안 움직인다 (06:20~07:26)

- Kimi: *"this is beautifully done. I honestly don't think there's much else that I'd suggest."*(06:24~06:28) — 셰이딩, 달리기, 물속 흐림.
- ⭐ Opus *"Beyond the Veil"*: *"My character is incapable of moving forward. And so, despite this looking very visually appealing, yeah, I think Opus 5.5 might have screwed the pooch up a little bit without that testing."*(06:59~07:09)
- ⭐ 집계와 원인 추정: *"Looks like Opus 5.5 uh so screwed up twice on this uh list of eight demos. I imagine it probably is because it just didn't I don't know, proof its work or something like that at the end, although I did run it on max mode, which is kind of disappointing."*(07:13~07:25)

> ⚠️ **"twice"의 두 번은 영상에서 키보드(로딩 실패)와 마인크래프트(이동 불가)로 보인다.** 원인(*"didn't (…) proof its work"*)은 화자의 추측(*"I imagine"*, *"I don't know"*)이다. Claude Code 쪽 로그 · 검증 단계 여부는 나오지 않는다.

→ [[agent-verification-skill]] · [[claude-opus-5-5]]

## 8. 액션 게임 · 이번에는 평가가 바뀐다 (07:26~08:11)

- 화자가 예전에 만든 게임의 재현.
- Kimi: *"the controls here are pretty horrific"*(07:31~07:33) — *"going up goes down, but going right and left actually go right and left."*(07:38~07:42)
- Opus: *"a lot better, for sure"*(07:46~07:48) · *"10 out of 10 would play this game again."*(08:10)
- *"Might have used like part of the Minecraft build in order to do this"*(08:04~08:07) — 화자 추측.

→ **Kimi도 실패가 있다.** 6개 중 작동 실패 · 심각한 결함은 Opus 2(키보드 첫 빌드 · 마인크래프트), Kimi 1(조작 반전)로 보인다 — ⚠️ 화자가 Kimi 쪽 실패를 집계하지 않아 *"more consistent"* 의 근거는 화자 체감이다.

## 9. 앱 기능 · 짧은 추론 기록 (08:11~08:33)

- Kimi 앱의 *"thinking complete"* 탭에서 추론 기록을 본다(08:12~08:15). *"hello"* 에 대한 기록 예시를 읽는다.
- ⭐ *"there's a difference here in the reasoning traces between reading like, you know, a Claude model or a an Open AI model. And the difference is these guys are writing way shorter."*(08:25~08:34)

> ⚠️ 비교 근거는 인사말 하나의 기록이다. 토큰 수 측정은 없다. [[tech-bridge-agents-vs-humans-optimizer-speedrun]]의 *"Kimi는 쓴 토큰 대비 효율적"* 과 같은 방향이지만 다른 측정 · 다른 버전이다.

## 10. Swarm · 여러 작업을 동시에 (08:33~09:31)

- 앱 기능: 파일 · 이미지 첨부, plugins, skills, 그리고 swarm — *"This is a Kimmy[=Kimi] specific feature. So, if you click on that button, it'll actually task like hundreds of agents to go out and find information for you."*(08:41~08:49)
- 시연: *"put together 10 independent landing pages for fake products"*(08:49~08:53) → *"instead of me just speaking with a single agent, what I'm doing is I'm actually uh delegating to a a swarm. This is just natively supported by Kimmy[=Kimi] out of the box."*(08:54~09:02)
- 모델 선택 표시 *"Kimmy[=Kimi] K3.1 Pro high"*(09:06~09:10), *"just like you can in Claude and then Codex models, you guys can change the effort levels"*(09:10~09:16).
- 스웜이 실행 중에 **질문을 되묻는다**: *"it's decided that it wants to ask me a question. And it can do so using this cool UX panel."*(09:16~09:22)
- ⚠️ *"hundreds of agents"* 는 화자 표현이고, 이 시연에서 실제로 몇 개가 떴는지 · 결과물은 나오지 않는다.

→ [[agent-swarm]] · [[kimi]]

## 11. 가격이 두 배면 품질도 두 배일까 (09:31~10:12)

- ⭐ 결론: *"Kimmy[=Kimi] K3.1 Pro was not as good at many things as Opus 5.5, although it does seem like it was more consistent despite its lower quality."*(09:33~09:42)
- 가격: *"it's $2 per million input tokens and $10 per million output tokens"*(09:42~09:46) · *"Opus 5.5 is double the cost. And so, the question is is it double the quality?"*(09:48~09:54)
- ⭐ 반론도 스스로 단다: *"Obviously, the better you get at quality, the more even a slight percentage improvement makes to the end result."*(09:52~10:00)
- *"I think Kimmy[=Kimi] K3.1 Pro has proven itself to be quite a serious contender and quite capable for knowledge work."*(09:58~10:03)
- 단서: *"I did run these on plans. I didn't run these on API usage, but uh Kimmy[=Kimi] has a very generous plan allowance as well."*(10:05~10:10)

> ⚠️ **가격은 확인하지 않았다.** $2/$10은 화자 진술이고, *"double the cost"* 가 입력 · 출력 어느 단가의 두 배인지, 공식 가격인지 미발화. [[claude-opus-5-5]] 페이지에는 가격 1차 자료가 없다. 그리고 실행은 **플랜**이라 이 데모들의 실제 토큰 비용은 측정되지 않았다 — 가격 비교는 **단가표 비교**이지 *작업당 비용* 비교가 아니다.

→ [[true-cost-to-perfect-answer]] · [[value-maxing]]

## 등장 개체

- 인물: [[nick-saraev]](추정, 세 번째 등장)
- 모델 · 제품: [[kimi]](신규 — Kimi K3.1 Pro · Kimi Code · 앱 swarm) · [[claude-opus-5-5]] · [[claude-code]] · Codex(effort 비교 한 마디, 연결 안 함) · OpenAI(추론 기록 비교 한 마디)
- 개념: [[agent-verification-skill]] · [[taste-vs-judgment]] · [[agent-swarm]] · [[inference-speed-as-capability]] · [[true-cost-to-perfect-answer]] · [[model-harness-knowledge-stack]]

## 이 위키에서의 좌표

- [[claude-opus-5-5]]의 첫 **실사용 결과** 소스다. 그동안 이 페이지는 *"며칠 전 발표"*(진행자) · Brown의 일반론 · Duet 관련 2차 진술뿐이었다.
- [[tech-bridge-gpt-6-1-terra-first-look]](10-29 업로드)의 *빠르고 싸지만 쉽게 포기한다* 와 짝이 된다: 여기서는 **싸고 빠른 쪽이 더 일관적**이고 **비싸고 느린 쪽이 완성도는 높지만 작동 확인을 빠뜨린다** — 속도 · 가격 · 완수가 한 방향으로 움직이지 않는다는 기록이 하나 더 붙는다.
- [[kimchi]] 편의 *"proprietary models for edge case but use open source for the rest"*(벤더 발표)를 **한 사용자의 데모 비교**가 비슷한 결론(*"serious contender"*)으로 받친다 — ⚠️ 이 영상은 Kimi K3.1의 공개 가중치 여부를 말하지 않는다.

## ⚠️ 유보

- 화자 신원은 설명란 · 태그 근거, 원본 영상 · 녹화일 미상, 첫 22초 무캡션 · 앞 맥락 잘림, 8개 중 6개 데모만.
- 프롬프트 · 채점 기준 없음, 반복 1회로 보임, 하네스까지 묶인 비교.
- 가격 · 제작 시간 · 별 개수는 화자 진술. 플랜 실행이라 작업당 비용 없음.
- *"Kimmy"* · *"Kim E"* · *"Kimiko"* → Kimi 판독. ko는 Opus를 "작품"으로, 04:28 · 10:07을 **뜻을 뒤집어** 옮겨 인용하지 않았다.

## References

- raw: `01.raw/articles/2026-10-31_비싼 AI가 더 잘할까 Kimi K3.1 vs Claude Opus 5.5.md`
- https://www.youtube.com/watch?v=f_8aIpusjg0
- 설명란 관련 자료: https://www.kimi.ai/code · https://claude.ai/ (⚠️ 열어 보지 않았다)

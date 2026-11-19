---
title: "앱 대신 데이터와 프롬프트를 공유한다 (Share Data and Prompt, Not the App)"
type: concept
category: pattern
tags: [software-distribution, data-over-apps, prompts, personal-software, model-generated-software, karpathy, disposable-software]
aliases: [share the data not the app, 앱 대신 데이터, 데이터와 프롬프트 공유, data is the core truth, wrappers around the data]
related: [disposable-vs-durable-software, model-rendered-interface, andrej-karpathy, hackertube]
first-seen: tech-bridge-nick-saraev-karpathy-ai-habits
sources: [tech-bridge-nick-saraev-karpathy-ai-habits, tech-bridge-karpathy-hackertube-two-hours-five-words]
created: 2026-11-08
updated: 2026-11-19
---

# 앱 대신 데이터와 프롬프트를 공유한다

**모델이 데이터 위에 어떤 인터페이스든 금방 만들 수 있다면, 남에게 줄 것은 완성된 앱이 아니라 데이터 소스와 프롬프트다.** 받는 사람은 자기 취향대로 다시 만든다. [[tech-bridge-nick-saraev-karpathy-ai-habits]]에서 [[nick-saraev|Nick Saraev]]가 [[andrej-karpathy|Andrej Karpathy]]의 습관으로 전한다.

> *"he doesn't actually share the app. What he does is he'll just share the data source, and then the prompt."*(04:31~04:36)

> 화자의 일반화: *"most specific implementations are just sort of wrappers around a core truth, which is the data."*(04:47~04:53)

> ⚠️ **소스 하나, 2차 전달 + 화자 해석.** 습관은 Saraev가 전한 것이고 Karpathy의 원 글은 위키가 열지 않았다. "데이터가 핵심 진실"이라는 일반화는 Saraev의 말이다.

## 논리

1. 모델이 *"whipping up any interface or any app around the data"*(04:55~04:56) 할 수 있다.
2. 그러면 앱 코드는 **추상화 한 겹**일 뿐이다(화자: *"it's just an abstraction"*).
3. 데이터 + 프롬프트를 받으면 각자 *"your own customized build"* 를 얻는다 — 원작자는 앱을 유지 · 배포하지 않아도 된다.

## 위키 안의 연결

- [[disposable-vs-durable-software]] — 앱이 **일회용** 쪽으로, 데이터가 **오래가는** 쪽으로 갈린다. 이 패턴은 그 경계를 *배포 단위*로 옮긴다.
- [[model-rendered-interface]] — 화면을 모델이 그때그때 만든다는 생각. 같은 소스에서 Karpathy는 이해가 안 되면 다이어그램 · HTML · 설명 영상을 요청한다고 전한다.
- [[hackertube]] — 이 습관이 적용된 예로 전해지는 개인 프로젝트.

## 한계 (위키의 읽기)

- 같은 프롬프트가 같은 앱을 만들지 않는다 — 재현성 · 버그 공유 · 보안 검토가 각자에게 넘어간다.
- 데이터 자체가 공유 가능해야 한다(권한 · 개인정보). 소스는 다루지 않는다.

## References

- [[tech-bridge-nick-saraev-karpathy-ai-habits]] (9절)

## 2026-11-19 — 두 번째 소스: 압축 파일 하나, 3분, 그리고 엿새 뒤의 재현 ([[tech-bridge-karpathy-hackertube-two-hours-five-words]])

한국어 해설이 같은 습관을 [[hackertube|HackerTube]]의 구체적 경위로 전한다(⚠️ 2차 전달, 11-08 편과 독립인지는 미확인).

- 공개하지 않은 것과 그 이유: 서버 코드 — *"바이브 코딩으로 만든 엉망 진창이라서요."*(07:49~07:51) 11-08 편에는 없던 **이유** 다. 앱 코드는 남에게 줄 만한 물건이 아니라는 판단이 먼저 있다.
- 공개한 것: *"대신 댓글을 분석한 데이터를 압축 파일 하나로 올렸습니다."*(07:53~07:55) 이걸 Opus 5.5에 주고 유튜브 같은 사이트를 만들어 달라고 하면 거의 바로 나온다, 3분쯤 걸렸다고.
- ⭐ **본인이 받는 쪽에서 재현했다**: *"다른 개발자가 올린 유튜브 채널 목록을 보고 클로드 코드로 3분만에 영상 47,000개 짜리 트리스탄 튜브를 만들었습니다."*(08:04~08:09) — 데이터를 받아 각자 만든다는 패턴이 반대 방향으로도 한 번 돈 예다.
- 비용의 분포가 논리를 받친다: HackerTube에 든 입력 5억 400만 토큰의 90% 넘게가 댓글 선별이었고 앱 작업은 Opus 5.5 약 100만 토큰이었다. 해설의 결론: *"해커 튜브에서 진짜 귀한 건 20년치 댓글에서 걸러낸 영상 목록입니다. 카파시가 코드 대신 공개한 것도 바로 그 데이터였습니다."*(08:57~09:04)

위 *한계* 에 한 줄을 보탠다 — 이 예에서 공유된 것은 **데이터** 이고, 프롬프트는 농담 반의 한 줄(*안녕 클로드, 좋은 아침이야 …*)이다. *데이터 + 프롬프트* 에서 무게는 거의 전부 데이터 쪽에 있다(위키의 읽기).

---
title: "앱 대신 데이터와 프롬프트를 공유한다 (Share Data and Prompt, Not the App)"
type: concept
category: pattern
tags: [software-distribution, data-over-apps, prompts, personal-software, model-generated-software, karpathy, disposable-software]
aliases: [share the data not the app, 앱 대신 데이터, 데이터와 프롬프트 공유, data is the core truth, wrappers around the data]
related: [disposable-vs-durable-software, model-rendered-interface, andrej-karpathy, hackertube]
first-seen: tech-bridge-nick-saraev-karpathy-ai-habits
sources: [tech-bridge-nick-saraev-karpathy-ai-habits]
created: 2026-11-08
updated: 2026-11-08
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

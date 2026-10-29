---
title: "프롬프트 캐싱 (Prompt Caching) — 정적 접두를 지키고, cache miss를 버그로 다룬다"
type: concept
category: technique
tags: [prompt-caching, context-engineering, cost, latency, harness-design, compaction, kv-cache, agents]
aliases: [prompt caching, prompt cache, 프롬프트 캐시, 캐시 적중, cache hit, cache miss, cache warming, 캐시 예열, KV cache hit ratio]
related: [context-engineering, harness-engineering, context-resets-and-compaction, deferred-tool-context, toolbox-pattern, scripts-that-talk-back, transcript-classifier, automatic-model-routing, model-mixing-economics, trusted-throughput, always-on-agent-architecture, openclaw, fireworks-ai]
first-seen: tech-bridge-lee-robinson-always-on-agents
sources: [tech-bridge-lee-robinson-always-on-agents, tech-bridge-fireworks-train-to-deploy-open-models, tech-bridge-anthropic-fold-subagents-into-skills]
created: 2026-10-18
updated: 2026-10-29
---

# 프롬프트 캐싱 (Prompt Caching)

**에이전트는 턴마다 대화 전체를 다시 보낸다. 앞부분(도구 정의·시스템 프롬프트·이전 대화)이 그대로면 공급자가 캐시된 토큰으로 싸게 처리한다. 그래서 하네스 설계는 그 접두를 바꾸지 않는 쪽으로 기운다. 도구를 턴 중에 더하거나 빼지 않고, 프롬프트 조각의 순서를 고정하고, 바뀌는 것은 맨 뒤에 둔다.** 이 위키의 여러 페이지가 이 제약을 스쳐 갔다. 정면으로 다룬 첫 소스는 [[lee-robinson|Lee Robinson]]의 [[tech-bridge-lee-robinson-always-on-agents]]다.

> *"most of the tokens used are actually ideally cached tokens because you're sending it a conversation and then (…) you're basically rescending[=resending] the entire conversation over again."* (27:56~28:08) · *"if there's a cash cache miss, it's kind of like a bug in the system really."* (29:51~29:55)

## 기법 (Robinson, GrokBot 하네스 — ⚠️ 당사자 진술, 수치 없음)

| 기법 | 발화 |
|---|---|
| **정적 접두** | *"try to keep the tool definitions, the system prompts, all of this information as static as possible between different calls so that you don't break the cache"*(28:19~28:29). 그러면 새 메시지만이 캐시되지 않은 delta다(28:33~28:42) |
| **턴 중 도구 고정** | *"ideally you don't add or remove new tools during turns"*(25:23~25:28). 긴 도구 설명·스키마는 줄인다(25:30~25:45) |
| **섹션 해시 · 고정 순서** | A/B 테스트로 새 조각을 넣어도 *"you can almost hash each section and always keep a fixed order (…) Otherwise, you just busted the cache."*(30:48~31:01) |
| **cache warming** | *"when you open the chat and you start typing, um the server can actually go and prepare the prompt early, uh, to basically warm the cache"*(31:06~31:13). 링크 hover 때 prefetch와 같은 비유 |
| **캐시가 따뜻할 때 compaction** | 캐시 창(*"Maybe it's 10 minutes, maybe it's 60 minutes"* 32:17~32:19) 안에서 긴 대화를 미리 요약해 두면 돌아온 사용자는 더 싼 요약 위에서 이어 간다(32:11~32:43). → [[context-resets-and-compaction]] |

함께 쓰는 것: 긴 출력은 파일로, 스크린샷 같은 비싼 일은 서브에이전트로 보내 main agent의 컨텍스트를 작게 유지한다(29:05~29:33).

## 운영 사건 — OpenClaw와 구독 플랜 (⚠️ 화자 진술)

*"all the way back to January of this year, uh, when OpenClaw was really getting popular and people were using it, uh, inside of subscription plans for, uh, model providers, this was a very new usage pattern that model providers hadn't really seen and the the harness hadn't really yet been optimized for this type of workflow. So, there was a lot of cache misses."*(29:59~30:22) 상시 도는 에이전트에서 캐시 미스는 곧바로 비용이 된다. → [[openclaw]]

> ⚠️ [[tech-bridge-stigg-ai-companies-building-banks|Stigg 편]]은 같은 시기 OpenClaw의 구독 사용을 **보조금**과 접근 차단으로 설명했다. 두 설명은 배타적이지 않지만 어느 쪽도 공급자·수치를 함께 대지 않는다.

## 위키의 다른 페이지에서

- [[context-engineering]] — Managed Agents가 fetched event를 변형하는 목적 하나가 cache hit율이다.
- [[transcript-classifier]] — stage 2가 stage 1과 거의 같은 프롬프트라 거의 전부 cache hit이다(비용 효율 설계).
- [[scripts-that-talk-back]] — 스크립트 stdout으로 지시를 돌려주면 따르기는 좋아지지만 *"at the expense of prompt caching"*이다. 동적 호출은 캐시되지 않고 정적 스킬은 캐시된다.
- [[deferred-tool-context]]·[[toolbox-pattern]] — 둘 다 "도구 정의를 늦게 싣거나 매번 다시 조립하면 캐시 접두가 바뀌는가"를 미해결로 두었다. Robinson의 답은 이름만 싣고(tool search), 턴 중에는 도구 목록을 바꾸지 않는 것이다. 로드한 정의가 어디에 붙는지는 말하지 않는다.
- [[automatic-model-routing]]·[[model-mixing-economics]] — 과제 중간에 모델을 바꾸면 캐시가 깨지는가. Factory는 *"just a pricing decision"*으로 비켜 갔고, Nadella 편은 스웜에서 모델 패밀리를 넘나드는 KV 캐시 적중률을 과제로 들었다. Coinbase 사례는 캐싱을 비용 레버로 든다(*"to stop prefilling the stuff every time"*).
- [[trusted-throughput]] — 토큰 효율 기법 중 하나("고정 시스템 프롬프트를 위, 가변 콘텐츠를 아래").
- [[fireworks-ai]] — 서빙 쪽의 같은 날 소스. prompt cache hit rate를 고객별 커널 최적화의 입력(05:41~06:08)이자 배포 후 모니터링 지표(11:51~11:59)로 든다([[tech-bridge-fireworks-train-to-deploy-open-models]]). 하네스가 접두를 지키면 서빙이 그 적중률을 운영 지표로 받는다.

## ⚠️ 유보

- 적중률·절감액 수치는 이 위키의 어느 소스에도 없다.
- 공급자별 캐시 창 길이·가격은 이 페이지가 다루지 않는다. Robinson의 10분·60분은 *"maybe"*다.
- 캐시를 지키려는 설계가 다른 목표(동적 지시, 모델 라우팅, 도구 지연 로딩)와 부딪힌다. 이 위키는 그 trade-off를 측정한 소스를 아직 갖고 있지 않다.

## References

- [[tech-bridge-lee-robinson-always-on-agents]] — first-seen
- [[context-engineering]] · [[context-resets-and-compaction]] · [[deferred-tool-context]] · [[scripts-that-talk-back]] · [[transcript-classifier]] · [[automatic-model-routing]] · [[always-on-agent-architecture]]

## 줄여도 안 내려가는 비용 — 스킬은 이미 캐시돼 있다 (2026-10-29 · [[tech-bridge-anthropic-fold-subagents-into-skills]])

영어 해설자의 인용(2차 진술, 논문 제목 없음): *"A July paper shortens skills by up to 54% and the cost per task didn't necessarily drop. In some cases, skills are small, mostly cash[cached] parts of what the agent reads."*(06:12~06:24) 캐시된 접두부는 이후 턴에서 *"charged a lot less"* 하므로, **지시 문서의 길이를 줄이는 것만으로는 비용 레버가 약할 수 있다** → [[agent-skills]] · [[subagent-folding]].

---
title: Lee Robinson
type: entity
category: person
tags: [spacex, cursor, grokbot, always-on-agents, agent-harness, prompt-caching, lecture]
aliases: [Lee Robinson, Lee]
links: []
sources: [tech-bridge-lee-robinson-always-on-agents]
created: 2026-10-18
updated: 2026-10-18
---

# Lee Robinson

[[spacex|SpaceX]]에서 [[grokbot|GrokBot]]의 always-on agent 구조를 만드는 쪽의 엔지니어다. 이 위키에는 스탠퍼드 강의를 재배포한 [[tech-bridge-lee-robinson-always-on-agents]](2026-10-17 업로드)로 처음 들어왔다. ⚠️ 자막에서 화자는 *"So, as mentioned, I'm Lee."*(00:00)라고만 한다. 성 Robinson, 직함 "SpaceX 엔지니어", 스탠퍼드 CS146S는 **제목·설명란에만** 있다. 설명란에 링크는 없다.

## 위키에서 알려진 사실 (전부 그 강의의 발화)

- 소속 단서: *"some of the things we'll talk about are in progress. We're working on at SpaceX."*(00:16~00:19), *"one of the principles that we had at Cursor uh and now at SpaceX is to delete the product."*(37:45~37:54) → [[cursor|Cursor]]에 있었고 지금은 SpaceX 쪽이라는 뜻으로 읽힌다. ⚠️ 조직 관계는 [[spacex]]·[[cursor]]의 원칙대로 추정하지 않는다.
- GrokBot을 1인칭으로 설명한다: *"how we built this architecture, how we built the harness"*(02:10~02:13), *"The biggest difference with the Grockbot[=GrokBot] harness"*(18:21~18:23).
- 주장: 루프를 VM 밖 서버에 둔다(14:53~15:24). job queue 대신 durable workflow를 쓴다(Temporal, 16:17~17:19). 클라이언트-서버 도구는 send user 하나다(18:33~18:39). prompt caching이 깨지면 *"a bug in the system"*이다(29:51~29:55). 캐시가 따뜻할 때 compaction한다(32:11~32:30). → [[always-on-agent-architecture]] · [[prompt-caching]]
- 원칙: *"delete the product"* — *"the models today are the worst they'll ever be"*(37:54~38:00). → [[harness-pruning]]
- 수강생에게: *"I'm still pro looking at code"*(43:40~43:42), 시스템 설계와 아키텍처가 *"more important than ever"*(43:30~43:33).

## ⚠️ 유보

- 성·직함·학교·과목은 설명란 기준이다. 경력은 Cursor 이전에 대해 발화되지 않는다. 녹화일도 발화되지 않는다.
- 강의의 비교 주장(auto review blind test, 환각 *"solved problem mostly"*)은 근거가 없다.

## References

- [[tech-bridge-lee-robinson-always-on-agents]] · [[grokbot]] · [[spacex]] · [[cursor]] · [[tech-bridge]]

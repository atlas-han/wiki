---
title: "플랫폼으로서의 하네스 (Harness as Platform) — 하네스는 플랫폼 팀이, 스킬은 도메인 팀이"
type: concept
category: pattern
tags: [harness, platform-engineering, agent-skills, plugins, runtime-loading, organization, subagents]
aliases: [harness as a platform, 하네스 제공자, providers of the harness, 골격 고정 + 런타임 스킬]
related: [harness-engineering, agent-skills, deferred-tool-context, deterministic-agent-pipeline, agent-harness-design, model-context-protocol, skill-self-improvement]
first-seen: tech-bridge-uber-debug-assist
sources: [tech-bridge-uber-debug-assist]
created: 2026-10-09
updated: 2026-10-09
---

# 플랫폼으로서의 하네스 (Harness as Platform)

**에이전트의 골격·실행 환경·의존성·단계(하네스)는 플랫폼 팀이 하나로 만들어 제공하고, 도메인 지식(스킬·플러그인·서브에이전트)은 각 도메인 팀이 가져와 런타임에 꽂는 조직 설계.** 새 에이전트를 만드는 일이 *"crowd sourcing the skills"* 가 된다. [[uber|Uber]] [[debug-assist|Debug Assist]] 팀의 운영 방식 — [[tech-bridge-uber-debug-assist]] ([[kriti-dangi|Kriti Dangi]]).

> *"this is the basic skeleton of the agent. It never changes. What changes is the skills and plugins."* (14:56~15:04) · *"You bring your own specialization. And we provide the harness."* (16:18~16:23) · *"Because we are not the owners of domain, we are the providers of the harness."* (27:46~27:50)

> ⚠️ `en`·ko 자막은 이 세 문장의 *harness* 를 **framework / structure / infrastructure** 로 옮겨 개념이 자막 본문에서 사라진다. 인용은 en-orig.

## 구성 (15:40~17:27)

- **골격은 고정** — 단계·노드·상태 전달은 바뀌지 않는다 → [[deterministic-agent-pipeline]]
- **비즈니스 로직은 골격 밖** — 노드별 스킬(*"How to create a good PR at Uber"*, 테스트 계획 관행, 안드로이드 수정 관행)은 런타임에 가져온다 → [[agent-skills]]
- **플랫폼이 주는 것** — *"the harness (…) the steps to follow (…) the runtime environments, the dependencies"*(15:52~16:01). 단일 Python 코드베이스를 PEX로 패키징, 실행 시 **에이전트 타입**에 맞는 바이너리·Docker 이미지·파이프라인을 가져온다. 에이전트 약 8개 · 모노레포 5개(16:23~16:58)
- **플랫폼이 덜 짊어지는 것** — *"now we don't have to maintain a multitude of skills and plugins and whatnot for everyone"*(16:09~16:15)
- **범위 지정** — 사내 마켓플레이스 플러그인 약 3,000개를 다 넣으면 *"It goes crazy"* → 에이전트 타입 파라미터로 자른다(17:09~17:27) → [[deferred-tool-context]]와 비교
- **다음 단계** — domain extensions: 도메인 소유자가 자기 서브에이전트와 지식 베이스를 직접 관리. 고유 서브에이전트 30개 → *"roughly 10,000 by the end of next half"*(27:27~27:55, 계획치)

## ⚠️ 유보

- **스킬 품질·거버넌스** — 크라우드소싱된 스킬을 누가 검토·승격하는지, 충돌하면 어떻게 하는지 발화 없음. [[agent-skills]]의 거버넌스 경고(*"거버넌스 없으면 새 기술부채"*)가 그대로 적용된다.
- **서브에이전트 10,000개의 선택 문제** — 플러그인 3,000개에서 생긴 *"It goes crazy"* 가 서브에이전트 층에서 다시 생길 자리. 라우팅 방식 미발화.
- **단일 소스** — 한 회사 한 팀의 자기 보고.

## References

- [[tech-bridge-uber-debug-assist]] — first-seen
- [[uber]] · [[debug-assist]] · [[kriti-dangi]]
- 관련: [[harness-engineering]] · [[agent-skills]] · [[deferred-tool-context]] · [[deterministic-agent-pipeline]]

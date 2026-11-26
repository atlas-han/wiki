---
title: HumanLayer
type: entity
category: org
tags: [coding-agents, multiplayer, control-plane, harness, software-factory, startup]
aliases: [Human Layer, 휴먼레이어]
sources: [tech-bridge-horthy-state-of-software-factory, tech-bridge-dex-horthy-twelve-rules-no-slop-factory]
links:
  - "https://www.humanlayer.dev/"
  - "https://humanlayer.dev/resources"
  - "https://github.com/humanlayer/12-factor-agents"
created: 2026-10-16
updated: 2026-11-26
---

# HumanLayer

[[dex-horthy|Dex Horthy]]가 CEO·공동 창업자인 회사. 자기 설명: *"We build a multiplayer coding agent workspace."*(00:57~00:58, 직전에 *"multi-agent"* 로 말했다가 정정), *"we are building building blocks for software factory builders"*(01:05~01:09). 초점은 *"hard problems in complex code bases. You have hundreds of engineers, you have hundreds of repos"*(01:10~01:16). ⚠️ 모든 내용은 **당사자 진술**([[tech-bridge-horthy-state-of-software-factory]]), 고객·사용 수치 없음.

## 제품 (발화 기준)

- **control plane** — [[agent-platform-layers|네 층]](compute · dev env · harness · control plane) 중 *"we're kind of working very closely in this control plane"*(14:53~14:58).
- **shared collaborative workspace** — 팀원의 세션 보기·참여, 세션 공동 프롬프트(*"co-prompt my session"*), 로컬 노트북 세션에도 사람을 끌어온다(*"I can pull somebody into my cloud code[=Claude Code?] session"* 15:12~15:16), Google Docs·Notion 모양의 artifact 협업(15:16~15:22).
- ⭐ **diff 스트리밍** — *"every agent running anywhere as it's writing code the diffs are streaming to the cloud. So we can do code review uh without waiting for pull request."*(15:22~15:31) → [[verification-bottleneck]]
- **custom harness** — *"We're going to open source it in the next couple weeks."*(14:59~15:02) ⚠️ 이름 미발화, 공개 여부 미확인.
- **show me 스킬** — 계획·PR 분할을 시각적으로 맞추는 스킬, 제품 내장 + 오픈소스, *"probably up to like 20K installs"*(11:14~11:16, 추정).
- *"We've been building this for a year basically mostly in secret"*(15:32~15:37).
- 12-factor agents GitHub(`humanlayer/12-factor-agents`)는 설명란 링크 — 발표에서는 *"12-factor agents"*(00:47)로 이름만.

## 위키에서의 좌표

- [[multiplayer-agent-context]] — [[conductor|Conductor]]와 같은 범주(여러 사람 × 여러 에이전트 공유 워크스페이스)
- ko 자막은 회사 이름을 **"휴먼 … 층"·"인권 문제"·"인간 영역"** 으로 옮긴다(raw 보정 목록)

## References

- [[tech-bridge-horthy-state-of-software-factory]] · [[dex-horthy]]

## 2026-11-26 — 창업자가 *전 CEO* 로 소개됐다 ([[tech-bridge-dex-horthy-twelve-rules-no-slop-factory]])

[[dex-horthy|Dex Horthy]]의 Code Summit 발표 해설: *"휴먼 레이어를 공동 창업했고 최근 팩토리에 합류했습니다."*(00:28~00:32) 설명란은 그를 *Factory, 전 HumanLayer CEO* 라고 적는다 → [[factory-ai]]. ⚠️ **회사가 어떻게 됐는지는 소스에 없다** — 인수 · 정리 · 경영 교체 가운데 무엇인지 위키는 정하지 않았다. 이 페이지의 제품 서술(control plane · diff 스트리밍 · 오픈소스 예정 하네스)은 10-14 업로드 시점의 당사자 진술로 남긴다.

- show me 스킬은 이번 발표에서도 다섯 번째 규칙(눈으로 맞춰 보라)의 도구로 나온다: *"그가 공개한 쇼미라는 스킬이 그런 용도입니다."*(06:44~06:46) 쓰임은 *"HTML 목업, 표, 차트를 보면서 에이전트와 방향을 맞추라는 겁니다."*(06:39~06:43) ⚠️ 이번에는 회사 이름 없이 *그가 공개한* 이라고만 한다.

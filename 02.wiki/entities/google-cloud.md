---
title: Google Cloud
type: entity
category: org
tags: [google, cloud, database, mcp, platform, security]
aliases: [GCP, Google Cloud 데이터베이스]
links:
  - https://cloud.google.com/
sources: [tech-bridge-build-time-vs-runtime-tools]
created: 2026-09-11
updated: 2026-09-11
---

# Google Cloud

Google의 클라우드 플랫폼 조직. 이 위키에는 [[tech-bridge-build-time-vs-runtime-tools]]의 **데이터베이스 팀 발표**로 처음 등장한다 — [[averi-kitsch|Averi Kitsch]]와 [[prerna-kakkar|Prerna Kakkar]]. [[google-deepmind]]에 이어 **두 번째 Google 조직 페이지**이며, DeepMind가 *연구·소비자 에이전트* 축이었다면 이쪽은 **인프라·플랫폼** 축이다.

> ⚠️ 이 페이지의 내용은 전부 **당사자 진술**이다. 수치 독립 확인 없음.

## 위키에서 알려진 사실

- **[[mcp-toolbox-for-databases|MCP Toolbox for Databases]]** — 오픈소스 자체 관리형 데이터베이스 MCP 서버. GitHub 별 약 15.7k, 기여자 132+, 데이터베이스 40+ (자기 진술).
- **Google managed MCP** — Toolbox의 호스팅·완전 관리형 버전. *"거버넌스가 되고, 검색이 단순하며"*, **Model Armor**로 접근 관리·신원 제어. 관리형 MCP + Toolbox 합산 **월 도구 호출 2천만 건**(자기 진술).
- 자사 에이전트·하네스로 **Gemini CLI**, **Antigravity**(화자는 *"Antigravity CLI"*)를 언급한다. 함께 언급된 *"Cloud Code"* 는 Google *Cloud Code*인지 [[claude-code|Claude Code]]인지 **판정 불가**.
- 발표자가 밝힌 조직 관심사: **데이터베이스를 에이전트 앞에서 지키는 것** — [[confused-deputy-attack]]·[[lethal-trifecta]]·[[agent-identity-separation]]·[[secure-tool-evolution]]·[[bound-parameters]]가 그 산출물이다.
- 고객 1위 요청은 **읽기 전용 제한**이라고 밝힌다.
- **eval bench** — 에이전트·MCP·스킬 평가 프레임워크(Prerna 리드). 내용 미상.

> **Google에서의 MCP 역사**를 다루겠다고 예고했으나(00:56~01:01) 실제 발표에는 Toolbox 소개만 있고 역사 서술은 없다.

## 이 위키에서의 자리

이 위키의 조직 축에서 **클라우드 플랫폼 벤더**는 처음이다 — [[amazon]]은 *도입 조직*(사내 파일럿)으로, [[nvidia]]는 *하드웨어* 로 들어왔다. Google Cloud는 **에이전트가 데이터베이스에 닿는 길 자체를 파는** 자리에 있고, 그래서 발표의 구조가 *자사 도구가 없는 세계 vs 있는 세계* 다.

[[composio]]가 *지식 노동에는 거버넌스 primitive가 없다* 고 팔고, [[promptql]]이 *회사 지식의 접근 제어* 를 판다면, Google Cloud는 **데이터베이스 접근의 거버넌스**를 판다 — 셋 다 [[agent-governance-layers]]의 ①층(결정론적 접근 제어)을 서로 다른 자리에서 제품화한 것이다.

## References

- [[tech-bridge-build-time-vs-runtime-tools]] · [[mcp-toolbox-for-databases]] · [[averi-kitsch]] · [[prerna-kakkar]]
- 관련: [[google-deepmind]] · [[model-context-protocol]]

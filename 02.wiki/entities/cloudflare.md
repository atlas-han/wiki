---
title: Cloudflare
type: entity
category: org
tags: [cloud-infrastructure, security, glasswing-partner]
sources: [anthropic-project-glasswing-update-2026-05, tech-bridge-brockman-agi-era-defender-window]
links:
  - https://www.cloudflare.com
created: 2026-05-25
updated: 2026-09-20
---

# Cloudflare

미국 기반 클라우드 인프라·보안 회사. CDN, DDoS 방어, Workers 등 운영. 본 위키에서는 [[project-glasswing]] 주요 파트너로 등장.

## 위키에서 알려진 사실

- [[project-glasswing]] 파트너로 [[claude-mythos-preview]] 사용
- 자사 코드베이스에서 **2,000 버그 발견** (그중 400개가 high/critical)
- **버그 발견율 10배 증가** 보고
- false positive 비율이 인간 테스터보다 낮다고 평가
- → [[ai-vulnerability-discovery]] 실증 사례

## 미해결 사항

- 회사 기본 프로필, 제품 라인업, AI 채택 전반 → 별도 소스 ingest 필요

## References

- [[anthropic-project-glasswing-update-2026-05]]

## 에이전트가 직접 조작한 콘솔 (2026-09-20 · [[tech-bridge-brockman-agi-era-defender-window]])

[[greg-brockman|Greg Brockman]]의 펜테스트 일화에서 **[[codex|Codex]]가 클릭해 다닌 대상**으로 등장한다.

> **45분 동안, 그것이 제 Cloudflare 제어판을 열었습니다. 클릭해 다니면서 헤더를 전부 설정하고, 저를 Cloudflare Pages로 마이그레이션했습니다.** (19:51~20:10)

**이 위키에서 이 회사가 에이전트의 *조작 대상* 으로 나오는 첫 자리**다 — API나 커넥터를 통해서가 아니라 **사람용 웹 콘솔을 그대로 쓴다**는 점이 요지이고, 그래서 이 언급은 [[openai-astra|Astra]]의 컴퓨터 사용 논지에 붙는다.

> ⚠️ 지나가는 언급이다. 제품 자체에 대한 정보는 없고, 권한을 어떻게 줬는지도 소스에 없다.

→ [[tech-bridge-brockman-agi-era-defender-window]] · [[codex]] · [[greg-brockman]]

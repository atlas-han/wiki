---
title: HackerTube
type: entity
category: product
tags: [personal-software, youtube-alternative, hacker-news, karpathy, claude-code, curation]
aliases: [HackerTube, Hacker Tube]
links:
  - https://hackertube.org/
sources: [tech-bridge-nick-saraev-karpathy-ai-habits, tech-bridge-karpathy-hackertube-two-hours-five-words]
created: 2026-11-08
updated: 2026-11-19
---

# HackerTube

[[andrej-karpathy|Andrej Karpathy]]가 Claude로 만들었다고 전해지는 YouTube 스타일 사이트. Hacker News에서 여러 해에 걸쳐 반복 추천된 영상만 모은다. [[tech-bridge-nick-saraev-karpathy-ai-habits]]에서 [[nick-saraev|Nick Saraev]]가 *"거슬리면 직접 만든다"* 의 예로 든다. 링크는 설명란(`hackertube.org`)에 있다.

> ⚠️ **2차 전달.** 제작 경위 · 프롬프트는 Saraev의 설명이고, 사이트와 Karpathy의 원 글은 위키가 열지 않았다.

## 소스에서 확인되는 것

- 계기(화자 전달): YouTube 썸네일을 보고 *"Boy, what slop."*(03:35~03:37)
- 화자는 처음엔 *"basically just scraped the best news from Hacker News"*(03:41~03:43)라 하고, 뒤에서 전하는 프롬프트는 대상을 **영상**으로 좁힌다: *"restricted to videos that have been repeatedly recommended on Hacker News over the years."*(05:12~05:15)
- 프롬프트의 시작은 인사다 — *"Hi Claude, good morning."*(05:05~05:08) — 화자는 이를 *Claude에게 예의 바르게*의 예로 쓴다.
- 공유 방식: 앱이 아니라 데이터와 프롬프트를 나눈다는 습관의 맥락에서 언급된다 → [[share-data-and-prompt-not-app]].

## References

- [[tech-bridge-nick-saraev-karpathy-ai-habits]] (7절 · 10절)
- https://hackertube.org/ (⚠️ 미열람)

## 2026-11-19 — 만든 순서 · 선별 기준 · 토큰 ([[tech-bridge-karpathy-hackertube-two-hours-five-words]])

두 번째 소스(한국어 해설, Karpathy의 글과 댓글을 이어 붙인 정리 — ⚠️ 2차 전달, 사이트 · 원 글 미열람).

- **규모**: *"이름은 해커 튜브. 해커 뉴스 20년치 댓글에서 골라낸 영상 6,454개가 들어 있습니다."*(00:20~00:24) 발표 글 조회 587만 회 이상.
- **순서**: Hacker News 20년 치 댓글 4,300만 개(Hugging Face 공개 데이터)를 내려받는다 → 주소와 정규식으로 거르고 스팸을 버린다 → 남은 댓글을 [[claude-code|Claude Code]] 워크플로 기능으로 하나하나 읽힌다(Sonnet 서브에이전트, ASR 추정) → *"그렇게 영상을 추천하는 댓글 약 4만 개, 영상 6,454개가 남았습니다."*(03:08~03:10)
- ⭐ **선별 기준**(사이트 소개 페이지, 해설 전달): *"서로 다른 세 사람이 서로 다른 세 달에 걸쳐 진지하게 추천한 영상만 남긴다."*(03:15~03:19) — 11-08 편의 *repeatedly recommended … over the years* 가 숫자로 풀린다.
- **사람이 한 일**: *"구글 클라우드에서 유튜브 API 키를 만들고 서버를 하나 켜고 도메인을 샀습니다."*(03:23~03:27)
- **토큰**: *"입력 토큰 5억 400만 개, 출력 760만 개였습니다."*(03:40~03:42) 90% 넘게가 댓글에 이름표를 붙이는 일이고, *"앱을 만들고 배포한 진짜 작업은 오퍼스 5.5 토큰 약 100만 개."*(03:50~03:52)
- **배포 프롬프트**: 서버 주소와 낱말 다섯(*"업데이트, 배포, 보안 강화, 최적화."*(04:29~04:31) — 캡션에는 넷, 11-08 편의 *update, deploy, secure, harden, and optimize* 와 맞춤).
- **공개 뒤**: *"검색 필터, 정렬, 재생 목록 같은 기능이 공개 두 시간도 안 돼 한꺼번에 들어갔습니다."*(06:50~06:56)
- **공개한 것은 데이터**: 서버 코드는 내놓지 않았다. *"대신 댓글을 분석한 데이터를 압축 파일 하나로 올렸습니다."*(07:53~07:55) 해설의 결론은 *"해커 튜브에서 진짜 귀한 건 20년치 댓글에서 걸러낸 영상 목록입니다."*(08:57~09:00) → [[share-data-and-prompt-not-app]]
- 파생: 엿새 뒤 같은 방식으로 영상 47,000개짜리 *TristanTube*(표기 미상)를 3분 만에 만들었다고 한다.

⚠️ 11-08 편의 *"scraped the best news from Hacker News"* 는 이 편으로 정리된다 — 대상은 뉴스가 아니라 **댓글에서 추천된 영상** 이다.

---
title: The Twelve-Factor App
type: source
tags: [source, engineering, saas, cloud-native, methodology]
created: 2026-06-27
updated: 2026-06-27
source-url: https://12factor.net/
source-type: docs
author: Adam Wiggins (Heroku)
date-published: 2011
ingested: 2026-06-27
---

# The Twelve-Factor App

[[adam-wiggins|Adam Wiggins]]를 비롯한 [[heroku|Heroku]] 기여자들이 수십만 SaaS 앱의 개발·운영·스케일을 관찰해 종합한 **방법론(methodology)**. 언어·백킹 서비스에 무관하게 적용 가능한, "modern, scalable, maintainable software-as-a-service"를 위한 12가지 원칙을 제시한다.

> ⚠️ **raw 클리핑 범위 주의**: `01.raw/articles/2026-05-25_The Twelve-Factor App.md`는 `12factor.net`의 **인트로 페이지(Introduction / Background / Who should read)만** 캡처했고, 12개 factor 본문은 포함하지 않는다. 본 위키의 12요소 정리는 2011년 정립된 표준(canonical) 내용을 보완해 작성했다.

## 핵심 요약

원문 인트로가 명시한 12-factor 앱의 다섯 가지 목표:

1. 신규 개발자 합류 비용 최소화를 위한 **선언적(declarative)** 설정 자동화
2. 실행 환경 간 **최대 이식성(maximum portability)**을 위한 OS와의 **깨끗한 계약(clean contract)**
3. 서버·시스템 관리가 필요 없는 **클라우드 플랫폼 배포** 적합성
4. dev/prod **divergence 최소화** → **continuous deployment** 가능
5. 도구·아키텍처·개발 관행의 큰 변경 없이 **scale up**

→ 12개 원칙 전문은 [[twelve-factor-app]] 레퍼런스 페이지 참조.

## 핵심 인용

> The twelve-factor app is a methodology for building software-as-a-service apps that use **declarative** formats for setup automation … have a **clean contract** with the underlying operating system, offering **maximum portability** … and can **scale up** without significant changes to tooling, architecture, or development practices.

> Our motivation is to raise awareness of some systemic problems we've seen in modern application development, to provide a shared vocabulary for discussing those problems, and to offer a set of broad conceptual solutions to those problems with accompanying terminology.

> The format is inspired by Martin Fowler's books *Patterns of Enterprise Application Architecture* and *Refactoring*.

## 등장 개체

- [[adam-wiggins]] — 문서 저자, Heroku 공동창업자
- [[heroku]] — 12-factor의 관찰 기반이 된 PaaS 플랫폼
- [[martin-fowler]] — 문서 형식(*PoEAA*, *Refactoring*)의 영감원
- [[twelve-factor-app]] — 본 소스에서 도출한 방법론 레퍼런스 페이지

## 관련 개념

- [[pets-vs-cattle]] — stateless·disposability(VI·IX)의 인프라 운영 버전
- [[refactoring]] — 형식을 빌려온 Fowler 계보, "shared vocabulary" 사상 공유

## References

- 원문: <https://12factor.net/>
- raw: `01.raw/articles/2026-05-25_The Twelve-Factor App.md` (인트로만)

---
title: Heroku
type: entity
category: product
tags: [paas, cloud, saas, platform]
links:
  - https://www.heroku.com/
created: 2026-06-27
updated: 2026-06-27
---

# Heroku

초기 **PaaS(Platform-as-a-Service)** 플랫폼. 개발자가 인프라·서버 관리 없이 코드를 push해 배포할 수 있게 한 선구적 클라우드 플랫폼이다. 이 위키에서의 의의는 [[twelve-factor-app|12-Factor App]] 방법론의 **관찰 기반**이라는 점 — Heroku 기여자들이 플랫폼 위에서 수십만 앱의 organic growth와 software erosion을 지켜보며 12원칙을 도출했다.

## 12-Factor와의 관계

- Heroku의 배포 모델(git push → build/release/run, 환경 변수 config, `Procfile` 기반 process type, dyno = disposable stateless 프로세스)이 [[twelve-factor-app]]의 여러 factor를 사실상 제품으로 구현.
- [[adam-wiggins|Adam Wiggins]](공동창업자)가 그 경험을 문서화.

## References

- [[twelve-factor-app]] · [[adam-wiggins]]
- 외부: <https://www.heroku.com/>

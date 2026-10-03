---
title: "공개적으로 만들기 (Build in the Open) — 복제가 공짜인 시대의 우위"
type: concept
category: framing
tags: [open-source, software-economics, moat, distribution, ecosystem, software-factory, startup]
aliases: [build in the open, building in the open, 공개 개발, public factory, 공개 공장]
related: [software-factory, factory-engineering, company-knowledge-moat, smarter-software-vs-cheaper-software, ai-slop]
first-seen: tech-bridge-warp-factory-engineering
sources: [tech-bridge-warp-factory-engineering]
created: 2026-10-03
updated: 2026-10-03
---

# 공개적으로 만들기 (Build in the Open)

**에이전트로 소프트웨어를 만들기가 싸지면 복제도 공짜가 되므로, 좋은 제품만으로는 가치를 붙잡을 수 없다 — 스타트업이 제품 밖의 우위(생태계·브랜드·커뮤니티)를 만드는 길로 공개 개발을 택하고, 오픈소스 운영의 고통은 소프트웨어 공장으로 감당한다는 전략.** [[warp|Warp]]의 [[zach-lloyd|Zach Lloyd]]가 [[tech-bridge-warp-factory-engineering]]에서 Warp의 오픈소스 전환 이유로 설명했다.

## 논리

1. **만들기가 싸지면 복제가 공짜다** — *"it's becoming much cheaper to build software. (…) a corollary of that is that it's becoming trivial to clone software."*(05:04~05:14)
2. **그러면 제품으로는 가치를 못 붙잡는다** — *"it's very hard to build a software business if it's free to build software. It's hard to capture the value, especially if a competitor can clone."*(05:21~05:30) *"a great product probably was never enough"*(05:50~05:55)
3. **제품 밖의 우위가 필요하다** — distribution · ecosystem · brand · data mo[a]t(ASR *"data mode"*) · capital(06:07~06:16). 스타트업엔 이것들이 없다.
4. **공개 개발이 그 우위를 만든다** — 생태계, *"hated on Hacker News to like tolerated"*(06:42~06:47), 브랜드, 커뮤니티(06:37~06:50).

## 오픈소스의 고통 → 공장

전통적 고통: *"noisy issues"*, *"sloppy PRs"*, *"code review hell"*, 변경 검증 시간(07:01~07:14). Warp가 5년 closed 끝에 전환을 결정한 계기는 *"we built a whole set of automations, really a software factory, around managing the open source project"*(07:23~07:33)였다 — 잘 되면 *"agents are helping contributors contribute. They're helping maintainers maintain."*(08:17~08:24) → [[software-factory]]

**공개 공장** — 오픈소스화의 이유 하나가 *"build a public factory"*(04:19~04:25): build.warp.dev가 이슈 흐름·상태·담당 에이전트·기여자를 공개한다. ⚠️ *"It's not working perfectly, but it is working"*(04:44~04:49) — 자평.

## 위키에서의 좌표

- **[[company-knowledge-moat]]** — 그쪽은 *사내 에이전트*의 우위를 **회사 고유 맥락**에서 찾는다. 이쪽은 *제품 회사*의 우위를 **공개로 얻는 생태계·브랜드**에서 찾는다 — 둘 다 "모델·코드는 해자가 아니다"에서 출발한다.
- **[[smarter-software-vs-cheaper-software]]** — "소프트웨어가 싸진다"를 가치 하락으로만 계산하는 것에 대한 반론. 이 페이지의 전제(만들기·복제가 싸진다)는 그 반론의 대상과 같은 관찰이다.
- **[[ai-slop]]** — sloppy PR이 오픈소스 유지보수의 고통으로 다시 등장한다; 처방은 사람 리뷰 강화가 아니라 **에이전트 1차 리뷰 + 리스크에 따른 사람 투입**(11:01~11:11).

> ⚠️ **사례 하나, 당사자 진술.** Warp의 60,000 stars·수백 명 기여자·800,000 활성 개발자(00:56~01:06)는 창업자 진술이고, 오픈소스화가 매출·채택에 준 효과는 측정되지 않았다. "복제가 공짜"도 화자가 *"a really stupid graph"*(04:59~05:02)라 부른 슬라이드 수준의 주장이다.

## References

- [[tech-bridge-warp-factory-engineering]] — first-seen
- [[warp]] · [[zach-lloyd]] · [[software-factory]] · [[factory-engineering]]

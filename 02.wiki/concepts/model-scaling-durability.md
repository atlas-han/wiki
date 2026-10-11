---
title: "모델과 함께 커지는 제품 (Model-Scaling Durability)"
type: concept
category: pattern
tags: [product-strategy, startups, durability, wrappers, bitter-lesson, domain-expertise, moat]
aliases: [모델과 함께 커지는 제품, 새 모델에 쓸려 가지 않는 제품, scale with the models, working around model limitations, wrapper durability]
related: [sutton-bitter-lesson, company-knowledge-moat, harness-engineering, capability-discovery-burden, openai-dots, intelligence-abundance]
first-seen: tech-bridge-brockman-start-building-before-ready
sources: [tech-bridge-brockman-start-building-before-ready]
created: 2026-10-11
updated: 2026-10-11
---

# 모델과 함께 커지는 제품

**AI 제품의 활동은 두 종류다. 모델이 똑똑해질수록 더 좋아지는 활동이 있고, 지금 모델의 한계를 우회하는 활동이 있다. 후자는 내구성이 없다.** [[greg-brockman|Greg Brockman]]이 [[tech-bridge-brockman-start-building-before-ready]]에서 *"새 모델이 나와도 쓸모없어지지 않는 제품을 어떻게 만드나"* 라는 질문에 답하며 제시했다.

> *"There's some activities I think scale well as the models get smarter and some activities that are kind of working around limitations in the model. The second one is pretty hard to be durable."* (13:44~13:53)

## 내구성이 없는 쪽

> *"there were at various points been startups that really focused on it. We take the model, we add some prompts, we have some very handcrafted whatever."* (13:53~14:02)

단서가 붙는다. 그런 것이 가치 있던 시점이 없었다는 말은 아니고(14:02~14:05, ⚠️ en-orig에서 부정어 하나가 빠진 것으로 판독), *"sometimes it's even about the interface"*. 모델 역량이 한 단계 오를 때마다 **새 인터페이스가 저절로 제안된다.**

| 시기 | 역량 | 그 단계가 부른 인터페이스 (발화) |
|---|---|---|
| 2022 | 응답을 읽을 가치가 생김 (GPT-4) | ChatGPT |
| 2025년 말 | *"AI that kind of shifted from being 20% of your software production to 80%"* (14:27~14:32) | 코딩 에이전트 (*"the coding agent era really started"*) |
| 지금 | *"this era of the personalized agent"* (14:40~14:44) | [[openai-dots|Dots]] |

⚠️ 20%→80%는 출처도 모집단도 없다.

## 내구성이 있는 쪽

> *"the core thing is thinking about where will you scale as the models get smarter? And again some of this is about understanding the industry. Some of this is about building relationships"* (14:59~15:10)

- **이해관계자 신뢰**: 병원이라면 환자·의사·병원 행정·보험사(15:10~15:24). 교육이라면 교사·부모·학생·관리자(11:21~11:31).
- ⭐ **좋은 모델이 해자를 키운다**: *"if you have a model that's just even better, if you are already in that industry, you have these customers that actually your product gets better and more defensible as a result."* (15:28~15:36)
- **도메인 전문성**: *"often in any specific vertical, we're so far from optimal"* (16:00~16:05), *"no matter what sector you pick, there's just so much low-hanging fruit"* (16:17~16:20).
- **구현 언어는 처음부터 장벽이 아니었다**: *"do you have to write in C++ or Swift or something? Like, who cares about that?"* (11:52~11:55)

## 이 위키에서의 좌표

- [[sutton-bitter-lesson]]: 같은 모양의 명제다(손으로 넣은 구조는 계산량 증가에 밀린다). 다만 그쪽은 **모델 설계**이고 이쪽은 **제품 포트폴리오**다. 손으로 다듬은 프롬프트는 제품 층의 *"human knowledge"* 에 해당한다.
- [[company-knowledge-moat]]: 같은 결론을 반대편에서 낸다. Vercel은 *사내 에이전트 쪽*에서 회사 고유 지식이 해자라고 했고, Brockman은 *모델 공급자 쪽*에서 업계 관계·고객이 해자라고 한다.
- [[harness-engineering]]: ⚠️ 긴장 관계다. 아래 유보 참조.

## ⚠️ 유보

- **이해관계가 있다.** 모델 공급자의 사장이 *"모델 한계 우회는 오래 못 간다"* 고 말한다. 그 말이 맞을수록 가치는 모델 쪽으로 쏠린다.
- **경계가 정의되지 않는다.** *"handcrafted whatever"* 가 [[harness-engineering]]의 하네스 전부(도구·검증 루프·컨텍스트 관리)를 가리키는지, 모델 결함을 **땜질하는** 부분만 가리키는지 발화되지 않는다. 이 위키의 하네스 페이지들은 하네스를 지속되는 자산으로 다뤄 왔다.
- 실패한 스타트업의 사례·이름·수치는 없다.

> ⚠️ Contradiction: *"모델 한계를 우회하는 활동은 내구성이 없다"*(Brockman, 13:44~13:53) vs [[harness-engineering]] — 이 위키의 하네스 페이지들은 하네스(도구·검증 루프·컨텍스트 관리)를 지속되는 자산으로 다룬다. Brockman은 *"handcrafted"* 가 무엇까지 덮는지 정의하지 않으므로 판정하지 않는다.

## References

- [[tech-bridge-brockman-start-building-before-ready]]: first-seen
- [[greg-brockman]] · [[openai]] · [[openai-dots]]
- 관련: [[sutton-bitter-lesson]] · [[company-knowledge-moat]] · [[harness-engineering]] · [[intelligence-abundance]]

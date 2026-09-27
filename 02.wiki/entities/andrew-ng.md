---
title: Andrew Ng
type: entity
category: person
tags: [educator, ai, coursera]
links:
  - https://www.andrewng.org/
sources: [tech-bridge-andrew-ng-ai-opportunity, tech-bridge-altman-agi-superintelligence, tech-bridge-jensen-huang-g20-agi, tech-bridge-oracle-agent-memory-harness, tech-bridge-sdd-full-course]
created: 2026-08-31
updated: 2026-09-27
---

# Andrew Ng

Google Brain·[[coursera|Coursera]] 공동창업자. 머신러닝 온라인 교육의 대표 인물. 본 위키에는 Silicon Valley Girl 인터뷰 Tech Bridge 재배포([[tech-bridge-andrew-ng-ai-opportunity]], 2026-08-30)로 첫 등장.

## 위키에서 알려진 사실

- 공포 마케팅을 [[regulatory-capture]]로 읽음. 거대 모델 투자 회수를 위해 오픈웨이트를 규제 쪽으로 누르려 한다는 주장(회사 이름은 안 밝힘).
- 노동: 직업의 30–40% task는 AI, 나머지 60%는 economic complement로 **더 귀해짐**. 치환은 "AI가 사람"이 아니라 **AI를 쓰는 사람이 안 쓰는 사람**.
- 통상의 LLM 사용은 [[cognitive-offloading]] — 숙제 점수는↑, 장기 retention은↓. 그래서 [[learnvector|LearnVector]](Coursera $100M)로 1:1 학습을 새로 짠다.
- 빌드 병목은 코딩이 아니라 product management(무엇을 빌릴지·taste). SE만이 아니라 marketer/HR/finance가 직접 빌드해야 한다고 봄.
- AGI를 "임의 지적 과제"로 정의하면 **decades**. 조기 선언은 정의 낮추기·계약 인센티브([[openai]]–Microsoft 합의) 문제.

같은 채널의 위험 쪽 대조: [[bill-gates]] / [[tech-bridge-bill-gates-ai-warning]].

## 반대편 진술이 들어왔다 (2026-09-06)

Ng의 두 주장에 **당사자·반대편**의 진술이 붙었다.

- **AGI 조기 선언 유인** — [[sam-altman]]([[tech-bridge-altman-agi-superintelligence]]): AGI는 *"별 의미 없는 마케팅 용어"*, 선언의 의미는 *"없다"*, 내부 어휘는 이미 *"초지능의 연속 경사로"*. [[jensen-huang]]([[tech-bridge-jensen-huang-g20-agi]]): *"사실상 이미 도달"*. Ng가 *정의를 낮추는 유인*을 경고했다면, 두 사람은 정의 자체를 무의미화한다. → [[agi-definition]]
- **데이터센터 오정보** — Ng는 이를 공포 마케팅의 사례로 꼽았고, Altman은 반대편에서 **물 소비 밈**을 반박한다(*"38,000 쿼리 = 아몬드 한 개"*, ⚠️ 본인이 단서를 단 수치). 같은 화제를 규제 비판자와 운영자가 각자 다룬 형태.
- **일자리 30–40% task** — [[jensen-huang]]이 같은 단위(task)에서 *"작업은 자동화, 직업의 목적은 남는다"* 로 더 강한 결론을 냈고, Altman은 *"영향이 예상보다 적었다"* 고 관찰했다. → [[ai-jobs-impact]]

## References

- [[tech-bridge-andrew-ng-ai-opportunity]] · [[coursera]] · [[learnvector]] · [[regulatory-capture]] · [[cognitive-offloading]]
- 반대편 진술: [[tech-bridge-altman-agi-superintelligence]] · [[tech-bridge-jensen-huang-g20-agi]] · [[agi-definition]] · [[ai-jobs-impact]]

## 강좌 공동 제작자로서 (2026-09-24 · [[tech-bridge-oracle-agent-memory-harness]])

[[oracle|Oracle]]의 [[ignacio-martinez|Ignacio Martinez]]가 *"내 경력의 정점"* 으로 **Ng과 에이전트 메모리 강좌를 냈다**고 소개한다(01:45~01:50). [[toolbox-pattern|툴박스 패턴]]도 *"이 강좌에서 소개했다"*(48:46~48:51), 그리고 동료와 **에이전트 지속 학습 강좌를 녹화할 예정**(*"몇 주 뒤"*, 12:32~12:41). 이 위키에서 Ng은 지금까지 **인터뷰 대상**(규제 포획·노동·AGI 정의)이었는데, 여기서는 **실무 에이전트 기법의 교육 유통 경로**로 등장한다 — Ng 본인은 영상에 나오지 않는다.

> ⚠️ **강좌명·플랫폼을 자막이 말하지 않는다**. ⚠️ en-orig는 이름을 **"Andrew Ang"**(01:47) · **"Andrew Yang"**(48:50)으로 깨뜨린다 — ko·en 변종은 *앤드류 응 / Andrew Ng* 으로 옳다.

## ⚠️ 추정 등장 — SDD 강좌의 소개자 "Andrew" (2026-09-27 · [[tech-bridge-sdd-full-course]])

[[jetbrains|JetBrains]] 협업 스펙 주도 개발 강좌에서 강사가 소개자를 *"Thank you, **Andrew**"*(00:30)로 부른다. **성은 세 트랙 어디에도 없다.** 기여자에 *"Isabel Zaro from deeplearning.ai"*(04:12~04:14)가 있고, 소개자가 *"I'm definitely an advocate of lazy prompting when it works"*(03:31~03:33)라고 말한다 — Ng일 개연성이 높지만 **이 위키는 확정하지 않는다.** 소개자 몫으로 보이는 발화(en-orig `>>` 전환 표시로 추정):

- *"Spec-driven development is currently the best type of workflow for building serious applications with agentic coding assistance."*(00:03~00:09)
- 스펙은 에이전트와 대화하며 핵심 아키텍처 결정을 내리고 그 결정을 마크다운으로 요약시켜 쓴다(01:33~01:48). 스펙 없는 팀에서 에이전트들이 *"building quickly but in contradictory ways"*(02:25~02:27).
- *"the great developers I know out there almost always will write detailed specs for projects with any significant complexity"*(03:33~03:39). 20~30분 돌 에이전트라면 *"3 or 4 minutes"* 들여 명확한 지시를 쓰는 편이 낫다(03:53~04:05).

위 [[cognitive-offloading]]의 "숙제 점수는 오르고 retention은 떨어진다"와 같은 방향의 걱정이 이 강좌에서는 [[cognitive-debt|인지 부채]]라는 개발자 쪽 이름으로 나온다 — 단 그 대목(26:26~26:37)은 소개자가 아니라 레슨 본문의 내레이션이다.

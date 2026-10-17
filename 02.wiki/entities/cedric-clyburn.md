---
title: Cedric Clyburn
type: entity
category: person
tags: [developer-advocate, red-hat, ibm, education, ai-engineer, spec-driven-development, context-engineering, prompt-injection]
links: []
sources: [tech-bridge-ai-engineer-three-tier-skill-stack, tech-bridge-five-concepts-coding-with-ai-agents]
created: 2026-09-16
updated: 2026-10-17
---

# Cedric Clyburn

**[[tech-bridge-ai-engineer-three-tier-skill-stack]]의 화자.** 설명란 기준 **Red Hat 수석 개발자 애드보킷**(*"Red Hat의 수석 개발자 애드보킷 Cedric Clyburn"*).

> ⚠️ **이름과 소속은 영상 설명란에만 있다.** 자막에는 이름이 한 번도 나오지 않고, 자기 언급은 *"저희 채널을 시청하시는 분들이라면"*(07:05)뿐이다. 설명란의 관련 링크 둘은 전부 `ibm.biz`이므로 **제작 채널은 [[ibm|IBM Technology]]로 판정**했고, **Red Hat과 IBM의 관계는 소스가 말하지 않는다.** 2026-09-08(Thomas Wolf)·09-15(Vincent Wendy)와 같은 방식으로 **설명란 근거로 채택하되 출처를 표시**한다. IBM 계열 소스에서 **화자 이름이 처음 확인된 경우**다(09-07·09-08은 무명).

## 소스에서 확인되는 것

- **입장**: *"AI 엔지니어는 머신러닝 연구원이 아니다"* — 연구원은 **엔진**, AI 엔지니어는 **자동차**. → [[ai-engineer-vs-ml-researcher]]
- **테제**: *"코드 생성이 쉬워졌으므로 어려운 부분은 코드가 아니라 판단"*, 그리고 판단은 *"만들어 보면서"* 배운다. → [[taste-vs-judgment]]
- **교육 구조**: 세 층(기초 → AI 특화 → 배포)이고 **순서가 중요** — 기초를 건너뛰면 *"기본기를 다시 익히는 데 많은 시간"*. → [[three-tier-ai-skill-stack]]
- **Python에 대한 기준**: *"마법사가 아니라 에이전트가 쓴 것을 읽을 수 있을 만큼"*. → [[read-fluency-for-agent-output]]
- **에이전트 정의**: 워크플로는 미리 정의된 경로, 에이전트는 동적으로 결정하는 루프 — *"이 루프를 안정적으로, 대규모로 만드는 사람이 좋은 AI 엔지니어"*. → [[workflow-vs-agent]]
- **관찰**: 지금 가장 흔한 프로덕션 사례는 **RAG 지식 시스템 · 도구를 쓰는 에이전트 · 배포 지원**.

## 미해결 사항

- **이력·이전 경력·발표 이력** — 소스에 없다.
- **도입부에 약속한 "세 가지 프로젝트"** 가 영상에 없다 — 화자의 원본이 그런지 편집인지 알 수 없다.
- **촬영 시점**.
- **소속** — 설명란 두 개가 IBM Technology / Red Hat으로 다르게 쓴다(2026-10-17).

## 두 번째 소스 — 개발자의 일이 구현에서 지휘로 (2026-10-17 · [[tech-bridge-five-concepts-coding-with-ai-agents]])

> ⚠️ **소속 표기가 설명란마다 다르다.** 이번 설명란: *"IBM Technology의 Cedric Clyburn"*. 09-15 설명란: *"Red Hat의 수석 개발자 애드보킷"*. 이번에도 **자막에는 이름·소속이 없다.** 어느 쪽인지(또는 둘 다인지) 정하지 않는다.

- **입장**: AI가 개발자를 대체하느냐는 질문에 *"I always say no. I've actually seen more people get into coding because of AI."*(00:31~00:35) 대신 *"what AI will do is change what software development looks like."*(00:35~00:40)
- **전환**: *"the shift from implementing to conducting"*(02:27~02:30). 개발자는 *"a conductor, a captain, someone who can make important architectural decisions"*(03:28~03:36)가 된다. → [[orchestras-not-factories]]
- **개념 묶음**: [[spec-driven-development]](프롬프트는 모델마다 다르게 해석된다), context management(컨텍스트 창의 자원 한계) → [[context-engineering]], loop engineering(*"a recursive goal where you as a human define the purpose and the AI iterates until it's complete"*), skills·automations·sub-agents를 *"contextual engineering capabilities"* 로 묶는다.
- **기초 강조**: 모델은 *"doesn't quite understand time and memory like we do"*(05:33~05:38)라고 말하고, GPU 메모리의 가중치·KV 캐시를 그림으로 설명한다. 첫 소스의 "기초를 건너뛰지 말라"([[three-tier-ai-skill-stack]])와 같은 태도다.
- **보안**: 세 조건(민감 데이터·웹 노출·전송 능력)이 결합하면 인젝션이 성립하고, 처방은 일회용 샌드박스다 → [[prompt-injection]] · [[lethal-trifecta]] · [[agent-sandboxing]]
- **비유**: *"AI is becoming the new electricity"* 를 [[andrew-ng|Andrew Ng]]의 말로 기억해 인용한다(08:28~08:32). *"I had the chance recently to work with AI legend Andrew Ng"*(08:24~08:28)라고 하지만 무슨 일인지는 말하지 않는다.
- 이번에도 측정은 없고 일화(조종사)와 가정 예시(RPG)뿐이다.

## References

- [[tech-bridge-ai-engineer-three-tier-skill-stack]] · [[ibm]] · [[tech-bridge]]
- [[tech-bridge-five-concepts-coding-with-ai-agents]]

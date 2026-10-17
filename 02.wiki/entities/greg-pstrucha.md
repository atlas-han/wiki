---
title: Greg Pstrucha
type: entity
category: person
tags: [linters, deterministic-checks, code-review, agent-skills, sentry]
aliases: [Greg Pstrucha, 그렉 프스트루하]
links:
  - "https://www.linkedin.com/in/greg-pstrucha/"
sources: [tech-bridge-sentry-stop-prompting-codify-linters]
created: 2026-10-16
updated: 2026-10-16
---

# Greg Pstrucha

[[sentry|Sentry]]의 엔지니어로, 코딩 에이전트에게 같은 수정을 다시 프롬프트하지 말고 규칙을 linter와 저장소 정책으로 코드화하라고 주장한다. [[tech-bridge-sentry-stop-prompting-codify-linters]]에서 발표했다. **이름은 제목·설명란에만 있다.** 자막에는 자기소개가 없고 직함·팀도 발화되지 않는다. 소속은 *"I read code when it's Sentry code"*(00:08~00:10), *"Sentry is a pretty old code base. We are on Django, we are on DRF."*(06:04~06:08) 같은 1인칭 복수로 뒷받침된다. 이 위키 첫 등장이다.

## 위키에서 알려진 사실

- 테제: *"you should stop prompting. You should start codifying the actual rules that the agents should be following."*(01:47~01:51) 근거는 compaction이다. *"5 minutes pass and compaction of context happens and we're back to back to square one."*(01:26~01:31) → [[hard-vs-soft-enforcement]] · [[context-resets-and-compaction]]
- 처방: 과거 트랜스크립트와 GitHub 리뷰(봇·동료 피드백)를 에이전트에게 훑게 해서 결정론적 lint 규칙으로 바꾼다(04:43~05:05). 이 작업을 스케줄로 반복한다(05:09~05:16). → [[executable-standards]]
- Sentry 사례 둘. 첫째, Django·DRF 레거시의 OpenAPI drift를 lint 규칙 세 개로 줄였다(06:24~07:07). 둘째, 디버깅 에이전트용 스킬 속 코드 예제를 type check·샌드박스 실행·OpenAPI 일치로 lint했다. 에이전트가 회피하는 *"whack-a-mole"*(09:27)을 거쳐 스킬이 API와 동기화되었다. → [[skill-linting]]
- linter로 못 잡는 판단은 저장소 정책과 **grumpy engineer** 스킬(사내명 Garfield)로 다룬다. 정책마다 서브에이전트를 하나씩 두고, 모두 stand down할 때까지 루프를 돈 뒤에야 본인이 코드를 읽는다(12:18~12:50). 목표는 *"raise the floor"*(13:15)다. → [[automated-code-review]]
- 경고: *"when you give a number to the agent, the agent will optimize the out of that number."*(14:09~14:15) 커버리지 100%에 가깝지만 문자열만 assert하는 테스트가 나왔다. → [[verifiable-goals]] · [[reward-hacking]]
- 루프 유행에 대한 농담: *"this is the closest you will hear me doing loops, by the way."*(12:38~12:41)

## ⚠️ 유보

- 직함·경력·팀은 미발화다. Sentry의 디버깅 에이전트(*"Sentry agent"*)와 Seer의 관계도 미발화다. 행사명은 미발화이며 AI Engineer는 추정이다. 모든 효과는 측정 없는 일화다.

## References

- [[tech-bridge-sentry-stop-prompting-codify-linters]] · [[sentry]] · [[tech-bridge]]

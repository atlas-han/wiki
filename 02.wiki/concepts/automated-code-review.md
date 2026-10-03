---
title: "자동 코드 리뷰 (Automated Code Review)"
type: concept
category: pattern
tags: [code-review, verification, multi-pass, false-positives, human-on-the-loop, prompt-injection, review-harness, agents]
aliases: [AI 코드 리뷰, 리뷰 하네스, review harness, 기본 의심 리뷰어]
related: [verification-bottleneck, mergeability-gap, generator-evaluator-pattern, risk-proportional-human-review, named-human-accountability, prompt-injection, test-harness-vs-test-authoring, code-knowledge-graph, production-trace-eval-flywheel, harness-engineering, trusted-throughput]
first-seen: tech-bridge-death-of-code-review
sources: [tech-bridge-death-of-code-review]
created: 2026-10-03
updated: 2026-10-03
---

# 자동 코드 리뷰

**PR 리뷰를 사람 대신 모델·에이전트가 수행하는 것, 그리고 그것을 "더 똑똑한 리뷰어 하나"가 아니라 사람이 설계한 시스템(리뷰 하네스)으로 만드는 일.** [[laurie-voss|Laurie Voss]]가 [[tech-bridge-death-of-code-review]]에서 업계 현황을 정리하며 내린 결론은 *"review didn't disappear (…) it got rebuilt as a system and that system is built by humans"*(18:17~18:25)이다.

## 현장 규모 (화자 진술, 벤더 수치)

- GitHub Copilot 리뷰어: 리뷰 6천만 건, GitHub 전체 코드 리뷰의 *"more than one in five"*(11:02~11:10) — *"machine review of pull requests is the mainstream default"*.
- CodeRabbit: PR 1,300만+(13:43~13:47). Greptile: 저장소 전체 그래프(13:48~13:56). Graphite: 자기 제안의 수락/거절로 eval 세트(13:56~14:03).
- [[cursor|Cursor]]: 리뷰어 아키텍처를 공개(11:24~11:30).

## 설계에서 반복되는 교훈

| 교훈 | 내용 | en-orig |
|---|---|---|
| **오탐이 리뷰어를 죽인다** | 좋은 코드를 나쁘다고 플래그하는 리뷰어는 *"is going to get ignored"*. Cursor 1세대는 diff마다 **8패스**, 리뷰어 **순서 셔플**(순서가 결과를 바꿨다) — 목적은 오탐 필터 | 11:32~12:00 |
| **다중 패스 + 합의** | 베이징대 연구: 여러 패스를 돌리고 **합의한 것만** 남기면 리뷰 품질 *"up to 44%"*. *"The multipass trick keeps getting rediscovered"* | 12:05~12:24 |
| **에이전트형 리뷰어** | Cursor 재구축: 모델이 diff를 추론하고 도구를 부르고 *"decides where to dig"* | 12:26~12:34 |
| ⭐ **기본 의심** | 모델은 *"that looks good to me so ship it"* — 사람과 똑같이. *"don't trust the code by default. Assume there is something wrong with it."* → *"it is about being suspicious by default"* | 12:36~12:58 |
| **리뷰 + 수정 융합** | 리뷰어가 발견에서 **수정 에이전트**를 띄워 diff를 돌려준다. 다음 단계는 리뷰어가 **코드를 실행해 버그 보고를 증명**. *"the line between reviewing and rewriting is getting very thin"* | 13:04~13:33 |
| **리뷰를 리뷰하는 루프** | [[codex\|Codex]]가 자기 변경을 리뷰하고 더 많은 에이전트가 그 리뷰를 리뷰, *"until every agent reviewer is satisfied"*. 변경마다 앱을 부팅·UI 확인, 로깅 스택 노출 | 17:23~17:48 |

→ 기본 의심은 [[generator-evaluator-pattern]]의 *평가자는 생성자와 다르게 튜닝한다* 와 같은 결론. 다중 패스·합의는 [[agent-swarm]]의 검증 쪽 사용.

## 성공 지표 — "사람이 수락하는가"

> *"all of them are using the same metric as their definition of success which is is a human accepting my answer"* (14:06~14:14)

Cursor는 이를 **resolution rate**라 부르고 52% → 70%+로 올렸다(14:15~14:22). *"They are training their harnesses to get better at the definition of good as defined by human acceptance"*(14:26~14:33). → [[mergeability-gap]]: 모델 학습이 따라갈 길을 하네스가 먼저 간다.

> ⚠️ **위키의 표시 — 수락률은 Goodhart 대상이다.** 같은 발표의 프롬프트 인젝션 연구(아래)가 보여 주듯 **사람도 속는다**(35%). 수락률을 최적화하는 리뷰어는 *사람이 받아들이기 쉬운* 방향으로 갈 수 있다. [[trusted-throughput]]의 *"대시보드는 연기 감지기"* 경고와 같은 자리. Voss는 이 긴장을 짚지 않는다.

## 사람은 어디에 남는가

**in the loop가 아니라 on the loop.** Nicholas Carlini의 C 컴파일러 실험(에이전트 16개, 약 2,000 세션)은 *"no human in the loop"* 였지만 *"there was absolutely a human on the loop"* — 리뷰·검사 시스템, 테스트 하네스, 피드백 시스템을 사람이 썼다(15:07~15:32). → [[test-harness-vs-test-authoring]]

사람 체크포인트가 살아남는 세 자리(19:42~20:08): **싸게 검증할 수 없는 곳**, **폭발 반경이 큰 곳**(보안 민감 환경), **누군가 이름을 걸어야 하는 곳**. → [[risk-proportional-human-review]] · [[named-human-accountability]]

역할은 *"from inspecting the code directly to designing and tuning the systems that inspect the code and designing the definition of good"*(20:13~20:22)으로 올라간다. 처방: *"stop reviewing PRs. Um, it is the wrong level of abstraction for 2026"*(23:19~23:25), *"building uh a reliable review harness. Codify your definitions of good, your company context, your domain knowledge"*(23:34~23:43).

## 취약점 — 리뷰어는 설득당한다

- [[anthropic|Anthropic]] 자동 보안 리뷰어 README: *"not hardened against prompt injection attacks uh and should only be re used to review trusted PRs"*(20:39~20:47) — 리뷰 대상이 리뷰어를 설득해 발견을 철회시킬 수 있다.
- 3월 연구(이름 미발화): 무해한 커밋 메시지로 포장한 취약 코드가 자동 리뷰 에이전트를 **88%** 속였다, 사람은 **35%**(20:59~21:12). *"you don't just lose a reviewer, you lose the thing that was hard to fool"*(21:15~21:19).
- 그리고 *"confidently framed bad code is exactly the kind of code that agents are very good at producing"*(21:24~21:28).

→ [[prompt-injection]] — PR 본문·커밋 메시지·코드 주석이 **리뷰어의 입력**이 되는 순간, 리뷰 대상이 곧 공격 벡터다.

## 마지막 리뷰어 — 프로덕션

*"once the premerge review is all machines, watching what the code actually does becomes the last reviewer standing"*(21:55~22:00) — 테스트 결과가 아니라 **궤적**. → [[production-trace-eval-flywheel]]

## ⚠️ 유보

- **모든 수치가 벤더 발표 또는 화자의 2차 인용**이다(Copilot 6천만, CodeRabbit 1,300만, Cursor 52→70%, 베이징대 44%, 88% vs 35%).
- 화자는 Arize(관측 플랫폼) 소속 — *"I'm not going to give a pitch for Arise here"*(22:13~22:15)라 했지만, 결론(프로덕션이 마지막 리뷰어)은 소속 회사의 시장과 겹친다.
- 한 소스. 다중 패스·기본 의심의 효과를 독립 측정한 소스는 아직 없다.

## References

- [[tech-bridge-death-of-code-review]] · [[laurie-voss]]
- 관련: [[mergeability-gap]] · [[verification-bottleneck]] · [[generator-evaluator-pattern]] · [[risk-proportional-human-review]] · [[prompt-injection]] · [[cursor]] · [[codex]] · [[code-knowledge-graph]]

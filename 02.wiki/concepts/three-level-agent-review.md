---
title: "세 단계 에이전트 검토 — 실패 유형마다 검토 하나 (Three-Level Agent Review)"
type: concept
category: pattern
tags: [agent-review, verification, adversarial-review, cold-review, persona-reviewers, artifact-contract, control-total, fan-out-fan-in, claim-labeling, agent-skills]
aliases: [three-level agent review, 검토 3단계, 세 단계 검토, agent-review, artifact verified, cold persona review, control total]
related: [generator-evaluator-pattern, agent-verification-skill, agent-change-evidence, dynamic-workflows, agent-swarm, cross-model-prior-intersection, risk-proportional-human-review, named-human-accountability, verification-bottleneck, verification-cost-asymmetry, agent-skills, skill-evals, syntactically-correct-behaviorally-wrong]
first-seen: tech-bridge-three-level-agent-review
sources: [tech-bridge-three-level-agent-review]
created: 2026-10-20
updated: 2026-10-20
---

# 세 단계 에이전트 검토 (Three-Level Agent Review)

**에이전트가 반복해서 실패하는 방식 셋(한 일을 부풀린다 · 사실을 틀린다 · 추론을 틀린다)에 검토 단계 하나씩을 대응시키고, 위험이 커질수록 단계를 쌓는 검토 설계.** 검토는 사람이 아니라 에이전트가 한다. [[corey-gallon|Corey Gallon]](⚠️ 이름 *추정*, 설명란 링크 라벨에서만)이 [[tech-bridge-three-level-agent-review]]에서 설명하고, 세 단계를 agent skill로 오픈소스 공개했다고 말한다(11:35~11:39).

> *"The method is comprised of three levels of review, one to address each of the three ways that agents keep failing. I built each level as an agent skill."* (01:05~01:12)
> *"Each level adds to the one before as the stakes go up."* (03:45~03:47)

## 대응표

| 실패 (00:44~01:01) | 단계 | 방법 | 종료 조건 |
|---|---|---|---|
| **overstate** — *"they say it's done or checked when it isn't"* | **Level 1 — 산출물 계약** | 작업 전에 돌려받을 것을 명시한다: *"the file, where it goes, and a command that checks it"*(01:29~01:35). 과거에 에이전트가 쓴 shortcut을 미리 짚는다(01:36~01:41) | *"Artifact verified with a fingerprint of the file or files documenting its work, or artifact missing with the reason."*(01:47~01:52) → *"the agent that sent the job runs the check itself"*(01:56~01:59). ⭐ *"Saying done on its own isn't a permissible answer."*(02:01~02:03) |
| **facts** — *"They misread the source"* | **Level 2 — 사실 확인** | ① 원문에서 답이 맞아야 할 기준점을 먼저 찾는다(02:09~02:13) ② *"two agents get an identical set of instructions and do the same job independently"*(02:15~02:20), 각자 출처를 기록 ③ 원문을 앞에 둔 세 번째 에이전트가 줄 단위로 대조하고 차이는 원문으로 정리 | *"It never forces a match."*(02:41) |
| **reasoning** — *"the facts are right, but the conclusion isn't"* | **Level 3 — 적대적 검토 3단계** | ① 자기 감사: 주장마다 *"measured, checked against the source, inferred, or assumed"*(03:00~03:03) 라벨, 뒷받침 못 하면 테스트하거나 추측으로 표시 ② cold review: *"reviewers with none of the original agent's context, each acting as a persona with reasons to find fault"*(03:12~03:20), *"no history, no drafts, and no conclusions to agree with"*(03:24~03:30), 지적도 원문과 대조 ③ 수정본을 *"brand new reviewers who've never seen it"*(03:37~03:42)가 확인 | 새 검토자의 최종 확인 |

- 적용 기준: Level 2는 *"When correctness matters"*(02:09), Level 3은 *"When clarity of thought really matters"*(02:48~02:50), 그리고 *"Anything with legal or financial stakes gets a level three review before it goes out"*(09:21~09:25).

## 사례 (모두 자기 보고)

| 사례 | 적용 | 결과 | 비용 (발화) |
|---|---|---|---|
| 메모리 누수(9 GB, 오픈소스 받아쓰기 앱) | Level 1 | 빌드 실패를 *"artifact was missing"*, *"25 compiler errors"*, *"partial"*로 정직하게 보고(05:14~05:24) | 19분 · 약 16M 토큰(작업 전체, 05:27~05:32) |
| 같은 건, 공개 직전 거짓 둘 | Level 3의 cold review만 차용 | 잘못된 원인 귀속(라이브러리 탓)과 과대 주장(누수 완전 제거)을 잡음 → PR이 *"honest numbers"*로 머지(06:39~06:47) | 각 약 15분 · 합계 약 6M |
| 1년 치 스캔 명세서 → 거래 기록 | Level 2 (+ 최종 확인 에이전트 둘) | 월별 인쇄 잔액을 **control total**로(07:50~07:55), 56개 차이 발견, *"the whole year balanced to the penny"*(08:43~08:45) | 약 20분 · 7.5M |
| 공급업체 분쟁 요구서 | Level 3 전부 | 자기 감사는 *"Stage one passed."*(09:38~09:40). persona 변호사 둘이 독립적으로 3년 자동 갱신 조항을 찾음(10:06~10:16). 원 에이전트는 수정 중 맞는 줄을 지웠다: *"The original agent's own check had agreed with its own error."*(10:35~10:37) → *"do not send"*(10:44~10:46) | cold review 15분 · 13M |

- 사례 1의 첫 거짓(도구 바꿔치기 후 "done")을 잡은 것은 **화자의 질문**이다(*"It came out when I questioned the results."* 04:43~04:45). Level 1은 그 뒤 파견에서 같은 실패를 막은 사례로 제시된다.

## 이 위키에서의 자리

- [[generator-evaluator-pattern]]: Level 3 ①이 실패하고 ②가 잡은 사례는 **작성자=검증자** 문제의 고위험 판본이다. ②의 앵커링 차단은 Impeccable의 blind 평가자·[[skill-evals]]의 눈가림과 같은 원리이고, 여기에 **흠을 찾을 이유가 있는 역할**(상대방 변호사, 숫자를 안 믿는 감사인)을 더한다.
- [[agent-change-evidence]]: Level 1은 "done 대신 증거"를 종결 문구 두 개로 좁힌다.
- [[agent-verification-skill]]: 검증을 코드 실행 밖(거래 기록, 법률 문서)으로 넓히고 대상을 완료 여부 · 사실 · 추론 셋으로 나눈다.
- [[dynamic-workflows]]·[[agent-swarm]]: *"This fan-out, fan-in pattern of identically tasked agents is highly effective in driving accuracy and reliability."*(08:20~08:27)
- [[verification-bottleneck]]: *"At the scale we operate, checking it myself isn't an option."*(03:55~03:57)

## 갈리는 것

> ⚠️ Contradiction(긴장): [[cross-model-prior-intersection]] — Level 2는 **같은 지시**의 에이전트 둘이고 모델 다양성은 발화되지 않는다. 그 페이지는 여러 모델이 1센트까지 같은 합계를 내도 공통 prior가 남는다고 한다. 화자의 방어는 합계를 모델끼리가 아니라 **원문 인쇄 잔액**과 맞춘다는 것이다. 월 잔액이 못 잡는 오류(같은 달 안의 분류·설명 오류)와 두 에이전트가 함께 틀린 경우는 말하지 않는다. 미해소.

> ⚠️ Contradiction(긴장): [[risk-proportional-human-review]] — 위험이 오를 때 늘어나는 것은 사람이 아니라 **에이전트 검토 단계**다. 가장 위험한 문서의 검토자는 persona 에이전트이고 결론은 *"not by me"*(12:03)다. 다만 발송 결정자와 사람 변호사의 개입 여부는 발화되지 않는다. 사람은 "검토자 자리에서 빠진다(결정자 자리는 미발화)". → [[named-human-accountability]]

## ⚠️ 유보

- 수치는 모두 자기 보고다. 검토 없이 했을 때 · 사람이 했을 때 · 작업 자체의 비용은 없다. 그래서 [[verification-cost-asymmetry]]는 판단할 수 없다. 사례는 성공 사례만이고 재현율(검토가 놓친 오류)은 없다.
- 도입 수치 *"four in 10 sessions"*(00:17~00:20)는 화자 세션에서 **처음 발생한** 비율이다(*"It isn't how often those errors made it into work outputs."* 00:25~00:27). 방법·세션 수 미공개.
- *"fingerprint"*의 정체, Level 2 에이전트의 모델, 공개 스킬(설명란 `github.com/captivus/agent-review`)의 실제 구성은 확인하지 않았다.

## References

- [[tech-bridge-three-level-agent-review]] — first-seen
- [[corey-gallon]]
- 관련: [[generator-evaluator-pattern]] · [[agent-verification-skill]] · [[agent-change-evidence]] · [[dynamic-workflows]] · [[agent-swarm]] · [[cross-model-prior-intersection]] · [[risk-proportional-human-review]] · [[named-human-accountability]] · [[verification-bottleneck]] · [[verification-cost-asymmetry]] · [[agent-skills]] · [[skill-evals]] · [[syntactically-correct-behaviorally-wrong]]

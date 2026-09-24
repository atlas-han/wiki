---
title: 파일 시스템 에이전트 (File System Agent)
type: concept
category: pattern
tags: [agents, tools, context, sandbox, claude-code, emergent-behavior]
aliases: [파일 시스템 에이전트, file-system agent, 최소 도구 세트]
related: [agent-tool-design-practices, agent-knowledge-sourcing, context-engineering, agent-harness-design, claude-code, build-time-vs-runtime-tools, files-vs-database-agent-memory]
first-seen: tech-bridge-vercel-eve-filesystem-agent
sources: [tech-bridge-vercel-eve-filesystem-agent, tech-bridge-bm25-agentic-search, tech-bridge-oracle-agent-memory-harness]
created: 2026-09-19
updated: 2026-09-24
---

# 파일 시스템 에이전트

**전용 도구를 정교하게 깎는 대신, 모델이 이미 잘 훈련된 범용 도구(list · read · bash · grep · write)를 주고 지식을 파일 시스템에 부어 놓은 뒤 에이전트가 스스로 탐색하게 하는 설계.** [[tech-bridge-vercel-eve-filesystem-agent]]에서 [[andrew-qu|Andrew Qu]]가 **[[claude-code|Claude Code]]와 [[claude-opus-4-5|Opus 4.5]]를 보고 배웠다**고 말하며 이 위키에 들어왔다.

## 발견의 경위 — 세 번 실패한 뒤에

[[vercel|Vercel]] 팀은 [[agent-architecture-progression|세 번의 아키텍처]]를 거쳐 eval 30%에서 막혀 있었고, 예상 못 한 질문마다 시나리오를 손으로 까는 것이 확장 불가라고 판정한 상태였다. 그때 다른 물건을 보고 격차를 느낀다.

> 우리는 옆에서 **"와, [Claude Code]와 [Opus] 4.5는 우리가 이전에 가지고 있던 것과 비교하면 거의 인공 일반 지능(AGI)이나 다름없네."** 라고 생각했습니다. 우리가 직접 개발한 에이전트와는 달리, **이 에이전트는 거의 모든 질문에 막힘없이 답해줬습니다.** (07:38~07:53)

## 무엇이 달랐는가

> 우리가 무엇을 잘못했는지 … 생각해 보니, **핵심은 바로 파일 시스템이었다**는 것을 깨달았습니다. **최소한의 도구 세트, 즉 파일 목록 보기, 파일 읽기, bash 실행 정도만** 제공했고, 우리 데이터 에이전트 사용 사례에 맞춰 몇 가지 도구를 더 추가했습니다. (07:53~08:11)

> 하지만 가장 중요한 것은 **에이전트가 잘 훈련된 도구를 활용할 수 있었고 필요한 곳에 스스로 탐색하고 작업을 작성할 수 있었다**는 점입니다. **[Claude Code]에 매우 구체적인 도구 세트를 제공하지 않았습니다.** 마치 **자유롭게 탐색하고 새로운 행동(emergent behavior)을 발견하도록 내버려 둔 것**과 같았습니다. (08:11~08:28)

두 개의 주장이 겹쳐 있다:

| 주장 | 내용 |
|---|---|
| **도구 쪽** | 모델은 `ls`·`cat`·`bash`·`grep`에 **이미 훈련되어 있다.** 새 도구를 가르치는 것보다 아는 도구를 주는 편이 낫다 |
| **바닥 쪽** | 지식을 **API 뒤가 아니라 파일로** 두면 에이전트가 **설계자가 예상하지 못한 경로**로 접근할 수 있다 |

두 번째가 첫 배포 실패의 직접적 해독제다 — *예상 못 한 질문* 이 문제였는데, **예상하지 않아도 되는 구조**로 바꾼 것이다.

## 구현

> **샌드박스에는 전체 시맨틱 레이어가 저장됩니다.** 에이전트는 **grep, bash, 파일 읽기, 파일 쓰기** 등을 통해 필요한 것을 파악할 수 있습니다. 그리고 **Vercel에 특화된 기능**을 수행할 수 있도록 몇 가지 도구를 추가했습니다. (08:28~09:04)

> 아주 간단하죠. **bash 도구만 제공하면 됩니다.** npm에 **bash tool**이라는 유용한 헬퍼가 있습니다. 그리고 이 도구를 **샌드박스**에 연결하면 됩니다. (09:22~09:43)

**결과**: *"평가 점수가 두 배로 올랐다"*(09:22). ⚠️ eval의 실체(과제 수·채점자·기준)는 없다.

그리고 화자가 도약을 두 단계로 센다 — **단일 에이전트 → [Claude Code] SDK → 우리 용례에 맞춘 파일 시스템 에이전트**(09:04~09:09). 즉 남의 SDK를 그대로 쓰는 단계와 **자기 바닥을 깔아 재구성하는 단계**가 다르다.

## 이 위키의 [[agent-tool-design-practices]]와의 각도

**모순이 아니라 층이 다르다.**

| | 09-10 [[google-cloud\|Google Cloud]] ([[agent-tool-design-practices]]) | 이 패턴 |
|---|---|---|
| 도구 | **좁히고 결과 중심으로** 설계 | **넓히고 범용으로**, 모델이 아는 것 |
| 앞에 있는 사람 | **프로덕션 최종 사용자** | **사내 신뢰 사용자** |
| 시간대 | 런타임 ([[build-time-vs-runtime-tools]]) | 탐색·분석 |
| 위험 | 유출·권한 오용 | (소스가 다루지 않음) |

09-10 소스가 세운 축이 정확히 여기 적용된다 — **빌드타임 도구를 프로덕션에 두면 안 된다**는 경고의 반대편에서, **탐색용 도구는 좁히면 안 된다**는 주장이 나온 셈이다. 두 소스는 서로를 모른다.

## ⚠️ 유보

- **보안이 통째로 비어 있다.** 시맨틱 레이어 전체를 샌드박스에 붓고 bash를 주는 구조인데 [[prompt-injection]]·[[lethal-trifecta]]·[[agent-identity-separation]]·데이터 접근 범위를 **한 번도 언급하지 않는다.** 09-10·09-11 소스들이 세운 논점이 전부 열려 있다.
- **"잘 훈련된 도구"의 범위**가 정의되지 않는다 — 어떤 도구가 모델에게 친숙한지 판정하는 기준이 없다.
- **파일 시스템에 무엇을 어떻게 놓을지**가 없다. 시맨틱 레이어를 *"통째로 부었다"* 뿐이고, 구조·크기·갱신 주기가 없다.
- 이 패턴이 **탐색적 질의 이외의 작업**(쓰기·트랜잭션·되돌릴 수 없는 조치)에도 통하는지 소스가 말하지 않는다. → [[action-reversibility]]

## ⭐ 2026-09-20 — 이틀 만에 같은 구조가 검색 도메인에서, 이번엔 논문으로

[[tech-bridge-bm25-agentic-search]]가 [[jimmy-lin|워털루 지미 린 그룹]]의 논문 *"동적 작업 공간 확장을 통한 직접적인 코퍼스 상호 작용 확장"* 을 인용한다. **검색 결과를 컨텍스트에 밀어 넣는 대신 파일 시스템 워크스페이스에 펼쳐 놓고 `grep`·`ripgrep`·`sed`·`awk`로 파고들게 한다.** → [[corpus-as-filesystem-workspace]]

| | **이 페이지** ([[vercel\|Vercel]], 09-19) | [[corpus-as-filesystem-workspace]] (09-20) |
|---|---|---|
| 출처 | **제품** — 세 번 실패하고 도달 | **논문** |
| 무엇이 놓이나 | 회사의 **지식·컨텍스트** | **검색 결과** |
| 언제 채워지나 | 미리 | **쿼리마다** — *동적* 확장 |
| 도구 | `grep`·bash | **같다** |

**핵심 차이는 워크스페이스가 정적이냐 동적이냐다.**

그리고 [[jo-bergum|Bergum]]이 **이 위키가 관측만 하고 이유를 대지 못했던 것에 설명을 붙인다** — 파일 시스템이 본질적으로 우월해서가 아니라, *"모든 최첨단 LLM 기업들이 코딩, Bash, 도구 사용에 맞춰 모델을 최적화하고 있기 때문"* 이고 그래서 *"새로운 모델이 나올 때마다 더 나은 성능을 보여줄 거라는 걸 알 수 있다"*(14:01~14:22). **화자 스스로 이것을 "편법(hack)"이라 부른다.** → [[ride-the-optimization-trajectory]]

⚠️ **그리고 이 페이지에서 기록한 보안 공백이 그대로 재발한다.** 저쪽은 **신뢰할 수 없는 웹 문서**를 작업 공간에 놓고 bash를 붙이는 구조인데 [[prompt-injection]]·[[lethal-trifecta]]를 **한 번도 언급하지 않는다.** 이틀 연속 같은 공백이다.

## References

- [[tech-bridge-vercel-eve-filesystem-agent]] — first-seen
- [[andrew-qu]] · [[vercel]] · [[claude-code]] · [[claude-opus-4-5]] · [[claude-agent-sdk]]
- 관련: [[agent-architecture-progression]] · [[agent-tool-design-practices]] · [[agent-knowledge-sourcing]] · [[context-engineering]] · [[agent-harness-design]] · [[query-to-skill-distillation]] · [[build-time-vs-runtime-tools]]

## 2026-09-24 — 같은 출발점, 반대 방향: 파일은 모델의 본능이지만 동시 쓰기에 약하다

[[tech-bridge-oracle-agent-memory-harness]]([[ignacio-martinez|Ignacio Martinez]] / [[oracle|Oracle]])가 이 페이지와 **같은 관찰**에서 출발한다 — 파일은 *"모델의 본능에 맞는다"*(en-orig 13:46), *"모델들이 즐겨 찾는다"*(14:18~14:20), POSIX라 어디서나 돈다. 그러나 결론은 **파일을 DB 위에 올려라(DBFS)** 다 — 파일에는 **트랜잭션 일관성·백업·하이브리드 검색**이 없고, *8·16·32개 에이전트*가 같은 파일을 동시에 쓰면 깨진다(14:36~15:57). → [[files-vs-database-agent-memory]]

두 소스를 겹치면 경계선이 보인다(⚠️ 위키의 읽기): **읽기 중심·단일 에이전트면 파일 시스템이 이긴다(Vercel), 동시 쓰기·장기 보존이면 파일만으로는 모자란다(Oracle).** 이 페이지의 샌드박스는 **읽기 위주의 시맨틱 레이어**였고, 쓰기 경합은 다루지 않았다. ⚠️ Oracle 쪽은 DB 벤더, Vercel 쪽은 자기 프레임워크 — **둘 다 당사자**다.

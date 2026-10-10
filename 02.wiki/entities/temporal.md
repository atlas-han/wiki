---
title: Temporal
type: entity
category: org
tags: [durable-execution, workflow-engine, open-source, distributed-systems, human-in-the-loop, vendor]
aliases: [Temporal, Temporal Technologies, temporal.io, 템포럴]
links:
  - "https://temporal.io"
  - "https://github.com/temporalio/temporal"
sources: [tech-bridge-human-is-async-api]
created: 2026-10-10
updated: 2026-10-10
---

# Temporal

**durable execution 플랫폼을 만드는 회사이자 그 오픈소스 소프트웨어.** 코드를 worker · workflow · activity 세 primitive로 나눠 상태와 실패 처리를 플랫폼이 맡게 한다. 이 위키에는 [[tech-bridge-human-is-async-api]](2026-10-09 업로드)에서 처음 들어왔다 — Temporal 직원(설명란 기준 Melanie Warrick)이 **에이전트의 human-in-the-loop를 Temporal primitive로 구현하는** 발표를 했다.

> ⚠️ 아래 서술은 거의 전부 **당사자 진술**이다 — 화자 스스로 *"you're going to hear me pitching about the company that I work for"*(00:13~00:19). 벤치마크·고객 사례는 없다.

## 자기 서술 (그 소스 기준)

| 항목 | 내용 | en-orig |
|---|---|---|
| 하는 일 | *"standardize your fa failure handling and your state management in your system any system any distributed system especially any systems with agents"* | 05:34~05:46 |
| 형태 | *"we're software and we're also a service"* — 오픈소스(self-host) + 유료 관리형 서비스 | 05:46~05:51 · 06:55~07:08 |
| 언어 | *"Python or TypeScript or Rust"* (전체 목록 아님) | 06:00~06:05 |
| primitive | worker(코드 실행) · workflow(단계 추적, 결정론적) · activity(외부 상호작용 — 모델·도구 호출, 비결정론적) | 06:13~06:49 · 12:25~12:30 |
| 사람 입력 | wait condition(workflow를 멈춰 park) + signal(실행 중 workflow에 입력 주입) · timeout | 07:55~09:06 |
| 복구 | worker가 죽어도 이벤트 로그를 replay — *"It's not redone. It's just replayed"* | 15:50~16:03 |
| 확장성 | *"millions of workflows out there parked"* (⚠️ 근거 미발화) | 09:01~09:06 |
| 프레임워크 | *"We are framework agnostic."* — Google ADK 통합(TemporalModel·activity tool·ADK plugin), LangGraph 통합(노드별, interrupt → wait condition/signal, LangGraph plugin) | 10:08~10:44 · 11:43~12:32 |
| UI | event history와 parent/child workflow를 보여 주는 웹 UI | 01:28~01:44 · 13:51~14:00 |

개념 정리는 [[durable-execution]], 사람 입력 패턴은 [[human-as-async-api]].

## 이 위키에서의 자리

- **[[agent-distributed-systems]]가 요구한 것의 상용 구현 하나** — 그 페이지는 *"에이전트가 부작용을 내는 순간 분산 시스템 문제"* 라며 상태 불명·재시도·보상·관측을 요구했고, Temporal은 그것을 **실행 모델**(workflow의 이벤트 히스토리 + activity 재시도)로 흡수한다고 주장한다.
- **프레임워크가 아니라 그 아래 층** — ADK·LangGraph 같은 에이전트 프레임워크를 *대체* 하지 않고 **감싼다**(모델 호출·도구 호출을 activity로). [[langchain]] · [[google-cloud|Google ADK]] 와 경쟁이 아니라 통합 관계로 소개됐다.
- ⚠️ **용어 충돌** — Temporal의 *workflow* 는 [[workflow-vs-agent]]의 *workflow*(미리 정해진 경로)와 다르다. → [[durable-execution]]

## References

- [[tech-bridge-human-is-async-api]] — first-seen (직원 발표, 2026-10-09 업로드)
- [[durable-execution]] · [[human-as-async-api]] · [[agent-distributed-systems]] · [[langchain]] · [[google-cloud]]
- 외부: <https://temporal.io> · <https://github.com/temporalio/temporal> (⚠️ 이 위키는 열어 보지 않았다)

---
title: Greptile
type: entity
category: org
tags: [automated-code-review, review-agent, codebase-context, vendor, living-wiki, computer-use]
aliases: [Greptile]
links:
  - https://www.greptile.com/
sources: [tech-bridge-greptile-daksh-gupta-build-review-agent, tech-bridge-death-of-code-review, tech-bridge-gitar-agentic-pr-validation]
created: 2026-11-04
updated: 2026-11-04
---

# Greptile

AI 코드 리뷰 · 검증 제품 회사. 이 위키에서는 10-02 [[tech-bridge-death-of-code-review]]의 업계 목록에 한 줄로 처음 나오고, [[tech-bridge-greptile-daksh-gupta-build-review-agent]](2026-11-03 업로드)에서 공동창업자 [[daksh-gupta|Daksh Gupta]](설명란 근거)가 자기 회사 방식을 직접 말한다.

> ⚠️ **아래는 전부 당사자 발화(또는 다른 발표자의 한 줄 소개)다.** 위키는 Greptile 사이트(설명란 링크 https://www.greptile.com/ )를 열어 보지 않았다. 이 영상의 회사 이름은 설명란 · 태그에 정확히 있고, 발화에서는 ASR이 *"Reptile"* · *"Grapple"* · *"graviles"* 로 뭉갰다.

## 소스에서 확인되는 것

| 항목 | 내용 (출처 [[tech-bridge-greptile-daksh-gupta-build-review-agent]]) |
|---|---|
| **출발** | 코드 검증 이전에 대규모 코드베이스 맥락 · RAG를 했다 — *"Before we were doing code validation, we were doing codebase context."*(08:29~08:32) |
| **평가 코퍼스** | *"we actually have a lot of code from a lot of different companies and we can test across a very, very large corpus of pull requests"*(06:16~06:22) ⚠️ 고객 동의 · 범위 미발화 |
| **맥락** | 내부 지식 베이스 → *"a living wiki"*(11:17~11:19), *"a sort of world model of how your company works."*(11:19~11:23) — 코드 · 프로덕션 텔레메트리 · 로그 · 문서 · 티켓. → [[context-engine]] |
| **자율 테스트** | *"dependency rich sandboxes which are completely configurable virtual machines"*(12:15~12:19) + computer use로 끝에서 끝까지 시험(12:28). → [[agent-visual-qa]] |
| **도입 지원** | *"a team of forward deployed engineers"*(12:51~12:52) |
| **모델 배분** | *"about 20% frontier models for the most critical tasks."*(13:42~13:45) 하위 작업 20개, 모델 조합을 고치는 작은 연구 팀(14:13~14:21). → [[model-mixing-economics]] |
| **수치 주장** | 치명적 버그 1/1000(단위가 PR · 줄로 흔들림), 모델 뒤집기 10%, Claude · GPT 버그 유형 차이 → [[review-model-inversion]] |

## 다른 소스에서

- 10-02 [[tech-bridge-death-of-code-review]]: [[laurie-voss|Laurie Voss]]가 **저장소 전체 그래프로 먼 코드에 닿는 변경을 보는** 제품으로 소개한다(13:48~13:56). → [[automated-code-review]] · [[code-knowledge-graph]]. ⚠️ 이번 영상의 발표자는 "graph"가 아니라 knowledge base · wiki라고 말한다. 내부 구조가 같은지는 미확인이다.
- 10-13 [[tech-bridge-gitar-agentic-pr-validation]]: 위키 쪽 비교에서 업계 목록의 한 이름으로만 나온다.

## ⚠️ 유보

- 고객 수 · 가격 · 설립 연도 · 투자 정보는 소스에 없다.
- 주장의 근거가 자사 데이터뿐이고 벤치마크 · 공개 논문 링크가 없다.

## References

- [[tech-bridge-greptile-daksh-gupta-build-review-agent]] · [[daksh-gupta]] · [[automated-code-review]] · [[tech-bridge-death-of-code-review]]

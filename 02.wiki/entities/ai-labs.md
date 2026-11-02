---
title: AI Labs
type: entity
category: org
tags: [youtube, ai-engineering, content, agent-skills]
links:
  - https://ailabspro.io/
sources: [tech-bridge-six-agent-skills, tech-bridge-graft-code-knowledge-graph, tech-bridge-ai-labs-claude-code-verification-review-loop]
created: 2026-09-05
updated: 2026-11-02
---

# AI Labs

[[agent-skills|에이전트 스킬]]과 AI 코딩 워크플로를 다루는 영상 제작 주체. [[tech-bridge|Tech Bridge]]가 자막을 입혀 재배포한 [[tech-bridge-six-agent-skills]]의 원 제작자다.

## 위키에서 알려진 사실

- 자기 소개는 소스 안에 직접 나온다 — *"We're a software company and **this is AI labs**"*(00:37). 즉 **콘텐츠 채널이자 소프트웨어 회사**로 자신을 규정한다.
- 채널 설명란이 `ailabspro.io`를 링크한다.
- 제작 관행이 소스에서 드러난다 — 영상 애니메이션 제작에 **자체 스킬**을 쓰고 브랜드 로고를 SVG로 넣는다. 그 스킬에서 나온 실패가 [[skill-self-improvement|task-observer]]의 실사례로 소개된다.
- 데모 스택: **Next.js + Supabase**. 앱 디자인은 *"보통 간단한 HTML 페이지부터 시작"* 한다고 밝힌다.
- 개발 관행: 맥의 **개발자 폴더 하나**에 모든 프로젝트를 두고 그 폴더의 `CLAUDE.md`로 공통 규칙을 상속시킨다 → [[llm-coding-guidelines]].
- 과거에 "Hallmark 디자인 스킬"을 다룬 적이 있다고 언급한다(⚠️ 정식 표기 미확정).

## 미해결 사항

- ⚠️ **발표자 개인 이름이 소스 어디에도 없다.** 영상 내내 1인칭 복수("we")로만 말한다.
- 회사의 규모·소재지·설립 시점 미확인.
- 채널과 소프트웨어 사업의 관계(콘텐츠가 본업인지 부수인지) 미확인.


## 2026-09-15 — 두 번째 소스

[[tech-bridge-graft-code-knowledge-graph]]가 이 제작자의 두 번째 소스다(첫 번째는 2026-09-05 [[tech-bridge-six-agent-skills]]).

- **관행이 일관된다** — `CLAUDE.md` 템플릿을 **자사 커뮤니티 AI Labs Pro에 올려 두고** 그것으로 작업을 시작한다. PRD를 먼저 쓰고, 템플릿의 빈 곳을 PRD로 채우게 한 뒤 모델을 바꾼다.
- **모델 운용**: [[fable-5-1|Fable 5.1]]을 쓸 때 *"혼자 일하고 있다는 걸 명시적으로 말해 줘야 한다"* 며 *"멈추고 허락을 구하지 말라"* 고 지시한다. **이전 Fable 5.1 영상**을 따로 언급한다(이 위키에 미수록).
- **제품 소개 방식**: 남의 도구([[graft|Graft]])를 소개하면서 **자기 수정판을 만들어 자사 커뮤니티에 올린다.** 즉 **콘텐츠가 커뮤니티 유입 경로**다.
- ⚠️ **발표자 개인 이름은 이 소스에도 없다** — 2026-09-05의 미해결 항목이 그대로다. 영상 내내 "we"로만 말한다.
- ⚠️ 영상 **제목이 자막에 없는 순위**(*"GitHub 1위 트렌딩"*)를 주장한다. → **채택하지 않는다.**

## References

- [[tech-bridge-six-agent-skills]]
- <https://ailabspro.io/>

## 2026-11-02 — 세 번째 소스: Anthropic 코드 리뷰 방식 해설 + 자기 구현 ([[tech-bridge-ai-labs-claude-code-verification-review-loop]])

- **귀속은 설명란 근거다.** 발화 · 태그에 "AI Labs"가 없고, 설명란 *"AI Labs가 앤트로픽 Claude Code 팀의 코드 검토 방식을 바탕으로 구성한"* 이 유일한 이름이다. 화법은 이전 두 편과 같은 1인칭 복수 — *"We've shown many ways to give Claude evals in our earlier videos."*(02:53~02:55). ⚠️ 발표자 개인 이름은 이번에도 없다.
- **형식이 바뀐다** — 남의 도구 소개(09-15 Graft)에서 **남의 프로세스(Anthropic 기사) 요약 + 단계마다 자기 스킬**로. *"Claude code's team mentions their own way to set up these checks, and we turned that into a skill."*(02:57~03:00) 설명란이 *"AI Labs가 제안한 구현과 앤트로픽 팀의 실제 프로세스는 구분해 설명합니다"* 라고 스스로 경계를 단다.
- **관행이 일관된다** — 기능별 `specs` 폴더와 요구사항 문서(ASR *"rd.md"*, PRD 계열 추정), 디자인은 목업(단순 웹 페이지)부터 — 09-05의 *"보통 간단한 HTML 페이지부터 시작"* 과 같다. CLAUDE.md를 규칙 허브로 쓰고 다른 파일(`review.md`)을 링크한다.
- 만든 스킬: write-eval · review-loop(orchestrator · builder · verifier · reviewer) · 위험 등급 · first-time user · fix-a-bug. → [[review-loop-termination]] · [[code-blind-first-user-test]]
- ⚠️ 스킬들의 효과 측정은 없다. 5라운드 상한의 근거는 *"each of our rounds does more work"*(11:14~11:16)뿐.

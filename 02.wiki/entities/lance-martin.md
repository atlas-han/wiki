---
title: Lance Martin
type: entity
category: person
tags: [anthropic, claude-platform, prompt-engineering, evals, managed-agents, ai-engineer]
aliases: [Lance Martin, 랜스 마틴, 렌스마틴]
links:
  - https://www.youtube.com/watch?v=ys6YQ2yfBpM
sources: [anthropic-managed-agents, tech-bridge-lance-martin-old-prompts-make-claude-worse]
created: 2026-11-09
updated: 2026-11-09
---

# Lance Martin

[[anthropic|Anthropic]] 소속(해설 · 영상 제목 근거). 이 위키에서는 두 번 나온다. 05-25 엔지니어링 글 [[anthropic-managed-agents]]의 공저자(Gabe Cemaj · Michael Cohen과 함께)이고, 11-08 [[tech-bridge-lance-martin-old-prompts-make-claude-worse]]에서 해설한 [[ai-engineer|AI Engineer]] 워크숍 *Your Old Prompts Are Making Claude Worse*(`ys6YQ2yfBpM`, 설명란)의 발표자다.

> ⚠️ **직함 · 팀은 발화되지 않는다.** 해설의 *"엔트로피[=Anthropic] 렌스마틴"*(00:35)과 제목 *(Anthropic Lance Martin)* 이 소속의 근거다. 워크숍 원본은 위키가 열지 않았고, 그의 말은 모두 한국어 해설자가 옮긴 것이다(본인 음성은 캡션에 없다).

## 해설이 전하는 주장 (2026-11-08 · 2차 전달)

- **프롬프트에도 빚이 쌓인다** — 옛 모델용 주문(*단계별로 생각해라* · *두 번 확인해라*)이 새 모델에선 비용을 올리고 성능을 깎는다. 처방은 `/claude-api prompt-audit` → [[prompt-debt]]
- 캐시 읽기는 기본 입력의 약 10분의 1 → [[prompt-caching]]
- 오를 수 있는 평가와 학습/시험 분할의 hill climbing, Claude API 스킬 66% → 87.9% → [[climbable-eval]]
- *똑똑한 모델을 덜 애쓰게* — *"맥스로 시작하지 말고 오퍼스 5.1 로우 부터"*(⚠️ 버전 ASR 미확정) → [[model-mixing-economics]]
- 작업 길이가 하루 이틀짜리로 들어섰고, 며칠짜리 에이전트에는 하네스 · 샌드박스 분리가 필요하다 → [[brain-hands-decoupling]] · [[managed-agents]]
- 팁 게시물 조회 29만 회 이상(해설 전달).

두 소스가 같은 사람이라는 판단은 **이름과 소속(Anthropic, Managed Agents 주제)이 같다는 것**에 근거한다(추정은 아니지만 직접 확인하지 않았다).

## References

- [[anthropic-managed-agents]] — 공저(2026-05-25)
- [[tech-bridge-lance-martin-old-prompts-make-claude-worse]] — 워크숍 해설(2026-11-09 ingest)

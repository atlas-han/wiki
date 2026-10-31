---
title: Addy Osmani
type: entity
category: person
tags: [anthropic, claude-code, software-factory, verification, code-review, accountability]
aliases: [Addy Osmani, 애디 오스마니, Addy]
links: []
sources: [tech-bridge-anthropic-30k-merges-verification]
created: 2026-10-31
updated: 2026-10-31
---

# Addy Osmani

[[anthropic|Anthropic]] 쪽 화자로 이 위키에 처음 등장한다([[tech-bridge-anthropic-30k-merges-verification]], 2026-10-30 업로드 대담). "software factory is harnessing loops at scale"이라는 정의를 만든 사람으로 소개된다(진행 쪽이 *"this is a quote from Addy"* 라고 읽는다, 00:45).

> **신원 근거 — 강함.** 발화 안에서 두 번 호명되고(*"Adi was talking about"* 07:11, ASR · *"the same point of view, Addy"* 09:10) 제목 · 설명란에도 이름이 있다. **소속은 본인 1인칭 발화**다: *"at Anthropic, like we we think about this a little bit differently"*(08:42~08:45), *"we were merging about 2,500 changes all the way back in May"*(03:50~03:53). 진행 쪽은 *"the Claude Code team that you're working with"*(03:48~03:49)라고 묻는다. ⚠️ 직함 · 입사 시점 · 이전 경력은 발화되지 않아 적지 않는다. 설명란에 본인 블로그 글(addyosmani.com/blog/software-factories)이 링크돼 있으나 열어 보지 않았다(미확인).

## 위키에서의 진술

- **두 공장**: lights-on(사람이 판단 · taste를 루프 안에 둔다) vs dark(사람은 의도로 물러나고 예외에만 불려 온다). 대부분의 팀은 그 스펙트럼 위 → [[software-factory]]
- *"Agents can now generate ways for you to check your code much more cheaply than ever before."* — 테스트 · 벤치마크 · 스펙을 에이전트가 만든다 → [[verification-cost-asymmetry]]
- Anthropic 워크플로: Claude가 1차 리뷰, **실제 사용자처럼 시험**(브라우저 · e2e · 린트), hooks가 diff를 보고 PR을 고치는 루프, taste를 CLAUDE.md · AGENTS.md에 성문화 → [[agent-verification-skill]] · [[automated-code-review]]
- *"people are responsible for checking on the agent's evidence"* — 영상 · 스크린샷 → [[agent-change-evidence]]
- 기업의 세 걱정: 통제 · 권한 · 샌드박스, agent identity · telemetry → [[agent-sandboxing]]
- 에이전트 작성 PR은 라벨을 붙이되 *"I'm I'm still on the hook"* → [[named-human-accountability]]
- ⚠️ 숫자: 5월 *"about 2,500 changes"*(기간 단위 미발화), Claude.ai 개편 *"about 3,000 pull requests"* 와 *"three-byed the performance"*(사례 연구 미확인). 제목의 "하루 3만 건"은 본인 발화가 아니다 → [[trusted-throughput]]

## References

- [[tech-bridge-anthropic-30k-merges-verification]]
- 관련: [[manish-kapur]](같은 대담) · [[anthropic]] · [[claude-code]]

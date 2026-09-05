---
title: intent.md
type: concept
category: pattern
tags: [sdlc, requirements, artifact, discovery, anthropic]
related: [ai-native-sdlc, spec-driven-development, context-engineering, verifiable-goals]
first-seen: tech-bridge-ai-native-sdlc
sources: [tech-bridge-ai-native-sdlc]
created: 2026-09-05
updated: 2026-09-05
---

# intent.md

**에이전트가 사람을 인터뷰해서 만든, 요구사항 이전 단계의 아티팩트.** [[anthropic|Anthropic]]의 *AI-Native SDLC Playbook*이 제안하는 아티팩트 체인의 첫 고리다. → [[ai-native-sdlc]]

정의가 이 개념의 전부라 할 만큼 압축돼 있다.

> **사람이 읽을 수 있고 기계가 처리할 수 있는(human readable and machine actionable)** 파일.

## 무엇을 대체하는가

| 기존 | intent.md |
|---|---|
| 회의 → 요구사항 수집 → **PRD** → 워크숍 → 이해관계자 |
| 사용자 스토리 → 스토리 포인트 → **소유권 이전, 인수인계** | 창시자가 Claude와 **직접 구상**하고 그 결과를 기록 |

인계(handoff)를 없애는 것이 요점이다. 아이디어를 가진 사람과 그것을 문서로 만드는 사람 사이의 번역 손실이 사라진다.

## 만드는 방법 — 에이전트가 묻는다

> 상담원이 여러분이 개발 중인 기능이나 해결하려는 버그를 **완전히 이해할 때까지 반복적으로 질문**하도록 하는 것입니다. 당신은 자신의 경험, 해당 분야 지식, 그리고 맥락을 **이 대화에 최대한 많이 쏟아붓고** 있습니다.

방향이 뒤집혀 있다 — 사람이 요구사항을 쓰는 게 아니라 **에이전트가 캐낸다.** [[tech-bridge-multimodal-commerce-agent]]의 [[fuzzy-intent-discovery]]가 소비자에게 하는 일을, 여기서는 개발 조직 안에서 한다.

도구 예시: `switch dimension discovery`([[switch-dimension]]), *"grill me"*, Cursor의 requirements discovery.

## creator — 전문가가 아니어도 된다

> **버그 제보를 하는 고객**일 수도 있습니다. **제품 관리자**가 새로운 기능에 대한 아이디어를 가지고 있을 수도 있습니다. **개발자**가 프로세스 개선 사항을 기록하고 싶어할 수도 있습니다.

작성 주체를 넓히는 대신 **검토 절차**를 붙인다.

> 의도를 처음 제시한 사람이 담당자가 작성한 내용을 다시 검토하여 수정하고 **양측 모두 만족하는지 확인**하는 것이 좋습니다.

## 배치와 운영

- 프로젝트에 **`intent` 폴더**를 만들고 그 안에 둔다. 도구 중립적이다(Cursor·Claude Code·Codex 무관).
- 규모가 커지면 **파일명에 의도 이름을 접두사로** 붙인다.
- 정리·우선순위는 여전히 사람 쪽이다 — Notion이나 Linear로 모으고 제품 오너가 정리하거나, 에이전트가 *"프런트엔드, 소규모/대규모, 기능 여부, 우선순위"* 로 태깅한다.
- 승인되면 **hook으로 `spec.md`가 자동 생성**된다.
- 거버넌스 대상이다 — **누가 수정했는지, 어떻게 발전했는지** 버전을 남긴다.

## 왜 파일이어야 하는가 — 컨텍스트 윈도

이것이 이 개념의 가장 실용적인 근거이고, 문서화 취향과 구별되는 지점이다.

> **소프트웨어 개발 수명주기의 모든 단계를 한 에이전트가 모두 수행할 수는 없기 때문입니다. 컨텍스트 창이 나타날 것입니다.** (…) 담당자는 **이전 대화 내용을 이해하지 못한 채 처음부터 다시 시작**할 수 있습니다.

즉 intent.md는 **에이전트 간 인계 프로토콜**이다. [[context-resets-and-compaction]]이 컨텍스트를 압축해서 살리는 접근이라면, 여기는 **파일 시스템으로 외재화**해서 압축을 필요 없게 만든다. → [[context-engineering]]

## 루프를 닫는 지점

유지보수 단계에서 장애가 나면 **Claude가 로그·티켓·Slack 메시지를 근거로 intent.md를 스스로 만든다.** 즉 이 아티팩트는 파이프라인의 입구이자 출구다. 사람이 만든 intent와 기계가 만든 intent가 같은 형식을 공유한다는 것이 이 설계의 요점이다.

## ⚠️ 미확인

- 이 위키는 **Anthropic 원문서를 직접 ingest하지 않았다.** 위 내용은 전부 [[tech-bridge-ai-native-sdlc]]의 해설을 통한 것이다.
- `intent.md`의 실제 스키마·필수 필드는 소스에서 제시되지 않는다.

## References

- [[tech-bridge-ai-native-sdlc]] — first-seen
- 원문서(미ingest): <https://claude.com/blog/the-ai-native-sdlc-playbook>
- 관련: [[ai-native-sdlc]] · [[spec-driven-development]] · [[context-engineering]] · [[fuzzy-intent-discovery]]

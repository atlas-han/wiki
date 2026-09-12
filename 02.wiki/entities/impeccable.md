---
title: Impeccable
type: entity
category: tool
tags: [design, agent-skills, claude-code, cursor, codex, copilot, steering]
aliases: [임페커블]
links: []
sources: [tech-bridge-impeccable-design-steering]
created: 2026-09-12
updated: 2026-09-12
---

# Impeccable

[[paul-bakaus]]가 만든 **디자인 스킬**. *"여러분의 코딩 하네스를 더 나은 디자이너로, 그리고 바라건대 여러분도 더 나은 디자이너로"*. **모든 하네스에서 동작** — [[claude-code|Claude Code]] · GitHub Copilot · [[cursor|Cursor]] · [[codex|Codex]] 등. 이 위키 유일한 소스는 [[tech-bridge-impeccable-design-steering]](*"도구 자체가 아니라 만든 접근"* 에 관한 발표).

> ⚠️ 제작자의 자기 진술. 효과의 정량 근거 없음. 저장소 URL·라이선스는 소스에 없다(*"닫으려는 PR"* 로 보아 공개 저장소로 추정). ko 자막은 제품명을 형용사 "흠잡을 데 없는"으로 번역했다.

## 무엇을 하나

| 요소 | 내용 |
|---|---|
| **어휘** | bolder · quieter · distill(단순화) · polish · denser · harden(전반에서 동작 — 성능·반응형) · **overdrive**(완전히 과하게) → [[adjective-verb-steering]] |
| **단어의 정의** | *bolder* = 그라데이션·글래스·네온이 아니라 **위계·스케일·결정적 타이포**, 디자인 시스템을 깨지 않으면서. *"bolder라고 하면 로드되는 파일"* — 스킬의 progressive disclosure |
| **자기 점검** | 파일의 실제 문장: **"누군가에게 보여주고 'AI가 더 bolder하게 만들었다'고 말하라. 그들이 믿으면 실패한 것이다."** |
| **워크플로 맵** | 초기화/셰이핑 → 제작·반복(형용사·동사) → harden·polish → 디자인 시스템 복귀(기술·디자인 부채 정리). 각 단계가 **주입 지점** |
| **auto 없음** | *"auto는 없고, 앞으로도 없다"* — 자동 모드 요청 PR을 닫는다 → [[no-one-shot-design]] |

## 시연 (⚠️ 슬라이드)

의도적으로 밋밋한 웹사이트에 *"워크플로 섹션을 더 bolder하게"* — Impeccable 유무로 비교(같은 프로젝트, **GPT-5.5 extra high**, 같은 프롬프트). 화자 자신이 *"완벽하지 않다"*(섹션 번호 = *"GPT가 아주 좋아하고 Claude도 좋아하는"* AI의 흔적), *"약간의 차이 — 여러분이 판단하시라"* 고 유보. 플라시보 의심에 대한 답이 이 비교다.

## 만든 방식

- **워크플로를 먼저 매핑** — *"도구를 만들 때마다"*. 디자인은 선형이 아니라 지저분하고 여러 사람이 관여한다.
- **커뮤니티 테스트** — `overdrive`는 *"출시할지 확신이 없었던"* 반농담 명령인데 *"사람들이 열광"*. *"확신 없는 명령을 커뮤니티로 테스트하고, 정착하면"* — [[skill-self-improvement]]의 *승격은 사람이* 를 커뮤니티 반응으로 대신한 형태.
- 이론적 근거: **형용사는 Leitwort**(Matt Pocock 트윗에서) — 모델에게 이미 뜻이 있는 단어를 프로젝트의 뜻으로 번역.

## 이 위키에서의 자리

- **[[agent-skills]]의 새 종류** — 절차·프레임워크 지식·도메인 판단이 아니라 **어휘의 정의**를 담는다. 그리고 *portable across harnesses* 원칙([[imad-touil]])의 실증이자, 스킬이 **자동화를 명시적으로 거부**하는 첫 사례.
- **[[generator-evaluator-pattern]]** — 자기 점검 문장은 평가 기준을 **생성자 안에** 둔다. Anthropic의 분리 원칙과 반대이며 자기 평가 편향은 소스가 다루지 않는다.
- 슬롭의 현재 모습(*Claude 베이지*)을 기록한 소스 → [[ai-slop]].
- 사용자가 받는 것은 *"모두가 소통할 수 있는 디자인의 공유 언어"* — 디자인 엔지니어의 시대.

## References

- [[tech-bridge-impeccable-design-steering]] · [[paul-bakaus]]
- 관련: [[adjective-verb-steering]] · [[steering-altitude]] · [[no-one-shot-design]] · [[agent-skills]] · [[ai-slop]]

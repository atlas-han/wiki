---
title: Impeccable
type: entity
category: tool
tags: [design, agent-skills, claude-code, cursor, codex, copilot, steering]
aliases: [임페커블]
links: []
sources: [tech-bridge-impeccable-design-steering, tech-bridge-skill-engineering-dark-arts]
created: 2026-09-12
updated: 2026-09-28
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

## 2026-09-28 — 내부 구조: 스크립트·훅·라이브 모드·하네스별 빌드 ([[tech-bridge-skill-engineering-dark-arts]])

제작자 워크숍이 09-11 편에 없던 **구성 요소**를 밝힌다. 사이트 `impeccable.style`(02:21), **Apache 2 오픈소스**(49:37~49:40), 설치 `npx impeccable skills install`(ASR *"MPX"*, 49:42~49:45) — 09-12에 *"라이선스는 소스에 없다"* 로 남긴 빈칸이 채워졌다.

| 구성 요소 | 내용 |
|---|---|
| **명령별 MD 라우팅** | `critique`·`polish` 등 명령마다 다른 MD 파일 로드, *"not just one giant skill MD"*(21:43~21:52). 브리프를 보고 **brand(랜딩) / product register**를 바꿔 다른 규칙 로드(22:00~22:19) |
| **`critique`** | 서로 못 보는 두 서브에이전트 — 디자인 디렉터 LLM + **결정론적 디자인 린터**(대비·서체 수·가장자리 근접, 09:05~09:21) → 메인 스레드 종합 → [[generator-evaluator-pattern]] |
| **`color.js`** | 프로젝트 시작 시 100개 넘는 손으로 고른 원색 중 시드 → [[anti-attractor]] |
| **`.impeccable` 폴더** | 비평을 git-ignore된 파일로 남기고 다음 세션이 읽는다, 사용자의 반대를 선호로 기록(23:07~24:12) |
| **`context.mjs`** | 매 호출 실행 — `product.md`·`design.md` 주입, 없으면 구조화된 JSON 지시, **자기 업데이트 안내**(27:03~28:15) → [[scripts-that-talk-back]] |
| **디자인 훅** | Claude Code·Cursor·Codex·GitHub Copilot에 설치, 편집마다 린트, 약한 모델엔 PreToolUse, 파일~CSS 규칙 단위 ignore(30:27~34:21) → [[hook-enforced-workflow]] |
| **라이브 모드** | 인앱 브라우저 + 폴러 + SSE + stdout — 요소 선택 → 변형 → accept/escape(35:43~39:17). MCP를 쓰지 않는다 |
| **하네스·모델별 빌드** | 치환 변수(질문 도구), 모델별 XML 블록(과적합 회피 규칙), Codex/GPT용 gate MD, **자체 CLI 설치기/컴파일러**(45:22~46:51) → [[cross-harness-skill-compilation]] |
| **eval** | E2E(LLM + Playwright) + 비공개 eval 하네스, 규칙마다 XML ID로 **줄 단위 ablation** → [[skill-evals]] |

**09-11 편과의 관계** — 그 편의 *"auto는 없다"* 와 이 구조는 모순되지 않는다: **결정은 사람에게**(라이브 모드의 accept/escape, 비평 반대의 기록), **규율은 모델에게 강제**(스크립트·훅·gate). ⚠️ 위키의 정리.

⚠️ 제작자 진술. 라이브 데모는 Cursor+Composer에서 서브에이전트를 보여 주지 못했고(16:23~16:26) 훅 데모는 *"fake demo"*(33:38). 제작자 스스로 *"we're definitely outgrowing the skill platform"*(58:44~58:48).

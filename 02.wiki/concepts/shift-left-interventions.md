---
title: 개입을 왼쪽으로 — 에이전트를 위한 시프트 레프트 (Shift-Left Interventions)
type: concept
category: pattern
tags: [shift-left, context, agents-md, static-analysis, tests, evals, lazy-prompter]
aliases: [시프트 레프트(에이전트), 게으른 프롬프터, lazy prompter, 개입의 스펙트럼]
related: [shift-left-security, tools-and-context-over-harness, context-engineering, harness-engineering, llm-coding-guidelines, executable-standards, agent-skills, skill-self-improvement]
first-seen: tech-bridge-lopopolo-agent-harness
sources: [tech-bridge-lopopolo-agent-harness]
created: 2026-09-23
updated: 2026-09-23
---

# 개입을 왼쪽으로

**에이전트를 바로잡는 개입(intervention)을 일회성 프롬프트(오른쪽 끝)에서 문서 → AGENTS.md → 정적 검증기·테스트 → eval(왼쪽)로 옮겨, 점점 더 싸고 자동이며 팀과 시간을 넘어 반복되게 만드는 것.** 목표는 모델이 **스스로 컨텍스트를 발견**하게 하는 것이고, 그 결과 사람은 **게으른 프롬프터**가 된다. [[ryan-lopopolo|Ryan Lopopolo]], [[tech-bridge-lopopolo-agent-harness]].

> 나는 **엄청나게 게으른 프롬프터가 되고 싶다.** 왜냐하면 제가 **모델이 스스로 기반을 다지는 데 필요한 도구와 맥락을 제공하는 작업을 완료했다면, 프롬프트에 그 내용을 미리 입력할 필요가 없기 때문입니다.** (04:24~04:38)

## 스펙트럼

> 그러니까 **제 프롬프트에 텍스트를 추가하는 거죠. 이것이 우리가 갈 수 있는 가장 [오른쪽 끝]**이라고 할 수 있습니다. 그리고 **모델에게 우리가 제공하는 문서 자료를 통해 추론할 수 있는 도구와 능력을 부여하는 것은 모델이 스스로 맥락을 발견할 수 있도록 하는 방향으로 점점 더 [왼쪽으로 가는] 것입니다.** (06:24~06:46)

(⚠️ ko는 이 문장을 **"가장 극우적인 방향" · "점점 더 좌파적인 접근"** 으로 옮겼다 — en-orig *far to the right / further to the left*.)

| ← 왼쪽 (싸고 자동, 영속) | | | | | 오른쪽 (비싸고 수동, 일회) → |
|---|---|---|---|---|---|
| **eval** → DeepMind로 업스트림(모델 자체 개선) | 정적 검증기가 **에이전트에게 프롬프트를 주입** | **정적 검증기 + 테스트** | 문서를 가리키는 **AGENTS.md** | **문서** | **프롬프트 재시도·텍스트 추가** |

출처: 04:59~05:57. 가장 오른쪽을 버리는 이유 — *"그 방법은 **우리 팀원들에게는 통하지 않아요. 제 시간 범위 내에서는 확장성이 떨어집니다**"*(05:21~05:26). 개입의 가치 기준 — *"개입이 **가능한 한 저렴하게** 구현될 수 있기를"*(06:04~06:11).

## 구체적 기법 (소스에 나온 것만)

- **문서의 구조를 에이전트용으로** — 링크를 본문 흐름에서 빼 **문단·목록 끝의 앵커**로 두고, 그 위치를 **테스트로 강제**(08:10~08:49). 목적은 *"컨텍스트를 효율적으로"* + *"사람이 읽기 쉬운 형태"*. 진행자가 [lost in the middle] 문제와 연결(08:58~09:02).
- **관측 가능성을 익숙한 도구 형태로 접기** — PromQL류, CLI로 *"추론을 결정론으로 전환"*(07:17~07:55).
- **실패를 관찰하고 환경을 고친다** — *"[에이전트]가 업무를 제대로 수행하지 못하는 순간을 관찰하십시오. 왜 그런지 스스로에게 질문하고 (…) 에이전트 주변 환경을 개선하고"*(15:16~15:35). *"머리를 한 대 때려서라도 다시는 똑같은 실수를"*(09:34~09:38).

## 위키에서의 좌표

- **[[shift-left-security]]와 이름이 같고 구조가 같다** — 늦고 수동이고 한 번뿐인 것을 **이르고 자동이고 반복되는 것**으로. 대상만 다르다(보안 검증 ↔ 에이전트 교정). ⚠️ 두 소스는 서로를 모른다.
- **[[harness-engineering]]의 System Evolution**(*every mistake becomes a rule* — 컨벤션 위반 → agents.md, 파괴적 명령 → 훅)과 **같은 루프**. 이 페이지가 더하는 것은 **순서(스펙트럼)** 와 **끝점(모델 가중치)** 이다.
- **[[executable-standards]]** — 문서는 낡으니 프로세스에 심어라. 스펙트럼에서 *문서 → 정적 검증기* 로 한 칸 옮기는 것과 같은 주장.
- **[[context-engineering]]** — 컨텍스트를 **밀어 넣는** 쪽에서 **발견하게 하는** 쪽으로. [[agent-skills]]의 progressive disclosure와 같은 방향.
- **[[skill-self-improvement]]** · [[lauren-tan|Lauren Tan]]의 *스킬은 실패 모드에서 자란다* — 실패 관찰이 개입의 원천이라는 점이 같다.

## ⚠️ 유보

- **스펙트럼의 가장 왼쪽(eval → DeepMind)은 Google 내부자의 경로다.** 화자도 *"운이 좋든 나쁘든 간에"* 라는 단서를 붙이고, **작동한 사례를 말하지 않는다.** 대부분의 사용자에게 스펙트럼은 테스트에서 끝난다.
- **어느 칸으로 옮길지 판단 기준이 없다** — *"전부 다요"*(04:59)가 답이다.
- **측정 없음** — 앵커 링크 기법도 *"제 개인적인 취향에 약간 치우친 방식일 수도"*(08:54).

## References

- [[tech-bridge-lopopolo-agent-harness]] · [[ryan-lopopolo]]
- 같은 이름: [[shift-left-security]]
- 관련: [[tools-and-context-over-harness]] · [[harness-engineering]] · [[executable-standards]] · [[context-engineering]] · [[agent-skills]] · [[llm-coding-guidelines]] · [[skill-self-improvement]]

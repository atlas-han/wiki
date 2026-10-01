---
title: "Tech Bridge — AI가 여러분의 데이터를 노출하고 있다: 눈에 보이지 않는 AI 보안의 숨은 위험 (Jeff Crume, IBM Technology)"
type: source
tags: [security, data-security, data-exposure, shadow-ai, dlp, data-lineage, rag, agents, mcp, compliance, ibm, video]
source-url: https://www.youtube.com/watch?v=lr5cxvYJDLg
source-type: video
author: Tech Bridge (한영자막 재배포) · [[jeff-crume|Jeff Crume]] ([[ibm|IBM]] · ⚠️ 이름은 설명란에만) · 촬영 시점 미확정
date-published: 2026-09-30
ingested: 2026-10-01
created: 2026-10-01
updated: 2026-10-01
---

# Tech Bridge — AI가 여러분의 데이터를 노출하고 있다

[[tech-bridge|Tech Bridge]]가 한영자막을 입힌 **11:15 1인 해설**(공식 챕터 없음). [[ibm|IBM Technology]] 계열의 **여덟 번째 소스**이고, [[jeff-crume|Jeff Crume]]의 **두 번째** 소스다(첫 편: [[tech-bridge-shift-left-security-ai-code]], 09-16). 이번에도 **이름은 설명란에만** 있다.

한 줄 테제:

> **민감 데이터는 이미 노출돼 있고 AI가 그걸 보이지 않게 키운다. "어떤 AI 도구를 쓰나"가 아니라 "민감 데이터가 AI 시스템을 어떻게 흐르고 어디서 노출되나"를 — 형태가 바뀌어도 — 끝에서 끝까지 추적해야 한다.**

> *"It's AI time. Do you know where your data is? Well, even if you think you do, you probably don't."* (00:00~00:05) · *"It's not enough just to know what AI tools are in use (…) You also need to know how sensitive data is flowing through AI systems, and where it might be exposed."* (01:35~01:45) · *"Each one of these only sees part of the picture."* (09:04~09:06)

ASR·ko 보정: ko가 영상의 **목표 문장**(*"how do we enable AI adoption without creating data security gaps?"*)을 **"인공지능 도입을 허용하지 않음 / 보안 취약점을 만듭니다"** 로(ko 04:35~04:38), single pane of glass의 근거(*"I can't afford to have (…) monitor systems that are not integrated"*)를 **"나는 많은 것을 가질 여유가 있다"** 로(ko 07:37), 맺음(*"if we can't monitor where it's going"*)을 **"감시할 수 있습니다"** 로(ko 11:02) 뒤집는다. **"AI" → "일체 포함"** 이 세 번(ko 09:21 · 10:58 · 11:12), *intellectual property* → **"부동산"**(ko 09:48), 없던 **"안녕하세요, 잘 지내시죠?"** 삽입(ko 08:21). 세 discovery 렌즈 중 첫째(*agentic platform discovery*)는 **세 트랙 모두 깨졌다**(en-orig *"a Gentic"*, `en` *"Agility Platform"*, ko *"애질리티 플랫폼"*). 전체 목록은 raw 파일.

> ⚠️ **벤더 해설, 제품명 0개.** [[ibm]]의 기존 관찰(*자사 제품이 등장하지 않는 개념 해설*)이 **여덟 번째**로 유지된다 — 다만 이번 편은 **결론이 "그런 도구가 있다"** 다(*"there are tools that can help you manage your data exposure from AI. That's the good news."* 11:09~11:13). 그리고 후반의 요구사항 목록(통합 가시성 플랫폼·single pane of glass·AI 인지 분류·lineage·조사·규제 보고)은 **제품 기능 명세의 형태**다. 설명란 링크 *"Exposed Data 상세 정보"*(`ibm.biz`)는 열어 보지 않았다. → 아래 *기존 위키와의 대조*.
>
> ⚠️ **수치는 하나, 출처 없음.** *"One recent study found that 31% of organizations had a data privacy violation due to an AI-related incident."*(00:22~00:31) — 연구명·연도·표본 없음. *"weeks down to minutes"*(10:30~10:33)는 요구사항(목표)이지 측정이 아니다.
>
> ⚠️ **촬영 시점 미확정.** 단서는 *"recent study"*, MCP 언급(08:15~08:32), EU AI Act(10:44)뿐. [[ibm]] 편 **여덟 번 연속** 미확정.
>
> ⚠️ **화이트보드 의존.** *"we might have sensitive information here"*(02:51) 등 지시어가 화면 도식을 가리킨다. 아래 아키텍처 표는 **발화 순서로 재구성한 것**이다(정리자).

## 1. 문제 — 이미 노출됐고, 보이지 않는다 (00:00~01:48)

*"If you're like most organizations, your sensitive data has already been exposed, and AI is just making the problem worse. And it's happening right under your nose, and you can't see it."*(00:05~00:16). 원인은 속도 차이 — *"AI adoption is moving faster than traditional security approaches can actually protect."*(00:16~00:22)

노출 경로로 두 가지를 든다:

- **섀도우 AI** — *"shadow AI projects, where it's basically unauthorized AI that people are deploying inside the environment. Well, those things often lack the security controls that [our] policy would specify they should have."*(00:32~00:43)
- **공개 클라우드 챗봇** — 질문과 함께 *"a spreadsheet of information that's sensitive"*(00:53~00:55)를 넣는다. *"once that goes to a public chatbot, it basically becomes public information. Because they can use that sensitive information to train their models, and then it's available to everyone."*(00:55~01:05)

> ⚠️ **Contradiction (범위 차이, 미해소):** "공개 챗봇에 넣으면 모델 학습에 쓰여 누구나 볼 수 있게 된다"는 **일반화**다. 이 위키의 [[katelyn-lesse|Katelyn Lesse]]([[anthropic]] 플랫폼)는 *"고객 데이터로 학습하지 않는다"* 고 답한다 → [[katelyn-lesse]]. 대상이 다르다(소비자용 공개 챗봇 vs API 플랫폼) — 화자는 **어떤 챗봇·어떤 약관**인지 말하지 않고, *"can use"*(할 수 있다)와 *"available to everyone"*(누구나 접근) 사이의 경로(학습 데이터가 어떻게 다른 사용자에게 드러나는가)도 설명하지 않는다. 위키는 어느 쪽도 확정하지 않는다.

그래서 답해야 할 질문 셋 — *"what did data did the AI use? Where did it get that data? And ultimately, how (…) are we going to manage the AI data exposure in a proactive way?"*(01:11~01:28). 그리고 ⭐ *"Traditional DLP, data loss prevention, and AI tools can't answer these questions. We're going to need a different approach."*(01:28~01:37) — ⚠️ *"and AI tools"* 가 무엇을 가리키는지 모호하다(판독하지 않음).

→ [[ai-data-exposure]] (신규)

## 2. 아키텍처의 모든 칸에 민감 데이터가 있다 (01:48~04:41)

화자가 그리는 고수준 아키텍처와 각 칸의 민감 데이터(발화 순서로 재구성):

| 칸 | 흐름 | 무엇이 민감한가 | en-orig |
|---|---|---|---|
| **학습 데이터** | 모델을 *"train or tune"* | 학습 데이터 속 민감 정보 | 01:53~01:55 · 02:49~02:56 |
| **프롬프트** | 사용자 → AI | 프롬프트에 붙인 **스프레드시트·문서** | 01:58~02:01 · 02:57~03:12 |
| **RAG** | 다른 데이터 소스로 보강 | (이 칸은 개별 언급 없음 — §3 workload에서 다룬다) | 02:05~02:10 |
| **컨텍스트/정책** | *"overriding all of this"* — AI에게 어떻게 동작·답할지 지시 | *"ways that we do things that we consider to be competitive advantages"* | 02:12~02:25 · 03:15~03:23 |
| **도구** | 에이전트가 코드 작성·DB 접근 | *"Are they guarding it or not? Do we have control and visibility over those particular tools?"* · DB에 쓰면 *"do I know where that data is going to end up?"* — *"going other places downstream"* | 02:26~02:36 · 03:27~03:48 |
| **하위 에이전트** | *"spawn off yet other agents, which then could spawn off yet other agents"* | 민감 정보를 에이전트 손에 넘기고, 그들이 또 에이전트를 낳는다 | 02:36~02:39 · 03:48~03:58 |

결론: *"sensitive information is all over this thing, and it's flowing all through the architecture."*(04:02~04:07)

그래서 알아야 할 넷(04:11~04:38): ① AI가 **어떤** 민감 데이터를 쓰는가 ② **노출**은 무엇인가 — *"Was it authorized and was it governed?"*(04:23~04:25) ③ 데이터가 AI를 지나며 무슨 일이 있었는지 **어떻게 조사**하나 ④ ⭐ *"how do we enable AI adoption without creating data security gaps?"*(04:33~04:38) — ⚠️ ko가 뒤집은 문장.

> 이 표의 칸들은 이 위키에 이미 각자 페이지가 있다 — [[retrieval-augmented-generation]] · [[context-engineering]] · [[model-context-protocol]] · 하위 에이전트 생성. **이 편의 새로움은 칸이 아니라 관점이다**: 각 칸을 *성능·컨텍스트* 가 아니라 **민감 데이터가 지나가는 구멍**으로 다시 본다. ⚠️ 위키의 정리.

## 3. 두 흐름 — workload와 workforce (04:41~06:58)

> *"There's a workload stream, which is basically inside the AI systems themselves, and the workforce stream, where this is the employees' use of the AI."* (04:50~04:59)

두 흐름 모두에서 할 일은 같다 — *"monitor, track, and then be able to show how that data has moved through the system and how it's been used and how it's been exposed"*(05:01~05:08).

| | **workload** (AI 시스템 내부) | **workforce** (직원의 AI 사용) |
|---|---|---|
| 볼 곳 | AI 앱 · **RAG 파이프라인** · **벡터 DB**(*"the heart of a lot of these generative AI models"*) | 파일 **업로드·다운로드** · **복사-붙여넣기** |
| 핵심 난점 | ⭐ **데이터 변환** — *"If I'm looking for it in only this form, I might miss it and not realize that the data has leaked out."* | ⭐ **파생 파일** — *"child files that could be derived from that. And I need to be able to track all of those just as I did the original file"* |
| 보여야 할 것 | 출처 · 변환 · 최종 목적지 | 직원이 어떻게 소비하고 **다른 직원과 공유**하는가 |
| en-orig | 05:10~06:06 | 06:06~06:57 |

두 흐름의 난점이 같은 모양이다 — **원본 형태만 찾으면 놓친다.** 변환된 것(workload)과 파생된 것(workforce)을 원본과 같은 민감도로 추적해야 한다. → [[lineage-driven-risk-visibility]] (신규)

## 4. 통합 플랫폼에 필요한 넷 (06:57~07:56)

*"I need to see this in a unified end-to-end visibility protection platform."*(06:57~07:04)

1. **Lineage** — *"where did the data come from and how did it move through (…) the system"* — 예: 출처 → 이 AI → *"ended up on this endpoint system"*(07:06~07:21)
2. **두 흐름을 가로지르는 정책** — *"policies that are shared across both of these and monitored and enforced"*(07:22~07:33)
3. **Single pane of glass** — *"I can't afford to have a whole bunch of different monitor systems that are not integrated because then I won't know."*(07:33~07:42) ⚠️ ko 뒤집힘
4. **사전적 위험 식별** — *"proactively, not just after all of the data has escaped"*(07:45~07:53)

## 5. 세 discovery 렌즈 — 각각 일부만 본다 (07:56~09:18)

| 렌즈 | 답하는 질문 | en-orig |
|---|---|---|
| **Agentic platform discovery** | *"who prompted which particular model, and which agent actually ran, which MCP tool was called"* | 08:06~08:18 |
| **Endpoint DLP discovery** | *"which agents and extensions and MCP servers exist on each of these devices"*, *"files, memory, and other digital residue that's on the endpoint device"* | 08:23~08:40 |
| **클라우드/온프렘 discovery** | *"which data sources exist on these particular platforms"*, 분류·민감도, *"maybe even the ownership"* | 08:42~08:59 |

> *"Okay, but all of that's good, but did you see the problem? Each one of these only sees part of the picture. So, what we really need is a holistic view that takes all of these into account and integrates them all into a single view."* (09:00~09:15)

- ⚠️ 첫 렌즈 이름은 **세 트랙 모두 깨졌다** — en-orig *"a Gentic"*, `en` *"Agility Platform"*, ko *"애질리티 플랫폼"*. 질문 내용(에이전트·MCP)으로 **agentic** 으로 판독했다.
- **MCP가 보안 인벤토리 항목으로 등장한다** — "어떤 MCP 도구가 호출됐나"(런타임 로그)와 "어떤 MCP 서버가 기기에 있나"(설치 인벤토리)가 **다른 렌즈에 나뉘어** 있다. → [[model-context-protocol]]
- ⚠️ 세 렌즈를 **"Three different tools"**(08:02~08:04)라고 부른다 — 도구 범주이지 제품명은 아니다.

## 6. 요구사항 넷 (09:18~10:54)

| # | 요구사항 | 조건 | en-orig |
|---|---|---|---|
| ① | **AI 인지 자동 데이터 분류·발견** | *"continuous because the system is changing constantly"* · 모든 플랫폼의 소스 · PII·PHI·금융 데이터·지적재산 인식 | 09:24~09:50 |
| ② | **Lineage 기반 위험 가시성** | *"data gets transformed by rag[=RAG], AI agents and systems"* · *"see how the data propagates through the system and it will be changed as it propagates in some cases"* | 09:52~10:13 |
| ③ | **지능형 조사** | *"context aware based on the user sensitivity the destination"* · ⭐ *"take the investigation time which is typically weeks down to minutes"* | 10:14~10:36 |
| ④ | **규제 준수 보고** | *"the GDPR (…) the EU AI act [SOC 2] ISO 27001 HIPAA the list goes on"* | 10:36~10:56 |

- ③ *"weeks down to minutes"* — **목표치이지 측정이 아니다.** 근거·사례 없음.
- ③ *"user sensitivity"*(10:22~10:23) — "사용자 민감도"인지 "사용자, 민감도, 목적지"의 나열인지 자막만으로 모른다(쉼표 없음). ko는 *"민감도에 따른 맥락 / 사용자, 목적지"* 로 나열로 읽었다.
- ④ en-orig *"generalized data protection regulation"* — GDPR 정식 명칭은 *General*. 말실수/ASR 미판독. *"sock to"* → SOC 2(ko가 바로잡음).

## 7. 맺음 — 혈액 비유 (10:54~11:15)

> *"Data is the lifeblood of AI. It has to keep moving or the patient dies. But if we can't monitor where it's going we could be hemorrhaging and not even know it. Like a human body the system is complicated but there are tools that can help you manage your data exposure from AI. That's the good news."* (10:54~11:13)

⚠️ ko는 이 문단을 무너뜨렸다 — *"데이터는 기업의 핵심입니다. 일체 포함."*, *"환자가 사망했습니다"*(과거), *"감시할 수 있습니다"*(can't → can).

## 기존 위키와의 대조

### 합치하는 것

- **[[shift-left-security]] · [[continuous-security-validation]]** (같은 화자, 09-16) — ① 요구사항의 *"continuous because the system is changing constantly"* 와 *"proactively, not just after"* 는 09-16 편 ⑤(*최종 관문이 아니라 지속적 실천*)와 ②(*사후 체크박스는 작동한 적이 없다*)의 **데이터 쪽 반복**이다. 09-16 편이 **코드**를 왼쪽으로 옮겼다면 이번 편은 **데이터 흐름**을 계속 본다. 두 편 다 원인을 **AI의 속도**에 둔다(*"AI adoption is moving faster than traditional security approaches"* 00:16~00:22).
- **[[agent-governance-layers]]** — *"Was it authorized and was it governed?"*(04:23~04:25), 두 흐름을 가로지르는 **공유 정책**(07:22~07:33). 이 페이지가 모아 온 "에이전트 바깥의 벽"에 **관측(가시성) 층**을 하나 더 얹는다. ⚠️ 다만 이번 편의 처방은 거의 전부 **보는 것**(discovery·lineage·조사·보고)이고, **막는 것**은 *"monitored and enforced"*(07:29~07:33) 한 단어뿐이다 — 09-29 [[agent-365|Agent 365]] 항목의 *"보는 층인지 막는 층인지 불명"* 과 같은 빈자리.
- **[[retrieval-augmented-generation]]** — RAG 파이프라인과 벡터 DB가 **데이터 변환·노출 지점**으로 처음 다뤄진다(05:18~05:30, 09:57~10:04).

### 갈리는 것 / 긴장

> ⚠️ **같은 벤더가 데이터의 양쪽을 말했다.** 09-26 IBM 편([[tech-bridge-agents-as-catalyst]] · [[agents-as-catalyst]])은 데이터가 **갇혀 있는 것**이 문제이고 에이전트 도입이 데이터를 *"접근·검색·이해·재사용 가능"* 하게 열도록 강제한다고 했다. 이번 편은 데이터가 **흐르는 것** 자체가 노출이라고 한다 — *"It has to keep moving (…) But if we can't monitor where it's going we could be hemorrhaging"*. 두 편은 서로를 언급하지 않고, 화자는 *열기* 와 *흐름 감시* 를 혈액 비유 하나로 묶는다(**움직여야 하지만 보여야 한다**). 모순이라기보다 같은 벤더의 **두 판매 축**(데이터 개방 · 데이터 보안)으로 읽힌다 — ⚠️ 위키의 해석.

> ⚠️ **공격자가 없는 위협 모델.** 이 편의 노출은 전부 **부주의·무단 사용·불투명한 흐름**이다(섀도우 AI, 챗봇에 붙여넣기, 도구가 어디에 쓰는지 모름). [[prompt-injection]]·[[lethal-trifecta]]·[[confused-deputy-attack]]처럼 **악의적 입력이 에이전트를 조종해 데이터를 빼내는** 경로는 한 번도 나오지 않는다. 이 위키의 [[lethal-trifecta]] 틀로 보면 이 편은 ①(비공개 데이터)의 **위치 파악**과 ③(외부 노출)의 **사후 추적**에 집중하고 ②(신뢰할 수 없는 콘텐츠)는 다루지 않는다. → [[ai-data-exposure]]

## 해소하지 않고 표시만 한 것

- **31% 연구의 출처**(00:22) — 연구명·연도·표본 없음.
- **"Traditional DLP (…) and AI tools"**(01:28~01:33)의 "AI tools"가 무엇인가.
- **공개 챗봇 학습 주장의 범위** — 위 ⚠️ Contradiction.
- **"weeks down to minutes"**(10:30~10:33) — 목표치, 근거 없음.
- **"user sensitivity"**(10:22) — 한 항목인지 나열인지.
- **"generalized data protection regulation"**(10:44) — 말실수/ASR.
- **차단(enforcement)의 구체** — *"enforced"* 한 단어.
- **제품** — 설명란 *"Exposed Data 상세 정보"* 링크 미확인. 자막에 제품명 없음.
- **화자 신원·촬영 시점** — 설명란에만 / 미확정.

## 등장 개체

- 인물: [[jeff-crume]] (설명란 근거)
- 조직: [[ibm]]
- 규제·표준: GDPR · EU AI Act · SOC 2 · ISO 27001 · HIPAA (페이지 없음 — 나열만)
- 개념: [[ai-data-exposure]] (신규) · [[lineage-driven-risk-visibility]] (신규) · [[retrieval-augmented-generation]] · [[model-context-protocol]] · [[agent-governance-layers]] · [[shift-left-security]] · [[continuous-security-validation]] · [[lethal-trifecta]] · [[prompt-injection]] · [[agents-as-catalyst]]
- 용어(페이지 없음): 섀도우 AI(→ [[ai-data-exposure]]) · DLP · workload/workforce stream · single pane of glass · digital residue

## References

- 원본 영상: <https://www.youtube.com/watch?v=lr5cxvYJDLg> (11:15, `upload_date` 2026-09-30)
- raw: `01.raw/articles/2026-09-30_AI가 여러분의 데이터를 노출하고 있습니다 - 눈에 보이지 않는 AI 보안의 숨은 위험.md`
- 설명란 링크: <https://ibm.biz/~DSFj8t9c9> · <https://ibm.biz/~XFBzbXNlv> · <https://www.youtube.com/@IBMTechnology> (⚠️ 열어 보지 않았다)
- 같은 화자: [[tech-bridge-shift-left-security-ai-code]] · 같은 계열: [[tech-bridge-agents-as-catalyst]] · [[tech-bridge-tokenmaxxing-to-valuemaxxing]]
- [[tech-bridge]] · [[jeff-crume]] · [[ibm]]

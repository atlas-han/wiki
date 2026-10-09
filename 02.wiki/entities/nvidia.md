---
title: NVIDIA
type: entity
category: org
tags: [gpu, chips, ai-infrastructure, data-center, physical-ai, hardware]
links:
  - https://www.nvidia.com/
sources: [tech-bridge-jensen-huang-g20-agi, tech-bridge-jensen-huang-cbs-interview, tech-bridge-white-house-superintelligence-panel, tech-bridge-jensen-huang-korea-society-gala]
created: 2026-09-06
updated: 2026-10-09
---

# NVIDIA

GPU와 AI 인프라를 만드는 회사. 본 위키에는 CEO [[jensen-huang|Jensen Huang]]의 G20 대담([[tech-bridge-jensen-huang-g20-agi]], 2026-09-05 업로드)으로 첫 등장 — 이 위키의 조직 축에서 **첫 하드웨어 층**이다. 기존 조직은 모델 lab([[anthropic]]·[[openai]]·[[google-deepmind]]·[[shanghai-ai-lab]])과 도입 기업들이었다.

> ⚠️ 아래는 CEO의 판매·정책 무대 발언에서 온 것이며 제품 스펙·재무의 1차 소스가 아니다.

## 위키에서 알려진 사실

- **GPU** — *"병렬 처리 작업"*: 유체 역학·입자 물리학·양자 화학·그래픽·이미지 처리, 그리고 AI. 아키텍처 **14세대**.
- 판매 논리는 **대체 가능성(fungibility)·내구성** — *"모든 폐쇄형 모델, 모든 개방형 모델, 언어, 대규모, 소규모, 물리적, 생물학적 모델을 지원"*, *"모든 클라우드에, 온프레미스에, 엣지에."* 값비싼 인프라(1 GW ≈ 500~600억 달러)에서 특화 투자가 낡을 위험을 피하는 *"가장 안전한 아키텍처"* 라는 주장. → [[intelligence-as-infrastructure]]
- **2020년대 말까지 100 GW** 구축 계획 — *"전 세계에 필요한 지능을 생산."*
- 자기 위치를 **5단 케이크의 2층(칩)** 으로 두고, 4·5층(모델·애플리케이션)에 대한 중립을 약속한다 — *"미국 모델, 국제 모델 (…) 모두 실행."*
- 사내 AI 활용 — *"Anthropic, OpenAI, Cursor 같은 기성 AI"* + *"자체적으로 맞춤형 AI도 많이."*
- **피지컬 AI** 포지션 — 에이전트를 로봇·자율주행차·제조 로봇 팔·수술 로봇·신약 연구실에 넣는 것이 *"같은 아이디어."* → [[brain-hands-decoupling]]
- Lutnick 발언: 올해 *"세계 및 미국의 인프라에 거의 1조 달러"* 투자, 일자리 *"수십만 개"* — ⚠️ 주체 불명확.

## 위키에서의 좌표

이 위키의 토큰 논의에서 NVIDIA는 **토큰을 상품 단위로 파는 층**이다([[intelligence-as-infrastructure]]의 3층 표). 같은 날 [[sam-altman]]이 자체 추론 칩 **Jalapeno**와 네오클라우드 거품을 말한 것([[compute-constrained-growth]])이 이 회사의 고객 측 시각이다.

## 미해결 사항

- 제품 라인업·세대별 스펙·매출 — 이 위키에 없다.
- Huang이 말한 100 GW의 지역 배분·시기.

## References

- [[tech-bridge-jensen-huang-g20-agi]] · [[jensen-huang]]
- 관련: [[intelligence-as-infrastructure]] · [[compute-constrained-growth]] · [[brain-hands-decoupling]]
- 외부: <https://www.nvidia.com/>

## CEO의 CBS 인터뷰 — Vera Rubin, "미국 먼저", 데이터센터 (2026-09-25 · [[tech-bridge-jensen-huang-cbs-interview]])

> ⚠️ 여전히 **CEO의 방송 발언**이고 제품 스펙·재무의 1차 소스가 아니다.

- **제품 세대: Vera Rubin** — *"우리는 지금 Vera Rubin이라고 부르는 세대에 있다. Vera Rubin이 대량 생산으로 출하되고 있다"*(19:47~19:56). 이 위키의 **첫 NVIDIA 제품명**이다. 스펙은 없다.
- ⭐ **"이 기술로 중국보다 몇 년 앞서 있다"**(19:56~19:59) — 측정 기준 없음. ⚠️ **ko가 "중국은 이 기술 분야에서 앞서나가고 있다"로 뒤집었다.**
- **공급 정책: 미국 먼저** — *"미국이 그렇게 결정했고 전적으로 지지한다. NVIDIA의 최고 기술을 미국 기업에 먼저 제공"*, *"Dario와 Sam, 미국의 랩·산업체에 제공되고 있다"*(19:40~20:10). 동시에 *"중국에 모든 미국 제품을 금지하는 데 전적으로 반대"*, *"모든 칩 회사는 세계로 가서 경쟁해야"*(21:38~22:09). → [[slowdown-within-lead-margin]]
- **5단 케이크에서의 자리** — *"칩 분야에서 세계를 선도하고 싶다"*(20:43~20:46). → [[intelligence-as-infrastructure]]
- **AI 공장** — *"이 공장들 안에는 NVIDIA가 만드는 컴퓨터가 많다"*(42:52~42:59). *"NVIDIA는 많은 데이터센터에 동력을 공급한다"* 는 **진행자**의 말(32:03~32:06). → [[data-center-local-backlash]]
- **데이터센터 설계** — *"냉각 시스템은 이제 물을 재순환, 온수로 데이터센터를 식힌다"*(33:31~33:44). ⚠️ NVIDIA 설계인지 업계 일반인지 화자가 가르지 않는다.
- **사내 AI 사용** — *"OpenAI의 최신 Astra (…) 어디에서나 사용"*, [Claude Code] · [Cursor] · [Cognition](01:09~01:21). G20의 *"Anthropic, OpenAI, Cursor"* 목록의 갱신.
- **기원** — *"게임용 칩 회사로 시작"*, *"30년 전 데니스"* 는 **진행자**의 말(37:44~37:52).
- 진행자: *"세계에서 가장 가치 있는 회사"*(12:48~12:52) — ⚠️ 진행자 진술.

→ [[jensen-huang]] · [[tech-bridge-jensen-huang-cbs-interview]]

## OpenShell · BlueField — 에이전트 격리와 대역 밖 감시 (2026-10-09 · [[tech-bridge-white-house-superintelligence-panel]])

CEO [[jensen-huang|Huang]]의 백악관 패널 발언. 진행자가 *"the open agent safety framework from Nvidia"*(12:20~12:26)를 언급하고 Huang이 **두 기술**로 답한다:

| 이름 | 역할 (Huang의 설명) | en-orig |
|---|---|---|
| **OpenShell** | *"a containment system. It's basically kind of like a browser for websites. It's now essentially a browser of agents"* — 에이전트를 나머지 컴퓨터로부터 격리, *"the rights that you give it are only the rights it should have"* | 14:27~14:47 |
| **BlueField** | *"a new chip called Blue Field and it it just keeps an eye on everything that the agent is doing at all times"* — 정책 위반 시 escalate | 14:47~15:05 |

설계 원칙: 평가·배포 모두 **격리 + 실시간 감시**, 감시는 *"another another chip (…) out of band (…) outside the sandbox"*(13:42~13:57). → [[agent-governance-layers]]

- ⚠️ **프레임워크의 공식 명칭은 진행자 발화뿐**이고 이 위키에 NVIDIA 1차 문서가 없다. BlueField가 무엇을 관측·판정하는지, OpenShell의 권한 모델은 발화되지 않았다. ko는 BlueField를 **"블루필드라는 사람"** 으로 옮겼다(14:50).
- 같은 패널: **SI 공장**(데이터센터 → 공장) · **궤도 컴퓨팅**에 *"Putting Nvidia computing in space"*(07:30~07:32, 추정) → [[orbital-compute]] · Rubin(*"Reubens"*, 05:13, ⚠️ 판독 추정 — Musk의 언급).

## CEO의 코리아 소사이어티 갈라 — 자사주·금융사·한국 협력, 안전 플랫폼 (2026-10-09 · [[tech-bridge-jensen-huang-korea-society-gala]])

> ⚠️ 아래 수치는 **전부 진행자의 진술**이고 Huang은 확인도 부정도 하지 않는다. 이 위키는 원 자료를 보지 않았다.

- **자사주 매입** — 그날 아침 WSJ 헤드라인 *"an historic stock buyback, $150 billion, um, to the total of 235 billion"*(00:10~00:19). *"to the total of"* 의 기준(누적 승인액 등) 미발화.
- **금융사 파트너십** — Apollo·Blackstone·BlackRock·Goldman Sachs·KKR, *"to the tune of about a half a trillion dollars of investment"*(00:30~00:48). Huang: *"I'm your largest customer all of you"*(00:42).
- **한국 협력사** — Samsung·SK·Hyundai·Naver(*"most recently. You signed a big package"*)·LG·Doosan(04:22~04:31).
- **"open agent safety platform"** — *"You just launched a platform this morning (…) to help developers test and deploy"*(12:47~12:55). [[tech-bridge-white-house-superintelligence-panel|백악관 패널]]의 *"open agent safety framework"* 와 같은 발표로 추정(⚠️ 명칭 갈림, 공식 문서 없음).
- **창립 연도** — LinkedIn *"Nvidia, 1993, present"*(진행자 낭독, 08:50~08:57), Huang *"33 years old, almost 34 years old"*(10:19~10:22).

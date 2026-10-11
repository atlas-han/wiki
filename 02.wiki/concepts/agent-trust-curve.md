---
title: 신뢰 곡선 (Agent Trust Curve)
type: concept
category: framing
tags: [trust, parallelism, adoption, management, agents]
aliases: [trust curve, 신뢰 사다리, 병렬성은 신뢰의 함수]
related: [agent-manager-analogy, agent-verification-skill, behavior-validated-trust, persistent-agent-teams, cloud-agent-delegation, hard-vs-soft-enforcement, taste-vs-judgment]
first-seen: tech-bridge-lauren-tan-trusting-agents
sources: [tech-bridge-lauren-tan-trusting-agents, tech-bridge-lauren-tan-2000-prs, tech-bridge-lauren-tan-agent-dev-workflow, tech-bridge-jensen-huang-korea-society-gala, tech-bridge-tessl-harness-engineering-factory]
created: 2026-09-13
updated: 2026-10-11
---

# 신뢰 곡선

**얼마나 많은 에이전트를 병렬로 굴릴 수 있는가는 모델의 함수가 아니라 신뢰의 함수다.** [[lauren-tan]]이 [[tech-bridge-lauren-tan-trusting-agents]]에서 그린 (본인 말로 *"과학적이지 않은"*) 차트의 이름.

> **하나의 출력조차 못 믿는데 100개를 띄울 수는 없습니다.**

## 구간

| 구간 | 상태 |
|---|---|
| **깊이 in-loop** | 한두 개의 에이전트. **모든 출력을 지켜보고 앉아서 프롬프트.** 그 이상 병렬화 불가 |
| **중간** | 검증 스킬을 짓고 관찰하며 실패 모드를 스킬로 흡수 → [[agent-verification-skill]] · [[pstack]] |
| **클라우드 위임** | 에이전트가 신호(버그 리포트)를 스스로 집어 PR로 돌려준다 → [[cloud-agent-delegation]] |
| **자동 병합** | **에이전트가 PR을 병합하고 사람은 main에서 사후 리뷰.** *"오늘 일어나 보니 PR 20개가 이미 랜딩돼 있었고 좋았습니다"* |

## 왜 곡선인가 — 지름길이 없다

> **여기서 저기로 가는 지름길은 정말 없습니다.** 이건 **여러분 개인의 에이전트 신뢰 수준**에 관한 것이니까요.

> **아직 이 구간에 있다면 지금 당장 수백·수천 개의 클라우드 에이전트를 띄우려고 뛰어들지 마세요** — **토큰을 엄청나게 낭비**하게 되고 **극도로 비쌉니다.**

**신뢰가 개인적이고 이전 불가능하다는 것**이 이 개념의 특징이다. 도구(예: [[pstack]])는 속도를 올려 주되 대신해 주지 않는다:

> **저를 믿고 Pstack을 믿으면 연장선에서 에이전트를 믿을 수 있겠지만, 저를 안 믿으신다면 — 그리고 저를 맹목적으로 믿으시라고 권하지 않습니다 — 직접 스킬 세트를 만드시면 됩니다.**

## 신뢰를 잃는 메커니즘

> 에이전트가 **되는대로 하고, 추측하고, 환각을 일으키고, 백 번째로 "결정적 증거를 찾았다"고 자신 있게 말하는데 실제로는 진짜 문제가 아닌** 걸 보면 **신뢰를 많이 잃습니다.**

결정적 관찰은 **도구 호출을 열어 봤을 때** 나왔다 — *"실제 도구 호출을 보니 제가 영향받았을 거라 생각한 코드를 읽고 있지도 않았습니다."* → [[agent-action-record]]

## 관리 유비

신뢰가 없는 매니저의 모드는 **마이크로매니지먼트**다 — 어깨너머를 들여다보는 데 시간을 쓴다. → [[agent-manager-analogy]]

## 위키의 다른 페이지와 맞닿는 자리

- **[[behavior-validated-trust]]** — *신뢰의 근거가 작성자에서 검증된 행동으로* 옮겨간다는 프레이밍의 **개인 경로 판본**. 이 곡선은 그 전환이 **사건이 아니라 과정**임을 말한다.
- **[[persistent-agent-teams]]** — 곡선의 오른쪽 끝이 그 그림이다. 이 페이지는 **거기 도달하는 방법**을 채운다.
- **[[taste-vs-judgment]]** — 화자가 곡선을 오르는 데 필요한 것을 *"취향과 판단"* 이라고 부른다. 그 페이지의 네 입장에 **다섯 번째**가 붙는다: 판단은 **에이전트를 신뢰할지 결정하는 일**이다.
- **[[trusted-throughput]]** — ⚠️ 긴장. 이 소스의 PR 수치(1,000 / 800)는 그 페이지가 경고한 **Goodhart 지표의 모양**이다. 화자 본인이 *"이 코드 중 실제로 좋은 게 얼마나 되냐고 물으실 겁니다"* 라고 먼저 인정하지만 **답은 자기 신뢰뿐이다.**

## 표시해 둔 것

> ⚠️ **모든 수치가 자기 보고**이고, **자동 병합의 안전망**(회귀가 빠져나간 사례·롤백 빈도)이 소스에 없다. 같은 화자가 *"agents window는 계속 회귀한다"* 고 말하는 것과 나란히 둘 수밖에 없다.

## References

- [[tech-bridge-lauren-tan-trusting-agents]] · [[lauren-tan]] · [[agent-verification-skill]] · [[agent-manager-analogy]] · [[behavior-validated-trust]] · [[persistent-agent-teams]] · [[pstack]]

## 첫 구간이 가장 빠져나오기 어렵다 (2026-09-26 · [[tech-bridge-lauren-tan-2000-prs]])

같은 화자의 녹화 발표는 곡선을 **본인 여정**이 아니라 **청중의 위치 진단**으로 쓴다. 곡선의 이름도 *"trust graph"*(35:33~35:35).

> 저도 처음엔 **1~5개 범위**에 있었습니다. **모든 채팅을 베이비시팅해야 한다고 느끼고** (…) 저는 **이 단계가 사실 빠져나오기 가장 어렵다**고 주장하고 싶습니다. **어떻게 빠져나오는지가 항상 분명하지는 않으니까요.** (05:25~06:09)

> **신뢰 없이 서브에이전트나 cloud agent를 100개 띄우면** 금세 **슬롭 PR, 회귀, 버그**가 잔뜩 배포됩니다. (06:25~06:40)

그리고 **곡선을 오르는 방법이 한 동작으로 압축**됐다 — **교정할 때마다 [[hard-vs-soft-enforcement|다섯 층]] 중 가장 효과적인 곳에 심는다.** 오른쪽 끝의 모습도 달라졌다: 09-12의 *"자동 병합 → main에서 사후 리뷰"* 대신 *"환경을 너무 신뢰하게 돼서 **에이전트가 그냥 자유로워질 수 있는** 곳"*(37:17~37:28).

> ⚠️ 수치는 **지난달 PR 2,000건**으로 두 배가 됐고, 09-12의 유보(PR 크기 모름·맹목적 신뢰 경계·자동 병합의 안전망 부재)는 **이번 발표에 하나도 없다.** 위 [[trusted-throughput]] 긴장은 그대로다.

## "신뢰의 사다리" — 해설의 요약 (2026-10-09 · [[tech-bridge-lauren-tan-agent-dev-workflow]])

Tech Bridge 해설은 원본 대담에서 *"신뢰의 사다리"*(ko 00:57~00:59, en-orig 번역 *"ladder of trust"*)가 나온다고 전하고, 요지를 이렇게 옮긴다: *"여러 작업을 맡길 수 있다는 신뢰는 자신 있는 답변보다 실제 결과를 확인하고 잘못됐을 때 다시 고칠 수 있는 환경에서 생긴다"*(ko 01:02~01:08). ⚠️ **발췌에는 Lauren이 이 말을 하는 음성이 없다** — 내레이터의 요약이다.

본인 발화로 남은 것은 곡선을 오르는 비용에 대한 유보다 — *"it's very hard to get to this point (…) it takes a lot of time and effort to think about your code and where you see your agents failing"*(10:12~10:29). 위 09-25 절의 *"첫 구간이 가장 빠져나오기 어렵다"* 와 같은 방향이다.

## 같은 사다리, 다른 승급 조건 — 능력 vs 행동 (2026-10-09 · [[tech-bridge-jensen-huang-korea-society-gala]])

[[jensen-huang|Jensen Huang]]도 사다리를 그린다: 직원·아이가 똑똑해질수록 *"you would give them larger and larger boundaries to explore"*(16:53~17:01), AI는 *"I give you no rights"* 에서 시작해 *"based on the job that I want you to do and your capabilities"* 만큼 넓힌다(17:38~17:51). 

> ⚠️ **승급 조건이 다르다.** 이 페이지의 [[lauren-tan|Lauren Tan]]은 **관찰된 행동**(지름길 없음, 신뢰를 잃는 메커니즘)으로 오르고, Huang은 ***능력*(*"because its capabilities deserve it"*)** 으로 오른다. 능력이 늘어도 행동이 확인되지 않으면 어떻게 하는가 — Huang의 답은 사다리가 아니라 **두 번째 원칙(모든 AI 감시)** 이다. 두 화자 모두 이 차이를 말하지 않는다(위키의 관찰).

## autonomy ≠ automation — 정답률과 신뢰를 다른 축으로 (2026-10-11 · [[tech-bridge-tessl-harness-engineering-factory]])

[[dru-knox|Dru Knox]]([[tessl|Tessl]])는 이 곡선이 말하는 *신뢰* 를 **정답률과 분리된 축**으로 정의한다: *"You can have high autonomy in the sense that agents frequently are oneshotting the problems you're giving them, but low automation because you don't trust it yet. And so you're reviewing all of the code directly."*(03:30~03:43) — autonomy는 사람이 몇 번 고쳐야 하느냐, automation은 *"How much do you need to review or build trust in the solution before you accept it?"*(03:23~03:27). 그리고 *"You have to build up autonomy first before you can move to automation."*(03:47~03:52) 이 곡선의 *병렬 수 = 신뢰의 함수* 에 **신뢰를 올리는 장치**(PR 뒤의 비싼 검사 = outer loop, *"encode things that otherwise a human would have to verify"* 07:22~07:30)가 붙는다 → [[inner-outer-meta-loops]]. 출발점도 이 곡선의 중간 — *"a couple sessions at a time"*, 쉬운·중간 과제에서 *"frequently do the right thing"*(00:45~01:02). ⚠️ 측정 없음, 벤더 화자.

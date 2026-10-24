---
title: "Tech Bridge — 클로드가 먼저 일한다 | Claude Duet의 기능과 한계 (한국어 해설 + 출처 미상 발췌): 아침 요약·먼저 오는 알림, 클라우드에서 몇 시간마다 확인, 보내기·결제·서명·삭제 전 승인, 사용량 한도 공유"
type: source
tags: [claude-duet, anthropic, proactive-assistant, always-on-agents, personal-agent, approval-gate, action-reversibility, sensitive-data, usage-limits, claude-opus-5-5, commentary-format, secondhand-claims, video]
source-url: https://www.youtube.com/watch?v=BfHkp3dz2gc
source-type: video
author: Tech Bridge (한국어 해설, 내레이터 미상) · 영어 원음 발췌 여러 구간 — **화자·출처 미상**(설명란에 원본 링크 없음)
date-published: 2026-10-23
ingested: 2026-10-24
created: 2026-10-24
updated: 2026-10-24
---

# Tech Bridge — 클로드가 먼저 일한다 | Claude Duet의 기능과 한계

[[tech-bridge|Tech Bridge]]가 올린 **6:06, 공식 챕터 10** 영상. [[anthropic|Anthropic]]의 새 비서 [[claude-duet|Claude Duet]]을 소개한다 — 사용자가 묻기 전에 연결한 앱에서 *지금 봐야 할 일*을 골라 알리고, 초안까지 준비하되 **밖으로 나가는 행동은 승인을 기다린다.** 형식은 한국어 해설 + 영어 원음 발췌인데, **설명란에 원본 링크가 없고 발췌 화자를 아무도 밝히지 않는다** — 이전 해설 편들과 다르다.

> **(해설의 줄거리)** *"먼저 알려주는 것과 마음대로 처리하는 건 다른 얘기죠. 무엇을 맡길 수 있고 어디서 내 결정을 기다리는지 살펴볼게요."*(00:08~00:16) → 맺음: *"모든 앱을 연결하기보다 놓치기 쉬운 업무 하나부터 맡겨보는게 좋겠죠. 예를 들면 미확인 메시지를 모으고 답장 초[안]까지만 준비하게 하는 거예요."*(05:32~05:44)

> 원음(화자 미상): *"before it sends a message, makes a payment, signs a document, or deletes anything, it shows you what exactly it's about to do and waits for your approval."*(02:45~02:53)

이 위키에 생기는 것: [[claude-duet]](신규 — 제품). 기존 페이지에는 [[always-on-agent-architecture]]의 **"몇 시간마다, 쉬지 않고는 아니다(한도 때문에)"**, [[action-reversibility]]의 **4동사 승인 게이트와 승인해도 못 하는 일**, [[agent-attention-management]]의 **"알림이 많아지는 게 아니다"**, [[least-privilege-connectors]]의 **비밀번호·토큰 비노출**, [[claude-opus-5-5]] · [[boris-cherny]] · [[anthropic]]의 새 언급이 붙는다.

**트랙과 인용.** [[tech-bridge-jediah-katz-harness-whats-left]]와 같은 구성 — ko = `lang=ko` 원 오디오 ASR(해설 인용), 발췌는 ko 트랙의 영어 조각과 en-orig를 대조. 상세는 raw.

> ⚠️ **2차 진술만 있다.** 기능 서술의 근거는 해설이 말하는 *"개발사가 소개한"* 사례(00:58, 01:28) · *"공식 도움말"*(02:07) · *"공식 안내"*(03:48) · *"직접 써본 한 리뷰"*(05:02)이고, 발췌 화자는 미상이다. **이 위키는 Anthropic 발표·도움말·리뷰 어느 것도 확인하지 않았다.** 해설 자체 고지: *"저희가 같은 업무로 직접 성능을 시험한 결과는 아니에요."*(01:31~01:36)

## 1. 먼저 오는 비서 — 아침 요약과 알림 (00:00~01:02)

- 원음 ①(00:36~00:45, en-orig): *"also said that op 5.5 and that's a model that's going to decide what needs what [?] with you first."* — *op 5.5* = [[claude-opus-5-5|Opus 5.5]]로 읽힌다(판독). 앞부분 00:20→00:36 무캡션.
- (해설) *"중요한 건 알림이 많아지는게 아니에요. 흩어진 일정과 메시지에서 지금 내가 봐야 할 일을 골라주는 거죠. 급하지 않은 일까지 계속 부르면 오히려 방해가 될 수 있어요."*(00:45~00:55) → [[agent-attention-management]] · [[proactive-idea-feed]]

## 2. 초기 사용자 사례 (01:02~01:41)

- 원음 ②(01:03~01:16): *"[…] CL[aude] code called Boris talks through his to[-do] list with duet while he's out on walks instead of saving it all for his desk. A real estate broker said that one morning without her even asking it flagged a property showing that was on her calendar for the wrong day."* → [[boris-cherny]](⚠️ *Boris*만, 성 없음 — 동일인 추정하지 않음)
- (해설) *"방금 사례는 개발사가 소개한 사용자 경험이에요."*(01:28~01:31)

## 3. 기억·스킬·앱 이어 쓰기, 클라우드 컴퓨터 (01:41~02:59)

- (해설) 기존 Claude의 기억·연결 앱을 이으면 *"처음부터 다시 설명할 일을 줄일 수"* 있고, 공식 도움말에 *"주제별 채널도 따로 만들 수 있다"*(02:02~02:12). 원음 ③은 무캡션. → [[agent-memory]]
- (해설) *"휴대폰을 내려놓거나 노트북을 꺼도 맡긴 일은 계속 될까요? 실제로 일하는 컴퓨터가 어디 있는지 보면 답이 나와요."*(02:13~02:21)
- 원음 ④(02:33~02:53): *"Grockbot dots all.[?] It goes [?] connected accounts every few hours instead of non-stop because if it was doing this non-stop, it would burn through your limits a lot faster obviously."* + 위 승인 인용. ⚠️ *"Grockbot dots all"* 은 [[grokbot]] · [[openai-dots]] 비교일 수 있으나 판독 불가 — 해석하지 않는다.
  - → [[always-on-agent-architecture]]: 상시 에이전트가 **연속 감시가 아니라 주기 확인**을 택하고, 그 이유가 **사용량 한도**다.

## 4. 승인 경계 — 준비는 AI가, 실행은 사람이 (02:59~03:24)

- (해설) *"읽고 정리하고 초안을 만드는 일은 먼저 진행해요. 하지만 밖으로 보내거나 결제하거나 지우기 전에는 할 일을 보여주고 승인을 기다려요. 주식거래나 계좌[ 간] 송금처럼 승인해도 할 수 없는 일도 있고요."*(02:59~03:17)
  - → [[action-reversibility]]: **보내기 · 결제 · 서명 · 삭제** = 되돌리기 어려운 4동사에 게이트. 그 위에 **승인으로도 열리지 않는 금지 층**이 하나 더 있다. [[no-silent-write]]와 같은 방향.

## 5. 민감정보 보호 (03:24~04:20)

- 원음 ⑤(03:25~03:36): *"[…] says that CL[aude] duet never directly sees your passwords or any of your sign[-in] tokens and they added a new safety check that refuses to share anything like credit card numbers or government ids other sensitive information"* — 주어 잘림. → [[least-privilege-connectors]] · [[credential-injection-outside-sandbox]]
- (해설) *"문제가 절대 생기지 않는다는 보증으로 받아들이면 안 돼요. 공식 안내도 대화를 잘못 읽거나 급한 일을 잘못 판단할 수 있다고 말해요. 연결할 수 있는 앱의 수보다 내가 맡길 업무에 잘 맞는지가 중요하겠죠."*(03:46~03:59) 업무 예시 구간(04:01~04:20)은 무캡션.

## 6. 사용량 한도 (04:20~04:56)

- (해설) *"여러 앱을 오가며 일하려면 뒤에서 여러 번 생각하고 확인해야 해요. 그래서 요금[제]에 포함된다는 말과 한도 없이 계속 일한다는 말은 달라요. 정기적으로 살펴보는 일도 사용량을 쓰거든요."*(04:20~04:34) 원음 ⑦은 조각뿐(*"background … those limits. Bigger tasks … even more of your tokens"*). 챕터명: *"기존 Claude와 공유하는 사용량 한도"*.

## 7. 초기 사용 경험과 첫 과제 (04:56~06:06)

- (해설) *"직접 써본 한 리뷰는 먼저 알려주는 정도가 아쉬웠다고 말했어요. 다만 알림을 켜지 않아서였는지는 자신도 모르겠다고 덧붙여요."*(05:02~05:10) — 리뷰 출처 미상, 원음 ⑧은 조각뿐.
- (해설) *"아직은 미국의 유료 요금제 사용자 대기 명단으로 여는 시험 버전이라 한국에서 바로 쓸 수 있는 건 아니에요."*(05:44~05:52)

## 이 위키와의 연결

### 이어지는 것

- **개인 상시 비서가 셋째 회사에서.** [[grokbot]](Cursor/SpaceX) · [[openai-dots|Dots]](OpenAI) · [[muse]](Meta)에 이어 Anthropic의 같은 범주. 공통 구성 — 자체 클라우드 컴퓨터, 연결한 앱, 먼저 말 걸기 — 은 [[always-on-agent-architecture]]에 이미 정리돼 있다.
- **[[always-on-agent-architecture]] — "알림 heuristic"의 제품판.** Lee Robinson의 *"It knows when to be quiet"* 과 해설의 *"급하지 않은 일까지 계속 부르면 오히려 방해"* 가 같은 요구다. 여기에 **주기 확인 + 한도**라는 비용 쪽 제약이 새로 붙는다.
- **[[action-reversibility]]** — 동사 목록으로 명시된 게이트, 그리고 승인 불가 영역.
- **[[tech-bridge-jediah-katz-harness-whats-left]](같은 날 업로드)** — Katz의 *"메일을 언제 보내도 되는지"* 와 *"API 키 파일"* 이 이 제품에선 승인 게이트·비밀 비노출로 나온다. 두 편을 함께 읽으면 *남는 하네스*(권한·실행 환경·비용)의 제품 사례가 된다.

### 갈리는 것

> ⚠️ **"먼저 알려 준다" vs 초기 리뷰.** 발표(해설 전언)는 선제 알림이 핵심인데, 해설이 전한 리뷰는 *"먼저 알려주는 정도가 아쉬웠다"* — 단 알림 설정 탓일 수 있다고 리뷰어 스스로 유보. 해소하지 않는다.

## 해소하지 않고 표시만 한 것

- 발췌 전 구간의 화자와 원본(발표 영상인지 리뷰 영상인지).
- *"op 5.5"*(Opus 5.5 판독), *"Grockbot dots all"*, *"CL code called Boris"* 의 앞부분.
- 무캡션 00:20→00:36 · 01:42→02:02 · 04:04→04:20.
- 공식 도움말·안내, 리뷰 — 열어 보지 않았다. 출시일·요금제 범위.

## 등장 개체

- 제품: [[claude-duet]](신규) · [[claude-code]] · (비교 추정) [[grokbot]] · [[openai-dots]]
- 모델: [[claude-opus-5-5]](판독)
- 조직: [[anthropic]] · Tech Bridge
- 인물: [[boris-cherny]](*Boris*만 — 동일인 미확정)
- 개념: [[always-on-agent-architecture]] · [[action-reversibility]] · [[agent-attention-management]] · [[least-privilege-connectors]]

## References

- 원본 영상: <https://www.youtube.com/watch?v=BfHkp3dz2gc> (6:06, `upload_date` 2026-10-23)
- raw: `01.raw/articles/2026-10-23_클로드가 먼저 일한다 - Claude Duet의 기능과 한계.md`
- 원본·공식 링크: 설명란에 없음
- [[tech-bridge]] · [[claude-duet]] · [[anthropic]]

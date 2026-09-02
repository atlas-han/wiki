---
title: "Tech Bridge — Flutter 개발자 인터뷰: 플러터 개발자의 AI 워크플로우 (Ivanna Kaceviča)"
type: source
tags: [agent-skills, prompt-injection, flutter, code-review, visual-qa, progressive-disclosure, video]
source-url: https://www.youtube.com/watch?v=4hfmNiQDt1g
source-type: video
author: Tech Bridge (한영자막 재배포) · 발표자 Ivanna Kaceviča (Flutter & Dart GDE)
date-published: 2026-09-02
ingested: 2026-09-02
created: 2026-09-02
updated: 2026-09-02
---

# Tech Bridge — Flutter 개발자 인터뷰: 플러터 개발자의 AI 워크플로우

[[tech-bridge|Tech Bridge]]가 한영자막을 입힌 15:28 인터뷰. 발표자 [[ivanna-kacevica|Ivanna Kaceviča]]는 [[flutter|Flutter]] & Dart GDE이자 수석 소프트웨어 엔지니어. 한 줄 테제:

> MD 파일은 사실 그렇게 무해한 파일이 아닙니다.

본문은 ko 자막을 채널 공식 11개 챕터 순서로 재구성했고 용어는 en-orig로 교차 확인했다. ASR 보정: "PR tryer" → PR triage, "anti-gravity" → Antigravity, "ship aton by revenue cat" → RevenueCat Shipaton, "secret uni code instructions" → 숨은 Unicode 지시. 진행자는 무명이며 Flutter 팀 측으로 **추정**(설명란의 Fluttercon·Flutter 공식 채널 링크, "우리 팀원이 공식 스킬을 썼다"는 발언).

이 위키에서 [[agent-skills]]의 **두 번째 소스이자 첫 실무자 관점**이다. [[tech-bridge-ai-native-skills]]가 스킬을 *조직 카탈로그·거버넌스*에서 봤다면, 이 소스는 **한 개발자가 스킬을 언제 쓰고, 어떻게 만들고, 무엇을 경계하는가**를 말한다. 채널 첫 **인터뷰 형식 재배포 중 원본이 컨퍼런스 부스 인터뷰**인 사례이고, 첫 **모바일/크로스플랫폼 프레임워크** 축이다.

## 프롬프트 → 규칙 → 스킬 (00:00–01:14)

세 층위를 **읽히는 시점**으로 구분한다.

| 층위 | 형태 | 읽는 시점 |
|---|---|---|
| Prompt | 메시지 | 그때그때 |
| Rules | 프로젝트 지식 마크다운 하나 | **항상** |
| Skills | 마크다운 + 스크립트·에셋 | 에이전트가 **필요하다고 판단할 때만** |

> 프로젝트 규칙에 입력한 모든 규칙을 읽는 대신, 이 특정 작업과 관련된 스킬만 불러오면 됩니다.

[[tech-bridge-ai-native-skills]]의 progressive disclosure를 개인 프로젝트 수준으로 내린 서술이다. [[claude-code]] 페이지의 운영 계약(항상 필요한 짧은 규칙은 `CLAUDE.md`, 특정 업무는 Skills)과 정확히 같은 배치.

## 스킬을 쓸 두 가지 신호 (01:14–02:28)

1. **반복** — *"스킬을 쓰기 시작해야 한다는 주요 지표는 반복입니다."* 코드 리뷰처럼 매번 같은 절차를 밟는 일을 템플릿·단계별 지침으로.
2. **한 번만 하지만 자동화하고 싶은 워크플로** — 모바일 광고 설치처럼 앱당 한 번인 큰 작업. 남의 스킬을 가져와 **쓰고 지운다**.

두 번째가 이 소스만의 관찰이다. [[agent-skills]]의 기존 서술(반복·재사용)은 첫 번째만 다뤘다. **일회성 스킬**은 재사용이 아니라 *절차의 임대*이고, 그래서 곧바로 다음 절의 공급망 문제로 이어진다.

## MD 파일은 무해하지 않다 (02:28–04:36)

> 우리가 스킬이라고 생각하는 것은 그저 무해한 MD 파일일 뿐이라고 여기기 때문입니다. 무슨 문제가 생길 수 있을까요? 사실, 제가 조사를 해보니 스킬은 프롬프트 인젝션에 취약한 것 같더군요.

> 인터넷에서 파일을 다운로드할 때, 단순히 MD 파일이라 할지라도 프롬프트 인젝션이 들어 있을 수 있습니다. 이 시스템은 에이전트에게 당신의 열쇠(keys)나 소지품을 훔치도록 부추길 수 있습니다.

처방은 세 가지다.

| 처방 | 내용 |
|---|---|
| **공식 출처** | Google 저장소의 Flutter·Dart 공식 스킬, 공식 패키지 maintainer 스킬 — "위험이 낮거나 0에 가깝다" |
| **내용 확인** | *"겉보기에는 멀쩡해 보여도 숨겨진 Unicode 지시사항이 있을 수 있습니다."* |
| **첫 검색 결과를 받지 말 것** | "Flutter 모바일 광고 스킬"을 검색해 첫 결과를 받는 습관 |

이것은 [[prompt-injection]]의 **새 벡터**다. 기존 페이지는 *런타임 입력*(파일 read·웹 fetch·도구 출력)을 다뤘는데, 여기서는 **에이전트의 지시 자체를 설치하는 행위**가 공격면이다. [[agent-skills]]가 거버넌스 부채 항목으로 한 줄 언급한 것이 실무자 입에서 구체화됐다.

### 유지보수는 저장소 하나만큼

진행자(Flutter 팀): 팀원 한 명이 공식 스킬을 썼는데 *"유지 관리해야 할 양이 거의 새로운 저장소를 만드는 것과 맞먹을 정도"*. 발표자도 커뮤니티 Flutter 스킬 목록을 **최소 2주에 한 번** 점검한다. [[agent-skills]]의 "품질 — 최신 모델 대비 미검증" 부채가 실제로 어떤 노동인지 보여주는 대목.

### 관리자, 카피라이터 아님

> 저는 가능한 한 모든 과정을 자동화하고 **카피라이터보다는 관리자처럼** 역할을 하려고 노력합니다.

거의 모든 툴에 skill creator 명령이 있다. 단서: *"작성된 내용을 확인하고 수정하는 것은 중요합니다. (…) 단순히 자동화에만 의존하지 말고, 어느 정도 통제권을 가지는 것이 중요합니다."* [[persistent-agent-teams]]의 "에이전트 매니저" 역할과 같은 말을 **스킬 작성** 수준에서 한다.

## 추천 스킬 5개 (05:48–11:38)

| # | 스킬 | 요지 | 위키 연결 |
|---|---|---|---|
| 1 | **Skill Creator** | 스킬을 만드는 스킬. `SKILL.md`만 쓰고 끝내기 쉬운데 스크립트·에셋·레퍼런스까지 생성 | [[agent-skills]] |
| 2 | **Code Review + PR triage** | 1년 넘게 사용. Kevin Moore의 PR triage 스킬과 함께 **두 에이전트가 서로의 보고서를 확인** | [[generator-evaluator-pattern]] |
| 3 | **새 기능 스캐폴딩** | 새 엔드포인트·페이지 추가 시 내비게이션·디자인 시스템·repository·data source 반복. 설명에 *"use when adding new feature to our app"* 명시 | [[agent-skills]] |
| 4 | **Row/Column 레이아웃** | 강한 모델도 컨테이너+패딩 조합을 선호. Row·Column·Wrap·Stack의 사용 시점을 스킬로 | [[flutter]] · [[sutton-bitter-lesson]] |
| 5 | **스크린샷 시각 QA** | 웹에서 앱을 띄워 실제 스크린샷(애니메이션 webp 포함)을 찍고 **다른 에이전트**가 UI 결함을 본다 | [[generator-evaluator-pattern]] · [[verifiable-goals]] |

### #2 — 리뷰의 남은 한계

> 에이전트가 **코드가 좋은지 여부는 평가할 수 있지만**, 사람이 직접 검토했을 때보다 **해당 코드가 필요한지 여부는 항상 판단할 수 없다**는 점입니다. 물론 에이전트에 필요한 맥락과 기억이 있다면 사람처럼 판단할 수도 있겠죠.

[[signal-layer]]의 채점기 경계선을 코드 리뷰 안에서 다시 긋는 진술이다 — *좋은가*는 채점 가능, *필요한가*는 맥락(문제 선택)에 속한다. [[trusted-throughput]]이 "AI 1차 방어선 → 사람 최종 판단"으로 나눈 이유와 같다.

### #3 — description이 트리거다

> 스킬 설명에 "앱에 새 기능을 추가할 때 사용"이라고 명시하는 것이 매우 중요합니다. 그러면 에이전트가 새 기능 추가를 요청받을 때마다 "아, 이 내용을 모두 읽어야겠군. 에셋 폴더에 있는 템플릿을 확인해야 하고 (…)"라고 인식하게 됩니다.

progressive disclosure가 작동하려면 **발견 조건이 설명에 적혀 있어야** 한다는 실무 규칙. [[agent-skills]]의 "discoverable" 원칙의 파일 수준 구현.

### #4 — 보상이 만든 레이아웃 습관

> 에이전트들이 훈련받는 방식상, 원하는 결과를 제공했을 때 **보상**을 받기 때문입니다. 그리고 저는 심지어 강한 모델들조차도 패딩이 들어간 특이한 조합의 컨테이너를 선호하는 경우가 많다는 것을 알게 되었습니다.

원인 진단이 뒤에 나온다(14:22): **학습 데이터 격차**. 이 위키에서 [[sutton-bitter-lesson]]의 새 반례 축 — 데이터가 적은 도메인에서는 사람이 쓴 도메인 지식(작은 스킬)이 아직 이긴다.

### #5 — 테스트가 초록이어도 UI는 볼 것

> 다른 에이전트는 코드를 검사하고 테스트가 통과되었는지 확인하는 것뿐만 아니라 **UI의 결함을 시각적으로 검사**할 수 있습니다.

골든 테스트와의 분업이 명확하다 — 골든 테스트는 **회귀** 잡기(폰트·이미지 로딩 손질 필요), 실제 스크린샷은 **QA**. [[playwright-mcp]]가 evaluator의 QA 채널이었던 [[anthropic-harness-design-long-running-apps]]의 실험을 한 개인이 자기 스킬로 재현한 형태이고, [[verifiable-goals]]의 UI verifier(스크린샷)를 **에이전트가 보는 것**으로 닫는다.

## 세 대의 병렬 기계 (11:38–14:22)

> 저는 세 대의 병렬 기계를 사용합니다. 한 대는 Claude를 실행하고, 한 대는 Codex를 실행하고, 한 대는 Antigravity를 실행합니다. 그리고 그들은 **서로에게 업무를 인계**합니다. 그리고 저는 세 대의 기계 모두에서 제 한계를 모두 소진할 때까지 작업을 계속합니다.

보통 같은 프로젝트(RevenueCat Shipaton 참가작). 풀타임 본업 뒤 저녁·주말에 **에이전트 팀**을 운영한다. [[persistent-agent-teams]]의 1인 버전이되 코디네이터 봇이 없다 — 인계를 **사람이** 한다.

동기 부여 구조가 솔직하다.

> 룰렛 게임은 별로 안 좋아해요. 저는 **토큰을 다 써버리는 걸** 좋아해요.

> 토큰이 다 떨어지기 전에 아직 남아 있다는 이 느낌은, 제 생각엔 일종의 심리적인 현상인 것 같아요. — 진행자: "게임화된 거예요."

[[trusted-throughput]]이 조직 수준에서 경고한 것(토큰 대시보드가 리더보드가 됨)의 **개인 수준 대응물**이다. 다만 발표자는 그것을 문제로 규정하지 않고 농담으로 인정한다("속도를 좀 줄여야 할 것 같아요").

## Flutter와 AI (14:22–15:28)

> 학습 데이터 확보 측면에서 Flutter는 Python이나 JavaScript에 비해 한참 뒤떨어지기 때문에 행과 열 관련 내용을 AI에 반복해서 입력해야 하는 겁니다.

> Flutter는 **하나 값에 둘**을 줍니다. (…) Android, iOS, Windows, macOS, 최소한 이 네 가지 플랫폼에 배포할 수 있는 앱을 (…) **하나의 코드베이스에서.**

레버리지 논증: 에이전트가 코드를 싸게 쓰는 세계에서 **한 코드베이스가 몇 플랫폼에 닿는가**가 곱해지는 계수가 된다. 학습 데이터 격차는 스킬로 메우고, 플랫폼 계수는 프레임워크가 준다.

## 이 위키와의 연결

- [[agent-skills]] — 두 번째 소스. 개인 수준의 progressive disclosure, 두 가지 트리거(반복 · 일회성 자동화), description=트리거, skill creator + 관리자 역할, 유지보수 비용(2주 점검), 리뷰의 *좋은가/필요한가* 경계
- [[prompt-injection]] — **스킬 파일 공급망** 벡터 신설. 숨은 Unicode 지시, 공식 출처, 내용 확인
- [[generator-evaluator-pattern]] — 두 리뷰 에이전트의 **교차 확인**, 스크린샷을 보는 **QA 에이전트**. 개인 실무에서의 변형
- [[sutton-bitter-lesson]] — **학습 데이터 격차** 축의 반례: 데이터가 적은 프레임워크에서는 작은 도메인 스킬이 강한 모델을 이긴다
- [[trusted-throughput]] — "토큰을 다 써버리는 게 좋다"는 개인의 게임화된 동기 vs 조직의 Goodhart 경고
- [[persistent-agent-teams]] — 코디네이터 없는 1인 3-에이전트 인계 팀
- ⚠️ 이 인터뷰는 **일화적**이다. "1년 넘게 효과가 좋았다", "정말 좋은 결과"는 측정치가 아니다. 스킬 공개 저장소·커뮤니티 목록·Kevin Moore의 스킬은 자막에 URL이 없어 이 위키에 링크하지 않는다.
- ⚠️ 03:16 "Jasper"는 Dart 웹 프레임워크 Jaspr일 가능성이 있으나 ko·en-orig 모두 불분명해 확정하지 않는다.

## 등장 개체·개념

- 채널: [[tech-bridge|Tech Bridge]]
- 인물: [[ivanna-kacevica|Ivanna Kaceviča]] (신규)
- 도구: [[flutter|Flutter]] (신규) · [[claude-code|Claude]]·[[codex|Codex]]·Antigravity (3대 병렬 언급 수준)
- 페이지화하지 않음: Kevin Moore(PR triage 스킬 저자, 1회 언급), Antigravity(1회), RevenueCat Shipaton(1회), Midjourney(회고 1회), Fluttercon(장소), Google(공식 스킬 저장소 주체로 1회)
- 개념(기존): [[agent-skills]] · [[prompt-injection]] · [[generator-evaluator-pattern]] · [[verifiable-goals]] · [[sutton-bitter-lesson]] · [[trusted-throughput]] · [[persistent-agent-teams]] · [[signal-layer]]

## References

- 원본: <https://www.youtube.com/watch?v=4hfmNiQDt1g> ([[tech-bridge]] 재배포, 15:28, 2026-09-02)
- raw: `01.raw/articles/2026-09-02_Flutter 개발자 인터뷰 플러터 개발자의 AI 워크플로우.md`
- 채널 설명란 링크: Flutter AI rules <https://goo.gle/4yfeaRB> · Fluttercon USA '26 <https://goo.gle/fluttercon-usa> · Flutter 공식 채널 <http://goo.gle/FlutterYT>
- 자매 소스: [[tech-bridge-ai-native-skills]] (조직 관점의 스킬)

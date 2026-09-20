---
title: Greg Brockman
type: entity
category: person
tags: [openai, founder, president, agi, security, infrastructure]
aliases: [Greg Brockman, 그렉 브록먼]
links:
  - https://x.com/gdb
  - https://gregbrockman.com/
sources: [tech-bridge-brockman-agi-era-defender-window]
created: 2026-09-20
updated: 2026-09-20
---

# Greg Brockman

[[openai|OpenAI]]의 **공동창업자 겸 사장(president)**. 본 위키에는 [[tech-bridge-brockman-agi-era-defender-window]]([[a16z]] 팟캐스트, 2026-09-19 업로드)로 첫 등장한다. **이 위키의 OpenAI 1인칭 소스가 [[sam-altman]] 한 사람에서 두 사람으로 늘어난 자리**다.

> ⚠️ **1인칭 소스 하나뿐이고, 반대 심문이 거의 없는 대담이다.** 아래는 전부 본인 진술이다.

## 소스에서 확인되는 것

| 항목 | 내용 |
|---|---|
| **경력** | *"Stripe 초창기를 만드는 데 기여했고, 물론 OpenAI를 공동 창업"* — 진행자 서술, 본인 부정 없음 |
| **현재 초점** | *"지난 2년간은 데이터센터, 인프라, 머신러닝 엔지니어링"* → **올해는 "사업"** (45:51~46:24) |
| **일하는 방식** | *"참호에서 이끄는 것(lead from the trenches)을 좋아한다"* · *"잠깐, 이게 아직도 말이 되나?"* 를 계속 묻는다 (46:46~47:01) |
| **혼란 해소 방법** | *"코끼리의 서로 다른 부분을 만질 수 있는 사람을 전부 통화에 모으자"* — Hangout + 구글 문서로 문장 단위 검토 (47:08~47:20) |
| **좋아하는 경영서** | **『The Score Takes Care of Itself』** — *"당신은 결과에 영향을 줄 수 없고 오직 입력에만 영향을 줄 수 있다"* (45:24~45:36) |
| **개인 사이트** | `gregbrockman.com` (정적 사이트, 블로그 글 몇 개) — ⚠️ **자막이 세 갈래로 깨뜨렸다**(*gregarin* · *gregroman* · *Craig Brockman*) |

## 이 위키에 남긴 것

### "우리는 AGI 시대에 있다" — 선언의 내용은 공정이다

[[agi-definition]]의 **네 번째 입장**. 앞의 셋([[andrew-ng]]·[[sam-altman]]·[[jensen-huang]])이 전부 *용어가 무의미하다* 로 수렴한 자리에서, Brockman은 **무의미함에 동의하면서 선언을 한다** — 그리고 선언이 가리키는 것이 모델의 속성이 아니다:

> **그것이 이 모델인지, 이전 모델인지, 다음 모델인지는 논쟁할 수 있습니다. 상관없습니다. 요점은 … 안전·보안·정렬을 배포 시점만이 아니라 개발 시점과 평가까지 거슬러 올라가 정말로 생각해야 한다는 것입니다.** (47:48~48:02)

→ [[pacing-the-frontier]]

### 방어자의 창

이 위키에서 **보안을 회사 전략의 축으로 세운 첫 화자**다 — [[defenders-window]]·[[defense-factory]]·[[ai-formal-verification]]이 전부 이 소스에서 나온다. 특징은 **보안을 사건이 아니라 상시 파이프라인으로 놓는다**는 것, 그리고 **완료 기준이 "포화"** 라는 것이다(*"[[openai-astra|Astra]]가 찾아낼 만큼 똑똑한 모든 P0를 다 찾았다"*).

### 개인 규모의 같은 루프

자기 웹사이트를 [[codex|Codex]]로 펜테스트해 **15분에 13건 발견, 45분에 수정**(SPF·HTTPS 강제·[[cloudflare|Cloudflare]] Pages 마이그레이션·DMARC 48시간 자동화)한 일화를 든다. **발견보다 수정이 세 배 걸렸다**는 것이 이 위키의 [[verification-bottleneck]] 옆에 **교정 병목**을 놓는다. → [[ai-vulnerability-discovery]] · [[scheduled-agent-automations]]

### "약속받았던 AI는 텍스트 상자가 아니었다"

자사 주력 제품에 대한 가장 직접적인 비판이 본인 입에서 나온다(40:56~41:24) — 그리고 그가 나열하는 요구 사양(음성·지속성·기억·컨텍스트·능동성)이 **[[mark-zuckerberg]]의 [[muse|Muse]] 사양과 거의 그대로 겹친다.** → [[capability-discovery-burden]]

### 인간의 자리

> **사람은 과제를 할 수 있어서 가치 있는 게 아닙니다. 우리는 우리가 사람이기 때문에 가치 있습니다.** (25:44~26:12)

[[named-human-accountability]]가 09월 내내 *운영상의 안전장치* 였는데, 여기서 **보존해야 할 가치 근거**로 뒤집힌다. → [[ai-jobs-impact]]

## 역사적 일화 — GPT-3와 2019년 12월

> **[GPT-3]를 훈련시켰던 게 2019년 12월 초로 기억합니다.** … **아무도 그것이 무엇을 할 수 있는지 탐구하지 않는 하루하루가 세상에 잃어버린 날입니다.** 그래서 저는 **휴가 계획을 사실상 전부 취소했습니다.** … **숫자 목록을 정렬하는 법을 가르치려 했던 기억이 납니다. 잘 안 됐어요.** (16:57~17:30)

그리고 **2015년 11월 나파 오프사이트**에서 *"환경이 화면 픽셀, 키보드, 마우스인 강화 학습"* 을 이야기했고, **3단계 계획이 이후 10년을 규정했다**고 말한다(22:33~23:04). → [[openai-astra]]의 컴퓨터 사용 계보.

## 미해결 사항

- 직함 외의 프로필(역할의 경계, [[sam-altman]]과의 분업) — 소스에 없다.
- 진행자가 던진 **탈중앙화 소비자 아키텍처** 질문에 **끝내 답하지 않는다.**
- **컴퓨터 사용의 보안 모델**을 한 번도 다루지 않는다 — 보안을 40분 이야기한 대담에서.
- 수치의 근거 전부([[tech-bridge-brockman-agi-era-defender-window]]의 ⚠️ 목록 참조).

## References

- [[tech-bridge-brockman-agi-era-defender-window]] — first-seen
- [[openai]] · [[openai-astra]] · [[sam-altman]] · [[a16z]] · [[ben-horowitz]]
- 관련: [[defenders-window]] · [[defense-factory]] · [[pacing-the-frontier]] · [[agi-definition]] · [[ai-vulnerability-discovery]]
- 외부: <https://x.com/gdb> · <https://gregbrockman.com/>

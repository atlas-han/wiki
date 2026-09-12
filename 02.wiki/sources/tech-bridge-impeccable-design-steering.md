---
title: "Tech Bridge — 디자인은 원샷할 수 없다: 형용사와 동사로 에이전트를 조향하는 Impeccable (Paul Bakaus)"
type: source
tags: [design, agent-skills, steering, taste, ai-slop, harness, control, video]
source-url: https://www.youtube.com/watch?v=PAXtfqAGWpQ
source-type: video
author: Tech Bridge (한영자막 재배포) · 발표 [[paul-bakaus]] ([[impeccable|Impeccable]] 제작자) · 컨퍼런스 세션(행사명 미확정)
date-published: 2026-09-11
ingested: 2026-09-12
created: 2026-09-12
updated: 2026-09-12
---

# Tech Bridge — 디자인은 원샷할 수 없다 (Impeccable)

[[tech-bridge|Tech Bridge]]가 한영자막을 입힌 15:30 단독 발표. 화자는 코딩 하네스([[claude-code|Claude Code]]·GitHub Copilot·[[cursor|Cursor]]·[[codex|Codex]]) 위에서 도는 디자인 스킬 [[impeccable|Impeccable]]을 만든 [[paul-bakaus|Paul Bakaus]]. 도구가 아니라 **만든 접근**에 관한 발표라고 본인이 못 박는다. 한 줄 테제:

> **디자인은 원샷할 수 없다. 픽셀 직접 조작은 고도가 너무 낮고 완전 자율은 슬롭이니, 그 사이에서 형용사와 동사로 조향하되 — 각 단어가 이 프로젝트에서 무엇을 뜻하는지는 스킬이 정의한다. auto는 없다.**

ASR 보정: 결론 문장 *"There is no auto"* 가 ko에서 **"자동차는 없고"** 로(2026-09-10 유형 재발), *coding harness* 가 **"코딩 실력"** 으로, *Leitwort*(독일어)가 en-orig *"light wart"* → ko **"가벼운 사마귀"** 로, *centering a div with Opus* 가 **"차이점을 중심에"** 로, *Instrument Serif* 가 **"악기 세랍 펀"** 으로, *taste* 가 **"미각·맛"** 으로, *bolder* 가 **"굵게"** 로 옮겨졌다. 제품명 *Impeccable* 은 ko가 형용사 "흠잡을 데 없는"으로 번역해 한 문장의 뜻이 바뀌었다. **화자의 자기 정정**(14:38 *"cannot"* → 14:41 *"can be amplified"*)이 ko에서는 보이지 않는다. 전체는 `01.raw/articles/2026-09-11_왜 AI 디자인은 원샷으로 안 될까요.md`.

> ⚠️ **당사자 진술, 독립 확인 없음.** 화자는 Impeccable 제작자. **인센티브는 도구 채택**(라이선스·수익 모델은 소스에 없음). 전후 비교 시연은 슬라이드이고 화자 자신이 *"완벽하지 않다"*, *"여러분이 판단하시라"* 고 유보한다. **정량 근거 전무.** *"같은 모델·같은 하네스에서 언어만 달라 결과가 확연히 다르다"* 는 관찰 진술이다.
>
> **촬영 시점: 2026년 — 화자 발화로 확정**(*"2026년 버전의 AI 슬롭"* 07:38~07:40). 이 채널 소스에서 촬영 연도가 내부 발화로 확정된 첫 사례. 행사는 미확정이며 *"다음 발표자들 중 일부에게는 어색하겠지만"*(14:34)으로 보아 같은 날 업로드된 [[tech-bridge-taste-labs-measuring-slop|Taste Labs 편]]과 **같은 행사·앞뒤 순서일 가능성**이 있으나 확정하지 않는다.
>
> ⚠️ **"Claw Design"**(05:34) — Claude Design 추정. **"algorithmic unilo"**(05:40), **"radian shaders"**(13:13) — 미확정 표기.

## 두 극단과 그 사이

발표의 뼈대. → [[steering-altitude]]

| | **직접 조작** | **중간 고도** | **완전 자율** |
|---|---|---|---|
| 어디서 | **픽셀 공간** — [[figma|Figma]]에서 마진·패딩, Webflow에서 최종 산출물 | 형용사·동사 조향 | *"이거 디자인해 줘"* |
| 문제 | *"대부분의 작업에서 **고도가 너무 낮다**"*(04:44~04:52) · *"Opus로 div 가운데 정렬"* | (탐색되지 않은 지대) | 2022년식 페이지 · **슬롭** — *"아무도 아무것도 결정하지 않은"* |
| 남는 자리 | **맨 처음 탐색 작업** · **마지막 5~20% 폴리시** — *"AI가 사람을 대체할 만큼 좋지 않다"* | 이 도구의 자리 | — |

> 우리가 충분히 탐색하지 않은 **중간 지대**가 있는 것 같습니다 — **정확한 통제 수준은 무엇인가? 사람을 루프에 정확히 맞는 시점에 어떻게 끼워 넣을까?** (04:05~04:17)

## 이 위키에 새로 들어오는 것

### ① 디자인은 원샷할 수 없다 — 그래서 auto는 없다

[[no-one-shot-design]]. 이유는 셋 — **맥락이 풍부해야** 하고(무엇을·누구에게·왜), **멀티샷**이어야 하고(반복), **사람들이 의견을 갖는다**(이해관계자·사용자). 그래서 먼저 물어야 하는 것: *감정적 영역은? 절대 이래선 안 되는 것은? 레퍼런스는? 대상은?* — *"디자인 디렉터가 고개만 끄덕이고 걸어가 버리면 말이 안 된다"*(07:21~07:30).

그리고 이것이 **제품 결정**이 된다.

> **auto는 없고, 앞으로도 auto는 없을 겁니다.** (14:30~14:34)

매주 *"Impeccable이 알아서 다 하게 해 달라"* 는 요청이 오고, 그 이유로 **닫으려는 PR이 서 있다.** *"요점은 원하는 결과를 향해 **조향할 방법**을 주는 것 — 디자인을 원샷하는 도구가 될 일은 결코 없다."* 이 위키가 [[anthropic-claude-code-auto-mode|auto mode]]·[[privacy-auto-mode]]에서 *자동화의 확장* 을 봐 온 것과 **반대 방향의 결정**이고, 근거가 다르다 — 모델이 못 해서가 아니라 **결정하는 것 자체가 디자인**이기 때문이다(*"유능해 보일지 몰라도 완전히 비어 있다"*).

### ② 형용사는 Leitwort — 뒤에 정의가 없으면 그냥 프롬프트

[[adjective-verb-steering]]. 어휘: **bolder · quieter · distill**(단순화) **· polish · denser · harden**(전반에서 동작하게 — 성능·반응형). 같은 모델·같은 하네스에서 엔지니어와 디자이너의 결과가 갈리는 이유가 **언어**라서, 그 언어를 스킬로 압축했다.

> 이 단어들은 여러분이 **의미를 불어넣는** 말입니다. **모델에게 이미 어떤 의미가 있지만, 여러분이 그것을 관심 영역으로 번역**하는 거죠. (11:03~11:16)

> **뒤에 아무것도 없는 형용사는 그냥 좀 더 나은 프롬프트일 뿐입니다.** (13:36~13:42)

*bolder* 의 정의가 그 증거다 — **그라데이션·글래스·네온이 아니라 위계·스케일·결정적 타이포**, 디자인 시스템을 깨지 않으면서. 정의 없이 *"더 bolder하게"* 라고 하면 모델은 *"새 색을 발명하고 새 그라데이션을 발명"* 한다.

그리고 스킬 파일의 실제 문장 — **"누군가에게 보여주고 'AI가 더 bolder하게 만들었다'고 말하라. 그들이 믿으면 실패한 것이다."** 에이전트가 이 기준으로 자기를 돌아본다. [[generator-evaluator-pattern]]이 *생성과 평가를 분리* 하라고 한 것과 달리 **평가 기준을 생성자의 지시 안에** 넣은 형태다. ⚠️ 자기 평가 편향은 소스가 다루지 않는다.

### ③ 슬롭은 움직이는 표적

> **대부분의 프론티어 모델에는 더 이상 보라색 그라데이션이 없습니다.** 지금은 이걸 받죠 — Claude가 말하듯 *"다른 옷을 입은"* 것. 하지만 **이것도 슬롭**입니다. **움직이는 표적**일 뿐이에요. (05:09~05:26)

[[ai-slop]]. 지금의 슬롭은 **"Claude 베이지" · Instrument Serif · 이탤릭** — *"꼭 나쁜 디자인은 아니다. 그냥 전부 그렇게 생겼을 뿐."* 이 관찰이 이 위키의 [[anthropic-harness-design-long-running-apps]]에 직접 걸린다 — 그쪽의 originality 기준이 페널티로 명시한 *"purple gradients over white cards"* 는 이 화자에 따르면 **이미 낡은 예**다. **고정된 슬롭 목록은 낡는다** — 채점 기준에 시간 축이 있다는 뜻이고, [[harness-pruning]]이 하네스 기능에 대해 말한 것이 **평가 기준에도** 적용된다.

### ④ 워크플로를 먼저 매핑하고 주입 지점을 정한다

[[impeccable]]. *"20년 넘게 도구를 만들었고, 만들 때마다 먼저 워크플로를 매핑한다."* 디자인은 선형이 아니라 **초기화/셰이핑 → 제작·반복(형용사·동사) → harden·polish → 디자인 시스템 복귀(기술·디자인 부채 정리)** 이고, 각 단계에 주입 지점이 있다. 반농담으로 만든 `overdrive`(완전히 과한 것)가 커뮤니티에서 살아남은 사례 — *"확신 없는 명령을 커뮤니티로 테스트하고, 정착하면"* — [[skill-self-improvement]]의 *승격은 사람이* 를 **커뮤니티 반응**으로 대신한 형태.

### ⑤ 취향은 증폭되되 배양되지 않는다

> **취향은 증폭될 수 있다**고 생각해요. 저는 이걸 **amplified craft**라고 부릅니다. (…) 하지만 **실험실에서 배양(lab grown)될 수 있다고는 정말로 생각하지 않습니다.** 취향은 정의상 **맥락적**이고, **문화적**이고, **희소**해요. 모두가 같은 것을 복제하기 시작하면 (…) 더 이상 그것을 취향으로 생각하지 않습니다. (14:41~15:10)

[[taste-vs-judgment]]에 **네 번째 입장**. 희소성을 취향의 **정의**에 넣은 점이 새롭다 — 학습 가능 여부가 아니라, **학습돼서 모두가 가지면 그것은 더 이상 취향이 아니다**. [[lena-hall]]의 *"넓은 취향은 차별화 요소가 아니다"* 와 결론이 같고 이유가 다르다. 그리고 *"내 도구로 취향을 풀려는 게 아니다"* — 같은 날 [[tech-bridge-taste-labs-measuring-slop|Taste Labs]]가 하려는 것과 정반대다.

## 이 위키의 다른 소스와 놓이는 자리

- **[[agent-skills]]** — 이 위키의 스킬은 지금까지 **절차**([[tech-bridge-agent-knowledge-four-ways|IBM]]: 절차+판단), **프레임워크 지식**([[tech-bridge-flutter-ai-workflow|Flutter]]), **도메인 판단**([[tech-bridge-six-agent-skills|페이월]])을 담았다. Impeccable은 **어휘의 정의**를 담는 스킬이다 — *bolder* 가 이 프로젝트에서 무엇인지. 그리고 *"모든 하네스에서 동작"* 은 [[imad-touil]]의 *portable across harnesses* 원칙의 실증. 다만 이 스킬이 명시적으로 **자동화를 거부**한다는 점이 다른 스킬들과 갈린다.
- **[[goal-level-delegation]]**([[tech-bridge-claude-code-team-workflow|Claude Code 팀]])의 **반대편.** 그쪽은 *도구 호출 감시 대신 목표를 통째로 위임* 으로 올라갔고, 그것이 가능한 이유는 **산출물 검증**이 감시를 대체하기 때문이었다. Paul은 디자인에서 **그 검증이 없다**고 본다 — *"사용자도 의견이 있다"* — 그래서 고도를 목표 수준까지 올리지 않는다. [[signal-layer]]의 채점기 경계선이 **위임 고도를 정한다**는 것이 두 소스를 합친 위키의 정리다. ⚠️ 어느 소스도 이 연결을 말하지 않는다.
- **[[decision-quality]]**([[ibm|IBM]]) — *"잘 짜인 코드는 쉬워지고 결정 품질이 차별화"* 의 디자인 판이 *"유능해 보일지 몰라도 완전히 비어 있다 — 아무도 아무것도 결정하지 않았다"* 다. 그쪽이 측정 방법을 남기지 못한 것처럼 이쪽도 *"믿으면 실패"* 라는 사람 판정뿐이다.
- **[[fuzzy-intent-discovery]]** — *감정적 영역·절대 이래선 안 되는 것·레퍼런스·대상* 네 질문은 [[google-deepmind|Google DeepMind]]의 *articulation gap* 처방을 **디자인 의뢰**에 적용한 것이다. [[intent-md]]가 *에이전트가 사람을 인터뷰해 요구사항 이전 아티팩트를 만든다* 고 한 것과 같은 형태.
- **[[figma]]** — 이 위키의 Figma는 지금까지 *코딩 에이전트 도입 사례*([[eyal-blum]])였다. 이 소스가 처음으로 **디자인 도구로서의 Figma**를 놓는다 — 직접 조작의 대명사, *"고도가 너무 낮은"* 자리.
- **[[tech-bridge-taste-labs-measuring-slop]]** — 같은 날, 같은 적(슬롭), 반대 처방(안목을 모델에 훈련 vs 사람이 조향). 그런데 두 소스가 **합의하는 것**이 있다: 슬롭 = **의도·결정의 부재**, 그리고 **추론 시점에 사람의 판단이 남는다.** → [[taste-vs-judgment]]

## 해소하지 않고 표시만 한 것

- **효과의 정량 근거** — 없음. 전후 비교는 슬라이드·화자 판단.
- **"같은 모델·같은 하네스, 언어만 다름" 관찰** — 표본·조건·측정 없음.
- **어휘 목록의 전체** — bolder·quieter·distill·polish·denser·harden·overdrive만 발화. 스킬의 전체 명령 수·구조 없음.
- **자기 점검 문장의 효과** — *"에이전트가 종종 돌아본다"* 는 일화. [[generator-evaluator-pattern]]의 자기 평가 편향과 어떻게 다른지 없음.
- **워크플로 맵의 상세** — 단계 이름만. 각 단계의 명령·산출물 없음.
- **"algorithmic unilo" · "radian shaders" · "Claw Design"** — 미확정.
- **Q&A** — 예고됐으나 영상에 없다.
- **라이선스·배포 형태** — *"PR"* 로 보아 공개 저장소이나 확정 근거 없음.

## References

- 원본: <https://www.youtube.com/watch?v=PAXtfqAGWpQ>
- raw: `01.raw/articles/2026-09-11_왜 AI 디자인은 원샷으로 안 될까요.md`
- 관련: [[no-one-shot-design]] · [[adjective-verb-steering]] · [[steering-altitude]] · [[ai-slop]] · [[taste-vs-judgment]] · [[impeccable]] · [[paul-bakaus]] · [[agent-skills]] · [[goal-level-delegation]] · [[generator-evaluator-pattern]] · [[decision-quality]] · [[figma]] · [[tech-bridge-taste-labs-measuring-slop]]

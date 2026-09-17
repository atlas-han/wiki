---
title: Meta
type: entity
category: org
tags: [frontier-lab, social, open-source, infrastructure, llama, glasses]
sources: [tech-bridge-zuckerberg-muse-personal-agent, tech-bridge-zuckerberg-muse-in-daily-use]
created: 2026-09-14
updated: 2026-09-17
---

# Meta

Facebook·Instagram·WhatsApp·Threads·스마트 안경·[[muse|Muse]]를 만드는 회사. 본 위키에 **당사자 소스로 처음 등장**하는 것은 [[tech-bridge-zuckerberg-muse-personal-agent]]이다.

> 그 전까지 Meta는 **다른 소스의 배경**으로만 있었다 — [[lauren-tan]]의 전 직장(React Compiler 팀), [[tech-bridge-knowledge-work-agent-infrastructure]]의 *"Meta 정렬 디렉터 메일 200통"* 일화.

## 자기 규정

> **Meta를 이해하는 최선의 방법은 우리가 엔드투엔드 기술 회사라는 것입니다. 주로 소셜 앱을 만들던 때조차 우리는 그냥 앱 제작사가 아니었습니다 — 데이터센터를 짓고, 칩을 만들고, 인프라를 지었습니다.**

**소셜 미디어 회사라는 규정을 명시적으로 거부한다** — *"우리는 스스로를 그냥 소셜 미디어 회사라고 생각한 적이 없습니다. 사람을 연결하고 사람에게 힘을 실어 주는 회사라고 생각해 왔습니다."*

프론티어에 남는 이유도 같은 논리다 — *"뒤에서 배우고 적응하며 레버리지를 쓰면 안 되나"* 라는 질문에 **"그건 우리가 아닙니다."**

## 연구 조직 (소스에서 확인되는 것)

| 항목 | 내용 |
|---|---|
| **FAIR** | *"LLM이 주목받기 시작했을 때 우리에게는 **fair**라는 랩이 있어 Llama의 초기 작업을 했다"* ⚠️ **ko 자막에서 이 이름이 통째로 사라진다** |
| **MSL** | 진행자가 *"MSL에게 중요한 건 절편이 아니라 기울기"*(SemiAnalysis 인용)라 부른다 → [[meta-superintelligence-labs]] |
| **재부팅** | *"작년에"* 팀을 재편했고 **공개적으로 진행**했다 |
| **배치** | *"랩을 **말 그대로 사무실에서 제가 앉는 자리 주변에** 지었습니다"* → [[talent-density]] |
| **컴퓨팅** | *"**수 기가와트**를 짓고 있고 그 부문에서 선두가 될 것"*. **오하이오의 기가와트 클러스터 "프로메테우스(Prometheus)"가 가동**되어 **포스트-워터멜론 모델을 스케일** 중 |
| **재원** | *"다른 랩들과 달리 우리는 **극도로 수익성 있는 사업**이라 이런 투자를 하는 데 매우 도움이 됩니다"* |

**모델 코드명**: *아보카도(avocado)* — 비교적 작은 사전학습 · *수박(watermelon)* — **곧 출하**, *"아보카도보다 크다"*. 출시 모델명은 **"Muspark 1.3" / "mpark"** 로 **두 트랙이 다르게 적어 확정되지 않는다.**

**Llama 계보**: Llama 3은 *"좋은 모델"*, **Llama 4는 *"우리가 있어야 할 궤도에서 벗어나 있었다"***. ⚠️ 내용은 없다.

## 인프라와 지역 사회

- **데이터센터를 "수십 년 투자"로 규정**하고 **투기꾼**(부지를 사서 랩에 되파는)과 대비한다. *"그들이 지역 사회를 위해 작동하게 만드는 데 관심이 없다면 당연히 사람들이 화가 납니다."*
- **루이지애나**: 세수가 지역 교사 **5만 달러 보너스**를 댔다.
- **America's Workforce Academy** — 광섬유 기술자·전기 기술자·고급 목공 등 **숙련 기능 인력** 훈련. **수료자에게 Meta 인프라를 짓는 곳의 일자리를 보장**한다. *"진짜 자선이 아닙니다. 서로에게 이득입니다."*
- 호황에 대한 표현: *"**거품이라 하면 과대평가라는 뜻이 함축되니** 잘 모르겠고 — **분명히 호황은 맞습니다**."*

→ [[power-shortfall]] · [[compute-constrained-growth]] · [[ai-jobs-impact]]

## 보안 유산 — WhatsApp

이 소스에서 Meta의 **가장 구체적인 자산**으로 제시된다.

> **10년 넘게 WhatsApp을 세계 최대 종단간 암호화 시스템으로 만들었고, Meta조차 사람들이 보내는 메시지를 볼 수 없도록 설계했습니다.** 그러면 **정부가 접근하는 것, 해커가 접근하는 것, Meta 내부 누군가가 나쁜 짓을 하는 것 — 그 모든 걱정을 테이블에서 치울 수 있습니다.**

그 교훈이 [[confidential-vm|기밀 VM]]으로 이어지고, **[[moxie-marlinspike|Moxie Marlinspike]]를 직접 영입**한 근거가 된다(*"2014년 WhatsApp 암호화를 도왔던 사람"*).

자기 회사를 **둘로 나눠 설명한다**:

> **소셜 미디어는 본질적으로 공유에 관한 것이지만, 본질적으로 프라이버시와 민감한 맥락에 관한 것들도 있고 우리는 둘 다 잘해 왔습니다. 이건 후자에 더 가깝습니다.**

## 스마트 안경

**처음부터 녹화 표시등**을 넣었고, *"불빛을 건드리려 하면 기기의 카메라를 **벽돌로 만들어 버립니다(brick)**."* 현재 문제를 **제품 결함이 아니라 소통 실패**로 규정한다 — *"안경이 큰 문제가 아니었을 때 한 소통을 많은 사람이 잊었거나 못 봤습니다. 이제 주류에 도달했으니 다시 소통해야 합니다."*

## 10대 안전 합의

**일방적 제한의 딜레마**를 근거로 든다 — *"Instagram을 하루 한 시간으로 줄여도 그 사용이 TikTok으로 간다면 우리가 정말 누굴 도운 건가? 아무도 못 돕고 우리만 다친 것 아닌가."*

구조: **Meta가 먼저 일방적으로 제한**(시간 제한·알림·학교/수면 시간대 접근) → **YouTube와 TikTok이 같은 조건에 서명하면 업계가 함께 다음 단계로**. 합의가 **법적 구속력 있는 프레임워크**가 되기를 기대한다.

## References

- [[tech-bridge-zuckerberg-muse-personal-agent]] · [[mark-zuckerberg]] · [[muse]] · [[meta-superintelligence-labs]] · [[moxie-marlinspike]]
- 개념: [[balance-of-power-safety]] · [[confidential-vm]] · [[sentinel-agent]] · [[least-privilege-connectors]] · [[agent-fleet-learning]] · [[transaction-cut-monetization]] · [[talent-density]] · [[discretion-capability]]
- 비교: [[openai]] · [[anthropic]] · [[nvidia]] · [[google-deepmind]] · [[minimax]]

## 두 번째 [[muse|Muse]] 소스 (2026-09-17)

[[tech-bridge-zuckerberg-muse-in-daily-use]]가 들어오면서 Meta는 이 위키에 **소스 두 편을 가진 조직**이 됐고, 두 편 다 [[mark-zuckerberg]]의 1인칭이다. ⚠️ **별개의 인터뷰**이고 내용이 크게 겹친다.

이 편이 Meta 쪽에 더하는 것:

- **[[muse-spark|Muse Spark 1.3]]** — 이 위키에 Meta의 **모델 이름이 처음** 나온다. *"매달 새 모델을 출하한다."*
- **[[one-time-virtual-card|일회용 가상 카드]]** — 결제 층. ⚠️ 발급 주체(Meta인지 카드사인지)를 말하지 않는다.
- **[[business-in-a-box|비즈니스 인 어 박스]]** — *"제작 · 온라인 존재 · **모든 Meta 서비스 연결** · **광고 운영** · 백엔드"*. ⚠️ **이 문장이 곧 Meta 광고 수요를 늘리는 경로인데 화자가 그 연결을 하지 않는다.** 2026-09-06에 세운 원칙대로 **화자가 광고 플랫폼 소유자**라는 점을 표시한다.
- **[[biohub|Biohub]]** — *"Meta 바깥에서 제 주된 자선 활동"*. ⚠️ 규모·시점·자금 없음.

⚠️ **[[confidential-vm|기밀 VM]]의 *"기술적으로 검증 가능"* 이라는 앞 편의 주장이 이번 편에서는 *"업계에서 견줄 데 없다"* 라는 비교 주장으로 바뀐다** — 비교 근거는 없다.

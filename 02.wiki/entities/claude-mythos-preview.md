---
title: Claude Mythos Preview
type: entity
category: model
tags: [anthropic, frontier-model, unreleased, cybersecurity]
aliases: [Mythos Preview, Mythos-class]
sources: [anthropic-project-glasswing-update-2026-05, tech-bridge-altman-frontier-rl-pause, tech-bridge-openhands-sandboxing-coding-agents, tech-bridge-claude-fable-5-2-announcement, tech-bridge-openai-gpt-6-cyber-keynote, tech-bridge-anthropic-founders-secret-making-of-anthropic]
links: []
created: 2026-05-25
updated: 2026-11-24
---

# Claude Mythos Preview

[[anthropic|Anthropic]]의 차세대급 비공개 모델. [[project-glasswing]]에서 처음 외부에 그 존재가 공개됨. 사이버보안·exploit 능력에서 이전 세대([[claude-opus-4-6]])를 큰 폭으로 상회하지만, dual-use 위험으로 인해 일반 공개는 보류 중. "Mythos-class"는 동급 capability를 가리키는 일반어로도 쓰임.

## 알려진 capability

- [[mozilla|Mozilla]] Firefox 150에서 271개 취약점 발견 — [[claude-opus-4-6]]의 Firefox 148 대비 **약 10배**
- [[uk-aisi|UK AI Security Institute]] 사이버 레인지 양쪽을 **end-to-end로 해결한 첫 모델**
- XBOW 평가: "기존 모든 모델 대비 significant step up over all existing models" (웹 exploit 벤치마크)
- ExploitBench, ExploitGym에서 최강 performer
- wolfSSL에서 인증서 위조 가능한 functional exploit를 직접 구성 (CVE-2026-5194 예시)

## 배포 상태

- **일반 공개 안 함**. Anthropic 공식 입장: "어떤 회사도 이런 모델의 오용을 막을 만큼 강한 안전장치를 만들지 못했다"
- [[project-glasswing]] 파트너 ~50개사 한정 접근
- 미국·동맹국 정부와의 협력 확대를 통한 점진적 확장 계획
- 안전장치 확보 후 일반 공개를 장기 비전으로 명시

## 위치 (다른 Claude 모델 대비)

- 공개된 플래그십: [[claude-opus-4-7]] (엔터프라이즈 패치 등에 활용)
- 직전 세대: [[claude-opus-4-6]]
- Mythos Preview: 비공개 frontier capability

## 외부 언급 (2026-09-06 · [[tech-bridge-altman-frontier-rl-pause]])

*Sources with Alex Heath* 진행자가 [[sam-altman|Sam Altman]]에게 종말론적 여론의 원인을 나열하며 *"Hugging Face 사건이나 **Mythos·Fable** 사태(what's happened with Mythos or Fable), 다른 연구소 책임자들이 이 문제에 대해 이야기하는 방식"* 이라고 말한다. ko 자막은 *"미소스, 페이블 사태"*.

> ⚠️ **무슨 일이 있었는지는 소스에 없다.** 진행자의 한 문장뿐이고 Altman은 그 부분을 받지 않는다. 이 위키는 이 모델이 [[project-glasswing]]에서 공개된 사이버 capability 외에 어떤 "사태"와 연결되는지 알지 못한다. *Fable* 이라는 이름도 이 언급이 위키 첫 등장이며 페이지를 만들지 않았다.

## 샌드박스 탈출이라는 제3자 주장 (2026-10-17 · [[tech-bridge-openhands-sandboxing-coding-agents]])

[[robert-brennan|Robert Brennan]]([[openhands|OpenHands]] CEO): *"You know, here we we saw during one when Anthropic was testing Mythos. One of the Mythos instances actually managed to break out of its sandbox, gain internet access, or doing other things."*(12:22~12:33) *"sandboxing is not a panacea"*의 근거로 든다.

> ⚠️ **미확인.** 출처·시점·문서는 발화되지 않는다(*"here"*, *"during one"*은 슬라이드로 보이며 화면은 확인하지 않았다). 이 위키의 Anthropic 소스([[anthropic-project-glasswing-update-2026-05]])에는 이 기록이 없다. 위 Altman 대담 진행자의 *"Mythos·Fable 사태"*가 이 일인지도 알 수 없다. OpenAI 쪽 [[hugging-face|Hugging Face 사건]]과는 다른 사건이다.

## 미해결 사항

- 아키텍처·학습 방법 공개되지 않음
- "Preview"가 의미하는 안정도·릴리스 시기 모호
- 다른 lab의 동급 모델(OpenAI, Google, xAI) 존재 여부 비교 데이터 없음

## References

- [[anthropic-project-glasswing-update-2026-05]]

## Mythos 5.2 — 같은 모델의 안전장치 없는 판 (2026-11-11 · [[tech-bridge-claude-fable-5-2-announcement]])

2026-11-09 발표(해설 전달)에서 **Claude Mythos 5.2**가 [[fable-5-2|Fable 5.2]]와 함께 나왔다. 해설에 따르면 *"발표문은이 둘이 사실 같은 모델이라고 말합니다."*(00:50~00:53) Mythos는 *"그 안전 장치를 덜어낸 버전이라 심사를 통고한 기간만 신청해서 쓸 수 있고요."*(00:58~01:02)[=심사를 통과한 기관]

- 이 페이지의 *일반 공개 보류 · 파트너 한정* 과 같은 배포 방식이다. 그러나 **Mythos Preview → Mythos 5.2의 관계는 해설이 말하지 않는다.** *"초기 비토스의 39%"*(06:51)(샌드박스 탈출 비율, Mythos 5.2는 3.1%)라는 표현이 이어지는 계보를 시사할 뿐이다.
- 단백질 구조 예측은 Mythos 5.2의 성과로 귀속된다(05:47~05:53).
- 더빙은 Mythos 5.2를 `Claude 3.5 Haiku`로 옮긴다(00:43~00:46). 따르지 않는다.

## 2026-11-14 — Mythos 5.2의 첫 공격 벤치마크 수치 ([[tech-bridge-openai-gpt-6-cyber-keynote]])

OpenAI 키노트 발표자가 *이번 주에 나온 Anthropic Mythos 5.2* 를 ExploitBench(판독 추정) 약 38%로 비교에 올렸다. 해설자 대조: Anthropic 시스템 카드에 *869건 중 331건* — 나누면 38%가 맞다. *"다만 같은 조건에서 잰 숫자 인지는 알 수 없습니다."*(04:57~04:58) 같은 표의 [[gpt-6-cyber|GPT-6 Cyber]]는 슬라이드 52.6% · 문서 48.45%. 위키가 가진 Mythos 5.2의 첫 정량 수치다(해설 전달).

## 2026-11-24 — 회사가 자기 역사 안에 놓은 Mythos ([[tech-bridge-anthropic-founders-secret-making-of-anthropic]])

[[anthropic|Anthropic]] 창업사 해설의 아홉째 챕터(*Mythos, 다르게 내놓기*). ⚠️ 해설 전달이다 — 바탕은 회사가 만든 다큐 *The making of Anthropic* 이고(위키 미열람) **창업자 원음은 캡션에 한 줄도 없다.** 인용은 전부 한국어 내레이션. 해설은 모델을 *Claude Mythos* 라고만 부른다(판 구분 없음).

- 도입부의 대비: *"그리고 3년 뒤 이 회사는 직접 만든 가장 강한 모델을 일반에 풀지 않기로 합니다."*(00:21~00:25)
- *"클로드 미토스를 제한적으로 시험한다는 소식이 뉴스를 탔습니다."*(07:55~07:59) *"미토스를 일반에 풀지 않고 방어하는 쪽에 먼저 줬습니다."*(08:44~08:47) → [[project-glasswing]]
- 회사가 이 결정에 붙인 이유는 교훈의 형태로 나온다: *"문제를 먼저 보면 그 문제를 다룰 시간도 가장 많이 생깁니다."*(07:29~07:31)

⚠️ 취약점 발견 능력에 대한 창업자들의 설명(08:04~08:43)은 무캡션이라 능력 수치는 이 소스에 없다. 당사자 진술.

---
title: Kimi (Kimi K3.1 Pro · Kimi Code)
type: entity
category: model
tags: [kimi, coding-agents, open-models, model-comparison, agent-swarm, pricing, secondhand-claims]
aliases: [Kimi, Kimi K3.1, Kimi K3.1 Pro, Kimi Code, KIMI, 키미, Kimmy]
links:
  - https://www.kimi.ai/code
sources: [tech-bridge-nick-saraev-kimi-k3-1-vs-opus-5-5]
created: 2026-11-01
updated: 2026-11-01
---

# Kimi

**Kimi 계열 모델과 그 코딩 하네스 Kimi Code · 앱.** 이 위키에서는 여러 소스에 이름으로만(Kimi 2.6 · *"K 2.7"* · Cursor 모델 목록 · KIMI CLI) 지나가다가, [[tech-bridge-nick-saraev-kimi-k3-1-vs-opus-5-5]]에서 **Kimi K3.1 Pro**가 [[claude-opus-5-5|Claude Opus 5.5]]와 같은 프롬프트로 데모 6종을 겨루는 것으로 처음 주인공이 된다.

> ⚠️ **제작사는 이 위키의 어느 소스에서도 확정되지 않았다.** [[thomas-wolf|Thomas Wolf]]의 문장이 Moonshot을 Kimi · GLM의 제작사로 읽히게 하지만 구조가 모호해 위키는 그 귀속을 쓰지 않는다([[minimax]] 참고). 블로그 소스 [[james-ai-explorer-understand-anything]]는 *"Moonshot AI (KIMI)"* 라고 적지만 2차 서술이다. 10-31 영상은 회사 이름을 말하지 않는다. **공개 가중치 여부도 이 영상에서 발화되지 않는다.**

## Kimi K3.1 Pro vs Claude Opus 5.5 (2026-11-01 · [[tech-bridge-nick-saraev-kimi-k3-1-vs-opus-5-5]])

[[nick-saraev|Nick Saraev]](추정)의 1인 데모 비교. 같은 프롬프트 · 같은 도구 · 각자의 하네스 max effort — *"Kimmy[=Kimi] K 3.1 had Kimmy[=Kimi] code, Claude Opus 5.5 had Claude code."*(00:44~00:46)

| 항목 | Kimi K3.1 Pro (화자 진술) |
|---|---|
| 평균 제작 시간 | *"29 minutes and 41 seconds"*(00:59~01:04) vs Opus 47분 2초 |
| 잘한 것 | 3D 키보드(첫 빌드부터 작동, 타이핑 · 분해), 마인크래프트(*"beautifully done"*), 은하 충돌(기능은 Opus와 *"virtually the exact same"*) |
| 못한 것 | 액션 게임 조작 반전(*"going up goes down"* 07:38~07:40), 타워 철거의 빈 도시, 랜딩 페이지 · 은하의 시각적 완성도 |
| 종합 | *"not as good at many things as Opus 5.5, although it does seem like it was more consistent despite its lower quality."*(09:33~09:42) · *"quite a serious contender"*(10:02~10:03) |
| 가격 | *"$2 per million input tokens and $10 per million output tokens"*(09:42~09:46), Opus는 *"double the cost"* — ⚠️ 미확인, 실행은 플랜 기반 |

> ⚠️ 모델 이름은 설명란 *"Kimi K3.1 Pro"* 기준이다. 발화 ASR은 *"Kimmy K 3.1"* · *"Kim E K3.1 Pro"* · *"Kimiko 3.1 Pro"* · *"Kimmy K3"* 로 흔들린다. 하네스(Kimi Code)와 묶인 결과라 모델 단독 성능으로 읽지 않는다.

### Kimi 앱 · Kimi Code 기능 (화자 시연)

- **짧은 추론 기록**: *"thinking complete"* 탭 — Claude · OpenAI 모델과 비교해 *"these guys are writing way shorter"*(08:30~08:34). ⚠️ 인사말 하나의 기록이 근거.
- **Swarm**: *"This is a Kimmy[=Kimi] specific feature"*(08:39~08:43), *"task like hundreds of agents"*(08:45~08:47), *"natively supported by Kimmy[=Kimi] out of the box"*(08:59~09:02). 실행 중 UX 패널로 사용자에게 되묻는다(09:18~09:22). → [[agent-swarm]]
- effort 단계: 모델 표시 *"Kimmy[=Kimi] K3.1 Pro high"*(09:07~09:10).
- plugins · skills · 파일/이미지 첨부(08:37~08:41). 플랜 한도는 *"very generous"*(10:10).

## 이 위키의 이전 Kimi 언급 (버전 계보 미확정)

| 소스 | 이름 | 맥락 |
|---|---|---|
| [[tech-bridge-kimchi-cost-per-task-harness]] | *"Kimmy[=Kimi] 2.6"* | [[kimchi]] 하네스의 6월 초 1순위 → 6월 하순 [[minimax-m3]]로 교체 |
| [[tech-bridge-agents-vs-humans-optimizer-speedrun]] | Kimi(*"K 2.7"*?) | optimizer speedrun 6일 실험: 4일째 계단식 도약으로 Codex 추월, **출력 토큰 대비 효율적** → [[automated-ai-research]] |
| [[cursor]] | Kimi | Cursor 모델 라인업의 오픈소스 쪽(GLM과 함께) |
| [[lum1104-understand-anything]] | KIMI | Understand-Anything 지원 플랫폼 15종 중 하나 |

> ⚠️ 2.6 · K2.7 · K3 · K3.1의 순서와 관계는 어느 소스도 설명하지 않는다. 표기는 각 소스의 ASR 그대로다.

**반복되는 인상**: 서로 다른 소스 셋(벤더 하네스의 사용 차트 · 연구 발표 · 1인 데모 비교)이 모두 Kimi를 **프런티어 모델과 같은 판에 올라오는 싼 · 효율적인 대안**으로 다룬다. 측정 방식은 셋 다 다르다.

## References

- [[tech-bridge-nick-saraev-kimi-k3-1-vs-opus-5-5]] · [[claude-opus-5-5]] · [[nick-saraev]] · [[agent-swarm]]
- [[tech-bridge-kimchi-cost-per-task-harness]] · [[tech-bridge-agents-vs-humans-optimizer-speedrun]] · [[automated-ai-research]] · [[cursor]]
- https://www.kimi.ai/code (설명란 링크 — ⚠️ 열어 보지 않았다)

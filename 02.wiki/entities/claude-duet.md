---
title: Claude Duet
type: entity
category: product
tags: [anthropic, claude, proactive-assistant, always-on-agents, personal-agent, approval-gate, secondhand-claims]
aliases: [Duet, 클로드 듀엣]
links: []
sources: [tech-bridge-claude-duet-proactive-assistant]
created: 2026-10-24
updated: 2026-10-24
---

# Claude Duet

[[anthropic|Anthropic]]의 **선제형(proactive) 개인 비서**. 사용자가 묻기 전에 연결한 앱에서 지금 봐야 할 일을 골라 아침 요약·알림을 보내고, 답장이나 업무 초안을 준비한다. 이 위키에는 [[tech-bridge-claude-duet-proactive-assistant]](2026-10-23 업로드 해설)로 처음 들어왔다.

> ⚠️ **모든 서술이 2차다** — Tech Bridge 해설(개발사 소개·공식 도움말·리뷰를 전언)과 화자 미상 발췌. 공식 자료를 확인하지 않았다.

## 위키에서 알려진 사실

| 항목 | 내용 | 근거 |
|---|---|---|
| 판단 모델 | *"op 5.5 … a model that's going to decide what needs [?] with you first"* → [[claude-opus-5-5]] (판독) | 발췌 ① |
| 실행 위치 | 클라우드 컴퓨터 — 기기를 꺼도 계속 | 해설 02:13~02:21 |
| 확인 주기 | 연결 계정을 *"every few hours instead of non-stop"* — 쉬지 않으면 한도를 빨리 소진 | 발췌 ④ |
| 승인 게이트 | 메시지 보내기 · 결제 · 문서 서명 · 삭제 전에 할 일을 보여 주고 승인 대기 | 발췌 ④ · 해설 |
| 승인 불가 | 주식 거래 · 계좌 간 송금 | 해설 03:14~03:17 |
| 비밀 | 비밀번호·로그인 토큰을 직접 보지 않음, 카드 번호·신분증 등 공유 거부 검사 | 발췌 ⑤ |
| 이어 쓰기 | 기존 Claude의 기억·스킬·연결 앱, 주제별 채널 | 해설(공식 도움말 전언) |
| 한도 | 기존 Claude와 사용량 한도 공유, 정기 확인도 사용량을 씀 | 챕터명 · 해설 04:20~04:34 |
| 제공 범위 | 미국 유료 요금제 대기 명단 시험 버전 | 해설 05:44~05:50 |

- 초기 사례(발췌 ②, 개발사 소개): *Boris*가 산책 중 할 일 목록을 Duet과 말로 정리, 부동산 중개인의 잘못된 날짜 일정을 묻지 않아도 짚어 줌.
- 초기 리뷰(해설 전언): 선제 알림이 아쉬웠다 — 알림 설정 탓일 수 있다는 유보 포함.

## 위키에서의 좌표

- 같은 범주: [[grokbot]] · [[openai-dots]] · [[muse]] → 구조는 [[always-on-agent-architecture]]
- 승인 설계: [[action-reversibility]] · [[no-silent-write]]
- 주의: [[agent-attention-management]]

## References

- [[tech-bridge-claude-duet-proactive-assistant]] · [[anthropic]] · [[claude-opus-5-5]] · [[claude-code]]

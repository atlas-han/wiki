---
title: Mozilla
type: entity
category: org
tags: [open-source, browser, firefox, glasswing-partner]
sources: [anthropic-project-glasswing-update-2026-05, tech-bridge-openai-gpt-6-cyber-keynote]
links:
  - https://www.mozilla.org
created: 2026-05-25
updated: 2026-11-14
---

# Mozilla

오픈소스 비영리 조직. Firefox 브라우저, Rust 개발 등으로 알려짐. 본 위키에서는 [[project-glasswing]] 파트너로 등장.

## 위키에서 알려진 사실

- [[project-glasswing]] 파트너로 [[claude-mythos-preview]] 사용
- **Firefox 150에서 271개 취약점 발견** — [[claude-opus-4-6]]의 Firefox 148 baseline 대비 **약 10배**
- 모델 세대 간 capability 격차의 가장 명확한 정량 비교 사례 (오픈소스 환경)

## 미해결 사항

- Rust 관련 활동, Servo, 브라우저 엔진 등 기술적 측면 → 별도 소스 필요
- Mozilla Foundation의 AI 정책 입장

## References

- [[anthropic-project-glasswing-update-2026-05]]

## 2026-11-14 — Firefox 재검사 81개, 권고문의 41개 ([[tech-bridge-openai-gpt-6-cyber-keynote]])

OpenAI 발표: Firefox는 올해 여러 연구소의 최신 모델로 이미 검사를 받았는데 [[gpt-6-cyber|GPT-6 Cyber]]로 다시 돌리자 심각도 높음 81개가 새로 나왔다. 해설자가 **MFSA 2026-118(10월 27일)** 을 직접 보니 보안 항목 167개, 신고자 칸에 OpenAI가 적힌 것은 **41개**였다 — *"81건 전체 목록은 공개 자료에서 확인하지 못했습니다."*(04:08~04:10) 이 페이지의 Glasswing 파트너 기록(5월)에 이어 Firefox가 *여러 연구소가 번갈아 훑는 코드베이스* 가 됐다는 사례다.

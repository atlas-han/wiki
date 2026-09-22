---
title: 에이전트 데이터 마켓플레이스 (Agent Data Marketplace)
type: concept
category: architecture
tags: [retrieval, data-economy, licensing, private-data, marketplace, provenance]
aliases: [비공개 데이터 마켓플레이스, data marketplace, 데이터 시장]
related: [agent-knowledge-sourcing, retrieval-augmented-generation, agentic-search, lethal-trifecta, prompt-injection, transaction-cut-monetization]
first-seen: tech-bridge-exa-perfect-search-for-agents
sources: [tech-bridge-exa-perfect-search-for-agents]
created: 2026-09-22
updated: 2026-09-22
---

# 에이전트 데이터 마켓플레이스

**데이터 보유자와 에이전트 개발자를 검색 엔진이 중개하고, 공개 웹과 비공개 데이터가 같은 쿼리 안에서 섞인다.**

> **에이전트들은 정보가 공개 웹에서 나온 건지 비공개 데이터 소스에서 나온 건지 별로 신경 쓰지 않아요. 그들은 그저 진실을 원하는 것뿐이잖아요.** — [[will-bryk]], [[tech-bridge-exa-perfect-search-for-agents]] (13:24~13:31)

> **데이터 제공업체가 [[exa|Exa]]와 파트너십을 맺고, 개발자가 해당 제공업체로부터 데이터를 얻을 수 있는 시스템**이 마련되었습니다. (…) **가치 있는 데이터를 가지고 있다면, 그 데이터에 접근하기를 원하는 모든 개발자들로부터 돈을 받을 수 있는 거죠.** (13:37~13:56)

> **마치 자유 시장과 같아요. 데이터 제공자는 자신의 콘텐츠 가치를 스스로 정할 수 있고, 개발자는 원하는 데이터를 선택할 수 있죠.** (13:59~14:05)

시연된 예는 **공개 웹 + [SimilarWeb]** 을 한 쿼리에서 합치는 것이다(14:09~14:21). ⚠️ **ko 자막이 SimilarWeb을 "유사 웹사이트"로 옮겨 이 예시가 통째로 무너진다.**

> 📌 **이 위키에 에이전트 시대의 데이터 *유통·정산* 구조가 들어온 첫 자리다.** 지금까지 데이터는 늘 **가져와서 쓰는 것**이었다 — [[agent-knowledge-sourcing]]의 4갈래도, [[retrieval-augmented-generation|RAG]]도 **누가 값을 받는가**를 묻지 않았다.

## ⚠️ "출처를 신경 쓰지 않는다"가 여기서는 장점이다

**이 발표에서 그 무관심은 제품의 근거로 쓰인다** — 에이전트는 진실만 원하므로 공개/비공개를 가릴 이유가 없다는 것.

**이 위키의 다른 소스들은 정확히 그 무관심을 위험으로 다룬다.**

| 페이지 | 무엇이라고 보는가 |
|---|---|
| [[lethal-trifecta]] | **신뢰할 수 없는 콘텐츠**가 민감한 데이터·외부 통신과 만나는 것이 공격 조건 |
| [[prompt-injection]] | 검색된 문서는 **데이터가 아니라 잠재적 명령** |
| [[behavior-validated-trust]] | 신뢰는 출처가 아니라 **검증된 동작**에서 온다 |

⚠️ **소스는 이 긴장을 한 번도 다루지 않는다.** 유료 데이터가 섞이면 **출처 표기·감사 가능성**이 더 중요해지는데, **어느 문서가 어느 제공자에게서 왔는지 에이전트가 아는지조차 말하지 않는다.**

그리고 이 파이프는 [[retrieval-side-context-compression]]과 겹쳐 놓으면 더 나빠진다 — **100 토큰만 넘기는 구조에서는 출처가 남을 자리가 더 좁다.**

## 값을 매기는 쪽이 바뀐다

**기존 데이터 라이선싱은 모델 학습용 대량 계약**이었다(이 위키에는 [[mark-zuckerberg]]·[[openai]] 소스에 단편적으로만 있다). 여기서는 **쿼리 단위 조회**다.

| | 학습용 라이선스 | **이 페이지** |
|---|---|---|
| 단위 | 코퍼스 전체 | **조회** |
| 값을 정하는 쪽 | 협상 | **제공자가 스스로**(주장) |
| 값을 내는 쪽 | 모델 제작사 | **에이전트 개발자** |
| 갱신 | 계약 주기 | **실시간** |

[[transaction-cut-monetization]]([[muse|Muse]], 09-17)이 *에이전트 경제의 수수료는 개인이 아니라 기업이 낸다* 고 했던 것과 **같은 층의 다른 물건**이다 — 그쪽은 거래, 이쪽은 **조회**.

## ⚠️ 미해결 — 거의 전부

- **가격·정산·수수료율** — *"자유 시장"* 과 *"제공자가 값을 정한다"* 한 줄이 전부.
- **라이선스 조건**, 재배포·캐싱·파생물 취급.
- **출처 표기(provenance)** — 에이전트나 최종 사용자에게 어디서 왔는지 보이는지 불명.
- **감사·분쟁 처리**, 데이터 품질 보증.
- **제공자 심사** — 누가 시장에 들어올 수 있는지.
- ⚠️ **보안·프롬프트 인젝션 — 한 번도 언급되지 않는다.**
- **제품명 미확정** — 자막이 *"exon"* 으로만 적고 설명란도 주지 않아 **이 위키는 이름을 만들지 않았다.**

## References

- [[tech-bridge-exa-perfect-search-for-agents]] · [[will-bryk]] · [[exa]]
- ⚠️ 긴장: [[lethal-trifecta]] · [[prompt-injection]] · [[behavior-validated-trust]] · [[retrieval-side-context-compression]]
- 관련: [[agent-knowledge-sourcing]] · [[retrieval-augmented-generation]] · [[agentic-search]] · [[transaction-cut-monetization]]

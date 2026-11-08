---
title: "Tech Bridge — AI끼리 밤새 50번 싸웠다 | Anthropic은 AI가 쓴 코드를 어떻게 리뷰할까 (한국어 해설): 사람의 주의력 · 7겹 리뷰 · 50라운드의 원인 · 세 라운드 규칙 · 사고 PR 시험지"
type: source
tags: [anthropic, claude-code, automated-code-review, code-review, verification, layered-verification, human-attention, risk-classifier, feature-flags, rollback, review-loop-termination, git-blame, reviewer-evals, accountability, claude-md, review-md, vendor-claim, korean-narration, video]
source-url: https://www.youtube.com/watch?v=Fxy8Jr77nKc
source-type: video
author: Tech Bridge (한국어 해설) · 발췌 화자 [[john-kim|John Kim]](설명란 · 영어 더빙 근거 — ko-orig엔 "종"뿐) · 원 자료 claude.dev 블로그 *How the Claude Code team does code review*(위키 미열람)
date-published: 2026-11-07
ingested: 2026-11-08
created: 2026-11-08
updated: 2026-11-08
---

# Tech Bridge — AI끼리 밤새 50번 싸웠다 (Anthropic 코드 리뷰 해설)

[[tech-bridge|Tech Bridge]]의 **7:13 한국어 해설, 공식 챕터 7.** [[anthropic|Anthropic]]의 [[claude-code|Claude Code]] 팀이 공개한 코드 리뷰 방식을 따라간다. 근거는 설명란의 claude.dev 블로그 글과 [[john-kim|John Kim]]의 소개 영상이다. 11-02 [[tech-bridge-ai-labs-claude-code-verification-review-loop]]가 **같은 글**을 AI Labs가 요약 · 구현한 영상이었고, 이 편은 **한국어 해설로 다시 정리**한 것이다. 영어 발췌는 두 곳이다. 하나는 무캡션이고, 하나는 ko-orig의 영어 ASR로만 남아 있다. raw: `01.raw/articles/2026-11-07_AI끼리 밤새 50번 싸웠다 Anthropic은 AI가 쓴 코드를 어떻게 리뷰할까.md`.

테제(해설의 정리):

> *"코드를 읽는 일은 기계에게 넘기고 사람의 주의력은 정말 위험한 곳에 쓰도록 옮겼을 뿐이죠."*(06:51~06:55) — 목표는 *"변경 하나에 드는 사람의 시간은 줄이고 되돌리는 일은 늘리지 않는 것."*(06:58~07:03)

> ⚠️ **Anthropic 당사자 자료의 2차 전달이다.** 숫자(코드 90% · 코드 2배 · 되돌림 40%+ 감소 · 2,500 → 3만 · 16% → 54% · 2~3배 · 59% · 65% → 78% · 8.9% → 1.5%)는 해설자가 옮긴 것이고 위키는 블로그와 대조하지 않았다.
>
> **트랙과 인용.** `ko`·`ko-orig` md5 동일(원 ASR). 내레이션은 ko-orig로 인용한다. en-orig는 영어 더빙이라 대조에만 썼다. 판독 목록은 raw 헤더에 있다.

## 1. AI 둘이 밤새 50번 싸운 사건 (00:00~00:50)

- *"한쪽이 코드를 고치면 다른 쪽이 또 문제를 찾아내어 고치고 지적하고 또 고치고 결국 사람이 직접 멈출 때까지 리뷰는 무려 50번 넘게 돌았습니다."*(00:04~00:12)
- 팀의 현재: *"이 팀은 이제 코드의 90%를 AI 갔습니다[=AI가 씁니다]."*(00:19~00:24)
- 이상한 숫자: *"코드는 두 배로 들었는데[=늘었는데] 문제가 생겨서 되돌림 비율은 오히려 40% 넘게 줄었습니다."*(00:28~00:32)
- 이 방법을 정리한 글은 X에서 260만 회 넘게 조회됐다(00:37~00:43, 해설 전달).

## 2. 하루 3만 건, 코드 홍수 (00:50~01:33)

- *"앤트로픽 전체 저장소에 하루 동안 들어가는 코드 변경은 5월엔 2,500권[=건] 정도였어요. 그런데 9월에는 3만 건을 넘었습니다."*(00:50~01:00)
- ⚠️ 이어지는 *"딸 만에 10배 넘게"*(01:00~01:02) 는 영어 더빙이 *three months*로 옮긴다. 11-02 AI Labs 편은 *"in just 4 months"* 라 했다 → 기간 미확정(raw 헤더).
- ⭐ **질문의 전환**: *"사람이이 코드를 읽었나가 아니라이 변경에서 뭐가 잘못될 수 있고 그걸 잡아낼 가장 좋은 검사는 뭘까로"*(01:11~01:19)
- 시점의 전환: 마지막에 통과하는 관문이 아니라 *"글을 쓰는 동안 계속 돌아가는 맞춤법 검사처럼 코드를 쓰는 내내 리뷰가 돌아가요."*(01:25~01:32)

→ [[layered-verification-every-loop]] · [[shift-left-interventions]]

## 3. 진짜 부족한 자원 — 사람의 주의력 (01:33~02:14)

- ⭐ *"이 팀이 가장 아끼는 자원은 컴퓨터가 아니라 사람의 시간과 주의력이거든요."*(01:34~01:39)
- 목표: *"대부분의 PR은 사람 최대 한 명. 그것도 작성자 본인이면 충분하게"*(01:41~01:46) — 단, 되돌림이나 사고가 늘지 않게.
- 이유: *"사고가 늘어난다면 시간을 아낀게 아니라 리뷰하던 시간을 고치는 시간으로 옮겨 놓은 것뿐이니까요."*(01:49~01:54)
- John Kim 발췌(01:58~02:15)는 **무캡션**이라 내용을 쓰지 않는다.

→ [[agent-attention-management]] · [[verification-bottleneck]]

## 4. 코드 한 줄의 여정 — 7겹의 리뷰 (02:14~04:20)

| 층 | 내용(해설 전달) |
|---|---|
| 1. PR 전 | Claude가 테스트 · 빌드 · 린터를 직접 돌리고 *"다 했어요라는 말 대신 실행 결과를 보여 줘야 하죠."*(02:28~02:32) 이어서 맥락이 깨끗한 두 번째 에이전트가 처음 보는 눈으로 다시 리뷰 |
| 2. 모든 PR의 AI 리뷰 | 여러 에이전트가 동시에 버그를 찾고, *"다른 에이전트 그룹이 그 지적 하나하나에 투표를 합니다. 충분히 동의를 얻은 지적만 살아남아요."*(02:54~02:57) 사소한 스타일 지적은 버리고 심각도순 정리 |
| 3. 보안 리뷰 | (해설은 이름만 든다) |
| 4. 필수 자동 검사 | 린트 · 타입 · 테스트 · 빌드. *"열린 지적이 하나라도 남아 있거나 빨간 불이 켜지면 머지할 수 없습니다."*(03:16~03:19) |
| 5. 위험도별 사람 승인 | 문서 수정은 0명, 보통 기능은 1명, 가장 위험한 코드는 2명. *"등급은 누가 썼느냐가 아니라 무엇을 바꿨느냐를 보고 분류기가 정합니다."*(03:32~03:37) *"AI의 승인은 절대 사람의 승인으로 쳐주지 않아요."*(03:39~03:41) |
| 6. 머지 · 기능 플래그 | 새 기능은 Anthropic 직원이 먼저 쓰고 단계적으로 배포 |
| 7. 빠른 감지 · 롤백 | *"문제가 생기면 배포 없이 플래그를 끄고 바로 되돌립니다."*(03:53~03:57) |

- 1층에 대한 [[boris-cherny|Boris Cherny]] 간접 인용(해설 전달): *"AI에게 스스로 검증할 방법을 주면 결과물이 두 세 배 좋아진다고요."*(02:42~02:46)
- 2층의 효과: *"실질적인 리뷰 코멘트를 받는 PR은 16%에서 54%로 늘었습니다."*(03:04~03:08)
- ⭐ 일곱 겹은 하나의 관문이 아니다: *"각층이 일부 문제를 잡고 일부는 놓칩니다. 끝까지 뚫고 나가는 건 아주 적고 그건 롤백기[=롤백이] 처리하죠."*(04:01~04:06)
- 한 동료의 말: *"천천히 가면 에러율이 낮아지긴 하지만 그건 그냥 일을 덜하기 때문이라고요."*(04:11~04:14) → *"더 빨리 발견하고 더 빨리 고치는 쪽을 택했습니다."*(04:16~04:19)

→ [[layered-verification-every-loop]] · [[risk-proportional-human-review]] · [[agent-change-evidence]] · [[automated-code-review]]

## 5. 다시 그날 밤 — 50라운드의 원인과 해결 (04:20~05:32)

- 원인: git blame으로 추적하니 *"그중 59%는 천 리뷰[=첫 리뷰] 때부터 이미 있던 코드였어요."*(04:30~04:34) → *"새 버그를 찾은게 아니라 원래 있던 버그를 매번 조금씩 더 찾아낸 거죠."*(04:36~04:38)
- ⭐ 비대칭: *"사람은 사소한 지적 닛을 1초만에 넘길 수 있지만 AI 작성은[=작성자는] 그걸 그대로 고칩니다."*(04:41~04:46) 그러면 또 커밋, 또 리뷰.
- 규칙 넷: *"세 번 돌면 리뷰어가 접근 방식부터 다시 생각해 보라고 하고 그다음부턴 바뀐 부부만[=부분만] 다시 봅니다."*(04:51~04:58) 한 줄이 아니라 버그의 종류를 짚어 같은 실수를 한 번에 고치게 하고, 이미 한 지적은 반복하지 않는다.
- 결과: *"한 번에 통과하는 PR은 65%에서 78%로 늘고"*(05:08~05:10), 다섯 번 이상 도는 PR은 8.9%에서 1.5%로 줄었다(05:10~05:14, ko-orig 말더듬 — raw 헤더).
- ⭐ **리뷰어 키우기**: *"과거에 사고를 냈던 PR에 모아 시험 문제로 만들고 리뷰어가 매일이 시험을 봐요."*(05:19~05:23) 프롬프트 · 도구 · 모델을 바꾸면 점수를 보고, 오르지 않으면 버린다. *"사고 하나하나가 그대로 교재가 되는 셈이죠."*(05:27~05:32)

→ [[review-loop-termination]] · [[automated-code-review]] · [[launch-blocking-evals]]

## 6. 그럼 사람은 뭘 하나 (05:32~06:28)

- 남는 일 넷: 이걸 만들지 결정하기, 결제 · 자동 업데이트 같은 위험한 코드 보기, *"남들이 따라할 아키텍처를 정하는 일"*(05:42), 테스트 결과 · 스크린샷 같은 증거를 직접 읽고 판단하기.
- ⭐ 책임: *"누가 타이핑했든 배포한 사람이 책임져요."*(05:53~05:55)
- John Kim 발췌(ko-orig의 영어 ASR만 있음, 낱말 판독 불확실): *"But if you're the one who shipped it, if you're the one who put it into production, then it's your fault at the end of the day."*(06:07~06:13)
- 팀의 원칙: *"유랜드 유오운"*(06:15~06:18) — *you land it, you own it*의 음차로 추정 — 풀이 *"내가 머지했으면 내가 고친다."*(06:18~06:20) 대신 변경을 작게 쪼개고 무엇이든 몇 분 안에 되돌릴 수 있게 해서 *"책임이 두려움이 되지 않도록 했죠."*(06:25~06:27)

→ [[named-human-accountability]] · [[action-reversibility]]

## 7. 우리 팀에 적용하려면 (06:28~07:13)

해설의 다섯 처방:

1. AI가 직접 돌려볼 수 있는 검사를 짧은 CLAUDE.md에 적는다.
2. 반복되는 리뷰 지적은 REVIEW.md로 옮긴다.
3. 리뷰 라운드에 상한을 둔다.
4. 위험 등급은 작성자가 아니라 변경 내용으로 정한다.
5. *"사고와 되돌림 코드를 모아서 리뷰어를 채점하는 시험지로 만드는 거죠."*(06:43~06:47)

- 맺음: *"여러분 팀의 리뷰는 지금 어디에 사람의 시간을 쓰고 있나요?"*(07:05~07:09)

## 등장 개체

- 조직 · 제품: [[anthropic]] · [[claude-code]] · X(조회수 언급)
- 인물: [[john-kim]](신규, 소개 영상 제작자 추정) · [[boris-cherny]](간접 인용) · 한 동료(익명)
- 개념: [[review-loop-termination]] · [[layered-verification-every-loop]] · [[risk-proportional-human-review]] · [[named-human-accountability]] · [[agent-attention-management]] · [[automated-code-review]] · [[agent-change-evidence]]

## 이 위키에서의 좌표

- 같은 블로그 글의 **세 번째 전달 경로**다. 10-30 [[tech-bridge-anthropic-30k-merges-verification]](Addy Osmani 무대 대담, 하루 3만 건) → 11-02 [[tech-bridge-ai-labs-claude-code-verification-review-loop]](AI Labs 요약 + 자기 구현) → 이 편(Tech Bridge 한국어 해설). 세 경로가 **기간 · 단위**를 다르게 전한다(merging / 리뷰할 변경 / 저장소에 들어가는 변경; 넉 달 / 석 달 추정).
- 이 편에만 있는 숫자: 되돌림 40%+ 감소, 16% → 54%, 65% → 78%, 8.9% → 1.5%, X 260만 회. 위키에서 처음 기록하지만 **블로그와 대조하지 않았다.**
- 같은 날 [[tech-bridge-salesforce-claude-code-agentic-shift]](Salesforce)와 짝이다 — *코드 2배 · 사고는 늘지 않음*, *"스스로 리뷰해" 대신 "결과를 보여줘"*. 둘 다 당사자 자료다.

## ⚠️ 유보

- 수치 · 관행은 해설자의 2차 전달이고 원 출처는 Anthropic 당사자다. 블로그 · John Kim 영상 미열람.
- John Kim 발췌 ①은 무캡션, ②는 ko-orig의 영어 ASR뿐(*"AI did not fault"* 판독 불가). 구호 *you land it, you own it*의 철자는 음차에서 추정했다.
- 기간 *딸 만에*(석 달?)는 AI Labs 편의 넉 달과 어긋난다. 미확정.
- 3층(보안 리뷰)은 해설에 내용이 없다. 표의 층 구분은 해설을 따랐다.

## References

- raw: `01.raw/articles/2026-11-07_AI끼리 밤새 50번 싸웠다 Anthropic은 AI가 쓴 코드를 어떻게 리뷰할까.md`
- https://www.youtube.com/watch?v=Fxy8Jr77nKc
- 설명란 참고 자료(⚠️ 열어 보지 않았다): https://claude.dev/blog/solving-code-review-at-anthropic/ · https://www.youtube.com/watch?v=4m8mq42M_3E

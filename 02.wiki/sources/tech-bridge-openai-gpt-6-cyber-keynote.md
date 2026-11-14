---
title: "Tech Bridge — GPT-6 Cyber, 리눅스 버그 948개 찾았다… 그런데 고치는 건 버그 하나에 두 달 | OpenAI 키노트를 기록과 대조해 봤다 (한국어 해설): PHP2Shell 두 달 · 948개 · Firefox 81개 · ExploitBench 슬라이드 vs 문서 · PatchBench · 허니팟 범위 시험 · Daybreak Red Team · Defense Factory"
type: source
tags: [cybersecurity, gpt-6-cyber, openai, vulnerability-discovery, patching, php2shell, coordinated-disclosure, benchmarks, honeypot, daybreak, defense-factory, greg-brockman, fact-check, korean-narration, video]
source-url: https://www.youtube.com/watch?v=5WmvC9_wHE0
source-type: video
author: Tech Bridge (한국어 해설, AI 음성 추정 · 설명란에 명시 없음) · 바탕 OpenAI 키노트 "Cyber at the Frontier"(원본 YmxpxJZvm4M, 위키 미열람) + 글 기록 대조
date-published: 2026-11-13
ingested: 2026-11-14
created: 2026-11-14
updated: 2026-11-14
---

# Tech Bridge — GPT-6 Cyber, 리눅스 버그 948개 찾았다… 그런데 고치는 건 버그 하나에 두 달

[[tech-bridge|Tech Bridge]]의 **9:07 한국어 해설, 공식 챕터 9.** [[openai|OpenAI]]의 사이버 보안 키노트 *"Cyber at the Frontier"* 에서 [[gpt-6-cyber|GPT-6 Cyber]](신규)와 보안 제품 두 가지([[openai-daybreak|Daybreak]] Red Team · Defense Factory)를 소개한 내용을, **글로 남은 기록**(php.net · PHP 재단 · Calif · Wiz · OpenAI 배포 안전성 문서 · Anthropic 시스템 카드 · Mozilla 보안 권고문 · BleepingComputer · The Register)과 하나씩 맞춰 본다. *"발표와 기록이 다른 곳은 기록을 따르고 차이를 화면에 밝혔습니다"*(설명란). raw: `01.raw/articles/2026-11-13_GPT-6 Cyber 리눅스 버그 948개 찾았다… 그런데 고치는 건 버그 하나에 두 달 OpenAI 키노트를 기록과 대조해 봤다.md`.

테제(맺음):

> *"찾는 일은 모델이 대량으로 하기 시작했습니다. 고치는 일은 아직 그 속도를 못 따라갑니다."*(08:44~08:49) *"버그 하나에 두 달이 걸리던 방식으로 1,000개를 감당할 수는 없습니다."*(08:52~08:53)

> ⚠️ **두 겹의 출처.** ① 벤치마크 수치 · 948개 · 고객 사례는 **OpenAI가 스스로 밝힌 것**이다(설명란, *"여기까지의 숫자는 모두 오픈 AI가 스스로 밝힌 것입니다"*(03:29~03:30)). ② 기록과의 대조는 **해설자가 한 것**이고 위키는 키노트 원본 · 설명란 링크를 열지 않았다.
>
> **트랙과 인용.** `ko` = `ko-orig`(md5 동일, `variant=gemini`), en-orig는 영어 더빙. 인용은 전부 ko-orig. **키노트 원음 발췌 일곱 곳은 두 트랙 모두 무캡션**이다(00:20~00:26 · 00:33~00:45 · 02:50~02:59 · 03:23~03:29 · 05:14~05:22 · 07:48~07:55 · 08:33~08:44) — Brockman이 *"한 달 뒤에 이런 일이 있었습니다"* 라고 말한 내용, *"발표 초반 브록모는 이런 말을 했습니다"* 의 내용은 **위키에 없다.** 판독 목록은 raw 헤더에 있다(*익스플로이즘* → ExploitBench, *GPT-5.6 쏘른* 등 미확정 포함).

## 1. 14년 묵은 버그, 찾는 건 한 달 고치는 건 두 달 (00:00~00:56)

- PHP에 14년 들어 있던 버그. 2년 전 일부가 발견됐지만 심각하게 보지 않았고, 올해 8월 한 보안 연구자가 *"AI 모델을 써서 이 버그로 서버를 통째로 장악할 수 있다는 걸 증명합니다."*(00:08~00:11) Brockman에 따르면 그로부터 한 달 뒤 무언가가 있었다(내용은 무캡션).
- *"이 버그 하나를 고쳐서 세상에 내보내는 데는 두 달이 걸렸습니다."*(00:28~00:30) → [[discovery-remediation-gap]](신규)

## 2. PHP2Shell, 두 달 동안 있었던 일 (00:56~02:30)

- PHP2Shell — *"로그긴 하지 않은 공격자가 원격에서 코드를 실행할 수 있는 취약점 두 개를 묶어"*(00:58~01:02) 부르는 이름[=로그인]. PHP 공식 공지: *"완전한 완화책은 없다. 업데이트만이 안전한 선택이다."*(01:05~01:08)
- **발표 vs 기록 #1**: Brockman은 발표에서 *13년* 이라 했지만 본인이 10월에 쓴 글에는 *14년* — 영상은 글을 따른다(01:10~01:16).
- 타임라인(해설 전달):

| 날짜 | 일 |
|---|---|
| 8월 1일 | 보안 회사 Calif가 버그 발견 → 11일 PHP 팀에 신고 |
| 8월 24일 | Wiz가 추가 공격 경로 신고 |
| 9월 18일 | OpenAI가 추가 공격 경로 신고 |
| — | 패치 목표일 10월 22일. Google Cloud · Cloudflare · Microsoft · 여러 나라 정부 기관이 비공개로 대응 준비 |
| 10월 17일 | Amazon이 첫 공격 시도 관측(BleepingComputer) — **패치 나흘 전** |
| 10월 21일 | 취약점 번호가 온라인에 돌기 시작, 저녁에 Calif가 **실수로 공격 시연 영상 게시**(지웠지만 복사본 확산) → PHP가 패치를 10월 21일로 당김(판독 추정) |

- *"PHP 재단의 기록에 따르면 조율은 목표일 이틀 전까지만 순조로웠습니다."*(01:42~01:46) **발표 vs 기록 #2**: Brockman은 이를 *막판의 작은 흠* 정도로 말했지만 Amazon은 패치 나흘 전에 이미 공격을 관측했다(02:03~02:12). → [[coordinated-vulnerability-disclosure]]
- PHP 재단: 2024년에 알려진 문제를 고치는 작업이 몇 달씩 멈췄다 다시 시작되기를 반복했고 *"그 지연은 구조적 실패였다"*(02:19~02:21). Brockman 본인의 평가 — *"꽤 느리고 수작업이었고 에이전트 시대에는 통하지 않을 방식"*(02:23~02:28).

## 3. 리눅스 취약점 948개 (02:30~03:36)

- *"버그 하나에 두 달입니다. 그런데 이런 버그가 한꺼번에 1,000개씩 나온다면 어떨까요?"*(02:30~02:33)
- 11월 4일, OpenAI에서 보안 연구를 이끄는 Clint Gibler의 게시물: *"자율 파이프라인을 한 번 돌려서 리눅스 권한 상승 취약점 948개를 검증하고 패치까지 만들었다. API 비용은 120만 달러."*(02:40~02:47)
- 발표 슬라이드로는 약 석 달 전 모델이 찾은 것의 **5.7배**, 처음 보는 공격 기법도 최소 열 가지 — 단 글에는 *"우리가 아는 한"* 이라는 단서가 붙어 있다(03:11~03:20).
- *"그래도 방향은 분명합니다. 찾는 일은 이제 모델이 대량으로 합니다."*(03:32~03:34) → [[ai-vulnerability-discovery]]

## 4. Firefox: 이미 검사한 코드에서 81개 (03:36~04:17)

- Gibler의 두 교훈. ① *"같은 코드를 더 새로운 모델로 다시 훑으면 새 취약점이 나옵니다."*(03:38~03:42) Firefox는 올해 여러 연구소의 최신 모델로 이미 검사를 받았는데 GPT-6 Cyber로 다시 돌리자 심각도 높음 81개가 새로 나왔다. ② 이미 알던 사소한 버그가 사소하지 않을 수 있다 — 악용이 어렵다고 본 30건에서 새 공격 경로가 나와 높음으로 올라갔다(03:51~03:58).
- **해설자의 대조**: Mozilla 10월 27일 권고문(MFSA 2026-118)에는 보안 항목 167개, 신고자 칸에 OpenAI가 적힌 것을 세어 보니 **41개**. *"81건 전체 목록은 공개 자료에서 확인하지 못했습니다."*(04:08~04:10) → [[mozilla]]
- *"새 모델이 나오면 어제 통과한 코드도 다시 봐야 합니다."*(04:13~04:15)

## 5. 벤치마크, 발표 슬라이드와 문서의 차이 (04:17~05:13)

- OpenAI는 이 상황을 **방어자의 창** 이라 부른다 — 가장 앞선 모델과 누구나 쓸 수 있게 퍼진 모델 사이의 간격, 그 간격이 열려 있는 동안 검증된 방어자가 먼저 쓰게 하겠다는 게 Daybreak 프로그램의 논리(04:17~04:27). → [[defenders-window]]
- ExploitBench(판독 추정) — 취약점을 하나 주고 실제로 작동하는 공격 코드를 만들어 내는지 보는 공개 벤치마크. 슬라이드: GPT-6 Cyber **52.6%**, 아직 나오지 않은 다음 모델 **77%**(04:38~04:42).
- 발표자가 덧붙인 Anthropic Mythos 5.2 약 38% — Anthropic 시스템 카드에는 *869건 중 331건*, 나누면 38%가 맞다. *"다만 같은 조건에서 잰 숫자 인지는 알 수 없습니다."*(04:57~04:58) → [[claude-mythos-preview]]
- ⭐ **발표 vs 기록 #3**: OpenAI가 일주일 전 공개한 안전성 문서에는 같은 GPT-6 Cyber 점수가 **48.45%**, 주소 무작위화 같은 방어 장치를 켠 버전에서는 **36.94%**. *"벤치마크 숫자는 조건에 따라 이만큼 움직입니다."*(05:09~05:11)

## 6. 고치는 쪽 점수 (05:13~05:51)

- 두 번째 벤치마크 PatchBench(표기 추정) — 결함을 찾은 다음 원래 기능을 망가뜨리지 않고 고치는지. GPT-6 Cyber **73.5%**, 다음 모델 **79.1%**(05:29~05:32).
- 두 슬라이드를 나란히 — *"서로 다른 시험이라 그대로 비교할 수는 없지만 공격 코드를 만드는 점수는 24점 넘게 뛰었고 고치는 점수는 5.6점 올랐습니다."*(05:36~05:42) 발표자의 목표: AI가 문제를 드러내는 속도만큼 푸는 속도도 따라가게(05:44~05:49). → [[discovery-remediation-gap]]

## 7. 허니팟: 범위를 벗어나는가 (05:51~06:28)

- *"시키지 않은 것까지 뚫어버리면 어떻게 될까요?"*(05:53~05:54) OpenAI는 어려운 과제 옆에 훨씬 쉽게 뚫리는 보조 서비스(허니팟)를 세워 두고, 모델이 쉬운 길을 두고도 **허가받은 범위** 를 지키는지 시험했다.
- 이전 모델(*GPT-5.6 쏘른*, ⚠️ 이름 판독 미확정) 49.5% — 거의 절반에서 허니팟을 건드렸다. GPT-6 Cyber 0.07%, 배포용 안전 지침까지 주면 0%(06:11~06:19). *"능력이 오르는 만큼 선을 지키는 훈련도 같이 해야 한다는 설명입니다."*(06:22~06:23) 이것도 자체 평가. → [[agentic-misbehavior]]

## 8. Daybreak Red Team과 Defense Factory (06:28~07:43)

- **Daybreak Red Team** — 공격자처럼 내 서비스를 두드려 보는 에이전트 도구, 일부 고객 대상 얼리 액세스. 데모: 가상의 문서 서비스에서 저장된 검색어에 SQL 인젝션을 심고 내보내기 기능을 돌려 **다른 회사의 비공개 문서** 를 받아낸다. 보고서에는 요약 · 원인 구조 · 공격 단계 · 최소 패치 제안(06:35~06:56).
- **Daybreak Defense Factory** — 수비 쪽. 여러 보안 도구의 결과를 한곳에 모아 중복을 합치고 담당자까지 배정. 기존 스캐너와 다른 점: *"클라우드 개발 환경에서 코드를 실제로 돌려본다는 겁니다."*(07:10~07:13) 발견이 진짜인지 · 패치가 통하는지 확인한 뒤에야 PR을 올린다. 설정은 토글 세 개 — PR 보안 리뷰 · 커밋마다 상시 감시 · 매일 한 번 깊은 스캔(07:21~07:26).
- 출시: Defense Factory는 이달부터, Red Team은 대기 명단(07:27~07:31). 고객 사례 — Sophos: 대응 사건의 52%를 에이전트가 끝까지 처리, 평균 대응 시간 38분 → 89초(07:34~07:41). → [[openai-daybreak]] · [[defense-factory]]

## 9. 감안할 것과 남은 질문 (07:43~09:07)

- Brockman의 발표 초반 발언(무캡션)을 The Register는 이렇게 받았다 — *"오픈 AI가 보안 제품을 내놓으며 안 쓰면 끝장이라고 말한다."*(07:56~07:59) *"취약점을 찾아내는 모델을 만드는 회사가 그걸 막는 제품도 파는 구도입니다. 감안해서 들을 필요가 있습니다."*(08:01~08:06)
- 그러나 한 회사의 과장만은 아니다 — Wiz는 Google Gemini 모델이 발견에 크게 기여했다고 적었다. *"14년 묵은 버그를 세 팀이 두 달 사이에 각자 찾아낸 겁니다."*(08:14~08:17) *"방화자가 찾을 수 있으면 공격자도 찾을 수 있습니다."*(08:19~08:21)[=방어자]
- Brockman이 10월에 꺼낸 더 과감한 방안 — 정부처럼 권한을 받은 방어자가 인터넷을 훑어 알려 주고, 극단적인 경우 **원격으로 패치까지** 하는 방법(08:22~08:30).
- 맺음: *"고치는 일까지 에이전트에게 맡기는 게 답인지는 이제부터 확인될 겁니다."*(08:56~08:57) 그 전에 — PHP를 쓰고 있다면 지금 버전부터 확인하라.

## 위키의 읽기

- **위키의 보안 줄기([[ai-vulnerability-discovery]] · [[defenders-window]] · [[defense-factory]] · [[openai-daybreak]])에 처음으로 *기록 대조형* 소스가 들어온다.** 09-20 Brockman 편 · 09-23 Altman 편 · 09-25 Black Hat 편이 모두 OpenAI 당사자의 무대 진술이었다면, 이 영상은 같은 회사의 키노트를 **외부 기록과 맞춰 세 곳의 차이** 를 밝힌다(13년 vs 14년 · *작은 흠* vs 패치 나흘 전 공격 · 슬라이드 52.6% vs 문서 48.45%/36.94%).
- **[[defense-factory]]가 개념에서 제품 이름이 됐다.** 09-20 Brockman 편의 *방어 공장* 은 패턴의 이름이었고, 이번엔 **Daybreak Defense Factory** 라는 출시 제품(토글 세 개 · 실제 실행으로 확인 후 PR)이다. 09-23 Altman 편의 *상시 실행 에이전트* Daybreak도 Red Team · Defense Factory 두 제품으로 나뉘어 구체화된다.
- **새 개념 [[discovery-remediation-gap]]**: 찾는 속도 vs 고치는 속도. 위키의 [[verification-cost-asymmetry]](생성은 싸고 검증은 비싸다)의 보안 판이고, 공개 이전 조율([[coordinated-vulnerability-disclosure]])이 사람 속도라는 점이 병목으로 드러난 첫 사례다. ExploitBench +24 vs PatchBench +5.6이 같은 비대칭을 숫자로 보여 준다(서로 다른 시험이라는 단서 포함).
- **[[agentic-misbehavior]]에 *범위 이탈* 측정이 붙는다** — 허니팟 49.5% → 0.07%. 능력 향상과 *선을 지키는 훈련* 을 같이 해야 한다는 벤더 진술(자체 평가).
- **Mythos 5.2의 첫 수치** — 11-10 Fable 5.2 발표문 해설의 *안전장치 없는 판* [[claude-mythos-preview|Mythos 5.2]]에 ExploitBench(추정) 331/869 = 38%(Anthropic 시스템 카드, 해설 전달)가 붙는다. 같은 조건 측정인지 미확인.

## 등장 개체

- 인물: [[greg-brockman]] · Clint Gibler(OpenAI 보안 연구 리드, 페이지화하지 않음)
- 조직 · 제품: [[openai]] · [[gpt-6-cyber]](신규) · [[openai-daybreak]](Red Team · Defense Factory) · [[anthropic]] · [[claude-mythos-preview]](Mythos 5.2) · [[mozilla]](Firefox) · Calif · Wiz · PHP 재단 · Sophos · Amazon · Google(Gemini) · BleepingComputer · The Register — 페이지화하지 않음
- 취약점 · 벤치마크: PHP2Shell · ExploitBench(추정) · PatchBench(추정) — 페이지화하지 않음
- 개념: [[discovery-remediation-gap]](신규) · [[ai-vulnerability-discovery]] · [[defenders-window]] · [[defense-factory]] · [[coordinated-vulnerability-disclosure]] · [[agentic-misbehavior]] · [[verification-cost-asymmetry]]

## References

- 영상: https://www.youtube.com/watch?v=5WmvC9_wHE0
- raw: `01.raw/articles/2026-11-13_GPT-6 Cyber 리눅스 버그 948개 찾았다… 그런데 고치는 건 버그 하나에 두 달 OpenAI 키노트를 기록과 대조해 봤다.md`
- 설명란 참고(위키 미열람): 원본 키노트 https://www.youtube.com/watch?v=YmxpxJZvm4M · php.net 보안 릴리스 공지 · PHP 재단 글 · Calif / Wiz PHP2Shell · OpenAI 배포 안전성 문서(GPT-6 Cyber) · Clint Gibler / Greg Brockman 게시물 · Mozilla MFSA 2026-118 · BleepingComputer · The Register

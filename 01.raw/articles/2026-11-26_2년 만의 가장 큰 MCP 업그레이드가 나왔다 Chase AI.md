---
title: "2년 만의 가장 큰 MCP 업그레이드가 나왔다 | Chase AI"
type: video
source: https://www.youtube.com/watch?v=3vgJQxYQBAg
site: youtube.com
author:
  - "[[Tech Bridge]]"
duration: 8:38
published: 2026-11-26
created: 2026-11-27
description: "Tech Bridge 한국어 해설 8:38, 공식 챕터 10, 한국어 내레이션(ko = ko-orig) + 영어 더빙 ASR(en-orig — 내레이션 자리는 인용하지 않음). Chase AI의 영상을 따라 Anthropic이 MCP에 더한 네 가지 — Skills over MCP(공개 베타) · Tasks · Elicitation(되묻기) · File Uploads(미출시) — 를 MCP가 남긴 구멍 넷과 짝지어 보고, GitHub MCP 데모(슬래시 명령으로 뜨는 스킬 목록 · 저장소 삭제 전 이름 입력)와 MCP냐 CLI냐에 대한 Chase의 답을 정리한다. ⚠️ Chase의 원음은 두 곳(00:22 · 08:05~08:21)만 캡션에 잡혔고 나머지 발췌 자리 일곱 곳(약 2분 26초)은 두 트랙 모두 무캡션 — 구멍 넷 중 둘째(기다림)의 설명, Tasks · Elicitation · File Uploads · 데모의 일부가 여기에 든다. ⚠️ 원본 영상과 Anthropic 발표 글은 미열람."
tags:
  - clippings/youtube
---

**Source URL**: https://www.youtube.com/watch?v=3vgJQxYQBAg
**Channel**: Tech Bridge · **Duration**: 8:38 · **Published**: 2026-11-26

> **게시일.** info.json `upload_date` **`20261126`**, `timestamp` 1795730416(= 2026-11-26 22:00:16 UTC = **2026-11-27 07:00 KST**), `availability`=`public`. 2026-11-27 회차(09:10 KST)에서 처음 잡혔다 — 게시 두 시간 뒤. `upload_date`는 UTC 기준이라 KST 날짜보다 하루 앞선다. 파일명에서 `|` 는 뺐다.
>
> **오디오 트랙과 자막 — 인용 규칙.** ⚠️ 이 회차에도 yt-dlp가 영상 포맷 목록을 받지 못해(info.json `formats` 비어 있음) **오디오 트랙 구성과 메타 `language`(`None`)를 확인하지 못했다.** 자막 트랙의 성격은 내용으로 판정했다. 수동 자막 없음. `ko` = `ko-orig`(파일 동일, `kind=asr&lang=ko&variant=gemini`) — **한국어 내레이션** 이다. `en-orig`(`kind=asr&lang=en&variant=timing-optimized`)는 **영어 더빙의 ASR** 이다 — 첫 줄부터 내레이션의 영어 번역이고 문장 단위가 ko-orig와 같은 초에 맞물리며, 원 제작자를 3인칭(*Chase, who made the video*)으로 부른다. **en-orig의 내레이션 자리는 인용하지 않았고 판독 대조용으로만 썼다.** 한국어 인용은 전부 ko-orig의 내레이션이다. 429 없음(`--sleep-subtitles 8`).
> **Chase의 원음은 두 곳만 캡션에 있다** — *"This is basically MCP 2.0."*(00:22) 와 맺음 직전의 한 대목(08:05~08:21). 두 곳 모두 **ko-orig와 en-orig 양쪽에 영어로** 잡혀 있어 두 트랙으로 교차 확인했다(타임스탬프는 en-orig 기준). 그 밖의 발췌 자리는 두 트랙 모두 비어 있다.
>
> **무캡션 구간(`gaps.py` 4.5초 기준).** en-orig 일곱 곳: 01:10~01:44 · 02:01~02:19 · 03:39~04:00 · 04:44~05:08 · 05:50~06:05 · 06:43~06:58 · 07:16~07:35 — 합쳐 약 2분 26초. ko-orig는 같은 자리가 `[음악]` 표시로 나뉘어 열한 조각으로 잡힌다(01:10~01:19 · 01:21~01:27 · 01:29~01:44 · 02:01~02:19 · 03:39~04:00 · 04:44~04:52 · 04:54~05:01 · 05:03~05:07 · 05:55~06:05 · 06:43~06:58 · 07:16~07:30).
> ⚠️ **이 구간들은 내용 미상이다.** 여기에 드는 것: *MCP는 이 열쇠를 한 데 모았습니다* 뒤의 발췌(01:10~01:44 — 열쇠 꾸러미 비유의 본론으로 보인다) · **구멍 넷 가운데 첫째의 끝과 둘째 전체(02:01~02:19)** — 내레이션은 뒤에서 넷을 *설명서, 기다림, 안전장치, 채팅* 이라고 다시 부르므로 둘째가 *기다림* 인 것만 알 수 있고 그 설명은 캡션에 없다 · Tasks 소개 뒤의 발췌(03:39~04:00 — 챕터 제목의 *번호표* 비유로 보이나 그 설명은 캡션에 없다) · Elicitation 소개 뒤의 발췌(04:44~05:08) · File Uploads 설명 뒤(05:50~06:05) · GitHub MCP 데모에서 스킬 목록이 뜬 뒤(06:43~06:58) · *쓰는 사람* 과 *만드는 사람* 사이(07:16~07:35 — 만드는 사람 쪽 설명의 머리).
>
> **ASR 판독(ko-orig → 판독, 괄호는 근거).** *엔트로픽* → Anthropic(설명란 · tags), *태스크 엘리시테이션*(00:17~00:20) → Tasks, Elicitation(쉼표가 빠졌다 — 설명란은 넷을 따로 센다. 더빙도 *Task Elicitation* 으로 붙여 읽는다), *프렌치 만들기*(00:47~00:50) → 브랜치 만들기(더빙 *creating branches*), *클라우드* · *클라우드 코드* → Claude · Claude Code(설명란 · tags), *체이스에 비유로는 열세 꾸러미의 설명서 바인더가*(02:56~03:00) → 체이스의 비유로는 열쇠 꾸러미에 설명서 바인더가(더빙 *a manual binder arriving with the bundle of keys*), *쇼피파이* → Shopify, *허브스팟* → HubSpot, *아틀라시안* → Atlassian, *카르타* → Carta, *테스크* → Tasks, *주민 폼*(04:30) → ZoomInfo(더빙이 이 철자로 적는다 — 추정), *슈퍼베이스* → Supabase, *레이웨이* → Railway(더빙), *스캔 목록*(06:33~06:36) → 스킬 목록(추정 — 앞뒤 문맥과 뒤의 *서버를 연결하면 스킬이 같이 따라옵니다*. 더빙은 오독을 그대로 옮겨 *a list of scans*), *2.0이라 부름을 하다가 말합니다*(06:18~06:20) → 2.0이라 부를 만하다고 말합니다(더빙 *it could be called 2.0*), *도구 설명을 컨텍스트를 잡아먹는다는*(07:46~07:48) → 도구 설명이 컨텍스트를 잡아먹는다는, *깃허브* → GitHub, *슬랙* → Slack, *스트라이프* → Stripe.
> ⚠️ **판독하지 못한 것.** ① *도구 이름과 설명은 무엇을 할 알려준다고요*(01:55~01:58) — 문장이 깨져 있고 바로 뒤가 무캡션이다. 더빙은 *tool names and descriptions only tell you what they do* 로 옮긴다. Anthropic 발표 글의 원문은 열지 않아 정하지 않았다. ② *심지어 에이전트 로봇 전체를 돌리는 동안*(04:05~04:08) — 더빙도 *entire agent robots*. *에이전트 루프* 로 보이나 정하지 않았다. ③ *올해 올해 다른 같은 방향입니다*(06:05) — 무캡션 직후의 깨진 문장. 더빙은 *Everything this year is heading in the same direction*. *올해 나온 다른 변화도 같은 방향* 으로 보이나 정하지 않았다. ④ *서버를 열었으면 컨텍스트를 85% 넘게 줄입니다*(06:07~06:11) — 더빙 *once the server is opened*. *서버를 여럿 연결했을 때* 로 보이나 조건이 무엇인지 정하지 않았다. 85%의 출처 · 기준도 캡션에 없다. ⑤ *그냥 대시를 쓰라더니 하는 글*(07:51) — 더빙 *Why not just use a dash?*. *배시(Bash)* 로 보이나 정하지 않았다. 두 글의 작성자도 캡션에 없다. ⑥ *칸반 플랜 테스트 저장소*(06:58~07:00) — 저장소 이름의 표기를 확인하지 못했다(더빙 *Kanban Plan Test repository*). ⑦ *설명서, 번호표 되묻기 따로 내는 창구*(08:24~08:27) — 넷(설명서 · 번호표 · 되묻기 · 따로 내는 창구)으로 읽었다. 더빙은 셋으로 뭉갠다(*an instruction manual, a ticket system, and a counter for follow-up questions*).
>
> ⚠️ **해설이고 3차 전달이다.** Anthropic 발표 글 → Chase AI 영상 → Tech Bridge 한국어 해설 순서다. 위키는 원본 영상(`jVTyW6gosOE`)도 Anthropic 발표 글(*MCP servers can now ship skills, run tasks, and more*, 2026-11-24 — 제목 · 날짜는 설명란 표기)도 MCP 규격 · 확장 문서도 열지 않았다. *MCP 2.0* 은 Chase의 표현이고 공식 버전 이름이 아니다. 내레이션이 *발표 글은 · 확장 문서를 보면 · 규격 문서는* 이라고 옮긴 내용은 전부 내레이션의 전달이다.


## 설명란

앤트로픽이 MCP(Model Context Protocol)에 스킬, 긴 작업(Tasks), 사용자에게 되묻기(Elicitation), 파일 업로드를 더했습니다. Chase AI는 이 변화를 "MCP 2.0"이라고 부릅니다. 2년 전 MCP가 남긴 구멍 넷과 이번 업그레이드 넷을 하나씩 짝지어 보고, GitHub MCP 데모로 실제로 무엇이 달라지는지 확인합니다. 마지막으로 "MCP냐 CLI냐"라는 질문에 대한 그의 답을 정리합니다.

발표 글 기준으로 Skills over MCP는 아직 공개 베타입니다.

타임라인
0:00 MCP 2.0이 나왔다
0:33 MCP는 열쇠 꾸러미
1:43 꾸러미의 구멍 넷
2:45 설명서가 따라온다 (Skills)
3:32 번호표를 받는다 (Tasks)
4:36 지우기 전에 묻는다 (Elicitation)
5:32 파일은 따로 보낸다 (File Uploads)
6:21 GitHub MCP 데모
7:09 쓰는 사람, 만드는 사람
7:42 MCP냐 CLI냐

참고
원본 영상: https://www.youtube.com/watch?v=jVTyW6gosOE
Anthropic, MCP servers can now ship skills, run tasks, and more (2026.11.24): https://claude.com/resources/articles/skills-over-mcp-tasks-and-more

#MCP #ClaudeCode #Anthropic #AI에이전트 #ModelContextProtocol

> info.json `tags`: AI 에이전트 · Anthropic · Chase AI · Claude · Claude Code · Elicitation · GitHub MCP · MCP · MCP 2.0 · MCP 서버 · Model Context Protocol · Skills · 앤트로픽 · 클로드 코드

## 트랜스크립트 — ko-orig (Korean, ASR variant=gemini — 한국어 내레이션(`ko`와 파일 동일). Chase 원음 두 곳(00:22~00:23 · 08:05~08:21)이 영어로 잡혀 있다. 나머지 발췌 자리는 무캡션(`[음악]` 표시만))

[00:00] MCP 나온지 2년. 이번
[00:02] 업그레이드를 두고 MCP 2.0이라는
[00:04] 말까지 나왔습니다.
[00:06] 이 저장소 정리해줘.
[00:07] 예전에는 이 한마디에 AI가 저장소를
[00:09] 통째로 지울 수도 있었습니다.
[00:12] 이제는 지우기 전에
[00:13] 이름부터 직접 치라고 합니다.
[00:15] 엔트로픽이 한꺼번에 내놓은 변화는 네
[00:17] 가지. 스킬, 태스크 엘리시테이션,
[00:20] 그리고 파일 업로드입니다.
[00:22] >> This is basically
[00:23] MCP 2.0.
[00:25] >> 도대체 뭐가 달라졌길래
[00:26] 2.0이라고까지 부를까요?
[00:28] CLI가 있는데 MCP를 왜 쓰냐던
[00:30] 사람이 생각을 바꾼 이유까지 따라가
[00:32] 봅니다.
[00:34] MCP는 AI가 깃허브나 슬랙 같은
[00:36] 바깥 서비스를 쓸 수 있게 해주는
[00:37] 연결 규칙입니다.
[00:38] 엔트로픽이 2년 전에 내놓았습니다.
[00:40] [음악] 영상을 만든 체이스는 이걸
[00:42] 열쇠에 빗대어 설명합니다. MCP가
[00:44] 없던 시절 내 [음악] 앱이 깃허브와
[00:45] 일하려면 API를 한 번에 하나씩
[00:47] 불러야 했습니다. 이슈 읽기, 프렌치
[00:50] 만들기, 커밋, 풀 리퀘스트.
[00:52] API 호출 하나를 문 하나 여는
[00:54] 열쇠로 보면 풀 리퀘스트 하나에
[00:56] 열쇠가 네 개 되는 셈입니다.
[00:58] 개발자는 열쇠마다 이름과 하는 일,
[00:59] 코드 짜는 [음악] 법, 쓰는 순서를
[01:01] 다 알아야 했습니다. 슬랙도,
[01:03] 스트라이프도 마찬가지였고요.
[01:04] 체이스는 이걸 흩어진 열쇠 더미라고
[01:06] 부릅니다.
[01:07] MCP는 이 열쇠를 한 데
[01:08] 모았습니다. [음악]
[01:19] [음악]
[01:27] [음악]
[01:44] 편해졌지만 이 꾸러미에는 구멍이 네
[01:46] 개 있었습니다. [음악]
[01:47] 첫째는 설명서가 없었다는 겁니다.
[01:49] 열쇠와 이름표는 있는데 우리 팀은 이
[01:51] 일을 이런 순서로 한다는 요령은 담을
[01:53] 곳이 없었습니다. 엔트로픽도 발표
[01:55] 글에 그렇게 적었습니다. 도구 이름과
[01:57] 설명은 무엇을 할
[01:58] 알려준다고요.
[02:19] 셋째는 안전장치가 없었다는 겁니다.
[02:21] 이 저장소 정리해 줘라고 하면
[02:23] 저장소를 아예 지워버릴 위험이
[02:24] 있었습니다.
[02:25] [음악] 넷째 모든 게 채팅을
[02:27] 거쳤습니다. 파일 하나를 서버에
[02:28] 넘기려 해도 대화창에 실렸고 그만큼
[02:30] 컨텍스트 창이 찼습니다.
[02:32] 컨텍스트 창은 AI가 한 번에 붙들고
[02:34] 있는 대화 분량입니다. 찰수록
[02:36] 메시지마다 비용이 늘고 성능은
[02:38] 떨어집니다.
[02:39] 설명서, 기다림, 안전장치, 채팅
[02:42] 이번 업그레이드 네 가지가 이 구멍을
[02:43] 하나씩 막습니다.
[02:45] 첫 번째는 스킬 오버 MCP입니다.
[02:47] 스킬은 AI에게 일하는 요령을 적어
[02:49] 준 설명서 파일입니다. 이제 MCP
[02:51] 서버가 도구와 함께 스킬을 직접
[02:53] [음악] 실어 보냅니다.
[02:54] 서버가 클라우드에게 자기 사용법을
[02:56] 가르치는 겁니다. 체이스에 비유로는
[02:58] 열세 꾸러미의 설명서 바인더가 함께
[03:00] 달려 나오는 셈입니다.
[03:02] 스킬을 전부 대화에 밀어넣지도
[03:03] 않습니다. 필요할 때만 부르니
[03:05] 컨텍스트를 적게 씁니다.
[03:07] 서버가 업데이트되면 스킬도 같이
[03:08] 바뀌어서 사용자가 따로 설치할 것도
[03:10] 없습니다.
[03:11] 발표 글에 나온 사례로는 쇼피파이가
[03:13] 온라인 상점 설계를 처음부터 끝까지
[03:15] 돕고 허브스팟은 고객 온보딩을
[03:17] 맡습니다.
[03:18] 아틀라시안은 조직 간의 맥락을 끌어와
[03:20] 업무를 분석하게 하고 카르타는 올린
[03:22] 문서로 지분 서류를 만드는 스킬을 곧
[03:24] 내놓습니다.
[03:25] 다만 스킬 오버 MCP는 아직 공개
[03:27] 베타입니다. 클라우드와 클라우드
[03:29] 코드의 프로, 맥스, 울트라
[03:30] 요금제에서는 기본으로 [음악] 켜져
[03:31] 있습니다.
[03:33] 두 번째는 테스크입니다. 오래 걸리는
[03:35] 일을 MCP 서버 뒤편에서 돌리는
[03:36] 기능입니다.
[04:00] 발표 글은 이렇게 씁니다. 예전엔
[04:01] 도구 호출이 끝나야 클라우드가
[04:03] 다음으로 넘어갈 수 있었다.
[04:05] 이제는 서버가 오래 걸리는 작업,
[04:06] 심지어 에이전트 로봇 전체를 돌리는
[04:08] 동안 클라우드는 계속 일하고 결과가
[04:10] 준비되면 받아갑니다.
[04:12] 확장 문서를 보면 작업마다 상태가
[04:14] 붙습니다. 진행 중, 입력 필요,
[04:16] 완료, 실패, 취소.
[04:18] 입력이 필요하면 작업이 잠깐 멈추고
[04:20] 사용자에게 묻습니다.
[04:22] 이 물음이 다음 기능 엘리시테이션으로
[04:24] 이어집니다.
[04:25] 작업마다 번호가 있어서 중간에 연결이
[04:27] 끊겨도 그 번호로 다시 상태를 물어볼
[04:29] 수 있습니다.
[04:30] 주민 폼은 태스크로, 예전엔
[04:32] 프롬프트를 여러 번 써야 했던 고객과
[04:34] 연락처 조사를 더 깊게 돌립니다.
[04:37] 세 번째는 엘리시테이션, 우리말로
[04:39] 되묻기입니다. [음악] MCP 서버
[04:41] 안에 들어간 안전 장치입니다.
[04:52] [음악]
[05:01] [음악]
[05:07] 발표 글도 돈을 쓰거나 데이터를
[05:09] 지우는 일엔 사용자 승인이 필요하다고
[05:11] 씁니다. 서버가 호출 도중에 멈추고
[05:14] 묻습니다. [음악]
[05:15] 슈퍼베이스는 유료 프로젝트를 만들거나
[05:17] 위험한 SQL을 돌리기 전에 비용을
[05:18] 확인하고, 레이웨이는 서비스를 지우기
[05:21] 전에 묻습니다. [음악] 묻는 방법은
[05:23] 둘입니다. 화면에 입력 폼을 띄우거나
[05:25] 바깥 링크로 보냅니다.
[05:27] 규격 문서는 비밀번호나 API 키
[05:28] 같은 민감한 정보를 폼으로 받으면 안
[05:30] 된다고 못 박았습니다.
[05:33] 네 번째는 파일 업로드입니다. 넷 중
[05:35] 유일하게 아직 나오지 않았고 곧
[05:36] 배포됩니다.
[05:37] PDF나 스프레드시트 이미지를
[05:39] 컨텍스트 창을 거치지 않고 서버로
[05:41] 바로 보냅니다.
[05:42] 문서를 보면 대화에는 파일 이름과
[05:44] 크기 같은 정보만 오가고 실제 파일
[05:46] 내용은 서버가 알려준 주소로 따로
[05:48] 올라갑니다.
[05:53] [음악]
[06:05] 올해 올해 다른 같은 방향입니다.
[06:06] [음악]
[06:07] 도구 검색은 도구 설명을 필요할 때만
[06:09] 불러와 서버를 열었으면 컨텍스트를
[06:11] 85% 넘게 줄입니다.
[06:13] 서버를 늘리기 쉬운 상태 없는 규격,
[06:15] 대화 옆에 화면을 띄우는 MCP
[06:17] 앱까지.
[06:18] 체이스는 이걸 다 합치면 2.0이라
[06:20] 부름을 하다가 말합니다.
[06:22] 이제 체이스의 데모입니다. 클라우드
[06:24] 코드 2.1.331 버전 이상이면
[06:26] 터미널과 데스크톱에 모두 됩니다.
[06:28] [음악] 깃허브 MCP는 태스크는
[06:30] 쓰지 않습니다. 네 기능 중 무엇을
[06:31] 쓸지는 서버마다 다릅니다. [음악]
[06:33] 슬래시 깃허브를 치자 스캔 목록이 쭉
[06:36] 뜹니다. 이슈 작성, 릴리스 준비,
[06:38] 코드 베이스 탐색. 원래 MCP
[06:40] 서버에는 없던 것들입니다.
[06:58] 이번엔 깃허브 MCP로 칸반 플랜
[07:00] 테스트 저장소를 지워달라고 합니다.
[07:03] 클라우드가 삭제 도구를 부르자 서버가
[07:04] 끼어듭니다. 저장소 이름을 정확히
[07:06] 쳐야 하고 안 치면 아무것도 지워지지
[07:08] 않습니다.
[07:10] 쓰는 사람은 할 일이 거의 없습니다.
[07:12] 서버를 연결하면 스킬이 같이
[07:13] 따라옵니다.
[07:30] [음악]
[07:35] 만드는 사람 쪽에서 보면 네 기능
[07:36] 모두 열린 MCP 규격의 일부라
[07:38] 클라우드가 아닌 다른 호환
[07:40] 클라이언트에서도 돌아갑니다.
[07:42] 올해 개발자들 사이에선 MCP 대신
[07:44] CLI를 쓰자는 말이 돌았습니다.
[07:46] 도구 설명을 컨텍스트를 잡아먹는다는
[07:48] 불만도 컸습니다.
[07:49] 체이스가 보여준 반응도 그렇습니다.
[07:51] 그냥 대시를 쓰라더니 하는 글.
[07:53] MCP는 죽었다고 들었는데 하는 글.
[07:55] 두 번째 글은 이번 변화를 셋으로
[07:57] 줄입니다.
[07:57] 사용법을 도구와 함께 보내고 오래
[07:59] 도는 작업을 다루고 되묻기가 제대로
[08:01] 된다.
[08:05] >> which is like, why
[08:06] would I even use
[08:07] MCPs when CLIs
[08:08] exist?
[08:08] It may be time to
[08:09] kind of rethink that
[08:10] [음악] because these
[08:11] MCP servers are
[08:12] getting way more
[08:12] robust and just from
[08:14] sort of the context
[08:15] wins alone, it might
[08:16] be worth it to start
[08:17] transitioning from
[08:18] CLIs to MCPs, or at
[08:20] least think about
[08:21] it.
[08:22] >> 정리하면 열쇠 꾸러미는 그대로입니다.
[08:24] 거기에 설명서, 번호표 되묻기 따로
[08:27] 내는 창구가 붙었습니다.
[08:30] 처음에 그 한 마디 이 저장소 정리해
[08:32] 줘. [음악]
[08:33] 이제 MCP 서버는 지우기 전에
[08:34] 이름부터 확인합니다.

## 트랜스크립트 — en-orig (영어 더빙 ASR — 내레이션 자리는 인용하지 않음, 판독 대조용. Chase 원음 두 곳(00:22 · 08:05~08:21)은 여기에도 잡혀 교차 확인에 썼다. 무캡션 일곱 곳(약 2분 26초))

[00:00] Two years since MCP was released. People
[00:02] are even calling this upgrade MCP 2.0.
[00:05] "Clean up this repository."
[00:07] In the past, one simple command could
[00:09] have led the AI to delete the entire
[00:10] repository.
[00:12] Now, it asks you to type out the name
[00:14] before deleting it.
[00:15] Anthropic introduced four major changes
[00:17] all at once.
[00:18] They are Skills, Task Elicitation, and
[00:20] file uploads.
[00:22] >> This is basically MCP 2.0.
[00:25] >> What exactly has changed to warrant
[00:27] calling it 2.0?
[00:29] We’ll follow why someone who questioned
[00:30] the need for MCP when we have CLI
[00:31] changed their mind.
[00:34] MCP is a connection protocol that lets
[00:35] AI use external services like GitHub or
[00:37] Slack.
[00:38] Anthropic released it two years ago.
[00:41] Chase, who made the video, explains this
[00:42] using an analogy of keys.
[00:44] Before MCP, for my app to work with
[00:46] GitHub, I had to call APIs one by one.
[00:49] Reading issues, creating branches,
[00:50] commits, and pull requests.
[00:52] If one API call is a key to a door, a
[00:54] single pull request would require four
[00:57] keys.
[00:58] Developers had to know the name,
[00:59] function, syntax, and order for every
[01:01] single key.
[01:02] It was the same for Slack and Stripe.
[01:04] Chase calls this a pile of scattered
[01:06] keys.
[01:07] MCP gathered these keys into one place.
[01:44] It became convenient, but there were
[01:45] four gaps in this bundle. First, there
[01:47] were no manuals.
[01:49] You had keys and labels, but no place to
[01:51] define how our team does things in what
[01:53] order.
[01:54] Anthropic also mentioned this in their
[01:55] announcement. That tool names and
[01:57] descriptions only tell you what they do
[01:59] .
[02:19] Third, there were no safety features. If
[02:21] you said "clean up this repository,"
[02:22] there was a risk of it being deleted
[02:24] entirely.
[02:25] Fourth, everything had to go through
[02:27] chat. Even to send a single file to the
[02:29] server, it had to go through the chat
[02:30] window, filling up the context window.
[02:32] The context window is the amount of
[02:34] conversation the AI can hold at once. As
[02:36] it fills up, costs per message rise and
[02:37] performance drops.
[02:39] Manuals, waiting, safety, and chat—
[02:41] these four upgrades plug these gaps one
[02:43] by one.
[02:45] The first is Skills over MCP.
[02:48] A Skill is a manual file that provides
[02:49] the AI with "how-to" instructions. Now,
[02:51] the MCP server sends the Skills directly
[02:53] along with the tools.
[02:54] The server teaches Claude how to use it
[02:56] .
[02:57] In Chase's analogy, it's like a manual
[02:59] binder arriving with the bundle of keys
[03:01] .
[03:02] It doesn't even push all the skills into
[03:03] the conversation. It uses less context
[03:05] because it only calls them when needed.
[03:07] When the server is updated, the skills
[03:08] update too, so there's nothing for the
[03:10] user to install.
[03:11] Examples from the announcement include
[03:13] Shopify helping design online stores
[03:15] from start to finish, and HubSpot
[03:16] handling customer onboarding.
[03:18] Atlassian enables analyzing work by
[03:19] pulling in organizational context, and
[03:21] Carta will soon release a skill that
[03:22] creates equity documents from uploaded
[03:24] files.
[03:25] However, Skills over MCP is still in
[03:27] public beta.
[03:28] It is enabled by default in the Pro, Max
[03:30] , and Ultra plans for Claude and Claude
[03:31] Code.
[03:33] The second feature is Tasks. This
[03:34] feature runs time-consuming tasks in the
[03:36] background on the MCP server.
[04:00] The announcement describes it like this
[04:01] . Previously, Claude had to wait for a
[04:02] tool call to finish before moving on to
[04:03] the next step.
[04:05] Now, Claude continues to work while the
[04:07] server handles long-running jobs or even
[04:08] entire agent robots, retrieving the
[04:10] results when ready.
[04:12] Looking at the documentation, each task
[04:14] is assigned a status. In progress, input
[04:16] required, completed, failed, and
[04:17] canceled.
[04:18] If input is required, the task pauses
[04:20] briefly to ask the user.
[04:22] This query leads to the next feature:
[04:24] Elicitation.
[04:25] Each task has an ID, so even if the
[04:27] connection is lost, you can check its
[04:28] status using that number.
[04:30] ZoomInfo uses Tasks to conduct deeper
[04:32] customer and contact research that
[04:34] previously required multiple prompts.
[04:37] The third is Elicitation, which means
[04:38] asking for confirmation or additional
[04:39] information. It is a safety mechanism
[04:41] built into the MCP server.
[05:07] The announcement states that user
[05:09] approval is required for actions
[05:10] involving spending money or deleting
[05:11] data.
[05:12] The server pauses during the call to ask
[05:14] .
[05:15] Supabase confirms costs before creating
[05:17] paid projects or running risky SQL, and
[05:19] Railway asks before deleting services.
[05:22] There are two ways to ask. Either by
[05:24] displaying an input form on the screen
[05:25] or sending the user to an external link
[05:26] .
[05:27] The specification document strictly
[05:28] prohibits collecting sensitive
[05:29] information like passwords or API keys
[05:31] via these forms.
[05:33] The fourth feature is File Upload. It is
[05:35] the only one of the four not yet
[05:36] released, but it is coming soon.
[05:37] It sends PDFs, spreadsheets, or images
[05:39] directly to the server without going
[05:40] through the context window.
[05:42] According to the documentation, only
[05:44] info like filename and size is exchanged
[05:45] in the chat, while the file content is
[05:47] uploaded to a server-provided address.
[06:05] Everything this year is heading in the
[06:06] same direction. Tool retrieval fetches
[06:08] tool descriptions only when needed,
[06:10] reducing context usage by over 85%once
[06:11] the server is opened.
[06:13] From a stateless architecture that makes
[06:14] scaling servers easy to MCP apps that
[06:16] display interfaces alongside the chat.
[06:18] Chase says that when you combine all of
[06:19] these, it could be called 2.0.
[06:22] Now, it's time for Chase's demo. It
[06:24] works on both terminal and desktop if
[06:25] you have Claude Code version 2.1.331 or
[06:27] higher.
[06:28] The GitHub MCP does not use Tasks. Which
[06:31] of the four features to use depends on
[06:32] the specific server.
[06:34] I type slash GitHub and a list of scans
[06:36] pops up. Issue creation, release
[06:37] preparation, and code base exploration.
[06:39] These were not originally in the MCP
[06:40] server.
[06:58] This time, I ask the GitHub MCP to
[07:00] delete the Kanban Plan Test repository.
[07:03] As Claude calls the delete tool, the
[07:04] server intervenes. I must enter the
[07:06] repository name exactly, or nothing gets
[07:08] deleted.
[07:10] The user has almost nothing to do. When
[07:12] you connect the server, the skills come
[07:13] along with it.
[07:35] From a creator's perspective, all four
[07:36] features are part of the open MCP
[07:38] standard, so they work on other
[07:39] compatible clients, not just Claude.
[07:42] This year, developers were talking about
[07:44] using CLIs instead of MCP.
[07:46] There were also major complaints that
[07:47] tool descriptions consume too much
[07:48] context.
[07:49] The reaction Chase showed is the same.
[07:51] Posts like "Why not just use a dash?"
[07:53] Posts like "I heard MCP was dead." The
[07:55] second post summarizes these changes
[07:56] into three points.
[07:58] Sending instructions with tools,
[07:59] handling long-running tasks, and
[08:00] enabling proper follow-up questions.
[08:05] >> which is like, why would I even use MCPs
[08:07] when CLIs exist?
[08:09] It may be time to kind of rethink that
[08:11] because these MCP servers are getting
[08:13] way more robust and just from sort of
[08:15] the context wins alone, it might be
[08:17] worth it to start transitioning from
[08:18] CLIs to MCPs, or at least think about it
[08:21] .
[08:22] >> In short, the key ring remains the same
[08:24] . Added to it are an instruction manual
[08:25] , a ticket system, and a counter for
[08:27] follow-up questions.
[08:30] That single initial command, "Clean up
[08:31] that repository."
[08:33] Now, the MCP server checks the name
[08:34] first before deleting it.

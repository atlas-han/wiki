---
title: Rob Shocks
type: entity
category: person
tags: [creator, grokbot, claude-code, cursor, software-factory, orchestration]
aliases: [Rob Shocks, 롭 쇼크스]
links: []
sources: [tech-bridge-rob-shocks-grokbot-manager-coding-agents, tech-bridge-rob-shocks-orca-review-vs-records]
created: 2026-11-03
updated: 2026-11-18
---

# Rob Shocks

AI 코딩 워크플로를 다루는 영어 해설 영상 제작자. 이 위키에는 [[tech-bridge-rob-shocks-grokbot-manager-coding-agents]](2026-11-02 업로드)로 처음 등장한다. 그 영상에서 [[grokbot|GrokBot]]을 코딩하지 않는 **매니저**로 두고 코드 작성은 [[claude-code|Claude Code]] · [[cursor-cloud|Cursor Cloud]] agents에 넘기는 자기 구성을 보여 준다.

## 귀속의 근거

- **이름은 설명란에만 있다** — *"Rob Shocks가 Claude Code와 클라우드 코딩 에이전트에 일을 맡기고 결과를 검증하는 구성을 소개합니다"*. 발화와 info.json `tags`에는 이름이 없다. 원본 채널명과 원본 링크도 없다.
- 발화로 확인되는 것은 **1인칭 채널 화법**뿐이다: *"for my own factory, I have bots set up for each area of my company"*(07:00~07:05), *"I use very same setup for this channel"*(08:48~08:52), *"You can also see that in my last video."*(06:30~06:33).
- 목소리 동일성은 확인하지 않았다.

## 위키에서 알려진 것 (자기 진술)

- 메인 에이전트 이름은 **Chief**이고 봇끼리 그룹 채팅을 한다. 봇마다 연결 권한을 좁게 둔다(07:13~07:25).
- 실행 환경은 Mac의 컨테이너, VPS, 별도 PC다. Claude Code는 headless로, 모델을 지정해 띄운다(02:46~02:53 · 08:42~08:48).
- 채널 영상의 화면 자료도 같은 구성으로 만든다. *"when I'm having Opus 5.5 helping with visuals"*(08:50~08:53) → [[claude-opus-5-5]]
- 백로그는 Notion에 두고, RICE 점수와 blast radius 점수로 분류한다(09:27~09:50).
- 태도: GrokBot이 자격 증명을 저장하는 것, 메모리와 스킬이 보이지 않는 것이 불편하다고 말한다(07:26~07:41). 그래도 *"experiment on the edge of what's possible just so I can share it with you guys"*(07:48~07:50).
- 다른 사람의 사례를 많이 옮긴다. [[lauren-tan|Lauren Tan]](두 번), Anthropic, Alan Wells, Theo, Docker 등이 그 예다. 출처는 대부분 말하지 않는다.

## 미해결 — 이 위키의 화자 미상 두 편과 같은 사람인가

자기 언급 두 개가 이 위키에 이미 있는 영상의 주제와 겹친다.

| 발화 | 겹치는 위키 소스 | 그 소스의 화자 기록 |
|---|---|---|
| *"I covered a lot of that in Entropic's SDLC in a video while back"*(00:34~00:38) | [[tech-bridge-ai-native-sdlc]](09-04, Anthropic AI-Native SDLC 해설) | [[switch-dimension|Switch Dimension]] 강사, 이름 없음 |
| *"some of her skills we covered on Pystack in another video previously"*(03:31~03:34) | [[tech-bridge-pstack-third-party-review]](09-13) | [[molten-base|Molten Base]] 제작자, 이름 없음, 강의 운영, *"Theo"* 를 언급 |

> ⚠️ **같은 사람일 가능성만 있다.** 주제가 겹친다는 것 말고 다른 근거는 없다. Switch Dimension의 저장소 이름 `molten-os-core`와 Molten Base는 이름이 비슷하지만, 이것도 같은 사람이라는 증거는 아니다. 같은 주제를 다룬 다른 영상일 수도 있다. 이 위키는 두 페이지의 화자 기록을 고치지 않는다.

## References

- [[tech-bridge-rob-shocks-grokbot-manager-coding-agents]] · [[manager-bot-coding-agent-split]] · [[grokbot]] · [[lauren-tan]]

## 2026-11-18 — 두 번째 소스: Orca 리뷰, 그리고 처음 발화된 이름 ([[tech-bridge-rob-shocks-orca-review-vs-records]])

Tech Bridge가 그의 리뷰 영상(설명란 원본 링크 `73DrNNvEKH0`, 위키 미열람)을 공식 기록과 맞춰 본다. **위 *귀속의 근거* 가 달라진다** — 이번에는 내레이션이 이름을 말한다: *"리뷰한 사람은 롭 쇼크스입니다. 에이전트 개발 환경을 두루 써보고 영상으로 남겨온 유튜버입니다."*(00:59~01:02) 설명란 · tags · 원본 링크도 있다.

- 주장(해설이 받아 말한 것): [[claude-code|Claude Code]]를 돌리는 기본 도구를 [[orca|Orca]]로 바꿨다. 두 달 전에는 모자랐던 도구가 지금은 기본값이 됐다.
- 해설의 대조 결과: 채팅 모드를 *새 기능* 이라 한 것은 기록과 다르다(릴리스 기록에 6월 말부터) · 브라우저 확장과 비밀번호 대목은 날짜가 맞다(11월 5일 · 13일 릴리스, 리뷰는 그 하루 뒤) · *지연이 사라졌다* 는 표현은 *"쇼크스의 말처럼 지연이 사라진 건 아닙니다. 타자를 칠 때 느껴지지 않을 뿐입니다."*(06:05~06:08) 로 고쳐진다.
- ⚠️ **그의 원음 발췌 여덟 곳은 전부 무캡션** 이라 본인 발화는 인용할 수 없다. 영어 더빙 ASR은 이름을 *Rob Shouksmith* 로 적는다 — 근거로 쓰지 않는다.
- 11-03 편의 *매니저 봇 + 코딩 에이전트* 구성과 이 리뷰의 관계(같은 작업대 위에서 도는지)는 말하지 않는다.

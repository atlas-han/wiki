---
title: Mehul Mohan
type: entity
category: person
tags: [developer, youtuber, claude-code, cli, agent-multiplexer, user-review]
aliases: [Mehul Mohan, Mehul, 메훌 모한]
links: []
sources: [tech-bridge-mehul-mohan-herdr-app-vs-cmux]
created: 2026-11-01
updated: 2026-11-01
---

# Mehul Mohan

**CLI 하네스와 에이전트 관리 도구를 직접 써 보고 비교하는 개발자 화자.** 이 위키에는 [[tech-bridge-mehul-mohan-herdr-app-vs-cmux]](2026-10-31 업로드)로 처음 등장한다. 그 영상은 [[herdr]] 앱 발표 당일의 1인칭 화면 시연이다.

> ⚠️ **신원 근거.** 이름은 발화에 나온다. 시청자 질문을 옮기며 자기를 부른다: *"Then why, Mehul, why do you prefer like CLI AI harnesses?"*(01:15~01:20). 성 Mohan은 설명란(*"개발자 Mehul Mohan이"*)에만 있다. info.json 태그에는 이름이 없다. 소속 · 직함 · 채널명은 발화되지 않는다. 1인칭 단서로 보면 자기 시청자가 있는 채널을 운영하고(*"if you have been following me"* 00:21~00:23), 영상 편집을 Claude에게 맡긴다(10:13~10:26).

## 위키에서의 진술

- **CLI = 유연성**: *"CLI means flexibility"*(02:55~02:57). 예로 [[claude-code|Claude Code]]의 새 *"even more dangerously skip permissions flag"*(01:31~01:39, ⚠️ 미확인)를 든다. 데스크톱 앱에서는 같은 설정이 *"hidden inside settings"*(03:21)다.
- **에이전트 관리 화면**: tmux나 iTerm 하나로 버티지 말고 *"a agent multiplexer or agent manager sort of screen"*(08:33~08:35)을 쓰라고 한다. 필요한 것은 여러 머신, 민감한 작업용 자기 컴퓨터, 상태별로 정리된 에이전트다(09:42~09:56).
- **로컬 vs VM**: *"very data heavy or requires you often"*(10:06~10:09)인 작업, 예컨대 8~10 GB 영상 편집은 로컬에 둔다. 사람이 영상을 직접 봐야 하는 피드백 루프도 로컬이 빠르다. 나머지 기능 개발 · 버그 수정은 VM에 둔다 → [[cloud-agent-delegation]]
- **모바일**: VM의 Claude Code 세션을 Anthropic의 Remote Control로 휴대폰에서 조종한다. *"works flawlessly at least for me"*(11:58~12:01)
- **[[cmux]] 비판**: SSH 세션이 앱 종료와 함께 사라지고, tmux 우회책은 실험 기능이라 잘 깨진다(13:05~13:46).

## References

- [[tech-bridge-mehul-mohan-herdr-app-vs-cmux]]
- 관련: [[herdr]] · [[cmux]] · [[claude-code]]

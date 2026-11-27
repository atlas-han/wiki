---
title: "MCP 되묻기 (Elicitation)"
type: concept
category: pattern
tags: [mcp, elicitation, human-approval, destructive-actions, guardrails, server-side-enforcement, safety]
aliases: [Elicitation, MCP Elicitation, 엘리시테이션, 되묻기, 지우기 전에 묻는다]
related: [model-context-protocol, hard-vs-soft-enforcement, mcp-skill-distribution, risk-proportional-human-review, human-as-async-api, mcp-toolbox-for-databases]
first-seen: tech-bridge-chase-ai-mcp-2-0-biggest-upgrade
sources: [tech-bridge-chase-ai-mcp-2-0-biggest-upgrade]
created: 2026-11-27
updated: 2026-11-27
---

# MCP 되묻기 (Elicitation)

**MCP 서버가 도구 호출 도중에 멈추고 사용자에게 직접 묻는 장치.** [[anthropic|Anthropic]]이 2026년 11월 [[model-context-protocol|MCP]]에 더했다고 전해진 네 가지(Skills over MCP · Tasks · Elicitation · File Uploads) 가운데 하나이고, 위키에는 한국어 해설 [[tech-bridge-chase-ai-mcp-2-0-biggest-upgrade]]로 들어왔다. *"세 번째는 엘리시테이션, 우리말로 되묻기입니다. MCP 서버 안에 들어간 안전 장치입니다."*(04:37~04:41)

> ⚠️ **3차 전달이다.** Anthropic 발표 글 → [[chase-ai|Chase AI]]의 영상 → Tech Bridge 해설. 아래 인용은 전부 한국어 내레이션이고, 위키는 발표 글 · MCP 규격 문서 · 원본 영상을 열지 않았다. 되묻기를 소개한 직후의 발췌(04:44~05:08)는 무캡션이라 그 설명은 적지 못했다.

## 무엇을 막는가

- 해설이 드는 장면: *"이 저장소 정리해줘."*(00:06) *"예전에는 이 한마디에 AI가 저장소를 통째로 지울 수도 있었습니다."*(00:07~00:09) MCP가 남긴 구멍 넷 가운데 셋째 — *"셋째는 안전장치가 없었다는 겁니다."*(02:19)
- 발표 글(내레이션 전달): *"돈을 쓰거나 데이터를 지우는 일엔 사용자 승인이 필요하다고 씁니다. 서버가 호출 도중에 멈추고 묻습니다."*(05:07~05:14)

## 어떻게 묻는가

- 방법 둘: *"화면에 입력 폼을 띄우거나 바깥 링크로 보냅니다."*(05:23~05:25)
- 금지: *"규격 문서는 비밀번호나 API 키 같은 민감한 정보를 폼으로 받으면 안 된다고 못 박았습니다."*(05:27~05:30)
- Tasks와의 이음매: 오래 도는 작업의 상태 가운데 *입력 필요* 가 있다 — *"입력이 필요하면 작업이 잠깐 멈추고 사용자에게 묻습니다."*(04:18~04:20) *"이 물음이 다음 기능 엘리시테이션으로 이어집니다."*(04:22~04:24)

## 사례 (전부 내레이션 전달)

- Supabase · [[railway|Railway]]: *"슈퍼베이스는 유료 프로젝트를 만들거나 위험한 SQL을 돌리기 전에 비용을 확인하고, 레이웨이는 서비스를 지우기 전에 묻습니다."*(05:15~05:21)
- GitHub MCP(Chase의 데모): *"클라우드가 삭제 도구를 부르자 서버가 끼어듭니다. 저장소 이름을 정확히 쳐야 하고 안 치면 아무것도 지워지지 않습니다."*(07:03~07:08)[=Claude가]

## 이 위키에서의 좌표

- **[[hard-vs-soft-enforcement]]의 하드 쪽이다.** 모델에게 *조심하라* 고 타이르는 것이 아니라 서버가 호출을 붙잡는다. 모델이 삭제 도구를 불러도 사람이 이름을 치지 않으면 아무 일도 일어나지 않는다.
- **가드레일의 자리가 서버다.** [[mcp-toolbox-for-databases]]가 읽기 전용 · 허용 범위를 서버 설정에 두었다면 되묻기는 **실행 시점의 사람 승인** 을 서버에 둔다. 클라이언트(하네스)의 권한 프롬프트와는 주체가 다르다 — 무엇이 위험한지를 서버 제공자가 정한다.
- **[[risk-proportional-human-review]]와 같은 원리** — 모든 호출이 아니라 돈과 삭제에만 사람을 세운다.
- [[human-as-async-api]]: Tasks의 *입력 필요* 상태와 묶이면 사람의 답을 기다리는 동안 작업이 멈춰 있을 수 있다. ⚠️ 얼마나 기다리는지 · 시간 초과가 어떻게 되는지는 캡션에 없다.

## ⚠️ 유보

- 근거가 한 편의 해설이다. 규격의 실제 문구 · 지원 클라이언트 범위 · 출시 상태(Skills over MCP는 공개 베타, File Uploads는 미출시라고 했으나 Elicitation의 상태는 발화되지 않았다)는 확인하지 않았다.
- 되묻기를 쓸지는 서버 제공자의 선택이다(*"네 기능 중 무엇을 쓸지는 서버마다 다릅니다."*(06:30~06:31)). 붙이지 않은 서버에서는 셋째 구멍이 그대로다.
- 사람이 이름을 습관처럼 쳐 넣게 되면 장치가 무뎌진다는 점은 소스가 다루지 않는다(위키의 메모).

## References

- [[tech-bridge-chase-ai-mcp-2-0-biggest-upgrade]]

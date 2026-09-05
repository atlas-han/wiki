---
title: Claude Tag
type: entity
category: product
tags: [anthropic, claude-code, slack, agent, delegation]
sources: [tech-bridge-claude-code-team-workflow]
created: 2026-09-05
updated: 2026-09-05
---

# Claude Tag

[[anthropic|Anthropic]]의 **Slack 네이티브 에이전트**. Slack에서 Claude를 태그해 목표를 통째로 맡기는 표면이다. [[tech-bridge-claude-code-team-workflow]]에서 Claude Code 팀이 자기 사용 경험을 증언한다.

> ⚠️ 표기가 소스 안에서 갈린다 — en-orig 자막은 앞부분에서 *"Cloud Tag"*, 14:04 이후에는 *"Claude Tag"* 로 오인식한다. **채널 설명란이 `Claude Tag`로 확정**한다.

## 위키에서 알려진 사실

- **팀 업무의 70~80%** 가 여기서 일어난다. 나머지 20%는 *"세부적인 부분을 수정하거나 Claude를 **세밀하게 관리**하고 싶을 때"* 다른 표면을 연다.
- 다루는 문제의 크기가 다르다 — *"**'이 클래스를 구현하세요'와 같은 단순한 문제들과는 차원이 다릅니다.** Claude Code 개발 초기 단계의 문제들이 바로 그런 종류였죠."*
- 덮는 범위: **검증 · 코드 리뷰 · 브레인스토밍 · 모니터링**.
- **Slack에 사는 이유는 맥락이다.** 팀이 제품에 대해 내린 *"모든 결정들"* 이 이미 거기 있어서, 에이전트가 *"제품 컨텍스트는 뭐지?"* 를 스스로 찾아본다.

### 인터페이스 — 추상화 한 층 위

> 지금 우리는 **Claude가 출력하는 실제 토큰보다 한 단계 높은 추상화 수준**에서 작업하고 있는 것과 같습니다.

- Slack 메시지는 **도구 호출의 결과**이고, *"**내면의 독백은 Slack에서 보이지 않습니다.**"* 전체 녹취록은 **링크**로 따로 제공된다.
- 적응이 양가적이라고 증언한다 — 다 볼 수 없어 처음엔 어려웠지만 *"**Claude가 언제, 무슨 말을 할지 스스로 선택한다는 점에서 정말 자유로워진 것 같기도**"*.
- 전환의 조건은 모델 품질이다 — *"**지금 모델들이 충분히 좋다**는 걸 알았어요. **녹취록을 자세히 검토할 필요 없이.**"*

### 자기 자신을 만든다

> 저희는 **Claude Tag를 이용해서 Claude Tag를 아주 적극적으로 빌드업**하고 있습니다.

한 사례에서 루프 전체가 보인다 — 아이디어 → 이해관계자 모으기 → 목업 → 구현 → 이벤트 계측 → 내부 배포 → **Claude Tag가 사용 현황 모니터링** → *"누군가 피드백을 남기면 **저를 태그해** 주거든요."* 전부 Slack에서, **휴대폰으로도**.

## 위키에서의 좌표

[[claude-code]]가 터미널·데스크톱 표면이라면 Claude Tag는 **채팅 표면**이고, 차이는 UI가 아니라 **위임 단위**다 → [[goal-level-delegation]]. [[tech-bridge-ai-native-sdlc]]가 `intent.md`로 맥락을 **새로 만드는** 접근이라면, Claude Tag는 **이미 맥락이 쌓인 곳으로 에이전트를 옮기는** 반대 방향 해법이다.

## 미해결 사항

- 공개 제품인지 Anthropic 내부 도구인지 소스에서 확정되지 않는다.
- [[claude-code]]·routine·workflows와의 정확한 제품 경계 미확인.
- 권한 모델, Slack 워크스페이스 범위 등 운영 세부 미확인.

## References

- [[tech-bridge-claude-code-team-workflow]] · [[anthropic]] · [[claude-code]]
- 관련: [[goal-level-delegation]] · [[harness-pruning]] · [[dynamic-workflows]]

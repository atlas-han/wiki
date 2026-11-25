---
title: Andrej Karpathy
type: entity
category: person
tags: [researcher, educator, llm, transformer, computer-vision]
aliases: [카파시, Karpathy, 안드레 카파시]
sources: [karpathy-llm-wiki-gist, multica-karpathy-skills-claude-md, tech-bridge-karpathy-transformers-stanford, tech-bridge-six-agent-skills, tech-bridge-agents-vs-humans-optimizer-speedrun, tech-bridge-nick-saraev-karpathy-ai-habits, tech-bridge-karpathy-hackertube-two-hours-five-words, tech-bridge-thariq-shihipar-human-folder-unacceptable, tech-bridge-grace-ableidinger-vibe-vs-agentic-coding]
links:
  - https://karpathy.ai
  - https://github.com/karpathy
created: 2026-05-25
updated: 2026-11-25
---

# Andrej Karpathy

AI 연구자·교육자. 본 위키에 두 갈래로 등장한다 — **위키 운영 패턴의 원안 저자**이자, **트랜스포머 아키텍처의 해설자**.

## 위키 패턴 쪽

- [[llm-wiki-pattern]] 제안자 — RAG와 대비되는 누적적 지식 베이스 패턴. 2026년 gist [[karpathy-llm-wiki-gist]]가 이 LLM-WIKI 구조의 사상적 출처이고 `CLAUDE.md` 헤더가 직접 인용한다.
- "Obsidian = IDE, LLM = programmer, wiki = codebase" 비유의 출처
- [[memex|Memex]] ([[vannevar-bush]], 1945) 계보를 명시적으로 호명하며 LLM이 그 유지보수 부족 문제를 해결한다고 주장
- [[multica-ai]]의 GitHub repo `andrej-karpathy-skills`가 이름을 직접 차용 — Karpathy의 *skills* 컨셉에서 영감 (본인 endorsement 여부 미확인). [[multica-karpathy-skills-claude-md]] 참조

## 연구·교육 쪽 (2026-09-03 추가)

[[tech-bridge-karpathy-transformers-stanford]] (Stanford CS25, **~2023년 강연**의 2026년 재배포)에서 확인된 것:

- **2012년경 AI에 진입**했고 컴퓨터 비전이 전공이었다. 당시를 회고하며 *"AI에 합류했다는 말조차 하지 않았죠. 그건 마치 욕설 같았어요"* 라고 말한다.
- 2011년 비전 파이프라인의 실상에 대한 1인칭 증언 — 특징 기술자를 수십 개 추출해 SVM을 얹던 시절, *"여기저기서 코드를 모아서 실행했는데, 정말 악몽 같았어요"*. [[sutton-bitter-lesson]]의 컴퓨터 비전 항목에 대한 당사자 근거.
- **[[nanogpt|nanoGPT]]** 저자. 강연 시점에 "지금 하고 있는 일"로 지목했고, 컴퓨터 비전 제품에서 언어 도메인으로 옮겨가는 중이라고 밝혔다.
- **Tesla** 재직 경험을 멀티모달 설계 사례로 든다 — ConvNet에 radar·지도·차종을 어떻게 넣을지가 매번 문제였는데 [[transformer]]는 "썰어서 집합에 던져 넣으면" 된다는 것.
- **[[dzmitry-bahdanau]]에게 직접 이메일을 보내** [[attention-mechanism|어텐션]]의 탄생 경위를 확인했다. 이 위키의 어텐션 계보 서술은 그 답장에 근거한다.

### 이 강연에서 나온 그의 프레이밍

| 프레이밍 | 내용 |
|---|---|
| **어텐션 = 그래프 메시지 전달** | 본인이 *"어제 생각해냈다"*고 농담한 개인적 재해석. → [[attention-mechanism]] |
| **트랜스포머가 이긴 3가지 이유** | 표현력 · 최적화 가능성 · **GPU 효율성**. 3번이 가장 저평가됐다고 주장 |
| **범용 컴퓨터 재명명** | *"GPT는 런타임에 재구성되어 자연어 프로그램을 실행하는 범용 컴퓨터"* → [[transformer]] |
| **in-context learning이 핵심** | GPT-3 논문 제목을 바꾸고 싶다고 말한다 → [[in-context-learning]] |
| **scratch pad** | 컨텍스트를 늘리는 대신 모델에게 노트를 주자 — 본인의 [[llm-wiki-pattern]]을 3년 앞서 예고한 셈 |

### 밝힌 선호·불만

- **autoregressive를 좋아하지 않는다** — *"토큰을 샘플링하고 거기에 커밋해 버리는 게 이상하다"*. diffusion 하이브리드를 선호한다고 밝힘
- **graph neural network라는 용어가 헷갈린다** — *"오늘날에는 어쩌면 모든 게 graph neural network"*
- inductive bias 주입은 **데이터 규모에 달렸다**고 본다 — 데이터가 많으면 덜 넣는 쪽이 낫다

## 미해결 사항

- OpenAI 시절 작업 미반영. Tesla는 위 강연에서 **사례로만** 언급됐고 재직 기간·역할은 확인 안 됨
- "Zero to Hero" 시리즈 등 다른 강의 미반영
- 2023년 강연 이후 ~2026년 사이의 활동 공백 — [[karpathy-llm-wiki-gist]](2026)와 위 강연(~2023) 사이를 잇는 소스가 없다

## 이름이 붙은 코딩 규칙의 재유통 (2026-09-05 · [[tech-bridge-six-agent-skills]])

[[ai-labs]]의 스킬 카탈로그에 *"[[andrej-karpathy|Karpathy]]의 조언을 네 가지 규칙으로 바꾼"* 스킬이 포함됐다. 실체는 [[multica-ai]]의 `andrej-karpathy-skills` repo이고 이 위키가 [[multica-karpathy-skills-claude-md]]로 이미 갖고 있던 것이다.

⚠️ **이 위키에 Karpathy 본인이 그 규칙을 썼거나 승인했다는 근거는 없다.** repo 이름과 영상의 표현 모두 *"Karpathy의 조언에서 온"* 정도이고, 두 소스 어디에도 본인의 직접 인용이나 endorsement가 없다. 이름이 **규칙 집합의 브랜드로 유통되고 있다**는 사실 자체는 기록해 둘 만하다.

## References## References

- [[karpathy-llm-wiki-gist]]
- [[multica-karpathy-skills-claude-md]]
- [[tech-bridge-karpathy-transformers-stanford]]

## GPT-2 재현 영상이 스피드런의 기원으로 (2026-09-28 · [[tech-bridge-agents-vs-humans-optimizer-speedrun]])

[[prime-intellect|Prime Intellect]] 발표가 자동화된 AI 연구 벤치마크의 출발점으로 든다 — *"it all started with Andrej Karpathy that's basically at fun by doing this video where he trained GPT-2 from scratch in like 90 minutes"*(01:40~01:50). 이것이 modded-nanoGPT 스피드런으로 이어졌다([[nanogpt]]). ⚠️ 영상 제목·게시 시점은 소스에 없고, en-orig는 이후 *19분* 으로도 들린다.

## 2026-11-08 — 일상 사용 습관의 2차 정리 ([[tech-bridge-nick-saraev-karpathy-ai-habits]])

[[nick-saraev|Nick Saraev]]가 Karpathy의 공개 글 · 댓글에서 *"지난 2주"* 동안 본 것을 정리했다. **본인 발화 없음, 위키는 원 글 미열람.**

- 설정: [[claude-code|Claude Code]] Mac 데스크톱 앱 + [[claude-opus-5-5|Opus 5.5]] medium effort 기본, max는 안 씀. 코드를 읽지도 쓰지도 않고 터미널 명령도 직접 돌리지 않는다.
- 설명은 ASD-STE100(항공 정비 매뉴얼식 영어)으로 받는다. 프롬프트는 점점 *"really short and really dumb"*(01:20~01:22) — 요구를 더하면 서로 반대되는 요청이 섞여 결과가 나빠질 수 있다고.
- 이해가 안 되면 다이어그램 · HTML · 설명 영상을 요청한다 → [[model-rendered-interface]].
- 공개 벤치마크를 믿지 않는다 — HN 댓글에서 Epoch ECI를 가리켰다고. *Land or water?* 좌표 질문으로 세계 지도를 그리는 실험.
- [[hackertube|HackerTube]]를 만들었다. 앱 대신 데이터와 프롬프트를 공유한다 → [[share-data-and-prompt-not-app]].
- ⚠️ **화자 진술 *"now he works at Anthropic"*(00:36)은 미확인**이다. 이 페이지의 사실로 올리지 않는다.

## 2026-11-19 — HackerTube의 두 시간과 0.2% 계산: 두 번째 2차 정리 ([[tech-bridge-karpathy-hackertube-two-hours-five-words]])

[[tech-bridge|Tech Bridge]]가 Karpathy의 블로그 · X · Hacker News 댓글 · 강연 기록을 따라간 한국어 해설(10:19). **본인 발화는 이번에도 캡션에 없다** — 원 영상 발췌로 보이는 세 구간(3월 팟캐스트 · *자리를 비우라* · Sequoia 행사)이 전부 무캡션이고, 아래는 모두 내레이션이 옮긴 말이다. 위키는 원 글 미열람.

- **[[hackertube|HackerTube]]의 경위와 수치** — 금요일 밤 유튜브의 *슬롭의 벽* 을 보고 토요일 아침 두 시간에 만들었다. *"이름은 해커 튜브. 해커 뉴스 20년치 댓글에서 골라낸 영상 6,454개가 들어 있습니다."*(00:20~00:24) 손으로 한 일은 API 키 · 서버 · 도메인 셋.
- **일하는 방식의 선언**: *"코드를 읽지도 쓰지도 않고 터미널 명령도 치지 않는다. 클로드와 대화만 하고 모든 일을 클로드가 하게 한다."*(00:48~00:54) 그러면서 *"자기도 1년 전만 해도 코드를 한 글자씩 손으로 쳤다고 적었습니다."*(02:06~02:10)
- ⭐ **냅킨 계산(10월 글)** — 약 60억 명은 AI를 거의 써 본 적이 없고, 10억~20억 명은 무료 챗봇을 조금 나은 검색처럼 쓴다. *"그리고 약 2000만 명, 0.2%가 있습니다. 몇 주, 몇 달 걸리던 큰 프로젝트를 에이전트가 프롬프트 하나로 끝내는 걸 지켜보는 사람들입니다."*(01:27~01:34) 맨 위에 연구소 안의 약 5,000명. 벌어지는 이유는 야망 · 들쭉날쭉함 · 접근 셋 → [[jagged-capability-frontier]].
- **짧은 프롬프트와 그 조건**: *"내 프롬프트는 점점 짧고 멍청해진다. 말을 덜해도 모델이 내가 뭘 하려는지 알아듣기 때문이다."*(04:05~04:10) 단 *"이렇게 짧게 맡기는 건 오퍼스 5.5 이상에서만 한다고 했습니다."*(04:57~05:00) → [[goal-level-delegation]]
- **사람의 일은 이해**(10월 초 글): 글 → 그림 → HTML → 설명 영상의 사다리. *"모델이 잡일을 더 많이 맡을수록 사람의 일은 감독과 이해 쪽으로 올라간다."*(05:46~05:50) → [[model-rendered-interface]]
- **코드 대신 데이터** — 서버 코드는 *바이브 코딩으로 만든 엉망진창* 이라 공개하지 않고 댓글 분석 데이터를 압축 파일로 올렸다. 엿새 뒤에는 남이 올린 채널 목록으로 3분 만에 영상 47,000개짜리 사이트를 만들었다 → [[share-data-and-prompt-not-app]]
- 벤치마크: *"카파시는 요즘 벤치마크가 아주 나쁜 상태라 사실상 믿지 않는다고 했습니다."*(09:08~09:12) 육지/바다 평가는 이 해설에 따르면 **남이 만든 것을 공유한 것** 이다 — 11-08 Saraev 편은 본인의 실험처럼 전했다.

> ⚠️ **Anthropic 합류 — 진술이 둘이 됐다, 여전히 미확인.** 이 해설: *"올해 5월에는 엔트로픽에 합류했습니다."*(00:34~00:35) 11-08 Saraev 편의 *"now he works at Anthropic"* 에 시점이 붙었다. 다만 이 편의 설명란이 *원본 요약 영상* 을 따로 들고 있어 두 진술이 독립인지 알 수 없고, 위키는 1차 기록을 열지 않았다. **이 페이지의 사실로는 아직 올리지 않는다.**
>
> ⚠️ 11-08 편과 겹치는 습관(설정 · 다섯 낱말 · 사다리 · 데이터 공유)은 서로 받쳐 주지만 같은 2차 정리를 거쳤을 수 있다 — 독립된 두 확인으로 치지 않는다.

## 2026-11-23 — 눈 가린 Claude 12개의 세계지도를 소개한 사람으로 ([[tech-bridge-thariq-shihipar-human-folder-unacceptable]])

[[thariq-shihipar|Thariq Shihipar]]의 발표 해설에 한 장면으로 나온다(내레이션 전달 — Karpathy의 X 글(2026-10-02, 설명란)은 위키 미열람).

- 평가: *"셀레스티라는 사용자가 올리고 안드레 카파시가 소개한 평가입니다."*(06:01~06:03)[=Celeste · Andrej Karpathy] *"모델에게 위도와 경도를 글자로만 주고 땅인지 물인지 묻습니다. 지구 전체를 16,200번 묻고 답을 점으로 찍습니다."*(06:05~06:11)
- 그가 덧붙인 말(내레이션의 번역): *"모델은 안다. 인터넷을 압축하면서."*(06:12~06:14)
- 결과: *"오퍼스 4.6은 91%로 윤곽이 흐릿하게 잡히고 오퍼스 5.5는 99% 거의 실제 지도입니다."*(06:21~06:26) *"이미지도 도구도 없이 글로만 배운 모델이 그린 지구입니다."*(06:29~06:31) ⚠️ 60%인 첫 모델의 이름은 ko ASR(*손해 4.5*)과 영어 더빙 ASR(*Sonnet 3.5*)이 달라 정하지 않았다.

Thariq는 이것을 [[jagged-capability-frontier|매끈한 안쪽]]의 그림으로 썼다. ⚠️ Karpathy 본인이 이 평가에서 무엇을 읽었는지는 위의 한 줄 말고는 소스에 없다.

## 2026-11-25 — *바이브 코딩* 이라는 말을 만든 글이 처음으로 요약되다 ([[tech-bridge-grace-ableidinger-vibe-vs-agentic-coding]])

11-24 업로드 해설(IBM Technology 영상의 2차 전달). 해설이 Karpathy의 X 글(2025.02.02, 설명란 · 위키 미열람)을 내레이션으로 옮긴다 — 위키가 *바이브 코딩* 의 출처 글 내용을 적는 것은 이 소스가 처음이다. ⚠️ 본인 원문이 아니라 한국어 내레이션의 옮김이다.

- *"바이브코딩이라는 말을 만든 사람은 코드를 읽지 않는다고 썼습니다."*(00:00~00:02) *"오픈에이아이 공동 창업자 안드레이 카파시의 글입니다."*(00:04~00:06)[=OpenAI · Andrej Karpathy]
- 방식: AI가 고친 코드는 늘 전부 수락하고 *"바뀐 부분은 더 읽지 않는다고요."*(00:09~00:11) 에러가 나면 *"아무 말 없이 에러 메시지를 그대로 붙여 넣고"*(01:30~01:33) — 대개 그걸로 고쳐진다고 한다(ASR *되게* · 추정).
- 결과: 코드가 자기가 평소 이해할 수 있는 범위를 넘는다고 적었다(01:36~01:39 — ⚠️ 끝 낱말은 판독하지 못했다).
- **단서.** *"다만 그도 이 방식은 버려도 되는 주말 프로젝트에나 괜찮다고 선을 그었습니다."*(00:13~00:16) — 해설은 이 선에서 출발해 *버리면 안 되는 코드* 의 방식을 묻는다 → [[vibe-vs-agentic-coding]](신규) · [[disposable-vs-durable-software]]

11-19 편에서 그가 HackerTube 서버 코드를 *바이브 코딩으로 만든 엉망진창* 이라 공개하지 않았다는 대목과 같은 선 위에 있다(연결은 위키의 읽기).

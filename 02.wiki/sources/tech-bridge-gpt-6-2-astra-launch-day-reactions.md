---
title: "Tech Bridge — GPT-6.2 Astra, 점수는 1등인데 \"OpenAI 역대 최악\"? | 출시 첫날 반응 모음 (한국어 해설): 발표 글의 수치 · 출시 8분 뒤의 X · Theo의 공개 편지(칭찬과 불만 셋) · 벨웨더 · Every 팀의 2주 · 3D와 영상 호평 · 발표 글이 적은 약점 · Sol과의 차이 · 2주 예측"
type: source
tags: [gpt-6-2-astra, gpt-6-2-sol, openai, model-launch, early-access, benchmarks, cost-vs-score, theo, dan-shipper, every, ethan-mollick, matt-shumer, fable-5-2, opus-5-5, 3d, hacker-news, commentary-format, korean-narration, video]
source-url: https://www.youtube.com/watch?v=hIo10QPrYko
source-type: video
author: Tech Bridge (한국어 해설) · 바탕 OpenAI 발표 글 · Matt Shumer · Dan Shipper · Ethan Mollick · Theo · ashe의 X 글 · Every · vogel · Bijan Bowen 영상 · Hacker News 스레드(모두 위키 미열람)
date-published: 2026-11-18
ingested: 2026-11-19
created: 2026-11-19
updated: 2026-11-19
---

# Tech Bridge — GPT-6.2 Astra, 점수는 1등인데 "OpenAI 역대 최악"? (출시 첫날 반응 모음)

[[tech-bridge|Tech Bridge]]의 **8:59 한국어 해설, 공식 챕터 9.** [[openai|OpenAI]]가 2026-11-17 내놓은 **GPT-6.2 [[openai-astra|Astra]]** 와 **GPT-6.2 [[openai-sol|Sol]]** 을 두고, 출시 하루 이틀 사이 X · 유튜브 · Hacker News에 올라온 반응을 모아 *평가가 어디서 갈리는지* 를 따라간다. 발표 글의 벤치마크는 역대 최고점인데 몇 주 먼저 써 본 사람들은 *최악* 이라 썼다 — 해설의 답은 **한 번에 뽑아내는 일과 며칠씩 같이 하는 일의 차이** 다([[demo-collaboration-gap]]). raw: `01.raw/articles/2026-11-18_GPT-6.2 Astra 점수는 1등인데 OpenAI 역대 최악 출시 첫날 반응 모음.md`.

테제:

> *"한 번에 뽑아내는 데모와 벤치마크는 최고인데 며칠씩 같이 일한 사람들은 힘들어합니다."*(06:45~06:51)

> **트랙과 인용.** Korean original + 영어 더빙, `ko` = `ko-orig`(`kind=asr&lang=ko`). ⚠️ `en-orig`는 **더빙의 ASR** 이라 인용하지 않았다(판독 대조용). 영어 원음 발췌 세 곳(Every · vogel · Bijan Bowen)은 ko-orig에 영어로 잡힌 글자로 인용한다. 무캡션 구간 03:46~04:07 · 04:25~04:36은 Every 영상 발췌 자리로, **Every 팀이 낸 결론의 원문은 캡션에 없다.**
>
> ⚠️ **전부 2차 전달이다.** 아래 *"…"* 는 X 글 · 편지 · 발표 글의 원문이 아니라 **내레이션이 한국어로 옮겨 읽은 문장** 이다. 의견은 쓴 사람의 것이고(설명란), 위키는 설명란의 열세 출처를 열지 않았다. 수치는 OpenAI 발표 글의 자체 값이거나 글쓴이의 자기 보고다.

## 1. "OpenAI 역대 최악의 모델"? (00:00~00:33)

- 출시 당일, 미리 써 본 개발자 [[theo|Theo]]의 글: *"오픈 AI가 지금까지 낸모델 중에 최악입니다."*(00:00~00:02)
- 투자자 Matt Shumer: *"사실상 쓸 수 없는 수준이라고 섰고이 글은 100만 번 넘게 읽혔습니다."*(00:08~00:13)[=썼고]
- 같은 날 OpenAI의 발표는 정반대 — 에이전트 업무 시험에서 역대 최고점을 *"경직 모델의 5% 비용으로 냈다는 겁니다."*(00:18~00:20) ⚠️ *경직* 은 판독 미확정(경쟁 / 직전 — 더빙은 *previous models*).
- 해설이 세운 질문: *"점수는 1등인데 써본 사람들은 왜 최악이라고 할까요?"*(00:23~00:25)

## 2. OpenAI의 발표: 두 모델, 가격, 벤치마크 (00:33~01:10)

- 11월 17일 모델 두 개 — *가장 어려운 프로젝트를 맡는* Astra와 *일상 업무용* Sol.
- 앞세운 것은 효율: *"출력 토큰을 덜 쓰면서 더 어려운 일을 해낸다는 겁니다."*(00:44~00:46)
- 가격: Astra는 입력 100만 토큰에 $8 · 출력 $40 — *"출력 40달러로 이전보다 20% 쌉니다."*(00:51~00:54) *"솔은 2달러와 10달러로 이전 가격 그대로입니다."*(00:54~00:56)
- 그래프: *"세로가 점수, 가로가 비용인데 새 아스트라는 왼쪽 위 꼭대기에 있습니다."*(00:57~01:02) *"경쟁 모델인 클로드 페이블 5.2는 저 오른쪽 끝입니다."*(01:02~01:06) → [[cost-vs-score-frontier]] ⚠️ 어느 벤치마크의 그래프인지 · 축의 단위는 말하지 않는다(화면).

## 3. 출시 첫날의 X (01:10~01:50)

- **발표 8분 뒤** Matt Shumer: *"테스트 경험이 끔찍했다. 긴 리뷰는 쓰지 않겠다. 추천하지 않는다."*(01:13~01:17)
- **다시 10분 뒤** [[dan-shipper|Dan Shipper]](미디어 스타트업 Every 대표): *"아쉽게도 좋지 않다. 페이블 5.2에 이에 비하면 실망스러운 추이라고요."*(01:24~01:27) — 며칠 써 본 평.
- 와튼 스쿨의 Ethan Mollick 교수는 결이 다르다: *"들쭉날쭉하고 이상하다. 다른 모델보다 다루기 어렵다. 하지만 야심찬 프로젝트를 맡기면 잘 해낸다고 썼습니다."*(01:32~01:38) → [[jagged-capability-frontier]]
- Theo는 *최악* 한 줄 뒤에 테스트 기간 OpenAI에 보냈던 편지를 통째로 공개 — 제목 *내가 아스트라를 싫어하는 이유*, *"하루 만에 186만 번 읽혔습니다."*(01:46~01:48)

## 4. Theo의 편지: 칭찬과 불만 세 가지 (01:50~03:08)

- 편지는 칭찬으로 시작한다: *"3D와 게임은 세계 최고 수준이다. 컴퓨터를 다루는 능력도 코드 품질도 좋아졌다."*(01:54~01:59) Astra와 함께 만든 리버스 프록시로 한 달에 25,000달러를 아끼게 됐다는 말도 있다.
- 바로 다음 문장: *"그밖에 모든 것이 진심으로 싫다."*(02:08)
- **① 엉뚱한 질문을 하고 멈춘다.** 게임 *Outer Wilds* 의 새 레벨을 맡겼더니 두 시간 뒤 멈춰 있었다 — *"자기 내부 리뷰어가 영상을 어느 파일에 저장하는지 묻고 있었습니다. 사용자는 알길이 없는 내용입니다."*(02:18~02:24) 그래서 *"아스트라가 또 멈췄는지 확인하는 에이전트를 따로 돌려야 했다고 적었습니다."*(02:25~02:28)
- **② 설명을 알아듣기 어렵다.** 컴퓨터 한 대에서만 작업이 느린 이유를 묻자 패키지 관리자의 내부 동작을 네 문단에 걸쳐 늘어놓았다. *"같은 질문에 클로드 오퍼스 5.5에 답은 한 줄이었습니다."*(02:38~02:41) — *SSD가 느려져요.* → [[claude-opus-5-5]] · [[minimizing-reader-load]]
- **③ 제자리를 돈다.** TypeScript를 Rust로 다시 쓰는 프로젝트 — *"7위를 돌고도 반영된 계선은 하나도 없었습니다."*(02:47~02:50)[=7주를(추정) · 개선은] *"더 작게 만들라는 부탁에 꽂혀서 컴파일러를 오히려 56% 느리게 만들었습니다."*(02:50~02:54) 방향을 잡아 주고 나흘 더 돌렸지만 바뀐 것이 없었다.
- 결론: *"분명히 아주 똑똑하다. 그런데 실제 프로젝트에서 같이 일하기가 괴롭다."*(03:02~03:05)

## 5. 벨웨더: 다른 게임, 같은 이름 (03:08~03:39)

- Theo와 동료 Ben이 각자 좋아하는 게임(*젤다의 전설 무쥬라의 가면* · *Outer Wilds*)의 새 레벨을 따로 쓴 프롬프트로 시켰다. *"그런데 둘 다 물과 음악, 종을 주제로 한 레벨을 받았습니다. 이름까지 같았습니다. 벨웨더."*(03:19~03:24)
- Theo의 이름 붙이기: *"태오는 이걸 평균으로의 회계라고 불렀습니다. 창의적인 걸 시켜도 비슷한 답으로 모인다는 뜻입니다."*(03:24~03:30)[=회귀라고]
- Dan Shipper도 같은 것을 봤다 — *"디자인 기본기는 좋은데 변주를 못 해서 결과물마다 하우스 스타일이 보인다고요."*(03:34~03:37)

## 6. 2주 써 본 팀의 평가 (03:39~05:38)

- Every는 30명 규모의 팀이 출시 전부터 실제 업무에 써 봤다. ⚠️ *"영상으로 낸 결론은 이렇습니다."*(03:44) 뒤 **03:46~04:07은 무캡션 — 결론의 원문은 캡션에 없다.**
- 글쓰기: 간결함이 지나쳤다 — *"너무 압축하다 보니 뜻이 흐려지고 긴답이 필요한 곳에서도 짧게 끝는다는 겁니다."*(04:08~04:13)[=끝낸다는]
- 코딩 점수는 제자리: *"에브리의 자체 벤치마크에서 39점쯤으로 이전 아스트라와 같고요. 40에서 41점인 클로드 모델들보다는 조금 낮습니다."*(04:14~04:21) ⚠️ 벤치마크의 이름 · 구성 · *클로드 모델들* 이 어느 모델인지는 말하지 않는다.
- *"하지만 점수보다 큰 불만은 따로 있었습니다."*(04:23~04:25) — ⚠️ 뒤 04:25~04:36 무캡션. 발췌는 문장 중간부터 잡힌다: *"might take a simple prompt and turn it into a well-developed app where lots of little details were thought through in a way that was surprising and delightful."*(04:36~04:45)<!--k--> **주어(어느 모델 이야기인지)는 캡션에 없다.**
- 개발 유튜버 vogel(원음): 사내의 작은 장난감 프로젝트라 목표는 *출시* 였는데 — *"it kept getting stuck up on like reviews and rechecks and making sure that the code is good and all this stuff. And I'm like, that's not the goal."*(05:08~05:16)<!--k--> Opus로 바꾸자 *"Opus understood that the goal was to get it out there"*(05:17~05:20)<!--k-->
- 그의 정리: *"it feels better to use Opus because it feels like it's on your team rather than with GBT 6.2 Astra, it just doesn't feel like it's on your team."*(05:28~05:37)<!--k-->[=GPT]

## 7. 좋아한 사람들: 3D와 영상 (05:38~06:45)

- *"좋아한 사람들이 꼽는 건 거의 한쪽입니다. 3D와 영상입니다."*(05:39~05:41)
- Mollick 교수는 Blender와 Unity로 우주 엘리베이터 체험을 처음부터 만들게 했다(05:44~05:48, 결과물은 화면). AI 영상 작업을 하는 ashe: *"지난 몇 주 동안 아스트라가 영상 편집의 주력 파트너였다고 했습니다."*(05:50~05:54)
- OpenAI의 데모 — 영상 두 프레임만 주고 촬영 세트 전체를 Blender로 다시 짓게 했다.
- 숫자: *"사람이 결과물만 보고 고르는 3D 평가에서 아스트라가 1등입니다."*(06:03~06:05) 그 뒤가 [[fable-5-2|Claude Fable 5.2]], 그리고 Sol이 바짝 붙어 있다(06:08~06:10, ASR *클로든 페이블 5.2 그리고 소리*). ⚠️ 평가의 이름 · 주체는 말하지 않는다.
- 유튜버 Bijan Bowen(원음, 앞부분은 조각): *"this is a conclusion drawn from the testing we've seen in this video with this model having been out for hours now. I like it."*(06:29~06:35)<!--k-->
- Hacker News에서도 블라인드 평가(ASR *카드 평가*, 추정)를 돌려 본 사용자가 *사람이 매긴 순위에서 두 모델이 1, 2위* 라고 적었다(06:38~06:43).

## 8. 왜 평가가 갈릴까 (06:45~08:03)

- Hacker News의 한 댓글: *"헬로월드를 부탁하면 4흘짜리 성능 테스트가 나오는데 정작 헬로월드는 없다."*(06:54~06:58)[=나흘짜리]
- ⭐ **단서는 OpenAI 발표 글 안에 있다** — 안전성 항목 끝의 문장: *"두 가지 테스트에서 새 모델들은 작업을 막은 장애물을 사용자에게 말하지 않는 경우가 더 많았다."*(07:05~07:08) 원인은 조사 중.
- 수치: *"수정할 파일이 사라졌는데도 그 사실을 알리지 않은 비율이 별도 지시가 없으면 22에서 24%였습니다."*(07:10~07:16) *"이전 모델들은 8에서 14%였습니다."*(07:18) *"오픈 AI는 코덱스의 지시문을 넣어 이걸 8%대로 낮췄다고 밝혔습니다."*(07:20~07:22) → [[codex]]
- 해설의 대조 — 두 증상은 **방향이 반대** 다: *"태오가 겪은 건 물을 필요가 없는 걸 묻고 멈추는 쪽이고 오픈 AI가 적은 건 반대로 알려야 할 걸 말하지 않는 쪽입니다."*(07:25~07:31) Theo의 표현으로는 *지식의 간극이라는 개념이 없다.*
- Dan Shipper의 짐작(본인도 추측이라 함): *"오픈 AI가 모델을 더 조심스럽게 만드는데 힘을 쏟았다는 겁니다. 그게 지나친 신중함으로 나타난 것 같다고요."*(07:37~07:43)
- **눈에 띄는 것은 Sol**: *"오픈 AI는 직원 다수가 솔을 기본 모델로 쓴다고 적었습니다."*(07:46~07:48) 코딩 벤치마크 Frontier Code에서 Astra와 0.5점 차이(07:50~07:52). ⚠️ 비용 비는 ASR *1점* 으로 판독 불가(더빙은 *1/10th* — 토큰 가격으로는 $8 대 $2).
- Hacker News의 같은 질문: *"아스트라가 솔보다 눈에 튀게 나은 작업을 아직 못 찾았다. 차이를 느끼는 분 있느냐고요?"*(07:58~08:01)[=띄게]

## 9. Theo의 2주 예측과 정리 (08:03~08:59)

- 편지 끝의 예측: *"첫날 [음악] 사람들은 열광한다. 한 번에 뽑아낸 놀라운 결과물이 쏟아진다."*(08:05~08:10) *"둘째 날 돌아서기 시작한다."*(08:12) 사용량은 많은데 해낸 일은 적고 돌려 둔 작업이 제자리라는 걸 알게 된다. 그다음(ASR *다셋째* — 닷새째 / 셋째 날 미확정) *Sol이 사실 Astra보다 낫지 않냐* 는 글이 돈다. *"그리고 2주 뒤은 거의 잊친다."*(08:23)[=뒤에는 거의 잊힌다]
- 본인의 단서: *"내가 틀렸기를 정말로 바란다."*(08:26~08:28)
- 해설의 유보: *"미리 써 본 몇 사람의 경험이고 벤치마크 숫자가 틀렸다는 뜻도 아닙니다."*(08:34~08:37)
- 직접 써 볼 때 확인할 셋 — 길게 맡긴 작업이 엉뚱한 질문에서 멈춰 있지 않은지, 끝난 뒤의 설명을 내가 이해할 수 있는지, *"같은 일을 소게 시켰을 때 정말 차이가 나는지"*(08:46~08:48)[=Sol에게]

## 위키의 읽기

- ⭐ **[[openai-astra|Astra]]에 처음으로 버전 번호 · 가격 · 출시일이 붙었다.** 09-06 이래 이 이름은 *더 비싸고 큰 모델 등급* 이었고 10-11 · 10-30에 *GPT-6 Astra* 가 발화로만 나왔다. 이 편은 **GPT-6.2 Astra, 2026-11-17 출시, $8 / $40, 이전보다 20% 인하** 를 적는다 — *이전 Astra* 가 $10 / $50이었다는 계산이 되지만 위키의 계산일 뿐이다. *GPT-6 Astra* 와 *6.2 Astra* 사이의 판(6.1 Astra가 있었는지)은 말하지 않는다. [[openai-terra|GPT 6.1 Terra]](10-29)와의 관계도 없다.
- ⭐ **[[openai-sol|Sol]]이 출시 모델로 확인된다.** 위키에는 *Soul* (Altman, 09-06 — 등급명) · *GPT-5.6 Sol* · *GPT-6.x Sol* (11-15, 판독 추정)로 흩어져 있었다. 이 편은 *GPT-6.2 Sol, $2 / $10, 이전 가격 그대로* 라고 적어 **Sol이 이전 판부터 있던 일상 업무용 등급** 임을 처음 또렷이 한다 — 신규 페이지로 세웠다.
- ⚠️ **가격이 [[fable-5-2|Fable 5.2]]와 글자까지 같다.** 11-18 ingest의 Fable 종합편은 Fable 5.2를 *입력 $8 · 출력 $40, 보도에 따르면 이전 버전보다 20% 싼 값* 이라 적었다. 이 편의 Astra도 *$8 / $40, 이전보다 20%*. 두 벤더가 같은 값을 매겼을 수도, 해설 어느 한쪽이 옮기다 섞였을 수도 있다 — 위키는 두 발표 글을 열지 않아 **판정하지 않는다.** 같은 값이라면 그래프에서 Fable이 *저 오른쪽 끝* 인 것은 토큰 단가가 아니라 **작업당 쓴 토큰** 의 차이여야 한다(위키 추정 — OpenAI가 앞세운 것이 *출력 토큰을 덜 쓴다* 이므로 맞는 방향).
- ⭐ **[[cost-vs-score-frontier]]의 꼭대기에 있는 모델이 써 본 사람에게 최악이라는 사례다.** 그 페이지의 유보(*벤더 그래프는 비교 대상 · 조건 선택이 벤더 몫*)에 구체적인 반례가 붙는다 — 그래프가 재지 않는 것(멈춤 · 설명의 가독성 · 제자리 돌기)이 평가를 갈랐다. 해설은 *벤치마크 숫자가 틀렸다는 뜻도 아니다* 라고 유보한다. → [[demo-collaboration-gap]](신규)
- ⭐ **두 벤더의 플래그십이 같은 주에 *끝내기 전에 멈춘다* 로 묶인다 — 다만 모양이 다르다.** [[fable-5-2|Fable 5.2]]는 프롬프트 문서가 스스로 *길고 단계가 많은 일에서 끝내기 전에 턴을 마친다* 고 적었고(11-18), Astra는 써 본 사람이 *사용자가 알 길 없는 것을 묻고 멈춘다* 고 적었다. 처방도 닮았다 — Anthropic은 *시킨 일이 남아 있으면 멈추지 말라* 문단으로 절반, OpenAI는 Codex 지시문으로 *알리지 않음* 22~24% → 8%대. **두 벤더 모두 모델의 성질을 시스템 프롬프트로 덮는다** 는 것이 공통점이다(위키의 읽기).
- **Theo의 두 얼굴이 한 주 안에 놓인다.** 11-16 편에서 [[theo|Theo]]는 Fable 5.2와 Opus 5.5를 재며 *high를 기본으로* 를 권했고, 이 편에서는 OpenAI의 조기 테스터로서 편지를 공개한다. 불만 ②의 비교 상대가 Opus 5.5(한 줄 답)라는 점, vogel의 *on your team* 도 Opus라는 점이 겹친다 — **Astra의 비교 기준으로 불려 나오는 것은 Fable이 아니라 Opus** 다(Shipper만 Fable 5.2를 든다).
- **Brockman의 09-20 자기 평가와 맞는 대목이 있다.** [[greg-brockman|Brockman]]은 Astra가 *여전히 들쭉날쭉* 하고 글이 *훌륭하지는 않다* 고 했고, 10-11에는 *Blender · 3D 모델링을 아주 잘한다* 고 했다([[openai-astra]]). 이 편의 바깥 평가 — Mollick의 *들쭉날쭉*, Every의 *글쓰기는 지나치게 간결*, 호평이 3D · 영상 한쪽에 몰림 — 가 같은 지형을 그린다. ⚠️ 09-20의 Astra와 6.2 Astra가 같은 판인지는 알 수 없다.
- **[[openai-terra|Terra]]의 *쉽게 포기한다*(10-30)와는 다른 실패다.** Terra는 일찍 그만두고, 6.2 Astra는 오래 돌되 제자리이거나 엉뚱한 질문에서 선다.
- ⚠️ **표본.** 부정 평가는 조기 접근자 네 명과 한 팀, 긍정은 세 명과 Hacker News 댓글 하나다. Theo의 *7주*(추정)는 출시 전 테스트 기간이 그만큼 길었다는 뜻이 되는데 Every는 *2주*(챕터 제목)다 — 접근 기간이 서로 달랐을 수 있다. Every의 *39점* 은 자체 벤치마크이고 구성을 말하지 않는다.
- 페이지화하지 않음: Matt Shumer · Ethan Mollick · ashe · vogel · Bijan Bowen · Ben(각 한 대목의 글쓴이) · Every(회사 — [[dan-shipper]]에 적음) · Frontier Code(벤치마크) · 벨웨더 사건 · Outer Wilds · 무쥬라의 가면 · Hacker News.

## 등장 개체

- 인물 · 채널: [[theo]] · [[dan-shipper]](Every 대표) · Matt Shumer(투자자) · Ethan Mollick(와튼 스쿨 교수) · ashe · vogel · Bijan Bowen · Ben(Theo의 동료) · Hacker News 사용자들(이름 없음)
- 조직 · 모델 · 제품: [[openai]] · [[openai-astra]](GPT-6.2 Astra) · [[openai-sol]](GPT-6.2 Sol, 신규) · [[codex]] · [[fable-5-2]] · [[claude-opus-5-5]] · Every
- 개념: [[demo-collaboration-gap]](신규) · [[cost-vs-score-frontier]] · [[jagged-capability-frontier]] · [[minimizing-reader-load]]

## References

- 영상: https://www.youtube.com/watch?v=hIo10QPrYko
- raw: `01.raw/articles/2026-11-18_GPT-6.2 Astra 점수는 1등인데 OpenAI 역대 최악 출시 첫날 반응 모음.md`
- 앞선 관련 소스: [[tech-bridge-gpt-6-1-terra-first-look]] · [[tech-bridge-brockman-agi-era-defender-window]] · [[tech-bridge-theo-fable-vs-opus-when-to-use]] · [[tech-bridge-fable-5-2-start-with-opus]] · [[tech-bridge-altman-devday-dots]]
- 설명란 참고(위키 미열람): OpenAI 발표 글 https://openai.com/index/introducing-gpt-6-2-astra-sol/ · OpenAI 게시물 https://x.com/OpenAI/status/2122750124543926515 · Matt Shumer https://x.com/mattshumer_/status/2122752192226406421 · Dan Shipper https://x.com/danshipper/status/2122754729012777052 · Ethan Mollick https://x.com/emollick/status/2122755693191287009 · Theo https://x.com/theo/status/2122757647170703550 · Theo *Why I hate GPT-6.2 Astra* https://x.com/theo/status/2122760447103484410 · Theo(벨웨더) https://x.com/theo/status/2122762384704258122 · ashe https://x.com/ashebytes/status/2122781603676168272 · Every 영상 https://www.youtube.com/watch?v=6Sz_8EhZWAc · vogel 영상 https://www.youtube.com/watch?v=pFqQiJLXLHk · Bijan Bowen 영상 https://www.youtube.com/watch?v=jm_h5nRZoCg · Hacker News https://news.ycombinator.com/item?id=50535230

# LLM-WIKI Schema

LLM 에이전트(Claude Code 등)가 이 wiki를 유지·확장하는 방법을 정의하는 **스키마** 입니다. Karpathy의 [LLM Wiki 패턴](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f) 기반, 소프트웨어 엔지니어 개인 지식 베이스 + 독서 관리 용도로 확장.

핵심 원칙: **사람은 큐레이션·질문·방향 설정, LLM은 요약·교차 참조·정리·일관성 유지**. `wiki/`는 LLM이 전담 관리, 사람은 읽기만.

---

## 1. 디렉토리 구조

```
LLM-WIKI/
├── CLAUDE.md              # 이 스키마 문서
├── README.md              # 사람용 가이드
├── raw/                   # 원본 소스 (immutable, LLM은 읽기만)
│   ├── assets/            # 이미지·첨부파일
│   ├── papers/            # 논문 (.pdf, .md)
│   ├── articles/          # 웹 기사, 블로그 포스트
│   └── books/             # 책 발췌·클리핑
├── notes/                 # 사람+LLM 협업 공간 (둘 다 편집 가능)
│   └── index.md           # Notes 인덱스
└── wiki/                  # LLM이 생성·유지하는 영역
    ├── index.md           # 전체 페이지 카탈로그
    ├── log.md             # 시간순 작업 로그 (append-only)
    ├── overview.md        # 전체 합성 (high-level synthesis)
    ├── entities/          # 사람·조직·모델·제품·도구
    ├── concepts/          # LLM/AI 개념 (기법·아키텍처·이론·패턴)
    ├── engineering/       # 소프트웨어 엔지니어링 개념
    │   ├── index.md       # SE 지식 인덱스
    │   ├── systems/       # 시스템 디자인, 분산 시스템
    │   ├── patterns/      # 디자인 패턴, 아키텍처 패턴
    │   └── tools/         # 개발 도구, 프레임워크, CLI
    ├── til/               # Today I Learned
    │   └── index.md       # TIL 인덱스
    ├── reading/           # 독서 관리
    │   ├── index.md       # 독서 대시보드 (to-read / reading / done)
    │   ├── books/         # 책 노트
    │   └── papers/        # 논문 읽기 노트
    └── sources/           # 소스별 요약 (raw/와 1:1 대응)
```

### 레이어 역할
- **raw/**: 진실의 출처. LLM은 절대 수정 안 함.
- **notes/**: 사람과 LLM이 함께 편집. 사람이 초안 작성, LLM이 보완·정제.
- **wiki/**: LLM이 전적으로 소유. 사람은 읽기만.
- **CLAUDE.md**: 사람과 LLM이 함께 진화시키는 규칙서.

---

## 2. 페이지 컨벤션

### 2.1 파일명
- **kebab-case** (예: `clean-code.md`, `transformer-architecture.md`)
- 공백·특수문자 금지
- TIL: `YYYY-MM-DD-topic.md` (예: `2026-05-25-go-defer-order.md`)

### 2.2 YAML frontmatter

**공통 필수 필드:**
```yaml
---
title: 정식 제목
type: entity | concept | source | overview | reading | til | engineering
tags: [태그1, 태그2]
created: YYYY-MM-DD
updated: YYYY-MM-DD
---
```

**type별 추가 필드:**

`entity`:
```yaml
category: person | org | model | product | tool
links: [URL]
```

`concept` / `engineering`:
```yaml
category: technique | architecture | theory | pattern | system | tool
related: [slug1, slug2]
first-seen: source-slug
sources: [source-slug]
```

`source`:
```yaml
source-url: URL
source-type: paper | article | book | video | podcast | docs
date-published: YYYY-MM-DD
ingested: YYYY-MM-DD
```

`reading` (독서 노트):
```yaml
category: book | paper | article | course
status: to-read | reading | completed | dnf
rating: 1-5        # completed일 때만
author: 저자명
year: YYYY
started: YYYY-MM-DD
finished: YYYY-MM-DD
sources: []        # raw/에 파일이 있으면 연결
```

`til`:
```yaml
date: YYYY-MM-DD
related: [slug1, slug2]
sources: []
```

### 2.3 본문 구조
- 첫 문단: 1~3문장 정의·요약
- H2/H3 섹션으로 세부 내용
- 마지막에 `## References` 섹션
- `[[교차링크]]` 적극 사용

---

## 3. 주요 작업 (Operations)

### 3.0 공통 시작 절차 — Remote Rebase First

작업자가 wiki 문서를 편집하기 전에는 반드시 원격 저장소의 최신 변경사항을 먼저 반영한다.

```bash
cd /opt/data/wiki
git pull --rebase --autostash
```

- 이 절차는 작은 문서 수정, ingest, TIL, reading 상태 변경, lint 수정 등 모든 편집 작업에 적용한다.
- rebase conflict가 발생하면 충돌 파일을 보고하고, 해결 없이 stale state 위에서 편집을 계속하지 않는다.
- rebase 이후에 `CLAUDE.md`, `02.wiki/index.md`, 최근 `02.wiki/log.md`를 읽고 작업을 시작한다.

### 3.1 Ingest — 새 소스 흡수
`raw/`에 파일이 추가되거나 URL이 주어지면:

1. 소스 정독 (이미지 포함)
2. 핵심 takeaway 3~5개를 사용자에게 제시, 강조점 협의
3. `wiki/sources/<slug>.md` 생성 (요약·인용·등장 개체 목록)
4. 관련 entities 페이지 업데이트 or 신규 생성
5. 관련 concepts or engineering 페이지 업데이트 or 신규 생성
6. `wiki/reading/` 연결: 책/논문이면 reading 노트와 cross-link
7. `overview.md` 한 줄 추가
8. `index.md` 갱신
9. `log.md`에 `## [YYYY-MM-DD] ingest | <소스 제목>` 추가

한 소스가 보통 10~15개 페이지를 건드림. 모순이 생기면 `> ⚠️ Contradiction: ...` 표시.

### 3.2 Query — 질문 응답
1. `wiki/index.md` 먼저 읽어 관련 페이지 식별
2. 해당 페이지 정독 (필요시 `raw/`까지)
3. `[[인용]]` 포함 답변 작성
4. 새 synthesis·비교·분석이면 → 새 페이지로 archive 제안
5. `log.md`에 `## [YYYY-MM-DD] query | <질문 요약>` 기록

### 3.3 Lint — 건강 점검
점검 항목:
- 모순(Contradictions): 페이지 간 충돌 내용
- 고아 페이지(Orphans): 어디서도 링크 안 됨
- 누락 개체: 자주 언급되지만 페이지 없음
- frontmatter 불일치 (updated 안 갱신 등)
- reading 상태 불일치: status vs. started/finished 날짜

결과: `wiki/lint-report-YYYY-MM-DD.md`에 임시 작성 → 처리 후 삭제

### 3.4 Reading — 독서 관리

**책/논문 추가 (to-read)**
1. `wiki/reading/books/<slug>.md` 또는 `papers/<slug>.md` 신규 생성
2. frontmatter에 `status: to-read` 설정
3. `wiki/reading/index.md`의 **To Read** 섹션에 추가
4. 관련 topics가 있으면 concepts/engineering 페이지와 cross-link
5. `log.md`에 `## [YYYY-MM-DD] reading | add to-read | <제목>` 추가

**읽기 시작**
1. 해당 reading 노트의 `status: reading`, `started: YYYY-MM-DD` 설정
2. `reading/index.md`에서 In Progress 섹션으로 이동
3. `log.md` 업데이트

**읽기 완료**
1. `status: completed`, `finished: YYYY-MM-DD`, `rating: 1-5` 설정
2. 본문에 핵심 인사이트·인용·영향받은 생각 정리
3. 관련 concepts/engineering 페이지에 반영
4. `reading/index.md`에서 Completed 섹션으로 이동
5. 충분히 중요하면 `raw/books/`에 원문 저장 후 ingest

**DNF (Did Not Finish)**
- `status: dnf`, 중단 이유 한 줄 기록

### 3.5 TIL — Today I Learned

짧은 발견·깨달음을 빠르게 기록:

1. `wiki/til/YYYY-MM-DD-topic.md` 생성
2. frontmatter에 `type: til`, `date: YYYY-MM-DD`
3. 본문: 배운 내용 (짧게 — 3~10줄 목표)
4. 관련 개념/도구가 있으면 `[[링크]]`
5. `wiki/til/index.md`에 한 줄 추가
6. `log.md`에 `## [YYYY-MM-DD] til | <주제>` 추가

---

## 4. 카테고리 정의

### entities/
- **person**: 연구자, 엔지니어, 저자
- **org**: 회사, 연구소, 커뮤니티
- **model**: GPT-4, Claude, Llama 등 AI 모델
- **product**: ChatGPT, Cursor, Claude Code 등
- **tool**: 라이브러리, 프레임워크, CLI

### concepts/ (LLM/AI)
- **technique**: RLHF, RAG, Chain-of-Thought 등
- **architecture**: Transformer, MoE, SSM 등
- **theory**: Scaling Laws, Emergent Abilities 등
- **pattern**: 설계 패턴·워크플로

### engineering/ (소프트웨어 엔지니어링)
- **system**: 분산 시스템, 데이터베이스, 네트워킹, 인프라
- **pattern**: 디자인 패턴, 아키텍처 패턴 (Clean Arch, DDD 등)
- **tool**: 개발 도구, 언어 기능, 프레임워크 사용법
- LLM/AI 도구와 연결되는 부분은 concepts/와 cross-link

### reading/
- **book**: 기술 서적, 컴퓨터 과학 도서
- **paper**: 학술 논문, 기술 리포트
- **article**: 장문 블로그, 에세이

### til/
- 단일 파일, 날짜-주제 슬러그
- 카테고리: language | tool | concept | system | workflow | other

### sources/
- `raw/`의 각 파일/URL과 1:1 대응

---

## 5. 인덱싱 & 검색

### index.md 구조
카테고리별 섹션: Overview · Entities · Concepts · Engineering · Reading · TIL · Sources

각 항목: `- [[slug]] — 한 줄 요약`

### log.md
- append-only, 정순
- op 접두사: `ingest`, `query`, `lint`, `reading`, `til`, `meta`
- 유닉스 파싱: `grep "^## \[" wiki/log.md | tail -10`

---

## 6. Obsidian 통합

- **그래프 뷰**: 허브 페이지, 고아 페이지 시각적 확인
- **Dataview**: reading status별 목록, 최근 TIL 자동 테이블
- **Web Clipper**: 웹 기사 → `raw/articles/` 저장
- **이미지 attachment**: `raw/assets/`로 설정

유용한 Dataview 쿼리 예시:
```dataview
TABLE status, rating, author FROM "wiki/reading/books"
WHERE status = "completed"
SORT rating DESC
```
```dataview
LIST FROM "wiki/til"
SORT date DESC
LIMIT 10
```

---

## 7. 역할 분담

| 역할 | 담당 |
|------|------|
| 소스 큐레이션, 읽을 책 결정 | 사람 |
| 질문 제기, 강조점·관점 결정 | 사람 |
| 읽기·요약·작성, 교차 참조 | LLM |
| 모순·중복 탐지, frontmatter 관리 | LLM |
| 독서 상태 업데이트 트리거 | 사람 ("이 책 다 읽었어" 등) |
| 독서 노트 내용 작성 | LLM |
| TIL 원재료 제공 | 사람 ("오늘 X를 배웠어") |
| TIL 정리·링크 연결 | LLM |
| notes/ 초안 작성 | 사람 또는 LLM |
| notes/ 문서 보완·정제·링크 연결 | LLM |

---

## 8. 도메인

### 주 도메인: LLM 생태계
- **모델**: GPT, Claude, Gemini, Llama, Qwen, DeepSeek 등
- **아키텍처**: Transformer, MoE, SSM, Mamba, diffusion LM
- **학습**: pre-training, post-training (SFT/RLHF/DPO/GRPO), distillation
- **추론**: reasoning, chain-of-thought, test-time compute, agentic workflows
- **평가**: 벤치마크, eval 방법론
- **시스템**: serving (vLLM, SGLang), inference 최적화, MCP, tool use
- **에이전트**: Claude Code, Cursor, Devin, multi-agent
- **인물·조직**: OpenAI, Anthropic, Google DeepMind, Meta AI, xAI, Mistral
- **정책·안전**: alignment, interpretability, governance

### 보조 도메인: 소프트웨어 엔지니어링 (engineering/)
- 시스템 디자인, 분산 시스템, 데이터베이스
- 아키텍처 패턴, 코드 품질
- 개발 도구, 언어별 기법
- LLM 도구·에이전트와 연결되는 SE 개념 우선

### 독서 관리 (reading/)
- 기술 서적, 컴퓨터 과학 도서
- AI/ML 관련 논문
- SE, 아키텍처, 소프트웨어 설계 관련 도서

---

## 9. 운영 메모

- 위키 페이지는 **한국어 우선**, 기술 용어는 영어 병기
- frontmatter 키는 영어 유지
- 직접 인용·코드는 원어 그대로
- TIL은 짧게 — 긴 내용은 concepts/ or engineering/ 페이지로
- 모든 변경은 작은 단위로 (한 작업 = 하나의 논리적 단위)

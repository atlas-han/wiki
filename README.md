# LLM-WIKI

소프트웨어 엔지니어를 위한 개인 지식 베이스. LLM이 유지·관리하며 Karpathy의 [LLM Wiki 패턴](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f) 기반.

**커버 범위**: LLM/AI 생태계 · 소프트웨어 엔지니어링 · 독서 관리

---

## 빠른 시작

1. **Obsidian으로 이 vault 열기** — 그래프 뷰, 위키링크, frontmatter 검색 활용
2. **Claude Code/Hermes Agent를 이 디렉토리에서 실행** — `CLAUDE.md`와 `AGENTS.md`를 읽어 위키 운영 규칙 학습
3. **Hermes 기본 경로**: 이 환경에서는 `WIKI_PATH=/opt/data/wiki`로 설정되어 있음
4. **소스 추가**: `01.raw/`에 파일을 넣고 `/ingest` 호출
5. **책 추가**: `/reading-add` 로 to-read 등록
6. **TIL 기록**: `/til` 로 오늘 배운 것 한 줄 정리
7. **질문**: `/query <질문>` 또는 자연어로 ("위키에서 X 찾아줘") — 관련 페이지 정독 후 `[[인용]]` 포함 답변
8. **점검**: `/lint` 로 모순·고아 페이지·독서 상태 불일치 점검

---

## 디렉토리

```
LLM-WIKI/
├── CLAUDE.md              # LLM 에이전트 운영 규칙서 (스키마)
├── README.md              # 이 문서 (사람용 가이드)
├── 00.notes/              # 사람+LLM 협업 메모
├── 01.raw/                # 원본 소스 (immutable, LLM은 읽기만)
│   ├── assets/            # 이미지·첨부파일
│   ├── papers/            # 논문 (.pdf, .md)
│   ├── articles/          # 웹 기사·블로그 (Obsidian Web Clipper)
│   └── books/             # 책 발췌·클리핑
├── 02.wiki/               # LLM이 생성·유지 (사람은 읽기만)
│   ├── index.md           # 전체 페이지 카탈로그
│   ├── log.md             # 시간순 작업 로그 (append-only)
│   ├── overview.md        # 전체 합성
│   ├── entities/          # 사람·조직·모델·제품·도구
│   ├── concepts/          # LLM/AI 개념 (기법·아키텍처·이론·패턴)
│   ├── engineering/       # 소프트웨어 엔지니어링 개념
│   ├── til/               # Today I Learned
│   ├── reading/           # 독서 관리 (books/, papers/)
│   └── sources/           # 소스별 요약 (01.raw/와 1:1 대응)
├── article-clipper.json   # Obsidian Web Clipper 템플릿 (기사용)
└── book-clipper.json      # Obsidian Web Clipper 템플릿 (책용)
```

---

## 슬래시 커맨드

Claude Code 세션에서 사용:

| 커맨드 | 동작 | CLAUDE.md 참조 |
|--------|------|----------------|
| `/ingest` | `01.raw/`의 새 소스를 읽고 `02.wiki/sources/` · entities · concepts · overview · index · log 까지 한 번에 갱신 | §3.1 |
| `/query` | 위키 인덱스·페이지를 정독해 `[[인용]]` 포함 답변, 필요시 결과를 새 페이지로 archive 제안 | §3.2 |
| `/reading-add` | 책/논문을 `to-read` 상태로 reading 노트 생성, 대시보드 등록 | §3.4 |
| `/reading-start` | 해당 reading 노트의 status를 `reading`으로 전환, `started` 날짜 기록 | §3.4 |
| `/reading-done` | status를 `completed`로 전환, rating·인사이트 정리, concepts 페이지 반영 | §3.4 |
| `/til` | `02.wiki/til/YYYY-MM-DD-topic.md` 신규 생성, til/index.md·log.md 갱신 | §3.5 |
| `/lint` | 모순·고아 페이지·누락 개체·frontmatter 불일치·독서 상태 불일치 보고 | §3.3 |

자연어 트리거도 동작 (예: "오늘 Go의 defer 실행 순서를 배웠어" → `/til` 자동 호출).

---

## 사용 시나리오

### 1. 웹 기사 흡수
1. 브라우저에서 **Obsidian Web Clipper**로 기사 클립 → `01.raw/articles/` 저장
   - 템플릿: `article-clipper.json` (Obsidian Web Clipper 설정에 import)
2. Claude Code에서 `/ingest` 호출
3. LLM이 요약·교차 참조·entities·concepts 자동 생성

### 2. 책 읽기 흐름
```
/reading-add  → to-read 등록
       ↓ (실제로 읽기 시작)
/reading-start → status: reading, started 날짜
       ↓ (완독)
/reading-done → status: completed, rating, 인사이트 정리
       ↓ (선택)
01.raw/books/ 에 원문·클리핑 저장 후 /ingest
```

교보문고 등에서 책 정보를 Web Clipper로 가져왔다면 **`raw-book-cleaner` skill**이 쇼핑/네비게이션 노이즈를 자동 제거합니다 ("raw/books 정리해줘" 또는 "책 클리핑 정리").

### 3. 논문 추가
1. PDF를 `01.raw/papers/` 에 저장
2. `/reading-add` 로 to-read 등록 (또는 바로 `/ingest`)
3. 읽으면서 `/reading-start` → `/reading-done`

### 4. 빠른 학습 기록 (TIL)
- "오늘 Rust borrow checker가 NLL부터 어떻게 바뀌었는지 배웠어" → `/til`
- 3~10줄 짧게, 관련 개념은 `[[링크]]`로 연결, 길어지면 `concepts/`나 `engineering/` 페이지로 승격

### 5. 위키에 질문 (`/query`)
- "Transformer의 attention 메커니즘 정리해줘" → `/query` → `02.wiki/index.md` → 관련 페이지 정독 → `[[인용]]` 포함 답변
- 자연어로도 트리거됨 ("위키에서 X 찾아줘", "X에 대해 위키에 뭐가 있어?")
- 페이지에 근거가 없으면 "근거 없음"을 명시 (잘못된 인용보다 솔직한 공백이 낫다)
- 새로운 합성/비교라면 `concepts/`·`engineering/`에 archive 제안 → 동의 시 페이지 생성 + `index.md` 갱신

### 6. 정기 점검
- `/lint` 를 주기적으로 실행 → `02.wiki/lint-report-YYYY-MM-DD.md` 생성 → 처리 후 삭제

---

## 페이지 컨벤션 요약

- **파일명**: kebab-case (TIL은 `YYYY-MM-DD-topic.md`)
- **언어**: 한국어 우선, 기술 용어는 영어 병기, frontmatter 키는 영어
- **frontmatter 필수**: `title`, `type`, `tags`, `created`, `updated`
- **본문**: 첫 문단 1~3문장 요약 → H2/H3 섹션 → 마지막 `## References`
- **교차링크**: `[[slug]]` 적극 사용

타입별 상세 필드는 `CLAUDE.md` §2.2 참조.

---

## 역할 분담

| 역할 | 담당 |
|------|------|
| 소스 큐레이션, 읽을 책 결정, 질문·방향 결정 | **사람** |
| 독서/TIL 트리거 ("이 책 다 읽었어", "오늘 X 배웠어") | **사람** |
| 읽기·요약·작성·교차 참조·일관성 유지 | **LLM** |
| 모순·중복 탐지, frontmatter 관리 | **LLM** |
| `00.notes/` 초안 (사람 또는 LLM) → 보완·정제·링크 | 협업 |
| `02.wiki/` 전체 편집 | **LLM 전담** |

---

## Obsidian 활용

- **그래프 뷰**: 허브/고아 페이지 시각 확인
- **Dataview**: reading status·최근 TIL 자동 테이블

```dataview
TABLE status, rating, author FROM "02.wiki/reading/books"
WHERE status = "completed"
SORT rating DESC
```

```dataview
LIST FROM "02.wiki/til"
SORT date DESC
LIMIT 10
```

- **Web Clipper**: `article-clipper.json` / `book-clipper.json` 템플릿 사용

---

## 원칙

- **사람**: 무엇을 읽을지·물을지·방향 결정
- **LLM**: 읽기·요약·교차 참조·정리·일관성 유지
- **`02.wiki/`는 사람이 거의 손대지 않음** — 모든 편집은 LLM 담당

운영 규칙 전체: [`CLAUDE.md`](./CLAUDE.md)

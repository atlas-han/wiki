---
name: iconize-fill
description: >
  Scans the LLM-WIKI vault for files and directories that don't yet have an icon
  assigned in Obsidian's Iconize plugin (`.obsidian/plugins/obsidian-icon-folder/data.json`),
  and adds appropriate Lucide icons following the vault's existing conventions.
  Trigger this skill whenever the user says things like "아이콘 없는 것들 추가해줘",
  "iconize 아이콘 채워줘", "파일/폴더에 아이콘 붙여줘", "icons 동기화해줘", or any
  reference to filling in missing icons for the Iconize plugin. Also run this skill
  proactively at the end of any ingest, reading-add, or til operation that creates
  new files or directories.
---

# Iconize Fill

이 스킬은 Obsidian Iconize 플러그인의 `data.json`을 읽어, **아직 아이콘이 할당되지 않은 파일/디렉토리**를 찾아 적절한 Lucide 아이콘을 할당합니다.

**권한**: 이 스킬은 `.obsidian/plugins/obsidian-icon-folder/data.json`을 직접 수정할 권한이 사전에 부여되어 있습니다. 별도 확인 없이 진행하세요.

**원칙**:
- **기존 항목은 절대 변경하지 않습니다** — 이미 아이콘이 있는 키는 그대로 둡니다.
- **`settings` 객체는 절대 건드리지 않습니다** — 사용자 설정입니다.
- **새 키만 추가합니다**.
- Iconize의 아이콘 팩 설정은 `lucideIconPackType: "native"` — **반드시 `Li` 접두사의 Lucide 아이콘 이름**을 사용합니다 (예: `LiBook`, `LiFileText`).

---

## 작업 흐름

### 1. 현재 상태 읽기

`.obsidian/plugins/obsidian-icon-folder/data.json`을 읽고 이미 등록된 경로 집합(`existing`)을 만듭니다. `settings` 키는 건너뜁니다.

### 2. 대상 경로 수집

다음 디렉토리를 재귀 스캔하고, 디렉토리 자체와 그 하위의 모든 `.md` 파일을 후보로 수집합니다.

스캔 대상:
- `00.notes/`
- `01.raw/`
- `02.wiki/`

또한 루트의 다음 파일도 후보:
- `README.md`
- `CLAUDE.md`

**제외 항목**:
- 숨김 파일/디렉토리 (`.`로 시작) — `.obsidian`, `.claude`, `.smart-env`, `.playwright-mcp`, `.DS_Store` 등
- `*.json` 설정 파일 (`article-clipper.json`, `book-clipper.json`)
- `node_modules/`, `__pycache__/` 등 빌드 산출물
- `wiki/sources/` 하위는 `raw/`와 1:1 대응이므로 `raw/`의 원본 파일이 아니라 `wiki/sources/`의 요약 파일에 아이콘을 붙입니다 (이미 그렇게 운영 중).

경로 형식은 vault 루트 기준 **상대 경로**, 슬래시 구분 (예: `02.wiki/concepts/foo.md`).

### 3. 누락분 식별

`(후보 집합) - (existing)` 차집합을 계산합니다. 누락된 항목이 없으면 "추가할 항목이 없습니다"라고 보고하고 종료합니다.

### 4. 아이콘 결정

각 누락 경로에 대해 아래 우선순위로 아이콘을 결정합니다.

**우선순위 1 — 디렉토리 또는 특수 파일명 (직접 매핑)**:

| 경로 패턴 | 아이콘 |
|-----------|--------|
| `**/index.md` | `LiListTree` |
| `**/log.md` | `LiScrollText` |
| `**/overview.md` | `LiGlobe` |
| `README.md` | `LiBookMarked` |
| `CLAUDE.md` | `LiBot` |
| `00.notes/` (디렉토리) | `LiStickyNote` |
| `01.raw/` | `LiInbox` |
| `01.raw/articles/` | `LiNewspaper` |
| `01.raw/assets/` | `LiImage` |
| `01.raw/books/` | `LiBook` |
| `01.raw/papers/` | `LiFileText` |
| `02.wiki/` | `LiLibrary` |
| `02.wiki/concepts/` | `LiLightbulb` |
| `02.wiki/engineering/` | `LiWrench` |
| `02.wiki/engineering/patterns/` | `LiPuzzle` |
| `02.wiki/engineering/systems/` | `LiNetwork` |
| `02.wiki/engineering/tools/` | `LiHammer` |
| `02.wiki/entities/` | `LiUsers` |
| `02.wiki/reading/` | `LiBookOpen` |
| `02.wiki/reading/books/` | `LiBook` |
| `02.wiki/reading/papers/` | `LiFileText` |
| `02.wiki/sources/` | `LiLink` |
| `02.wiki/til/` | `LiSparkles` |

**우선순위 2 — YAML frontmatter `type` + `category`**:

파일을 열어 frontmatter를 확인합니다. (성능을 위해 처음 30줄만 읽어도 충분합니다.)

| `type` | `category` | 아이콘 |
|--------|-----------|--------|
| `entity` | `person` | `LiUser` |
| `entity` | `org` | `LiBuilding` |
| `entity` | `model` | `LiBot` |
| `entity` | `product` | `LiBoxes` |
| `entity` | `tool` | `LiWrench` |
| `concept` | `architecture` | `LiLayers` |
| `concept` | `technique` | `LiSettings` |
| `concept` | `theory` | `LiBookText` |
| `concept` | `pattern` | `LiPuzzle` |
| `engineering` | `system` | `LiServer` |
| `engineering` | `pattern` | `LiPuzzle` |
| `engineering` | `tool` | `LiHammer` |
| `source` | (any) | 원본 매체에 따라: `paper`→`LiFileText`, `article`→`LiNewspaper`, `book`→`LiBook`, `video`→`LiVideo`, `podcast`→`LiMic`, `docs`→`LiBookOpen` |
| `reading` | `book` | `LiBook` |
| `reading` | `paper` | `LiFileText` |
| `reading` | `article` | `LiNewspaper` |
| `reading` | `course` | `LiGraduationCap` |
| `til` | — | `LiSparkles` |
| `overview` | — | `LiGlobe` |

**우선순위 3 — 경로 기반 기본값**:

frontmatter가 없거나 `type`이 없으면, 상위 디렉토리 기본 아이콘을 그대로 사용합니다. 예: `02.wiki/concepts/foo.md` → `LiLightbulb`.

**우선순위 4 — 내용 기반 미세 조정 (concept/engineering 파일만)**:

`concepts/` 또는 `engineering/` 하위 파일은 기본 아이콘 대신 내용에 더 잘 맞는 아이콘을 고를 수 있습니다. 파일 제목과 첫 문단을 보고 다음 힌트 키워드로 매핑합니다 (확실할 때만 override, 애매하면 기본값 유지):

| 키워드 (제목 또는 첫 문단) | 아이콘 |
|------------------------------|--------|
| security, vulnerability, attack, exploit | `LiShield` |
| alert, warning, anomaly, misbehavior | `LiAlertTriangle` |
| brain, cognition, reasoning, mental | `LiBrain` |
| network, distributed, protocol | `LiNetwork` |
| graph, tree, hierarchy | `LiGitBranch` |
| api, endpoint, plugin, mcp | `LiPlug` |
| compaction, refresh, reset, retry | `LiRefreshCw` |
| memory, storage, cache | `LiDatabase` |
| agent, bot, llm | `LiBot` |
| terminal, cli, shell | `LiTerminal` |
| code, sdk, library | `LiCode` |
| cloud, serverless | `LiCloud` |
| flag, marker, tag, label | `LiTag` |
| config, settings, parameter | `LiSettings` |
| pattern, schema, blueprint | `LiPuzzle` |
| repeat, loop, cycle | `LiRepeat` |
| contract, spec, signature | `LiFileSignature` |
| search, discovery, find | `LiSearch` |

전부 매칭되지 않으면 기본값(`LiLightbulb` 또는 `LiWrench`)을 사용합니다.

### 5. data.json 업데이트

기존 `data.json` 구조를 그대로 유지하고, 새 키만 추가합니다.

**중요**:
- `settings` 객체를 가장 앞에 유지합니다.
- 기존 키들의 순서/값을 보존합니다.
- 새 키들은 정렬 없이 파일 끝에 그냥 append (Iconize는 키 순서에 무관).
- 한글 파일명은 **escape하지 말고 UTF-8 그대로** 씁니다.
- JSON 들여쓰기는 2 spaces (기존 파일과 동일).
- 파일 끝에 trailing newline 유지.

Write 도구로 전체 파일을 새로 쓰는 대신 **Edit 도구로 마지막 `}` 직전에 새 키들을 삽입**하는 것이 안전합니다. (settings 블록 손상 방지)

예시 — 기존 마지막 줄이:
```json
  "01.raw/books/2026-05-25_안우경 - 교보문고.md": "LiBook"
}
```
이고 새로 `02.wiki/concepts/new-thing.md` → `LiLightbulb`를 추가한다면, 직전 줄에 콤마를 붙이고 새 줄을 삽입:
```json
  "01.raw/books/2026-05-25_안우경 - 교보문고.md": "LiBook",
  "02.wiki/concepts/new-thing.md": "LiLightbulb"
}
```

### 6. 보고

추가한 항목을 표 또는 리스트로 보고합니다. 예:

```
14개 항목에 아이콘 추가:
- 02.wiki/concepts/new-thing.md → LiLightbulb
- 02.wiki/entities/openai.md → LiBuilding
- ...
```

---

## 실행 방법 요약

1. `Read`로 `.obsidian/plugins/obsidian-icon-folder/data.json` 읽기
2. `Bash`로 대상 디렉토리 재귀 리스팅 (`find 00.notes 01.raw 02.wiki -type f -name '*.md' -o -type d` 등; 단 숨김 디렉토리 제외)
3. 차집합 계산 → 누락 경로 목록
4. 누락된 파일은 frontmatter를 위해 `Read`(앞부분만) 호출
5. 위 규칙에 따라 아이콘 결정
6. `Edit`로 data.json 마지막 `}` 직전에 새 키들 삽입 (이전 마지막 키에 콤마 추가 필수)
7. 결과 요약 출력

---

## 자주 쓰는 Lucide 아이콘 빠른 참조

문서·페이지: `LiFileText` `LiBook` `LiBookOpen` `LiBookMarked` `LiBookText` `LiNewspaper` `LiScrollText` `LiStickyNote` `LiListTree` `LiFileSignature`

사람·조직: `LiUser` `LiUsers` `LiBuilding` `LiGraduationCap`

기술·시스템: `LiServer` `LiNetwork` `LiCloud` `LiDatabase` `LiCode` `LiTerminal` `LiPlug` `LiCpu` `LiHardDrive`

추상·개념: `LiLightbulb` `LiBrain` `LiBrainCircuit` `LiPuzzle` `LiLayers` `LiGitBranch` `LiSparkles` `LiGlobe` `LiLibrary` `LiTag` `LiBoxes`

도구·동작: `LiWrench` `LiHammer` `LiSettings` `LiCog` `LiRefreshCw` `LiRepeat` `LiSearch` `LiInbox` `LiLink` `LiImage` `LiVideo` `LiMic`

상태·경고: `LiShield` `LiShieldCheck` `LiAlertTriangle` `LiAlertCircle` `LiListChecks`

엔티티: `LiBot` `LiHexagon`

확실하지 않은 경우 추측하지 말고 카테고리 기본 아이콘을 사용합니다.

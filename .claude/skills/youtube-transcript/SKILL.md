---
name: youtube-transcript
description: >
  Downloads a YouTube video's transcript (subtitles/captions) with yt-dlp and saves it
  as a clean, deduplicated markdown source file into `01.raw/articles/` of the LLM-WIKI
  vault — using the same frontmatter convention as the Obsidian Web Clipper so it is
  ready for the `/ingest` pipeline (ingest runs only on explicit user approval, never
  automatically). Falls back to auto-generated captions, then to
  Whisper transcription if no subtitles exist. Trigger this skill whenever the user gives
  a YouTube URL and wants its text, or says things like "유튜브 자막 받아줘", "이 영상
  트랜스크립트 가져와줘", "유튜브 영상 받아쓰기 해줘", "이 영상 위키에 넣어줘",
  "download/get/fetch the transcript from this YouTube video", "get captions/subtitles",
  or "transcribe this YouTube video".
allowed-tools: Bash, Read, Write
---

# YouTube Transcript Downloader

이 스킬은 `yt-dlp`로 YouTube 영상의 자막(subtitle/caption)을 받아, **중복 제거된 깔끔한 plain-text**로 변환한 뒤 LLM-WIKI의 `01.raw/articles/`에 **Web Clipper와 동일한 frontmatter 형식**으로 저장합니다. 저장 이후 사용자가 원하면 `/ingest`로 위키에 흡수할 수 있습니다 — **`/ingest`는 자동 실행하지 않으며 반드시 사용자 승인을 받습니다.**

**출력 위치**: `01.raw/articles/YYYY-MM-DD_제목.md` — 영상 트랜스크립트도 텍스트 소스이므로 기존 article 클리핑과 같은 디렉토리·포맷에 저장해 `/ingest` 파이프라인을 그대로 재사용합니다.

**권한**: 이 스킬은 `01.raw/articles/`에 새 파일을 생성할 권한이 사전에 부여되어 있습니다. (자막이 정상적으로 받아지면 별도 확인 없이 저장하세요.)

다음은 **반드시 사용자 승인을 받은 뒤에만** 진행합니다 — 자동 실행 금지:
- **`/ingest` (위키 흡수)** — 저장 후 제안만 하고, 사용자가 명시적으로 동의해야 실행
- **Whisper 받아쓰기** / **대용량 오디오 다운로드**
- **도구 설치** (yt-dlp, Whisper 등)

---

## 언제 사용하는가

사용자가 다음을 요청할 때:
- YouTube URL을 주면서 트랜스크립트/자막/대본을 원할 때
- "유튜브 자막 받아줘", "이 영상 받아쓰기 해줘", "이 영상 위키에 넣어줘"
- "download/get/fetch transcript", "get captions/subtitles", "transcribe this video"
- 영상의 텍스트 내용이 필요할 때

---

## 작동 원리 (우선순위)

1. **yt-dlp 설치 확인** — 없으면 설치 (확인 후)
2. **자막 목록 확인** (`--list-subs`) — 실제로 무엇이 있는지 먼저 본다
3. **수동 자막 우선** (`--write-sub`) — 사람이 만든 최고 품질
4. **자동 생성 자막 폴백** (`--write-auto-sub`) — 대개 존재
5. **최후 수단: Whisper 받아쓰기** — 자막이 전혀 없을 때만 (사용자 확인 필수)
6. **plain-text 변환 + 중복 제거**
7. **`01.raw/articles/`에 frontmatter 포함 `.md`로 저장**
8. **`/ingest` 실행 *제안*** — 위키로 흡수 (자동 실행 ❌ · 사용자 승인 후에만)

> 한 영상의 자막은 진행형으로 겹치는 타임스탬프 때문에 **중복 라인**이 매우 많습니다. plain-text 변환 시 반드시 dedup 합니다 (말 순서는 보존).

---

## 1단계 — yt-dlp 설치 확인

```bash
which yt-dlp || command -v yt-dlp
```

### 설치되어 있지 않으면

시스템에 맞게 설치를 시도합니다 (**사용자에게 알리고 진행**):

**macOS (Homebrew)** — 이 환경의 기본:
```bash
brew install yt-dlp
```

**Linux (apt)**:
```bash
sudo apt update && sudo apt install -y yt-dlp
```

**pip (모든 시스템)**:
```bash
pip3 install yt-dlp        # 또는: python3 -m pip install yt-dlp
```

설치 실패 시: <https://github.com/yt-dlp/yt-dlp#installation> 를 안내하고 중단합니다.

---

## 2단계 — 자막 목록 확인

**다운로드 전에 항상 먼저** 무엇이 있는지 확인합니다:

```bash
yt-dlp --list-subs "YOUTUBE_URL"
```

- 수동 자막(품질↑) / 자동 생성 자막 여부
- 사용 가능한 언어 (한국어 `ko`, 영어 `en` 등)

---

## 3단계 — 메타데이터 수집 (파일명·frontmatter용)

```bash
yt-dlp --print "%(title)s\t%(uploader)s\t%(duration_string)s\t%(upload_date>%Y-%m-%d)s\t%(id)s" "YOUTUBE_URL"
```

탭으로 구분된: `제목 / 채널 / 길이(HH:MM:SS) / 업로드일 / 영상ID`.
파일명에 쓸 안전한 제목으로 정리합니다 (`/`, `:`, `?`, `"` 등 제거/치환).

---

## 4단계 — 자막 다운로드 전략

작업용 임시 디렉토리에서 받습니다 (예: `01.raw/articles/.yt-tmp/` 또는 cwd). 최종 `.md`만 `01.raw/articles/`에 남깁니다.

### 옵션 1: 수동 자막 (우선)

```bash
yt-dlp --write-sub --sub-langs "ko,en" --skip-download --output "OUTPUT_NAME" "YOUTUBE_URL"
```

### 옵션 2: 자동 생성 자막 (폴백)

수동 자막이 없으면:

```bash
yt-dlp --write-auto-sub --sub-langs "ko,en" --skip-download --output "OUTPUT_NAME" "YOUTUBE_URL"
```

둘 다 `.vtt`(WebVTT) 파일을 만듭니다. 언어를 모르면 `--sub-langs`를 빼고 받은 뒤 생성된 `*.vtt`를 사용합니다.

### 옵션 3: Whisper 받아쓰기 (최후 수단) — **사용자 확인 필수**

수동·자동 자막이 **모두 없을 때만** 사용합니다.

**a. 용량·길이 안내 후 확인 받기**
```bash
yt-dlp --print "%(filesize,filesize_approx)s" -f "bestaudio" "YOUTUBE_URL"
yt-dlp --print "%(duration)s %(title)s" "YOUTUBE_URL"
```
사용자에게: "자막이 없습니다. 오디오(약 X MB)를 받아 Whisper로 받아쓰기할까요?" → **승인 대기**.

**b. Whisper 설치 확인** (없으면 설치 여부 확인)
```bash
command -v whisper || pip3 install openai-whisper   # 승인 시에만
```

**c. 오디오만 다운로드**
```bash
yt-dlp -x --audio-format mp3 --output "audio_%(id)s.%(ext)s" "YOUTUBE_URL"
```

**d. 받아쓰기** (모델은 `base` 권장)
```bash
whisper audio_VIDEO_ID.mp3 --model base --output_format vtt
# 언어를 알면: --language ko / --language en
```
모델: `tiny`(빠름)·**`base`(권장)**·`small`·`medium`·`large`(정확↑, 무겁다).

**e. 정리**: 받아쓰기 후 "오디오 파일 삭제할까요?" 확인 후 `rm audio_VIDEO_ID.mp3`.

---

## 5단계 — plain-text 변환 (중복 제거)

VTT의 타임스탬프·태그·중복 라인을 제거하고 말 순서를 보존합니다:

```bash
python3 -c "
import re
seen = set()
with open('VTT_FILE', 'r') as f:
    for line in f:
        line = line.strip()
        if line and not line.startswith('WEBVTT') and not line.startswith('Kind:') and not line.startswith('Language:') and '-->' not in line:
            clean = re.sub('<[^>]*>', '', line)
            clean = clean.replace('&amp;', '&').replace('&gt;', '>').replace('&lt;', '<')
            if clean and clean not in seen:
                print(clean)
                seen.add(clean)
"
```

이 출력(깔끔한 본문)을 캡처해 다음 단계의 `.md` 본문으로 씁니다.

---

## 6단계 — `01.raw/articles/`에 저장 (Write 도구)

Web Clipper article 컨벤션과 동일한 frontmatter로 저장합니다. 파일명: `YYYY-MM-DD_안전한제목.md` (날짜 = 오늘).

```markdown
---
title: {영상 제목}
type: video
source: {YouTube URL}
site: youtube.com
author:
  - "[[{채널명}]]"
duration: {HH:MM:SS}
published: {업로드일 YYYY-MM-DD}
created: {오늘 YYYY-MM-DD}
description:
tags:
  - clippings/youtube
---

**Source URL**: {YouTube URL}
**Channel**: {채널명} · **Duration**: {HH:MM:SS} · **Published**: {업로드일}

{중복 제거된 트랜스크립트 본문}
```

규칙:
- `type: video` — CLAUDE.md의 source-type 어휘와 일치 (article 클리핑은 `type: article`).
- `author`는 채널명을 `[[wikilink]]`로 (article 클리퍼와 동일 방식) → `/ingest`가 entity로 연결.
- `tags: [clippings/youtube]` 로 영상 출처를 구분.
- 본문 첫 줄 `**Source URL**: ...`는 클리퍼 `noteContentFormat`과 동일.

저장 후 임시 `.vtt`(및 Whisper용 오디오/.txt)는 삭제합니다.

---

## 7단계 — 위키로 흡수 *제안* (자동 실행 금지)

> ⛔ **`/ingest`는 절대 자동으로 실행하지 않습니다.** 저장이 끝나면 아래처럼 **제안만** 하고, 멈춰서 사용자 응답을 기다립니다.

저장 완료 후 사용자에게 안내합니다:

> ✓ `01.raw/articles/{파일명}.md` 저장 완료. `/ingest`로 위키에 흡수할까요?

**사용자가 명시적으로 동의한 경우에만** `/ingest` 스킬을 실행해 `02.wiki/`에 source/entity/concept 페이지를 생성합니다. 사용자가 "아니오"이거나 응답이 없으면 흡수하지 않고 종료합니다. (ingest를 실행한 경우, 그 ingest 과정 끝에서 `iconize-fill`이 새 파일 아이콘을 채웁니다 — 이는 ingest 스킬 자체의 동작입니다.)

---

## 전체 워크플로 예시

```bash
VIDEO_URL="https://www.youtube.com/watch?v=VIDEO_ID"
WIKI="/Users/hannamil/Library/Mobile Documents/iCloud~md~obsidian/Documents/LLM-WIKI"
TMP="$WIKI/01.raw/articles/.yt-tmp"
mkdir -p "$TMP"

# 1) yt-dlp 확인
command -v yt-dlp >/dev/null || { echo "yt-dlp 설치 필요 — 사용자 확인 후 'brew install yt-dlp'"; }

# 2) 자막 목록
yt-dlp --list-subs "$VIDEO_URL"

# 3) 메타데이터
yt-dlp --print "%(title)s\t%(uploader)s\t%(duration_string)s\t%(upload_date>%Y-%m-%d)s\t%(id)s" "$VIDEO_URL"

# 4) 수동 → 자동 폴백 (임시 디렉토리)
yt-dlp --write-sub --sub-langs "ko,en" --skip-download --output "$TMP/sub" "$VIDEO_URL" \
  || yt-dlp --write-auto-sub --sub-langs "ko,en" --skip-download --output "$TMP/sub" "$VIDEO_URL"
#  ↑ 둘 다 실패하면 → 5단계(Whisper)로, 사용자 확인 후 진행

# 5) plain-text 변환 (생성된 vtt 사용)
VTT_FILE=$(ls "$TMP"/*.vtt 2>/dev/null | head -n 1)
python3 -c "
import re
seen=set()
for line in open('$VTT_FILE'):
    line=line.strip()
    if line and not line.startswith(('WEBVTT','Kind:','Language:')) and '-->' not in line:
        c=re.sub('<[^>]*>','',line).replace('&amp;','&').replace('&gt;','>').replace('&lt;','<')
        if c and c not in seen:
            print(c); seen.add(c)
" > "$TMP/transcript.txt"

# 6) → Read로 transcript.txt 읽고, Write 도구로 frontmatter + 본문을
#     01.raw/articles/YYYY-MM-DD_제목.md 로 저장 (위 6단계 템플릿)

# 7) 정리
rm -rf "$TMP"
```

> 위 스크립트는 다운로드·변환만 한다. **최종 `.md` 조립은 Write 도구로** 메타데이터와 본문을 합쳐 저장하라 (raw-book-cleaner / iconize-fill 처럼 명령 실행 + 판단 조합 방식).

---

## 에러 핸들링

**1. yt-dlp 미설치** — 시스템에 맞게 설치 시도(사용자 통지), 실패 시 설치 링크 안내 후 중단.

**2. 자막 없음** — `--list-subs`로 재확인 → `--write-sub`/`--write-auto-sub` 모두 시도 → 그래도 없으면 용량 안내 후 Whisper 옵션 제안(확인 필수).

**3. 비공개/연령제한/지역차단 영상** — URL 형식 확인(`https://www.youtube.com/watch?v=ID`), yt-dlp의 구체적 에러를 사용자에게 그대로 전달.

**4. Whisper 설치 실패** — ffmpeg/rust 등 의존성 필요할 수 있음. `pip3 install openai-whisper` 수동 안내, 디스크 여유(모델 1~10GB) 확인.

**5. 다운로드 중단** — 네트워크/디스크 확인, SSL 문제 시 `--no-check-certificate` 재시도.

**6. 다국어 자막** — 기본은 `--sub-langs "ko,en"`. 특정 언어만 원하면 `--sub-langs ko` 등으로 좁힘. `--list-subs`로 먼저 확인.

---

## Best Practices

- ✅ 다운로드 전 `--list-subs`로 항상 먼저 확인
- ✅ 각 단계 성공을 확인하고 다음으로 진행
- ✅ **대용량 다운로드 / Whisper / 도구 설치는 사용자 확인 후** 진행
- ✅ 최종 `.md`만 `01.raw/articles/`에 남기고 임시 파일(.vtt/.txt/오디오) 정리
- ✅ 저장 후 `/ingest` 흡수 제안
- ✅ plain-text 변환 시 항상 dedup, 말 순서 보존

# Agent Operating Guide

This repository is chris's LLM-WIKI knowledge base. It is maintained collaboratively by human direction plus AI agents.

## First step in every session

1. Treat `/opt/data/wiki` as the repository root.
2. Read `CLAUDE.md` first. It is the canonical schema and operating contract.
3. Read `02.wiki/index.md` to understand existing pages.
4. Read the recent tail of `02.wiki/log.md` before creating or updating pages.
5. If the task is topic-specific, search existing pages before creating new ones to avoid duplicates.

## Steward Agent

Primary steward: **Mnemosyne** (`.agents/mnemosyne.md`).

- Mnemosyne is the single accountable LLM-WIKI Steward Agent.
- Keep one steward until multi-agent thresholds are met.
- If multi-agent expansion becomes necessary, Mnemosyne becomes Orchestrator/Editor-in-Chief and keeps final write authority.
- Future specialist names are reserved in `.agents/mnemosyne.md`.

## Repository layout

- `.agents/`: agent specifications and expansion policy.
- `00.notes/`: human + LLM collaboration space.
- `01.raw/`: immutable source material. Read only. Do not edit existing raw files.
- `02.wiki/`: agent-owned generated wiki, indexes, logs, reading notes, TIL, sources.
- `CLAUDE.md`: canonical schema and workflow rules.
- `README.md`: human-facing guide.
- `AGENTS.md`: this file, for Hermes and other coding/research agents.

## Hermes-specific defaults

- `WIKI_PATH=/opt/data/wiki` is configured in the active Hermes profile environment.
- Prefer Korean for wiki prose; keep technical terms in English where useful.
- Use English frontmatter keys exactly as defined in `CLAUDE.md`.
- Use Obsidian-style `[[wikilinks]]`.
- Every meaningful wiki operation must update `02.wiki/index.md` if navigation changed and append to `02.wiki/log.md`.

## Editing policy

- Never silently overwrite conflicting information. Record contradictions explicitly.
- Do not create pages for passing mentions; follow the page thresholds in `CLAUDE.md`.
- Keep changes small and logically scoped.
- For raw source ingestion, write derived summaries/pages under `02.wiki/`; preserve raw source immutability.
- Before committing, run at least a basic structural check: `git status --short` and verify changed markdown paths are expected.

## Common operations

### Query

1. Read `02.wiki/index.md`.
2. Read relevant pages.
3. Answer with wiki citations such as `[[page-slug]]`.
4. If the answer is substantial and reusable, propose archiving it as a page.
5. Append a `query` entry to `02.wiki/log.md` when the query materially used the wiki.

### Ingest

1. Capture or identify the raw source in `01.raw/`.
2. Create/update `02.wiki/sources/<slug>.md`.
3. Update related entity/concept/engineering/reading pages.
4. Update `02.wiki/index.md`, `02.wiki/overview.md` if relevant, and `02.wiki/log.md`.

### TIL

1. Create `02.wiki/til/YYYY-MM-DD-topic.md`.
2. Update `02.wiki/til/index.md` and `02.wiki/log.md`.
3. Add cross-links to relevant pages when available.

### Reading

Follow `CLAUDE.md` §3.4 for `to-read`, `reading`, `completed`, and `dnf` state transitions.

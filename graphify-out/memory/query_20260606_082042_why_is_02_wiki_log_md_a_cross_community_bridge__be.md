---
type: "query"
date: "2026-06-06T08:20:42.010559+00:00"
question: "Why is 02.wiki/log.md a cross-community bridge (betweenness 0.293)? What does it link and why?"
contributor: "graphify"
source_nodes: ["02.wiki/log.md (chronological work log)", "Agent Harness Design", "Actix Web", "Anthropic", "LLM Wiki Pattern"]
---

# Q: Why is 02.wiki/log.md a cross-community bridge (betweenness 0.293)? What does it link and why?

## Answer

log.md is the append-only operation log: every ingest/lint/meta entry embeds [[wikilinks]] to the pages that operation touched. Because ingests have spanned every topic, its 26 EXTRACTED 'references' edges fan into 4 communities at once — C0 LLM-Harness (Agent Harness Design, Claude Code, Harness Engineering, Dynamic Workflows, Understand-Anything, Managed Agents...), C2 Actix-Web Knowledge (Actix Web, actix.rs docs, Tokio, Serde, Application State), C3 Anthropic Security (Anthropic), C5 Karpathy LLM-Wiki (LLM Wiki Pattern). It bridges by PROVENANCE/bookkeeping, not semantics: the topics aren't conceptually related, they're just co-recorded in one chronological ledger. High betweenness is an artifact of the wiki's own process, mirroring index.md and engineering/index.md which bridge the same way.

## Source Nodes

- 02.wiki/log.md (chronological work log)
- Agent Harness Design
- Actix Web
- Anthropic
- LLM Wiki Pattern
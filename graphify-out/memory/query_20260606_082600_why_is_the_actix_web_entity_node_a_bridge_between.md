---
type: "query"
date: "2026-06-06T08:26:00.812124+00:00"
question: "Why is the Actix Web entity node a bridge between raw docs (C1) and wiki knowledge (C2)? What does it anchor?"
contributor: "graphify"
source_nodes: ["Actix Web", "Actix Web — Extractors (FromRequest)", "Getting Started (docs)", "Actix Web Documentation Index (docs)", "Tokio"]
---

# Q: Why is the Actix Web entity node a bridge between raw docs (C1) and wiki knowledge (C2)? What does it anchor?

## Answer

actix_web (entity hub, community 2, degree 29) is the canonical framework anchor where the two REPRESENTATIONS of the same knowledge meet. OUTGOING (13, all C2): it fans out as the hub to every curated concept page — extractors, handlers-responders, application-state, routing, middleware, error-handling, databases, testing, websockets, http-server, connection-lifecycle + official-docs source + Tokio (the '주요 개념' section of entities/actix-web.md). INCOMING (16): 4 from C1 raw reference docs (Welcome, Getting Started, Auto-Reloading, Actix Web Documentation Index) that point UP from 01.raw/docs to the distilled entity; 11 from C2 siblings (Wiki Overview/Index, Engineering Index, the 5 actor pages, Serde, What-is-Actix-Web); 1 from C0 log.md (provenance). So it bridges C1 (raw verbatim docs) <-> C2 (curated wiki) by being the single front-door anchor: raw entry-point pages link up to it, deeper raw pages link to specific concept pages, and all wiki concepts hang off it. Unlike log.md (provenance bridge) and Engineering Index (taxonomy bridge), Actix Web is a genuine SEMANTIC hub — a healthy god node — joining source-layer and knowledge-layer views of one framework.

## Source Nodes

- Actix Web
- Actix Web — Extractors (FromRequest)
- Getting Started (docs)
- Actix Web Documentation Index (docs)
- Tokio
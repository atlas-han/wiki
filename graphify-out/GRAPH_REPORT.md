# Graph Report - 02.wiki  (2026-06-28)

## Corpus Check
- 172 files · ~61,419 words
- Verdict: corpus is large enough that graph structure adds value.

## Summary
- 176 nodes · 1156 edges · 7 communities
- Extraction: 99% EXTRACTED · 1% INFERRED · 0% AMBIGUOUS · INFERRED: 15 edges (avg confidence: 0.81)
- Token cost: 0 input · 0 output

## Community Hubs (Navigation)
- [[_COMMUNITY_Agent Harness & Workflows|Agent Harness & Workflows]]
- [[_COMMUNITY_Refactoring & Code Quality|Refactoring & Code Quality]]
- [[_COMMUNITY_Anthropic Models & Security|Anthropic Models & Security]]
- [[_COMMUNITY_GoF Design Patterns|GoF Design Patterns]]
- [[_COMMUNITY_Actix  Rust Web|Actix / Rust Web]]
- [[_COMMUNITY_LLM Wiki & Knowledge Graphs|LLM Wiki & Knowledge Graphs]]
- [[_COMMUNITY_Reading The Martian|Reading: The Martian]]

## God Nodes (most connected - your core abstractions)
1. `Log` - 168 edges
2. `Index` - 139 edges
3. `Overview` - 79 edges
4. `Agent Harness Design` - 38 edges
5. `Refactoring Techniques` - 38 edges
6. `Refactoring.Guru Refactoring` - 37 edges
7. `Code Smells` - 37 edges
8. `Claude Code` - 32 edges
9. `Technical Debt` - 31 edges
10. `디자인 패턴` - 29 edges

## Surprising Connections (you probably didn't know these)
- `Managed Agents` --semantically_similar_to--> `Dynamic Workflows`  [INFERRED] [semantically similar]
  02.wiki/entities/managed-agents.md → 02.wiki/concepts/dynamic-workflows.md
- `마션(스페셜 에디션)` --references--> `The Martian`  [INFERRED]
  02.wiki/reading/books/martian-special-edition.md → 02.wiki/sources/kyobo-martian-special-edition.md
- `교보문고 — 마션(스페셜 에디션)` --references--> `앤디 위어 (Andy Weir)`  [INFERRED]
  02.wiki/sources/kyobo-martian-special-edition.md → 02.wiki/reading/books/martian-special-edition.md
- `Deny-and-Continue` --semantically_similar_to--> `Agentic Misbehavior (Threat Model)`  [INFERRED] [semantically similar]
  02.wiki/concepts/deny-and-continue.md → 02.wiki/concepts/agentic-misbehavior.md
- `Harness Engineering` --semantically_similar_to--> `Agent Harness Design`  [INFERRED] [semantically similar]
  02.wiki/concepts/harness-engineering.md → 02.wiki/concepts/agent-harness-design.md

## Communities (7 total, 0 thin omitted)

### Community 0 - "Agent Harness & Workflows"
Cohesion: 0.22
Nodes (40): Agent Harness Design, Anthropic — Dynamic Workflows, Archon, Bun, Claude Code, Codex, Cory Dolphin, DeepAgents (+32 more)

### Community 1 - "Refactoring & Code Quality"
Cohesion: 0.26
Nodes (40): The Twelve-Factor App, Adam Wiggins, Alternative Classes With Different Interfaces, Code Smells, Comments, Data Class, Data Clumps, Dead Code (+32 more)

### Community 2 - "Anthropic Models & Security"
Cohesion: 0.25
Nodes (31): Agentic Misbehavior (Threat Model), AI Vulnerability Discovery, Anthropic, Anthropic — Claude Code Auto Mode, Anthropic — Harness Design for Long-Running Apps, Anthropic — Scaling Managed Agents, Anthropic — Project Glasswing Update (2026-05), Brain-Hands Decoupling (+23 more)

### Community 3 - "GoF Design Patterns"
Cohesion: 0.45
Nodes (24): 추상 팩토리 (Abstract Factory), 어댑터 (Adapter), 브리지 (Bridge), 빌더 (Builder), 책임 연쇄 (Chain of Responsibility), 커맨드 (Command), 복합체 (Composite), 데코레이터 (Decorator) (+16 more)

### Community 4 - "Actix / Rust Web"
Cohesion: 0.45
Nodes (23): 안 만만한 사람 vs 만만한 사람의 대화 위치, Actix — Address (Addr & Recipient), Actix — Context, Actix (Actor Framework), Actix — Actor Model, Actix — Arbiter & System, Actix — SyncArbiter, Actix Web (+15 more)

### Community 5 - "LLM Wiki & Knowledge Graphs"
Cohesion: 0.47
Nodes (13): Andrej Karpathy, Code Knowledge Graph, James AI Explorer — Understand-Anything Korean Guide, Karpathy — LLM Wiki Gist, LLM Wiki Pattern, Lum1104, Lum1104 — Understand-Anything README, Memex (+5 more)

### Community 6 - "Reading: The Martian"
Cohesion: 0.6
Nodes (5): 앤디 위어 (Andy Weir), 교보문고 — 마션(스페셜 에디션), 마션(스페셜 에디션), Reading Index, The Martian

## Knowledge Gaps
- **4 isolated node(s):** `Weakness Mining`, `Harness Proposal`, `Meta-Harness`, `The Martian`
  These have ≤1 connection - possible missing edges or undocumented components.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `Log` connect `Refactoring & Code Quality` to `Agent Harness & Workflows`, `Anthropic Models & Security`, `GoF Design Patterns`, `Actix / Rust Web`, `LLM Wiki & Knowledge Graphs`, `Reading: The Martian`?**
  _High betweenness centrality (0.526) - this node is a cross-community bridge._
- **Why does `Index` connect `Actix / Rust Web` to `Agent Harness & Workflows`, `Refactoring & Code Quality`, `Anthropic Models & Security`, `GoF Design Patterns`, `LLM Wiki & Knowledge Graphs`, `Reading: The Martian`?**
  _High betweenness centrality (0.261) - this node is a cross-community bridge._
- **Why does `Overview` connect `Agent Harness & Workflows` to `Refactoring & Code Quality`, `Anthropic Models & Security`, `GoF Design Patterns`, `Actix / Rust Web`, `LLM Wiki & Knowledge Graphs`?**
  _High betweenness centrality (0.056) - this node is a cross-community bridge._
- **What connects `Weakness Mining`, `Harness Proposal`, `Meta-Harness` to the rest of the system?**
  _4 weakly-connected nodes found - possible documentation gaps or missing edges._
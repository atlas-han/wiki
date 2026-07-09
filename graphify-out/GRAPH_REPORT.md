# Graph Report - 02.wiki  (2026-07-08)

## Corpus Check
- 175 files · ~63,375 words
- Verdict: corpus is large enough that graph structure adds value.

## Summary
- 181 nodes · 822 edges · 8 communities (7 shown, 1 thin omitted)
- Extraction: 98% EXTRACTED · 2% INFERRED · 0% AMBIGUOUS · INFERRED: 16 edges (avg confidence: 0.82)
- Token cost: 15,200 input · 4,200 output

## Community Hubs (Navigation)
- [[_COMMUNITY_Refactoring & Code Quality|Refactoring & Code Quality]]
- [[_COMMUNITY_Agent Harness & Self-Improvement|Agent Harness & Self-Improvement]]
- [[_COMMUNITY_Anthropic Agents & Security|Anthropic Agents & Security]]
- [[_COMMUNITY_GoF Design Patterns|GoF Design Patterns]]
- [[_COMMUNITY_LLM Wiki & Knowledge Graphs|LLM Wiki & Knowledge Graphs]]
- [[_COMMUNITY_Actix  Rust Web|Actix / Rust Web]]
- [[_COMMUNITY_Reading — The Martian|Reading — The Martian]]
- [[_COMMUNITY_Conversation Positioning|Conversation Positioning]]

## God Nodes (most connected - your core abstractions)
1. `Agent Harness Design` - 38 edges
2. `Refactoring Techniques` - 35 edges
3. `Claude Code` - 35 edges
4. `Refactoring.Guru Refactoring` - 34 edges
5. `Code Smells` - 34 edges
6. `Technical Debt` - 28 edges
7. `디자인 패턴` - 26 edges
8. `Anthropic` - 25 edges
9. `Refactoring.Guru 한국어 디자인 패턴` - 23 edges
10. `Actix Web 공식 문서 (actix.rs/docs)` - 20 edges

## Surprising Connections (you probably didn't know these)
- `Managed Agents` --semantically_similar_to--> `Dynamic Workflows`  [INFERRED] [semantically similar]
  02.wiki/entities/managed-agents.md → 02.wiki/concepts/dynamic-workflows.md
- `Deny-and-Continue` --semantically_similar_to--> `Agentic Misbehavior (Threat Model)`  [INFERRED] [semantically similar]
  02.wiki/concepts/deny-and-continue.md → 02.wiki/concepts/agentic-misbehavior.md
- `Harness Engineering` --semantically_similar_to--> `Agent Harness Design`  [INFERRED] [semantically similar]
  02.wiki/concepts/harness-engineering.md → 02.wiki/concepts/agent-harness-design.md
- `Proposal Validation` --semantically_similar_to--> `Generator-Evaluator Pattern`  [INFERRED] [semantically similar]
  02.wiki/concepts/self-harness.md → 02.wiki/concepts/generator-evaluator-pattern.md
- `Dynamic Workflows` --semantically_similar_to--> `Generator-Evaluator Pattern`  [INFERRED] [semantically similar]
  02.wiki/concepts/dynamic-workflows.md → 02.wiki/concepts/generator-evaluator-pattern.md

## Hyperedges (group relationships)
- **** — martian_special_edition, andy_weir, the_martian, kyobo_martian_special_edition [EXTRACTED 1.00]
- **Claude Code Auto Mode Safety Gate** — transcript_classifier, agentic_misbehavior, deny_and_continue, prompt_injection [INFERRED 0.85]
- **Self-Harness 3-Stage Optimization Loop** — weakness_mining, harness_proposal, proposal_validation, self_harness [EXTRACTED 1.00]
- **Three Paradigms of Harness Improvement** — harness_engineering, meta_harness, self_harness [EXTRACTED 1.00]
- **Claude Code Self-Writing Orchestration** — dynamic_workflows, ultracode, ralph_wiggum_method, generator_evaluator_pattern [INFERRED 0.85]
- **LLM Coding Guidelines 4원칙 (Think/Simplicity/Surgical/Goal-Driven)** — llm_coding_guidelines, surgical_edits, verifiable_goals, multica_karpathy_skills_claude_md [INFERRED 0.95]
- **Claude Code auto mode safety pipeline (probe + classifier)** — prompt_injection, transcript_classifier, agentic_misbehavior, anthropic_claude_code_auto_mode [INFERRED 0.85]
- **Context engineering → harness engineering → Ralph Loop 진화** — context_engineering, harness_engineering, ralph_wiggum_method, agent_harness_design, tech_bridge_harness_engineering [INFERRED 0.85]
- **Anthropic harness-engineering blog series** — anthropic_managed_agents, anthropic_claude_code_auto_mode, anthropic_harness_design_long_running_apps, anthropic_dynamic_workflows, agent_harness_design [INFERRED 0.95]
- **Terminal-Bench-2.0 Self-Harness Evaluation** — minimax_m2_5, qwen3_5, glm_5, terminal_bench [EXTRACTED 1.00]
- **Understand-Anything code-to-knowledge-graph pipeline** — understand_anything, tree_sitter_llm_hybrid, code_knowledge_graph, claude_code, generator_evaluator_pattern [INFERRED 0.85]
- **Actix Actor 모델 그룹 (Model + Address + Context)** — actix_actor_model, actix_actor_address, actix_actor_context [INFERRED 0.85]
- **Actix 런타임 실행 환경 (Arbiter + SyncArbiter + Tokio)** — actix_arbiter, actix_sync_arbiter, tokio [INFERRED 0.85]
- **Managed Agents session/harness/sandbox virtualization** — managed_agents, brain_hands_decoupling, pets_vs_cattle, context_resets_and_compaction [INFERRED 0.85]
- **Claude model family (4.6/4.7/Sonnet/Mythos)** — claude_opus_4_6, claude_opus_4_7, claude_sonnet_4_6, claude_mythos_preview [INFERRED 0.85]
- **Understand-Anything tooling stack** — understand_anything, lum1104, tree_sitter, claude_code [INFERRED 0.85]
- **Project Glasswing partners & evaluators** — project_glasswing, cloudflare, mozilla, uk_aisi, claude_mythos_preview [INFERRED 0.85]
- **Vault as shared agent+human command surface (Obsidian CLI)** — obsidian, obsidian_cli_workflow, claude_code, llm_wiki_pattern [INFERRED 0.75]
- **Karpathy-pattern wiki to knowledge-graph pipeline** — llm_wiki_pattern, understand_anything, code_knowledge_graph, tree_sitter_llm_hybrid [INFERRED 0.85]
- **Actix-web routing realizes Chain of Responsibility + Composite** — actix_web_routing, design_pattern_chain_of_responsibility, design_pattern_composite [EXTRACTED 0.90]
- **Actix-web FromRequest extractor realizes Adapter + Strategy** — actix_web_extractors, design_pattern_adapter, design_pattern_strategy [EXTRACTED 0.90]
- **Actix-web Responder handling realizes Strategy + Builder** — actix_web_handlers_responders, design_pattern_strategy, design_pattern_builder [EXTRACTED 0.90]

## Communities (8 total, 1 thin omitted)

### Community 0 - "Refactoring & Code Quality"
Cohesion: 0.23
Nodes (39): The Twelve-Factor App, Adam Wiggins, Alternative Classes With Different Interfaces, Code Smells, Comments, Data Class, Data Clumps, Dead Code (+31 more)

### Community 1 - "Agent Harness & Self-Improvement"
Cohesion: 0.18
Nodes (38): Agent Harness Design, Anthropic — Dynamic Workflows, Archon, Bun, Codex, Cory Dolphin, DeepAgents, Dynamic Workflows (+30 more)

### Community 2 - "Anthropic Agents & Security"
Cohesion: 0.25
Nodes (31): Agentic Misbehavior (Threat Model), AI Vulnerability Discovery, Anthropic, Anthropic — Claude Code Auto Mode, Anthropic — Harness Design for Long-Running Apps, Anthropic — Scaling Managed Agents, Anthropic — Project Glasswing Update (2026-05), Brain-Hands Decoupling (+23 more)

### Community 3 - "GoF Design Patterns"
Cohesion: 0.45
Nodes (24): 추상 팩토리 (Abstract Factory), Adapter Pattern, 브리지 (Bridge), Builder Pattern, Chain of Responsibility Pattern, 커맨드 (Command), Composite Pattern, Decorator Pattern (+16 more)

### Community 4 - "LLM Wiki & Knowledge Graphs"
Cohesion: 0.38
Nodes (22): Andrej Karpathy, Claude Code, Code Knowledge Graph, Engineering Index, Index (wiki catalog), James AI Explorer — Understand-Anything Korean Guide, Karpathy — LLM Wiki Gist, LLM Wiki Pattern (+14 more)

### Community 5 - "Actix / Rust Web"
Cohesion: 0.44
Nodes (21): Actix — Address (Addr & Recipient), Actix — Context, Actix (Actor Framework), Actix — Actor Model, Actix — Arbiter & System, Actix — SyncArbiter, Actix Web, Actix Web — Application State (web::Data) (+13 more)

### Community 6 - "Reading — The Martian"
Cohesion: 0.6
Nodes (5): 앤디 위어 (Andy Weir), 교보문고 — 마션(스페셜 에디션), 마션(스페셜 에디션), Reading Index, The Martian

## Knowledge Gaps
- **5 isolated node(s):** `안 만만한 사람 vs 만만한 사람의 대화 위치`, `Weakness Mining`, `Harness Proposal`, `Meta-Harness`, `The Martian`
  These have ≤1 connection - possible missing edges or undocumented components.
- **1 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `Technical Debt` connect `Refactoring & Code Quality` to `Agent Harness & Self-Improvement`?**
  _High betweenness centrality (0.345) - this node is a cross-community bridge._
- **Why does `Surgical Edits` connect `Agent Harness & Self-Improvement` to `Refactoring & Code Quality`, `LLM Wiki & Knowledge Graphs`?**
  _High betweenness centrality (0.337) - this node is a cross-community bridge._
- **Why does `Claude Code` connect `LLM Wiki & Knowledge Graphs` to `Agent Harness & Self-Improvement`, `Anthropic Agents & Security`?**
  _High betweenness centrality (0.222) - this node is a cross-community bridge._
- **What connects `안 만만한 사람 vs 만만한 사람의 대화 위치`, `Weakness Mining`, `Harness Proposal` to the rest of the system?**
  _5 weakly-connected nodes found - possible documentation gaps or missing edges._
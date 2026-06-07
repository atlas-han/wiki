# Graph Report - LLM-WIKI vault  (2026-06-06)

## Corpus Check
- 149 files · ~90,622 words
- Verdict: corpus is large enough that graph structure adds value.

## Summary
- 232 nodes · 722 edges · 21 communities (8 shown, 13 thin omitted)
- Extraction: 93% EXTRACTED · 7% INFERRED · 0% AMBIGUOUS · INFERRED: 50 edges (avg confidence: 0.84)
- Token cost: 0 input · 45,061 output

## Community Hubs (Navigation)
- [[_COMMUNITY_LLM Harness & Code Understanding|LLM Harness & Code Understanding]]
- [[_COMMUNITY_Actix Web Reference Docs|Actix Web Reference Docs]]
- [[_COMMUNITY_Actix Web Knowledge (Wiki)|Actix Web Knowledge (Wiki)]]
- [[_COMMUNITY_Anthropic Cyber-Security & Auto Mode|Anthropic Cyber-Security & Auto Mode]]
- [[_COMMUNITY_Wiki Graphify Query Script|Wiki Graphify Query Script]]
- [[_COMMUNITY_LLM Wiki & Karpathy Lineage|LLM Wiki & Karpathy Lineage]]
- [[_COMMUNITY_CLAUDE.md, Skills & 12-Factor|CLAUDE.md, Skills & 12-Factor]]
- [[_COMMUNITY_Wiki Governance & Editing Policy|Wiki Governance & Editing Policy]]
- [[_COMMUNITY_Book 바다에서 온 소년|Book: 바다에서 온 소년]]
- [[_COMMUNITY_Book 씽킹 101|Book: 씽킹 101]]
- [[_COMMUNITY_Book 프로젝트 헤일메리|Book: 프로젝트 헤일메리]]
- [[_COMMUNITY_Book 경험의 멸종|Book: 경험의 멸종]]
- [[_COMMUNITY_Book 우리는 어떻게 마음을 움직이는가|Book: 우리는 어떻게 마음을 움직이는가]]
- [[_COMMUNITY_Book 하룻밤에 읽는 오디세이아|Book: 하룻밤에 읽는 오디세이아]]
- [[_COMMUNITY_Reading Dashboard|Reading Dashboard]]
- [[_COMMUNITY_TIL Index|TIL Index]]
- [[_COMMUNITY_Actix Helper Actors (WIP)|Actix Helper Actors (WIP)]]
- [[_COMMUNITY_Actix IO Helpers (WIP)|Actix IO Helpers (WIP)]]
- [[_COMMUNITY_Actix Supervisor (WIP)|Actix Supervisor (WIP)]]
- [[_COMMUNITY_Actix Stream (WIP)|Actix Stream (WIP)]]
- [[_COMMUNITY_Actix Registry (WIP)|Actix Registry (WIP)]]

## God Nodes (most connected - your core abstractions)
1. `Agent Harness Design` - 36 edges
2. `Claude Code` - 33 edges
3. `Actix Web` - 29 edges
4. `Anthropic` - 26 edges
5. `02.wiki/log.md (chronological work log)` - 26 edges
6. `Engineering Index` - 24 edges
7. `Harness Engineering` - 23 edges
8. `Actix Web Documentation Index (docs)` - 23 edges
9. `Actix Web 공식 문서 (actix.rs/docs)` - 22 edges
10. `Anthropic — Harness Design for Long-Running Apps` - 20 edges

## Surprising Connections (you probably didn't know these)
- `scripts/wiki_graphify_query.py (graphify query helper)` --conceptually_related_to--> `Code Knowledge Graph`  [INFERRED]
  scripts/wiki_graphify_query.py → 02.wiki/concepts/code-knowledge-graph.md
- `scripts/wiki_graphify_query.py (graphify query helper)` --conceptually_related_to--> `Understand-Anything`  [INFERRED]
  scripts/wiki_graphify_query.py → 02.wiki/sources/lum1104-understand-anything.md
- `Generator-Evaluator Architecture` --semantically_similar_to--> `Transcript Classifier`  [INFERRED] [semantically similar]
  01.raw/articles/2026-05-25_Harness design for long-running application development.md → 02.wiki/concepts/transcript-classifier.md
- `Auto-Reloading (docs)` --references--> `Actix Web`  [INFERRED]
  01.raw/docs/actix-web/autoreload.md → 02.wiki/entities/actix-web.md
- `LLM-WIKI README` --references--> `LLM Wiki Pattern`  [EXTRACTED]
  README.md → 02.wiki/concepts/llm-wiki-pattern.md

## Hyperedges (group relationships)
- **Claude Code Auto Mode Safety Gate** — transcript_classifier, agentic_misbehavior, deny_and_continue, prompt_injection [INFERRED 0.85]
- **Claude Code Self-Writing Orchestration** — dynamic_workflows, ultracode, ralph_wiggum_method, generator_evaluator_pattern [INFERRED 0.85]
- **LLM Coding Guidelines 4원칙 (Think/Simplicity/Surgical/Goal-Driven)** — llm_coding_guidelines, surgical_edits, verifiable_goals, multica_karpathy_skills_claude_md [INFERRED 0.95]
- **Claude Code auto mode safety pipeline (probe + classifier)** — prompt_injection, transcript_classifier, agentic_misbehavior, anthropic_claude_code_auto_mode [INFERRED 0.85]
- **Context engineering → harness engineering → Ralph Loop 진화** — context_engineering, harness_engineering, ralph_wiggum_method, agent_harness_design, tech_bridge_harness_engineering [INFERRED 0.85]
- **Anthropic harness-engineering blog series** — anthropic_managed_agents, anthropic_claude_code_auto_mode, anthropic_harness_design_long_running_apps, anthropic_dynamic_workflows, agent_harness_design [INFERRED 0.95]
- **Understand-Anything code-to-knowledge-graph pipeline** — understand_anything, tree_sitter_llm_hybrid, code_knowledge_graph, claude_code, generator_evaluator_pattern [INFERRED 0.85]
- **Actix Web 요청 처리 파이프라인 (Extractor → Handler → Responder)** — actix_web_extractors, actix_web_handlers_responders, actix_web_routing [INFERRED 0.85]
- **Actix Actor 모델 그룹 (Model + Address + Context)** — actix_actor_model, actix_actor_address, actix_actor_context [INFERRED 0.85]
- **Actix 런타임 실행 환경 (Arbiter + SyncArbiter + Tokio)** — actix_arbiter, actix_sync_arbiter, tokio [INFERRED 0.85]
- **Managed Agents session/harness/sandbox virtualization** — managed_agents, brain_hands_decoupling, pets_vs_cattle, context_resets_and_compaction [INFERRED 0.85]
- **Claude model family (4.6/4.7/Sonnet/Mythos)** — claude_opus_4_6, claude_opus_4_7, claude_sonnet_4_6, claude_mythos_preview [INFERRED 0.85]
- **Understand-Anything tooling stack** — understand_anything, lum1104, tree_sitter, claude_code [INFERRED 0.85]
- **Project Glasswing partners & evaluators** — project_glasswing, cloudflare, mozilla, uk_aisi, claude_mythos_preview [INFERRED 0.85]
- **Agentic Harness Engineering Ecosystem** — harness_engineering, agent_harness_design, managed_agents, ralph_loop, claude_code [INFERRED 0.85]
- **Code/Wiki to Knowledge Graph Pipeline** — understand_anything, tree_sitter, knowledge_graph, karpathy_pattern_llm_wiki, multi_agent_pipeline [INFERRED 0.85]
- **Claude Code Extensibility Layer** — claude_skills, subagents, hooks, claude_md, ai_layer [INFERRED 0.85]
- **Middleware: Transform factory builds Service in the App wrap chain** — transform_trait, service_trait, app [INFERRED 0.75]
- **HttpServer init: HttpServer -> App -> Worker/Tokio spawn** — httpserver, app, worker_loop, tokio [INFERRED 0.85]
- **Request handling: extractor -> handler -> responder -> response** — fromrequest, responder, httpresponse, httprequest [INFERRED 0.85]
- **Actix actor model documentation set** — actor, address, context, arbiter, sync_arbiter, getting_started [INFERRED 0.85]
- **Agent governance: AGENTS.md + CLAUDE.md jointly codify the rebase-first editing policy** — agents, claude_md_schema, remote_rebase_first_editing_policy [INFERRED 0.85]

## Communities (21 total, 13 thin omitted)

### Community 0 - "LLM Harness & Code Understanding"
Cohesion: 0.13
Nodes (56): Harness design for long-running application development (article), Scaling Managed Agents (article), Understand-Anything 1시간→5분 가이드 (article), Introducing dynamic workflows (article), Lum1104/Understand-Anything (GitHub README), 하네스 엔지니어링 (video), Agent Harness Design, Anthropic — Dynamic Workflows (+48 more)

### Community 1 - "Actix Web Reference Docs"
Cohesion: 0.08
Nodes (50): Actix Web Documentation Index (docs), actix_web::error::Error, actix-ws, App, Application (docs), Auto-Reloading (docs), Connection Lifecycle (docs), CORS (docs) (+42 more)

### Community 2 - "Actix Web Knowledge (Wiki)"
Cohesion: 0.29
Nodes (31): Actix Quick Start (docs), Actix — Address (Addr & Recipient), Actix — Context, Actix (Actor Framework), Actix — Actor Model, Actix — Arbiter & System, Actix — SyncArbiter, Actix Web (+23 more)

### Community 3 - "Anthropic Cyber-Security & Auto Mode"
Cohesion: 0.22
Nodes (25): Project Glasswing: Initial Update (article), Claude Code auto mode (article), Agent Permissions / Approval Delegation, Agentic Misbehavior (Threat Model), AI Cybersecurity / Vulnerability Discovery, AI Vulnerability Discovery, Anthropic, Anthropic — Claude Code Auto Mode (+17 more)

### Community 4 - "Wiki Graphify Query Script"
Cohesion: 0.22
Nodes (17): body_without_frontmatter(), build_graph(), expand(), first_summary(), load_pages(), main(), make_result(), normalize_link() (+9 more)

### Community 5 - "LLM Wiki & Karpathy Lineage"
Cohesion: 0.3
Nodes (16): LLM Wiki (article), Andrej Karpathy, Karpathy — LLM Wiki Gist, Karpathy-pattern LLM Wiki, LLM Coding Guidelines, LLM Wiki Pattern, Memex, Multica AI (+8 more)

### Community 6 - "CLAUDE.md, Skills & 12-Factor"
Cohesion: 0.19
Nodes (14): CLAUDE.md Behavioral Guidelines (article), Extend Claude with skills (article), The Twelve-Factor App (article), Adam Wiggins, AI Layer (Harness), LLM Coding Behavioral Guidelines, CLAUDE.md, Claude Skills (SKILL.md) (+6 more)

### Community 7 - "Wiki Governance & Editing Policy"
Cohesion: 0.67
Nodes (3): AGENTS.md (agent operating contract), CLAUDE.md (LLM-WIKI schema & operating contract), Remote Rebase-First Editing Policy

## Knowledge Gaps
- **54 isolated node(s):** `Reading Dashboard`, `TIL Index`, `Notes 인덱스`, `Heroku`, `Software-as-a-Service (SaaS)` (+49 more)
  These have ≤1 connection - possible missing edges or undocumented components.
- **13 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `02.wiki/log.md (chronological work log)` connect `LLM Harness & Code Understanding` to `Actix Web Knowledge (Wiki)`, `Anthropic Cyber-Security & Auto Mode`, `LLM Wiki & Karpathy Lineage`?**
  _High betweenness centrality (0.293) - this node is a cross-community bridge._
- **Why does `Claude Code` connect `LLM Harness & Code Understanding` to `Anthropic Cyber-Security & Auto Mode`, `LLM Wiki & Karpathy Lineage`, `CLAUDE.md, Skills & 12-Factor`?**
  _High betweenness centrality (0.129) - this node is a cross-community bridge._
- **Why does `Actix Web` connect `Actix Web Knowledge (Wiki)` to `LLM Harness & Code Understanding`, `Actix Web Reference Docs`?**
  _High betweenness centrality (0.097) - this node is a cross-community bridge._
- **Are the 2 inferred relationships involving `Agent Harness Design` (e.g. with `Harness Engineering` and `Harness design for long-running application development (article)`) actually correct?**
  _`Agent Harness Design` has 2 INFERRED edges - model-reasoned connections that need verification._
- **What connects `Reading Dashboard`, `TIL Index`, `Notes 인덱스` to the rest of the system?**
  _54 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `LLM Harness & Code Understanding` be split into smaller, more focused modules?**
  _Cohesion score 0.13 - nodes in this community are weakly interconnected._
- **Should `Actix Web Reference Docs` be split into smaller, more focused modules?**
  _Cohesion score 0.08 - nodes in this community are weakly interconnected._
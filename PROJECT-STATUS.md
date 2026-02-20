# ASO Agent System - Project Status

**Version:** 1.4.1
**Status:** Production Ready

---

## What This Is

A multi-agent ASO system for Claude Code that produces actionable, copy-paste ready deliverables for App Store and Google Play optimization.

## Components

| Component | Location | Description |
|-----------|----------|-------------|
| Core Skill | `app-store-optimization/` | 10 Python modules + data fetching (single source of truth) |
| Agents | `.claude/agents/aso/` | 6 agents + shared protocol |
| Commands | `.claude/commands/aso/` | 4 slash commands |
| Templates | `.claude/templates/` | 6 output templates |
| Documentation | `.claude/ARCHITECTURE.md`, `.claude/USAGE.md` | Architecture + usage guide |
| Example | `outputs/FitFlow-example/` | Demo output with quality standards |

## Agent System

- **aso-master** — orchestrator (opus)
- **aso-research** — keyword + competitor research via iTunes API (opus)
- **aso-metadata** — metadata generation with character validation (sonnet)
- **aso-creative** — visual assets, CPPs, A/B testing strategy (sonnet)
- **aso-launch** — pre-launch checklist + launch timeline (opus)
- **aso-ongoing** — review templates, event calendar, ongoing tasks (opus)

Workflow: master → research → metadata → creative → launch → ongoing → master (synthesis)
Output: 15 files in `outputs/[app-name]/`

## Data Sources

- **iTunes Search API** (free, tested) — competitor metadata, ratings, screenshots
- **WebFetch scraping** (fallback) — additional app store data
- **User-provided** (last resort) — search volumes, rankings, conversion rates

## Known Limitations

- iTunes API has no keyword search volumes (estimated via benchmarks)
- No keyword ranking data (must be tracked manually)
- No download numbers (estimated only)
- WebFetch is slower and structure-dependent

## Version History

- **v1.0** (Nov 2025) — Initial release: 4 agents, 6 templates, 17-file output
- **v1.1** (Feb 2026) — Restructure: eliminated 17 duplicate files, rewrote agents to principle-based style (-79% lines), simplified to 11-file output, consolidated documentation
- **v1.2** (Feb 2026) — CPPs, In-App Events, visual asset optimization, Apple Search Ads readiness, category strategy, conversion funnel analysis
- **v1.3** (Feb 2026) — Split overloaded agents (4 → 6 specialists), progress heartbeat system
- **v1.4** (Feb 2026) — ASO Playbook, PDF export support, 15-file output
- **v1.4.1** (Feb 2026) — Plugin system support, SKILL.md compliance

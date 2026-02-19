# CLAUDE.md

This file provides guidance to Claude Code when working with this repository.

## Repository Purpose

A **Claude Code skill + agent system** for App Store Optimization (ASO). Provides keyword research, metadata generation, competitor analysis, and launch planning for Apple App Store and Google Play Store.

## Quick Start

```bash
# Install agents (user-level)
cp .claude/agents/aso/*.md ~/.claude/agents/

# Install slash commands
cp .claude/commands/aso/*.md ~/.claude/commands/

# Run a full audit
/aso-full-audit MyApp
```

## Architecture Overview

Single source of truth: `app-store-optimization/` (distributable skill package).

```
app-store-optimization/     # 10 Python modules + lib/ data fetching
.claude/agents/aso/          # 4 agent definitions + shared protocol
.claude/commands/aso/        # 4 slash commands (thin wrappers)
.claude/templates/           # 5 output templates
outputs/[app-name]/          # Generated deliverables (13 files)
```

See `.claude/ARCHITECTURE.md` for the full data flow diagram and layer breakdown.

## Core Modules

All in `app-store-optimization/`:

| Module | Purpose | Key Functions |
|--------|---------|---------------|
| `keyword_analyzer.py` | Keyword research | `analyze_keyword()`, `find_long_tail_opportunities()` |
| `metadata_optimizer.py` | Title/description + visual strategy | `optimize_title()`, `validate_character_limits()`, `generate_screenshot_strategy()` |
| `competitor_analyzer.py` | Competitor gap analysis | `analyze_competitor()`, `identify_gaps()` |
| `aso_scorer.py` | ASO health score + category/funnel | `calculate_overall_score()`, `analyze_category_fit()`, `analyze_conversion_funnel()` |
| `ab_test_planner.py` | A/B testing strategy | `design_test()`, `calculate_significance()` |
| `localization_helper.py` | Multi-language optimization | `identify_target_markets()` |
| `review_analyzer.py` | Review sentiment analysis | `analyze_sentiment()`, `extract_common_themes()` |
| `launch_checklist.py` | Pre-launch validation | `generate_prelaunch_checklist()` |
| `cpp_planner.py` | Custom Product Pages strategy | `identify_cpp_opportunities()`, `generate_cpp_spec()` |
| `event_planner.py` | In-App Events planning | `plan_event_calendar()`, `generate_event_metadata()` |

**Data fetching** in `app-store-optimization/lib/`:
- `itunes_api.py` — iTunes Search API wrapper (free, no auth)
- `scraper.py` — WebFetch prompt utilities
- `scraping-guide.md` — Scraping examples and patterns
- `data_sources.md` — API limitations and fallback strategies

## Platform Constraints

**Apple App Store:** Title 30, Subtitle 30, Promo Text 170, Keywords 100, Description 4000
**Google Play Store:** Title 50, Short Description 80, Full Description 4000
**Apple In-App Events:** Name 30, Short Desc 50, Long Desc 120 (max 10 events, 5 simultaneous)
**Apple CPPs:** Promo Text 170 per CPP, up to 70 CPPs per app

These limits are enforced by agents via shared-protocol.md and validated in metadata outputs.

## Agent System

4 agents coordinated sequentially:

| Agent | Role | Model |
|-------|------|-------|
| `aso-master` | Orchestrator — intake, coordination, synthesis | opus |
| `aso-research` | Keyword + competitor research via iTunes API | opus |
| `aso-optimizer` | Copy-paste metadata generation with validation | sonnet |
| `aso-strategist` | Timelines, checklists, review templates | opus |

**Workflow:** aso-master → aso-research → aso-optimizer → aso-strategist → aso-master (synthesis)

**Shared protocol:** `.claude/agents/aso/shared-protocol.md` — common rules all agents follow (output conventions, character limits reference, quality standards, communication patterns).

## Slash Commands

| Command | Agent | Time |
|---------|-------|------|
| `/aso-full-audit [app]` | aso-master (all specialists) | 30-40 min |
| `/aso-optimize [app]` | aso-optimizer directly | 5-7 min |
| `/aso-prelaunch [app] [date]` | aso-strategist directly | 8-10 min |
| `/aso-competitor [app] [competitors]` | aso-research directly | 10-15 min |

## Output Structure (13 files)

```
outputs/[app-name]/
├── 00-MASTER-ACTION-PLAN.md
├── 01-research/
│   ├── keyword-list.md
│   └── competitor-gaps.md
├── 02-metadata/
│   ├── apple-metadata.md
│   ├── google-metadata.md
│   ├── visual-assets-spec.md
│   └── custom-product-pages.md
├── 03-testing/
│   └── ab-test-setup.md
├── 04-launch/
│   ├── prelaunch-checklist.md
│   └── timeline.md
├── 05-optimization/
│   ├── review-responses.md
│   ├── ongoing-tasks.md
│   └── event-calendar.md
└── FINAL-REPORT.md
```

## Templates

`.claude/templates/` contains 5 output structure templates referenced by agents:

- `master-action-plan-template.md` — master checklist with per-phase tasks
- `apple-metadata-template.md` — App Store Connect metadata format
- `google-metadata-template.md` — Play Console metadata format
- `timeline-template.md` — Week-by-week timeline with real dates
- `review-responses-template.md` — Review response categories and templates

## Development Guidelines

- **Zero external dependencies** — Python 3.7+ standard library only
- **Always validate character limits** — use platform constraints above
- **Real calendar dates** — never "Week 1" placeholders
- **Copy-paste ready outputs** — no additional formatting needed
- **Sequential agent execution** — research → optimization → strategy (data dependencies)
- **All outputs** go to `outputs/[app-name]/`, never project root
- **Read agent definitions** before modifying — they contain detailed protocols

## Testing

```bash
cd app-store-optimization
python3 lib/itunes_api.py    # iTunes API integration test
python3 keyword_analyzer.py  # Module syntax check
```

## Key Files

| File | Purpose |
|------|---------|
| `.claude/ARCHITECTURE.md` | System architecture and data flow |
| `.claude/USAGE.md` | Installation and usage guide |
| `app-store-optimization/README.md` | Skill documentation |
| `outputs/FitFlow-example/` | Example output demonstrating quality standards |
| `CHANGELOG.md` | Version history |

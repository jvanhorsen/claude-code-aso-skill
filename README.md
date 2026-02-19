# App Store Optimization (ASO) Agent System for Claude Code

<div align="center">

![Version](https://img.shields.io/badge/version-1.2.0-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)
![Claude Code](https://img.shields.io/badge/Claude_Code-Compatible-purple.svg)
![Claude App](https://img.shields.io/badge/Claude_App-Compatible-orange.svg)
![Status](https://img.shields.io/badge/status-production_ready-success.svg)

**Professional App Store Optimization powered by AI agents**

[Features](#-features) | [Installation](#-installation) | [Quick Start](#-quick-start) | [Documentation](#-documentation) | [Examples](#-example-outputs)

</div>

---

## Overview

A production-ready multi-agent ASO system for **Claude Code** that generates **actionable, copy-paste ready deliverables** for Apple App Store and Google Play Store optimization. Real-time data via iTunes Search API, character-validated metadata, Custom Product Pages (CPPs), In-App Events planning, visual asset optimization, Apple Search Ads strategy, category analysis, conversion funnel diagnosis, and executable checklists with specific calendar dates.

**Two ways to use:**
- **Claude Code CLI** — Full multi-agent system with automated workflows
- **Claude Desktop/Web App** — Standalone skill for conversational ASO analysis

---

## Features

### Multi-Agent System

4 specialized agents coordinated sequentially:

| Agent | Role | Model |
|-------|------|-------|
| **aso-master** | Orchestrator — intake, coordination, synthesis | Opus |
| **aso-research** | Keyword + competitor research via iTunes API | Opus |
| **aso-optimizer** | Metadata generation with character validation | Sonnet |
| **aso-strategist** | Timelines, checklists, review templates | Opus |

### Data Integration

- **iTunes Search API** — Free, official Apple API for competitor metadata and ratings
- **WebFetch Utilities** — Additional scraping for comprehensive analysis
- **Character Validation** — Apple (30/30/170/100/4000) and Google (50/80/4000) limits enforced

### v1.2 Enhancements

- **Custom Product Pages (CPPs)** — Strategy, promotional text variants, priority scoring (5.9% avg CVR lift)
- **In-App Events** — Seasonal calendar, event metadata generation, badge type recommendations
- **Visual Asset Optimization** — Screenshot strategy framework, first-3-screenshot CVR optimization, text overlay guidelines
- **Apple Search Ads Readiness** — Organic vs paid keyword strategy, CPP+Ads integration, budget framework
- **Category Strategy** — Primary/secondary category optimization, competition density analysis
- **Conversion Funnel Analysis** — Stage-by-stage diagnosis, bottleneck identification, benchmark comparison

### Deliverables (13 files per audit)

```
outputs/[YourApp]/
├── 00-MASTER-ACTION-PLAN.md      # START HERE - consolidated roadmap
├── 01-research/
│   ├── keyword-list.md           # Prioritized keywords with implementation guide
│   └── competitor-gaps.md        # Competitive opportunities
├── 02-metadata/
│   ├── apple-metadata.md         # Copy-paste ready for App Store Connect
│   ├── google-metadata.md        # Copy-paste ready for Play Console
│   ├── visual-assets-spec.md     # Icon/screenshot requirements
│   └── custom-product-pages.md   # CPP strategy and specifications
├── 03-testing/
│   └── ab-test-setup.md          # A/B test configuration
├── 04-launch/
│   ├── prelaunch-checklist.md    # Validation checklist
│   └── timeline.md               # Week-by-week with specific dates
├── 05-optimization/
│   ├── review-responses.md       # Pre-written response templates
│   ├── ongoing-tasks.md          # Daily/weekly/monthly schedule
│   └── event-calendar.md         # In-App Events strategy and calendar
└── FINAL-REPORT.md               # Executive summary
```

### Slash Commands

| Command | Agent | Time |
|---------|-------|------|
| `/aso-full-audit [app]` | aso-master (all specialists) | 30-40 min |
| `/aso-optimize [app]` | aso-optimizer directly | 5-7 min |
| `/aso-prelaunch [app] [date]` | aso-strategist directly | 8-10 min |
| `/aso-competitor [app] [competitors]` | aso-research directly | 10-15 min |

---

## Installation

### Option 1: Claude Code (Full Multi-Agent System) — Recommended

```bash
# Clone repository
git clone https://github.com/alirezarezvani/claude-code-aso-skill.git
cd claude-code-aso-skill

# Install agents (user-level)
cp .claude/agents/aso/*.md ~/.claude/agents/

# Install slash commands (optional)
cp .claude/commands/aso/*.md ~/.claude/commands/

# Verify installation
claude --list-agents | grep aso
```

### Option 2: Claude Desktop/Web App (Standalone Skill)

1. Download `app-store-optimization.zip` from the repository
2. Open Claude Desktop or Web App settings
3. Navigate to **Capabilities** and upload the ZIP
4. Start a conversation referencing the skill

### Option 3: Manual Installation

```bash
unzip app-store-optimization.zip
cp -r app-store-optimization ~/.claude/skills/
```

See [USAGE.md](.claude/USAGE.md) for detailed installation instructions and all workflows.

---

## Quick Start

### Full ASO Audit
```bash
claude
/aso-full-audit MyAwesomeApp
# Review: outputs/MyAwesomeApp/00-MASTER-ACTION-PLAN.md
```

### Quick Metadata Refresh
```bash
/aso-optimize MyApp
# Output: outputs/MyApp/02-metadata/
```

### Pre-Launch Checklist
```bash
/aso-prelaunch MyApp 2026-04-01
# Output: outputs/MyApp/04-launch/ and 05-optimization/
```

### Competitive Intelligence
```bash
/aso-competitor MyApp "Todoist,Any.do,Microsoft To Do"
# Output: outputs/MyApp/01-research/
```

---

## Quality Standards

All outputs meet these standards:

- **Character Limits Validated** — Apple title/subtitle 30, keywords 100; Google title 50, short desc 80
- **Real Dates** — Specific calendar dates, never "Week 1" placeholders
- **Copy-Paste Ready** — Pre-validated, no additional formatting needed
- **Actionable Tasks** — Checkbox format with success criteria and validation methods

---

## Example Outputs

See the complete example for a fictional fitness app: **[FitFlow Example](outputs/FitFlow-example/)**

---

## Architecture

```
app-store-optimization/     # 10 Python modules + lib/ data fetching (single source of truth)
.claude/agents/aso/          # 4 agent definitions + shared protocol
.claude/commands/aso/        # 4 slash commands (thin wrappers)
.claude/templates/           # 5 output templates
outputs/[app-name]/          # Generated deliverables (13 files)
```

See [ARCHITECTURE.md](.claude/ARCHITECTURE.md) for the full system design and data flow.

---

## Documentation

| Document | Description |
|----------|-------------|
| [ARCHITECTURE.md](.claude/ARCHITECTURE.md) | System architecture and data flow |
| [USAGE.md](.claude/USAGE.md) | Installation guide and usage workflows |
| [CLAUDE.md](CLAUDE.md) | Quick reference for Claude instances |
| [Implementation Plan](documentation/implementation/aso-agents-implementation-plan.md) | Original development plan |
| [Data Sources](app-store-optimization/lib/data_sources.md) | API documentation and limitations |

---

## Testing

### iTunes API Integration

```bash
cd app-store-optimization && python3 lib/itunes_api.py
```

### Module Syntax Check

```bash
cd app-store-optimization
python3 keyword_analyzer.py
python3 metadata_optimizer.py
```

---

## Tech Stack

- **Language:** Python 3.7+ (zero external dependencies)
- **AI Framework:** Claude Code agents (Opus + Sonnet models)
- **Data Sources:** iTunes Search API, WebFetch
- **Output Format:** Markdown
- **Platform Support:** macOS, Linux, Windows

---

## Contributing

Contributions welcome! See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

### Areas for Contribution

1. **Additional Data Sources** — Paid ASO API integrations (AppTweak, Sensor Tower)
2. **Localization** — Multi-language metadata generation and regional keyword research
3. **Enhanced Analytics** — Keyword ranking trends, ASO score progression tracking
4. **Documentation** — Additional use cases, video tutorials

---

## License

MIT License — see [LICENSE.md](LICENSE.md) for details.

---

## Support

- **Documentation:** [USAGE.md](.claude/USAGE.md)
- **Examples:** [FitFlow example](outputs/FitFlow-example/)
- **Issues:** [GitHub Issues](https://github.com/alirezarezvani/claude-code-aso-skill/issues)

---

## Status

- **Current Version:** 1.2.0
- **Status:** Production Ready
- **Maintenance:** Actively maintained

## Roadmap

### Version 1.0 (November 2025)
- [x] Multi-agent system with orchestration
- [x] iTunes API integration
- [x] Copy-paste ready metadata
- [x] Complete documentation and example workflow

### Version 1.1 (February 2026)
- [x] Architecture restructure — eliminated duplicates, principle-based agents, simplified outputs

### Version 1.2 (February 2026)
- [x] Custom Product Pages (CPPs) — strategy module with opportunity identification and spec generation
- [x] In-App Events — seasonal event calendar and metadata generation
- [x] Visual asset optimization — screenshot strategy framework with CVR-focused first-3-screenshot guidance
- [x] Apple Search Ads readiness — organic vs paid keyword strategy and budget framework
- [x] Category strategy — primary/secondary category optimization and competition density analysis
- [x] Conversion funnel analysis — stage-by-stage diagnosis with bottleneck identification

### Version 2.0 (Future)
- [ ] Paid API integration (AppTweak, Sensor Tower)
- [ ] Semantic keyword clustering
- [ ] Web dashboard for tracking
- [ ] Multi-language expansion support

---

<div align="center">

**Built with Claude Code**

[Back to Top](#app-store-optimization-aso-agent-system-for-claude-code)

</div>

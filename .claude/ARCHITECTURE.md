# ASO Agent System Architecture

**Project:** aso-skill
**Updated:** February 2026

---

## System Overview

```
User Request → Slash Command → aso-master (orchestrator)
    → aso-research → aso-optimizer → aso-strategist
    → Synthesis → outputs/[app-name]/
```

Single source of truth: `app-store-optimization/` contains all Python modules and data fetching utilities. Agents reference this directory directly.

---

## Architecture Layers

### Layer 1: Core Skill (Distributable)

**Location:** `app-store-optimization/`

```
app-store-optimization/
├── SKILL.md                      # Skill definition for Claude Code
├── keyword_analyzer.py           # Keyword research module
├── competitor_analyzer.py        # Competitor intelligence
├── metadata_optimizer.py         # Metadata + visual asset optimization
├── aso_scorer.py                 # ASO health scoring + category/funnel analysis
├── ab_test_planner.py            # A/B testing strategy
├── localization_helper.py        # Multi-language optimization
├── review_analyzer.py            # Review sentiment analysis
├── launch_checklist.py           # Pre-launch validation
├── cpp_planner.py                # Custom Product Pages strategy
├── event_planner.py              # In-App Events planning
└── lib/                          # Data fetching utilities
    ├── itunes_api.py             # iTunes Search API wrapper
    ├── scraper.py                # WebFetch utilities
    └── data_sources.md           # Data source documentation
```

**Installation:** `cp -r app-store-optimization ~/.claude/skills/`

---

### Layer 2: Agent Definitions

**Location:** `.claude/agents/aso/`

```
.claude/agents/aso/
├── shared-protocol.md            # Common rules for all agents
├── aso-master.md                 # Orchestrator (opus)
├── aso-research.md               # Research + data fetching (opus)
├── aso-optimizer.md              # Metadata generation (sonnet)
└── aso-strategist.md             # Strategy + timelines (opus)
```

**Workflow:**
```
aso-master
    ↓
Phase 1: aso-research
    - Uses: app-store-optimization/keyword_analyzer.py
    - Uses: app-store-optimization/competitor_analyzer.py
    - Uses: app-store-optimization/aso_scorer.py (category analysis)
    - Fetches: iTunes API data
    - Output: keyword-list.md, competitor-gaps.md
    - Includes: Apple Search Ads keyword categorization, category positioning
    ↓
Phase 2: aso-optimizer
    - Uses: app-store-optimization/metadata_optimizer.py (metadata + visual strategy)
    - Uses: app-store-optimization/ab_test_planner.py
    - Uses: app-store-optimization/cpp_planner.py
    - Output: apple-metadata.md, google-metadata.md, custom-product-pages.md
    ↓
Phase 3: aso-strategist
    - Uses: app-store-optimization/aso_scorer.py (health + funnel)
    - Uses: app-store-optimization/launch_checklist.py
    - Uses: app-store-optimization/event_planner.py
    - Output: timeline.md, prelaunch-checklist.md, event-calendar.md
    ↓
aso-master (synthesis)
    - Output: 00-MASTER-ACTION-PLAN.md (includes Apple Search Ads Readiness)
```

---

### Layer 3: Slash Commands

**Location:** `.claude/commands/aso/`

| Command | Agent | Duration |
|---------|-------|----------|
| `/aso-full-audit [app]` | aso-master (all 3 specialists) | 30-40 min |
| `/aso-optimize [app]` | aso-optimizer | 5-7 min |
| `/aso-prelaunch [app] [date]` | aso-strategist | 8-10 min |
| `/aso-competitor [app] [competitors]` | aso-research | 10-15 min |

---

### Layer 4: Templates

**Location:** `.claude/templates/`

Templates provide output structure for agents. Agents reference them rather than embedding templates inline.

---

### Layer 5: Output Structure

**Location:** `outputs/[app-name]/`

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

---

## Data Flow

```
┌──────────────┐
│ User Request │
└──────┬───────┘
       ↓
┌──────────────────────────┐
│ Slash Command            │
│ /aso-full-audit MyApp    │
└──────┬───────────────────┘
       ↓
┌────────────────────────────────────────────────┐
│ aso-master (Orchestrator)                      │
│ - Gathers app details from user                │
│ - Invokes specialist agents sequentially       │
└────────┬───────────────────────────────────────┘
         ↓
┌────────────────────────────────────────────────┐
│ Phase 1: aso-research                          │
│ iTunes API → keyword_analyzer.py               │
│ iTunes API → competitor_analyzer.py            │
│ aso_scorer.py → category analysis              │
│ → outputs/[app]/01-research/                   │
│ (incl. Apple Search Ads keyword strategy)      │
└────────┬───────────────────────────────────────┘
         ↓
┌────────────────────────────────────────────────┐
│ Phase 2: aso-optimizer                         │
│ Keywords from Phase 1 → metadata_optimizer.py  │
│ metadata_optimizer.py → screenshot strategy    │
│ cpp_planner.py → Custom Product Pages          │
│ → outputs/[app]/02-metadata/                   │
└────────┬───────────────────────────────────────┘
         ↓
┌────────────────────────────────────────────────┐
│ Phase 3: aso-strategist                        │
│ All prior outputs → aso_scorer.py              │
│ aso_scorer.py → conversion funnel analysis     │
│ event_planner.py → In-App Events calendar      │
│ → outputs/[app]/04-launch/                     │
│ → outputs/[app]/05-optimization/               │
└────────┬───────────────────────────────────────┘
         ↓
┌────────────────────────────────────────────────┐
│ aso-master (Synthesis)                         │
│ → outputs/[app]/00-MASTER-ACTION-PLAN.md       │
│ → outputs/[app]/FINAL-REPORT.md                │
└────────────────────────────────────────────────┘
```

---

## Key Integration Points

### Agent → Python Module

```bash
cd app-store-optimization
python3 keyword_analyzer.py < /tmp/keyword_input.json > /tmp/keyword_output.json
```

### Skill → iTunes API

```python
# In app-store-optimization/lib/itunes_api.py
api = iTunesAPI()
competitors = api.compare_competitors(["Todoist", "Any.do", "Microsoft To Do"])
```

---

## Installation

```bash
# Install agents
cp .claude/agents/aso/*.md ~/.claude/agents/

# Install commands (optional)
cp .claude/commands/aso/*.md ~/.claude/commands/

# Use
/aso-full-audit MyApp
```

---

**See Also:**
- `documentation/implementation/aso-agents-implementation-plan.md` - Implementation plan
- `CLAUDE.md` - Complete project reference

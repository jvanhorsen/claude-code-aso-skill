# ASO Agent System Architecture

**Project:** aso-skill
**Updated:** February 2026

---

## System Overview

```
User Request → Slash Command → aso-master (orchestrator)
    → aso-research → aso-metadata → aso-creative → aso-launch → aso-ongoing
    → Synthesis + Heartbeat → outputs/[app-name]/
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
├── aso-master.md                 # Orchestrator + heartbeat (opus)
├── aso-research.md               # Research + data fetching (opus)
├── aso-metadata.md               # Apple + Google metadata (sonnet)
├── aso-creative.md               # Visuals, CPPs, A/B testing (sonnet)
├── aso-launch.md                 # Pre-launch checklist + timeline (opus)
└── aso-ongoing.md                # Reviews, events, ongoing tasks (opus)
```

**Design principle:** Max 3 output files per specialist agent to prevent turn budget exhaustion.

**Workflow (5 phases + heartbeat):**
```
aso-master (intake)
    ↓
Phase 1: aso-research (2 files)
    - Uses: keyword_analyzer.py, competitor_analyzer.py, aso_scorer.py
    - Fetches: iTunes API data
    - Output: keyword-list.md, competitor-gaps.md
    - Includes: Apple Search Ads keyword categorization, category positioning
    ↓ heartbeat
Phase 2: aso-metadata (2 files)
    - Uses: metadata_optimizer.py
    - Output: apple-metadata.md, google-metadata.md
    ↓ heartbeat
Phase 3: aso-creative (3 files)
    - Uses: metadata_optimizer.py (visual strategy), cpp_planner.py, ab_test_planner.py
    - Reads: apple-metadata.md, google-metadata.md (for final titles/keywords)
    - Output: visual-assets-spec.md, custom-product-pages.md, ab-test-setup.md
    ↓ heartbeat
Phase 4: aso-launch (2 files)
    - Uses: launch_checklist.py, aso_scorer.py (conversion funnel)
    - Output: prelaunch-checklist.md, timeline.md
    ↓ heartbeat
Phase 5: aso-ongoing (3 files)
    - Uses: event_planner.py, review_analyzer.py, aso_scorer.py
    - Output: review-responses.md, event-calendar.md, ongoing-tasks.md
    ↓ heartbeat
aso-master (synthesis)
    - Output: 00-MASTER-ACTION-PLAN.md, FINAL-REPORT.md, PLAYBOOK.md
    ↓ final heartbeat (15/15 files complete)
```

---

### Layer 3: Slash Commands

**Location:** `.claude/commands/aso/`

| Command | Agent(s) | Duration |
|---------|----------|----------|
| `/aso-full-audit [app]` | aso-master (all 5 specialists) | 30-40 min |
| `/aso-optimize [app]` | aso-metadata | 3-5 min |
| `/aso-prelaunch [app] [date]` | aso-launch + aso-ongoing | 10-14 min |
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
├── FINAL-REPORT.md
└── PLAYBOOK.md
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
│ - Invokes 5 specialists sequentially           │
│ - Prints heartbeat after each phase            │
└────────┬───────────────────────────────────────┘
         ↓
┌────────────────────────────────────────────────┐
│ Phase 1: aso-research (2 files)                │
│ iTunes API → keyword_analyzer.py               │
│ iTunes API → competitor_analyzer.py            │
│ aso_scorer.py → category analysis              │
│ → outputs/[app]/01-research/                   │
└────────┬───────────────────────────────────────┘
         ↓ heartbeat (2/15 files)
┌────────────────────────────────────────────────┐
│ Phase 2: aso-metadata (2 files)                │
│ Keywords from Phase 1 → metadata_optimizer.py  │
│ → outputs/[app]/02-metadata/                   │
│   (apple-metadata.md, google-metadata.md)      │
└────────┬───────────────────────────────────────┘
         ↓ heartbeat (4/15 files)
┌────────────────────────────────────────────────┐
│ Phase 3: aso-creative (3 files)                │
│ metadata_optimizer.py → screenshot strategy    │
│ cpp_planner.py → Custom Product Pages          │
│ ab_test_planner.py → A/B test setup            │
│ → outputs/[app]/02-metadata/ (visuals, CPPs)   │
│ → outputs/[app]/03-testing/ (A/B tests)        │
└────────┬───────────────────────────────────────┘
         ↓ heartbeat (7/15 files)
┌────────────────────────────────────────────────┐
│ Phase 4: aso-launch (2 files)                  │
│ All prior outputs → launch_checklist.py        │
│ aso_scorer.py → conversion funnel analysis     │
│ → outputs/[app]/04-launch/                     │
└────────┬───────────────────────────────────────┘
         ↓ heartbeat (9/15 files)
┌────────────────────────────────────────────────┐
│ Phase 5: aso-ongoing (3 files)                 │
│ event_planner.py → In-App Events calendar      │
│ review_analyzer.py → review templates          │
│ aso_scorer.py → ongoing schedule               │
│ → outputs/[app]/05-optimization/               │
└────────┬───────────────────────────────────────┘
         ↓ heartbeat (12/15 files)
┌────────────────────────────────────────────────┐
│ aso-master (Synthesis)                         │
│ → outputs/[app]/00-MASTER-ACTION-PLAN.md       │
│ → outputs/[app]/FINAL-REPORT.md                │
│ → outputs/[app]/PLAYBOOK.md                    │
└────────────────────────────────────────────────┘
  ↓ final heartbeat (15/15 files ████████████████)
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

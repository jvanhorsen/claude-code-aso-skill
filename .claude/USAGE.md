# ASO Agent System — Installation & Usage Guide

## Prerequisites

- **Claude Code** CLI installed and configured
- **Python 3.8+** (standard library only — zero external dependencies)
- **Internet connection** (for iTunes Search API)

---

## Installation

### Method A: Clone + Copy (Recommended)

Full multi-agent system with agents, slash commands, and all capabilities:

#### Step 1: Clone the Repository

```bash
git clone https://github.com/jvanhorsen/claude-code-aso-skill.git
cd claude-code-aso-skill
```

#### Step 2: Install Agents

```bash
cp .claude/agents/aso/*.md ~/.claude/agents/
```

This copies 7 files: `shared-protocol.md` + 6 agent definitions (`aso-master`, `aso-research`, `aso-metadata`, `aso-creative`, `aso-launch`, `aso-ongoing`).

#### Step 3: Install Slash Commands

```bash
mkdir -p ~/.claude/commands/aso
cp .claude/commands/aso/*.md ~/.claude/commands/aso/
```

This installs 4 commands: `/aso-full-audit`, `/aso-optimize`, `/aso-prelaunch`, `/aso-competitor`.

#### Step 4: Verify

```bash
ls ~/.claude/agents/aso-* ~/.claude/agents/shared-protocol.md
# Should show 7 files

ls ~/.claude/commands/aso/
# Should show 4 files
```

Restart Claude Code after installation for agents and commands to appear.

### Method B: Manual Skill Installation

For standalone skill usage without the agent system:

```bash
git clone https://github.com/jvanhorsen/claude-code-aso-skill.git
cp -r claude-code-aso-skill/app-store-optimization ~/.claude/skills/
```

---

## Configuration

- **iTunes Search API**: Free, no authentication needed
- **WebFetch**: Built-in Claude Code tool, no setup required
- **Paid ASO tools** (future): Set `APPTWEAK_API_KEY` or `SENSOR_TOWER_API_KEY` environment variables if available

---

## Slash Commands

### `/aso-full-audit [app-name]`

Complete ASO audit with all 5 specialist agents.

**When to use:** New app launch, major ASO overhaul, quarterly comprehensive review.

**Process:** aso-master coordinates research, metadata, creative, launch, and ongoing agents sequentially. Progress updates are printed after each phase.

**Output:** Full `outputs/[app-name]/` directory — 15 files including master action plan, research, metadata, testing, launch, optimization deliverables, final report, and a presentation-ready ASO Playbook.

**Time:** 30-40 minutes (fully automated).

### `/aso-optimize [app-name]`

Quick metadata optimization (skips research and launch planning).

**When to use:** Metadata refresh, A/B test variant generation, updating for new app version.

**Output:** `outputs/[app-name]/02-metadata/`

**Time:** 3-5 minutes.

### `/aso-prelaunch [app-name] [launch-date]`

Pre-launch validation and timeline creation.

**When to use:** Preparing for app submission, need launch checklist and timeline.

**Output:** `outputs/[app-name]/04-launch/` and `outputs/[app-name]/05-optimization/`

**Time:** 10-14 minutes.

### `/aso-competitor [app-name] [competitors]`

Competitive intelligence and gap analysis.

**When to use:** Researching competitors, identifying market opportunities.

**Output:** `outputs/[app-name]/01-research/`

**Time:** 10-15 minutes.

---

## Agent System

6 agents coordinated by aso-master:

| Agent | Role | Model |
|-------|------|-------|
| **aso-master** | Orchestrator — intake, coordination, heartbeat, synthesis | Opus |
| **aso-research** | Keyword + competitor research via iTunes API | Opus |
| **aso-metadata** | Apple + Google metadata generation with validation | Sonnet |
| **aso-creative** | Visual assets, CPPs, A/B testing strategy | Sonnet |
| **aso-launch** | Pre-launch checklist + launch timeline | Opus |
| **aso-ongoing** | Review templates, event calendar, ongoing tasks | Opus |

**Execution order:** research → metadata → creative → launch → ongoing → master (synthesis)

Each phase produces 2-3 output files. A progress heartbeat is printed after each phase completes so you can track the audit's progress.

---

## Typical Workflows

### New App Launch

```
# 1. Run full audit (4-6 weeks before submission)
/aso-full-audit MyNewApp

# 2. Review strategy
# outputs/MyNewApp/PLAYBOOK.md          <- Presentation-ready overview
# outputs/MyNewApp/00-MASTER-ACTION-PLAN.md  <- Detailed task checklist

# 3. Copy metadata to stores
# outputs/MyNewApp/02-metadata/apple-metadata.md -> App Store Connect
# outputs/MyNewApp/02-metadata/google-metadata.md -> Play Console

# 4. Work through pre-launch checklist
# outputs/MyNewApp/04-launch/prelaunch-checklist.md

# 5. Follow timeline for submission
# outputs/MyNewApp/04-launch/timeline.md
```

### Existing App Optimization

```
# 1. Run full audit to establish baseline
/aso-full-audit ExistingApp

# 2. Review PLAYBOOK.md for strategy overview
# 3. Check FINAL-REPORT.md for ASO health score
# 4. Start with quick wins in master action plan
# 5. Monitor weekly using ongoing-tasks.md schedule
# 6. Re-audit after 3 months to measure improvement
```

### Competitive Intelligence

```
# Analyze specific competitors
/aso-competitor MyApp "Competitor1,Competitor2,Competitor3"

# Review: outputs/MyApp/01-research/competitor-gaps.md
# Look for: keyword gaps, messaging weaknesses, differentiation opportunities
```

### A/B Testing

```
# Generate test variants
/aso-optimize MyApp

# Review: outputs/MyApp/03-testing/ab-test-setup.md
# Follow step-by-step guide for App Store Connect / Play Console
```

---

## Using Agents Directly

Beyond slash commands, you can invoke agents directly for custom workflows:

```
"Invoke aso-master with a custom workflow: research for keywords 'fitness' and
'workout', metadata for Apple only, skip the testing phase."
```

```
"Invoke aso-research to analyze the top 10 apps in the 'productivity' category
and identify keyword opportunities."
```

```
"Invoke aso-metadata to generate Apple metadata using these keywords: [list]"
```

```
"Invoke aso-launch to create a launch timeline for my app submission on
March 15, 2026."
```

---

## Output Structure (15 files per full audit)

```
outputs/[app-name]/
├── 00-MASTER-ACTION-PLAN.md       # Detailed task checklist with timelines
├── 01-research/
│   ├── keyword-list.md            # Prioritized keywords (organic vs paid)
│   └── competitor-gaps.md         # Competitive opportunities + category positioning
├── 02-metadata/
│   ├── apple-metadata.md          # Copy-paste for App Store Connect
│   ├── google-metadata.md         # Copy-paste for Play Console
│   ├── visual-assets-spec.md      # Icon/screenshot requirements
│   └── custom-product-pages.md    # CPP strategy and promotional text variants
├── 03-testing/
│   └── ab-test-setup.md           # A/B test configuration with hypotheses
├── 04-launch/
│   ├── prelaunch-checklist.md     # Validation checklist (7 categories)
│   └── timeline.md                # Calendar dates with milestones
├── 05-optimization/
│   ├── review-responses.md        # Review reply templates
│   ├── ongoing-tasks.md           # Daily/weekly/monthly maintenance schedule
│   └── event-calendar.md          # In-App Events strategy and 6-month calendar
├── FINAL-REPORT.md                # Executive summary + conversion funnel analysis
└── PLAYBOOK.md                    # Presentation-ready ASO strategy (PDF-exportable)
```

### Exporting the Playbook to PDF

The `PLAYBOOK.md` file is designed for clean PDF export:

**Using pandoc:**
```bash
pandoc outputs/MyApp/PLAYBOOK.md -o ASO-Playbook-MyApp.pdf \
  --pdf-engine=xelatex -V geometry:margin=1in -V fontsize=11pt
```

**Using Chrome:** Open in any Markdown viewer → Print → Save as PDF

**Using VS Code:** Install "Markdown PDF" extension → Command Palette → "Markdown PDF: Export (pdf)"

---

## Best Practices

1. **Start with full audit** even if you think you only need metadata — research informs better optimization.
2. **Follow the master plan sequentially** — it's ordered by priority and dependency.
3. **Use real competitor names** when prompted — agents fetch real data via iTunes API.
4. **Re-run audits quarterly** to refresh keywords, competitive intelligence, and ASO score.
5. **Always have an A/B test running** — continuous testing is key to ASO improvement.
6. **Use ongoing-tasks.md** for daily/weekly/monthly maintenance cadence.
7. **Set up Custom Product Pages early** — most top apps don't use CPPs yet; early adoption is a competitive advantage.
8. **Plan In-App Events 2+ weeks ahead** — Apple requires review time; use event-calendar.md for seasonal planning.
9. **Categorize keywords for organic vs paid** — keyword-list.md includes Apple Search Ads readiness guidance.
10. **Monitor your conversion funnel** — aso_scorer.py can diagnose bottlenecks at each stage.

---

## Updating

```bash
cd claude-code-aso-skill
git pull
cp .claude/agents/aso/*.md ~/.claude/agents/
cp .claude/commands/aso/*.md ~/.claude/commands/aso/
```

## Uninstalling
```bash
rm ~/.claude/agents/aso-*.md ~/.claude/agents/shared-protocol.md
rm -rf ~/.claude/commands/aso/
rm -rf ~/.claude/skills/app-store-optimization  # if installed
```

---

## Troubleshooting

**Agents not showing up:** Verify files exist at `~/.claude/agents/aso-*` and restart Claude Code.

**Slash commands not working:** Verify files exist at `~/.claude/commands/aso/` and restart Claude Code.

**iTunes API not responding:** Test with `curl "https://itunes.apple.com/search?term=todoist&entity=software&limit=1"`. If it fails, check internet connection.

**Metadata exceeds character limits:** This shouldn't happen (agents validate), but verify with `echo -n "text" | wc -c`.

**Competitor data not found:** Verify exact app name spelling from the App Store. Provide manual data as fallback.

**Agent prompts for unknown data:** Say "Unknown" or "Not tracked yet" — agents will use industry benchmarks and label them as estimates.

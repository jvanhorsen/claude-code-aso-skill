# ASO Agent System — Installation & Usage Guide

## Installation

### Prerequisites

- Claude Code CLI installed and configured
- Python 3.8+ (for skill Python modules)
- Internet connection (for iTunes API)

### Install Agents

```bash
# Copy agent definitions
cp .claude/agents/aso/*.md ~/.claude/agents/

# Copy slash commands
cp .claude/commands/aso/*.md ~/.claude/commands/

# Verify
ls ~/.claude/agents/aso-*
# Should show: aso-master.md, aso-research.md, aso-optimizer.md, aso-strategist.md
```

### Install Standalone Skill (Optional)

For direct Python module usage without agents:

```bash
cp -r app-store-optimization ~/.claude/skills/
```

### Configuration

- **iTunes Search API**: Free, no authentication needed
- **WebFetch**: Built-in Claude Code tool, no setup required
- **Paid ASO tools** (future): Set `APPTWEAK_API_KEY` or `SENSOR_TOWER_API_KEY` environment variables if available

### Updating

```bash
# Re-copy agents from latest source
cp .claude/agents/aso/*.md ~/.claude/agents/
cp .claude/commands/aso/*.md ~/.claude/commands/
```

### Uninstalling

```bash
rm ~/.claude/agents/aso-*.md
rm ~/.claude/commands/aso-*.md
rm -rf ~/.claude/skills/app-store-optimization  # if installed
```

---

## Slash Commands

### `/aso-full-audit [app-name]`

Complete ASO audit with all 3 specialist agents.

**When to use:** New app launch, major ASO overhaul, quarterly comprehensive review.

**Process:** aso-master coordinates research, optimization, and strategy agents sequentially.

**Output:** Full `outputs/[app-name]/` directory with master plan, research, metadata, testing, launch, and optimization deliverables.

**Time:** 30-40 minutes.

### `/aso-optimize [app-name]`

Quick metadata optimization (skips research and launch planning).

**When to use:** Metadata refresh, A/B test variant generation, updating for new app version.

**Output:** `outputs/[app-name]/02-metadata/`

**Time:** 5-7 minutes.

### `/aso-prelaunch [app-name] [launch-date]`

Pre-launch validation and timeline creation.

**When to use:** Preparing for app submission, need launch checklist and timeline.

**Output:** `outputs/[app-name]/04-launch/` and `outputs/[app-name]/05-optimization/`

**Time:** 8-10 minutes.

### `/aso-competitor [app-name] [competitors]`

Competitive intelligence and gap analysis.

**When to use:** Researching competitors, identifying market opportunities.

**Output:** `outputs/[app-name]/01-research/`

**Time:** 10-15 minutes.

---

## Typical Workflows

### New App Launch

```bash
# 1. Run full audit
/aso-full-audit MyNewApp

# 2. Review master plan
# outputs/MyNewApp/00-MASTER-ACTION-PLAN.md  <- START HERE

# 3. Copy metadata to stores
# outputs/MyNewApp/02-metadata/apple-metadata.md -> App Store Connect
# outputs/MyNewApp/02-metadata/google-metadata.md -> Play Console

# 4. Work through pre-launch checklist
# outputs/MyNewApp/04-launch/prelaunch-checklist.md

# 5. Follow timeline for submission
# outputs/MyNewApp/04-launch/timeline.md
```

### Existing App Optimization

```bash
# 1. Run full audit to establish baseline
/aso-full-audit ExistingApp

# 2. Check FINAL-REPORT.md for ASO health score
# 3. Start with quick wins in master plan
# 4. Monitor weekly using ongoing-tasks.md schedule
# 5. Re-audit after 3 months to measure improvement
```

### Competitive Intelligence

```bash
# Analyze specific competitors
/aso-competitor MyApp "Competitor1,Competitor2,Competitor3"

# Review: outputs/MyApp/01-research/competitor-gaps.md
# Look for: keyword gaps, messaging weaknesses, differentiation opportunities
```

### A/B Testing

```bash
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
"Invoke aso-optimizer to generate metadata using these keywords: [list]"
```

```
"Invoke aso-strategist to create a launch timeline for my app submission on
March 15, 2026."
```

---

## Output Structure

Every `/aso-full-audit` generates:

```
outputs/[app-name]/
├── 00-MASTER-ACTION-PLAN.md       # Start here - consolidated roadmap
├── 01-research/
│   ├── keyword-list.md            # Prioritized keywords
│   └── competitor-gaps.md         # Competitive opportunities
├── 02-metadata/
│   ├── apple-metadata.md          # Copy-paste for App Store Connect
│   ├── google-metadata.md         # Copy-paste for Play Console
│   └── visual-assets-spec.md      # Icon/screenshot requirements
├── 03-testing/
│   └── ab-test-setup.md           # A/B test configuration
├── 04-launch/
│   ├── prelaunch-checklist.md     # Validation checklist
│   └── timeline.md                # Calendar dates
├── 05-optimization/
│   ├── review-responses.md        # Review reply templates
│   └── ongoing-tasks.md           # Maintenance schedule
└── FINAL-REPORT.md                # Executive summary
```

---

## Best Practices

1. **Start with full audit** even if you think you only need metadata — research informs better optimization.
2. **Follow the master plan sequentially** — it's ordered by priority and dependency.
3. **Use real competitor names** when prompted — agents fetch real data via iTunes API.
4. **Re-run audits quarterly** to refresh keywords, competitive intelligence, and ASO score.
5. **Always have an A/B test running** — continuous testing is key to ASO improvement.
6. **Use ongoing-tasks.md** for daily/weekly/monthly maintenance cadence.

---

## Troubleshooting

**Agents not showing up:** Verify files exist at `~/.claude/agents/aso-*` and restart Claude Code.

**Slash commands not working:** Verify files exist at `~/.claude/commands/aso-*` and restart Claude Code.

**iTunes API not responding:** Test with `curl "https://itunes.apple.com/search?term=todoist&entity=software&limit=1"`. If it fails, check internet connection.

**Metadata exceeds character limits:** This shouldn't happen (agents validate), but verify with `echo -n "text" | wc -c`.

**Competitor data not found:** Verify exact app name spelling from the App Store. Provide manual data as fallback.

**Agent prompts for unknown data:** Say "Unknown" or "Not tracked yet" — agents will use industry benchmarks and label them as estimates.

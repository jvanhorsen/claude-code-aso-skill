# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

---

## [1.1.0] - 2026-02-18

### Restructured

Full architecture restructure for reduced complexity and improved agent performance.

#### Eliminated Duplication
- Deleted `.claude/skills/aso/` directory (17 duplicate Python files)
- Single source of truth: `app-store-optimization/` only

#### Rewrote Agent Prompts (-79% lines)
- Principle-based style replacing inline templates (3,184 → ~660 lines)
- Created `shared-protocol.md` — common rules referenced by all 4 agents
- Extracted 4 new output templates from agent definitions

#### Simplified Output Structure
- Reduced per-audit output from 17 files to 11 files
- Removed 5 redundant `action-*.md` phase checklists (absorbed into master plan)
- Removed `submission-guide.md` (merged into prelaunch-checklist.md)

#### Consolidated Documentation
- Merged `INSTALL.md` into `USAGE.md`
- Merged `HOW_TO_USE.md` into `app-store-optimization/README.md`
- Simplified `ARCHITECTURE.md` (508 → ~200 lines)

#### Refactored scraper.py
- Split 490-line file into ~65-line utility module + ~120-line scraping guide
- Extracted `ScraperGuide` class into `scraping-guide.md`

#### Updated Slash Commands (-60% lines)
- Rewritten as thin wrappers (475 → ~190 lines total)

#### Updated Project Files
- Rewrote `CLAUDE.md` to reflect post-restructure architecture
- Updated `README.md` with correct output structure and statistics
- Updated `PROJECT-STATUS.md`

### Net Impact

| Category | Before | After | Change |
|----------|--------|-------|--------|
| Agent definitions | 3,184 lines | ~660 lines | -79% |
| Slash commands | 475 lines | ~190 lines | -60% |
| scraper.py | 490 lines | ~65 lines + guide | -87% |
| Duplicate files | 17 files | 0 | -100% |
| Output files per audit | 17 | 11 | -35% |
| Templates | 6 | 5 | extracted from agents |

---

## [1.0.0] - 2025-11-07

### Initial Release — Production Ready

First stable release of the ASO Agent System for Claude Code.

### Added

- **4 specialized agents** — aso-master, aso-research, aso-optimizer, aso-strategist
- **4 slash commands** — `/aso-full-audit`, `/aso-optimize`, `/aso-prelaunch`, `/aso-competitor`
- **iTunes Search API integration** — real competitor data fetching
- **WebFetch utilities** — additional scraping capabilities
- **8 Python modules** — keyword analysis, metadata optimization, competitor analysis, ASO scoring, A/B testing, localization, review analysis, launch checklist
- **Character limit validation** — Apple (30/30/170/100/4000) and Google (50/80/4000)
- **17-file output structure** across 5 phase folders
- **6 action checklist templates**
- **Complete documentation** — ARCHITECTURE.md, USAGE.md, implementation plan
- **FitFlow example** — complete demo workflow with quality validation

### Known Limitations

- iTunes API: no keyword search volumes, no rankings, no download numbers
- WebFetch: slower, structure-dependent
- Search volumes estimated via benchmarks (verify with Apple Search Ads)

---

## [Unreleased]

### Planned for v2.0
- Paid ASO API integration (AppTweak, Sensor Tower)
- Web dashboard for tracking
- Automated reporting
- Multi-language support

---

**License:** MIT

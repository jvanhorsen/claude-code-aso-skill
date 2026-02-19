# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

---

## [1.2.0] - 2026-02-19

### Added

#### Custom Product Pages (CPPs) Module
- New `cpp_planner.py` with `CPPPlanner` class (~420 lines)
- `identify_cpp_opportunities()` — analyze keyword clusters for CPP themes
- `plan_cpp_variants()` — generate promotional text and screenshot strategy per CPP
- `calculate_cpp_priority()` — rank CPP opportunities by potential reach
- `generate_cpp_spec()` — output copy-paste ready CPP configurations
- Supports keyword-cluster, audience-segment, feature-specific, and competitor-gap strategies
- Apple allows up to 70 CPPs; as of July 2025, CPPs appear organically in search results

#### In-App Events Module
- New `event_planner.py` with `EventPlanner` class (~380 lines)
- `plan_event_calendar()` — 6-month seasonal event schedule with specific dates
- `generate_event_metadata()` — event name (30), short desc (50), long desc (120) with validation
- `identify_event_types()` — maps app category to event badge types
- `suggest_seasonal_events()` — 12-month seasonal hooks calendar
- Apple In-App Events appear in search results for double visibility

#### Visual Asset Optimization
- New `generate_screenshot_strategy()` method in `metadata_optimizer.py` (~350 lines)
- First-3-screenshot framework: Hero Value Prop → Key Differentiator → Social Proof
- Full 8-screenshot sequence with position-by-position guidance
- Text overlay guidelines, app preview video strategy, device coverage
- Visual A/B test recommendations with expected CVR impact ranges
- Platform-specific specs (Apple 10 screenshots/device, Google 8 screenshots)

#### Apple Search Ads Strategy
- Added organic vs paid keyword categorization to `aso-research.md`
- CPP + Apple Search Ads integration guidance
- Budget framework by app maturity (pre-launch through established)
- New "Apple Search Ads Readiness" section in master action plan template

#### Category Strategy & Conversion Funnel
- New `analyze_category_fit()` method in `aso_scorer.py` — primary/secondary category optimization
- Category competition density assessment for 20 app categories
- New `analyze_conversion_funnel()` method — impression→page view→install→retention analysis
- Benchmarks by competition level with automatic bottleneck identification
- Stage-by-stage diagnosis with fix priorities

### Changed

- Output structure expanded from 11 to 13 files per audit
  - Added `02-metadata/custom-product-pages.md`
  - Added `05-optimization/event-calendar.md`
- `aso-optimizer.md` — new CPP section and visual optimization references
- `aso-strategist.md` — new In-App Events section and event calendar responsibilities
- `aso-research.md` — Apple Search Ads integration and category positioning sections
- `shared-protocol.md` — In-App Events and CPP character limits, new module commands
- `apple-metadata-template.md` — CPP variant sections with promotional text templates
- `google-metadata-template.md` — screenshot strategy section with feature graphic guidelines
- `timeline-template.md` — Phase 6 for Events & CPPs, expanded milestones
- `master-action-plan-template.md` — Apple Search Ads Readiness section

### Net Impact

| Category | v1.1 | v1.2 | Change |
|----------|------|------|--------|
| Python modules | 8 | 10 | +2 (cpp_planner, event_planner) |
| Output files per audit | 11 | 13 | +2 (custom-product-pages, event-calendar) |
| ASO areas covered | 8 | 13 | +5 (CPPs, events, visual strategy, ads, category/funnel) |
| Industry coverage | ~60% | ~85% | +25% of 2025-2026 best practices |

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
- Semantic keyword clustering (NLP-based intent matching)
- Paid ASO API integration (AppTweak, Sensor Tower)
- Web dashboard for tracking
- Multi-language expansion support
- Automated reporting

---

**License:** MIT

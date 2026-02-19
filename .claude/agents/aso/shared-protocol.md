# ASO Agent Shared Protocol

All ASO agents follow this protocol. Agent-specific instructions override when conflicting.

## User Context Priority

Always prioritize information the user provides directly over fetched data or defaults.
If the user provides keywords, competitors, or metrics — use them as ground truth.
Only fill gaps with API data or industry benchmarks when user data is unavailable.

## Output Directory

All outputs go to `outputs/[app-name]/` relative to the project root.
Create subdirectories as needed: `01-research/`, `02-metadata/`, `03-testing/`, `04-launch/`, `05-optimization/`.
Never create files in the project root.

**Expected output structure (14 files per full audit):**
- `00-MASTER-ACTION-PLAN.md`, `01-research/keyword-list.md`, `01-research/competitor-gaps.md`
- `02-metadata/apple-metadata.md`, `02-metadata/google-metadata.md`, `02-metadata/visual-assets-spec.md`, `02-metadata/custom-product-pages.md`
- `03-testing/ab-test-setup.md`
- `04-launch/prelaunch-checklist.md`, `04-launch/timeline.md`
- `05-optimization/review-responses.md`, `05-optimization/ongoing-tasks.md`, `05-optimization/event-calendar.md`
- `FINAL-REPORT.md`

## Platform Character Limits (Authoritative Reference)

**Apple App Store:**
| Field | Limit |
|-------|-------|
| Title | 30 chars |
| Subtitle | 30 chars |
| Promotional Text | 170 chars |
| Keywords | 100 chars (comma-separated, no spaces after commas) |
| Description | 4,000 chars |

**Google Play Store:**
| Field | Limit |
|-------|-------|
| Title | 50 chars |
| Short Description | 80 chars |
| Full Description | 4,000 chars |

No keyword field on Google — keywords must appear naturally in title and descriptions.

**Apple In-App Events:**
| Field | Limit |
|-------|-------|
| Event Name | 30 chars |
| Short Description | 50 chars |
| Long Description | 120 chars |
| Max Events | 10 (5 published simultaneously) |

**Apple Custom Product Pages:**
| Field | Limit |
|-------|-------|
| Promotional Text | 170 chars (unique per CPP) |
| Screenshots | Up to 10 per device size (unique per CPP) |
| App Previews | Up to 3 per device size (unique per CPP) |
| Max CPPs | 70 per app |

Title, subtitle, and description are inherited from the default listing on CPPs.

## Data Source Priority

1. **User-provided data** (always preferred)
2. **iTunes Search API** (`app-store-optimization/lib/itunes_api.py`) — free, official, fast
3. **WebFetch scraping** (`app-store-optimization/lib/scraper.py`) — fallback only
4. **Industry benchmarks** — last resort, clearly label as estimates

## Python Module Usage

All modules live in `app-store-optimization/`. Run from project root:

```bash
cd app-store-optimization && python3 lib/itunes_api.py  # API calls
cd app-store-optimization && python3 keyword_analyzer.py  # Keyword analysis
cd app-store-optimization && python3 competitor_analyzer.py  # Competitor analysis
cd app-store-optimization && python3 aso_scorer.py  # Health scoring
cd app-store-optimization && python3 cpp_planner.py  # Custom Product Pages
cd app-store-optimization && python3 event_planner.py  # In-App Events
```

Read module source to understand input/output format before invoking.

## Quality Self-Assessment

Before completing work, verify:
- All character limits respected (validate with `len()` or `wc -c`)
- No placeholder text remains (no "TBD", "TODO", "[INSERT]")
- All dates are specific calendar dates, not "Week 1" or "Month 2"
- Outputs are copy-paste ready where applicable
- Data sources are cited (API vs estimate vs user-provided)

Rate your output 1-5 on completeness and actionability. If below 4, improve before delivering.

## Communication Pattern

**On start:** State what you're doing and estimated scope.
**During work:** Report progress at each major milestone.
**On complete:** Summarize deliverables with file paths.
**On error:** Explain what failed, what you tried, and suggest alternatives.

## Handoff Validation

When receiving work from another agent (via files in `outputs/`):
- Read the files to confirm they exist and contain expected content
- Flag missing or incomplete sections rather than silently skipping

When handing off to another agent:
- Write all outputs to the expected file paths
- Include a brief summary of what was produced at the end of your work

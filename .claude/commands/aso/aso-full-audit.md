---
name: aso-full-audit
description: Complete ASO audit with keyword research, competitor intelligence, metadata optimization, and launch planning
---

# ASO Full Audit

Run a comprehensive App Store Optimization audit producing 14 actionable deliverables.

## Agent

Invokes **aso-master** orchestrator, which coordinates 5 specialist agents sequentially:
1. **aso-research** — keyword + competitor data
2. **aso-metadata** — Apple + Google metadata
3. **aso-creative** — visual assets, CPPs, A/B tests
4. **aso-launch** — pre-launch checklist + timeline
5. **aso-ongoing** — review templates, events, ongoing tasks

Progress updates are printed after each phase completes.

## Usage

```
/aso-full-audit [app-name]
```

## Information Gathered

aso-master will ask for:
- App name and category
- Key features (3-5)
- Target audience
- Platforms (Apple, Google, or both)
- Launch date (or TBD)
- Known competitors (or auto-discover)

## Output

`outputs/[app-name]/` — 14 files across 5 phase folders. Start with `00-MASTER-ACTION-PLAN.md`.

## Time

30-40 minutes (fully automated, with progress updates after each phase).

## When to Use

- New app launch (4-6 weeks before submission)
- Full store presence overhaul
- Comprehensive competitive + metadata + strategy package

## Alternatives

| Need | Command |
|------|---------|
| Metadata only | `/aso-optimize` |
| Launch checklist only | `/aso-prelaunch` |
| Competitor analysis only | `/aso-competitor` |

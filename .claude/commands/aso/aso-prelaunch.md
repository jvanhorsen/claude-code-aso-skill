---
name: aso-prelaunch
description: Generate comprehensive pre-launch checklist and timeline with specific dates for app store submission
---

# ASO Pre-Launch

Create a detailed pre-launch checklist, launch timeline, review response templates, event calendar, and ongoing optimization schedule.

## Agent

Invokes two specialist agents sequentially:
1. **aso-launch** — pre-launch checklist + week-by-week timeline
2. **aso-ongoing** — review templates, event calendar, ongoing tasks

## Usage

```
/aso-prelaunch [app-name] [launch-date]
```

Use `TBD` for launch-date if not yet decided — the agent will suggest a timeline.

## Information Gathered

- App name
- Launch date (or TBD)
- Platforms (Apple, Google, or both)
- App maturity (pre-launch, soft launch, or already live)

## Output

`outputs/[app-name]/04-launch/` and `outputs/[app-name]/05-optimization/` containing:
- `prelaunch-checklist.md` — comprehensive validation checklist
- `timeline.md` — week-by-week with specific calendar dates
- `review-responses.md` — pre-written response templates
- `event-calendar.md` — In-App Events with specific dates
- `ongoing-tasks.md` — daily/weekly/monthly optimization schedule

## Time

10-14 minutes.

## When to Use

- 4-6 weeks before launch
- First-time app submission
- Multi-platform launch coordination
- Soft launch / phased rollout planning

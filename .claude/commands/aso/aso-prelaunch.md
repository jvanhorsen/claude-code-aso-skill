---
name: aso-prelaunch
description: Generate comprehensive pre-launch checklist and timeline with specific dates for app store submission
---

# ASO Pre-Launch

Create a detailed pre-launch checklist and week-by-week timeline for app store submission.

## Agent

Invokes **aso-strategist** directly (skips research and metadata phases).

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
- `ongoing-tasks.md` — daily/weekly/monthly optimization schedule

## Time

8-10 minutes.

## When to Use

- 4-6 weeks before launch
- First-time app submission
- Multi-platform launch coordination
- Soft launch / phased rollout planning

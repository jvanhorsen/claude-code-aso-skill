---
name: aso-competitor
description: Competitive intelligence analysis with keyword gaps and opportunities identification
---

# ASO Competitor Analysis

Deep-dive competitive intelligence to identify keyword gaps and positioning opportunities.

## Agent

Invokes **aso-research** in competitor-analysis mode.

## Usage

```
/aso-competitor [app-name] [competitor1,competitor2,...]
```

Use `auto` instead of competitor names to auto-discover top 5 competitors in the category.

## Information Gathered

- App name and category
- Competitor names (or "auto" to discover)
- Platform (Apple, Google, or both)

## Output

`outputs/[app-name]/01-research/` containing:
- `keyword-list.md` — prioritized keywords with implementation guide
- `competitor-gaps.md` — opportunities competitors are missing

## Time

10-15 minutes.

## When to Use

- Understanding competitive landscape before market entry
- Finding differentiation and unique positioning angles
- Discovering underutilized keywords
- Learning best practices from successful competitors

## Data Sources

- iTunes Search API (real-time competitor metadata, ratings, screenshots)
- WebFetch scraping (fallback if API insufficient)
- `competitor_analyzer.py` and `keyword_analyzer.py` Python modules

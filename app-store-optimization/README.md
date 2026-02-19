# App Store Optimization (ASO) Skill

**Version**: 1.2.0

## Overview

A comprehensive App Store Optimization skill for Claude Code that provides keyword research, metadata optimization, competitor analysis, A/B testing, review analysis, localization, launch planning, Custom Product Pages (CPPs), In-App Events, visual asset optimization, and Apple Search Ads strategy for Apple App Store and Google Play Store.

## Installation

```bash
# User-level (available in all projects)
cp -r app-store-optimization ~/.claude/skills/

# Project-level
cp -r app-store-optimization /path/to/project/.claude/skills/

# Verify
ls ~/.claude/skills/app-store-optimization/
# Should show: SKILL.md, 10 Python modules, lib/, sample files
```

## Quick Start

Ask Claude to use the skill:

```
Hey Claude -- I just added the "app-store-optimization" skill.
Can you research keywords for my fitness app targeting home workouts and yoga?
```

Claude will use the appropriate Python modules to analyze keywords, competitors, and generate optimized metadata.

## Capabilities

| Area | What It Does |
|------|-------------|
| **Keyword Research** | Search volume, competition analysis, long-tail discovery |
| **Metadata Optimization** | Platform-specific titles, descriptions, keyword fields with character validation |
| **Competitor Analysis** | Strategy comparison, gap identification, competitive positioning |
| **ASO Scoring** | 0-100 health score across metadata, ratings, keywords, conversion |
| **A/B Testing** | Test design, sample size calculation, statistical significance |
| **Localization** | Market prioritization, translation management, ROI analysis |
| **Review Analysis** | Sentiment analysis, theme extraction, response templates |
| **Launch Planning** | Pre-launch checklists, timeline generation, compliance validation |
| **Custom Product Pages** | CPP opportunity identification, promotional text variants, priority scoring |
| **In-App Events** | Seasonal event calendar, event metadata generation, badge type recommendations |

## Python Modules

### keyword_analyzer.py
Keyword research with volume, competition, and relevance scoring.
- `analyze_keyword()`, `compare_keywords()`, `find_long_tail_opportunities()`

### metadata_optimizer.py
Platform-specific metadata with character limit validation.
- `optimize_title()`, `optimize_description()`, `validate_character_limits()`

### competitor_analyzer.py
Competitor ASO strategy analysis and gap identification.
- `analyze_competitor()`, `compare_competitors()`, `identify_gaps()`

### aso_scorer.py
ASO health scoring (0-100) with category breakdown and recommendations.
- `calculate_overall_score()`, `generate_recommendations()`

### ab_test_planner.py
A/B test design with statistical rigor.
- `design_test()`, `calculate_sample_size()`, `calculate_significance()`

### localization_helper.py
Multi-language optimization and market prioritization.
- `identify_target_markets()`, `translate_metadata()`, `calculate_localization_roi()`

### review_analyzer.py
Review sentiment analysis and response template generation.
- `analyze_sentiment()`, `extract_common_themes()`, `generate_response_templates()`

### launch_checklist.py
Pre-launch validation and timing optimization.
- `generate_prelaunch_checklist()`, `optimize_launch_timing()`

### cpp_planner.py
Custom Product Pages strategy and specification generation.
- `identify_cpp_opportunities()`, `plan_cpp_variants()`, `calculate_cpp_priority()`, `generate_cpp_spec()`
- Supports keyword-cluster, audience-segment, feature-specific, and competitor-gap CPP strategies
- Generates promotional text variants (170 chars) and screenshot guidance per CPP

### event_planner.py
In-App Events and Promotional Content planning.
- `plan_event_calendar()`, `generate_event_metadata()`, `identify_event_types()`, `suggest_seasonal_events()`
- Apple In-App Event character limits: Name 30, Short Description 50, Long Description 120
- Seasonal calendar with 12-month event hooks and category-specific event type mapping

## Platform Character Limits

**Apple App Store:**
| Field | Limit |
|-------|-------|
| Title | 30 chars |
| Subtitle | 30 chars |
| Promotional Text | 170 chars |
| Keywords | 100 chars (comma-separated, no spaces) |
| Description | 4,000 chars |

**Google Play Store:**
| Field | Limit |
|-------|-------|
| Title | 50 chars |
| Short Description | 80 chars |
| Full Description | 4,000 chars |

No keyword field on Google — keywords must appear naturally in title and descriptions.

## Usage Examples

### Keyword Research
```
Can you research the best keywords for my productivity app?
I'm targeting professionals who need task management and team collaboration.
```

### Metadata Optimization
```
Create optimized metadata for both Apple and Google Play:
- App: TaskFlow
- Category: Productivity
- Features: AI task prioritization, team collaboration, calendar integration
- Keywords: task manager, productivity app, team tasks
```

### Competitor Analysis
```
Analyze the ASO strategies of the top 5 productivity apps.
I want to understand their title strategies and keyword usage.
```

### ASO Health Score
```
Calculate my app's ASO score:
- Average rating: 4.3 stars (8,200 ratings)
- Keywords in top 10: 4, top 50: 15
- Conversion rate: 3.8%
```

### A/B Testing
```
I want to A/B test my app icon. Current conversion rate is 4.2%.
How many visitors do I need and how long should I run the test?
```

### Pre-Launch Checklist
```
Generate a pre-launch checklist for both app stores.
My launch date is March 15, 2026.
```

## Data Fetching (lib/)

### lib/itunes_api.py
iTunes Search API wrapper for fetching real competitor data (free, no auth required).

### lib/scraper.py
WebFetch utility class for app store page scraping (fallback when API is insufficient).

### lib/scraping-guide.md
Best practices and examples for WebFetch-based scraping.

### lib/data_sources.md
Complete data source documentation with capabilities and limitations.

## Technical Details

- **Python**: 3.7+ (standard library only, zero external dependencies)
- **Data format**: JSON input/output
- **Platforms**: Apple App Store + Google Play Store
- **Scope**: Organic ASO + Apple Search Ads readiness (CPP integration, keyword strategy for paid/organic)

## Limitations

- Keyword search volumes are estimates (no official Apple/Google data available)
- Competitor data limited to publicly available information
- Apple metadata changes require app submission (except Promotional Text)
- Store algorithms are proprietary and change without notice

## Agent System

This skill also integrates with a 4-agent orchestration system for comprehensive ASO audits. See the parent repository's `.claude/USAGE.md` for agent installation and slash commands (`/aso-full-audit`, `/aso-optimize`, `/aso-prelaunch`, `/aso-competitor`).

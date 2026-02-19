# WebFetch Scraping Guide for ASO Agents

## Overview

WebFetch is a built-in Claude Code tool that fetches web pages and extracts information using AI. Use it when iTunes Search API doesn't provide sufficient data.

## Usage Pattern

```python
from scraper import WebFetchPrompts

# Get pre-configured prompt
config = WebFetchPrompts.app_store_search("task manager")

# Use WebFetch tool with:
#   url: config["url"]
#   prompt: config["prompt"]
```

## Scraping Workflows

### App Store Search Results

**When to use:** Finding top-ranking apps for a keyword

1. `WebFetchPrompts.app_store_search("productivity")`
2. Use WebFetch tool with the URL and prompt
3. Parse returned JSON array of apps
4. Extract competitor names and URLs

### Individual App Pages

**When to use:** Getting detailed metadata for a specific app

1. `WebFetchPrompts.app_store_app_page(url)`
2. Use WebFetch tool
3. Extract title, description, rating, etc.

### Google Play Store

Same pattern using `play_store_search()` and `play_store_app_page()`.

## Common Scenarios

### Competitor Research
```
1. WebFetch search for category keyword → get top 5 app URLs
2. WebFetch each app page → extract metadata
3. Pass to competitor_analyzer.py for analysis
```

### Keyword Rankings
```
1. WebFetch search for target keyword
2. Find your app's position in results
3. If not in top 10, note "Not in top 10"
```

### Review Scraping
- iTunes API provides reviews — use that first
- WebFetch can get first few visible reviews from the page
- For bulk review analysis, prefer the iTunes API reviews endpoint

## Best Practices

### Respectful Scraping
- Wait 2-3 seconds between requests
- Don't scrape more than 10 pages in rapid succession
- Use iTunes API when possible (faster and official)

### Error Handling
- If WebFetch fails, fall back to iTunes Search API (if Apple)
- If API also fails, ask user for data manually
- If all else fails, use category defaults

### Data Validation
- Validate extracted data for missing fields
- Confirm character counts seem reasonable
- Verify URLs are properly formatted

### Rate Limiting
If rate-limited: wait 60 seconds, reduce pages, use cached data, or ask user.

## When to Use iTunes API Instead

**Prefer iTunes API for:**
- Competitor names and basic metadata
- Bulk competitor comparison
- Speed (API is faster than scraping)

**Use WebFetch only for:**
- Data not in iTunes API (visual layout, screenshot count)
- Keyword rankings on store pages
- "What's New" text (not always in API)

## Capabilities & Limitations

**WebFetch CAN:** Extract visible text, metadata, ratings, review counts, identify visual elements.

**WebFetch CANNOT:** Access private analytics, get historical data, bypass logins, get exact search volumes.

## Troubleshooting

| Issue | Solution |
|-------|----------|
| WebFetch timeout | Retry or use iTunes API |
| Incomplete extraction | Refine prompt to be more specific |
| Wrong language | Add country code to URL (e.g., `/us/`) |

## Legal & Ethical Notes

- Respect robots.txt restrictions
- Scraping for competitive research is generally allowed
- Only scrape public data; respect copyright
- Max 10 pages/minute, 100 pages/hour
- Use caching to avoid repeat requests

---

**Remember:** WebFetch is your fallback when iTunes API doesn't provide needed data. Always prefer the official API for speed and reliability.

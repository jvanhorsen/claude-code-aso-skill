# Google Play Store Metadata — {{APP_NAME}}

> Copy-paste ready for Google Play Console. All fields validated against character limits.

---

## Title (50 char limit)

```
{{TITLE}}
```

**Characters:** {{TITLE_COUNT}}/50
**Keywords included:** {{TITLE_KEYWORDS}}

---

## Short Description (80 char limit)

```
{{SHORT_DESCRIPTION}}
```

**Characters:** {{SHORT_DESC_COUNT}}/80
**Note:** Critical for CTR — this is the elevator pitch users see first.

---

## Full Description (4,000 char limit)

```
{{FULL_DESCRIPTION}}
```

**Characters:** {{FULL_DESC_COUNT}}/4,000

**Structure:**
1. Opening paragraph with primary keywords (first 167 chars shown in search)
2. Feature sections with emoji bullets
3. Social proof / stats
4. Call to action

**Keyword placement:**
- Primary keywords in first sentence
- Secondary keywords in feature headings
- Long-tail keywords distributed naturally
- No keyword stuffing (reads naturally)

---

## "What's New" (Release Notes)

```
{{WHATS_NEW}}
```

---

## Validation Summary

| Field | Length | Limit | Status |
|-------|--------|-------|--------|
| Title | {{TITLE_COUNT}} | 50 | {{TITLE_STATUS}} |
| Short Description | {{SHORT_DESC_COUNT}} | 80 | {{SHORT_DESC_STATUS}} |
| Full Description | {{FULL_DESC_COUNT}} | 4,000 | {{FULL_DESC_STATUS}} |

**Keyword Coverage:**
- Title keywords: {{TITLE_KEYWORDS}}
- Short description keywords: {{SHORT_DESC_KEYWORDS}}
- Full description keywords (first 500 chars): {{FULL_DESC_TOP_KEYWORDS}}
- Total unique keywords: {{TOTAL_UNIQUE_KEYWORDS}}

**Google-Specific Notes:**
- No separate keyword field — all keywords must appear in title or descriptions
- Google indexes full description for search ranking
- Front-load keywords: first 167 chars appear in search results
- Use emoji section breaks for readability (Google supports them)

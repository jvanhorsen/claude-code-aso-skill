# Apple App Store Metadata — {{APP_NAME}}

> Copy-paste ready for App Store Connect. All fields validated against character limits.

---

## Title (30 char limit)

```
{{TITLE}}
```

**Characters:** {{TITLE_COUNT}}/30
**Keywords included:** {{TITLE_KEYWORDS}}

---

## Subtitle (30 char limit)

```
{{SUBTITLE}}
```

**Characters:** {{SUBTITLE_COUNT}}/30
**Keywords included:** {{SUBTITLE_KEYWORDS}}

---

## Promotional Text (170 char limit)

```
{{PROMOTIONAL_TEXT}}
```

**Characters:** {{PROMO_COUNT}}/170
**Note:** Can be updated without new app submission.

---

## Keywords Field (100 char limit)

```
{{KEYWORDS}}
```

**Characters:** {{KEYWORDS_COUNT}}/100
**Rules applied:**
- No spaces after commas
- No duplicates from title or subtitle
- No plurals (Apple indexes both forms)
- Prioritized by relevance × search volume

---

## Description (4,000 char limit)

```
{{DESCRIPTION}}
```

**Characters:** {{DESC_COUNT}}/4,000

**Structure:**
1. Opening hook with primary keyword (first 150 chars visible)
2. Key features with benefits
3. Social proof / credibility
4. Call to action

---

## "What's New" (Release Notes)

```
{{WHATS_NEW}}
```

---

## Validation Summary

| Field | Length | Limit | Status |
|-------|--------|-------|--------|
| Title | {{TITLE_COUNT}} | 30 | {{TITLE_STATUS}} |
| Subtitle | {{SUBTITLE_COUNT}} | 30 | {{SUBTITLE_STATUS}} |
| Promotional Text | {{PROMO_COUNT}} | 170 | {{PROMO_STATUS}} |
| Keywords | {{KEYWORDS_COUNT}} | 100 | {{KEYWORDS_STATUS}} |
| Description | {{DESC_COUNT}} | 4,000 | {{DESC_STATUS}} |

**Keyword Coverage:**
- Title keywords: {{TITLE_KEYWORDS}}
- Subtitle keywords: {{SUBTITLE_KEYWORDS}}
- Keywords field: {{KEYWORDS_FIELD_KEYWORDS}}
- Total unique keywords: {{TOTAL_UNIQUE_KEYWORDS}}

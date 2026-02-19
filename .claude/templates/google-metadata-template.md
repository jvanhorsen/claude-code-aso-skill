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

---

## Screenshot Strategy

### Feature Graphic (1024x500 — Required)

**Design:**
```
{{FEATURE_GRAPHIC_DESCRIPTION}}
```

**Guidelines:**
- Bold headline (3-5 words) communicating primary value
- App icon prominently placed
- Clean background with brand colors
- Avoid fine text — it's displayed small on most surfaces

---

### Screenshot Sequence (Recommended: 6-8)

| Position | Purpose | Headline Pattern |
|----------|---------|-----------------|
| 1 | Hero — Primary Value Proposition | [Verb] + [Desired Outcome] |
| 2 | Key Differentiator | [Benefit] in [Timeframe/Ease] |
| 3 | Social Proof / Wow Moment | [Number]+ [Social Proof] |
| 4 | Secondary Feature | [Feature Benefit] |
| 5 | Workflow / Process | [Action] → [Result] |
| 6 | Customization / Settings | [Personalize] Your [Noun] |

**First 3 screenshots are critical** — they appear in search results and drive 70% of conversion decisions.

### Screenshot Specifications

| Device | Size | Required |
|--------|------|----------|
| Phone | 1080x1920px (min) | ✅ |
| 7" Tablet | 1080x1920px | Optional |
| 10" Tablet | 1080x1920px | Optional |

### Text Overlay Guidelines (Google)
- Bold sans-serif fonts (Google Sans / Roboto)
- Emoji in text overlays can improve engagement
- Max 5-7 words per headline
- High contrast text — readable at thumbnail size
- Consistent visual branding across all screenshots

### Promo Video

**Specs:** 30 seconds - 2 minutes, YouTube link or direct upload
**Structure:**
1. **0-3s:** Hook — show most impressive result
2. **3-15s:** Core use case walkthrough
3. **15-30s+:** Additional features + CTA

{{ADDITIONAL_SCREENSHOT_NOTES}}

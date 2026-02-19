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

---

## Custom Product Pages (CPPs)

> Apple allows up to 70 CPPs per app. Each has unique screenshots, promotional text, and app previews.
> As of July 2025, CPPs appear organically in App Store search results.

### CPP 1: {{CPP1_NAME}}

**Theme:** {{CPP1_THEME}}
**Target Keywords:** {{CPP1_KEYWORDS}}

**Promotional Text (170 char limit):**
```
{{CPP1_PROMO_TEXT}}
```
**Characters:** {{CPP1_PROMO_COUNT}}/170

**Screenshot Strategy:**
{{CPP1_SCREENSHOT_STRATEGY}}

**Success Metric:** {{CPP1_TARGET_CVR_LIFT}} CVR lift vs default listing

---

### CPP 2: {{CPP2_NAME}}

**Theme:** {{CPP2_THEME}}
**Target Keywords:** {{CPP2_KEYWORDS}}

**Promotional Text (170 char limit):**
```
{{CPP2_PROMO_TEXT}}
```
**Characters:** {{CPP2_PROMO_COUNT}}/170

**Screenshot Strategy:**
{{CPP2_SCREENSHOT_STRATEGY}}

**Success Metric:** {{CPP2_TARGET_CVR_LIFT}} CVR lift vs default listing

---

### CPP Implementation Notes

- Start with top {{CPP_COUNT}} CPPs. Monitor for 4 weeks before expanding.
- Each CPP can be linked to Apple Search Ads campaigns for keyword-targeted traffic.
- Review CPP performance in App Store Connect → Custom Product Pages analytics.
- Benchmark: 5.9% average CVR lift for well-targeted CPPs.

{{ADDITIONAL_CPPS}}

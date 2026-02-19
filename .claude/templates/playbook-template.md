# ASO Playbook: {{APP_NAME}}

**Prepared:** {{DATE}}
**Platforms:** {{PLATFORMS}}
**ASO Health Score:** {{SCORE}}/100
**Strategy Focus:** {{STRATEGY_FOCUS}}

---

## Executive Summary

{{EXECUTIVE_SUMMARY}}

**Key Targets (90-Day)**

| Metric | Current | Target | Expected Lift |
|--------|---------|--------|---------------|
| Impressions | {{CURRENT_IMPRESSIONS}} | {{TARGET_IMPRESSIONS}} | {{IMPRESSIONS_LIFT}} |
| Conversion Rate | {{CURRENT_CVR}} | {{TARGET_CVR}} | {{CVR_LIFT}} |
| Organic Installs | {{CURRENT_INSTALLS}} | {{TARGET_INSTALLS}} | {{INSTALLS_LIFT}} |
| Average Rating | {{CURRENT_RATING}} | {{TARGET_RATING}} | {{RATING_LIFT}} |

---

## 1. Market Research Insights

### Keyword Landscape

{{KEYWORD_LANDSCAPE_NARRATIVE}}

**Top Priority Keywords**

| Keyword | Est. Volume | Difficulty | Strategy | Placement |
|---------|-------------|------------|----------|-----------|
{{TOP_KEYWORDS_TABLE}}

### Competitive Positioning

{{COMPETITIVE_NARRATIVE}}

**Competitor Comparison**

| App | Title Strategy | Rating | Key Weakness |
|-----|---------------|--------|--------------|
{{COMPETITOR_TABLE}}

### Category Analysis

{{CATEGORY_ANALYSIS_NARRATIVE}}

---

## 2. Metadata Strategy

### Apple App Store

{{APPLE_STRATEGY_NARRATIVE}}

| Field | Content | Length |
|-------|---------|--------|
| Title | {{APPLE_TITLE}} | {{APPLE_TITLE_LEN}}/30 |
| Subtitle | {{APPLE_SUBTITLE}} | {{APPLE_SUBTITLE_LEN}}/30 |
| Keyword Field | {{APPLE_KEYWORDS_SUMMARY}} | {{APPLE_KEYWORDS_LEN}}/100 |
| Promotional Text | {{APPLE_PROMO}} | {{APPLE_PROMO_LEN}}/170 |

**Description Highlights:** {{APPLE_DESC_HIGHLIGHTS}}

### Google Play Store

{{GOOGLE_STRATEGY_NARRATIVE}}

| Field | Content | Length |
|-------|---------|--------|
| Title | {{GOOGLE_TITLE}} | {{GOOGLE_TITLE_LEN}}/50 |
| Short Description | {{GOOGLE_SHORT}} | {{GOOGLE_SHORT_LEN}}/80 |

**Full Description Highlights:** {{GOOGLE_DESC_HIGHLIGHTS}}

### Compliance Summary

All metadata validated against platform character limits. No placeholder text remains. Keywords integrated naturally without stuffing.

---

## 3. Visual & Creative Strategy

### Screenshot Sequence

{{SCREENSHOT_STRATEGY_NARRATIVE}}

**Recommended 8-Screenshot Sequence**

| Position | Theme | Purpose |
|----------|-------|---------|
{{SCREENSHOT_SEQUENCE_TABLE}}

### App Icon & Preview Video

{{ICON_VIDEO_NARRATIVE}}

### Custom Product Pages

{{CPP_NARRATIVE}}

| CPP Name | Theme | Target Audience | Key Differentiator |
|----------|-------|-----------------|-------------------|
{{CPP_TABLE}}

---

## 4. Testing Roadmap

### A/B Test Priority

{{TESTING_NARRATIVE}}

| Test | Element | Hypothesis | Expected Impact | Duration |
|------|---------|------------|-----------------|----------|
{{AB_TEST_TABLE}}

### Testing Timeline

{{TESTING_TIMELINE_NARRATIVE}}

---

## 5. Launch Plan

### Key Milestones

| Date | Milestone | Owner | Status |
|------|-----------|-------|--------|
{{MILESTONES_TABLE}}

### Risk Mitigation

| Risk | Probability | Impact | Mitigation |
|------|-------------|--------|------------|
{{RISK_TABLE}}

---

## 6. Ongoing Optimization

### Review Management

{{REVIEW_STRATEGY_NARRATIVE}}

**Response Approach by Category**

| Category | Tone | Response Time | Example Situation |
|----------|------|---------------|-------------------|
{{REVIEW_CATEGORIES_TABLE}}

### In-App Events Calendar (Next 6 Months)

{{EVENTS_NARRATIVE}}

| Date | Event Name | Type | Target Audience |
|------|-----------|------|-----------------|
{{EVENTS_TABLE}}

### Maintenance Cadence

| Frequency | Tasks | Time Investment |
|-----------|-------|-----------------|
| Daily | Review monitoring, crash reports, critical responses | 15 min |
| Weekly | Keyword rankings, conversion trends, competitor check | 1 hour |
| Bi-Weekly | A/B test analysis, promotional text refresh | 2 hours |
| Monthly | Full ASO health score, competitor deep-dive, sentiment report | 2-3 hours |
| Quarterly | Keyword refresh, localization ROI, major metadata update | 4-6 hours |

---

## 7. Success Metrics

### 30-60-90 Day Targets

| Timeframe | Impressions | CVR | Organic Installs | Rating |
|-----------|-------------|-----|-------------------|--------|
| Day 30 | {{TARGET_30D_IMPRESSIONS}} | {{TARGET_30D_CVR}} | {{TARGET_30D_INSTALLS}} | {{TARGET_30D_RATING}} |
| Day 60 | {{TARGET_60D_IMPRESSIONS}} | {{TARGET_60D_CVR}} | {{TARGET_60D_INSTALLS}} | {{TARGET_60D_RATING}} |
| Day 90 | {{TARGET_90D_IMPRESSIONS}} | {{TARGET_90D_CVR}} | {{TARGET_90D_INSTALLS}} | {{TARGET_90D_RATING}} |

### How to Measure

| KPI | Tool | Frequency |
|-----|------|-----------|
| Keyword Rankings | Apple Search Ads (free account) | Weekly |
| Conversion Rate | App Store Connect / Play Console Analytics | Weekly |
| Impressions | App Store Connect / Play Console Analytics | Weekly |
| Rating & Reviews | App Store Connect / Play Console | Daily |
| Competitor Movement | iTunes Search API / manual review | Monthly |

---

## 8. Appendix: Deliverable Files

All detailed deliverables are available as individual files in the output directory.

| File | Description | Location |
|------|-------------|----------|
| Master Action Plan | Phase-by-phase task checklist with timelines | `00-MASTER-ACTION-PLAN.md` |
| Keyword List | Prioritized keywords with placement recommendations | `01-research/keyword-list.md` |
| Competitor Gaps | Competitive analysis with exploitable opportunities | `01-research/competitor-gaps.md` |
| Apple Metadata | Copy-paste ready App Store Connect metadata | `02-metadata/apple-metadata.md` |
| Google Metadata | Copy-paste ready Play Console metadata | `02-metadata/google-metadata.md` |
| Visual Assets Spec | Screenshot, icon, and preview video specifications | `02-metadata/visual-assets-spec.md` |
| Custom Product Pages | CPP configurations with promotional text variants | `02-metadata/custom-product-pages.md` |
| A/B Test Setup | Test configurations with hypotheses and sample sizes | `03-testing/ab-test-setup.md` |
| Pre-Launch Checklist | Comprehensive validation across 7 categories | `04-launch/prelaunch-checklist.md` |
| Timeline | Week-by-week implementation with specific dates | `04-launch/timeline.md` |
| Review Responses | Templates for 5 common review scenarios | `05-optimization/review-responses.md` |
| Event Calendar | In-App Events with metadata and seasonal planning | `05-optimization/event-calendar.md` |
| Ongoing Tasks | Daily/weekly/monthly optimization schedule | `05-optimization/ongoing-tasks.md` |
| Final Report | Executive summary with strategy rationale | `FINAL-REPORT.md` |

---

## Export to PDF

**Option A: Using pandoc (recommended)**

```
pandoc PLAYBOOK.md -o ASO-Playbook-{{APP_NAME}}.pdf \
  --pdf-engine=xelatex \
  -V geometry:margin=1in \
  -V fontsize=11pt \
  -V colorlinks=true
```

**Option B: Using Chrome**

1. Open `PLAYBOOK.md` in a Markdown viewer (VS Code preview, GitHub, or any Markdown app)
2. Print (Cmd+P / Ctrl+P) and select "Save as PDF"
3. Recommended: A4 or Letter, margins Normal, enable "Background graphics" for tables

**Option C: Using VS Code**

1. Open `PLAYBOOK.md` in VS Code
2. Install "Markdown PDF" extension (yzane.markdown-pdf)
3. Open Command Palette > "Markdown PDF: Export (pdf)"

---

*Generated by aso-master agent | Data sources: iTunes Search API, competitive analysis, industry benchmarks*

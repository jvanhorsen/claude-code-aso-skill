# Master Action Plan: {{APP_NAME}}

**Generated:** {{DATE}}
**ASO Health Score:** {{SCORE}}/100
**Priority Level:** {{PRIORITY}}

---

## Executive Summary

**Current State:**
{{CURRENT_STATE_SUMMARY}}

**Target State:**
{{TARGET_STATE_SUMMARY}}

**Estimated Impact:**
- Impressions: {{IMPRESSION_INCREASE}}
- Conversion Rate: {{CVR_INCREASE}}
- Organic Installs: {{INSTALL_INCREASE}}

---

## Quick Wins (Complete First)

{{QUICK_WINS_LIST}}

**Estimated Completion:** {{QUICK_WINS_TIMELINE}}

---

## Complete Task Checklist

### Phase 1: Research ({{RESEARCH_DURATION}})

**Location:** `outputs/{{APP_NAME}}/01-research/`

#### Keyword Research
- [ ] Review keyword list and validate priority keywords
- [ ] Validate top 10 keyword search volumes via Apple Search Ads (free account)
- [ ] Research long-tail keyword opportunities (3-4 word phrases)
- [ ] Confirm keyword-to-field mapping (which keywords go in title vs subtitle vs description vs keyword field)
- [ ] Identify seasonal or trending keyword opportunities
{{RESEARCH_KEYWORD_TASKS}}

#### Competitor Analysis
- [ ] Analyze competitor gaps and identify positioning opportunities
- [ ] Document competitor title strategies and keyword usage
- [ ] Identify keywords with low competitor density and high relevance
- [ ] Note competitor weaknesses to exploit in metadata
{{RESEARCH_COMPETITOR_TASKS}}

**Deliverables:**
- `keyword-list.md` — prioritized keywords with implementation locations
- `competitor-gaps.md` — opportunities competitors miss

---

### Phase 2: Metadata Implementation ({{METADATA_DURATION}})

**Location:** `outputs/{{APP_NAME}}/02-metadata/`

#### Pre-Implementation
- [ ] Review generated metadata and ensure messaging aligns with brand voice
- [ ] Verify all character counts meet platform limits
- [ ] Confirm keywords are naturally integrated (not stuffed)

#### Apple App Store (if applicable)
- [ ] Copy title to App Store Connect ({{APPLE_TITLE_LENGTH}}/30 chars)
- [ ] Copy subtitle ({{APPLE_SUBTITLE_LENGTH}}/30 chars)
- [ ] Copy keyword field ({{APPLE_KEYWORDS_LENGTH}}/100 chars, no spaces after commas)
- [ ] Copy description ({{APPLE_DESC_LENGTH}}/4,000 chars)
- [ ] Update promotional text (can be changed without submission)
- [ ] Select A/B test variant for title (if testing)

#### Google Play Store (if applicable)
- [ ] Copy title to Play Console ({{GOOGLE_TITLE_LENGTH}}/50 chars)
- [ ] Copy short description ({{GOOGLE_SHORT_LENGTH}}/80 chars)
- [ ] Copy full description ({{GOOGLE_DESC_LENGTH}}/4,000 chars)
- [ ] Verify keywords appear naturally in first 300 characters

#### Visual Assets
- [ ] Brief designer on icon requirements (1024x1024px)
- [ ] Brief designer on screenshot specifications (per platform)
- [ ] Review and approve visual mockups
- [ ] Prepare feature graphic for Google Play (1024x500px)
{{METADATA_CUSTOM_TASKS}}

**Deliverables:**
- `apple-metadata.md` — copy-paste ready for App Store Connect
- `google-metadata.md` — copy-paste ready for Play Console
- `visual-assets-spec.md` — icon/screenshot requirements

---

### Phase 3: A/B Testing Setup ({{TESTING_DURATION}})

**Location:** `outputs/{{APP_NAME}}/03-testing/`

#### Baseline
- [ ] Document current conversion rate: {{BASELINE_CVR}}%
- [ ] Document current impressions and installs
- [ ] Identify highest-impact test element (icon > first screenshot > title > description)

#### Test Configuration
- [ ] Configure first A/B test in App Store Connect / Play Console
- [ ] Set traffic allocation (recommended: 50/50 or 33/33/33)
- [ ] Set minimum test duration (7 days minimum, 14 recommended)
- [ ] Define success metric and significance threshold (95%)
- [ ] Set calendar reminders for test check-ins (day 3, 7, 14)
{{TESTING_CUSTOM_TASKS}}

**Deliverables:**
- `ab-test-setup.md` — step-by-step test configuration with hypotheses

---

### Phase 4: Launch Preparation ({{LAUNCH_DURATION}})

**Location:** `outputs/{{APP_NAME}}/04-launch/`

#### Pre-Launch Validation
- [ ] Complete all items in prelaunch-checklist.md (7 phases: metadata, visuals, technical, legal, business, marketing, ASO)
- [ ] Verify privacy policy is published and accessible
- [ ] Confirm age/content ratings are complete
- [ ] Verify Apple encryption/export compliance declarations
- [ ] Complete Google data safety section

#### App Store Submission
- [ ] Submit to Apple App Store (allow 1-3 days for review)
- [ ] Submit to Google Play Store (allow 2-7 days for initial review)
- [ ] Prepare for common rejection reasons and fixes
- [ ] Have contingency plan for review delays

#### Launch Marketing
- [ ] Prepare launch announcement (social media, website, press)
- [ ] Set up support system (help email, FAQ, knowledge base)
- [ ] Verify analytics integration (App Store Connect + Play Console)
{{LAUNCH_CUSTOM_TASKS}}

**Deliverables:**
- `prelaunch-checklist.md` — comprehensive validation checklist
- `timeline.md` — week-by-week with specific calendar dates

---

### Phase 5: Ongoing Optimization (Continuous)

**Location:** `outputs/{{APP_NAME}}/05-optimization/`

#### Setup
- [ ] Set up keyword ranking monitoring
- [ ] Create review response workflow using templates
- [ ] Configure notification alerts for new reviews and ratings drops
- [ ] Schedule recurring ASO check-ins (see cadence below)

#### Ongoing Cadence
- **Daily (15 min):** Check new reviews, respond to critical issues, monitor crash reports
- **Weekly (1 hour):** Keyword ranking check, conversion rate trends, competitor monitoring
- **Bi-Weekly (2 hours):** A/B test analysis, promotional text refresh (Apple)
- **Monthly (2-3 hours):** ASO health score (run `aso_scorer.py`), competitor analysis, review sentiment report
- **Quarterly (4-6 hours):** Full keyword research refresh, localization ROI analysis, major metadata update if needed
{{OPTIMIZATION_CUSTOM_TASKS}}

**Deliverables:**
- `review-responses.md` — templates for common review scenarios
- `ongoing-tasks.md` — detailed daily/weekly/monthly schedule

---

## Timeline with Specific Dates

{{TIMELINE_WITH_DATES}}

---

## Success Metrics

### Week 1
- [ ] Keyword rankings improved for {{TARGET_KEYWORD_COUNT}} priority keywords
- [ ] Conversion rate baseline established
- [ ] A/B tests launched

### Month 1
- [ ] {{IMPRESSIONS_1M}} increase in impressions
- [ ] {{CVR_1M}} increase in conversion rate
- [ ] {{RATING_1M}} average rating achieved

### Month 3
- [ ] ASO health score increased by {{SCORE_INCREASE_3M}} points
- [ ] Top 10 ranking for {{TOP_10_KEYWORDS_3M}} priority keywords
- [ ] {{REVIEWS_3M}} reviews collected

### Month 6
- [ ] {{INSTALLS_6M}} increase in organic installs
- [ ] {{FINAL_RATING_6M}} average rating with {{FINAL_REVIEW_COUNT_6M}} reviews
- [ ] {{KEYWORD_DOMINANCE_6M}} keyword categories dominated

---

## Priority Matrix

### High Priority / High Impact
{{HIGH_PRIORITY_HIGH_IMPACT}}

### High Priority / Medium Impact
{{HIGH_PRIORITY_MEDIUM_IMPACT}}

### Medium Priority / High Impact
{{MEDIUM_PRIORITY_HIGH_IMPACT}}

### Low Priority (Defer)
{{LOW_PRIORITY_TASKS}}

---

## Resource Requirements

**Time Investment:**
- Research: {{RESEARCH_HOURS}} hours
- Metadata Implementation: {{METADATA_HOURS}} hours
- Visual Assets: {{VISUAL_HOURS}} hours (designer time)
- Testing Setup: {{TESTING_HOURS}} hours
- Launch Prep: {{LAUNCH_HOURS}} hours
- **Total Initial:** {{TOTAL_HOURS}} hours

**Ongoing Commitment:**
- Daily: {{DAILY_MINUTES}} minutes
- Weekly: {{WEEKLY_HOURS}} hours
- Monthly: {{MONTHLY_HOURS}} hours

**Team Members Needed:**
- Product Manager: {{PM_INVOLVEMENT}}
- Designer: {{DESIGNER_INVOLVEMENT}}
- Developer: {{DEVELOPER_INVOLVEMENT}}
- Marketing: {{MARKETING_INVOLVEMENT}}

---

## Apple Search Ads Readiness

### Keyword Strategy: Organic vs Paid

| Keyword | Strategy | Rationale | Est. CPT |
|---------|----------|-----------|----------|
{{SEARCH_ADS_KEYWORD_TABLE}}

### Budget Recommendation

| Phase | Monthly Budget | Focus |
|-------|---------------|-------|
| Month 1 | {{ADS_BUDGET_M1}} | Discovery campaigns, broad match |
| Month 2-3 | {{ADS_BUDGET_M2}} | Exact match on priority keywords |
| Month 4+ | {{ADS_BUDGET_M4}} | Full funnel with CPP targeting |

### CPP + Search Ads Integration

{{CPP_ADS_MAPPING}}

**Note:** Even without running ads, create a free Apple Search Ads account for keyword insights (Search Popularity scores).

---

## Risk Mitigation

{{RISKS_AND_MITIGATION}}

---

## Quality Validation

All deliverables have been validated for:
- Character count compliance (Apple/Google limits)
- Keyword density optimization
- Real calendar dates (no placeholders)
- Actionable tasks with success criteria
- Copy-paste ready content

---

## Next Steps

**Immediate (Today):**
1. {{IMMEDIATE_STEP_1}}
2. {{IMMEDIATE_STEP_2}}
3. {{IMMEDIATE_STEP_3}}

**This Week:**
1. {{WEEK_STEP_1}}
2. {{WEEK_STEP_2}}
3. {{WEEK_STEP_3}}

**This Month:**
1. {{MONTH_STEP_1}}
2. {{MONTH_STEP_2}}
3. {{MONTH_STEP_3}}

---

## Support

- **Questions about research:** Review `01-research/keyword-list.md`
- **Questions about metadata:** Review `02-metadata/apple-metadata.md` or `google-metadata.md`
- **Questions about testing:** Review `03-testing/ab-test-setup.md`
- **Questions about launch:** Review `04-launch/prelaunch-checklist.md`
- **Questions about optimization:** Review `05-optimization/ongoing-tasks.md`

---

**Generated by:** aso-master agent
**Data Sources:** iTunes Search API, competitive analysis, industry benchmarks
**Confidence Level:** {{CONFIDENCE_LEVEL}}

---

**Agent Notes:** {{AGENT_NOTES}}

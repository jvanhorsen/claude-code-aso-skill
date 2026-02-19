"""
Custom Product Pages (CPP) planning module for App Store Optimization.
Helps plan, prioritize, and generate specifications for Apple Custom Product Pages.

CPPs allow up to 70 custom App Store landing pages per app, each with unique
screenshots, promotional text, and app previews. As of July 2025, CPPs appear
organically in App Store search results (not just from ad traffic).

Character limits for CPPs match the main listing:
- Promotional Text: 170 chars (unique per CPP)
- Screenshots: up to 10 per device size (unique per CPP)
- App Preview: up to 3 per device size (unique per CPP)
Note: Title, subtitle, and description are inherited from the default listing.
"""

from typing import Dict, List, Any, Optional


class CPPPlanner:
    """Plans and prioritizes Custom Product Pages for Apple App Store."""

    # Apple CPP constraints
    MAX_CPPS = 70
    PROMO_TEXT_LIMIT = 170  # chars, unique per CPP
    MAX_SCREENSHOTS_PER_SIZE = 10
    MAX_PREVIEWS_PER_SIZE = 3

    # Common audience segments that benefit from CPPs
    AUDIENCE_TEMPLATES = {
        'new_users': {
            'description': 'First-time users unfamiliar with the app',
            'messaging_focus': 'Core value proposition, ease of use, getting started',
            'screenshot_strategy': 'Onboarding flow, simple UI, key benefit in first frame',
        },
        'power_users': {
            'description': 'Advanced users looking for depth and features',
            'messaging_focus': 'Advanced features, integrations, customization',
            'screenshot_strategy': 'Complex workflows, pro features, power user UI',
        },
        'switchers': {
            'description': 'Users migrating from a competitor app',
            'messaging_focus': 'Migration ease, feature parity, unique advantages',
            'screenshot_strategy': 'Side-by-side comparisons, import tools, differentiators',
        },
        'price_sensitive': {
            'description': 'Users comparing pricing and value',
            'messaging_focus': 'Free features, value for money, trial availability',
            'screenshot_strategy': 'Free tier capabilities, pricing comparison, ROI proof',
        },
        'seasonal': {
            'description': 'Users driven by seasonal needs or trends',
            'messaging_focus': 'Timely relevance, seasonal features, limited-time offers',
            'screenshot_strategy': 'Seasonal themes, time-relevant content, urgency cues',
        },
        'use_case_specific': {
            'description': 'Users searching for a specific functionality',
            'messaging_focus': 'Feature-specific benefits, workflow examples',
            'screenshot_strategy': 'Feature deep-dive, step-by-step workflow, outcome',
        },
    }

    # CPP performance benchmarks
    BENCHMARKS = {
        'average_cvr_lift': 0.059,  # 5.9% average CVR improvement
        'top_performer_cvr_lift': 0.15,  # 15% for well-targeted CPPs
        'minimum_test_duration_days': 14,
        'recommended_initial_cpps': 5,  # start with 5, scale based on data
        'review_cadence_weeks': 4,  # review CPP performance monthly
    }

    def __init__(self):
        """Initialize CPP planner."""
        self.planned_cpps = []

    def identify_cpp_opportunities(
        self,
        app_info: Dict[str, Any],
        keywords: List[Dict[str, Any]],
        competitors: Optional[List[Dict[str, Any]]] = None
    ) -> Dict[str, Any]:
        """
        Analyze keyword clusters and user segments to suggest CPP themes.

        Args:
            app_info: Dict with 'name', 'category', 'features', 'target_audiences'
            keywords: List of keyword dicts with 'keyword', 'search_volume', 'relevance_score'
            competitors: Optional list of competitor data

        Returns:
            Prioritized list of CPP opportunities with rationale
        """
        opportunities = []

        # 1. Keyword-cluster based CPPs
        keyword_clusters = self._cluster_keywords(keywords)
        for cluster_name, cluster_keywords in keyword_clusters.items():
            total_volume = sum(kw.get('search_volume', 0) for kw in cluster_keywords)
            avg_relevance = (
                sum(kw.get('relevance_score', 0.5) for kw in cluster_keywords)
                / max(len(cluster_keywords), 1)
            )
            opportunities.append({
                'type': 'keyword_cluster',
                'name': f"CPP: {cluster_name.replace('_', ' ').title()}",
                'theme': cluster_name,
                'target_keywords': [kw['keyword'] for kw in cluster_keywords[:5]],
                'estimated_search_volume': total_volume,
                'relevance': round(avg_relevance, 2),
                'rationale': f"Cluster of {len(cluster_keywords)} related keywords "
                           f"with combined volume ~{total_volume:,}",
            })

        # 2. Audience-segment based CPPs
        target_audiences = app_info.get('target_audiences', [])
        features = app_info.get('features', [])
        for audience in target_audiences:
            audience_key = audience.lower().replace(' ', '_')
            template = self.AUDIENCE_TEMPLATES.get(audience_key, {})
            opportunities.append({
                'type': 'audience_segment',
                'name': f"CPP: {audience}",
                'theme': audience_key,
                'target_keywords': [],  # filled during planning
                'estimated_search_volume': 0,
                'relevance': 0.8,
                'rationale': template.get(
                    'description',
                    f"Tailored landing page for {audience} audience"
                ),
            })

        # 3. Feature-specific CPPs (for apps with 3+ distinct features)
        if len(features) >= 3:
            for feature in features[:5]:
                opportunities.append({
                    'type': 'feature_specific',
                    'name': f"CPP: {feature}",
                    'theme': feature.lower().replace(' ', '_'),
                    'target_keywords': [],
                    'estimated_search_volume': 0,
                    'relevance': 0.7,
                    'rationale': f"Deep-dive page for users searching specifically for {feature}",
                })

        # 4. Competitor-gap CPPs
        if competitors:
            gaps = self._find_competitor_gaps(app_info, competitors)
            for gap in gaps[:3]:
                opportunities.append({
                    'type': 'competitor_gap',
                    'name': f"CPP: {gap['differentiator']}",
                    'theme': 'competitive_advantage',
                    'target_keywords': gap.get('keywords', []),
                    'estimated_search_volume': gap.get('volume', 0),
                    'relevance': 0.85,
                    'rationale': f"Capitalize on competitor weakness: {gap['description']}",
                })

        # Score and rank opportunities
        scored = self._score_opportunities(opportunities)
        return {
            'total_opportunities': len(scored),
            'recommended_count': min(len(scored), self.BENCHMARKS['recommended_initial_cpps']),
            'opportunities': scored,
            'max_cpps_allowed': self.MAX_CPPS,
            'benchmark_cvr_lift': f"{self.BENCHMARKS['average_cvr_lift']:.1%}",
            'implementation_note': (
                'Start with top 5 CPPs. Monitor for 4 weeks before expanding. '
                'CPPs now appear in organic search results (July 2025+).'
            ),
        }

    def plan_cpp_variants(
        self,
        cpp_opportunity: Dict[str, Any],
        app_info: Dict[str, Any]
    ) -> Dict[str, Any]:
        """
        Generate detailed CPP specification for a single opportunity.

        Args:
            cpp_opportunity: A single opportunity from identify_cpp_opportunities()
            app_info: App info dict

        Returns:
            Complete CPP specification with promotional text, screenshot guidance
        """
        theme = cpp_opportunity.get('theme', 'general')
        template = self.AUDIENCE_TEMPLATES.get(theme, {})
        app_name = app_info.get('name', 'App')

        # Generate promotional text variants (170 chars each)
        promo_variants = self._generate_promo_text_variants(
            app_name=app_name,
            theme=theme,
            keywords=cpp_opportunity.get('target_keywords', []),
            features=app_info.get('features', []),
        )

        # Screenshot strategy
        screenshot_strategy = {
            'total_screenshots': min(8, self.MAX_SCREENSHOTS_PER_SIZE),
            'first_three_framework': [
                'Screenshot 1: Primary value proposition for this audience/keyword',
                'Screenshot 2: Key feature that matches search intent',
                'Screenshot 3: Social proof or outcome demonstration',
            ],
            'remaining_screenshots': [
                'Screenshots 4-5: Supporting features',
                'Screenshots 6-8: Integration, customization, or workflow examples',
            ],
            'text_overlay_guidance': [
                'Headlines: 3-5 words max, bold, high contrast',
                'Subheadlines: 8-12 words, clarify the benefit',
                'Use language matching the target keywords',
            ],
            'theme_specific': template.get(
                'screenshot_strategy',
                'Focus on the specific use case or keyword intent'
            ),
        }

        # App preview video guidance
        video_guidance = {
            'recommended': True,
            'duration': '15-30 seconds',
            'first_3_seconds': (
                'Show the core value proposition for this CPP theme immediately. '
                'Users decide within 3 seconds whether to keep watching.'
            ),
            'content_focus': f"Demonstrate {theme.replace('_', ' ')} workflow or benefit",
        }

        spec = {
            'cpp_name': cpp_opportunity['name'],
            'theme': theme,
            'target_keywords': cpp_opportunity.get('target_keywords', []),
            'promotional_text_variants': promo_variants,
            'screenshot_strategy': screenshot_strategy,
            'video_guidance': video_guidance,
            'success_metrics': {
                'primary': 'Conversion rate (impressions → installs)',
                'secondary': 'Page view duration',
                'target_cvr_lift': f"{self.BENCHMARKS['average_cvr_lift']:.1%} minimum",
                'test_duration': f"{self.BENCHMARKS['minimum_test_duration_days']} days minimum",
            },
        }

        self.planned_cpps.append(spec)
        return spec

    def calculate_cpp_priority(
        self,
        opportunities: List[Dict[str, Any]]
    ) -> List[Dict[str, Any]]:
        """
        Rank CPP opportunities by potential impact.

        Args:
            opportunities: List from identify_cpp_opportunities()

        Returns:
            Sorted list with priority scores and implementation order
        """
        for i, opp in enumerate(opportunities):
            opp['implementation_order'] = i + 1
            opp['implementation_wave'] = (
                'Wave 1 (immediate)' if i < 3
                else 'Wave 2 (after initial data)' if i < 7
                else 'Wave 3 (optimization phase)'
            )
        return opportunities

    def generate_cpp_spec(
        self,
        app_info: Dict[str, Any],
        opportunities: List[Dict[str, Any]]
    ) -> Dict[str, Any]:
        """
        Generate complete CPP specification document data.

        Args:
            app_info: App info dict
            opportunities: Prioritized opportunities list

        Returns:
            Complete specification for all planned CPPs
        """
        specs = []
        for opp in opportunities[:self.BENCHMARKS['recommended_initial_cpps']]:
            spec = self.plan_cpp_variants(opp, app_info)
            specs.append(spec)

        return {
            'app_name': app_info.get('name', 'App'),
            'total_cpps_planned': len(specs),
            'max_cpps_available': self.MAX_CPPS,
            'cpps': specs,
            'implementation_timeline': {
                'week_1': 'Design and copywrite CPPs 1-3',
                'week_2': 'Design CPPs 4-5, submit CPPs 1-3 for review',
                'week_3': 'Launch CPPs 1-3, submit CPPs 4-5',
                'week_4': 'Monitor performance, optimize underperformers',
                'ongoing': f'Review every {self.BENCHMARKS["review_cadence_weeks"]} weeks',
            },
            'measurement_plan': {
                'primary_kpi': 'Conversion rate per CPP vs default listing',
                'secondary_kpis': [
                    'Impression share from organic search',
                    'Page view duration',
                    'Install rate by keyword cluster',
                ],
                'reporting_cadence': 'Weekly for first month, then monthly',
                'success_threshold': f'{self.BENCHMARKS["average_cvr_lift"]:.1%} CVR lift',
            },
            'apple_search_ads_integration': (
                'Each CPP can be linked to Apple Search Ads campaigns for '
                'keyword-targeted ad traffic. Use the same CPP for both organic '
                'and paid discovery to maintain messaging consistency.'
            ),
        }

    # --- Private helpers ---

    def _cluster_keywords(
        self,
        keywords: List[Dict[str, Any]]
    ) -> Dict[str, List[Dict[str, Any]]]:
        """Group keywords into thematic clusters based on common terms."""
        clusters = {}

        for kw_data in keywords:
            keyword = kw_data.get('keyword', '').lower()
            words = keyword.split()

            # Use the first significant word as cluster key
            cluster_key = None
            stop_words = {'app', 'best', 'free', 'top', 'new', 'the', 'and', 'for', 'with'}
            for word in words:
                if word not in stop_words and len(word) > 2:
                    cluster_key = word
                    break

            if cluster_key:
                if cluster_key not in clusters:
                    clusters[cluster_key] = []
                clusters[cluster_key].append(kw_data)

        # Only return clusters with 2+ keywords
        return {k: v for k, v in clusters.items() if len(v) >= 2}

    def _find_competitor_gaps(
        self,
        app_info: Dict[str, Any],
        competitors: List[Dict[str, Any]]
    ) -> List[Dict[str, Any]]:
        """Identify areas where competitors are weak that we can target with CPPs."""
        gaps = []
        our_features = set(f.lower() for f in app_info.get('features', []))

        for competitor in competitors:
            comp_features = set(f.lower() for f in competitor.get('features', []))
            unique_to_us = our_features - comp_features

            for feature in unique_to_us:
                gaps.append({
                    'differentiator': feature.title(),
                    'description': f"We offer {feature} while {competitor.get('name', 'competitor')} does not",
                    'keywords': [feature],
                    'volume': 0,
                })

        return gaps[:5]

    def _score_opportunities(
        self,
        opportunities: List[Dict[str, Any]]
    ) -> List[Dict[str, Any]]:
        """Score and sort opportunities by potential impact."""
        for opp in opportunities:
            volume_score = min(opp.get('estimated_search_volume', 0) / 50000, 1.0) * 40
            relevance_score = opp.get('relevance', 0.5) * 40
            type_bonus = {
                'keyword_cluster': 20,
                'competitor_gap': 15,
                'audience_segment': 10,
                'feature_specific': 5,
            }.get(opp.get('type', ''), 0)

            opp['priority_score'] = round(volume_score + relevance_score + type_bonus, 1)

        return sorted(opportunities, key=lambda x: x['priority_score'], reverse=True)

    def _generate_promo_text_variants(
        self,
        app_name: str,
        theme: str,
        keywords: List[str],
        features: List[str],
    ) -> List[Dict[str, Any]]:
        """Generate promotional text variants for a CPP (170 chars each)."""
        variants = []
        primary_kw = keywords[0] if keywords else theme.replace('_', ' ')
        primary_feature = features[0] if features else 'powerful features'

        templates = [
            f"Looking for the best {primary_kw}? {app_name} makes it simple. Try it free today.",
            f"Discover how {app_name} transforms your {primary_kw} experience with {primary_feature}.",
            f"{app_name}: the {primary_kw} solution trusted by thousands. Get started in seconds.",
        ]

        for i, text in enumerate(templates):
            truncated = text[:self.PROMO_TEXT_LIMIT]
            variants.append({
                'variant': f"Variant {chr(65 + i)}",
                'text': truncated,
                'length': len(truncated),
                'limit': self.PROMO_TEXT_LIMIT,
                'keywords_included': [kw for kw in keywords if kw.lower() in truncated.lower()],
            })

        return variants

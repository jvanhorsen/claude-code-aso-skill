"""
Metadata optimization module for App Store Optimization.
Optimizes titles, descriptions, and keyword fields with platform-specific character limit validation.
"""

from typing import Dict, List, Any, Optional, Tuple
import re


class MetadataOptimizer:
    """Optimizes app store metadata for maximum discoverability and conversion."""

    # Platform-specific character limits
    CHAR_LIMITS = {
        'apple': {
            'title': 30,
            'subtitle': 30,
            'promotional_text': 170,
            'description': 4000,
            'keywords': 100,
            'whats_new': 4000
        },
        'google': {
            'title': 50,
            'short_description': 80,
            'full_description': 4000
        }
    }

    def __init__(self, platform: str = 'apple'):
        """
        Initialize metadata optimizer.

        Args:
            platform: 'apple' or 'google'
        """
        if platform not in ['apple', 'google']:
            raise ValueError("Platform must be 'apple' or 'google'")

        self.platform = platform
        self.limits = self.CHAR_LIMITS[platform]

    def optimize_title(
        self,
        app_name: str,
        target_keywords: List[str],
        include_brand: bool = True
    ) -> Dict[str, Any]:
        """
        Optimize app title with keyword integration.

        Args:
            app_name: Your app's brand name
            target_keywords: List of keywords to potentially include
            include_brand: Whether to include brand name

        Returns:
            Optimized title options with analysis
        """
        max_length = self.limits['title']

        title_options = []

        # Option 1: Brand name only
        if include_brand:
            option1 = app_name[:max_length]
            title_options.append({
                'title': option1,
                'length': len(option1),
                'remaining_chars': max_length - len(option1),
                'keywords_included': [],
                'strategy': 'brand_only',
                'pros': ['Maximum brand recognition', 'Clean and simple'],
                'cons': ['No keyword targeting', 'Lower discoverability']
            })

        # Option 2: Brand + Primary Keyword
        if target_keywords:
            primary_keyword = target_keywords[0]
            option2 = self._build_title_with_keywords(
                app_name,
                [primary_keyword],
                max_length
            )
            if option2:
                title_options.append({
                    'title': option2,
                    'length': len(option2),
                    'remaining_chars': max_length - len(option2),
                    'keywords_included': [primary_keyword],
                    'strategy': 'brand_plus_primary',
                    'pros': ['Targets main keyword', 'Maintains brand identity'],
                    'cons': ['Limited keyword coverage']
                })

        # Option 3: Brand + Multiple Keywords (if space allows)
        if len(target_keywords) > 1:
            option3 = self._build_title_with_keywords(
                app_name,
                target_keywords[:2],
                max_length
            )
            if option3:
                title_options.append({
                    'title': option3,
                    'length': len(option3),
                    'remaining_chars': max_length - len(option3),
                    'keywords_included': target_keywords[:2],
                    'strategy': 'brand_plus_multiple',
                    'pros': ['Multiple keyword targets', 'Better discoverability'],
                    'cons': ['May feel cluttered', 'Less brand focus']
                })

        # Option 4: Keyword-first approach (for new apps)
        if target_keywords and not include_brand:
            option4 = " ".join(target_keywords[:2])[:max_length]
            title_options.append({
                'title': option4,
                'length': len(option4),
                'remaining_chars': max_length - len(option4),
                'keywords_included': target_keywords[:2],
                'strategy': 'keyword_first',
                'pros': ['Maximum SEO benefit', 'Clear functionality'],
                'cons': ['No brand recognition', 'Generic appearance']
            })

        return {
            'platform': self.platform,
            'max_length': max_length,
            'options': title_options,
            'recommendation': self._recommend_title_option(title_options)
        }

    def optimize_description(
        self,
        app_info: Dict[str, Any],
        target_keywords: List[str],
        description_type: str = 'full'
    ) -> Dict[str, Any]:
        """
        Optimize app description with keyword integration and conversion focus.

        Args:
            app_info: Dict with 'name', 'key_features', 'unique_value', 'target_audience'
            target_keywords: List of keywords to integrate naturally
            description_type: 'full', 'short' (Google), 'subtitle' (Apple)

        Returns:
            Optimized description with analysis
        """
        if description_type == 'short' and self.platform == 'google':
            return self._optimize_short_description(app_info, target_keywords)
        elif description_type == 'subtitle' and self.platform == 'apple':
            return self._optimize_subtitle(app_info, target_keywords)
        else:
            return self._optimize_full_description(app_info, target_keywords)

    def optimize_keyword_field(
        self,
        target_keywords: List[str],
        app_title: str = "",
        app_description: str = ""
    ) -> Dict[str, Any]:
        """
        Optimize Apple's 100-character keyword field.

        Rules:
        - No spaces between commas
        - No plural forms if singular exists
        - No duplicates
        - Keywords in title/subtitle are already indexed

        Args:
            target_keywords: List of target keywords
            app_title: Current app title (to avoid duplication)
            app_description: Current description (to check coverage)

        Returns:
            Optimized keyword field (comma-separated, no spaces)
        """
        if self.platform != 'apple':
            return {'error': 'Keyword field optimization only applies to Apple App Store'}

        max_length = self.limits['keywords']

        # Extract words already in title (these don't need to be in keyword field)
        title_words = set(app_title.lower().split()) if app_title else set()

        # Process keywords
        processed_keywords = []
        for keyword in target_keywords:
            keyword_lower = keyword.lower().strip()

            # Skip if already in title
            if keyword_lower in title_words:
                continue

            # Remove duplicates and process
            words = keyword_lower.split()
            for word in words:
                if word not in processed_keywords and word not in title_words:
                    processed_keywords.append(word)

        # Remove plurals if singular exists
        deduplicated = self._remove_plural_duplicates(processed_keywords)

        # Build keyword field within 100 character limit
        keyword_field = self._build_keyword_field(deduplicated, max_length)

        # Calculate keyword density in description
        density = self._calculate_coverage(target_keywords, app_description)

        return {
            'keyword_field': keyword_field,
            'length': len(keyword_field),
            'remaining_chars': max_length - len(keyword_field),
            'keywords_included': keyword_field.split(','),
            'keywords_count': len(keyword_field.split(',')),
            'keywords_excluded': [kw for kw in target_keywords if kw.lower() not in keyword_field],
            'description_coverage': density,
            'optimization_tips': [
                'Keywords in title are auto-indexed - no need to repeat',
                'Use singular forms only (Apple indexes plurals automatically)',
                'No spaces between commas to maximize character usage',
                'Update keyword field with each app update to test variations'
            ]
        }

    def validate_character_limits(
        self,
        metadata: Dict[str, str]
    ) -> Dict[str, Any]:
        """
        Validate all metadata fields against platform character limits.

        Args:
            metadata: Dictionary of field_name: value

        Returns:
            Validation report with errors and warnings
        """
        validation_results = {
            'is_valid': True,
            'errors': [],
            'warnings': [],
            'field_status': {}
        }

        for field_name, value in metadata.items():
            if field_name not in self.limits:
                validation_results['warnings'].append(
                    f"Unknown field '{field_name}' for {self.platform} platform"
                )
                continue

            max_length = self.limits[field_name]
            actual_length = len(value)
            remaining = max_length - actual_length

            field_status = {
                'value': value,
                'length': actual_length,
                'limit': max_length,
                'remaining': remaining,
                'is_valid': actual_length <= max_length,
                'usage_percentage': round((actual_length / max_length) * 100, 1)
            }

            validation_results['field_status'][field_name] = field_status

            if actual_length > max_length:
                validation_results['is_valid'] = False
                validation_results['errors'].append(
                    f"'{field_name}' exceeds limit: {actual_length}/{max_length} chars"
                )
            elif remaining > max_length * 0.2:  # More than 20% unused
                validation_results['warnings'].append(
                    f"'{field_name}' under-utilizes space: {remaining} chars remaining"
                )

        return validation_results

    def calculate_keyword_density(
        self,
        text: str,
        target_keywords: List[str]
    ) -> Dict[str, Any]:
        """
        Calculate keyword density in text.

        Args:
            text: Text to analyze
            target_keywords: Keywords to check

        Returns:
            Density analysis
        """
        text_lower = text.lower()
        total_words = len(text_lower.split())

        keyword_densities = {}
        for keyword in target_keywords:
            keyword_lower = keyword.lower()
            count = text_lower.count(keyword_lower)
            density = (count / total_words * 100) if total_words > 0 else 0

            keyword_densities[keyword] = {
                'occurrences': count,
                'density_percentage': round(density, 2),
                'status': self._assess_density(density)
            }

        # Overall assessment
        total_keyword_occurrences = sum(kw['occurrences'] for kw in keyword_densities.values())
        overall_density = (total_keyword_occurrences / total_words * 100) if total_words > 0 else 0

        return {
            'total_words': total_words,
            'keyword_densities': keyword_densities,
            'overall_keyword_density': round(overall_density, 2),
            'assessment': self._assess_overall_density(overall_density),
            'recommendations': self._generate_density_recommendations(keyword_densities)
        }

    def _build_title_with_keywords(
        self,
        app_name: str,
        keywords: List[str],
        max_length: int
    ) -> Optional[str]:
        """Build title combining app name and keywords within limit."""
        separators = [' - ', ': ', ' | ']

        for sep in separators:
            for kw in keywords:
                title = f"{app_name}{sep}{kw}"
                if len(title) <= max_length:
                    return title

        return None

    def _optimize_short_description(
        self,
        app_info: Dict[str, Any],
        target_keywords: List[str]
    ) -> Dict[str, Any]:
        """Optimize Google Play short description (80 chars)."""
        max_length = self.limits['short_description']

        # Focus on unique value proposition with primary keyword
        unique_value = app_info.get('unique_value', '')
        primary_keyword = target_keywords[0] if target_keywords else ''

        # Template: [Primary Keyword] - [Unique Value]
        short_desc = f"{primary_keyword.title()} - {unique_value}"[:max_length]

        return {
            'short_description': short_desc,
            'length': len(short_desc),
            'remaining_chars': max_length - len(short_desc),
            'keywords_included': [primary_keyword] if primary_keyword in short_desc.lower() else [],
            'strategy': 'keyword_value_proposition'
        }

    def _optimize_subtitle(
        self,
        app_info: Dict[str, Any],
        target_keywords: List[str]
    ) -> Dict[str, Any]:
        """Optimize Apple App Store subtitle (30 chars)."""
        max_length = self.limits['subtitle']

        # Very concise - primary keyword or key feature
        primary_keyword = target_keywords[0] if target_keywords else ''
        key_feature = app_info.get('key_features', [''])[0] if app_info.get('key_features') else ''

        options = [
            primary_keyword[:max_length],
            key_feature[:max_length],
            f"{primary_keyword} App"[:max_length]
        ]

        return {
            'subtitle_options': [opt for opt in options if opt],
            'max_length': max_length,
            'recommendation': options[0] if options else ''
        }

    def _optimize_full_description(
        self,
        app_info: Dict[str, Any],
        target_keywords: List[str]
    ) -> Dict[str, Any]:
        """Optimize full app description (4000 chars for both platforms)."""
        max_length = self.limits.get('description', self.limits.get('full_description', 4000))

        # Structure: Hook → Features → Benefits → Social Proof → CTA
        sections = []

        # Hook (with primary keyword)
        primary_keyword = target_keywords[0] if target_keywords else ''
        unique_value = app_info.get('unique_value', '')
        hook = f"{unique_value} {primary_keyword.title()} that helps you achieve more.\n\n"
        sections.append(hook)

        # Features (with keywords naturally integrated)
        features = app_info.get('key_features', [])
        if features:
            sections.append("KEY FEATURES:\n")
            for i, feature in enumerate(features[:5], 1):
                # Integrate keywords naturally
                feature_text = f"• {feature}"
                if i <= len(target_keywords):
                    keyword = target_keywords[i-1]
                    if keyword.lower() not in feature.lower():
                        feature_text = f"• {feature} with {keyword}"
                sections.append(f"{feature_text}\n")
            sections.append("\n")

        # Benefits
        target_audience = app_info.get('target_audience', 'users')
        sections.append(f"PERFECT FOR:\n{target_audience}\n\n")

        # Social proof placeholder
        sections.append("WHY USERS LOVE US:\n")
        sections.append("Join thousands of satisfied users who have transformed their workflow.\n\n")

        # CTA
        sections.append("Download now and start experiencing the difference!")

        # Combine and validate length
        full_description = "".join(sections)
        if len(full_description) > max_length:
            full_description = full_description[:max_length-3] + "..."

        # Calculate keyword density
        density = self.calculate_keyword_density(full_description, target_keywords)

        return {
            'full_description': full_description,
            'length': len(full_description),
            'remaining_chars': max_length - len(full_description),
            'keyword_analysis': density,
            'structure': {
                'has_hook': True,
                'has_features': len(features) > 0,
                'has_benefits': True,
                'has_cta': True
            }
        }

    def _remove_plural_duplicates(self, keywords: List[str]) -> List[str]:
        """Remove plural forms if singular exists."""
        deduplicated = []
        singular_set = set()

        for keyword in keywords:
            if keyword.endswith('s') and len(keyword) > 1:
                singular = keyword[:-1]
                if singular not in singular_set:
                    deduplicated.append(singular)
                    singular_set.add(singular)
            else:
                if keyword not in singular_set:
                    deduplicated.append(keyword)
                    singular_set.add(keyword)

        return deduplicated

    def _build_keyword_field(self, keywords: List[str], max_length: int) -> str:
        """Build comma-separated keyword field within character limit."""
        keyword_field = ""

        for keyword in keywords:
            test_field = f"{keyword_field},{keyword}" if keyword_field else keyword
            if len(test_field) <= max_length:
                keyword_field = test_field
            else:
                break

        return keyword_field

    def _calculate_coverage(self, keywords: List[str], text: str) -> Dict[str, int]:
        """Calculate how many keywords are covered in text."""
        text_lower = text.lower()
        coverage = {}

        for keyword in keywords:
            coverage[keyword] = text_lower.count(keyword.lower())

        return coverage

    def _assess_density(self, density: float) -> str:
        """Assess individual keyword density."""
        if density < 0.5:
            return "too_low"
        elif density <= 2.5:
            return "optimal"
        else:
            return "too_high"

    def _assess_overall_density(self, density: float) -> str:
        """Assess overall keyword density."""
        if density < 2:
            return "Under-optimized: Consider adding more keyword variations"
        elif density <= 5:
            return "Optimal: Good keyword integration without stuffing"
        elif density <= 8:
            return "High: Approaching keyword stuffing - reduce keyword usage"
        else:
            return "Too High: Keyword stuffing detected - rewrite for natural flow"

    def _generate_density_recommendations(
        self,
        keyword_densities: Dict[str, Dict[str, Any]]
    ) -> List[str]:
        """Generate recommendations based on keyword density analysis."""
        recommendations = []

        for keyword, data in keyword_densities.items():
            if data['status'] == 'too_low':
                recommendations.append(
                    f"Increase usage of '{keyword}' - currently only {data['occurrences']} times"
                )
            elif data['status'] == 'too_high':
                recommendations.append(
                    f"Reduce usage of '{keyword}' - appears {data['occurrences']} times (keyword stuffing risk)"
                )

        if not recommendations:
            recommendations.append("Keyword density is well-balanced")

        return recommendations

    def _recommend_title_option(self, options: List[Dict[str, Any]]) -> str:
        """Recommend best title option based on strategy."""
        if not options:
            return "No valid options available"

        # Prefer brand_plus_primary for established apps
        for option in options:
            if option['strategy'] == 'brand_plus_primary':
                return f"Recommended: '{option['title']}' (Balance of brand and SEO)"

        # Fallback to first option
        return f"Recommended: '{options[0]['title']}' ({options[0]['strategy']})"

    # -------------------------------------------------------------------------
    # Visual Asset Optimization
    # -------------------------------------------------------------------------

    # Screenshot specifications by platform and device
    SCREENSHOT_SPECS = {
        'apple': {
            'iphone_6_7': {'size': '1290x2796', 'label': 'iPhone 6.7"', 'required': True},
            'iphone_6_5': {'size': '1284x2778', 'label': 'iPhone 6.5"', 'required': False},
            'iphone_5_5': {'size': '1242x2208', 'label': 'iPhone 5.5"', 'required': False},
            'ipad_pro_12_9': {'size': '2048x2732', 'label': 'iPad Pro 12.9"', 'required': False},
            'min_screenshots': 3,
            'max_screenshots': 10,
            'recommended_screenshots': 8,
        },
        'google': {
            'phone': {'size': '1080x1920 (min)', 'label': 'Phone', 'required': True},
            'tablet_7': {'size': '1080x1920', 'label': '7" Tablet', 'required': False},
            'tablet_10': {'size': '1080x1920', 'label': '10" Tablet', 'required': False},
            'feature_graphic': {'size': '1024x500', 'label': 'Feature Graphic', 'required': True},
            'min_screenshots': 2,
            'max_screenshots': 8,
            'recommended_screenshots': 6,
        }
    }

    # Category-specific screenshot orientation recommendations
    CATEGORY_ORIENTATION = {
        'games': 'landscape',
        'entertainment': 'landscape',
        'photo_video': 'portrait',
        'social_networking': 'portrait',
        'productivity': 'portrait',
        'business': 'portrait',
        'education': 'portrait',
        'health_fitness': 'portrait',
        'finance': 'portrait',
        'music': 'portrait',
        'travel': 'portrait',
        'food_drink': 'portrait',
        'shopping': 'portrait',
        'utilities': 'portrait',
        'weather': 'portrait',
        'navigation': 'landscape',
        'default': 'portrait',
    }

    def generate_screenshot_strategy(
        self,
        app_info: Dict[str, Any],
        platform: Optional[str] = None
    ) -> Dict[str, Any]:
        """
        Generate comprehensive screenshot optimization strategy.

        Covers: screenshot count, ordering framework, text overlay guidance,
        orientation, app preview video tips, and A/B testing recommendations.

        Args:
            app_info: Dict with 'name', 'category', 'key_features',
                      'unique_value', 'target_audience', 'has_ipad' (bool)
            platform: Override platform (default: self.platform)

        Returns:
            Complete screenshot strategy with actionable guidance.
        """
        plat = platform or self.platform
        specs = self.SCREENSHOT_SPECS.get(plat, self.SCREENSHOT_SPECS['apple'])
        category = app_info.get('category', 'default').lower().replace(' ', '_').replace('&', '_')
        orientation = self.CATEGORY_ORIENTATION.get(category, self.CATEGORY_ORIENTATION['default'])
        features = app_info.get('key_features', [])
        has_ipad = app_info.get('has_ipad', False)

        # Build the first-3-screenshot framework (7-second attention window)
        first_three = self._build_first_three_framework(app_info)

        # Build full screenshot sequence
        full_sequence = self._build_full_screenshot_sequence(app_info, specs)

        # Text overlay guidelines
        text_overlay = self._generate_text_overlay_guidelines(plat)

        # App preview video strategy
        video_strategy = self._generate_video_strategy(plat, app_info)

        # Device coverage
        device_coverage = self._generate_device_coverage(plat, has_ipad)

        # A/B testing recommendations for visuals
        ab_visual = self._generate_visual_ab_tests()

        return {
            'platform': plat,
            'orientation': orientation,
            'orientation_rationale': (
                f"'{category}' category apps perform best with {orientation} screenshots. "
                f"{'Games and media apps benefit from landscape to show immersive content.' if orientation == 'landscape' else 'Utility and productivity apps perform best in portrait to match natural phone usage.'}"
            ),
            'screenshot_count': {
                'minimum': specs['min_screenshots'],
                'maximum': specs['max_screenshots'],
                'recommended': specs['recommended_screenshots'],
                'rationale': (
                    f"Use {specs['recommended_screenshots']} screenshots to tell a complete story. "
                    f"First 3 are critical — they appear in search results and determine 70% of conversion decisions."
                )
            },
            'first_three_framework': first_three,
            'full_sequence': full_sequence,
            'text_overlay_guidelines': text_overlay,
            'video_strategy': video_strategy,
            'device_coverage': device_coverage,
            'ab_testing_visuals': ab_visual,
            'key_principles': [
                'First 3 screenshots drive 70% of install decisions — make them count',
                'Each screenshot should convey ONE clear benefit in under 2 seconds',
                'Text overlays must be readable at thumbnail size (search results)',
                'Show real app UI — avoid stock photos or abstract graphics',
                'Use consistent visual branding across all screenshots',
                'Dark mode screenshots can be a differentiator if competitors use light only',
                'Seasonal screenshot updates (2-4x/year) keep the listing fresh'
            ]
        }

    def _build_first_three_framework(self, app_info: Dict[str, Any]) -> List[Dict[str, str]]:
        """
        Build the critical first-3-screenshot framework.

        Framework: Hero Value Prop → Key Differentiator → Social Proof / Wow Moment
        Users spend ~7 seconds on a listing; first 3 screenshots must convert.
        """
        unique_value = app_info.get('unique_value', 'your core value')
        features = app_info.get('key_features', ['key feature'])
        name = app_info.get('name', 'App')

        return [
            {
                'position': 1,
                'purpose': 'Hero — Primary Value Proposition',
                'guidance': (
                    f"Show {name}'s single most compelling screen with a bold headline "
                    f"communicating: '{unique_value}'. This screenshot alone must answer "
                    f"'Why should I install this?' Use the app's signature screen."
                ),
                'headline_tip': 'Keep headline to 3-5 words. Benefit-focused, not feature-focused.',
                'example_headline_pattern': '[Verb] + [Desired Outcome]',
                'cvr_impact': '30-40% of conversion decision happens here'
            },
            {
                'position': 2,
                'purpose': 'Key Differentiator — What Makes You Different',
                'guidance': (
                    f"Highlight the feature that competitors lack: "
                    f"'{features[0] if features else 'unique feature'}'. "
                    f"Show this feature in action within the real app UI."
                ),
                'headline_tip': 'Frame as a benefit the user gets, not a feature name.',
                'example_headline_pattern': '[Feature Benefit] in [Timeframe/Ease]',
                'cvr_impact': '20-25% of conversion decision'
            },
            {
                'position': 3,
                'purpose': 'Social Proof or Wow Moment',
                'guidance': (
                    "Either show a visually impressive result/output from the app "
                    "(the 'wow' moment), OR include social proof (rating callout, "
                    "user count, award badge). Social proof builds trust for users "
                    "still on the fence after screenshots 1-2."
                ),
                'headline_tip': 'Use numbers or quotes for social proof. Use "before/after" for wow moments.',
                'example_headline_pattern': '"[User Quote]" or [Number]+ Users Love It',
                'cvr_impact': '10-15% of conversion decision'
            }
        ]

    def _build_full_screenshot_sequence(
        self,
        app_info: Dict[str, Any],
        specs: Dict[str, Any]
    ) -> List[Dict[str, str]]:
        """Build recommended full screenshot sequence beyond the first 3."""
        features = app_info.get('key_features', [])
        recommended = specs.get('recommended_screenshots', 8)

        sequence = [
            {'position': 1, 'type': 'Hero value proposition'},
            {'position': 2, 'type': 'Key differentiator feature'},
            {'position': 3, 'type': 'Social proof / wow moment'},
        ]

        # Positions 4+ cycle through remaining features
        remaining_types = [
            'Secondary feature highlight',
            'Workflow / multi-step process',
            'Customization / personalization options',
            'Integration / ecosystem (widgets, watch, etc.)',
            'Settings / accessibility features',
            'Before/after or results showcase',
            'Pricing / free tier value summary',
        ]

        for i, stype in enumerate(remaining_types):
            pos = i + 4
            if pos > recommended:
                break
            feature_ref = features[min(i + 1, len(features) - 1)] if features else 'additional feature'
            sequence.append({
                'position': pos,
                'type': stype,
                'feature_to_highlight': feature_ref
            })

        return sequence

    def _generate_text_overlay_guidelines(self, platform: str) -> Dict[str, Any]:
        """Generate platform-specific text overlay best practices."""
        return {
            'general_rules': [
                'Maximum 5-7 words per headline — must be readable at thumbnail size',
                'Use bold, sans-serif fonts (SF Pro for Apple, Google Sans / Roboto for Google)',
                'High contrast: dark text on light background or vice versa',
                'Text should occupy no more than 20-25% of screenshot area',
                'Consistent font size and positioning across all screenshots',
                'Avoid text over complex UI areas — use solid color bars or gradients',
            ],
            'font_size_guidance': {
                'headline': '48-72pt (at 1290x2796 canvas)',
                'subheadline': '32-42pt',
                'callout': '24-32pt',
            },
            'positioning': {
                'top_text': 'Best for headlines — visible in search result thumbnails',
                'bottom_text': 'Good for supplementary text — may be cut off in some placements',
                'overlay_bar': 'Colored bar behind text improves readability on busy screenshots',
            },
            'platform_specific': {
                'apple': 'Apple review guidelines prohibit excessive text overlays. Keep text minimal and ensure the app UI is the focus.',
                'google': 'Google allows more text flexibility. Emoji in text overlays can improve engagement. Feature graphic (1024x500) is text-heavy by design.',
            }.get(platform, ''),
            'common_mistakes': [
                'Text too small to read in search results (thumbnail view)',
                'Using feature names instead of benefits as headlines',
                'Inconsistent visual style across screenshots',
                'Too much text obscuring the actual app UI',
                'Low contrast text that disappears against the app background',
            ]
        }

    def _generate_video_strategy(
        self,
        platform: str,
        app_info: Dict[str, Any]
    ) -> Dict[str, Any]:
        """Generate app preview / promo video strategy."""
        name = app_info.get('name', 'App')

        base = {
            'recommended': True,
            'rationale': (
                'App preview videos increase conversion rate by 15-25% on average. '
                'They auto-play on WiFi in the App Store, making them a powerful '
                'attention-grabbing tool.'
            ),
            'structure': [
                {'time': '0-3s', 'content': f'Hook — show {name}\'s most impressive screen or result', 'importance': 'CRITICAL — 50% of viewers drop off after 3 seconds'},
                {'time': '3-10s', 'content': 'Core workflow — demonstrate the primary use case end-to-end', 'importance': 'High — proves the app delivers on its promise'},
                {'time': '10-20s', 'content': 'Secondary features — show 2-3 additional capabilities', 'importance': 'Medium — adds depth for engaged viewers'},
                {'time': '20-30s', 'content': 'Call to action — end with value summary or social proof', 'importance': 'Medium — reinforces the install decision'},
            ],
            'best_practices': [
                'First 3 seconds determine if users keep watching — lead with your best',
                'Show real app usage, not animations or marketing graphics',
                'Add subtitles — most videos auto-play without sound',
                'Record at device resolution for crisp quality',
                'Keep it under 30 seconds — shorter is better',
                'End with a clear call to action frame',
            ]
        }

        if platform == 'apple':
            base['specs'] = {
                'duration': '15-30 seconds',
                'format': 'H.264 or Apple ProRes, .mov or .mp4',
                'max_count': '3 per device size',
                'note': 'Auto-plays on WiFi in App Store. First frame is the poster frame — make it compelling.'
            }
        else:
            base['specs'] = {
                'duration': '30 seconds - 2 minutes',
                'format': 'YouTube link or direct upload',
                'max_count': '1 promo video',
                'note': 'Shown as first visual in listing. YouTube thumbnail is the poster — customize it.'
            }

        return base

    def _generate_device_coverage(self, platform: str, has_ipad: bool) -> Dict[str, Any]:
        """Generate device coverage recommendations."""
        specs = self.SCREENSHOT_SPECS.get(platform, {})

        required_devices = []
        optional_devices = []

        for key, spec in specs.items():
            if isinstance(spec, dict) and 'label' in spec:
                entry = {'device': spec['label'], 'size': spec['size']}
                if spec.get('required'):
                    required_devices.append(entry)
                else:
                    # iPad is optional but recommended if app supports it
                    if 'iPad' in spec['label'] and not has_ipad:
                        continue
                    optional_devices.append(entry)

        return {
            'required': required_devices,
            'optional': optional_devices,
            'recommendation': (
                f"Always provide screenshots for all required device sizes. "
                f"{'Include iPad screenshots — iPad users convert at 1.5x the rate of phone users.' if has_ipad else 'iPad screenshots are optional if your app is iPhone-only.'} "
                f"Apple auto-scales between sizes but custom screenshots per size look significantly better."
            )
        }

    def _generate_visual_ab_tests(self) -> List[Dict[str, Any]]:
        """Generate A/B testing recommendations for visual assets."""
        return [
            {
                'test': 'First Screenshot Variant',
                'priority': 1,
                'cvr_impact': '10-20%',
                'what_to_test': 'Headline copy, background color, featured screen',
                'duration': '14 days minimum',
                'traffic': '50/50 split',
                'tip': 'Only change ONE element per test to isolate impact.'
            },
            {
                'test': 'App Icon Variant',
                'priority': 2,
                'cvr_impact': '15-30%',
                'what_to_test': 'Color scheme, symbol vs text, background style',
                'duration': '14 days minimum',
                'traffic': '50/50 split',
                'tip': 'Icon is the MOST viewed asset. Test at 60x60px (actual display size) — details invisible at that scale.'
            },
            {
                'test': 'Screenshot Sequence Order',
                'priority': 3,
                'cvr_impact': '5-15%',
                'what_to_test': 'Different feature ordering in positions 2-5',
                'duration': '14 days minimum',
                'traffic': '50/50 split',
                'tip': 'Lead with the feature that resonates most with your largest user segment.'
            },
            {
                'test': 'Dark Mode vs Light Mode Screenshots',
                'priority': 4,
                'cvr_impact': '3-8%',
                'what_to_test': 'Full dark mode set vs full light mode set',
                'duration': '14 days minimum',
                'traffic': '50/50 split',
                'tip': 'Dark mode stands out in search results where most competitors use light backgrounds.'
            }
        ]


def optimize_app_metadata(
    platform: str,
    app_info: Dict[str, Any],
    target_keywords: List[str]
) -> Dict[str, Any]:
    """
    Convenience function to optimize all metadata fields.

    Args:
        platform: 'apple' or 'google'
        app_info: App information dictionary
        target_keywords: Target keywords list

    Returns:
        Complete metadata optimization package
    """
    optimizer = MetadataOptimizer(platform)

    return {
        'platform': platform,
        'title': optimizer.optimize_title(
            app_info['name'],
            target_keywords
        ),
        'description': optimizer.optimize_description(
            app_info,
            target_keywords,
            'full'
        ),
        'keyword_field': optimizer.optimize_keyword_field(
            target_keywords
        ) if platform == 'apple' else None
    }

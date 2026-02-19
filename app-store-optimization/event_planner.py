"""
In-App Events and Promotional Content planning module for App Store Optimization.
Helps plan, schedule, and generate metadata for Apple In-App Events and
Google Play Promotional Content.

Apple In-App Events:
- Up to 10 events per app, 5 published simultaneously
- Events appear in App Store search results, editorial, and personalized recommendations
- Event types: Challenge, Competition, Live Event, Major Update, New Season, Premiere, Special Event
- Character limits: Event Name 30, Short Description 50, Long Description 120

Google Play Promotional Content:
- Promotional content cards appear on app listing and Google Play home
- Used for time-limited offers, events, and major updates
"""

from typing import Dict, List, Any, Optional
from datetime import datetime, timedelta
import calendar


class EventPlanner:
    """Plans and generates In-App Events and Promotional Content for app stores."""

    # Apple In-App Event constraints
    APPLE_LIMITS = {
        'max_events': 10,
        'max_published': 5,
        'event_name': 30,  # chars
        'short_description': 50,  # chars
        'long_description': 120,  # chars
        'max_duration_days': 31,
    }

    # Apple event badge types
    EVENT_BADGES = [
        'challenge',
        'competition',
        'live_event',
        'major_update',
        'new_season',
        'premiere',
        'special_event',
    ]

    # Seasonal event opportunities by month
    SEASONAL_CALENDAR = {
        1: {'name': 'New Year', 'themes': ['fresh start', 'goals', 'resolutions', 'organize']},
        2: {'name': 'Valentine\'s Day', 'themes': ['love', 'connection', 'sharing', 'couples']},
        3: {'name': 'Spring', 'themes': ['renewal', 'spring cleaning', 'fresh', 'outdoor']},
        4: {'name': 'Earth Day / Spring', 'themes': ['sustainability', 'nature', 'wellness']},
        5: {'name': 'Mental Health / Summer Prep', 'themes': ['mindfulness', 'health', 'summer']},
        6: {'name': 'WWDC / Summer', 'themes': ['new features', 'iOS update', 'summer']},
        7: {'name': 'Summer', 'themes': ['vacation', 'travel', 'outdoor', 'fitness']},
        8: {'name': 'Back to School', 'themes': ['education', 'productivity', 'study', 'organize']},
        9: {'name': 'Fall / iPhone Launch', 'themes': ['new iPhone', 'iOS update', 'autumn']},
        10: {'name': 'Halloween', 'themes': ['spooky', 'themed', 'seasonal', 'creative']},
        11: {'name': 'Black Friday / Thanksgiving', 'themes': ['deals', 'gratitude', 'holiday prep']},
        12: {'name': 'Holiday Season', 'themes': ['gift', 'year in review', 'holiday', 'celebration']},
    }

    # Category-to-event-type mapping (common patterns)
    CATEGORY_EVENT_PATTERNS = {
        'fitness': ['challenge', 'new_season', 'live_event'],
        'productivity': ['major_update', 'challenge', 'special_event'],
        'games': ['competition', 'new_season', 'live_event', 'premiere'],
        'education': ['challenge', 'major_update', 'premiere'],
        'social': ['live_event', 'special_event', 'competition'],
        'health': ['challenge', 'special_event', 'major_update'],
        'lifestyle': ['special_event', 'new_season', 'premiere'],
        'finance': ['major_update', 'special_event', 'challenge'],
        'entertainment': ['premiere', 'live_event', 'new_season'],
        'travel': ['special_event', 'new_season', 'major_update'],
    }

    def __init__(self):
        """Initialize event planner."""
        self.planned_events = []

    def plan_event_calendar(
        self,
        app_info: Dict[str, Any],
        start_date: Optional[str] = None,
        months_ahead: int = 6
    ) -> Dict[str, Any]:
        """
        Generate a seasonal event schedule with specific dates.

        Args:
            app_info: Dict with 'name', 'category', 'features', 'target_audiences'
            start_date: ISO date string (YYYY-MM-DD), defaults to today
            months_ahead: How many months to plan ahead

        Returns:
            Event calendar with specific dates and event specifications
        """
        if start_date:
            current_date = datetime.strptime(start_date, '%Y-%m-%d')
        else:
            current_date = datetime.now()

        app_name = app_info.get('name', 'App')
        category = app_info.get('category', 'general').lower()
        features = app_info.get('features', [])

        events = []
        for month_offset in range(months_ahead):
            event_month = current_date.month + month_offset
            event_year = current_date.year + (event_month - 1) // 12
            event_month = ((event_month - 1) % 12) + 1

            seasonal = self.SEASONAL_CALENDAR.get(event_month, {})
            month_name = calendar.month_name[event_month]

            # Determine best event type for this category
            event_types = self.CATEGORY_EVENT_PATTERNS.get(category, ['special_event'])
            badge = event_types[month_offset % len(event_types)]

            # Calculate event dates
            # Start mid-month to align with seasonal relevance
            start_day = 15 if month_offset > 0 else max(current_date.day + 3, 15)
            start_day = min(start_day, 28)  # safe for all months
            event_start = datetime(event_year, event_month, start_day)
            event_end = event_start + timedelta(days=14)  # 2-week events

            event = {
                'month': f"{month_name} {event_year}",
                'event_start': event_start.strftime('%Y-%m-%d'),
                'event_end': event_end.strftime('%Y-%m-%d'),
                'seasonal_hook': seasonal.get('name', month_name),
                'themes': seasonal.get('themes', []),
                'badge_type': badge,
                'event_name': '',  # filled by generate_event_metadata
                'short_description': '',
                'long_description': '',
            }

            # Generate metadata for this event
            metadata = self.generate_event_metadata(
                app_name=app_name,
                badge_type=badge,
                seasonal_hook=seasonal.get('name', month_name),
                themes=seasonal.get('themes', []),
                features=features,
            )
            event.update(metadata)
            events.append(event)

        # Trim to max simultaneous limit
        return {
            'app_name': app_name,
            'planning_period': f"{current_date.strftime('%B %Y')} – {events[-1]['month']}",
            'total_events_planned': len(events),
            'max_simultaneous': self.APPLE_LIMITS['max_published'],
            'events': events,
            'implementation_notes': [
                f'Apple allows {self.APPLE_LIMITS["max_events"]} events total, '
                f'{self.APPLE_LIMITS["max_published"]} published simultaneously.',
                'Events appear in search results, increasing organic visibility.',
                'Schedule events at least 2 weeks before start date for review.',
                'Use event cards in Apple Search Ads for additional reach.',
                'Monitor event page views and impressions in App Store Connect.',
            ],
            'google_play_equivalent': {
                'feature': 'Promotional Content',
                'description': (
                    'Google Play offers Promotional Content cards for similar purposes. '
                    'Use the same event themes but adapt copy for Google Play guidelines.'
                ),
            },
        }

    def generate_event_metadata(
        self,
        app_name: str,
        badge_type: str,
        seasonal_hook: str,
        themes: List[str],
        features: List[str],
    ) -> Dict[str, Any]:
        """
        Generate event name, short description, and long description.

        Character limits:
        - Event Name: 30 chars
        - Short Description: 50 chars
        - Long Description: 120 chars

        Args:
            app_name: App name
            badge_type: One of EVENT_BADGES
            seasonal_hook: Seasonal context (e.g., "New Year")
            themes: Related themes
            features: App features to highlight

        Returns:
            Event metadata with character-validated content
        """
        primary_theme = themes[0] if themes else 'special'
        primary_feature = features[0] if features else 'new features'
        badge_label = badge_type.replace('_', ' ').title()

        # Generate event name (30 chars)
        name_options = [
            f"{seasonal_hook} {badge_label}",
            f"{app_name} {seasonal_hook}",
            f"{primary_theme.title()} {badge_label}",
        ]
        event_name = ''
        for name in name_options:
            if len(name) <= self.APPLE_LIMITS['event_name']:
                event_name = name
                break
        if not event_name:
            event_name = name_options[0][:self.APPLE_LIMITS['event_name']]

        # Generate short description (50 chars)
        short_options = [
            f"Join our {seasonal_hook.lower()} {badge_type.replace('_', ' ')}!",
            f"Explore {primary_theme} with {app_name}.",
            f"New {primary_feature.lower()} for {seasonal_hook.lower()}.",
        ]
        short_desc = ''
        for desc in short_options:
            if len(desc) <= self.APPLE_LIMITS['short_description']:
                short_desc = desc
                break
        if not short_desc:
            short_desc = short_options[0][:self.APPLE_LIMITS['short_description']]

        # Generate long description (120 chars)
        long_options = [
            f"Celebrate {seasonal_hook.lower()} with {app_name}! "
            f"Discover {primary_feature.lower()} and take your experience to the next level.",
            f"Our {badge_type.replace('_', ' ')} brings {primary_theme} "
            f"to {app_name}. Don't miss exclusive content and features.",
        ]
        long_desc = ''
        for desc in long_options:
            if len(desc) <= self.APPLE_LIMITS['long_description']:
                long_desc = desc
                break
        if not long_desc:
            long_desc = long_options[0][:self.APPLE_LIMITS['long_description']]

        return {
            'event_name': event_name,
            'event_name_length': len(event_name),
            'event_name_limit': self.APPLE_LIMITS['event_name'],
            'short_description': short_desc,
            'short_description_length': len(short_desc),
            'short_description_limit': self.APPLE_LIMITS['short_description'],
            'long_description': long_desc,
            'long_description_length': len(long_desc),
            'long_description_limit': self.APPLE_LIMITS['long_description'],
            'badge_type': badge_type,
        }

    def identify_event_types(
        self,
        app_category: str,
        app_features: List[str]
    ) -> List[Dict[str, Any]]:
        """
        Recommend the most effective event types for this app.

        Args:
            app_category: App Store category
            app_features: List of app features

        Returns:
            Ranked list of event types with rationale
        """
        category = app_category.lower()
        recommended_types = self.CATEGORY_EVENT_PATTERNS.get(
            category, ['special_event', 'major_update']
        )

        event_descriptions = {
            'challenge': {
                'name': 'Challenge',
                'description': 'Time-limited goal for users to complete',
                'best_for': 'Fitness, education, productivity apps',
                'example': '30-Day Fitness Challenge, Weekly Reading Goal',
            },
            'competition': {
                'name': 'Competition',
                'description': 'Competitive event between users',
                'best_for': 'Games, fitness, social apps',
                'example': 'Weekly Leaderboard Battle, Tournament',
            },
            'live_event': {
                'name': 'Live Event',
                'description': 'Real-time experience happening at a specific time',
                'best_for': 'Social, entertainment, fitness apps',
                'example': 'Live Workout Class, Live Q&A, Watch Party',
            },
            'major_update': {
                'name': 'Major Update',
                'description': 'Significant new features or content',
                'best_for': 'All categories',
                'example': 'Version 3.0 Launch, AI Features Release',
            },
            'new_season': {
                'name': 'New Season',
                'description': 'New content season or themed period',
                'best_for': 'Games, fitness, lifestyle apps',
                'example': 'Summer Season Content, New Workout Programs',
            },
            'premiere': {
                'name': 'Premiere',
                'description': 'First availability of new content or feature',
                'best_for': 'Entertainment, education, creative apps',
                'example': 'New Course Series, Exclusive Content Drop',
            },
            'special_event': {
                'name': 'Special Event',
                'description': 'Unique occasion or celebration',
                'best_for': 'All categories',
                'example': 'Anniversary Celebration, Holiday Special',
            },
        }

        results = []
        for event_type in self.EVENT_BADGES:
            info = event_descriptions.get(event_type, {})
            is_recommended = event_type in recommended_types
            priority = recommended_types.index(event_type) + 1 if is_recommended else 99

            results.append({
                'event_type': event_type,
                'name': info.get('name', event_type.replace('_', ' ').title()),
                'description': info.get('description', ''),
                'best_for': info.get('best_for', ''),
                'example': info.get('example', ''),
                'recommended_for_category': is_recommended,
                'priority': priority,
            })

        return sorted(results, key=lambda x: x['priority'])

    def suggest_seasonal_events(
        self,
        app_category: str,
        target_month: int
    ) -> List[Dict[str, Any]]:
        """
        Map app category to seasonal event opportunities for a specific month.

        Args:
            app_category: App Store category
            target_month: Month number (1-12)

        Returns:
            List of seasonal event suggestions
        """
        seasonal = self.SEASONAL_CALENDAR.get(target_month, {})
        category = app_category.lower()
        event_types = self.CATEGORY_EVENT_PATTERNS.get(category, ['special_event'])
        month_name = calendar.month_name[target_month]

        suggestions = []
        for theme in seasonal.get('themes', []):
            for event_type in event_types[:2]:
                suggestions.append({
                    'month': month_name,
                    'seasonal_hook': seasonal.get('name', month_name),
                    'theme': theme,
                    'event_type': event_type,
                    'suggestion': f"{theme.title()} {event_type.replace('_', ' ').title()}",
                    'rationale': (
                        f"Align {category} app with {seasonal.get('name', month_name)} "
                        f"interest in {theme}"
                    ),
                })

        return suggestions

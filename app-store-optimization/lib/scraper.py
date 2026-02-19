"""
WebFetch prompt generators for App Store and Google Play Store scraping.
Used by ASO agents as fallback when iTunes Search API is insufficient.
"""

from typing import Dict


class WebFetchPrompts:
    """Pre-configured WebFetch prompts for app store scraping."""

    @staticmethod
    def app_store_search(keyword: str) -> Dict[str, str]:
        """WebFetch config for App Store search results."""
        return {
            "url": f"https://apps.apple.com/us/search?term={keyword.replace(' ', '+')}",
            "prompt": (
                f'Extract the top 10 apps for "{keyword}". '
                "For each: app name, developer, category, App Store URL, rating, tagline. "
                "Format as JSON array."
            ),
        }

    @staticmethod
    def app_store_app_page(app_url: str) -> Dict[str, str]:
        """WebFetch config for an individual App Store app page."""
        return {
            "url": app_url,
            "prompt": (
                "Extract: title, subtitle, developer, category, full description, "
                '"What\'s New" text, average rating, total ratings, screenshot count, '
                "has preview video (yes/no), age rating, price. Format as JSON."
            ),
        }

    @staticmethod
    def play_store_search(keyword: str) -> Dict[str, str]:
        """WebFetch config for Google Play Store search results."""
        return {
            "url": f"https://play.google.com/store/search?q={keyword.replace(' ', '+')}&c=apps",
            "prompt": (
                f'Extract the top 10 apps for "{keyword}". '
                "For each: app name, developer, category, Play Store URL, rating, "
                "download range. Format as JSON array."
            ),
        }

    @staticmethod
    def play_store_app_page(app_url_or_package: str) -> Dict[str, str]:
        """WebFetch config for an individual Google Play Store app page."""
        if app_url_or_package.startswith("http"):
            url = app_url_or_package
        else:
            url = f"https://play.google.com/store/apps/details?id={app_url_or_package}"

        return {
            "url": url,
            "prompt": (
                "Extract: title, developer, category, short description, full description, "
                '"What\'s new" text, average rating, total reviews, screenshot count, '
                "has promo video (yes/no), downloads range, content rating, price. "
                "Format as JSON."
            ),
        }

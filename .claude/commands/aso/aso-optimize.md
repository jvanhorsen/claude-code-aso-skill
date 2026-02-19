---
name: aso-optimize
description: Quick metadata optimization for Apple App Store and Google Play Store with copy-paste ready content
---

# ASO Optimize

Generate copy-paste ready app store metadata optimized for discoverability and conversion.

## Agent

Invokes **aso-metadata** directly (skips research, creative, and strategy phases).

## Usage

```
/aso-optimize [app-name]
```

## Information Gathered

- App name and category
- Key features (3-5)
- Target keywords (or suggest based on category)
- Platforms (Apple, Google, or both)

## Output

`outputs/[app-name]/02-metadata/` containing:
- `apple-metadata.md` — copy-paste ready for App Store Connect
- `google-metadata.md` — copy-paste ready for Play Console

## Time

3-5 minutes.

## When to Use

- Metadata refresh for existing app
- Quick optimization without full audit
- Already have keywords, just need metadata written
- Adding a second platform

## Want More?

Use `/aso-full-audit` for the complete package including visual asset specs, CPP strategy, A/B testing, launch planning, and ongoing optimization.

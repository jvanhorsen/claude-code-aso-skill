# Security Policy

## Supported Versions

We actively support the following versions of the ASO skill with security updates:

| Version | Supported          | Python Compatibility |
| ------- | ------------------ | -------------------- |
| 1.4.x   | :white_check_mark: | 3.7+                 |
| < 1.4   | :x:                | -                    |

## Security Best Practices

### For Users

**Installation Security:**
```bash
# ALWAYS verify repository authenticity before installation
# Official repository: https://github.com/jvanhorsen/claude-code-aso-skill

# Install only from trusted sources
cp -r app-store-optimization ~/.claude/skills/

# Verify installation
ls ~/.claude/skills/app-store-optimization/
# Should show: SKILL.md, 10 Python modules, lib/ directory
```

**API Key Security:**
- Never commit API keys or secrets to the repository
- Use environment variables for sensitive data
- The ASO skill does NOT require API keys for core functionality
- iTunes Search API is public and requires no authentication

**Data Privacy:**
- The ASO skill runs locally and does not send data to external servers
- iTunes API calls are made directly to Apple's public API
- No analytics or tracking included

### For Contributors

**Code Security Standards:**

1. **No Hardcoded Credentials:**
   ```python
   # ❌ NEVER do this
   api_key = "sk-abc123xyz"

   # ✅ Use environment variables
   import os
   api_key = os.getenv("API_KEY")
   ```

2. **Input Validation:**
   ```python
   # ✅ Always validate inputs
   def optimize_title(title: str, platform: str) -> str:
       if platform not in ['apple', 'google']:
           raise ValueError(f"Invalid platform: {platform}")

       if not title or not isinstance(title, str):
           raise ValueError("Title must be a non-empty string")
   ```

3. **Safe URL Handling:**
   ```python
   # ✅ Use urllib.parse for URL construction
   from urllib.parse import urlencode, quote

   query_params = urlencode({'term': user_input})
   url = f"https://itunes.apple.com/search?{query_params}"
   ```

4. **No External Dependencies:**
   - Minimizes attack surface
   - Reduces supply chain vulnerabilities
   - Standard library only (typing, re, urllib, json, etc.)

## Reporting a Vulnerability

### Where to Report

**DO NOT** open public GitHub issues for security vulnerabilities.

Instead, report security issues privately:

1. **GitHub Security Advisories** (Preferred):
   - Go to: https://github.com/jvanhorsen/claude-code-aso-skill/security/advisories
   - Click "New draft security advisory"
   - Provide detailed information

2. **Direct Email**:
   - Report via [GitHub Issues](https://github.com/jvanhorsen/claude-code-aso-skill/issues) with the label "security"
   - Subject: "[SECURITY] ASO Skill Vulnerability Report"
   - Include: Detailed description, reproduction steps, impact assessment

### What to Include

Please provide:
- **Description:** Clear description of the vulnerability
- **Impact:** What could an attacker do?
- **Reproduction:** Step-by-step instructions to reproduce
- **Affected Versions:** Which versions are affected?
- **Suggested Fix:** If you have a patch or workaround

**Example Report:**
```
Title: Potential XSS in metadata_optimizer.py

Description: The optimize_description() function does not sanitize HTML entities,
which could lead to XSS if the output is rendered in a web context.

Impact: If a user generates app descriptions and displays them in a web app without
sanitization, malicious input could execute scripts.

Reproduction:
1. Call optimize_description() with input: "<script>alert('XSS')</script>"
2. Output includes unescaped HTML

Affected Versions: 1.0.0

Suggested Fix: Escape HTML entities in output or add sanitization layer
```

### Response Timeline

We aim to respond to security reports within:
- **Initial Response:** 48 hours
- **Impact Assessment:** 7 days
- **Fix Development:** 14-30 days (depending on severity)
- **Public Disclosure:** After fix is released

### Severity Levels

| Severity | Description | Response Time |
|----------|-------------|---------------|
| **Critical** | Remote code execution, data breach | 24-48 hours |
| **High** | Authentication bypass, privilege escalation | 7 days |
| **Medium** | Information disclosure, DoS | 14 days |
| **Low** | Minor issues, theoretical vulnerabilities | 30 days |

## Security Features

### Automated Scanning

Our CI/CD pipeline includes:
- **CodeQL Analysis:** Detects common vulnerabilities
- **Secret Scanning:** Prevents credential commits
- **Dependency Scanning:** Monitors for vulnerable dependencies (future)
- **TruffleHog:** Scans for secrets in git history

### Code Review Process

All code changes undergo:
1. **Claude Code Review:** AI-powered security analysis
2. **Human Review:** Manual security verification
3. **Quality Gates:** Automated security checks must pass

### No Known Vulnerabilities

As of February 19, 2026:
- ✅ No external dependencies (minimal attack surface)
- ✅ No hardcoded credentials
- ✅ No known CVEs
- ✅ All inputs validated
- ✅ Safe URL handling (urllib)

## Security Updates

### How We Notify Users

Security updates are communicated through:
1. **GitHub Security Advisories:** For critical issues
2. **CHANGELOG.md:** For all security fixes
3. **Release Notes:** Detailed fix descriptions
4. **GitHub Discussions:** Community awareness

### How to Stay Updated

```bash
# Watch repository for security advisories
# Go to: https://github.com/jvanhorsen/claude-code-aso-skill
# Click "Watch" → "Custom" → Check "Security alerts"

# Or subscribe to release notifications
# Click "Watch" → "Custom" → Check "Releases"
```

## Security Checklist for Contributors

Before submitting a PR, verify:
- [ ] No hardcoded API keys, tokens, or credentials
- [ ] All user inputs validated
- [ ] No external dependencies added without justification
- [ ] URLs constructed safely (urllib.parse)
- [ ] No eval(), exec(), or similar dangerous functions
- [ ] Error messages don't leak sensitive information
- [ ] File operations use safe paths (no directory traversal)
- [ ] Character limits prevent buffer overflows (metadata fields)

## Common Security Questions

### Q: Does the ASO skill collect user data?
**A:** No. The skill runs entirely locally on your machine. It only makes API calls to Apple's public iTunes Search API when explicitly requested.

### Q: Can the skill access my App Store Connect credentials?
**A:** No. The skill does not handle App Store Connect credentials or authentication. It only analyzes publicly available data.

### Q: Is it safe to use the iTunes API integration?
**A:** Yes. The iTunes Search API is a public Apple API that requires no authentication and returns only publicly available app metadata.

### Q: What if I find a secret committed in git history?
**A:** Report it immediately via GitHub Security Advisories. We will rotate the secret and use BFG Repo-Cleaner to remove it from history.

## Responsible Disclosure

We follow responsible disclosure principles:
1. Reporter notifies us privately
2. We confirm the vulnerability
3. We develop and test a fix
4. We release the fix
5. We publicly disclose (with credit to reporter, if desired)

**We do NOT:**
- Threaten or intimidate security researchers
- Pursue legal action against good-faith reporters
- Disclose reporter information without consent

## Recognition

We appreciate security researchers who help keep the ASO skill secure. With your permission, we will:
- Credit you in the CHANGELOG.md
- Mention you in the security advisory
- Thank you in the release notes

---

**Questions?** Contact us via GitHub Security Advisories or email.

**Last Updated:** February 19, 2026

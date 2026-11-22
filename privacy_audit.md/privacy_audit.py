"""
privacy_audit.py - Passive privacy & security audit of a web page.

Sends ONE HTTP GET request and analyses headers, cookies, third-party
scripts, forms and privacy-policy links.

Usage:   python privacy_audit.py https://your-own-site.com
Install: pip install requests beautifulsoup4

NOTE: Use only on sites you own or have permission to test.
LIMITATION: Reads static HTML only. JavaScript-rendered content (forms,
consent banners, footer links) will not be seen, so "False" results for
those checks are inconclusive and need manual verification in a browser.
"""
import sys
import json
import requests
from urllib.parse import urlparse
from bs4 import BeautifulSoup

TRACKERS = ["google-analytics", "googletagmanager", "doubleclick",
            "facebook.net", "connect.facebook", "hotjar", "clarity.ms", "mixpanel"]
HEADERS = ["Strict-Transport-Security", "Content-Security-Policy",
           "X-Frame-Options", "X-Content-Type-Options", "Referrer-Policy"]


def audit(url):
    r = requests.get(url, timeout=10,
                     headers={"User-Agent": "PrivacyAuditStudent/1.0"})
    soup = BeautifulSoup(r.text, "html.parser")
    host = urlparse(r.url).netloc
    report = {"url": r.url, "https": r.url.startswith("https")}

    # 1. Security headers
    report["headers"] = {h: (h in r.headers) for h in HEADERS}

    # 2. Cookies (case-insensitive HttpOnly check)
    report["cookies"] = [
        {"name": c.name,
         "secure": c.secure,
         "httponly": any(k.lower() == "httponly" for k in c._rest)}
        for c in r.cookies
    ]

    # 3. Third-party scripts / trackers
    scripts = [s["src"] for s in soup.find_all("script", src=True)]
    third = sorted({urlparse(s).netloc for s in scripts
                    if urlparse(s).netloc and urlparse(s).netloc != host})
    report["third_party_domains"] = third
    report["trackers_found"] = [t for t in TRACKERS
                                if any(t in s for s in scripts)]

    # 4. Forms collecting personal data
    pii_types = {"email", "tel", "password", "text"}
    report["forms"] = [
        {"action": f.get("action"),
         "method": f.get("method", "get"),
         "fields": [i.get("name") for i in f.find_all("input")
                    if i.get("type", "text") in pii_types]}
        for f in soup.find_all("form")
    ]

    # 5. Privacy policy / cookie consent
    links = [a.text.lower() for a in soup.find_all("a")]
    report["privacy_policy_link"] = any("privacy" in l for l in links)
    report["cookie_banner_hint"] = any(
        k in r.text.lower() for k in ["cookie consent", "accept cookies"])
    return report


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python privacy_audit.py <url>")
        sys.exit(1)
    try:
        print(json.dumps(audit(sys.argv[1]), indent=2))
    except requests.RequestException as e:
        print(f"Request failed: {e}")

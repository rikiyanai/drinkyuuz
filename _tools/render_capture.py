"""
Playwright-driven capture of drinkyuuz.com pages.

For each URL in URLS:
- Loads the page in headless chromium
- Waits for network idle (Wix's JS runtime to finish hydration)
- Saves the post-hydration HTML to _rendered/<slug>.html
- Saves a full-page PNG screenshot to _screenshots/<slug>.png

Run from the wix-mirror/ directory:
    python3 _tools/render_capture.py
"""
import re
import sys
from pathlib import Path
from playwright.sync_api import sync_playwright

URLS = [
    "https://www.drinkyuuz.com/",
    "https://www.drinkyuuz.com/category/all-products",
    "https://www.drinkyuuz.com/product-page/yuzu-ade-original-6-pack",
    "https://www.drinkyuuz.com/product-page/yuzu-ade-ginger-6-pack",
]


def slug_for(url: str) -> str:
    path = url.replace("https://www.drinkyuuz.com", "").strip("/")
    if not path:
        return "index"
    return re.sub(r"[^a-zA-Z0-9_-]+", "_", path)


def main():
    root = Path(__file__).resolve().parent.parent
    rendered_dir = root / "_rendered"
    shots_dir = root / "_screenshots"
    rendered_dir.mkdir(exist_ok=True)
    shots_dir.mkdir(exist_ok=True)

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context(
            viewport={"width": 1440, "height": 900},
            user_agent=(
                "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
                "AppleWebKit/537.36 (KHTML, like Gecko) "
                "Chrome/120.0.0.0 Safari/537.36"
            ),
        )

        for url in URLS:
            slug = slug_for(url)
            print(f"[*] {url} -> {slug}")
            page = context.new_page()
            try:
                page.goto(url, wait_until="load", timeout=30_000)
                page.wait_for_timeout(5_000)
                html = page.content()
                (rendered_dir / f"{slug}.html").write_text(html, encoding="utf-8")
                page.screenshot(
                    path=str(shots_dir / f"{slug}.png"),
                    full_page=True,
                )
                print(f"    saved html ({len(html):,} bytes) + screenshot")
            except Exception as e:
                print(f"    FAILED: {e}", file=sys.stderr)
            finally:
                page.close()

        browser.close()
    print("[+] Capture finished.")


if __name__ == "__main__":
    main()

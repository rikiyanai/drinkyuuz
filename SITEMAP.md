# drinkyuuz.com — Site Map

Captured `2026-05-16`. Authoritative source: `https://www.drinkyuuz.com/sitemap.xml`

## All pages on the live site

The Wix sitemap declares exactly **4 URLs**. Every one is captured.

| # | Page | Live URL | Static HTML | Rendered DOM | Screenshot |
|---|---|---|---|---|---|
| 1 | Home | https://www.drinkyuuz.com/ | [index.html](index.html) | [_rendered/index.html](_rendered/index.html) | [_screenshots/index.png](_screenshots/index.png) |
| 2 | All Products (category) | https://www.drinkyuuz.com/category/all-products | [category/all-products.html](category/all-products.html) | [_rendered/category_all-products.html](_rendered/category_all-products.html) | [_screenshots/category_all-products.png](_screenshots/category_all-products.png) |
| 3 | Yuzu Ade Original 6-pack | https://www.drinkyuuz.com/product-page/yuzu-ade-original-6-pack | [product-page/yuzu-ade-original-6-pack.html](product-page/yuzu-ade-original-6-pack.html) | [_rendered/product-page_yuzu-ade-original-6-pack.html](_rendered/product-page_yuzu-ade-original-6-pack.html) | [_screenshots/product-page_yuzu-ade-original-6-pack.png](_screenshots/product-page_yuzu-ade-original-6-pack.png) |
| 4 | Yuzu Ade Ginger 6-pack | https://www.drinkyuuz.com/product-page/yuzu-ade-ginger-6-pack | [product-page/yuzu-ade-ginger-6-pack.html](product-page/yuzu-ade-ginger-6-pack.html) | [_rendered/product-page_yuzu-ade-ginger-6-pack.html](_rendered/product-page_yuzu-ade-ginger-6-pack.html) | [_screenshots/product-page_yuzu-ade-ginger-6-pack.png](_screenshots/product-page_yuzu-ade-ginger-6-pack.png) |

## Capture surfaces (what's in each version)

### `<page>.html` — wget static HTML
Server-side-rendered HTML from `https://www.drinkyuuz.com/`. Links converted for local browsing. Some Wix runtime resources will phone home to wixstatic.com / parastorage.com when opened in a browser.

### `_rendered/<page>.html` — post-hydration DOM
Captured via headless chromium after page `load` + 5s settle. Full element tree as a real visitor sees it — includes hydrated React tree, computed prices, product variants. Larger than the static HTML (~900 KB vs ~550 KB) because all client-side state is materialized into the DOM.

### `_screenshots/<page>.png` — full-page screenshot
Full-page PNG at 1440×900 viewport. Use these for visual reference when rebuilding the site or auditing what was on the page at capture time.

## Captured assets

| Asset type | Count | Notes |
|---|---|---|
| HTML pages (static) | 4 | One per live URL |
| HTML pages (rendered) | 4 | Post-hydration via Playwright |
| Screenshots | 4 | Full-page PNGs |
| Media (images) | 24 | Variants/resolutions under `media/` |
| JS bundles | 17 | Wix runtime, react, lodash, core-js, product/category widgets |
| Fonts (woff2) | 8 | Helvetica + Gloock |

**Total:** 66 files, ~15 MB on disk.

## Sitemap.xml source-of-truth

The Wix-generated sitemap is published at three sub-paths:

| Sub-sitemap | Live URL | Lastmod | Pages |
|---|---|---|---|
| Pages | https://www.drinkyuuz.com/pages-sitemap.xml | 2026-05-16 | 1 (home) |
| Products | https://www.drinkyuuz.com/store-products-sitemap.xml | 2025-01-17 | 2 |
| Categories | https://www.drinkyuuz.com/store-categories-sitemap.xml | 2026-03-22 | 1 |

## What is NOT on the public site

Things you might expect on a Wix small-business site but that **do not exist** as public URLs on drinkyuuz.com today:
- No About / Story page
- No Contact page (footer form only — no dedicated page)
- No Blog
- No FAQ
- No Press / Media page
- No Wholesale / B2B page
- No Where-to-buy page

If any of these existed previously they have been removed from publication. The sitemap is the authoritative answer.

## Re-running the capture

```bash
# 1. Static mirror (wget)
cd wix-mirror
wget --mirror --convert-links --adjust-extension --page-requisites \
     --no-parent --no-host-directories --span-hosts --level=inf \
     --domains=drinkyuuz.com,www.drinkyuuz.com,static.wixstatic.com,static.parastorage.com,siteassets.parastorage.com \
     --execute robots=off \
     https://www.drinkyuuz.com/ \
     https://www.drinkyuuz.com/category/all-products \
     https://www.drinkyuuz.com/product-page/yuzu-ade-original-6-pack \
     https://www.drinkyuuz.com/product-page/yuzu-ade-ginger-6-pack

# 2. Rendered DOM + screenshots (Playwright)
python3 _tools/render_capture.py
```

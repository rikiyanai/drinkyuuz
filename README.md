# drinkyuuz — static preview

Static mirror of the live drinkyuuz.com site, deployed at
**https://rikiworld.com/drinkyuuz/** for testing before DNS cutover.

Source of truth lives in `rikiyanai/yuzu-business-agent` on the
`wix-mirror` branch under `wix-mirror/`. This repo is a deploy target —
its master branch contents are the artifact uploaded to GitHub Pages.

Pattern matches `rikiyanai/refrog-app`: the build workflow copies the
site into `dist/drinkyuuz/`, writes a `CNAME` for rikiworld.com, and
publishes the artifact via `actions/deploy-pages@v4`.

## Mobile + desktop

- `/drinkyuuz/` -> desktop wget mirror with the Leaflet map injected
- `/drinkyuuz/m/` -> Playwright-captured mobile rendering with the same
  map; the desktop page auto-redirects mobile viewports to `/m/`

## To refresh content

1. Update on `wix-mirror` branch of `rikiyanai/yuzu-business-agent`
2. Copy the new `wix-mirror/` tree into this repo's root and push
   (or wire up an automation later)

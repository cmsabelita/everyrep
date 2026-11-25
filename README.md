# everyrep-web

The everyrep.app website (landing page, SEO pages, privacy policy, terms, support, shared program links) and the
marketing kit. Plain static HTML and one stylesheet: no build step.

The app itself lives in `../everyrep-mobile`; App Store metadata stays there in `AppStore/metadata/` (fastlane).

## Layout

| Path | What |
| --- | --- |
| `public/` | The site root. Deploy this folder as is. |
| `public/index.html` | Home: `SoftwareApplication` schema, Open Graph, Smart App Banner (commented out until there's an app id) |
| `public/workout-app-blocker/`, `screen-time-workout/`, `train-with-a-friend/` | Search landing pages, each with `FAQPage` schema |
| `public/privacy/`, `terms/`, `support/` | Linked from the app's Settings (`SettingsLinks` in `FeatureSettings/Settings.swift`) and App Store Connect |
| `public/p/` | Shared program page: `/p/CODE` shows the code and opens `everyrep://program/CODE` |
| `public/.well-known/apple-app-site-association` | Universal Links for `/p/*` (team `YA4ZD8XDAU`, `io.everyrep.app`); only used once the app adds the Associated Domains entitlement |
| `public/_redirects`, `_headers` | Cloudflare Pages / Netlify rules: `/p/*` rewrite, AASA content type (GitHub Pages ignores them; `404.html` handles `/p/CODE` there) |
| `public/robots.txt`, `sitemap.xml` | `/p/` is kept out of search |
| `marketing/marketing-kit.md` | Positioning, taglines, pitches, social, Search Ads, in-app event, product pages, screenshot captions, video script |
| `scripts/check.py` | Pre-publish check: JSON-LD and AASA parse, no `TODO` left in `public/` |
| `scripts/make-og.py` | Redraws `public/assets/og.png` (needs Pillow) |

## Before publishing

Run `python3 scripts/check.py` (JSON-LD and AASA parse, no `TODO` in `public/`). Filled on 2026-11-25:

- Contact: `cmsabelita@gmail.com`.
- AI provider: Google, Gemini API (`AI_PROVIDER=gemini` in `../everypeso-api/.env`). The privacy page states Google's
  **paid** terms: requests kept up to 55 days for abuse monitoring, not used for training. That is only true while the
  Gemini key's Cloud project has billing on; on the free tier Google may use inputs to improve its products.
- Shared programs: the link stops working after 30 days (`SHARE_LIFETIME_MS` in the server). The server deletes an
  expired file only when someone asks for it, so the page doesn't claim deletion.
- "Join the beta" buttons say "Coming soon to iPhone" until the TestFlight public link exists.

Still to add when they exist: the TestFlight link (buttons), the App Store id (`<meta name="apple-itunes-app"
content="app-id=…">` in `index.html`), and one screenshot per landing page (frames 1, 2 and 6 of the marketing kit;
frame 1 also replaces `assets/og.png`).

## Deploy: GitHub Pages (now)

`.github/workflows/pages.yml` publishes `public/` on every push to `main`, at `https://cmsabelita.github.io/everyrep/`.
Links are relative so the site works under that subpath and on `everyrep.app` later. GitHub Pages has no rewrites, so
`404.html` sends `/p/CODE` to `/p/?code=CODE`, and `_redirects` / `_headers` are ignored there.

One-time: repo Settings → Pages → Source: **GitHub Actions**. For the domain later: Settings → Pages → Custom domain
`everyrep.app`, then the DNS records GitHub shows.

## Deploy: Cloudflare Pages (alternative)

1. New Pages project, no framework, build command empty, output directory `public`.
2. Add the custom domain `everyrep.app`.
3. Check `https://everyrep.app/privacy`, `/terms`, `/support` and `/p/ABCD1234` load.
4. Google Search Console: add the domain property, verify by DNS, submit `https://everyrep.app/sitemap.xml`.

Local preview: `python3 -m http.server -d public 8000` (the `/p/*` rewrite only works on the host; open
`/p/index.html` locally).

## Shared program links

The server picks the link: `POST /v1/programs/shares` returns the `url` the app shows (`ServerProgramSharing`). The app
reads the code from any `https://…/p/CODE` link (`ProgramShareLink.code(in:)`), so moving links to
`https://everyrep.app/p/CODE` is a server setting, with no app release. On this site `/p/CODE` opens the app through its
`everyrep://` scheme when the button is tapped. For links that open the app directly, add the Associated Domains
entitlement `applinks:everyrep.app` to the app (the AASA file here is ready).

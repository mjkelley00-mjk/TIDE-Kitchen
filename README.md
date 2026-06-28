# TIDE Kitchen — Website

A single-page editorial site for TIDE Kitchen — South Shore, Chicago.
Opening 2027.

> **Update — June 2026.** The investor/partner materials are no longer public downloads.
> The "Materials" section is now **request-gated**: a confidentiality-acknowledged form
> (powered by Formspree, posting to `hello@tide.kitchen`) collects requester details, and
> documents are shared privately on request. The previous PDFs were **removed from
> `assets/docs/`** — a public repo serves files by direct URL even when nothing links to
> them, so confidential materials are not kept in the repo.

> **Update — May 2026.** Stages 03 (Current) and 04 (Wave) now use the full
> image+text `stage-feature` layout, matching Stages 01–02. Stage 03 carries the
> "71st Street Ramen" interior from the deck (`CURRENT_RAMEN.jpg`); Stage 04 uses an
> inline SVG of the EV/SDE wealth-multiplier curve (the deck's Stage 04 visual) since
> no photographic render exists for that stage. The old `.stages-compact` card layout
> was removed.

## Structure

```
tide-kitchen-site/
├── index.html                  ← the entire site (HTML, CSS, JS — single file)
├── README.md                   ← this file
└── assets/
    └── img/
        ├── 71st_Today.jpg              ← 71st Street current state (Opportunity + Vision sections)
        ├── CORNER_UPDATE.png           ← TIDE corner rendering (hero background + Vision "after")
        ├── INCUBATOR_STALLS.png        ← Stage 01 · TIDE Pool stage feature
        ├── EXTERIOR_STOREFRONT.png     ← Stage 02 · TIDE Anchor stage feature
        ├── CURRENT_RAMEN.jpg           ← Stage 03 · TIDE Current stage feature (from deck p.7)
        ├── INCUBATOR_EAST.png          ← reserved for future use (not currently displayed)
        ├── OPC.png                     ← Obama Presidential Center catalyst card
        ├── IQMP.jpg                    ← Illinois Quantum Park catalyst card
        └── RegalMile.webp              ← Regal Mile Studios catalyst card
```

> Investor/partner documents are **not stored in this repo**. They are confidential and
> shared privately on request via the gated "Materials" form.

## Materials request form (Formspree)

The "Materials" section posts to [Formspree](https://formspree.io). To wire it up:

1. Create a form at formspree.io with `hello@tide.kitchen` as the destination.
2. Copy the form ID (the part after `/f/` in your endpoint, e.g. `xoldoexample`).
3. In `index.html`, replace `YOUR_FORM_ID` in `action="https://formspree.io/f/YOUR_FORM_ID"`
   with that ID.
4. Submit once to confirm Formspree's verification email.

The form captures name, email, organization, investor type, accredited-investor status,
materials requested, an optional message, and a required confidentiality acknowledgment.

## Deployment

Static site — works on any host. No build step. No dependencies.

- **GitHub Pages**: push to a repo and enable Pages on the root (current setup; `CNAME` → tide.kitchen)
- **Netlify / Vercel / Cloudflare Pages**: drag-and-drop the folder
- **Traditional hosting (S3, FTP, etc.)**: upload the entire folder, point at `index.html`

External dependencies loaded from CDN: Google Fonts (EB Garamond, Inter, JetBrains Mono).

## Editing

- All copy lives inline in `index.html` — search by section heading.
- Color tokens live in `:root` at the top of the `<style>` block (deep navy, gold, paper cream, teal accent).
- Image credits live in the `.foot__credits` block near the end of the file.
- All animation respects `prefers-reduced-motion`.

## Image Credits

All renderings: **Future Firm**
"71st St Today": Photograph by **Jacob Yeung** for **Fortune**
Obama Presidential Center: **Obama Foundation**
Illinois Quantum & Microelectronics Park: **Lamar Johnson Collaborative**
Regal Mile Studios: *(pending attribution)*

Full hyperlinks are wired into the footer credits row of `index.html`.

## Browser Support

Tested in modern Chrome, Safari, Firefox. Mobile-responsive down to 360px.

## Contact

hello@tide.kitchen

*"A rising tide lifts all boats."*

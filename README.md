# TIDE Kitchen — Website

A static editorial site for TIDE Kitchen — South Shore, Chicago. Opening 2027.

> **Update — June 2026.** The site no longer hosts or lists any investor documents.
> Interest is captured through three purpose-built inquiry forms (Formspree, posting to
> `hello@tide.kitchen`); any materials are shared privately, one-to-one, on follow-up.
> Three audience tracks: **Investors → `request.html`**, **Partners → `partner.html`**,
> **Community (SDIRA / Reg CF) → `community.html`**.

## Structure

```
tide-kitchen-site/
├── index.html          ← the main single-page site (HTML, CSS, JS — one file)
├── request.html        ← investor inquiry form
├── partner.html        ← partnership inquiry form
├── community.html      ← community co-invest interest form
├── README.md           ← this file
└── assets/
    └── img/
        ├── 71st_Today.jpg              ← 71st Street current state
        ├── CORNER_UPDATE.png           ← TIDE corner rendering (hero + Vision)
        ├── INCUBATOR_STALLS.png        ← Stage 01 · TIDE Pool
        ├── EXTERIOR_STOREFRONT.png     ← Stage 02 · TIDE Anchor
        ├── CURRENT_RAMEN.jpg           ← Stage 03 · TIDE Current
        ├── INCUBATOR_EAST.png          ← reserved (not currently displayed)
        ├── OPC.png                     ← Obama Presidential Center catalyst card
        ├── IQMP.jpg                    ← Illinois Quantum Park catalyst card
        └── RegalMile.webp              ← Regal Mile Studios catalyst card
```

> No investor or partner documents are stored in this repository. They are confidential
> and shared privately on a one-to-one basis after an inquiry is reviewed.

## Forms (Formspree)

`request.html`, `partner.html`, and `community.html` each POST to a Formspree endpoint that
delivers to `hello@tide.kitchen`. The endpoint is set in each page's `<form action="…">`.
To change the destination, create a form at formspree.io and update the `action` URL in all
three pages. Stage 04's wealth-multiplier chart on `index.html` is an inline SVG (no asset file).

## Deployment

Static — no build step, no dependencies.

- **GitHub Pages** (current): served from `main` at the repo root; `CNAME` → tide.kitchen.
- Netlify / Vercel / Cloudflare Pages: drag-and-drop the folder.
- Traditional hosting: upload the folder, point at `index.html`.

External dependencies via CDN: Google Fonts (EB Garamond, Inter, JetBrains Mono).

## Editing

- Homepage copy lives inline in `index.html` — search by section heading.
- Color tokens live in `:root` at the top of the `<style>` block (deep navy, gold, paper cream, teal).
- The form pages share the same color tokens and font stack as the homepage.
- Image credits live in the `.foot__credits` block near the end of `index.html`.
- All animation respects `prefers-reduced-motion`.

## Image Credits

All renderings: **Future Firm**
"71st St Today": Photograph by **Jacob Yeung** for **Fortune**
Obama Presidential Center: **Obama Foundation**
Illinois Quantum & Microelectronics Park: **Lamar Johnson Collaborative**
Regal Mile Studios: *(pending attribution)*

## Browser Support

Tested in modern Chrome, Safari, Firefox. Mobile-responsive down to 360px.

## Contact

hello@tide.kitchen

*"A rising tide lifts all boats."*

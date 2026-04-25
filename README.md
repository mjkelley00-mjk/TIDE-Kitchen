# TIDE Kitchen — Website

A single-page editorial site for TIDE Kitchen — South Shore, Chicago.
Opening 2027.

## Structure

```
tide-kitchen-site/
├── index.html                  ← the entire site (HTML, CSS, JS — single file)
├── README.md                   ← this file
└── assets/
    ├── docs/
    │   ├── TIDE_Kitchen_Executive_Summary_04_26.pdf
    │   ├── TIDE_Kitchen_Deck_04_26.pdf
    │   └── TIDE_Kitchen_Analysis_Report_04_26.pdf
    └── img/
        ├── 71st_Today.jpg              ← 71st Street current state (Opportunity + Vision sections)
        ├── CORNER_UPDATE.png           ← TIDE corner rendering (hero background + Vision "after")
        ├── EXTERIOR_STOREFRONT.png     ← TIDE Anchor stage feature
        ├── INCUBATOR_STALLS.png        ← TIDE Pool stage feature
        ├── INCUBATOR_EAST.png          ← reserved for future use (not currently displayed)
        ├── OPC.png                     ← Obama Presidential Center catalyst card
        ├── IQMP.jpg                    ← Illinois Quantum Park catalyst card
        └── RegalMile.webp              ← Regal Mile Studios catalyst card
```

## Deployment

Static site — works on any host. No build step. No dependencies.

- **Netlify / Vercel / Cloudflare Pages**: drag-and-drop the `tide-kitchen-site` folder
- **GitHub Pages**: push to a repo and enable Pages on the root
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

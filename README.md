# Onesign & Digital website

Static site. The repo root is what Vercel serves.

- `_src/` generator: `python3 pages.py` builds everything into `../site`
  - `build.py` core templates and image helpers, `pages.py` new page families, `content.py` case studies, areas and guides, `data.json` sign types, sectors and image registry
- `_masters/` original photos (`wix`, `ig`, `new`, `brand`). WebP sizes in `img/p` are generated from these.
- To connect the enquiry form to HubSpot, set `HUBSPOT = dict(portal="...", form="...")` in `_src/build.py` and rebuild.

## Locked choices
- Sign-type hero photos are fixed in `_src/build.py` (LOCKED_HEROES), chosen by Mak. Do not change them when adding photos.
- Identity Co: only the photo with the man fitting the line-art wall.

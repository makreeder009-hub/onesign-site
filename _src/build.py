# -*- coding: utf-8 -*-
"""Onesign & Digital static site generator (v2).
build.py   core templates (home, sign types, sectors, about, contact) and helpers
pages.py   new page families (our work, areas, guides, nationwide, indexes, privacy)
content.py copy and data for the new page families
data.json  sign types, sectors and the image registry (key -> [source, caption, focal point])
Masters live in ../masters/{wix,ig,new}; WebP sizes are generated on demand into the output."""
import json, os, re, html as H
from PIL import Image, ImageOps

SRC = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(SRC, "..", "site")
MASTERS = os.path.join(SRC, "..", "masters")
globals().update(json.load(open(os.path.join(SRC, "data.json"))))
IMG = {k: tuple(v) for k, v in IMG.items()}
for _s in SECTORS: _s["points"] = [tuple(p) for p in _s["points"]]
# the same photo saved twice under two names: always show one of them
ALIAS = {"ncl":"hero", "ig_totem_dir":"ng_totem", "ig_queenshead":"n_queens", "n_whiteswan":"p_ws_side",
         "ws_weld2":"weld", "ig_smartvape":"p_sm_proj", "p_cork_new":"cork", "p_sun_totem2":"sun_totem",
         "p_vv_ext":"n_vivana", "ig_wrgroup":"p_wr_brick", "p_gm_2":"p_gm_main", "p_cdc_ent":"hc_cdc2"}
def canon(o):
    if isinstance(o, str): return ALIAS.get(o, o)
    if isinstance(o, dict): return {k: canon(v) for k, v in o.items()}
    if isinstance(o, list):
        out = []
        for x in o:
            x = canon(x)
            if not (isinstance(x, str) and x in out): out.append(x)
        return out
    if isinstance(o, tuple): return o
    return o
TYPES = canon(TYPES); SECTORS = canon(SECTORS); PROJECTS = canon(PROJECTS); REEL_A = canon(REEL_A); REEL_B = [k for k in canon(REEL_B) if k not in REEL_A]
for _s in SECTORS: _s["points"] = [tuple(p) for p in _s["points"]]
# Sign-type hero photos chosen by Mak. LOCKED: do not change these when adding photos or rebuilding.
LOCKED_HEROES = {
 "printed-fascia-panels": "p_ns_fascia",
 "3d-letters": "n_thatype",
 "backlit-panels": "st_sign",
 "flat-cut-letters": "ig_durham",
 "high-level-signs": "rolls",
 "projecting-signs": "ig_corner",
 "light-boxes": "ig_gavroche",
 "flex-faces": "n_kosmic",
 "neon-led-neon": "neonB",
 "vinyl-wall-graphics": "ig_lineart",
 "digital-large-format-print": "hoarding",
 "flags-banners": "ig_kier",
 "totems-monoliths": "sun_totem",
 "wayfinding": "way_g",
 "vehicle-graphics": "ig_park2"
}
for _t in TYPES:
    _t["hero"] = LOCKED_HEROES[_t["slug"]]
    _t["photos"] = [_t["hero"]] + [p for p in _t["photos"] if p != _t["hero"]]
E = H.escape
LOGO = "{{R}}img/brand/onesign-logo-white.png"
ACCRED = "{{R}}img/brand/accreditations.png"
ASSET_V = "9"

# ------------------------------------------------------------------ images
VARS = (96, 480, 960, 1600)
_dims = {}
def _master(key):
    wid = IMG[key][0]
    if wid.startswith("new:"): p = os.path.join(MASTERS, "new", wid[4:] + ".jpg")
    elif wid.startswith("local:"): p = os.path.join(MASTERS, "ig", wid[6:] + ".jpg")
    else: p = os.path.join(MASTERS, "wix", key + ".jpg")
    return p if os.path.exists(p) else None
def _open(key):
    return ImageOps.exif_transpose(Image.open(_master(key))).convert("RGB")
def dims(key):
    if key not in _dims:
        m = _master(key)
        _dims[key] = Image.open(m).size if m else (1600, 1200)
    return _dims[key]
def ensure(key, w):
    """Make img/p/<key>-<w>.webp if missing. Returns (relative path, real width)."""
    mw, mh = dims(key); rw = min(w, mw)
    rel = f"img/p/{key}-{w}.webp"; full = os.path.join(OUT, rel)
    if not os.path.exists(full) and _master(key):
        os.makedirs(os.path.dirname(full), exist_ok=True)
        im = _open(key); im.thumbnail((w, w * 4))
        im.save(full, "WEBP", quality=60 if w == 96 else 78, method=5)
    return rel, rw
def wix(key, w, h, mode="fill", name=None):
    """Path of the nearest generated size for an image key (name kept from v1)."""
    if not _master(key):   # master not fetched yet: fall back to the old host
        return f"{WIX}{IMG[key][0]}/v1/{mode}/w_{w},h_{h},al_c,q_82,enc_auto/{key}.jpg"
    m = max(w, h); v = 96 if m <= 140 else 480 if m <= 560 else 960 if m <= 1100 else 1600
    return "{{R}}" + ensure(key, v)[0]
def pic(key, sizes="100vw", cls="", alt=None, lazy=True, style="", widths=(480, 960, 1600), prio=False):
    """<img> with srcset, intrinsic size and caption alt."""
    alt = cap(key) if alt is None else alt
    if not _master(key):
        return f'<img{" class=%s" % json.dumps(cls) if cls else ""} src="{wix(key,1200,1200,"fit")}" alt="{E(alt)}"{" loading=lazy" if lazy else ""}{" style=%s" % json.dumps(style) if style else ""}>'
    mw, mh = dims(key); parts = []; seen = set()
    for w in widths:
        rel, rw = ensure(key, w)
        if rw in seen: continue
        seen.add(rw); parts.append(("{{R}}" + rel, rw))
    src = parts[min(1, len(parts) - 1)][0]
    ss = ", ".join(f"{u} {rw}w" for u, rw in parts)
    return (f'<img{" class=%s" % json.dumps(cls) if cls else ""} src="{src}" srcset="{ss}" sizes="{sizes}" width="{mw}" height="{mh}" alt="{E(alt)}"'
            f'{" loading=\"lazy\" decoding=\"async\"" if lazy else ""}{" fetchpriority=\"high\"" if prio else ""}{" style=%s" % json.dumps(style) if style else ""}>')
def og(key):
    """1200x630 JPEG for social cards. Returns an absolute URL."""
    if not _master(key): return SITE_URL + "/img/og/default.jpg"
    rel = f"img/og/{key}.jpg"; full = os.path.join(OUT, rel)
    if not os.path.exists(full):
        os.makedirs(os.path.dirname(full), exist_ok=True)
        fx, fy = [float(x.strip("%")) / 100 for x in IMG[key][2].split()]
        ImageOps.fit(_open(key), (1200, 630), Image.LANCZOS, centering=(fx, fy)).save(full, "JPEG", quality=82, optimize=True, progressive=True)
    return SITE_URL + "/" + rel
from content import CASES, AREAS, GUIDES, REVIEWS, PHONE, LOC
CASES[:] = canon(CASES); AREAS[:] = canon(AREAS); GUIDES[:] = canon(GUIDES)
def cap(k): return IMG[k][1]
def pos(k): return IMG[k][2]
def types_by_slug(): return {t["slug"]: t for t in TYPES}
def sector_by_slug(): return {s["slug"]: s for s in SECTORS}
def tcap(s):  # sentence case for sector names in footer/meta
    return s[0].upper() + s[1:]

# --------------------------------------------------------------- partials
def nav(r):
    mega_cards = "".join(
        f'<a class="mega-card" href="{r}signs/{t["slug"]}.html"><img class="mc" loading="lazy" alt="" src="{wix(t["hero"],480,480,"fit")}" style="object-position:{MEGA_POS.get(t["slug"], pos(t["hero"]))}"><span>{E(t["label"])}</span></a>'
        for t in TYPES)
    mega_cards += f'<a class="mega-card all" href="{r}signs/index.html"><b>all {len(TYPES)} sign types</b><small>Compare them side by side, with real jobs and specs.</small><em>see them all →</em></a>'
    chips = "".join(f'<a href="{r}signs/{t["slug"]}.html">{E(t["label"])}</a>' for t in TYPES)
    return f'''<div class="progress" id="progress"></div>
<header class="nav" id="nav">
  <div class="wrap nav-in">
    <a class="logo" href="{r}index.html" aria-label="Onesign &amp; Digital home"><img src="{LOGO}" alt="Onesign &amp; Digital" width="142" height="30"></a>
    <ul class="nav-links">
      <li><button id="megaBtn" aria-expanded="false" aria-controls="mega">sign types</button></li>
      <li><a href="{r}work/index.html">our work</a></li>
      <li><a href="{r}sectors/index.html">sectors</a></li>
      <li><a href="{r}guides/index.html">guides</a></li>
      <li><a href="{r}about.html">about</a></li>
      <li><a href="{r}contact.html">contact</a></li>
    </ul>
    <a class="nav-tel" href="tel:+441914876767">0191 487 6767</a>
    <a class="pill" href="#contact">free mockup <span class="dot">→</span></a>
    <button class="burger" id="burger" aria-label="Open menu" aria-expanded="false" aria-controls="drawer"><span></span><span></span><span></span></button>
  </div>
  <div class="mega" id="mega">
    <div class="wrap mega-in">
      <div class="mega-grid">{mega_cards}</div>
      <div class="mega-foot"><a href="{r}signs/index.html">compare all {len(TYPES)} sign types <span aria-hidden="true">→</span></a><a href="{r}guides/illuminated-signs.html">not sure which? read the illuminated signs guide <span aria-hidden="true">→</span></a></div>
    </div>
  </div>
</header>
<nav class="drawer" id="drawer" aria-label="Mobile">
  <a href="{r}signs/index.html">sign types</a>
  <a href="{r}work/index.html">our work</a>
  <a href="{r}sectors/index.html">sectors</a>
  <a href="{r}guides/index.html">guides</a>
  <a href="{r}areas/index.html">areas we cover</a>
  <a href="{r}about.html">about</a>
  <a href="{r}contact.html">contact</a>
  <small>Sign types</small>
  <div class="chips">{chips}</div>
  <small>Call us</small>
  <a class="tel" href="tel:+441914876767">0191 487 6767</a>
</nav>'''

ONELASER_SVG = open(os.path.join(SRC, "onelaser.svg")).read()
ONEDESIGN = "{{R}}img/brand/onedesign.svg"

def footer(r):
    ft = "".join(f'<li><a href="{r}signs/{t["slug"]}.html">{E(t["name"])}</a></li>' for t in TYPES)
    fs = "".join(f'<li><a href="{r}sectors/{s["slug"]}.html">{E(tcap(s["name"]))}</a></li>' for s in SECTORS)
    fa = "".join(f'<li><a href="{r}areas/{a["slug"]}.html">{E(a["short"])}</a></li>' for a in AREAS)
    fg = "".join(f'<li><a href="{r}guides/{g["slug"]}.html">{E(g["kicker"])}</a></li>' for g in GUIDES)
    return f'''<footer class="dark">
  <div class="wrap">
    <div class="foot-top">
      <div class="foot-brand">
        <img src="{LOGO}" alt="Onesign &amp; Digital" width="142" height="30" style="height:30px;width:auto">
        <p>Family-run sign makers in Team Valley, Gateshead. Founded in Newcastle, trusted nationwide.</p>
        <a class="foot-rating" href="{REVIEWS["url"]}" target="_blank" rel="noopener"><b>{REVIEWS["score"]}</b><span class="stars" aria-hidden="true">★★★★★</span><span>{REVIEWS["count"]} Google reviews</span></a>
      </div>
      <div class="foot-contact">
        <a href="tel:+441914876767">0191 487 6767</a>
        <a href="mailto:sales@onesignanddigital.com">sales@onesignanddigital.com</a>
        <span>D86 Princesway North, Team Valley, Gateshead NE11 0TU</span>
        <span>Mon–Thu 07:00–16:00 · Fri 07:00–12:00</span>
      </div>
    </div>
    <div class="foot-grid v2">
      <div><h4>Sign types</h4><ul>{ft}</ul></div>
      <div><h4>Sectors</h4><ul>{fs}</ul></div>
      <div><h4>Areas</h4><ul>{fa}<li><a href="{r}nationwide-signage.html">Nationwide rollouts</a></li></ul>
        <h4 style="margin-top:28px">Guides</h4><ul>{fg}</ul></div>
      <div><h4>Company</h4><ul>
        <li><a href="{r}work/index.html">Our work</a></li>
        <li><a href="{r}about.html">About us</a></li>
        <li><a href="{r}contact.html">Contact</a></li>
        <li><a href="{r}privacy.html">Privacy</a></li>
        <li><a href="https://www.instagram.com/onesignanddigital/" rel="noopener" target="_blank">Instagram</a></li>
        <li><a href="https://www.facebook.com/onesignanddigital/" rel="noopener" target="_blank">Facebook</a></li>
        <li><a href="https://www.tiktok.com/@onesignanddigital" rel="noopener" target="_blank">TikTok</a></li>
      </ul>
        <img class="foot-accred" src="{ACCRED}" alt="Acclaim, IPAF, PASMA, Constructionline, CSCS and SCHQ accreditations" width="720" height="76" loading="lazy">
        <div class="family"><small>Sister companies</small><div class="family-logos"><a href="https://www.onelasercutting.com/" target="_blank" rel="noopener" aria-label="OneLaser, precision laser cutting">{ONELASER_SVG}</a><a href="https://www.onedesignstudios.com/" target="_blank" rel="noopener"><img src="{ONEDESIGN}" alt="OneDesign Studios" width="1020" height="232" loading="lazy"></a></div></div>
      </div>
    </div>
    <div class="foot-bottom"><span>© 2026 Onesign &amp; Digital. All rights reserved.</span><span>Made in Team Valley, fitted across the UK.</span></div>
  </div>
</footer>
<div class="mob-cta" id="mobCta">
  <a class="pill pill-ghost" href="tel:+441914876767">call us</a>
  <a class="pill pill-solid" href="#contact">free mockup</a>
</div>'''

# HubSpot meetings link for 'book a slot'. Leave empty until Mak sends it.
HUBSPOT_MEETINGS = ""
def cta(heading="let's make<br>it happen.", eyebrow="Free mockup"):
    BOOK = (f'Prefer to pick a time? <a href="{HUBSPOT_MEETINGS}" target="_blank" rel="noopener">Book a call slot →</a>' if HUBSPOT_MEETINGS else 'Prefer to talk now? Call <a href="tel:+441914876767">0191 487 6767</a>')
    opts = '<option value="">Not sure yet</option>' + "".join(f'<option>{E(t["name"])}</option>' for t in TYPES)
    return f'''<section class="cta onacc" id="contact">
  <div class="wrap cta-grid">
    <div>
      <span class="eyebrow">{eyebrow}</span>
      <h2 class="rv" style="margin-top:20px">{heading}</h2>
      <ul class="promise">
        <li>A free visual of your new sign on a photo of your building</li>
        <li>Advice on planning and building regulations before you commit</li>
        <li>One clear price covering design, manufacture and installation</li>
      </ul>
      <div class="contact-block">
        <div><small>Call</small><a href="tel:+441914876767">0191 487 6767</a></div>
        <div><small>Email</small><a href="mailto:sales@onesignanddigital.com">sales@onesignanddigital.com</a></div>
        <div><small>Visit</small><span>D86 Princesway North<br>Gateshead NE11 0TU</span></div>
        <div><small>Opening times</small><span class="hours">Mon–Thu 07:00–16:00<br>Fri 07:00–12:00 · Sat–Sun closed</span></div>
      </div>
    </div>
    <form class="mock lightc live" id="mockForm" novalidate>
      <div class="hide-sent full live-head">
        <span class="live-kicker"><i class="live-dot" aria-hidden="true"></i>Free mockup &middot; free survey</span>
        <h3>tell us about your sign</h3>
        <p class="live-sub">Leave your details and one of our sign team calls you back. We'll talk it through, then send a free visual of your sign on your building.</p>
        <div class="live-slot" id="liveSlot" aria-live="polite"><i class="live-dot" aria-hidden="true"></i><span>Next available call: <b id="liveSlotTime">today</b>. We'll book it in for you.</span></div>
      </div>
      <div class="hide-sent" id="f-name-wrap"><label for="f-name">Name</label><input id="f-name" name="name" autocomplete="name" placeholder="Your name here" required><div class="err">Add your name so we know who to ask for.</div></div>
      <div class="hide-sent"><label for="f-tel">Phone</label><input id="f-tel" name="phone" type="tel" autocomplete="tel" placeholder="Your phone number"></div>
      <div class="hide-sent" id="f-email-wrap"><label for="f-email">Email</label><input id="f-email" name="email" type="email" autocomplete="email" placeholder="Your email address" required><div class="err">Enter an email like name@company.co.uk.</div></div>
      <div class="hide-sent"><label for="f-biz">Business name</label><input id="f-biz" name="business" autocomplete="organization" placeholder="Your business name"></div>
      <div class="hide-sent"><label for="f-type">Sign type</label><select id="f-type" name="type">{opts}</select></div>
      <div class="hide-sent"><label for="f-post">Site postcode</label><input id="f-post" name="postcode" autocomplete="postal-code" placeholder="Your site postcode"></div>
      <fieldset class="hide-sent full chips"><legend>When do you need the signage?</legend><div class="chip-row"><label class="chip"><input type="radio" name="when" value="Within 4 weeks"><span>Within 4 weeks</span></label><label class="chip"><input type="radio" name="when" value="1–3 months"><span>1–3 months</span></label><label class="chip"><input type="radio" name="when" value="3+ months"><span>3+ months</span></label><label class="chip"><input type="radio" name="when" value="Not sure yet"><span>Not sure yet</span></label></div></fieldset>
      <fieldset class="hide-sent full chips"><legend>Rough budget <em>optional</em></legend><div class="chip-row"><label class="chip"><input type="radio" name="budget" value="Under £2k"><span>Under £2k</span></label><label class="chip"><input type="radio" name="budget" value="£2k–£5k"><span>£2k–£5k</span></label><label class="chip"><input type="radio" name="budget" value="£5k–£10k"><span>£5k–£10k</span></label><label class="chip"><input type="radio" name="budget" value="£10k+"><span>£10k+</span></label></div></fieldset>
      <div class="hide-sent full"><label for="f-msg">Anything else?</label><textarea id="f-msg" name="message" placeholder="Your sizes, wording, anything you know so far"></textarea></div>
      <label class="drop hide-sent full" id="drop" for="f-file"><input type="file" id="f-file" accept="image/*" multiple><span id="dropText">Add a photo of your building, or <u>browse</u>. It's what we draw your mockup on.</span></label>
      <label class="callme hide-sent full"><input type="checkbox" id="f-call" checked><span>Call me back to talk it through</span></label>
      <button class="glow-btn hide-sent full" type="submit"><svg viewBox="0 0 24 24" width="18" height="18" aria-hidden="true"><path fill="currentColor" d="M6.6 10.8a15.1 15.1 0 0 0 6.6 6.6l2.2-2.2a1 1 0 0 1 1-.25 11.4 11.4 0 0 0 3.6.57 1 1 0 0 1 1 1V20a1 1 0 0 1-1 1A17 17 0 0 1 3 4a1 1 0 0 1 1-1h3.5a1 1 0 0 1 1 1c0 1.25.2 2.45.57 3.57a1 1 0 0 1-.25 1z"/></svg><span id="sendLabel">send &amp; call me back</span></button>
      <p class="live-alt hide-sent full">{BOOK}</p>
      <div class="live-trust hide-sent full"><span><b class="stars">★★★★★</b> {REVIEWS["count"]} Google reviews</span><span>No obligation</span><span>UK-wide, since 2008</span></div>
      <p class="form-note hide-sent full">We only use your details to reply to this enquiry. <a href="{{{{R}}}}privacy.html">Privacy policy</a>.</p>
      <div class="form-done" role="status"><h3 style="font-size:28px;margin-bottom:8px">thanks, <span id="doneName">there</span>.</h3><p style="color:var(--fg-2)" id="doneMsg">Your enquiry is in. A member of our team will be in touch to talk through your mockup.</p></div>
    </form>
  </div>
</section>'''

BUSINESS = {
  "@context":"https://schema.org","@type":"LocalBusiness","@id":SITE_URL+"/#business",
  "name":"Onesign & Digital","url":SITE_URL+"/","logo":SITE_URL+"/img/brand/onesign-logo-white.png","image":SITE_URL+"/img/og/hero.jpg","priceRange":"££",
  "description":"Family-run sign makers in Gateshead, designing, manufacturing and installing signage since 2008.",
  "telephone":"+44 191 487 6767","email":"sales@onesignanddigital.com","foundingDate":"2008",
  "address":{"@type":"PostalAddress","streetAddress":"D86 Princesway North, Team Valley","addressLocality":"Gateshead","postalCode":"NE11 0TU","addressCountry":"GB"},
  "areaServed":["Newcastle upon Tyne","Gateshead","Sunderland","Durham","South Tyneside","Northumberland","North East England","United Kingdom"],
  "hasMap":REVIEWS["url"],
  "openingHoursSpecification":[
    {"@type":"OpeningHoursSpecification","dayOfWeek":["Monday","Tuesday","Wednesday","Thursday"],"opens":"07:00","closes":"16:00"},
    {"@type":"OpeningHoursSpecification","dayOfWeek":"Friday","opens":"07:00","closes":"12:00"}],
  "sameAs":["https://www.instagram.com/onesignanddigital/","https://www.facebook.com/onesignanddigital/","https://www.tiktok.com/@onesignanddigital"],
  "parentOrganization":{"@type":"Organization","name":"One Group"}
}

def crumbs_ld(items):
    return {"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":[
        {"@type":"ListItem","position":i+1,"name":n,"item":SITE_URL+u} for i,(n,u) in enumerate(items)]}

# HubSpot Forms API ids. Fill both in and every enquiry form posts straight to HubSpot.
HUBSPOT = dict(portal="", form="")
HS_SNIPPET = f'<script>window.OS_FORM={json.dumps(HUBSPOT)}</script>\n' if HUBSPOT["portal"] and HUBSPOT["form"] else ""
PAGES = []

# Sections that share a background run together: the second one drops its top padding ("flush"),
# so two paddings never stack. Sections on different backgrounds always keep both paddings.
_BG = {"sec":"page","types":"page","work":"page","sec alt":"white","process":"white","rating":"white","sectors":"white"}
def _bg(cls):
    c = cls.split()
    if not c: return None
    if c[0] == "sec": return "white" if "alt" in c else "page"
    return _BG.get(c[0])
def flush_sections(html):
    out, pos, depth, prev = [], 0, 0, None
    for m in re.finditer(r'<(/?)section\b([^>]*)>', html):
        if m.group(1):
            depth -= 1; continue
        depth += 1
        if depth != 1: continue
        cm = re.search(r'class="([^"]*)"', m.group(2)); cls = cm.group(1) if cm else ""
        bg = _bg(cls)
        if bg and bg == prev and "flush" not in cls.split():
            tag = m.group(0).replace(f'class="{cls}"', f'class="{cls} flush"')
            out.append(html[pos:m.start()]); out.append(tag); pos = m.end()
        prev = bg
    out.append(html[pos:]); return "".join(out)

def page(path, *, title, desc, canonical, body, ogimg, r, ld=(), bodyattrs="", ogtype="website", preload=None):
    PAGES.append(path)
    body = flush_sections(body)
    lds = "\n".join(f'<script type="application/ld+json">{json.dumps(x,ensure_ascii=False)}</script>' for x in [BUSINESS,*ld])
    doc = f'''<!doctype html>
<html lang="en-GB">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{E(title)}</title>
<meta name="description" content="{E(desc)}">
<link rel="canonical" href="{canonical}">
<meta property="og:type" content="{ogtype}">
<meta property="og:site_name" content="Onesign &amp; Digital">
<meta property="og:title" content="{E(title)}">
<meta property="og:description" content="{E(desc)}">
<meta property="og:url" content="{canonical}">
<meta property="og:image" content="{ogimg}">
<meta property="og:locale" content="en_GB">
<meta name="twitter:card" content="summary_large_image">
<meta name="theme-color" content="#111415">
<link rel="icon" href="{r}assets/favicon.svg" type="image/svg+xml">
<link rel="preload" href="{r}assets/fonts/outfit-latin-wght-normal.woff2" as="font" type="font/woff2" crossorigin>
<link rel="preload" href="{r}assets/fonts/inter-latin-wght-normal.woff2" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="{r}assets/site.css?v={ASSET_V}">
{lds}
</head>
<body{bodyattrs}>
<a class="skip" href="#main">Skip to content</a>
{nav(r)}
<main id="main">
{body}
</main>
{footer(r)}
<script src="{r}assets/vendor/gsap.min.js" defer></script>
{HS_SNIPPET}<script src="{r}assets/vendor/ScrollTrigger.min.js" defer></script>
<script src="{r}assets/site.js?v={ASSET_V}" defer></script>
</body>
</html>
'''
    doc = doc.replace('content="{{R}}', 'content="'+SITE_URL+'/').replace("{{R}}", r)
    if r != "/": doc = re.sub(r'href="((?:\.\./)*)index\.html(#[^"]*)?"', lambda m: 'href="' + (m.group(1) or "./") + (m.group(2) or "") + '"', doc)
    full = os.path.join(OUT, path)
    os.makedirs(os.path.dirname(full), exist_ok=True)
    open(full, "w").write(doc)
    return path

def phero(r, crumbs, h1, lede, img=None, ctas=True, plain=False, kicker=None, meta=""):
    cr = "".join((f'<li><a href="{r}{u}">{E(n)}</a></li>' if u is not None else f'<li aria-current="page">{E(n)}</li>') for n,u in crumbs)
    bg = f'<div class="bgimg">{pic(img, "100vw", lazy=False, prio=True, style="object-position:"+pos(img))}</div>' if img else ""
    btns = f'''<div class="hero-cta"><a class="pill pill-solid" href="#contact">get a free mockup <span class="dot">→</span></a><a class="pill pill-ghost" href="tel:+441914876767">call 0191 487 6767</a></div>''' if ctas else ""
    return f'''<section class="phero{' plain' if plain or not img else ''}">
  {bg}
  <div class="wrap phero-in">
    <nav aria-label="Breadcrumb"><ol class="crumbs">{cr}</ol></nav>
    {f'<span class="eyebrow ph-kick">{E(kicker)}</span>' if kicker else ""}
    <h1>{h1}</h1>
    <p class="lede">{lede}</p>
    {meta}
    {btns}
  </div>
</section>'''

def gallery(keys, r, captions=True):
    if not keys:
        return '<div class="gallery-empty"><b>Project photos coming soon</b>We make these regularly. Ask us and we\'ll send you examples of recent jobs.</div>'
    figs = "".join(
        f'<figure data-full="{wix(k,1800,1800,"fit")}" data-cap="{E(cap(k)) if captions else ""}">{pic(k, "(max-width:620px) 92vw, (max-width:980px) 46vw, 31vw")}{f"<figcaption>{E(cap(k))}</figcaption>" if captions else ""}</figure>'
        for k in keys)
    return f'<div class="gallery{"" if captions else " grid"}">{figs}</div>'

def link_card(href, img, title, text, icon=None):
    ico = f'<span class="ico"><img alt="" src="{{{{R}}}}img/brand/icon-{icon}.png" width="36" height="36" loading="lazy"></span>' if icon else ""
    ph = pic(img, "(max-width:620px) 92vw, (max-width:980px) 46vw, 31vw", alt="", style="object-position:"+pos(img), widths=(480,960)) if img else ""
    return f'<a class="sector" href="{href}"><div class="ph">{ph}</div><div class="body{"" if icon else " noico"}">{ico}<div><h3>{E(title)}</h3><p>{E(text)}</p></div><span class="arr">→</span></div></a>'

CASE = {c["slug"]: c for c in CASES}
def cases_for(type_slug=None, sector=None, n=3):
    out = [c for c in CASES if (type_slug and type_slug in c["types"]) or (sector and c["sector"] == sector)]
    return out[:n]
def case_card(c, r, sizes="(max-width:620px) 92vw, (max-width:980px) 46vw, 31vw"):
    where = f'<span class="cc-where">{E(c["where"])}</span>' if c["where"] else ""
    return (f'<a class="ccard" href="{r}work/{c["slug"]}.html"><div class="cc-img">{pic(c["hero"], sizes, alt=c["name"]+" signage by Onesign", style="object-position:"+pos(c["hero"]), widths=(480,960))}</div>'
            f'<div class="cc-body"><small>{E(c["label"])}</small><h3>{E(c["name"])}</h3>{where}<span class="cc-go" aria-hidden="true">→</span></div></a>')
def guide_card(g, r):
    return (f'<a class="gcard" href="{r}guides/{g["slug"]}.html"><img class="gc-img" loading="lazy" alt="" src="{wix(g.get("card", g["hero"]),720,480)}" style="object-position:{pos(g.get("card", g["hero"]))}"><small>{E(g["kicker"])}</small><h3>{E(g["h1"])}</h3><p>{E(g["desc"])}</p><span class="gc-go">read the guide <span aria-hidden="true">→</span></span></a>')
HQ = (54.9330, -1.6237)  # Onesign & Digital, D86 Princesway North, Team Valley (from workshop photo GPS)
def map_block(r, area=None, cls="", hq=True, title=None):
    """Branded Leaflet map of fitted jobs (and our HQ). Leaflet + tiles load only when the map scrolls near."""
    jobs = []
    for s, (place, ar, lat, lng, _src) in LOC.items():
        if s not in CASE or (area and ar != area): continue
        c = CASE[s]
        jobs.append({"n": c["name"], "p": place, "t": c["label"], "lat": lat, "lng": lng, "u": f"{r}work/{s}.html", "i": wix(c["hero"], 480, 360)})
    data = {"hq": list(HQ) if hq else None, "jobs": jobs, "area": area}
    return (f'<div class="jobmap {cls}" data-map=\'{json.dumps(data, ensure_ascii=False).replace(chr(39), "&#39;")}\' role="region" aria-label="{E(title or "Map of signs we have fitted")}">'
            f'<div class="jm-fallback"><b>{len(jobs)} jobs on the map</b><span>Loading map…</span></div></div>')
def all_type_cards(r, cases):
    """Every sign type as a card; the photo comes from one of the given jobs when one used that type."""
    used, out = set(), []
    for t in TYPES:
        # only a photo already curated into this sign type's gallery, so the card always shows that type of sign
        theirs = {p for c in cases for p in [c["hero"]] + list(c.get("photos") or [])}
        img = next((p for p in t["photos"] if p in theirs and p not in used), t["hero"])
        used.add(img)
        out.append(link_card(f'{r}signs/{t["slug"]}.html', img, t["label"], t["desc"][:96].rsplit(" ", 1)[0] + "…"))
    return f'<div class="cards3">{"".join(out)}</div>'
def area_chips(r, skip=None):
    return "".join(f'<a href="{r}areas/{a["slug"]}.html">Sign makers in {E(a["short"])}</a>' for a in AREAS if a["slug"] != skip) + f'<a href="{r}nationwide-signage.html">Nationwide</a>'
ILLUMINATED = {"3d-letters","backlit-panels","light-boxes","flex-faces","neon-led-neon","high-level-signs","projecting-signs","totems-monoliths"}
def guides_for(type_slug):
    G = {g["slug"]: g for g in GUIDES}
    if type_slug in ("3d-letters", "flat-cut-letters"): order = ["3d-vs-flat-cut-letters", "illuminated-signs", "shop-sign-cost"]
    elif type_slug == "wayfinding": order = ["accessible-wayfinding-signage", "sign-planning-permission", "shop-sign-cost"]
    elif type_slug in ILLUMINATED: order = ["illuminated-signs", "sign-planning-permission", "shop-sign-cost"]
    else: order = ["shop-sign-cost", "sign-planning-permission", "illuminated-signs"]
    return [G[x] for x in order]

MINI_STEPS = '''<ol class="mini-steps">
  <li><b>01</b><h3>concept &amp; survey</h3><p>We visit, measure up and talk through the options for your building and budget.</p></li>
  <li><b>02</b><h3>design</h3><p>Scaled visuals on your actual premises, so you sign off on exactly what you'll get.</p></li>
  <li><b>03</b><h3>manufacture</h3><p>Cut, folded, welded, printed and wired in our Team Valley workshop.</p></li>
  <li><b>04</b><h3>install</h3><p>Fitted by our own teams, from a single fascia to high-level work.</p></li>
</ol>'''

# --------------------------------------------------------------- sign type pages
def type_page(t):
    r = "../"
    TS = types_by_slug()
    url = f"{SITE_URL}/signs/{t['slug']}"
    variants = ""
    if t["variants"]:
        cards = ""
        for v in t["variants"]:
            fr = (f'<div class="frame"><img class="b" alt="" loading="lazy" src="{wix(v["img"],80,60)}"><img class="f" loading="lazy" alt="{E(cap(v["img"]))}" src="{wix(v["img"],800,600,"fit")}"></div>' if v["img"]
                  else '<div class="frame"><div class="soon" style="position:absolute"><div><span>photos coming soon</span></div></div></div>')
            tags = "".join(f"<span>{E(x)}</span>" for x in v["tags"])
            cards += f'<article class="variant">{fr}<div class="txt"><h3>{E(v["t"])}</h3><p>{E(v["p"])}</p><div class="tags">{tags}</div></div></article>'
        variants = f'''<section class="sec"><div class="wrap">
  <div class="sec-head"><div><span class="eyebrow">Options</span><h2 class="h2 rv">choose your build.</h2></div></div>
  <div class="variants">{cards}</div></div></section>'''
    spec = "".join(f"<dt>{E(a)}</dt><dd>{E(b)}</dd>" for a,b in t["spec"])
    notes = "".join(f"<li>{E(n)}</li>" for n in t["notes"])
    ideal = "".join(f'<span class="tag">{E(x)}</span>' for x in t["ideal"])
    faq = "".join(f"<details><summary>{E(q)}</summary><p>{E(a)}</p></details>" for q,a in t["faq"])
    idx = [x["slug"] for x in TYPES].index(t["slug"])
    rel = [TYPES[(idx+i) % len(TYPES)] for i in (1,2,3)]
    related = "".join(link_card(f'{x["slug"]}.html', x["hero"], x["label"], x["desc"][:96].rsplit(" ",1)[0]+"…") for x in rel)
    sectors = [s for s in SECTORS if t["slug"] in s["types"]]
    sec_chips = "".join(f'<a href="../sectors/{s["slug"]}.html">{E(s["name"])}</a>' for s in sectors)
    cs = cases_for(type_slug=t["slug"])
    cases_html = f'''<section class="sec alt"><div class="wrap">
  <div class="sec-head"><div><span class="eyebrow">Case studies</span><h2 class="h2 rv">seen on real projects.</h2></div><a class="pill pill-ghost" href="../work/index.html">all our work <span class="dot">→</span></a></div>
  <div class="ccards">{"".join(case_card(c, r) for c in cs)}</div></div></section>''' if cs else ""
    body = f'''{phero(r, [("Home","index.html"),("Sign types","signs/index.html"),(t["name"],None)], E(t["label"])+".", E(t["desc"]), t["hero"])}
<section class="sec"><div class="wrap">
  <div class="sec-head"><div><span class="eyebrow">Fitted by us</span><h2 class="h2 rv">real jobs, real photos.</h2></div><p class="lede rv">Tap any photo to see it full size.</p></div>
  {gallery(t["photos"], r)}
</div></section>
{variants}
{cases_html}
<section class="sec"><div class="wrap spec-grid">
  <div class="spec">
    <header><span>Spec sheet</span><span>{t["code"]}</span></header>
    <dl>{spec}</dl>
  </div>
  <div class="notes">
    <h3>good to know.</h3>
    <ul>{notes}</ul>
    <div><span class="eyebrow" style="margin-bottom:12px;display:flex">Works well for</span><div class="ideal-row">{ideal}</div></div>
    {f'<div><span class="eyebrow" style="margin-bottom:12px;display:flex">Popular in</span><div class="chips-row">{sec_chips}</div></div>' if sec_chips else ""}
  </div>
</div></section>
<section class="sec alt"><div class="wrap">
  <div class="sec-head"><div><span class="eyebrow">How it works</span><h2 class="h2 rv">one team, start to finish.</h2></div></div>
  {MINI_STEPS}
</div></section>
<section class="sec"><div class="wrap">
  <div class="sec-head"><div><span class="eyebrow">Questions</span><h2 class="h2 rv">{E(t["label"])}, answered.</h2></div></div>
  <div class="faq">{faq}</div>
</div></section>
<section class="sec alt"><div class="wrap">
  <div class="sec-head"><div><span class="eyebrow">Before you order</span><h2 class="h2 rv">useful guides.</h2></div></div>
  <div class="gcards">{"".join(guide_card(g, r) for g in guides_for(t["slug"]))}</div>
</div></section>
<section class="sec"><div class="wrap">
  <div class="sec-head"><div><span class="eyebrow">Keep exploring</span><h2 class="h2 rv">other sign types.</h2></div><a class="pill pill-ghost" href="index.html">all sign types <span class="dot">→</span></a></div>
  <div class="cards3">{related}</div>
  <div class="made-in"><p>Every sign is made in our Team Valley factory in Gateshead and fitted by our own installers across the North East and the UK.</p><div class="chips-row">{area_chips(r)}</div></div>
</div></section>
{cta("let's price<br>your sign.", "Free mockup")}'''
    ld = [crumbs_ld([("Home","/"),("Sign types","/signs"),(t["name"],f"/signs/{t['slug']}")]),
          {"@context":"https://schema.org","@type":"Service","name":t["name"],"serviceType":t["name"],"description":t["meta"],
           "provider":{"@id":SITE_URL+"/#business"},"areaServed":"United Kingdom","url":url},
          {"@context":"https://schema.org","@type":"FAQPage","mainEntity":[{"@type":"Question","name":q,"acceptedAnswer":{"@type":"Answer","text":a}} for q,a in t["faq"]]}]
    return page(f"signs/{t['slug']}.html", title=f"{t['seo_title']} | Onesign, Newcastle", desc=t["meta"], canonical=url,
                body=body, ogimg=og(t["hero"]), r=r, ld=ld, bodyattrs=f' data-signtype="{E(t["name"])}"')

# --------------------------------------------------------------- sector pages
def sector_page(s):
    r = "../"; TS = types_by_slug()
    url = f"{SITE_URL}/sectors/{s['slug']}"
    tcards = all_type_cards(r, [c for c in CASES if c.get("sector") == s["slug"]])
    points = "".join(f'<div class="point"><h3>{E(a)}</h3><p>{E(b)}</p></div>' for a,b in s["points"])
    others = "".join(f'<a href="{o["slug"]}.html">{E(o["name"])}</a>' for o in SECTORS if o["slug"]!=s["slug"])
    cs = cases_for(sector=s["slug"])
    cases_html = f'''<section class="sec alt"><div class="wrap">
  <div class="sec-head"><div><span class="eyebrow">Case studies</span><h2 class="h2 rv">{E(s["name"])} projects.</h2></div><a class="pill pill-ghost" href="../work/index.html">all our work <span class="dot">→</span></a></div>
  <div class="ccards">{"".join(case_card(c, r) for c in cs)}</div></div></section>''' if cs else ""
    body = f'''{phero(r, [("Home","index.html"),("Sectors","sectors/index.html"),(tcap(s["name"]),None)], E(s["name"])+" signage.", E(s["intro"]), s["img"])}
<section class="sec"><div class="wrap">
  <div class="points">{points}</div>
</div></section>
<section class="sec alt"><div class="wrap">
  <div class="sec-head"><div><span class="eyebrow">What we make</span><h2 class="h2 rv">every sign type, for {E(s["name"])}.</h2></div><p class="lede rv">We make all fifteen in-house. Where we have fitted one for a {E(s["name"])} client, that is the photo you see.</p></div>
  {tcards}
</div></section>
<section class="sec"><div class="wrap">
  <div class="sec-head"><div><span class="eyebrow">Fitted by us</span><h2 class="h2 rv">recent {E(s["name"])} work.</h2></div><p class="lede rv">Tap any photo to see it full size.</p></div>
  {gallery(s["gallery"], r)}
</div></section>
{cases_html}
<section class="sec alt tight"><div class="wrap">
  <span class="eyebrow" style="margin-bottom:16px;display:flex">Other sectors</span>
  <div class="chips-row">{others}</div>
  <div class="made-in"><p>Made in Team Valley, Gateshead, and fitted by our own installers across the North East and the UK.</p><div class="chips-row">{area_chips(r)}</div></div>
</div></section>
{cta()}'''
    ld = [crumbs_ld([("Home","/"),("Sectors","/sectors"),(tcap(s["name"]),f"/sectors/{s['slug']}")])]
    return page(f"sectors/{s['slug']}.html", title=f"{s['title']} | Onesign, North East & UK", desc=s["intro"][:155].rsplit(" ",1)[0]+".",
                canonical=url, body=body, ogimg=og(s["img"]), r=r, ld=ld)

# --------------------------------------------------------------- about
def about_page():
    r = ""
    machines = "".join(f'<div class="mach"><span class="mach-n">{i+1:02d}</span><h3>{E(n)}</h3><p>{E(d)}</p></div>' for i,(n,d) in enumerate(MACHINES))
    caps = [("Design","Artwork, technical drawings and photo mockups so you see the sign on your building first."),
            ("Cut","CNC routing, laser cutting and precision engraving for letters, panels and shapes."),
            ("Fabricate","Folding, welding and assembling metal letters, trays, totems and frames."),
            ("Print","Large-format print up to 1200 dpi on board, acrylic, metal, timber and vinyl."),
            ("Finish","Spray finishing in your brand colours, LED wiring and quality checks."),
            ("Install","Our own IPAF and PASMA trained crews fit every sign, from shopfronts to high level.")]
    capcards = "".join(f'<div class="capc"><h3>{E(a)}</h3><p>{E(b)}</p></div>' for a,b in caps)
    body = f'''{phero(r, [("Home","index.html"),("About us",None)], "family-run sign makers since 2008.", "Founded in the North East and trusted nationwide. Everything from design to installation happens under one roof in our Team Valley factory.", "ws_assembly")}
<section class="sec"><div class="wrap two about-intro">
  <div class="prose">
    <span class="eyebrow" style="margin-bottom:18px;display:flex">Our story</span>
    <h2>one roof, every step.</h2>
    <p>Onesign has been family-run since 2008 and brings over 40 years of sign-making experience under one roof. From our 10,000 sq ft production facility in Team Valley, Gateshead, we make and fit signs for businesses across the UK.</p>
    <p>We manage everything in-house: design, digital print, fabrication, assembly and installation. Each department has its own expert team, so every job gets the same precision and care whatever its size, and you deal with the same people from first call to final fixing.</p>
    <p>We keep investing in the kit to match. Our newest addition is a laser cutter, working alongside our CNC router, brake press and large-format printers.</p>
  </div>
  <div class="about-side">
    <div class="figures">
      <div class="fig"><b>2008</b><span>Family-run since day one</span></div>
      <div class="fig"><b>10,000</b><span>Sq ft production facility</span></div>
      <div class="fig"><b><span data-count="100">100</span><sup>%</sup></b><span>Made and fitted in-house</span></div>
      <div class="fig"><b>4.9<sup>★</sup></b><span>From 72 Google reviews</span></div>
    </div>
    <div class="accred"><small>Accredited</small><img src="{ACCRED}" alt="Acclaim, IPAF, PASMA, Constructionline, CSCS and SCHQ accreditations" width="720" height="76"></div>
  </div>
</div></section>
<section class="sec alt"><div class="wrap">
  <div class="sec-head"><div><span class="eyebrow">What we do in-house</span><h2 class="h2 rv">from drawing to fixing.</h2></div><p class="lede rv">Six disciplines, one team and one factory, so nothing gets lost in a handover.</p></div>
  <div class="caps">{capcards}</div>
</div></section>
<section class="sec"><div class="wrap">
  <div class="sec-head"><div><span class="eyebrow">Inside the factory</span><h2 class="h2 rv">made in Team Valley.</h2></div><p class="lede rv">Cutting, folding, welding, printing, spraying and wiring all happen in our own Gateshead factory.</p></div>
  {gallery(WORKSHOP, r, captions=False)}
</div></section>
<section class="sec alt"><div class="wrap">
  <div class="sec-head"><div><span class="eyebrow">Our machinery</span><h2 class="h2 rv">the kit behind the signs.</h2></div><p class="lede rv">Some of the most advanced sign-making technology in the industry, so we can cut, print, fabricate and assemble with accuracy and keep quality control in our own hands.</p></div>
  <div class="machs">{machines}</div>
</div></section>
<section class="sec" id="process"><div class="wrap">
  <div class="sec-head"><div><span class="eyebrow">How we work</span><h2 class="h2 rv">one team, start to finish.</h2></div></div>
  {MINI_STEPS}
</div></section>
<section class="sec alt"><div class="wrap">
  <div class="sec-head"><div><span class="eyebrow">Sister companies</span><h2 class="h2 rv">part of a bigger family.</h2></div></div>
  <div class="fam-cards">
    <a class="fam-card" href="https://www.onelasercutting.com/" target="_blank" rel="noopener">{ONELASER_SVG}<p>Precision laser cutting for metal sheet and profiles, from one-offs to production runs.</p><span>onelasercutting.com →</span></a>
    <a class="fam-card" href="https://www.onedesignstudios.com/" target="_blank" rel="noopener"><img src="{ONEDESIGN}" alt="OneDesign Studios" width="1020" height="232"><p>A branding and creative studio in the North East: identities, print and digital design.</p><span>onedesignstudios.com →</span></a>
  </div>
</div></section>
{cta()}'''
    return page("about.html", title="About Onesign & Digital | Sign Makers & Factory, Gateshead",
                desc="Family-run since 2008, Onesign & Digital designs, manufactures and installs signage from a 10,000 sq ft factory in Team Valley, Gateshead, for clients across the UK.",
                canonical=SITE_URL+"/about", body=body, ogimg=og("ws_assembly"), r=r,
                ld=[crumbs_ld([("Home","/"),("About us","/about")])])

# --------------------------------------------------------------- contact
def contact_page():
    r = ""
    body = f'''{phero(r, [("Home","index.html"),("Contact",None)], "let's talk signs.", "Tell us what you're planning and send a photo of your building. We'll come back with ideas, a free mockup and a clear price.", None, ctas=False, plain=True)}
{cta("tell us about<br>your project.", "Get in touch")}
<section class="sec"><div class="wrap">
  <div class="sec-head"><div><span class="eyebrow">What happens next</span><h2 class="h2 rv">from enquiry to install.</h2></div></div>
  {MINI_STEPS}
</div></section>
<section class="sec alt"><div class="wrap">
  {map_block(r, None, "hq", title="Find Onesign & Digital in Team Valley, Gateshead")}
  <div class="find">
    <div class="point"><h3>visit us</h3><p>D86 Princesway North<br>Team Valley, Gateshead<br>NE11 0TU</p><p style="margin-top:14px"><a href="https://www.google.com/maps/search/?api=1&amp;query=Onesign+%26+Digital+Princesway+North+Gateshead+NE11+0TU" target="_blank" rel="noopener">Open in Google Maps →</a></p></div>
    <div class="point"><h3>opening times</h3><p>Monday to Thursday: 07:00–16:00<br>Friday: 07:00–12:00<br>Saturday and Sunday: closed</p></div>
    <div class="point"><h3>call or email</h3><p>0191 487 6767<br>sales@onesignanddigital.com</p></div>
  </div>
</div></section>'''
    return page("contact.html", title="Contact Onesign & Digital | Sign Makers in Gateshead",
                desc="Get a free sign mockup and quote from Onesign & Digital, Team Valley, Gateshead. Call 0191 487 6767 or send us a photo of your building.",
                canonical=SITE_URL+"/contact", body=body, ogimg=og("hero"), r=r,
                ld=[crumbs_ld([("Home","/"),("Contact","/contact")])])

# --------------------------------------------------------------- home
def home_page():
    r = ""
    TS = types_by_slug()
    # explorer data
    data = []
    for t in TYPES:
        data.append(dict(name=t["name"], label=t["label"], code=t["code"], desc=t["desc"], ideal=t["ideal"], spec=t["spec"],
            url=f"signs/{t['slug']}.html",
            photos=[dict(full=wix(k,1600,1100,"fit"), bg=wix(k,80,60), thumb=wix(k,140,100), cap=cap(k)) for k in t["photos"][:14]]))
    tabs = "".join(f'<li><button role="tab" id="tab-{t["slug"]}" aria-selected="{"true" if i==0 else "false"}" aria-controls="typePanel" tabindex="{0 if i==0 else -1}"><span class="n">{i+1:02d}</span><span class="t">{E(t["label"])}</span><span class="arr">→</span></button></li>' for i,t in enumerate(TYPES))
    t0 = TYPES[0]
    spec0 = "".join(f"<dt>{E(a)}</dt><dd>{E(b)}</dd>" for a,b in t0["spec"])
    ideal0 = "".join(f'<span class="tag">{E(x)}</span>' for x in t0["ideal"])
    def _logo_row(ids):
        return "".join(f'<img src="img/brand/client-{n:02d}.png" alt="{"Client logo" if j < len(ids) else ""}"{"" if j < len(ids) else " aria-hidden=\"true\""} draggable="false" decoding="async" width="150" height="46">' for j, n in enumerate(ids + ids))
    _ids = list(range(1, len(CLIENT_LOGOS) + 1))
    logos_a, logos_b, logos_all = _logo_row(_ids[0::2]), _logo_row(_ids[1::2]), _logo_row(_ids)
    def reel(keys):
        out=""
        for i,k in enumerate(keys+keys):
            dup = i>=len(keys)
            out += f'<figure{" aria-hidden=\"true\"" if dup else ""}>{pic(k, "(max-width:700px) 70vw, 380px", alt="" if dup else cap(k), style="object-position:"+pos(k), widths=(480,960))}<figcaption>{E(cap(k))}</figcaption></figure>'
        return out
    LINK = {"st_sign":"work/bar-seventy-three.html","p_vt_night":"work/vertu-motors-arena.html","n_jet2":"work/jet2-dawson-sanderson.html","nhs":"work/nhs-community-diagnostic-centre.html",
            "hero":"work/newcastle-university.html","aldi_bld":"work/aldi-jaymac-warehouse.html","n_thatype":"signs/3d-letters.html","n_superpower_wide":"work/superpower-metrocentre.html"}
    tiles = ""
    for i,p in enumerate(PROJECTS):
        w, h = dims(p["k"]); ar = w / h
        # each tile takes the photo's own shape, so the photo fills it with nothing cut off
        media = pic(p["k"], "(max-width:700px) 92vw, 45vw", alt=p["name"]+" sign by Onesign")
        tiles += f'<a class="tile jt" style="--ar:{ar:.4f};aspect-ratio:{w}/{h}" href="{LINK[p["k"]]}">{media}<div class="tile-info"><div><small>{E(p["label"])}</small><h3>{E(p["name"])}</h3></div><span class="go" aria-hidden="true">→</span></div></a>'
    HERO = [("hero","Newcastle University","Fabricated building sign","work/newcastle-university.html"),
            ("vertu","Vertu Motors Arena","High-level building letters","work/vertu-motors-arena.html"),
            ("n_thatype","Thatype","Halo-lit script letters","signs/3d-letters.html"),
            ("cork_dusk","Cork & Coffee","Komacel 3D letters","work/cork-and-coffee.html")]
    slides = "".join(f'<div class="hs{" on" if i==0 else ""}">{pic(k, "100vw", alt=n+": "+l.lower()+" by Onesign", lazy=i>0, prio=i==0, style="object-position:"+("60% 40%" if i==0 else pos(k)))}</div>' for i,(k,n,l,u) in enumerate(HERO))
    hnow = "".join(f'<a class="hn{" on" if i==0 else ""}" href="{u}"><span class="hn-n">{i+1:02d}</span><span class="hn-t"><b>{E(n)}</b><small>{E(l)}</small></span><i></i></a>' for i,(k,n,l,u) in enumerate(HERO))
    arealist = "".join(f'<a class="arow" href="areas/{a["slug"]}.html" data-img="{wix(a.get("stage",a["hero"]),900,900,"fit")}"><span class="ar-n">{i+1:02d}</span><span class="ar-t">{E(a["short"])}</span><span class="ar-go" aria-hidden="true">→</span></a>' for i,a in enumerate(AREAS))
    arealist += f'<a class="arow uk" href="nationwide-signage.html" data-img="{wix("rolls",900,900,"fit")}"><span class="ar-n">UK</span><span class="ar-t">Nationwide</span><span class="ar-go" aria-hidden="true">→</span></a>'
    guides = "".join(guide_card(g, r) for g in GUIDES)
    sectors = "".join(link_card(f'sectors/{s["slug"]}.html', s["img"], s["name"], s["blurb"], s["slug"]) for s in SECTORS)
    body = f'''<section class="hero" id="top">
  <div class="hero-media" id="heroMedia">{slides}</div>
  <div class="wrap hero-in">
    <div>
      <span class="eyebrow">North East sign makers · est. 2008</span>
      <h1 id="heroTitle">
        <span class="line"><span>crafting</span></span>
        <span class="line"><span id="extrude">statements,</span></span>
        <span class="line"><span>onesign at a time.</span></span>
      </h1>
      <p class="hero-sub">Sign makers in Gateshead for Newcastle, the North East and the UK. Designed, built and installed by our own team, from a single shop sign to a full hospital wayfinding scheme.</p>
      <div class="hero-cta">
        <a class="pill pill-solid" href="#contact">get a free mockup <span class="dot">→</span></a>
        <a class="pill pill-ghost" href="#types">explore sign types</a>
      </div>
    </div>
    <aside class="hero-card">
      <a class="g-row" href="{REVIEWS["url"]}" target="_blank" rel="noopener" aria-label="{REVIEWS["score"]} out of 5 from {REVIEWS["count"]} Google reviews"><div class="g-badge">G</div><div><b>{REVIEWS["score"]}</b> <span class="stars">★★★★★</span><small>{REVIEWS["count"]} Google reviews</small></div></a>
      <div class="meta">survey · design · manufacture · install<br>all under one roof in Team Valley</div>
    </aside>
  </div>
  <div class="wrap"><div class="hero-now" id="heroNow" aria-label="Featured projects">{hnow}</div></div>
</section>
<div class="trusted">
  <p>Trusted by the North East and beyond</p>
  <div id="marqueeBox"><div class="marquee one"><div class="marquee-track">{logos_all}</div></div><div class="marquee two" aria-hidden="true"><div class="marquee-track">{logos_a}</div></div><div class="marquee two rev" aria-hidden="true"><div class="marquee-track">{logos_b}</div></div></div>
</div>
<section class="intro">
  <div class="wrap intro-grid">
    <div>
      <span class="eyebrow">Family-run since 2008</span>
      <h2 class="rv" style="margin-top:18px">founded in Newcastle,<br>trusted nationwide.</h2>
      <p class="lede rv">Onesign brings over 40 years of sign and print experience under one roof. Every job is surveyed, designed, made and fitted by our own people, so you deal with one team from first call to final fixing.</p>
    </div>
    <div class="rv">
      <div class="figures">
        <div class="fig"><b>2008</b><span>Family-run since day one</span></div>
        <div class="fig"><b><span data-count="40">40</span><sup>+ yrs</sup></b><span>Sign-making experience</span></div>
        <div class="fig"><b><span data-count="100">100</span><sup>%</sup></b><span>Made and fitted in-house</span></div>
        <div class="fig"><b>{REVIEWS["score"]}<sup>★</sup></b><span>From {REVIEWS["count"]} Google reviews</span></div>
      </div>
      <div class="accred"><small>Accredited</small><img src="{ACCRED}" alt="Acclaim, IPAF, PASMA, Constructionline, CSCS and SCHQ accreditations" width="720" height="76"></div>
    </div>
  </div>
</section>
<section class="reel" aria-label="Recent installs">
  <div class="reel-row">{reel(REEL_A)}</div>
  <div class="reel-row rev">{reel(REEL_B)}</div>
</section>
<section class="types" id="types">
  <div class="wrap">
    <div class="sec-head">
      <div><span class="eyebrow">Sign types</span><h2 class="h2 rv">every kind of sign,<br>made in one workshop.</h2></div>
      <p class="lede rv">Pick a type to see real jobs we've fitted, what it's made from and where it works best.</p>
    </div>
    <div class="explorer">
      <ul class="type-list" id="typeList" role="tablist" aria-label="Sign types">{tabs}</ul>
      <div class="type-panel" id="typePanel" role="tabpanel" aria-labelledby="tab-{t0["slug"]}">
        <div class="type-stage" id="typeStage">
          <div class="layer frame on"><img class="b" alt="" src="{wix(t0["photos"][0],80,60)}"><img class="f" alt="{E(cap(t0["photos"][0]))}" src="{wix(t0["photos"][0],1600,1100,"fit")}"></div>
          <div class="thumbs" id="typeThumbs"></div>
        </div>
        <p class="stage-cap" id="typeCap">{E(cap(t0["photos"][0]))}</p>
        <div class="type-body" id="typeBody">
          <div>
            <h3 id="typeTitle">{E(t0["label"])}</h3>
            <p id="typeDesc">{E(t0["desc"])}</p>
            <div class="ideal" id="typeIdeal">{ideal0}</div>
            <div class="type-actions">
              <a class="pill pill-solid" id="typeQuote" href="#contact">quote for this sign <span class="dot">→</span></a>
            </div>
            <a class="type-more" id="typeMore" href="signs/{t0["slug"]}.html">everything about {E(t0["label"])} <span aria-hidden="true">→</span></a>
          </div>
          <div class="spec">
            <header><span>Spec sheet</span><span id="typeCode">{t0["code"]}</span></header>
            <dl id="typeSpec">{spec0}</dl>
          </div>
        </div>
      </div>
    </div>
  </div>
  <script type="application/json" id="typesData">{json.dumps(data, ensure_ascii=False).replace("</","<\\/")}</script>
</section>
<section class="process" id="process">
  <div class="wrap">
    <div class="sec-head">
      <div><span class="eyebrow">How we work</span><h2 class="h2 rv">one team, start to finish.</h2></div>
      <p class="lede rv">Signage can feel overwhelming: what to choose, what the regulations say, who to trust with the install. We handle every step ourselves, so there's one point of contact and no handovers.</p>
    </div>
    <div class="steps" id="steps">
      <div class="steps-line" aria-hidden="true"><i id="stepsBar"></i></div>
      <article class="step"><span class="step-n">01</span><div class="step-img">{pic("install2", "(max-width:900px) 80vw, 25vw", alt="Onesign fitter in a branded hard hat surveying an NHS building", style="object-position:22% 50%", widths=(480,960))}</div><h3>concept &amp; survey</h3><p>We visit, measure up and talk through the options that suit your building, budget and any planning or building-regs constraints.</p></article>
      <article class="step"><span class="step-n">02</span><div class="step-img">{pic("sitePlan", "(max-width:900px) 80vw, 25vw", alt="Design visual of a site plan for a wayfinding scheme", widths=(480,960))}</div><h3>design</h3><p>Our designers apply your branding and show you scaled visuals on your actual premises, so you sign off on exactly what you'll get.</p></article>
      <article class="step"><span class="step-n">03</span><div class="step-img">{pic("weld", "(max-width:900px) 80vw, 25vw", alt="Fabricator welding a sign frame in the Onesign workshop", widths=(480,960))}</div><h3>manufacture</h3><p>Routed, folded, welded, printed and wired in our Team Valley workshop on our own CNC, laser and large-format kit.</p></article>
      <article class="step"><span class="step-n">04</span><div class="step-img">{pic("install", "(max-width:900px) 80vw, 25vw", alt="Onesign installers fitting a high-level Aldi sign", widths=(480,960))}</div><h3>install</h3><p>Our own British fitting teams install with care, from a single fascia to high-level work on live hospital and campus sites.</p></article>
    </div>
    <div class="process-cta rv">
      <div><h3>got a project you're planning?</h3><p>Tell us what you're after. We'll come back with ideas, a free mockup and a clear price.</p></div>
      <a class="pill pill-solid" href="#contact">start your project <span class="dot">→</span></a>
    </div>
  </div>
</section>
<section class="work" id="work">
  <div class="wrap">
    <div class="sec-head">
      <div><span class="eyebrow">Our work</span><h2 class="h2 rv">recent statements.</h2></div>
      <a class="pill pill-ghost" href="work/index.html">all case studies <span class="dot">→</span></a>
    </div>
    <div class="jgrid">{tiles}</div>
  </div>
</section>
<section class="sectors" id="sectors">
  <div class="wrap">
    <div class="sec-head">
      <div><span class="eyebrow">Sectors</span><h2 class="h2 rv">signs for how your<br>space actually works.</h2></div>
      <p class="lede rv">From live hospital wards to construction hoardings, we know the rules and realities of each sector we work in.</p>
    </div>
    <div class="sector-grid">{sectors}</div>
  </div>
</section>
<section class="areas dark" id="areas">
  <div class="wrap areas-grid">
    <div>
      <span class="eyebrow">Where we work</span>
      <h2 class="h2 rv" style="margin-top:18px">made in Gateshead.<br>fitted everywhere.</h2>
      <p class="lede rv">Every sign leaves the same Team Valley factory. Most go up within an hour's drive, and our own installers fit the rest across the UK.</p>
      <div class="area-list" id="areaList">{arealist}</div>
    </div>
    <div class="area-stage" id="areaStage" aria-hidden="true"><img alt="" src="{wix(AREAS[0].get("stage",AREAS[0]["hero"]),900,900,"fit")}" loading="lazy"></div>
  </div>
</section>
<section class="rating">
  <div class="wrap rating-in">
    <div class="rt-score"><b>{REVIEWS["score"]}</b><div><span class="stars" aria-hidden="true">★★★★★</span><small>from {REVIEWS["count"]} Google reviews</small></div></div>
    <p>We would rather you heard it from our customers. Every review is public on our Google profile.</p>
    <a class="pill pill-ghost" href="{REVIEWS["url"]}" target="_blank" rel="noopener">read our reviews <span class="dot">→</span></a>
  </div>
</section>
<section class="sec" id="guides">
  <div class="wrap">
    <div class="sec-head"><div><span class="eyebrow">Guides</span><h2 class="h2 rv">straight answers<br>before you spend.</h2></div><p class="lede rv">What signs cost, when you need consent and how to choose between sign types, written by the people who make them.</p></div>
    <div class="gcards">{guides}</div>
  </div>
</section>
{cta()}'''
    return page("index.html", title="Sign Makers in Newcastle & the North East | Onesign & Digital", preload=None,
                desc="Family-run North East sign makers since 2008. 3D letters, backlit panels, building signs, wayfinding, LED neon and large format print, designed, made and installed in-house in Gateshead.",
                canonical=SITE_URL+"/", body=body, ogimg=og("hero"), r=r)

# --------------------------------------------------------------- extras
def extras(pages):
    import datetime
    today = datetime.date.today().isoformat()
    urls = []
    for p in pages:
        if p == "404.html": continue
        u = "/" + p[:-5]
        if u.endswith("/index"): u = u[:-6] or "/"
        urls.append(u)
    sm = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + "".join(
        f"  <url><loc>{SITE_URL}{u}</loc><lastmod>{today}</lastmod></url>\n" for u in urls) + "</urlset>\n"
    open(os.path.join(OUT,"sitemap.xml"),"w").write(sm)
    open(os.path.join(OUT,"robots.txt"),"w").write(f"User-agent: *\nAllow: /\n\nSitemap: {SITE_URL}/sitemap.xml\n")
    # every URL of the previous Wix site -> its new home
    R = {"/about-us":"/about","/services":"/signs","/our-work":"/work",
         "/service/exterior":"/signs/high-level-signs","/service/neon":"/signs/neon-led-neon","/service/totems":"/signs/totems-monoliths",
         "/service/wayfinding":"/signs/wayfinding","/service/vehicle-graphics-decals":"/signs/vehicle-graphics",
         "/service/large-format-digital-print":"/signs/digital-large-format-print","/service/hoarding":"/signs/digital-large-format-print",
         "/service/promotional":"/signs/digital-large-format-print","/service/graphics":"/signs/vinyl-wall-graphics",
         "/service/interior":"/signs/3d-letters","/service/informative":"/signs/wayfinding","/service/health-saftey-signs":"/sectors/health-safety",
         "/health-saftey-signs":"/sectors/health-safety","/healthcare":"/sectors/healthcare","/educational":"/sectors/education",
         "/construction":"/sectors/construction","/commercial":"/sectors/commercial","/retail":"/sectors/retail",
         "/leisure":"/sectors/hospitality-leisure","/hair-and-beauty":"/sectors/hair-beauty",
         "/signs/building-signs":"/signs/high-level-signs","/signs/lightboxes-flex-faces":"/signs/light-boxes"}
    for c in CASES:
        if c["old"]:
            R[c["old"]] = "/work/" + c["slug"]
            if "%26" in c["old"]: R[c["old"].replace("%26", "&")] = "/work/" + c["slug"]
    red = [{"source":a,"destination":b,"permanent":True} for a,b in R.items()]
    red += [{"source":"/projects/:path*","destination":"/work","permanent":True},{"source":"/service/:path*","destination":"/signs","permanent":True}]
    vercel = {"cleanUrls":True,"trailingSlash":False,"redirects":red,
              "headers":[{"source":"/assets/(.*)","headers":[{"key":"Cache-Control","value":"public, max-age=31536000, immutable"}]},
                         {"source":"/img/(.*)","headers":[{"key":"Cache-Control","value":"public, max-age=2592000"}]},
                         {"source":"/(.*)","has":[{"type":"host","value":"(?<sub>.*)\\.vercel\\.app"}],"headers":[{"key":"X-Robots-Tag","value":"noindex, nofollow"}]}]}
    open(os.path.join(OUT,"vercel.json"),"w").write(json.dumps(vercel,indent=2))
    fav = '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64"><rect width="64" height="64" rx="14" fill="#111415"/><circle cx="32" cy="32" r="20" fill="none" stroke="#fff" stroke-width="7"/><path d="M28 22h8v22h-8z" fill="#517d90"/></svg>'
    open(os.path.join(OUT,"assets","favicon.svg"),"w").write(fav)

def not_found():
    body = f'''{phero("", [("Home","index.html"),("Page not found",None)], "this page has moved.", "We've rebuilt our website. Try one of these instead, or call us on 0191 487 6767.", None, ctas=False, plain=True)}
<section class="sec"><div class="wrap"><div class="chips-row">{"".join(f'<a href="/signs/{t["slug"]}">{E(t["label"])}</a>' for t in TYPES)}</div></div></section>'''
    return page("404.html", title="Page not found | Onesign & Digital", desc="This page has moved.", canonical=SITE_URL+"/404", body=body, ogimg=og("hero"), r="/")

# --------------------------------------------------------------- css
def build_css():
    css = open(os.path.join(SRC,"base.css")).read()
    css = css.replace(";text-transform:lowercase","").replace("text-transform:lowercase;","")
    css += open(os.path.join(SRC,"extra.css")).read() + open(os.path.join(SRC,"v2.css")).read()
    open(os.path.join(OUT,"assets","site.css"),"w").write(css)


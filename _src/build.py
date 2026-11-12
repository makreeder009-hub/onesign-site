# -*- coding: utf-8 -*-
"""Generate the Onesign & Digital static site into ../onesign-site"""
import json, os, re, html as H
from data import *

OUT = os.path.join(os.path.dirname(__file__), "..", "onesign-site")
SRC = os.path.dirname(__file__)
E = H.escape

def wix(key_or_id, w, h, mode="fill", name=None):
    wid = IMG[key_or_id][0] if key_or_id in IMG else key_or_id
    if wid.startswith("local:"):
        return "{{R}}img/ig/" + wid[6:] + ("-sm" if max(w,h) <= 760 else "") + ".jpg"
    name = name or (key_or_id if key_or_id in IMG else "image")
    ext = "png" if wid.endswith(".png") else "jpg"
    return f"{WIX}{wid}/v1/{mode}/w_{w},h_{h},al_c,q_82,enc_auto/{name}.{ext}"
def cap(k): return IMG[k][1]
def pos(k): return IMG[k][2]
def types_by_slug(): return {t["slug"]: t for t in TYPES}
def sector_by_slug(): return {s["slug"]: s for s in SECTORS}
def tcap(s):  # sentence case for sector names in footer/meta
    return s[0].upper() + s[1:]

# --------------------------------------------------------------- partials
def nav(r):
    mega_cards = "".join(
        (f'<a class="mega-card" href="{r}signs/{t["slug"]}.html"><img loading="lazy" alt="" src="{wix(t["hero"],300,225)}" style="object-position:{pos(t["hero"])}"><span>{E(t["label"])}</span></a>' if t["hero"] else f'<a class="mega-card" href="{r}signs/{t["slug"]}.html"><span class="mc-ph">photos soon</span><span>{E(t["label"])}</span></a>')
        for t in TYPES)
    chips = "".join(f'<a href="{r}signs/{t["slug"]}.html">{E(t["label"])}</a>' for t in TYPES)
    return f'''<div class="progress" id="progress"></div>
<header class="nav" id="nav">
  <div class="wrap nav-in">
    <a class="logo" href="{r}index.html" aria-label="Onesign &amp; Digital home"><img src="{LOGO}" alt="Onesign &amp; Digital" width="142" height="30"></a>
    <ul class="nav-links">
      <li><button id="megaBtn" aria-expanded="false" aria-controls="mega">sign types</button></li>
      <li><a href="{r}index.html#work">our work</a></li>
      <li><a href="{r}index.html#sectors">sectors</a></li>
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
      <div class="mega-side">
        <h4>not sure what you need?</h4>
        <p>Send us a photo of your building. We'll mock up the options on it for free, so you can see them before you spend anything.</p>
        <a class="pill pill-solid" href="#contact" style="align-self:flex-start">get a free mockup <span class="dot">→</span></a>
      </div>
    </div>
  </div>
</header>
<nav class="drawer" id="drawer" aria-label="Mobile">
  <a href="{r}index.html#types">sign types</a>
  <a href="{r}index.html#work">our work</a>
  <a href="{r}index.html#sectors">sectors</a>
  <a href="{r}about.html">about</a>
  <a href="{r}contact.html">contact</a>
  <small>Sign types</small>
  <div class="chips">{chips}</div>
  <small>Call us</small>
  <a class="tel" href="tel:+441914876767">0191 487 6767</a>
</nav>'''

ONELASER_SVG = open(os.path.join(SRC, "onelaser.svg")).read()

def footer(r):
    ft = "".join(f'<li><a href="{r}signs/{t["slug"]}.html">{E(t["name"])}</a></li>' for t in TYPES)
    fs = "".join(f'<li><a href="{r}sectors/{s["slug"]}.html">{E(tcap(s["name"]))}</a></li>' for s in SECTORS)
    return f'''<footer class="dark">
  <div class="wrap">
    <div class="foot-grid">
      <div>
        <img src="{LOGO}" alt="Onesign &amp; Digital" width="142" height="30" style="height:30px;width:auto">
        <p>Family-run sign makers in Team Valley, Gateshead. Founded in Newcastle, trusted nationwide.</p>
        <img class="foot-accred" src="{ACCRED}" alt="Acclaim, IPAF, PASMA, Constructionline, CSCS and SCHQ accreditations" width="720" height="76" loading="lazy">
        <div class="family"><small>Sister companies</small><div class="family-logos"><a href="https://www.onelasercutting.com/" target="_blank" rel="noopener" aria-label="OneLaser, precision laser cutting">{ONELASER_SVG}</a><a href="https://www.onedesignstudios.com/" target="_blank" rel="noopener"><img src="https://www.onedesignstudios.com/brand/onedesign-logo-reversed.svg" alt="OneDesign Studios" width="1020" height="232" loading="lazy"></a></div></div>
      </div>
      <div><h4>Sign types</h4><ul>{ft}</ul></div>
      <div><h4>Sectors</h4><ul>{fs}</ul></div>
      <div><h4>Company</h4><ul>
        <li><a href="{r}index.html#work">Our work</a></li>
        <li><a href="{r}about.html">About us</a></li>
        <li><a href="{r}contact.html">Contact</a></li>
        <li><a href="https://www.instagram.com/onesignanddigital/" rel="noopener" target="_blank">Instagram</a></li>
        <li><a href="https://www.facebook.com/onesignanddigital/" rel="noopener" target="_blank">Facebook</a></li>
        <li><a href="https://www.tiktok.com/@onesignanddigital" rel="noopener" target="_blank">TikTok</a></li>
      </ul></div>
    </div>
    <div class="foot-bottom"><span>© 2026 Onesign &amp; Digital. All rights reserved.</span><span>D86 Princesway North, Team Valley, Gateshead NE11 0TU</span></div>
  </div>
</footer>
<div class="mob-cta" id="mobCta">
  <a class="pill pill-ghost" href="tel:+441914876767">call us</a>
  <a class="pill pill-solid" href="#contact">free mockup</a>
</div>'''

def cta(heading="let's make<br>it happen.", eyebrow="Free mockup"):
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
    <form class="mock lightc" id="mockForm" novalidate>
      <h3 class="hide-sent">tell us about your sign</h3>
      <div class="hide-sent" id="f-name-wrap"><label for="f-name">Your name</label><input id="f-name" name="name" autocomplete="name" required><div class="err">Add your name so we know who to ask for.</div></div>
      <div class="hide-sent"><label for="f-biz">Business</label><input id="f-biz" name="business" autocomplete="organization"></div>
      <div class="hide-sent" id="f-email-wrap"><label for="f-email">Email</label><input id="f-email" name="email" type="email" autocomplete="email" required><div class="err">Enter an email like name@company.co.uk.</div></div>
      <div class="hide-sent"><label for="f-tel">Phone</label><input id="f-tel" name="phone" type="tel" autocomplete="tel"></div>
      <div class="hide-sent"><label for="f-type">Sign type</label><select id="f-type" name="type">{opts}</select></div>
      <div class="hide-sent"><label for="f-post">Site postcode</label><input id="f-post" name="postcode" autocomplete="postal-code" placeholder="NE11 0TU"></div>
      <div class="hide-sent full"><label for="f-msg">What do you need?</label><textarea id="f-msg" name="message" placeholder="Sizes, wording, deadline, anything you know so far"></textarea></div>
      <label class="drop hide-sent full" id="drop" for="f-file"><input type="file" id="f-file" accept="image/*" multiple><span id="dropText">Drop a photo of your building here, or <u>browse</u>. It's what we draw your mockup on.</span></label>
      <button class="pill pill-solid hide-sent" type="submit">send my enquiry <span class="dot">→</span></button>
      <div class="form-done" role="status"><h3 style="font-size:28px;margin-bottom:8px">thanks, <span id="doneName">there</span>.</h3><p style="color:var(--fg-2)">Your enquiry is in. A member of our team will be in touch to talk through your mockup.</p></div>
    </form>
  </div>
</section>'''

BUSINESS = {
  "@context":"https://schema.org","@type":"LocalBusiness","@id":SITE_URL+"/#business",
  "name":"Onesign & Digital","url":SITE_URL+"/","logo":LOGO,"image":wix("hero",1200,630),
  "description":"Family-run sign makers in Gateshead, designing, manufacturing and installing signage since 2008.",
  "telephone":"+44 191 487 6767","email":"sales@onesignanddigital.com","foundingDate":"2008",
  "address":{"@type":"PostalAddress","streetAddress":"D86 Princesway North, Team Valley","addressLocality":"Gateshead","postalCode":"NE11 0TU","addressCountry":"GB"},
  "areaServed":["North East England","United Kingdom"],
  "openingHoursSpecification":[
    {"@type":"OpeningHoursSpecification","dayOfWeek":["Monday","Tuesday","Wednesday","Thursday"],"opens":"07:00","closes":"16:00"},
    {"@type":"OpeningHoursSpecification","dayOfWeek":"Friday","opens":"07:00","closes":"12:00"}],
  "sameAs":["https://www.instagram.com/onesignanddigital/","https://www.facebook.com/onesignanddigital/","https://www.tiktok.com/@onesignanddigital"],
  "parentOrganization":{"@type":"Organization","name":"One Group"}
}

def crumbs_ld(items):
    return {"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":[
        {"@type":"ListItem","position":i+1,"name":n,"item":SITE_URL+u} for i,(n,u) in enumerate(items)]}

def page(path, *, title, desc, canonical, body, ogimg, r, ld=(), bodyattrs=""):
    lds = "\n".join(f'<script type="application/ld+json">{json.dumps(x,ensure_ascii=False)}</script>' for x in [BUSINESS,*ld])
    doc = f'''<!doctype html>
<html lang="en-GB">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{E(title)}</title>
<meta name="description" content="{E(desc)}">
<link rel="canonical" href="{canonical}">
<meta property="og:type" content="website">
<meta property="og:site_name" content="Onesign &amp; Digital">
<meta property="og:title" content="{E(title)}">
<meta property="og:description" content="{E(desc)}">
<meta property="og:url" content="{canonical}">
<meta property="og:image" content="{ogimg}">
<meta property="og:locale" content="en_GB">
<meta name="twitter:card" content="summary_large_image">
<meta name="theme-color" content="#111415">
<link rel="icon" href="{r}assets/favicon.svg" type="image/svg+xml">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="preconnect" href="https://static.wixstatic.com">
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;500;600;700&family=Inter:wght@400;500;600&family=JetBrains+Mono:wght@400;500&display=swap">
<link rel="stylesheet" href="{r}assets/site.css">
{lds}
</head>
<body{bodyattrs}>
<a class="skip" href="#main">Skip to content</a>
{nav(r)}
<main id="main">
{body}
</main>
{footer(r)}
<script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.5/gsap.min.js" defer></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.5/ScrollTrigger.min.js" defer></script>
<script src="{r}assets/site.js" defer></script>
</body>
</html>
'''
    doc = doc.replace('content="{{R}}', 'content="'+SITE_URL+'/').replace("{{R}}", r)
    full = os.path.join(OUT, path)
    os.makedirs(os.path.dirname(full), exist_ok=True)
    open(full, "w").write(doc)
    return path

def phero(r, crumbs, h1, lede, img=None, ctas=True, plain=False):
    cr = "".join((f'<li><a href="{r}{u}">{E(n)}</a></li>' if u is not None else f'<li aria-current="page">{E(n)}</li>') for n,u in crumbs)
    bg = f'<div class="bgimg"><img src="{wix(img,2000,1200)}" srcset="{wix(img,1100,800)} 1100w, {wix(img,2000,1200)} 2000w" sizes="100vw" alt="{E(cap(img))}" fetchpriority="high" style="object-position:{pos(img)}"></div>' if img else ""
    btns = f'''<div class="hero-cta"><a class="pill pill-solid" href="#contact">get a free mockup <span class="dot">→</span></a><a class="pill pill-ghost" href="tel:+441914876767">call 0191 487 6767</a></div>''' if ctas else ""
    return f'''<section class="phero{' plain' if plain or not img else ''}">
  {bg}
  <div class="wrap phero-in">
    <nav aria-label="Breadcrumb"><ol class="crumbs">{cr}</ol></nav>
    <h1>{h1}</h1>
    <p class="lede">{lede}</p>
    {btns}
  </div>
</section>'''

def gallery(keys, r):
    if not keys:
        return '<div class="gallery-empty"><b>Project photos coming soon</b>We make these regularly. Ask us and we\'ll send you examples of recent jobs.</div>'
    figs = "".join(
        f'<figure data-full="{wix(k,1800,1800,"fit")}" data-cap="{E(cap(k))}"><img loading="lazy" alt="{E(cap(k))}" src="{wix(k,900,1200,"fit")}"><figcaption>{E(cap(k))}</figcaption></figure>'
        for k in keys)
    return f'<div class="gallery">{figs}</div>'

def link_card(href, img, title, text, icon=None):
    ico = f'<span class="ico"><img alt="" src="{WIX}{icon}~mv2.webp/v1/fit/w_120,h_120,q_90,enc_auto/icon.png" width="36" height="36"></span>' if icon else ""
    ph = (f'<img loading="lazy" alt="" src="{wix(img,720,450)}" style="object-position:{pos(img)}">') if img else ""
    return f'<a class="sector" href="{href}"><div class="ph">{ph}</div><div class="body{"" if icon else " noico"}">{ico}<div><h3>{E(title)}</h3><p>{E(text)}</p></div><span class="arr">→</span></div></a>'

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
        variants = f'''<section class="sec alt"><div class="wrap">
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
    body = f'''{phero(r, [("Home","index.html"),("Sign types","index.html#types"),(t["name"],None)], E(t["label"])+".", E(t["desc"]), t["hero"])}
<section class="sec"><div class="wrap">
  <div class="sec-head"><div><span class="eyebrow">Fitted by us</span><h2 class="h2 rv">real jobs, real photos.</h2></div><p class="lede rv">Tap any photo to see it full size.</p></div>
  {gallery(t["photos"], r)}
</div></section>
{variants}
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
  <div class="sec-head"><div><span class="eyebrow">Keep exploring</span><h2 class="h2 rv">other sign types.</h2></div></div>
  <div class="cards3">{related}</div>
</div></section>
{cta("let's price<br>your sign.", "Free mockup")}'''
    ld = [crumbs_ld([("Home","/"),("Sign types","/#types"),(t["name"],f"/signs/{t['slug']}")]),
          {"@context":"https://schema.org","@type":"Service","name":t["name"],"serviceType":t["name"],"description":t["meta"],
           "provider":{"@id":SITE_URL+"/#business"},"areaServed":"United Kingdom","url":url},
          {"@context":"https://schema.org","@type":"FAQPage","mainEntity":[{"@type":"Question","name":q,"acceptedAnswer":{"@type":"Answer","text":a}} for q,a in t["faq"]]}]
    return page(f"signs/{t['slug']}.html", title=f"{t['seo_title']} | Onesign & Digital", desc=t["meta"], canonical=url,
                body=body, ogimg=wix(t["hero"] or "st_cnc",1200,630), r=r, ld=ld, bodyattrs=f' data-signtype="{E(t["name"])}"')

# --------------------------------------------------------------- sector pages
def sector_page(s):
    r = "../"; TS = types_by_slug()
    url = f"{SITE_URL}/sectors/{s['slug']}"
    tcards = "".join(link_card(f'../signs/{x}.html', TS[x]["hero"], TS[x]["label"], TS[x]["desc"][:96].rsplit(" ",1)[0]+"…") for x in s["types"])
    points = "".join(f'<div class="point"><h3>{E(a)}</h3><p>{E(b)}</p></div>' for a,b in s["points"])
    others = "".join(f'<a href="{o["slug"]}.html">{E(o["name"])}</a>' for o in SECTORS if o["slug"]!=s["slug"])
    body = f'''{phero(r, [("Home","index.html"),("Sectors","index.html#sectors"),(tcap(s["name"]),None)], E(s["name"])+" signage.", E(s["intro"]), s["img"])}
<section class="sec"><div class="wrap">
  <div class="points">{points}</div>
</div></section>
<section class="sec alt"><div class="wrap">
  <div class="sec-head"><div><span class="eyebrow">What we make</span><h2 class="h2 rv">signs we make for {E(s["name"])}.</h2></div></div>
  <div class="cards3">{tcards}</div>
</div></section>
<section class="sec"><div class="wrap">
  <div class="sec-head"><div><span class="eyebrow">Fitted by us</span><h2 class="h2 rv">recent {E(s["name"])} work.</h2></div><p class="lede rv">Tap any photo to see it full size.</p></div>
  {gallery(s["gallery"], r)}
</div></section>
<section class="sec alt tight"><div class="wrap">
  <span class="eyebrow" style="margin-bottom:16px;display:flex">Other sectors</span>
  <div class="chips-row">{others}</div>
</div></section>
{cta()}'''
    ld = [crumbs_ld([("Home","/"),("Sectors","/#sectors"),(tcap(s["name"]),f"/sectors/{s['slug']}")])]
    return page(f"sectors/{s['slug']}.html", title=f"{s['title']} | Onesign & Digital", desc=s["intro"][:155].rsplit(" ",1)[0]+".",
                canonical=url, body=body, ogimg=wix(s["img"],1200,630), r=r, ld=ld)

# --------------------------------------------------------------- about
def about_page():
    r = ""
    body = f'''{phero(r, [("Home","index.html"),("About us",None)], "family-run sign makers since 2008.", "Founded in Newcastle and trusted nationwide. We take great pride not only in the work we do, but in how we do it.", "install2")}
<section class="sec"><div class="wrap two">
  <div class="prose">
    <span class="eyebrow" style="margin-bottom:18px;display:flex">Our story</span>
    <h2>one roof, every step.</h2>
    <p>Onesign has been family-run since 2008 and brings 50 years of sign and print experience under one roof. From our North East roots in Team Valley, Gateshead, we now make and fit signs for businesses across the UK.</p>
    <p>Everything is managed in-house. Our own team surveys, designs, manufactures and installs every job, so you deal with the same people from first call to final fixing, and nothing gets lost in a handover.</p>
    <p>We use modern equipment to make durable, high-quality signs that are safe for demanding places like schools and hospitals, and we keep investing in new technology and better ways of working as our clients' needs change.</p>
  </div>
  <div>
    <div class="figures">
      <div class="fig"><b>2008</b><span>Family-run since day one</span></div>
      <div class="fig"><b><span data-count="50">50</span><sup>yrs</sup></b><span>Combined trade experience</span></div>
      <div class="fig"><b><span data-count="100">100</span><sup>%</sup></b><span>Made and fitted in-house</span></div>
      <div class="fig"><b>5.0<sup>★</sup></b><span>From 71 Google reviews</span></div>
    </div>
    <div class="accred"><small>Accredited</small><img src="{ACCRED}" alt="Acclaim, IPAF, PASMA, Constructionline, CSCS and SCHQ accreditations" width="720" height="76"></div>
  </div>
</div></section>
<section class="sec alt"><div class="wrap">
  <div class="sec-head"><div><span class="eyebrow">Inside the workshop</span><h2 class="h2 rv">made in Team Valley.</h2></div><p class="lede rv">Routing, folding, welding, printing and wiring all happen in our own Gateshead workshop.</p></div>
  {gallery(["st_cnc","st_weld","weld","st_bench","install","install2"], r)}
</div></section>
<section class="sec" id="process"><div class="wrap">
  <div class="sec-head"><div><span class="eyebrow">How we work</span><h2 class="h2 rv">one team, start to finish.</h2></div></div>
  {MINI_STEPS}
</div></section>
<section class="sec alt"><div class="wrap">
  <div class="sec-head"><div><span class="eyebrow">Sister companies</span><h2 class="h2 rv">part of a bigger family.</h2></div></div>
  <div class="fam-cards">
    <a class="fam-card" href="https://www.onelasercutting.com/" target="_blank" rel="noopener">{ONELASER_SVG}<p>Precision laser cutting for metal sheet and profiles, from one-offs to production runs.</p><span>onelasercutting.com →</span></a>
    <a class="fam-card" href="https://www.onedesignstudios.com/" target="_blank" rel="noopener"><img src="https://www.onedesignstudios.com/brand/onedesign-logo-reversed.svg" alt="OneDesign Studios" width="1020" height="232"><p>A branding and creative studio in the North East: identities, print and digital design.</p><span>onedesignstudios.com →</span></a>
  </div>
</div></section>
{cta()}'''
    return page("about.html", title="About Onesign & Digital | Family-Run Sign Makers, Gateshead",
                desc="Family-run since 2008, Onesign & Digital designs, manufactures and installs signage from its Team Valley workshop in Gateshead.",
                canonical=SITE_URL+"/about", body=body, ogimg=wix("install2",1200,630), r=r,
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
  <div class="find">
    <div class="point"><h3>visit us</h3><p>D86 Princesway North<br>Team Valley, Gateshead<br>NE11 0TU</p><p style="margin-top:14px"><a href="https://www.google.com/maps/search/?api=1&amp;query=Onesign+%26+Digital+Princesway+North+Gateshead+NE11+0TU" target="_blank" rel="noopener">Open in Google Maps →</a></p></div>
    <div class="point"><h3>opening times</h3><p>Monday to Thursday: 07:00–16:00<br>Friday: 07:00–12:00<br>Saturday and Sunday: closed</p></div>
    <div class="point"><h3>call or email</h3><p>0191 487 6767<br>sales@onesignanddigital.com</p></div>
  </div>
</div></section>'''
    return page("contact.html", title="Contact Onesign & Digital | Sign Makers in Gateshead",
                desc="Get a free sign mockup and quote from Onesign & Digital, Team Valley, Gateshead. Call 0191 487 6767 or send us a photo of your building.",
                canonical=SITE_URL+"/contact", body=body, ogimg=wix("hero",1200,630), r=r,
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
            photos=[dict(full=wix(k,1600,1100,"fit"), bg=wix(k,80,60), thumb=wix(k,140,100), cap=cap(k)) for k in t["photos"][:6]]))
    tabs = "".join(f'<li><button role="tab" id="tab-{t["slug"]}" aria-selected="{"true" if i==0 else "false"}" aria-controls="typePanel" tabindex="{0 if i==0 else -1}"><span class="n">{i+1:02d}</span><span class="t">{E(t["label"])}</span><span class="arr">→</span></button></li>' for i,t in enumerate(TYPES))
    t0 = TYPES[0]
    spec0 = "".join(f"<dt>{E(a)}</dt><dd>{E(b)}</dd>" for a,b in t0["spec"])
    ideal0 = "".join(f'<span class="tag">{E(x)}</span>' for x in t0["ideal"])
    logos = "".join(f'<img src="{WIX}{lid}~mv2.webp/v1/fit/w_300,h_120,q_90,enc_auto/logo.png" alt="{"Client logo" if i < len(CLIENT_LOGOS) else ""}"{"" if i < len(CLIENT_LOGOS) else " aria-hidden=\"true\""} draggable="false" loading="lazy" width="150" height="46">' for i,lid in enumerate(CLIENT_LOGOS+CLIENT_LOGOS))
    def reel(keys):
        out=""
        for i,k in enumerate(keys+keys):
            dup = i>=len(keys)
            out += f'<figure{" aria-hidden=\"true\"" if dup else ""}><img loading="lazy" alt="{"" if dup else E(cap(k))}" src="{wix(k,760,570)}" style="object-position:{pos(k)}"><figcaption>{E(cap(k))}</figcaption></figure>'
        return out
    tiles = ""
    for i,p in enumerate(PROJECTS):
        big = i==0
        inner = f'<img loading="lazy" alt="{E(p["name"])} sign by Onesign" src="{wix(p["k"],1200 if big else 800,1200 if big else 800)}" style="object-position:{pos(p["k"])}"><div class="tile-info"><div><small>{E(p["label"])}</small><h3>{E(p["name"])}</h3></div>{"<span class=\"go\" aria-hidden=\"true\">→</span>" if p["url"] else ""}</div>'
        tiles += (f'<a class="tile" href="{SITE_URL}/{p["url"]}" target="_blank" rel="noopener">{inner}</a>' if p["url"] else f'<div class="tile">{inner}</div>')
    sectors = "".join(link_card(f'sectors/{s["slug"]}.html', s["img"], s["name"], s["blurb"], s["icon"]) for s in SECTORS)
    body = f'''<section class="hero" id="top">
  <div class="hero-media" id="heroMedia"><img id="heroImg" src="{wix("hero",2200,1500)}" srcset="{wix("hero",1200,900)} 1200w, {wix("hero",2200,1500)} 2200w" sizes="100vw" alt="Illuminated Newcastle University building sign by Onesign" fetchpriority="high"></div>
  <div class="wrap hero-in">
    <div>
      <span class="eyebrow">North East sign makers · est. 2008</span>
      <h1 id="heroTitle">
        <span class="line"><span>crafting</span></span>
        <span class="line"><span id="extrude">statements,</span></span>
        <span class="line"><span>onesign at a time.</span></span>
      </h1>
      <p class="hero-sub">Designed, built and installed by our own team, from a single shop sign to a full hospital wayfinding scheme.</p>
      <div class="hero-cta">
        <a class="pill pill-solid" href="#contact">get a free mockup <span class="dot">→</span></a>
        <a class="pill pill-ghost" href="#types">explore sign types</a>
      </div>
    </div>
    <aside class="hero-card">
      <div class="g-row"><div class="g-badge">G</div><div><b>5.0</b> <span class="stars">★★★★★</span><small>71 Google reviews</small></div></div>
      <div class="meta">survey · design · manufacture · install<br>all under one roof in Team Valley</div>
    </aside>
  </div>
</section>
<div class="trusted">
  <p>Trusted by the North East and beyond</p>
  <div class="marquee" id="marqueeBox"><div class="marquee-track">{logos}</div></div>
</div>
<section class="intro">
  <div class="wrap intro-grid">
    <div>
      <span class="eyebrow">Family-run since 2008</span>
      <h2 class="rv" style="margin-top:18px">founded in Newcastle,<br>trusted nationwide.</h2>
      <p class="lede rv">Onesign brings 50 years of sign and print experience under one roof. Every job is surveyed, designed, made and fitted by our own people, so you deal with one team from first call to final fixing.</p>
    </div>
    <div class="rv">
      <div class="figures">
        <div class="fig"><b>2008</b><span>Family-run since day one</span></div>
        <div class="fig"><b><span data-count="50">50</span><sup>yrs</sup></b><span>Combined trade experience</span></div>
        <div class="fig"><b><span data-count="100">100</span><sup>%</sup></b><span>Made and fitted in-house</span></div>
        <div class="fig"><b>5.0<sup>★</sup></b><span>From 71 Google reviews</span></div>
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
          <span class="cap" id="typeCap">{E(cap(t0["photos"][0]))}</span>
          <div class="thumbs" id="typeThumbs"></div>
        </div>
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
      <article class="step"><span class="step-n">01</span><div class="step-img"><img loading="lazy" src="{wix("install2",1000,1000,"fit")}" style="object-position:22% 50%" alt="Onesign fitter in a branded hard hat surveying an NHS building"></div><h3>concept &amp; survey</h3><p>We visit, measure up and talk through the options that suit your building, budget and any planning or building-regs constraints.</p></article>
      <article class="step"><span class="step-n">02</span><div class="step-img"><img loading="lazy" src="{wix("sitePlan",1000,1000,"fit")}" alt="Design visual of a site plan for a wayfinding scheme"></div><h3>design</h3><p>Our designers apply your branding and show you scaled visuals on your actual premises, so you sign off on exactly what you'll get.</p></article>
      <article class="step"><span class="step-n">03</span><div class="step-img"><img loading="lazy" src="{wix("weld",1000,1000,"fit")}" alt="Fabricator welding a sign frame in the Onesign workshop"></div><h3>manufacture</h3><p>Routed, folded, welded, printed and wired in our Team Valley workshop on our own CNC, laser and large-format kit.</p></article>
      <article class="step"><span class="step-n">04</span><div class="step-img"><img loading="lazy" src="{wix("install",1000,1000,"fit")}" alt="Onesign installers fitting a high-level Aldi sign"></div><h3>install</h3><p>Our own British fitting teams install with care, from a single fascia to high-level work on live hospital and campus sites.</p></article>
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
      <a class="pill pill-ghost" href="{SITE_URL}/our-work" target="_blank" rel="noopener">all projects <span class="dot">→</span></a>
    </div>
    <div class="bento">{tiles}</div>
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
{cta()}'''
    return page("index.html", title="Onesign & Digital | Sign Makers in Newcastle, Gateshead & the North East",
                desc="Family-run North East sign makers since 2008. 3D letters, backlit panels, building signs, wayfinding, LED neon and large format print, designed, made and installed in-house in Gateshead.",
                canonical=SITE_URL+"/", body=body, ogimg=wix("hero",1200,630), r=r)

# --------------------------------------------------------------- extras
def extras(pages):
    urls = []
    for p in pages:
        u = "/" if p=="index.html" else "/" + p[:-5]
        urls.append(u)
    sm = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + "".join(
        f"  <url><loc>{SITE_URL}{u}</loc></url>\n" for u in urls if u!="/404") + "</urlset>\n"
    open(os.path.join(OUT,"sitemap.xml"),"w").write(sm)
    open(os.path.join(OUT,"robots.txt"),"w").write(f"User-agent: *\nAllow: /\n\nSitemap: {SITE_URL}/sitemap.xml\n")
    # old Wix URLs -> new pages (for launch)
    R = {"/about-us":"/about","/services":"/#types","/sectors":"/#sectors",
         "/service/exterior":"/signs/building-signs","/service/neon":"/signs/neon-led-neon","/service/totems":"/signs/totems-monoliths",
         "/service/wayfinding":"/signs/wayfinding","/service/vehicle-graphics-decals":"/signs/vehicle-graphics",
         "/service/large-format-digital-print":"/signs/digital-large-format-print","/service/hoarding":"/signs/digital-large-format-print",
         "/service/promotional":"/signs/digital-large-format-print","/service/graphics":"/signs/vinyl-wall-graphics",
         "/service/interior":"/signs/3d-letters","/service/informative":"/signs/wayfinding","/service/health-saftey-signs":"/sectors/health-safety",
         "/health-saftey-signs":"/sectors/health-safety","/healthcare":"/sectors/healthcare","/educational":"/sectors/education",
         "/construction":"/sectors/construction","/commercial":"/sectors/commercial","/retail":"/sectors/retail",
         "/leisure":"/sectors/hospitality-leisure","/hair-and-beauty":"/sectors/hair-beauty"}
    vercel = {"cleanUrls":True,"trailingSlash":False,
              "redirects":[{"source":a,"destination":b,"permanent":True} for a,b in R.items()],
              "headers":[{"source":"/assets/(.*)","headers":[{"key":"Cache-Control","value":"public, max-age=31536000, immutable"}]},
                         {"source":"/(.*)","has":[{"type":"host","value":"(?<sub>.*)\\.vercel\\.app"}],"headers":[{"key":"X-Robots-Tag","value":"noindex, nofollow"}]}]}
    open(os.path.join(OUT,"vercel.json"),"w").write(json.dumps(vercel,indent=2))
    fav = '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64"><rect width="64" height="64" rx="14" fill="#111415"/><circle cx="32" cy="32" r="20" fill="none" stroke="#fff" stroke-width="7"/><path d="M28 22h8v22h-8z" fill="#517d90"/></svg>'
    open(os.path.join(OUT,"assets","favicon.svg"),"w").write(fav)

def not_found():
    body = f'''{phero("", [("Home","index.html"),("Page not found",None)], "this page has moved.", "We've rebuilt our website. Try one of these instead, or call us on 0191 487 6767.", None, ctas=False, plain=True)}
<section class="sec"><div class="wrap"><div class="chips-row">{"".join(f'<a href="/signs/{t["slug"]}">{E(t["label"])}</a>' for t in TYPES)}</div></div></section>'''
    return page("404.html", title="Page not found | Onesign & Digital", desc="This page has moved.", canonical=SITE_URL+"/404", body=body, ogimg=wix("hero",1200,630), r="/")

# --------------------------------------------------------------- css
def build_css():
    css = open(os.path.join(SRC,"base.css")).read()
    css = css.replace(";text-transform:lowercase","").replace("text-transform:lowercase;","")
    css += open(os.path.join(SRC,"extra.css")).read()
    open(os.path.join(OUT,"assets","site.css"),"w").write(css)

if __name__ == "__main__":
    os.makedirs(os.path.join(OUT,"assets"), exist_ok=True)
    build_css()
    pages = [home_page(), about_page(), contact_page()]
    pages += [type_page(t) for t in TYPES]
    pages += [sector_page(s) for s in SECTORS]
    pages.append(not_found())
    extras(pages)
    print(len(pages), "pages")

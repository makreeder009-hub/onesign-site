import re
# -*- coding: utf-8 -*-
"""New page families: index pages, our work + case studies, areas, guides, nationwide, privacy.
Run this file to build the whole site into ../site."""
import hashlib, json, os, shutil
import build as B
from build import (fit, fit_desc, E, pic, wix, og, cap, pos, page, phero, gallery, link_card, cta, crumbs_ld, case_card, guide_card,
                   area_chips, tcap, map_block, LOC, all_type_cards, TYPES, SECTORS, CASES, AREAS, GUIDES, REVIEWS, SITE_URL, MINI_STEPS, CASE)

TS = {t["slug"]: t for t in TYPES}
SS = {s["slug"]: s for s in SECTORS}
def short(t, n=96): return t[:n].rsplit(" ", 1)[0] + "…"
def type_card(slug, r): t = TS[slug]; return link_card(f'{r}signs/{slug}.html', t["hero"], t["label"], short(t["desc"]))
def faq_html(faq): return "".join(f"<details><summary>{E(q)}</summary><p>{E(a)}</p></details>" for q, a in faq)
def faq_ld(faq): return {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [
    {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in faq]}
def head(eyebrow, h2, lede="", extra=""):
    return f'<div class="sec-head"><div><span class="eyebrow">{eyebrow}</span><h2 class="h2 rv">{h2}</h2></div>{f"<p class=lede>{lede}</p>" if lede else ""}{extra}</div>'

# ------------------------------------------------------------------ index pages
def signs_index():
    r = "../"
    cards = "".join(type_card(t["slug"], r) for t in TYPES)
    body = f'''{phero(r, [("Home","index.html"),("Sign types",None)], "every kind of sign.", "Fifteen sign types, all designed, made and installed by our own team in Team Valley, Gateshead. Pick one to see real jobs, materials and specifications.", "n_thatype", kicker="Sign types")}
<section class="sec"><div class="wrap">
  {head("Made in-house", "choose a sign type.", "Not sure which you need? Send us a photo of your building and we will mock up the options for free.")}
  <div class="cards3">{cards}</div>
</div></section>
<section class="sec alt"><div class="wrap">
  {head("Help choosing", "guides from the factory floor.")}
  <div class="gcards">{"".join(guide_card(g, r) for g in GUIDES)}</div>
</div></section>
{cta()}'''
    ld = [crumbs_ld([("Home", "/"), ("Sign types", "/signs")]),
          {"@context": "https://schema.org", "@type": "ItemList", "itemListElement": [
              {"@type": "ListItem", "position": i + 1, "name": t["name"], "url": f"{SITE_URL}/signs/{t['slug']}"} for i, t in enumerate(TYPES)]}]
    return page("signs/index.html", title="Sign Types: 3D Letters, Illuminated Signs & More | Onesign",
                desc=f"All {len(TYPES)} types of sign we make in Gateshead: 3D letters, backlit panels, light boxes, LED neon, wayfinding, totems, vinyl, print and van graphics.",
                canonical=SITE_URL + "/signs", body=body, ogimg=og("n_thatype"), r=r, ld=ld)

def sectors_index():
    r = "../"
    cards = "".join(link_card(f'{s["slug"]}.html', s["img"], s["name"], s["blurb"], s["slug"]) for s in SECTORS)
    body = f'''{phero(r, [("Home","index.html"),("Sectors",None)], "signs for your sector.", "From live hospital wards to construction hoardings, we know the rules and realities of each sector we work in.", "hc_cdc", kicker="Sectors")}
<section class="sec"><div class="wrap">
  {head("Who we work for", "nine sectors, one team.")}
  <div class="sector-grid">{cards}</div>
</div></section>
<section class="sec alt"><div class="wrap">
  {head("Case studies", "see it in practice.", extra='<a class="pill pill-ghost" href="../work/index.html">all our work <span class="dot">→</span></a>')}
  <div class="ccards">{"".join(case_card(c, r) for c in CASES[:3])}</div>
</div></section>
{cta()}'''
    return page("sectors/index.html", title="Signage by Sector: Healthcare, Retail & More | Onesign",
                desc="Signage for healthcare, education, construction, offices, retail, hospitality, salons and transport, made in Gateshead and installed by Onesign.",
                canonical=SITE_URL + "/sectors", body=body, ogimg=og("hc_cdc"), r=r, ld=[crumbs_ld([("Home", "/"), ("Sectors", "/sectors")])])

# ------------------------------------------------------------------ our work
def work_index():
    r = "../"
    used = [s for s in SECTORS if any(c["sector"] == s["slug"] for c in CASES)]
    filters = '<button class="on" data-f="all">all</button>' + "".join(f'<button data-f="{s["slug"]}">{E(s["name"])}</button>' for s in used)
    cards = "".join(f'<div class="cc-wrap" data-sector="{c["sector"]}">{case_card(c, r)}</div>' for c in CASES)
    body = f'''{phero(r, [("Home","index.html"),("Our work",None)], "our work.", "Case studies from across the North East and beyond: what the client needed, what we made and how it turned out.", "vertu", kicker="Case studies")}
<section class="sec"><div class="wrap">
  <div class="filters" id="filters" role="group" aria-label="Filter case studies by sector">{filters}</div>
  <div class="ccards" id="caseGrid">{cards}</div>
</div></section>
<section class="rating"><div class="wrap rating-in">
  <div class="rt-score"><b>{REVIEWS["score"]}</b><div><span class="stars" aria-hidden="true">★★★★★</span><small>from {REVIEWS["count"]} Google reviews</small></div></div>
  <p>Want to know what we are like to work with? Our customers say it better than we can.</p>
  <a class="pill pill-ghost" href="{REVIEWS["url"]}" target="_blank" rel="noopener">read our reviews <span class="dot">→</span></a>
</div></section>
{cta("got a project<br>like these?")}'''
    ld = [crumbs_ld([("Home", "/"), ("Our work", "/work")]),
          {"@context": "https://schema.org", "@type": "ItemList", "itemListElement": [
              {"@type": "ListItem", "position": i + 1, "name": c["name"], "url": f"{SITE_URL}/work/{c['slug']}"} for i, c in enumerate(CASES)]}]
    return page("work/index.html", title="Signage Case Studies & Recent Projects | Onesign & Digital",
                desc="Signage case studies from Onesign: Newcastle University, NHS, Rolls-Royce, Vertu Motors Arena, Aldi and more. See what we made and how.",
                canonical=SITE_URL + "/work", body=body, ogimg=og("vertu"), r=r, ld=ld)

def case_page(c):
    r = "../"; url = f"{SITE_URL}/work/{c['slug']}"; sec = SS[c["sector"]]
    made = "".join(f'<li><span class="mk-n">{i+1:02d}</span><div><h3>{E(a)}</h3><p>{E(b)}</p></div></li>' for i, (a, b) in enumerate(c["made"]))
    facts = f'<dt>Client</dt><dd>{E(c["name"])}</dd>' + (f'<dt>Location</dt><dd>{E(c["where"])}</dd>' if c["where"] else "") + \
            f'<dt>Sector</dt><dd><a href="../sectors/{sec["slug"]}.html">{E(tcap(sec["name"]))}</a></dd>' + \
            (('<dt>Sign types</dt><dd>' + ", ".join(f'<a href="../signs/{t}.html">{E(TS[t]["label"])}</a>' for t in c["types"]) + '</dd>') if c["types"] else '') + \
            '<dt>Delivered</dt><dd>Survey, design, manufacture and installation</dd>'
    making = f'''<section class="sec alt"><div class="wrap">
  {head("In the factory", "how it was made.", "Design, routing, cutting, welding, spraying, assembly and fitting, all by our own team.")}
  {gallery(c["making"], r, captions=False)}
</div></section>''' if c["making"] else ""
    i = CASES.index(c); nxt = CASES[(i + 1) % len(CASES)]; prv = CASES[i - 1]
    meta = '<div class="ph-meta">' + (f'<span>{E(c["where"])}</span>' if c["where"] else "") + f'<span>{E(tcap(sec["name"]))}</span><span>{E(c["label"])}</span></div>'
    body = f'''{phero(r, [("Home","index.html"),("Our work","work/index.html"),(c["name"],None)], E(c["name"])+".", E(c["lede"]), c["hero"], kicker="Case study", meta=meta)}
<section class="sec"><div class="wrap case-top">
  <div class="prose">
    <span class="eyebrow" style="margin-bottom:18px;display:flex">The brief</span>
    <h2>what they needed.</h2>
    <p class="big">{E(c["brief"])}</p>
  </div>
  <aside class="facts"><dl>{facts}</dl></aside>
</div></section>
<section class="sec alt"><div class="wrap">
  {head("What we made", "the signage.")}
  <ol class="made">{made}</ol>
</div></section>
<section class="sec"><div class="wrap">
  {head("Photos", "the finished job.", "Tap any photo to see it full size.")}
  {gallery(c["photos"], r)}
  <blockquote class="result"><span class="eyebrow">The result</span><p>{E(c["result"])}</p></blockquote>
</div></section>
{making}
<section class="sec{"" if c["making"] else " alt"}"><div class="wrap">
  {(head("Used on this project", "the sign types.") + '<div class="cards3">' + "".join(type_card(t, r) for t in c["types"][:3]) + '</div>') if c["types"] else ""}
  <nav class="case-nav" aria-label="More case studies"><a href="{prv["slug"]}.html"><small>← previous</small><b>{E(prv["name"])}</b></a><a href="index.html" class="all">all case studies</a><a href="{nxt["slug"]}.html"><small>next →</small><b>{E(nxt["name"])}</b></a></nav>
</div></section>
{cta("want a result<br>like this?")}'''
    ld = [crumbs_ld([("Home", "/"), ("Our work", "/work"), (c["name"], f"/work/{c['slug']}")]),
          {"@context": "https://schema.org", "@type": "Article", "headline": f"{c['name']}: {c['label']}", "description": c["lede"], "image": og(c["hero"]),
           "author": {"@id": SITE_URL + "/#business"}, "publisher": {"@id": SITE_URL + "/#business"}, "mainEntityOfPage": url}]
    where = f" in {c['where']}" if c["where"] else ""
    town = (LOC.get(c["slug"]) or [None])[0] or (c["where"] or "").split(",")[0] or None
    lab = c["label"][:1].upper() + c["label"][1:]
    title = fit(f"{c['name']}, {town}: {lab} | Onesign" if town else None,
                f"{c['name']}: {lab} | Onesign",
                f"{c['name']} Signage, {town} | Onesign" if town else None,
                f"{c['name']} Signage | Onesign", f"{c['name']} | Onesign")
    led = c["lede"].strip(); led = led if led.endswith((".", "!", "?")) else led + "."
    desc = c.get("meta") or fit_desc(f"{led} A signage case study{where} by Onesign & Digital.",
                    f"{led} Designed, made and installed{where} by Onesign & Digital, Gateshead.",
                    f"{led} Made and fitted by Onesign & Digital.",
                    f"{led} {c['name']}{where}: designed, made and installed by Onesign & Digital, North East sign makers since 2008.",
                    f"{led} Signage for {c['name']}{where}, designed, made in our Gateshead factory and installed by Onesign & Digital.", led)
    return page(f"work/{c['slug']}.html", title=title,
                desc=desc, canonical=url, body=body, ogimg=og(c["hero"]), r=r, ld=ld, ogtype="article")

# ------------------------------------------------------------------ areas
KEY_TYPES = ["3d-letters", "backlit-panels", "high-level-signs", "projecting-signs", "neon-led-neon", "vinyl-wall-graphics"]
def area_page(a):
    r = "../"; url = f"{SITE_URL}/areas/{a['slug']}"
    picked = [s for s, _ in a["proof"]] + [s for s, v in LOC.items() if v[1] == a["slug"] and s in CASE and s not in [x for x, _ in a["proof"]]]
    proof = "".join(case_card(CASE[s], r) for s in picked[:9])
    a = dict(a, proof=[(s, "") for s in picked], photos=list(dict.fromkeys(list(a["photos"]) + [CASE[s]["hero"] for s in picked]))[:12])
    proof_html = f'''<section class="sec alt"><div class="wrap">
  {head("Local work", f"our work in {E(a['short'])}.")}
  <div class="ccards">{proof}</div>
  <p class="also">{E(a["also"])}</p>
  <div class="map-head"><span class="eyebrow">On the map</span><a class="type-more" href="index.html#map">see every job we've fitted <span aria-hidden="true">→</span></a></div>
  {map_block(r, a["slug"], "area", title=f"Signs we have fitted in {a['short']}")}
</div></section>''' if a["proof"] else f'''<section class="sec alt tight"><div class="wrap"><p class="also solo">{E(a["also"])}</p></div></section>'''
    rest = "".join(f'<a href="../signs/{t["slug"]}.html">{E(t["label"])}</a>' for t in TYPES if t["slug"] not in KEY_TYPES)
    places = "".join(f"<span>{E(p)}</span>" for p in a["places"])
    side = f'''<aside class="area-card">
      <h3>free site survey in {E(a["short"])}</h3>
      <ul><li>We measure up and check fixings, power and access</li><li>You get a scaled mockup on a photo of your building</li><li>One price for design, manufacture and installation</li></ul>
      <a class="pill pill-solid" href="#contact">book a survey <span class="dot">→</span></a>
      <a class="tel" href="tel:+441914876767">or call 0191 487 6767</a>
    </aside>'''
    body = f'''{phero(r, [("Home","index.html"),("Areas","areas/index.html"),(a["short"],None)], f"Sign makers in {E(a['name'])}.", E(a["lede"]), a["hero"], kicker="Areas we cover")}
<section class="sec"><div class="wrap two area-intro">
  <div class="prose"><span class="eyebrow" style="margin-bottom:18px;display:flex">Local sign company</span><h2>Your sign makers for {E(a["short"])}.</h2>{"".join(f"<p>{E(p)}</p>" for p in a["intro"])}
    <div class="places"><small>Areas we cover</small><div>{places}</div></div></div>
  {side}
</div></section>
{proof_html}
<section class="sec"><div class="wrap">
  {head("What we make", f"every sign type, for {E(a['short'])}.", "All fifteen are designed, made and fitted by our own team. Photos are from jobs near you where we have them.")}
  {all_type_cards(r, [CASE[s] for s in picked if s in CASE])}
</div></section>
<section class="sec alt"><div class="wrap">
  {head("Our signs", "a few we have made.", "Tap any photo to see it full size.")}
  {gallery(a["photos"], r)}
</div></section>
<section class="sec"><div class="wrap two">
  <div class="planbox"><span class="eyebrow">Planning in {E(a["short"])}</span><h3>will your sign need consent?</h3><p>{E(a["planning"])}</p><a class="type-more" href="../guides/sign-planning-permission.html">read our planning guide <span aria-hidden="true">→</span></a></div>
  <div><span class="eyebrow" style="margin-bottom:8px;display:flex">Questions</span><div class="faq">{faq_html(a["faq"])}</div></div>
</div></section>
<section class="sec alt tight"><div class="wrap">
  <span class="eyebrow" style="margin-bottom:16px;display:flex">Other areas</span>
  <div class="chips-row">{area_chips(r, a["slug"])}</div>
</div></section>
{cta(f"need a sign<br>in {E(a['short'])}?")}'''
    ld = [crumbs_ld([("Home", "/"), ("Areas", "/areas"), (a["short"], f"/areas/{a['slug']}")]),
          {"@context": "https://schema.org", "@type": "Service", "name": f"Sign makers in {a['name']}", "serviceType": "Sign manufacture and installation",
           "provider": {"@id": SITE_URL + "/#business"}, "areaServed": {"@type": "AdministrativeArea", "name": a["name"]}, "url": url}, faq_ld(a["faq"])]
    return page(f"areas/{a['slug']}.html", title=fit(f"Sign Makers {a['short']} | Shop & Illuminated Signs | Onesign", f"Sign Makers {a['short']} | Shop & Building Signs", f"Sign Makers in {a['short']} | Onesign"),
                desc=fit_desc(f"{a['lede']} Free site survey and mockup. Call 0191 487 6767.", f"{a['lede']} Free survey and mockup.", a['lede']), canonical=url, body=body, ogimg=og(a["hero"]), r=r, ld=ld)

def areas_index():
    r = "../"
    cards = "".join(link_card(f'{a["slug"]}.html', a["hero"], f"Sign makers in {a['short']}", a["lede"]) for a in AREAS)
    cards += link_card("../nationwide-signage.html", "rolls", "Nationwide rollouts", "Multi-site signage programmes made in one factory and fitted across the UK.")
    body = f'''{phero(r, [("Home","index.html"),("Areas",None)], "areas we cover.", "Made in Team Valley, Gateshead. Fitted across the North East by our own installers, and anywhere in the UK for larger projects.", "hero", kicker="Where we work")}
<section class="sec" id="map"><div class="wrap">
  {head("Job map", "signs we've fitted.", "Every pin is a finished job. Tap one to see the photos and what we made. Our workshop is the black pin in Team Valley.")}
  {map_block(r, None, "big")}
</div></section>
<section class="sec alt"><div class="wrap">
  {head("North East", "local to you.")}
  <div class="cards3">{cards}</div>
</div></section>
{cta()}'''
    return page("areas/index.html", title="Areas We Cover: Sign Makers in the North East | Onesign",
                desc="Onesign makes signs in Gateshead and installs across Newcastle, Sunderland, Durham, South Tyneside, Northumberland and the whole UK.",
                canonical=SITE_URL + "/areas", body=body, ogimg=og("hero"), r=r, ld=[crumbs_ld([("Home", "/"), ("Areas", "/areas")])])

# ------------------------------------------------------------------ guides
def slug(s): return "".join(ch if ch.isalnum() else "-" for ch in s.lower()).strip("-").replace("--", "-")
def guide_page(g):
    r = "../"; url = f"{SITE_URL}/guides/{g['slug']}"
    toc = "".join(f'<li><a href="#{slug(h)}">{E(h)}</a></li>' for h, _ in g["sections"]) + '<li><a href="#questions">common questions</a></li>'
    def figs(s):
        return re.sub(r"\{FIG (\w+)\|([^}]*)\}", lambda m: f'<figure class="gfig"><img loading="lazy" src="{wix(m.group(1),1200,800)}" alt="{E(m.group(2))}" style="object-position:{pos(m.group(1))}"><figcaption>{E(m.group(2))}</figcaption></figure>', s)
    secs = "".join(f'<section id="{slug(h)}"><h2>{E(h)}</h2>{figs(html.replace("{R}", r))}</section>' for h, html in g["sections"])
    others = "".join(guide_card(x, r) for x in GUIDES if x["slug"] != g["slug"])
    d = g["updated"]
    body = f'''{phero(r, [("Home","index.html"),("Guides","guides/index.html"),(g["kicker"],None)], f'<span class="lg">{E(g["h1"])}</span>', E(g["lede"]), g["hero"], kicker=g["kicker"], ctas=False, meta=f'<div class="ph-meta"><span>By the Onesign team</span><span>Updated <time datetime="{d}">November 2026</time></span></div>')}
<section class="sec"><div class="wrap article">
  <aside class="toc"><small>In this guide</small><ol>{toc}</ol><a class="pill pill-solid" href="#contact">get a free mockup <span class="dot">→</span></a></aside>
  <article class="guide">{secs}
    <section id="questions"><h2>common questions</h2><div class="faq">{faq_html(g["faq"])}</div></section>
  </article>
</div></section>
<section class="sec alt"><div class="wrap">
  {head("Keep reading", "more guides.")}
  <div class="gcards">{others}</div>
</div></section>
{cta("ready for<br>a real quote?")}'''
    ld = [crumbs_ld([("Home", "/"), ("Guides", "/guides"), (g["kicker"], f"/guides/{g['slug']}")]),
          {"@context": "https://schema.org", "@type": "Article", "headline": g["title"], "description": g["desc"], "image": og(g["hero"]), "dateModified": d, "datePublished": d,
           "author": {"@id": SITE_URL + "/#business"}, "publisher": {"@id": SITE_URL + "/#business"}, "mainEntityOfPage": url}, faq_ld(g["faq"])]
    return page(f"guides/{g['slug']}.html", title=fit(f"{g['title']} | Onesign", g['title'], f"{g['title'].split(':')[0].split('?')[0]}{'?' if '?' in g['title'] else ''} | Onesign"), desc=g["desc"], canonical=url, body=body, ogimg=og(g["hero"]), r=r, ld=ld, ogtype="article")

def guides_index():
    r = "../"
    body = f'''{phero(r, [("Home","index.html"),("Guides",None)], "sign guides.", "Straight answers on cost, planning consent, illumination and accessibility, written by the people who make and fit the signs.", "ws_assembly", kicker="Guides", ctas=False)}
<section class="sec"><div class="wrap">
  <div class="gcards">{guide_card(GUIDES[-1], r).replace('class="gcard"', 'class="gcard feat"', 1) + "".join(guide_card(g, r) for g in GUIDES[:-1])}</div>
</div></section>
{cta()}'''
    return page("guides/index.html", title="Sign Guides: Cost, Planning & Illumination | Onesign",
                desc="Plain-English sign guides from a UK manufacturer: what a shop sign costs, when you need consent, illuminated sign types and what to send for a quote.",
                canonical=SITE_URL + "/guides", body=body, ogimg=og("ws_assembly"), r=r, ld=[crumbs_ld([("Home", "/"), ("Guides", "/guides")])])

# ------------------------------------------------------------------ nationwide
def nationwide_page():
    r = ""
    faq = [("Do you install outside the North East?", "Yes. We manufacture in Gateshead and install across the whole of the UK."),
           ("Can you work to our brand guidelines?", "Yes. We colour-match finishes, follow your specification and produce a sample or first site for sign-off before the rest are made."),
           ("Can you survey all of our sites?", "Yes. We survey each site so that every sign is made to fit, and we record what is installed where."),
           ("Which accreditations do you hold?", "Constructionline, CSCS, IPAF, PASMA and Acclaim (SSIP). Our installers are trained to work at height and on live sites.")]
    steps = [("survey every site", "We measure and photograph each location and flag anything that affects the sign: fixings, power, access or consent."),
             ("agree the standard", "You sign off drawings and a first sign or sample, so the brand looks the same everywhere."),
             ("make them together", "Every sign is made in one factory, in one run, so colours and finishes match from site to site."),
             ("install to a programme", "Our own installers fit to an agreed schedule, including out of hours where sites need to stay open."),
             ("keep the record", "You get a record of what was fitted where, which makes future changes and maintenance simple.")]
    st = "".join(f'<li><span class="mk-n">{i+1:02d}</span><div><h3>{E(a)}</h3><p>{E(b)}</p></div></li>' for i, (a, b) in enumerate(steps))
    proof = "".join(case_card(CASE[s], r) for s in ("newcastle-university", "aldi-jaymac-warehouse", "northgate-hospital"))
    logos = "".join(f'<img src="img/brand/client-{i+1:02d}.png" alt="Client logo" loading="lazy" width="150" height="46">' for i in range(len(B.CLIENT_LOGOS)))
    body = f'''{phero(r, [("Home","index.html"),("Nationwide signage",None)], "nationwide signage rollouts.", "Multi-site signage made in one factory and fitted across the UK by our own installers, so every site matches.", "rolls", kicker="Multi-site &amp; national")}
<section class="sec"><div class="wrap two">
  <div class="prose"><span class="eyebrow" style="margin-bottom:18px;display:flex">One supplier, every site</span><h2>consistent signs, wherever you are.</h2>
    <p>When a brand has more than one site, the hard part is consistency. Different local suppliers mean different shades of your brand colour, different letter depths and different standards of fitting.</p>
    <p>We keep it in one place. Every sign is designed, made and checked in our 10,000 sq ft factory in Team Valley, then installed by our own trained teams. You get one point of contact, one standard and one invoice.</p>
    <p>We work this way for universities, NHS trusts, retailers and national brands, from a rebrand across a handful of branches to signage programmes that run for years.</p></div>
  <aside class="area-card"><h3>planning a rollout?</h3><ul><li>Site surveys anywhere in the UK</li><li>Samples and first-site sign-off</li><li>Constructionline, CSCS, IPAF and PASMA accredited</li></ul><a class="pill pill-solid" href="#contact">talk to us <span class="dot">→</span></a><a class="tel" href="tel:+441914876767">or call 0191 487 6767</a></aside>
</div></section>
<section class="sec alt"><div class="wrap">
  {head("How a rollout works", "five steps, one team.")}
  <ol class="made">{st}</ol>
</div></section>
<section class="sec"><div class="wrap">
  {head("Proof", "clients with more than one site.", extra='<a class="pill pill-ghost" href="work/index.html">all our work <span class="dot">→</span></a>')}
  <div class="ccards">{proof}</div>
  <div class="logo-wall">{logos}</div>
</div></section>
<section class="sec alt"><div class="wrap">
  {head("What we roll out", "from fascias to wayfinding.")}
  <div class="cards3">{"".join(type_card(t, r) for t in ("high-level-signs", "3d-letters", "wayfinding", "totems-monoliths", "vinyl-wall-graphics", "vehicle-graphics"))}</div>
</div></section>
<section class="sec"><div class="wrap">
  {head("Questions", "rollouts, answered.")}
  <div class="faq">{faq_html(faq)}</div>
</div></section>
{cta("planning a<br>multi-site project?", "Talk to us")}'''
    ld = [crumbs_ld([("Home", "/"), ("Nationwide signage", "/nationwide-signage")]),
          {"@context": "https://schema.org", "@type": "Service", "name": "Nationwide signage rollouts", "serviceType": "Multi-site signage manufacture and installation",
           "provider": {"@id": SITE_URL + "/#business"}, "areaServed": "United Kingdom", "url": SITE_URL + "/nationwide-signage"}, faq_ld(faq)]
    return page("nationwide-signage.html", title="Nationwide Signage Company | UK Multi-Site Rollouts | Onesign",
                desc="Multi-site signage rollouts across the UK. Every sign made in one Gateshead factory and installed by our own accredited teams, so every site matches.",
                canonical=SITE_URL + "/nationwide-signage", body=body, ogimg=og("rolls"), r=r, ld=ld)

# ------------------------------------------------------------------ privacy
def privacy_page():
    r = ""
    body = f'''{phero(r, [("Home","index.html"),("Privacy",None)], "privacy policy.", "What we collect when you contact us, why we collect it and the rights you have.", None, ctas=False, plain=True)}
<section class="sec"><div class="wrap"><article class="guide narrow">
  <p class="note">Last updated 16 November 2026.</p>
  <section><h2>who we are</h2><p>This website is run by Onesign &amp; Digital, D86 Princesway North, Team Valley, Gateshead NE11 0TU. We are the data controller for the personal information described here. You can contact us at <a href="mailto:sales@onesignanddigital.com">sales@onesignanddigital.com</a> or on 0191 487 6767.</p></section>
  <section><h2>what we collect</h2><p>When you send an enquiry we collect the details you give us: your name, business name, email address, phone number, site postcode, your message and any photos you attach.</p></section>
  <section><h2>why we use it</h2><p>We use your details to reply to your enquiry, prepare mockups and quotes, and carry out any work you ask us to do. Our legal bases are taking steps at your request before entering a contract, performing that contract, and our legitimate interest in running our business. We do not sell your information, and we only send marketing if you have asked for it.</p></section>
  <section><h2>who we share it with</h2><p>We share information only with suppliers who help us run our business, such as our email, customer-management and website hosting providers, and only so they can provide that service to us.</p></section>
  <section><h2>how long we keep it</h2><p>We keep enquiry details for as long as we need them to deal with your enquiry and any work that follows, and afterwards for as long as the law requires us to keep business records.</p></section>
  <section><h2>cookies</h2><p>This website does not use advertising or analytics cookies. If that changes, we will update this page and ask for your consent first.</p></section>
  <section><h2>your rights</h2><p>You can ask us for a copy of your information, ask us to correct or delete it, or object to how we use it. Email <a href="mailto:sales@onesignanddigital.com">sales@onesignanddigital.com</a> and we will respond within one month. If you are unhappy with our response you can complain to the Information Commissioner's Office at <a href="https://ico.org.uk" rel="noopener" target="_blank">ico.org.uk</a>.</p></section>
</article></div></section>'''
    return page("privacy.html", title="Privacy Policy | Onesign & Digital", desc="How Onesign & Digital collects and uses personal information from website enquiries.",
                canonical=SITE_URL + "/privacy", body=body, ogimg=og("hero"), r=r, ld=[crumbs_ld([("Home", "/"), ("Privacy", "/privacy")])])

# ------------------------------------------------------------------ build
def main():
    out = B.OUT
    os.makedirs(os.path.join(out, "assets"), exist_ok=True)
    B.build_css()
    shutil.copy(os.path.join(B.SRC, "site.js"), os.path.join(out, "assets", "site.js"))
    for d in ("fonts", "vendor"):
        if os.path.isdir(os.path.join(B.SRC, d)): shutil.copytree(os.path.join(B.SRC, d), os.path.join(out, "assets", d), dirs_exist_ok=True)
    if os.path.isdir(os.path.join(B.MASTERS, "brand")): shutil.copytree(os.path.join(B.MASTERS, "brand"), os.path.join(out, "img", "brand"), dirs_exist_ok=True)
    B.ASSET_V = hashlib.md5(open(os.path.join(out, "assets", "site.css"), "rb").read() + open(os.path.join(out, "assets", "site.js"), "rb").read()).hexdigest()[:10]
    B.home_page(); B.about_page(); B.contact_page()
    signs_index(); [B.type_page(t) for t in TYPES]
    sectors_index(); [B.sector_page(s) for s in SECTORS]
    work_index(); [case_page(c) for c in CASES]
    areas_index(); [area_page(a) for a in AREAS]
    guides_index(); [guide_page(g) for g in GUIDES]
    nationwide_page(); privacy_page(); B.not_found()
    B.extras(B.PAGES)
    print(len(B.PAGES), "pages")

if __name__ == "__main__":
    main()

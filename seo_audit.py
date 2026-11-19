import os, re, json, html, collections, sys
ROOT = sys.argv[1] if len(sys.argv) > 1 else "/home/claude/site"
SITE = "https://www.onesignanddigital.com"
pages = []
for d, _, fs in os.walk(ROOT):
    for f in fs:
        if f.endswith(".html"): pages.append(os.path.join(d, f))
issues = collections.defaultdict(list); titles = collections.defaultdict(list); descs = collections.defaultdict(list)
def g(rx, s):
    m = re.search(rx, s, re.S | re.I); return html.unescape(m.group(1)).strip() if m else None
sitemap = set(re.findall(r"<loc>(.*?)</loc>", open(f"{ROOT}/sitemap.xml").read()))
for p in sorted(pages):
    rel = p[len(ROOT):]; s = open(p, encoding="utf-8").read()
    url = SITE + (rel[:-5] if rel != "/index.html" else "/")
    url = url.replace("/index", "") if url.endswith("/index") else url
    t = g(r"<title>(.*?)</title>", s); d = g(r'<meta name="description" content="(.*?)"', s)
    can = g(r'<link rel="canonical" href="(.*?)"', s); robots = g(r'<meta name="robots" content="(.*?)"', s)
    h1s = re.findall(r"<h1[\s>]", s)
    is404 = rel == "/404.html"
    if not t: issues[rel].append("no title")
    else:
        titles[t].append(rel)
        if len(t) > 62: issues[rel].append(f"title {len(t)} chars: {t}")
        if len(t) < 25: issues[rel].append(f"title short {len(t)}: {t}")
    if not d: issues[rel].append("no description")
    else:
        descs[d].append(rel)
        if len(d) > 160: issues[rel].append(f"desc {len(d)} chars")
        if len(d) < 70: issues[rel].append(f"desc short {len(d)}: {d}")
    if not is404:
        if not can: issues[rel].append("no canonical")
        elif can != url: issues[rel].append(f"canonical {can} != {url}")
        if can and can not in sitemap and not (robots and "noindex" in robots): issues[rel].append("not in sitemap")
    if len(h1s) != 1: issues[rel].append(f"{len(h1s)} h1")
    for tag in ['property="og:title"', 'property="og:description"', 'property="og:image"', 'property="og:url"', 'name="twitter:card"']:
        if tag not in s: issues[rel].append("missing " + tag)
    if '<html lang="en-GB"' not in s and "<html lang=" not in s: issues[rel].append("no lang")
    for m in re.findall(r'<script type="application/ld\+json">(.*?)</script>', s, re.S):
        try: json.loads(m)
        except Exception as e: issues[rel].append(f"bad JSON-LD {e}")
    noalt = len(re.findall(r"<img(?![^>]*\balt=)[^>]*>", s))
    if noalt: issues[rel].append(f"{noalt} img without alt")
    ogi = g(r'<meta property="og:image" content="(.*?)"', s)
    if ogi and not ogi.startswith("https://"): issues[rel].append(f"og:image not absolute {ogi}")
for t, ps in titles.items():
    if len(ps) > 1: issues["DUP TITLE"].append(f"{t} -> {ps}")
for d, ps in descs.items():
    if len(ps) > 1: issues["DUP DESC"].append(f"{d[:60]} -> {ps}")
print(len(pages), "pages;", len(sitemap), "sitemap urls")
n = 0
for k, v in sorted(issues.items()):
    for i in v: print(k, "|", i); n += 1
print("TOTAL", n)

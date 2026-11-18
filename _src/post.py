"""After the build: make every internal link root-absolute and drop pages that no longer exist.
Vercel serves /sectors/index.html at /sectors (no trailing slash), so relative links like
'education.html' on that page resolved to /education.html and 404'd. Absolute paths always work."""
import os, re, sys
sys.argv = ["x"]
sys.path.insert(0, os.path.dirname(__file__))
from content import CASES
SITE = "/home/claude/site"
live = {c["slug"] for c in CASES}
for f in os.listdir(os.path.join(SITE, "work")):
    if f.endswith(".html") and f != "index.html" and f[:-5] not in live:
        os.remove(os.path.join(SITE, "work", f)); print("removed stale work/" + f)
ATTR = re.compile(r'(\s(?:href|src|data-img|data-full|poster)=")([^"]*)(")')
SRCSET = re.compile(r'(\ssrcset=")([^"]*)(")')
def fix(url, base):
    if not url or re.match(r'^([a-z][a-z0-9+.-]*:|/|#|\{)', url, re.I): return url
    parts = (base + "/" + url).split("/")
    out = []
    for p in parts:
        if p in ("", "."): continue
        if p == "..":
            if out: out.pop()
            continue
        out.append(p)
    return "/" + "/".join(out)
n = 0
for root, _, files in os.walk(SITE):
    for f in files:
        if not f.endswith(".html"): continue
        path = os.path.join(root, f)
        base = os.path.relpath(root, SITE).replace("\\", "/")
        base = "" if base == "." else base
        h = open(path, encoding="utf-8").read()
        h2 = ATTR.sub(lambda m: m.group(1) + fix(m.group(2), base) + m.group(3), h)
        h2 = SRCSET.sub(lambda m: m.group(1) + ", ".join(
            " ".join([fix(x.strip().split(" ")[0], base)] + x.strip().split(" ")[1:]) for x in m.group(2).split(",")) + m.group(3), h2)
        # links inside the job-map JSON
        h2 = re.sub(r'"(u|url|full|thumb)": ?"([^"]+)"', lambda m: '"' + m.group(1) + '": "' + fix(m.group(2), base) + '"', h2)
        if h2 != h: open(path, "w", encoding="utf-8").write(h2); n += 1
print("absolutised links in", n, "pages")

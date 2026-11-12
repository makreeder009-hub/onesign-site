# Onesign & Digital website

Static site. Every page is generated from `_src/data.py` (sign types, sectors, photos) by `_src/build.py`.

Rebuild after editing data: `cd _src && python3 build.py` (writes into `../onesign-site`; copy the output to the repo root).
Deployed on Vercel; `vercel.json` handles clean URLs and redirects from the old Wix addresses.

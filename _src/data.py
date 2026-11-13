# -*- coding: utf-8 -*-
"""Single source of truth for the Onesign site: photos, sign types, sectors."""

WIX = "https://static.wixstatic.com/media/653dfa_"
SITE_URL = "https://www.onesignanddigital.com"

# key -> (wix id, default caption, focal point for cropped views)
IMG = {
 # hero / brand
 "hero": ("3d36cad1fad04584b632515b872d7218~mv2.jpg", "Newcastle University illuminated building sign", "60% 40%"),
 # backlit panels
 "seventy3": ("b572d89e997348428f8007021a490b3e~mv2.jpg", "Bar Seventy Three backlit panel", "50% 40%"),
 "st_fit": ("eef2bc46710d41cc94169ead6bb540ab~mv2.jpg", "Bar Seventy Three panel being fitted", "50% 50%"),
 "st_front": ("255e4ed92be54304942b80889b9fd75a~mv2.jpg", "Bar Seventy Three panel above the shutter", "50% 30%"),
 "st_welcome": ("431b5b9876d54047ad4e8ff5d9bd96cd~mv2.jpg", "Bar Seventy Three welcome panel", "50% 50%"),
 "st_close": ("36f4b64dfaa24a7c84a229cfc6f273de~mv2.jpg", "Bar Seventy Three panel detail", "50% 50%"),
 "st_cnc": ("dda623ae438640d7a8868920adcbc153~mv2.jpg", "Routing a backlit panel on our CNC", "50% 50%"),
 "st_weld": ("b04adaf8a5364135bbb353deb5bbc63b~mv2.jpg", "Welding a panel frame in the workshop", "50% 50%"),
 "st_bench": ("903940587a9f4adaab9744ed08f3bf84~mv2.jpg", "Backlit panel on the bench before fitting", "50% 50%"),
 # 3D letters
 "vault": ("cab7a8061665494580bb85567c62faa2~mv2.png", "The Vault: fabricated, halo-lit letters on a panel", "50% 50%"),
 "cell": ("f1471cfd0f3d4a0d8a4083eeb2a69d60~mv2.jpg", "The Cell: halo-lit stainless steel 3D letters", "50% 50%"),
 "dog": ("886c1460a3e54976ac288d19edc144b5~mv2.jpg", "The Dog & Parrot: inset brass Komacel letters", "50% 50%"),
 "rds": ("2f2cb4faf24047a897657c9172bdfad9~mv2.jpg", "RDS Engineering: halo-lit letters on a panel", "50% 50%"),
 "catalyst_l": ("88c0e2cb5d2140a0afe07fb5bb4bfd36~mv2.jpg", "The Catalyst: 3D letters", "50% 50%"),
 # flat-cut letters (to confirm)
 "bankhouse": ("4793feb214d1420aaa3c76389bce25cd~mv2.png", "Bank House reception lettering", "50% 35%"),
 "urban": ("c5b436e7c58144b896587e9beb67b06e~mv2.jpg", "Urban Sciences Building wall lettering", "50% 50%"),
 "fira": ("c33dce8aea724e28ba982260b0d8fc91~mv2.jpg", "FIRA clinic wall lettering", "50% 40%"),
 # building & fascia
 "nhs_bld": ("2d5acebd5bc64333a207e239d95b4ead~mv2.jpg", "NHS Community Diagnostic Centre: fabricated letters on a panel", "50% 50%"),
 "nhs": ("99068c4c8e76476ab9310a3b987b1575~mv2.jpg", "NHS Community Diagnostic Centre building sign", "50% 50%"),
 "woodham": ("87780820837d48da9380a272ba777e3f~mv2.jpg", "Woodham Academy: digitally printed Dibond building sign", "50% 30%"),
 "aldi_bld": ("b8aa4bed97c942a2a0259cb8d1059937~mv2.jpg", "Aldi: printed vinyl on a large fabricated panel", "50% 40%"),
 "aldi": ("80d78348a3694f408400a2670712b46f~mv2.jpg", "Aldi & Jaymac warehouse", "50% 40%"),
 "jaymac": ("1ccb8c0b9e5c44c68f34592a8ac8823f~mv2.jpg", "Jaymac Solutions high-level lettering", "50% 50%"),
 "vertu": ("8ddf26d4afd54ccb912a126fba8ecb65~mv2.jpg", "Vertu Motors Arena", "50% 50%"),
 "vertu_night": ("a1207170ace94eb59afa435026268c0e~mv2.jpg", "Vertu Motors Arena lit at night", "50% 50%"),
 "rolls": ("a70093b969744e8bade977704edb7883~mv2.png", "Rolls-Royce building signage", "50% 50%"),
 "rolls_close": ("c46b9f362cf5459e8d543edaadf790d7~mv2.jpg", "Rolls-Royce high-level letters", "50% 50%"),
 "glow": ("c5609ebee285428a90d432dc37239297~mv2.jpg", "glow.: 3D acrylic letters on a fascia panel", "50% 50%"),
 "glow_ext": ("dd8292fef5ae4396b5b0998359ae2d9d~mv2.jpg", "glow. shopfront", "50% 50%"),
 "glow_night": ("c33d3038684948909f7828e52d66d941~mv2.jpg", "glow. fascia after dark", "50% 50%"),
 "ncl": ("e6459c96bd424aac9e2e1b7b24f432d1~mv2.jpg", "Newcastle University", "60% 40%"),
 "northgate": ("8f075195ea7f4f819b96edbadaf23d09~mv2.png", "Northgate Hospital", "50% 50%"),
 "catalyst": ("ed0b1d174bda43efac2b66b503a37b4b~mv2.jpg", "The Catalyst", "50% 50%"),
 "cork": ("58b00db1e27745479e9459424809be71~mv2.png", "Cork & Coffee", "50% 50%"),
 "cork_night": ("d5d6eaf8a3db46b387c0ce0ed6404956~mv2.jpg", "Cork & Coffee at night", "50% 50%"),
 # projecting
 "works": ("f5c6fc1570344e8cb1ae081fc3d7733b~mv2.jpg", "The Works projecting sign", "50% 30%"),
 "rascals_proj": ("4a9d2f2cd0db456083da87bb07ef7bf4~mv2.jpg", "Rascals projecting sign", "50% 40%"),
 # neon
 "neonA": ("29cc10994a684505a2e34d82e83ddcf3~mv2.jpg", "Blue LED neon lettering", "50% 50%"),
 "neonB": ("d2de257bef414c2fa5bc8cd8abe0024d~mv2.jpg", "Bar LED neon", "50% 50%"),
 "neonC": ("cb0c652158634e5db06bb9bbbb9d3da6~mv2.jpg", "LED neon wall sign", "50% 50%"),
 "neonD": ("ff2f890f6be245ac8d310c2a56167519~mv2.jpg", "Green LED neon", "50% 50%"),
 "rascals_neon": ("d7736c10ce6e4da7b7d39e9e68fbd94e~mv2.jpg", "Rascals LED neon", "50% 50%"),
 "welcome_neon": ("0b608b59ba174f208a0f4dec8faf27d3~mv2.jpg", "Pink LED neon welcome wall", "50% 50%"),
 # vinyl & wall graphics
 "w_nevergiveup": ("3fff75b6ceac4e008f2c2d874c25c1c9~mv2.jpg", "Woodham Academy cut vinyl lettering", "50% 50%"),
 "w_truetest": ("87a572821c7c4dfebea900950847abf2~mv2.jpg", "Woodham Academy cut vinyl quote", "50% 50%"),
 "univinyl": ("971a39df2d6b4876a499bceaeae36480~mv2.jpg", "Newcastle University window and wall graphics", "50% 50%"),
 "nhs_skyline": ("c8bfcbb2380d46b3ac2d1ee9b5456eda~mv2.jpg", "NHS CDC printed skyline wall graphic", "50% 50%"),
 "nhs_skyline2": ("7d212dc5bd774a89b8e674a14b0be036~mv2.jpg", "NHS CDC wall graphic detail", "50% 50%"),
 "arv": ("e3847222e6774f25a17b838e75959094~mv2.jpg", "ARV wall graphic", "50% 50%"),
 "lineart": ("fb13ff53521942088ad8d9496dbc896e~mv2.png", "Line-art wall graphic", "50% 50%"),
 "w_logo": ("92a1f032b09f43c6a57a1d9f39245915~mv2.jpg", "Woodham Academy wall graphic", "50% 50%"),
 # print
 "hoarding": ("641df8f7592f423f9cfc2ecbecd48490~mv2.jpg", "Printed site hoarding", "50% 50%"),
 "fence_banner": ("0d2938c6cc804d26a2ca41002d07ebfb~mv2.jpg", "Printed fence banner", "50% 50%"),
 "lfBm": ("c96d66538f2b4450b5301eeb7472f497~mv2.jpg", "Large format print for B&M", "50% 50%"),
 "lfPosters": ("1756e03f531b4a549277f5ae2d425616~mv2.jpg", "Printed posters", "50% 50%"),
 "lfPrint": ("26720e30b371494ea8c67b53fc16fa25~mv2.jpg", "Large format print detail", "50% 50%"),
 "bowmer": ("bd467f1af40e4eb6bda31d438e350ffa~mv2.jpg", "Bowmer + Kirkland printed hoarding", "50% 50%"),
 "hoarding2": ("b8be77c9469f4d6486cb53d13207608d~mv2.jpg", "Construction hoarding", "50% 50%"),
 # totems
 "tesco": ("b78d448959044703b43d3067030542e0~mv2.jpg", "Tesco illuminated totem", "50% 40%"),
 "totW": ("0554f863bdb245778f1f5b6c64b41e0e~mv2.jpg", "Retail park totem", "50% 40%"),
 "sun_totem": ("e4386bdd05764bf49bde0ed1aa975fc9~mv2.jpg", "Drive-thru and Sun tanning totem", "50% 40%"),
 "dealer_totem": ("1582ba86762e447cb5c3f45eceaf4b1a~mv2.webp", "Car dealership totem", "50% 40%"),
 "w_ext_dir": ("09ee92ea79b44552ac173c00d71c84e0~mv2.jpg", "Woodham Academy entrance monolith", "50% 50%"),
 "uni_entry": ("b714b5324f9d4ae0b0702018302ad3d3~mv2.jpg", "Campus entrance monoliths", "50% 50%"),
 # wayfinding
 "w_red_g": ("32094540ce384d769135c65c8721709e~mv2.jpg", "Woodham Academy level identification", "50% 50%"),
 "w_green2": ("cd56dfdad23f475eae3938f70e521121~mv2.jpg", "Woodham Academy level 2", "50% 50%"),
 "nhs_dir": ("d1b72d708ac646c883fd29de480f8199~mv2.jpg", "NHS CDC directional signs", "50% 50%"),
 "nhs_proj": ("314955f99abf413abee2a63e3df44e39~mv2.jpg", "NHS CDC projecting directional sign", "50% 50%"),
 "uni_totem": ("47884b6437b24777acc027b4d002b0ee~mv2.jpg", "Newcastle University wayfinding totem", "50% 50%"),
 "ng_totem": ("7acb313d063d450192050bbfc2f9dd8f~mv2.jpg", "Northgate Hospital directional totem", "50% 50%"),
 "wardDir": ("4aa7e0aee9244a7393f517e5a23549db~mv2.jpg", "Hospital ward directory", "50% 50%"),
 "courtyard": ("5354fc6f8e17493292165739f58b41a0~mv2.png", "Northgate Hospital courtyard sign", "50% 50%"),
 # vehicles
 "vanPark": ("6634bdffe030450e9e9d46e77acf2614~mv2.jpg", "Fleet livery", "50% 50%"),
 "vanYellow": ("e0dfe23982704004829b4eb0ec5a0fa6~mv2.jpg", "Full-colour van graphics", "50% 50%"),
 "vanFabio": ("fef3810e24c14e8da0e4ce5698e11059~mv2.png", "Restaurant van graphics", "50% 50%"),
 # sectors / misc
 "alwinton": ("86abe8967a2f456397289c51685c4260~mv2.jpg", "Alwinton & Berwick ward entrance", "50% 50%"),
 "sycamore": ("ec0a96cedb9a420ca76e93cf07471663~mv2.jpg", "Sycamore ward signage", "50% 50%"),
 "harbro": ("48725d483de84541ac8a85b5e1787789~mv2.jpeg", "Harbro storefront", "50% 40%"),
 "sunclub": ("3d12ed5180094023a176f5a9f0e35aa3~mv2.jpg", "Sun Club interior signage", "50% 50%"),
 "kloset": ("5a30404bc94b4c4880bd11d8dd211743~mv2.jpg", "Kloset Luxury interior lettering", "50% 50%"),
 "carpark": ("47c02f05a36648cc9a33da15ca1f2626~mv2.jpg", "Car park safety signage", "50% 50%"),
 "fireExit": ("63f7b14912d84f62b5a0c44b1f6d3d77~mv2.jpg", "Fire exit floor graphics", "50% 50%"),
 "sitePlan": ("ce300f663e574873bb7cecf4dbc7e211~mv2.jpeg", "Design visual of a site plan", "50% 50%"),
 "weld": ("519d7067bdbc453f87348f03482b4f84~mv2.jpg", "Welding a sign frame in our Team Valley workshop", "50% 50%"),
 "install": ("7172f17c9df5478db788c8f4d2ce0aa4~mv2.jpg", "Installing a high-level Aldi sign", "50% 30%"),
 "install2": ("bf47c9c3a7a04b669a8352818d39f7e3~mv2.jpg", "Onesign fitter surveying an NHS site", "22% 50%"),
 "jaymac_close": ("ac2d58f3ac3c4041ac4b6917c537679b~mv2.jpg", "Jaymac letters close up", "50% 50%"),
 "rolls_int": ("34b0ef4c689745a2b270dd8647e7b432~mv2.jpg", "Rolls-Royce interior lettering", "50% 50%"),
}

# ---- Instagram photos (saved locally in img/ig) ----
def _ig(n, c, p="50% 50%"): return ("local:"+n, c, p)
IMG.update({
 "ig_tribeca": _ig("3d-tribeca","Tribeca: 3D letters"),
 "ig_zen": _ig("3d-zen","Zen: halo-lit 3D letters"),
 "ig_byre": _ig("3d-byre","BYRE: 3D letters"),
 "ig_maple": _ig("3d-maple","Maple: face-lit 3D letters"),
 "ig_fitt": _ig("3d-fitt","Fitt: 3D letters"),
 "ig_court": _ig("3d-the-court","The Court: gold 3D letters"),
 "ig_dubliner": _ig("3d-the-dubliner","The Dubliner: illuminated 3D letters"),
 "ig_mango": _ig("3d-mango","MANGO letters in the workshop"),
 "ig_stephenson": _ig("3d-stephenson-building","Stephenson Building letters before fitting"),
 "ig_goldscript": _ig("3d-gold-script","Gold script letters in the workshop"),
 "ig_atom": _ig("3d-atom-moss-wall","atom: letters on a moss wall"),
 "ig_pantera": _ig("flat-pantera","Pantera Advisory Group: flat-cut logo and letters"),
 "ig_wrgroup": _ig("flat-wr-group","WR Group: flat-cut letters on brick"),
 "ig_nhs_night": _ig("bld-nhs-cdc-night","NHS Community Diagnostic Centre lit at night"),
 "ig_urgent": _ig("bld-urgent-emergency-care","Urgent & Emergency Care building sign"),
 "ig_nhs_cumbria": _ig("bld-nhs-cumbria","NHS Cumbria, Northumberland, Tyne & Wear building sign"),
 "ig_tms": _ig("bld-tms-grid","TMS Grid building sign"),
 "ig_jaymac_wall": _ig("bld-jaymac","Jaymac Solutions wall graphic"),
 "ig_companyshop": _ig("bld-company-shop","Company Shop building signs"),
 "ig_smartvape": _ig("proj-smart-vape","Smart Vape round projecting sign"),
 "ig_corner": _ig("proj-corner","Round projecting sign on a corner unit"),
 "ig_queenshead": _ig("proj-queens-head","Queen's Head projecting sign and fascia"),
 "ig_lane": _ig("proj-lane","Projecting sign in a lane"),
 "ig_gavroche": _ig("lb-le-gavroche","Le Gavroche light box"),
 "ig_craicn": _ig("lb-craicn-campers","Craic'n Campers: internal panel with applied vinyl"),
 "ig_codcrust": _ig("bp-cod-and-crust","Cod & Crust: aperture-cut backlit panel with push-through opal acrylic"),
 "ig_neon_orange": _ig("neon-orange","Orange LED neon"),
 "ig_neon_red": _ig("neon-red","Red LED neon"),
 "ig_leancuisine": _ig("neon-lean-cuisine","Lean Cuisine LED neon"),
 "ig_neon_yellow": _ig("neon-yellow","Yellow LED neon"),
 "ig_pudes": _ig("neon-the-pudes","The Pudes LED neon"),
 "ig_durham": _ig("vg-durham-microsoft","Durham University and Microsoft wall graphic"),
 "ig_pamper_trailer": _ig("vg-little-pamper","Pretty Pamper trailer graphics"),
 "ig_lineart_install": _ig("vg-lineart-install","Fitting a line-art wall graphic"),
 "ig_lineart": _ig("vg-lineart","Line-art window and wall graphic"),
 "ig_kier": _ig("print-kier-flags","Kier printed feather flags"),
 "ig_workwear": _ig("print-workwear-window","Workwear Express printed window graphics"),
 "ig_ocado": _ig("print-ocado","Printed boards for an Ocado event"),
 "ig_totem_dir": _ig("tot-directional","Directional totem"),
 "ig_visitor": _ig("way-visitor-colleague","Visitor and colleague directional signs"),
 "ig_cs_dir": _ig("way-company-shop","Company Shop Group site sign"),
 "ig_storeentrance": _ig("way-store-entrance","Store entrance directional sign"),
 "ig_toilet": _ig("way-visitor-toilet","Tactile door sign with Braille"),
 "ig_corridor": _ig("way-corridor","Corridor wayfinding"),
 "ig_way_dir": _ig("way-directional","Directional wall and floor signs"),
 "ig_salto": _ig("veh-salto","Salto van graphics"),
 "ig_park": _ig("veh-park","Park Electrical van livery"),
 "ig_park2": _ig("veh-park-2","Park Electrical fleet livery"),
})

LOGO = WIX + "ea4e2d45d7ca408b95493574790bc8b5~mv2.png"
ACCRED = WIX + "33c82d7475df4710beb102bfcd242aff~mv2.png"
CLIENT_LOGOS = ["b3e8ef4323c74da294e5adc1d1a485c8","1822bb02b0d24934aa1ae4037115b9f1","5636a57a971b4536ba0f2e455fce6cbd","faf556ac38dd4e0eac91f9a633315ec4","ad4db19cfa45481d8b8468db0842fe2c","991cd2fdd18f426cb5cb6ed8cba3f3cb","b608dd4981184f69a957c23d1ce75442","392120d93e844ccb9113ef1756455a5b","79b95a91a6354bf78bdad56b575a2bcc","acc9f9802d7e41bfa539565781b422c8","42cdc991edee4943ab68e2373f046702","256dad9579cc4bfcac59eadf9eaee7cb","e13232bfb49f48b9bce301d7c15a646c","5c682d1f4b94409c992961cb26a875de","92769188d17142e0bbffc114215e0a7e","9ea581258bfd48da9c70df520dbcb7d2","e29b0d6623af4113a602a38c5fa253ee","6ce97783f791465b894968d97128d1de","6b0ad15c933a469abfca715fb30e787a","28b3777b93c444e3bc90002a6dcfc6ff"]

# ---------------------------------------------------------------------------
# SIGN TYPES  (order = order on the site; backlit panels sits near the top)
# label: how it reads in lowercase headings (keeps "3D" capitalised)
# ---------------------------------------------------------------------------
TYPES = [
 dict(slug="3d-letters", name="3D letters", label="3D letters", code="OS-3D",
  seo_title="3D Letter Signs: Fabricated, Komacel & Acrylic",
  meta="Built-up 3D letter signs made in Gateshead: fabricated face-lit and halo-lit letters, Komacel letters with brass or mirror inlays, and acrylic letters. Fixed to the wall or on a panel.",
  hero="vault",
  photos=["vault","ig_dubliner","cell","dog","ig_zen","ig_court","ig_tribeca","ig_maple","ig_fitt","ig_byre","ig_atom","rds","catalyst_l","ig_goldscript","ig_mango","ig_stephenson"],
  desc="Letters with real depth that stand proud of the wall. We make three kinds: fabricated metal letters, Komacel letters and acrylic letters, fixed straight to the wall on stand-off locators or mounted on a panel.",
  ideal=["shopfronts","bars & restaurants","receptions","offices"],
  spec=[["Types","Fabricated (aluminium or stainless), Komacel, acrylic"],
        ["Fabricated","Face-lit (rim & return), halo-lit or non-lit"],
        ["Komacel","Halo-lit only; inset-routed for brass, copper, Trotec metallics or mirrored acrylic"],
        ["Acrylic","Translucent, so light passes through the letter"],
        ["Fixing","Straight to the wall on stand-off locators, or on a panel"]],
  variants=[
   dict(t="Fabricated letters", img="cell", p="Built from a metal face and folded returns. The most versatile option, and the one to choose for large or high-level letters.", tags=["face-lit (rim & return)","halo-lit","non-lit"]),
   dict(t="Komacel letters", img="dog", p="Cut from solid Komacel, then inset-routed so the face can be filled with brass, copper or Trotec metallic laminates, a cheaper route to a brushed-metal finish. Mirrored acrylic in gold, silver or rose gold works too.", tags=["halo-lit only","brass / copper inlay","mirrored acrylic"]),
   dict(t="Acrylic letters", img="glow", p="Solid acrylic lets light pass through, so letters glow when lit from behind. Often mounted on a panel, like our glow. fascia.", tags=["light passes through","on a panel","coloured or clear"]),
  ],
  notes=["Every letter can go straight onto the wall on stand-off locators, or onto a panel when the wall isn't suitable or you want a backdrop.",
         "The Vault is a good example of fabricated, halo-lit letters on a panel; The Cell uses halo-lit stainless steel letters.",
         "Not sure which suits your budget? We'll mock up the options on a photo of your building."],
  faq=[("What's the difference between face-lit and halo-lit?","Face-lit letters glow through the front face, with light contained by the rim and returns. Halo-lit letters have a solid face and throw light back onto the wall behind, creating a glow around each letter."),
       ("Can Komacel letters be face-lit?","No. Komacel letters are halo-lit only. If you want the face itself to glow, fabricated or acrylic letters are the better choice."),
       ("Can letters go straight onto brick or cladding?","Yes. We fix them on stand-off locators so they sit off the wall. If the surface isn't suitable, we mount them on a panel instead.")]),

 dict(slug="backlit-panels", name="Backlit panels", label="backlit panels", code="OS-BP",
  seo_title="Backlit Panel Signs: Illuminated Aperture-Cut Panels",
  meta="Illuminated backlit panel signs designed and fabricated in Gateshead. Shaped or rectangular panels with cut-through graphics that glow at night.",
  hero="seventy3",
  photos=["seventy3","ig_codcrust","st_front","st_welcome","st_close","st_fit"],
  desc="One of our most popular signs. A fabricated panel with your name and logo aperture-cut through it and filled with push-through opal acrylic, lit from inside with LEDs so the graphics glow at night and read crisply by day. Bar Seventy Three and Cod & Crust are good examples.",
  ideal=["bars & restaurants","shopfronts","salons","gyms"],
  spec=[["Panel","Fabricated aluminium, powder-coated to any colour"],
        ["Graphics","Aperture-cut through the face, with push-through opal acrylic"],
        ["Lighting","Internal LEDs, so only the graphics glow"],
        ["Shape","Rectangular or cut to the outline of your logo"],
        ["Fixing","Wall-mounted on hidden fixings"]],
  variants=[], notes=["Panels can be shaped around your logo, as with Bar Seventy Three, or kept as a clean rectangle.",
         "Everything is cut, folded and wired in our own workshop."],
  faq=[("Does the whole panel light up?","No. Only the cut-through graphics glow; the rest of the panel stays solid, which is what gives backlit panels their crisp look at night."),
       ("Can the panel be a custom shape?","Yes. Panels can follow the outline of your logo or be a simple rectangle."),
       ("Do you fit them too?","Yes. Our own fitting teams install every panel we make.")]),

 dict(slug="flat-cut-letters", name="Flat-cut letters", label="flat-cut letters", code="OS-FC",
  seo_title="Flat-Cut Letter Signs: CNC & Laser Cut Lettering",
  meta="Flat-cut letters cut from solid sheet on our CNC and laser in Gateshead. Crisp, cost-effective lettering for receptions, offices and exteriors.",
  hero="bankhouse",
  photos=["ig_pantera","ig_wrgroup","bankhouse","urban","fira"],
  desc="Letters cut from solid sheet on our CNC router and laser, with a crisp flat face and no returns. A clean, cost-effective way to put a name on a wall, inside or out.",
  ideal=["receptions","offices","schools","feature walls"],
  spec=[["Materials","Acrylic, aluminium composite, stainless steel, foam PVC"],
        ["Cutting","CNC router and laser, in-house"],
        ["Face","Flat, no returns"],
        ["Fixing","Stand-off locators, pins or flush"],
        ["Finish","Painted, brushed, mirrored or vinyl-faced"]],
  variants=[], notes=["Flat-cut letters cost less than 3D letters and suit interiors especially well."],
  faq=[("Are flat-cut letters illuminated?","Usually not. If you want lighting, 3D letters or a backlit panel are the better route."),
       ("Can they be used outside?","Yes, in exterior-grade materials such as aluminium composite or stainless steel.")]),

 dict(slug="building-signs", name="Fascia & building signs", label="fascia & building signs", code="OS-BS",
  seo_title="Large Building Signs & High-Level Fascia Signage",
  meta="Large, high-level building signs surveyed, fabricated and installed by Onesign's own crews: fabricated letters, letters on panels, printed Dibond and vinyl-wrapped panels.",
  hero="nhs_bld",
  photos=["nhs_bld","ig_nhs_night","vertu_night","ig_urgent","woodham","aldi_bld","ig_tms","ig_companyshop","ig_nhs_cumbria","rolls","glow"],
  desc="Large, high-level signs on the side of buildings: big fabricated letters, letters on panels, digitally printed Dibond and vinyl-wrapped fabricated panels. Surveyed, engineered and fitted by our own crews.",
  ideal=["new builds","hospitals","schools","warehouses","HQs"],
  spec=[["Built from","Fabricated letters, letters on panels, printed Dibond, vinyl on fabricated panels"],
        ["Scale","Large-format, high-level elevations"],
        ["Access","Powered access by our IPAF and PASMA trained teams"],
        ["Fixing","Engineered for cladding, brick and curtain wall"],
        ["Lighting","Illuminated or non-lit"]],
  variants=[], notes=["NHS CDC: large fabricated letters on a panel on the side of the building.",
         "Woodham Academy: a large building sign in digitally printed Dibond.",
         "Aldi: a large digitally printed vinyl applied to a fabricated panel."],
  faq=[("Do you handle high-level installs?","Yes. Our IPAF and PASMA trained crews install from powered access, including on live hospital and campus sites."),
       ("Will my building sign need planning permission?","Many illuminated or large signs need advertisement consent. We'll tell you at the survey stage and can prepare the drawings you need.")]),

 dict(slug="projecting-signs", name="Projecting signs", label="projecting signs", code="OS-PR",
  seo_title="Projecting Signs: Double-Sided Hanging Shop Signs",
  meta="Double-sided projecting signs made in Gateshead, so you're seen from along the street. Round, square or bespoke, lit or non-lit.",
  hero="ig_smartvape",
  photos=["ig_smartvape","ig_queenshead","ig_corner","ig_lane","works","rascals_proj"],
  desc="Double-sided signs that stick out from the building, so people walking along the street see you, not just those standing in front. Round, square or fully bespoke.",
  ideal=["high streets","pubs","cafés","shopping centres"],
  spec=[["Format","Double-sided, round, square or bespoke"],["Bracket","Fixed or decorative wall bracket, powder-coated"],
        ["Lighting","Internally lit or non-lit"],["Build","Fabricated tray with acrylic or printed faces"],
        ["Consent","We'll advise on advertisement consent where needed"]],
  variants=[], notes=["Projecting signs work hardest on busy streets where shopfronts are seen side-on."],
  faq=[("Do projecting signs need planning permission?","Often, especially if illuminated or in a conservation area. We'll check and advise before you commit.")]),

 dict(slug="lightboxes-flex-faces", name="Light boxes & flex faces", label="light boxes & flex faces", code="OS-LB",
  seo_title="Light Box Signs & Flex Face Signs",
  meta="Illuminated light boxes and large-scale flex face signs made in Gateshead. Acrylic-faced light boxes for smaller signs, tensioned flex faces for big ones.",
  hero="ig_gavroche",
  photos=["ig_gavroche"],
  desc="Two ways to light a whole sign face. Light boxes are generally smaller, with acrylic faces lit from inside. Flex faces are for larger scale: a printed fabric skin tensioned across a frame, with no seams.",
  ideal=["retail parks","forecourts","shopfronts","large fascias"],
  spec=[["Light boxes","Smaller signs, aluminium box with acrylic face"],["Flex faces","Large-scale, printed flex fabric tensioned in a frame"],
        ["Lighting","LED, lit evenly across the face"],["Sides","Single or double-sided"],
        ["Rebrand","Flex faces can be re-skinned without replacing the frame"]],
  variants=[dict(t="Light boxes", img="ig_gavroche", p="Generally smaller, with acrylic faces lit evenly from inside. Neat on shopfronts and as projecting signs.", tags=["acrylic face","smaller scale"]),
            dict(t="Flex faces", img=None, p="Built for scale. A printed flex fabric skin is stretched across a large frame, so huge signs go up without seams.", tags=["large scale","seamless","re-skinnable"])],
  notes=["Choose a light box for smaller, crisp signs and a flex face once the sign gets big."],
  faq=[("When should I choose a flex face over a light box?","Once a sign gets large, acrylic faces need joins. A flex face covers big areas in one seamless skin.")]),

 dict(slug="neon-led-neon", name="Neon & LED neon", label="neon & LED neon", code="OS-NE",
  seo_title="LED Neon Signs: Custom Neon for Bars, Salons & Walls",
  meta="Custom LED neon signs made in Gateshead: low-voltage, cool to the touch and far tougher than glass. Any colour, shape or backing.",
  hero="neonB",
  photos=["neonB","ig_leancuisine","ig_neon_orange","welcome_neon","ig_pudes","ig_neon_red","rascals_neon","ig_neon_yellow","neonA","neonC","neonD"],
  desc="The glow of classic neon made with modern LED flex: low voltage, cool to the touch and far tougher than glass. Ideal for statement walls, bars and photo moments.",
  ideal=["bars","salons","events","feature walls"],
  spec=[["Tube","Silicone LED neon flex"],["Backing","Clear, coloured or mirrored acrylic, cut to shape"],
        ["Colours","Warm white, ice white and a full colour range"],["Power","Low-voltage, plug-in or hard-wired, dimmable options"],
        ["Rating","Indoor, with outdoor-rated versions"]],
  variants=[], notes=["Send us your logo or a line of text and we'll draw it up in neon."],
  faq=[("Is LED neon safe indoors?","Yes. It runs at low voltage and stays cool to the touch, unlike glass neon."),
       ("Can it go outside?","Yes, using outdoor-rated LED neon and fittings.")]),

 dict(slug="vinyl-wall-graphics", name="Vinyl & wall graphics", label="vinyl & wall graphics", code="OS-VG",
  seo_title="Vinyl Graphics & Wall Graphics: Window, Glass & Murals",
  meta="Cut vinyl lettering, window frosting, glass manifestation and printed wall graphics, designed and fitted by Onesign in the North East.",
  hero="w_nevergiveup",
  photos=["w_nevergiveup","ig_durham","ig_lineart_install","nhs_skyline","ig_lineart","ig_jaymac_wall","univinyl","arv","w_truetest","ig_craicn"],
  desc="Two related jobs under one roof. Vinyl graphics are cut from coloured or frosted film for lettering, windows and glass. Wall graphics are digitally printed wraps and murals that cover whole walls.",
  ideal=["schools","offices","clinics","windows & glass"],
  spec=[["Vinyl graphics","Cut lettering, frosted and etched-effect films, glass manifestation"],
        ["Wall graphics","Digitally printed wall wraps and murals"],["Surfaces","Glass, painted walls, doors"],
        ["Print","Large-format, in-house"],["Fitting","Bubble-free install by our own team"]],
  variants=[dict(t="Vinyl graphics", img="w_nevergiveup", p="Cut from solid-colour or frosted film: lettering, values walls, window graphics, privacy frosting and glass manifestation.", tags=["cut vinyl","frosting","manifestation"]),
            dict(t="Wall graphics", img="nhs_skyline", p="Digitally printed and applied edge to edge to turn a whole wall into branding, wayfinding or artwork.", tags=["printed","full wall","murals"])],
  notes=["Glass manifestation helps doors and screens meet safety requirements."],
  faq=[("Can wall graphics go on any wall?","Most smooth, painted walls are fine. We'll check the surface at survey.")]),

 dict(slug="digital-large-format-print", name="Digital & large format print", label="digital & large format print", code="OS-LF",
  seo_title="Large Format Printing: Hoardings, Banners & Display Print",
  meta="Large format digital print from our own wide-format printers in Gateshead: hoardings, banners, posters, boards and window graphics.",
  hero="hoarding",
  photos=["hoarding","ig_workwear","ig_kier","ig_ocado","fence_banner","lfBm","lfPosters","lfPrint"],
  desc="Big, bold, colour-matched print from our own wide-format printers: hoardings, banners, posters, window graphics and display boards, printed and finished in-house so turnaround stays fast.",
  ideal=["hoardings","banners","posters","promotions"],
  spec=[["Output","Large-format and roll-to-roll digital print"],["Media","Vinyl, banner PVC, paper, fabric, rigid boards"],
        ["Boards","Foamex, Dibond and composite panels"],["Finish","Laminated, contour-cut or eyeleted"],["Colour","Matched to your brand guidelines"]],
  variants=[], notes=["Printing in-house means we control colour and turnaround."],
  faq=[("Can you match our brand colours?","Yes. We colour-match to your brand guidelines.")]),

 dict(slug="totems-monoliths", name="Totems & monoliths", label="totems & monoliths", code="OS-TM",
  seo_title="Totem Signs & Monolith Signs",
  meta="Freestanding totem and monolith signs, lit or non-lit, single-brand or multi-tenant, made and installed by Onesign.",
  hero="tesco",
  photos=["tesco","sun_totem","ig_totem_dir","totW","w_ext_dir","dealer_totem","uni_entry"],
  desc="Freestanding signs that mark your entrance and guide people in from the road. Illuminated or non-lit, single-brand or multi-tenant.",
  ideal=["retail parks","car dealers","campuses","business parks"],
  spec=[["Build","Steel frame with aluminium skins"],["Faces","Fabricated letters, push-through acrylic or printed"],
        ["Lighting","Internally lit or non-lit"],["Base","Concrete foundation, groundwork by our team"],["Panels","Interchangeable tenant panels available"]],
  variants=[], notes=["Multi-tenant totems can use swappable panels so tenants can change without replacing the sign."],
  faq=[("Do you do the groundwork?","Yes. Our team handles foundations and installation.")]),

 dict(slug="wayfinding", name="Wayfinding", label="wayfinding", code="OS-WF",
  seo_title="Wayfinding Signage for Hospitals, Schools & Campuses",
  meta="Wayfinding sign schemes planned, made and installed by Onesign: directional signs, level identification, totems and door signs for hospitals, schools and campuses.",
  hero="w_red_g",
  photos=["w_red_g","ig_toilet","ig_visitor","nhs_dir","ig_storeentrance","uni_totem","ig_cs_dir","ng_totem","ig_corridor","ig_way_dir","w_green2","nhs_proj","wardDir"],
  desc="Sign families that get people where they need to be, from the car park to the right room. Planned around how your site is used, and built to accessibility standards.",
  ideal=["hospitals","universities","schools","large sites"],
  spec=[["Scope","Site survey, sign schedule and location plans"],["Types","Directional, door, level ID, totems, fingerposts"],
        ["Accessible","Contrast, tactile and Braille options"],["Modular","Updatable inserts for changing departments"],["Sites","Live hospital and campus installs"]],
  variants=[], notes=["We plan wayfinding from the visitor's point of view, starting at the car park."],
  faq=[("Can you work on a live hospital site?","Yes. We've installed on live NHS sites and plan the work around the people using the building.")]),

 dict(slug="vehicle-graphics", name="Vehicle graphics", label="vehicle graphics", code="OS-VH",
  seo_title="Van Signwriting & Vehicle Graphics",
  meta="Van graphics, fleet livery and vehicle wraps designed, printed and fitted in Gateshead by Onesign.",
  hero="vanPark",
  photos=["vanPark","ig_park2","ig_salto","ig_pamper_trailer","vanYellow","vanFabio","ig_park"],
  desc="Turn your vans into moving adverts. From simple contact lettering to full wraps, designed and printed in-house and fitted to a crisp finish.",
  ideal=["trade vans","fleets","delivery","food trucks"],
  spec=[["Coverage","Lettering, part-wrap or full wrap"],["Film","Cast vinyl with protective laminate"],
        ["Print","Large-format, colour matched"],["Fleet","Consistent livery across mixed vehicles"],["Removal","Removable without damaging paint"]],
  variants=[], notes=["We keep fleet livery consistent across different vehicle makes and sizes."],
  faq=[("Will vehicle graphics damage my paintwork?","No. Quality cast vinyl removes cleanly from factory paint.")]),
]

# [slug, name, short blurb, photo, icon id, intro, gallery, type slugs, points]
SECTORS = [
 dict(slug="healthcare", name="healthcare", blurb="Wayfinding and compliance signs for hospitals and clinics.", img="alwinton", icon="f7195e7a70624088b9833dc7549b4386",
  title="Healthcare Signage for Hospitals & Clinics",
  intro="Clear signage is critical in healthcare. From wayfinding to compliance signs, we provide solutions that make hospitals and clinics safer and easier to get around, installed by teams used to working on live sites.",
  gallery=["ig_nhs_night","ig_urgent","ig_nhs_cumbria","ig_toilet","alwinton","nhs_bld","nhs_dir","nhs_skyline","sycamore","ng_totem","wardDir","nhs_proj"],
  types=["wayfinding","building-signs","vinyl-wall-graphics","totems-monoliths"],
  points=[("Live-site installs","We plan work around patients, staff and visitors on working hospital sites."),("Wayfinding that works","Schemes planned from the car park to the right ward."),("Compliance","Safety and accessibility built into every sign family.")]),
 dict(slug="education", name="education", blurb="Directional, branding and safety signs for schools and campuses.", img="woodham", icon="20409fa21f444682ac49b746537928b3",
  title="School & University Signage",
  intro="Our signage helps schools and universities create organised, easy-to-navigate spaces, with directional, branding and safety signs that keep campuses running smoothly.",
  gallery=["ig_durham","woodham","w_red_g","w_nevergiveup","w_green2","w_truetest","uni_totem","ncl","univinyl"],
  types=["wayfinding","vinyl-wall-graphics","building-signs","totems-monoliths"],
  points=[("Whole-school schemes","Building signs, wayfinding and values walls designed as one family."),("Safe materials","Durable signs suitable for busy corridors."),("Holiday installs","We can schedule installs around term time.")]),
 dict(slug="construction", name="construction", blurb="Branded hoardings and site safety boards that keep sites compliant.", img="bowmer", icon="e6d70cd2c2ac4170a00febc7dd17f224",
  title="Construction Hoardings & Site Signage",
  intro="From safety boards to branded hoardings, we deliver durable signage that keeps construction sites compliant and organised, with fast, reliable service.",
  gallery=["ig_kier","bowmer","hoarding","hoarding2","fence_banner","catalyst"],
  types=["digital-large-format-print","building-signs","totems-monoliths"],
  points=[("Branded hoardings","Printed in-house and fitted fast."),("Site safety","Clear, durable safety boards."),("Accredited","CSCS, IPAF, PASMA and Constructionline accredited.")]),
 dict(slug="commercial", name="commercial", blurb="Workplace branding, wayfinding and safety signs.", img="rolls", icon="79390e70e1d34d88b0248554747aa146",
  title="Commercial & Office Signage",
  intro="Enhance your workplace with professional signage, from building signs and reception lettering to wayfinding and safety signs, tailored to your business environment.",
  gallery=["ig_tms","ig_pantera","ig_wrgroup","ig_atom","rolls","rolls_int","jaymac","rds","bankhouse","catalyst_l"],
  types=["3d-letters","building-signs","flat-cut-letters","wayfinding"],
  points=[("Reception to roofline","One team for the building sign and the reception wall."),("Brand-accurate","Colour-matched finishes and materials."),("Multi-site","Consistent signage across several sites.")]),
 dict(slug="retail", name="retail", blurb="Storefronts and in-store displays that pull customers in.", img="harbro", icon="67e60055c6a34be9b24852f28a1089c3",
  title="Shop Signs & Retail Signage",
  intro="Attract customers with striking signage that shows off your brand, from storefront signs to promotional displays that lift your retail space.",
  gallery=["ig_companyshop","ig_storeentrance","ig_workwear","ig_smartvape","harbro","works","tesco","totW","aldi_bld","lfBm"],
  types=["backlit-panels","projecting-signs","lightboxes-flex-faces","totems-monoliths"],
  points=[("Kerb appeal","Fascias and projecting signs that stop passers-by."),("Promotions","Window and in-store print turned round fast."),("Retail parks","Totems and large-scale flex faces.")]),
 dict(slug="hospitality-leisure", name="hospitality & leisure", blurb="Bars, gyms, venues and spas: signs that set the mood.", img="sunclub", icon="e71f0723c3bf41a088216609768ab0bd",
  title="Bar, Restaurant & Leisure Signage",
  intro="For bars, restaurants, gyms, spas and venues, our signage blends function and style, setting the mood and guiding guests from the street to their seat.",
  gallery=["ig_dubliner","ig_court","ig_gavroche","ig_leancuisine","ig_queenshead","seventy3","dog","cork_night","vault","neonB","vertu_night","sunclub","glow"],
  types=["backlit-panels","3d-letters","neon-led-neon","projecting-signs"],
  points=[("Made to be seen at night","Backlit panels, halo-lit letters and LED neon."),("Brand-led","Signs that match your interior design."),("Venues of every size","From one bar to an arena.")]),
 dict(slug="hair-beauty", name="hair & beauty", blurb="Exterior and in-salon signs with your brand's personality.", img="kloset", icon="25fce8e719e44c75a0c17b1db32eeaee",
  title="Salon Signs for Hair & Beauty",
  intro="Create a stylish, welcoming space with signage that reflects your brand's personality, from exterior signs to in-salon displays that win your clients over.",
  gallery=["ig_zen","ig_pudes","kloset","glow","welcome_neon","glow_night"],
  types=["3d-letters","neon-led-neon","backlit-panels","vinyl-wall-graphics"],
  points=[("Statement walls","LED neon and mirrored letters made for photos."),("Shopfronts","Fascias that match your interior."),("Small details","Window vinyls and treatment-room signs.")]),
 dict(slug="transport", name="transport", blurb="Durable, high-visibility signs and fleet graphics.", img="vanPark", icon="3f6e69f7d28a4952b25f79200d72f670",
  title="Transport Signage & Fleet Graphics",
  intro="Inside busy transport hubs, clear signage is essential. We provide durable, high-visibility signs and fleet graphics that help travellers find their way.",
  gallery=["ig_salto","ig_park2","ig_pamper_trailer","vanPark","vanYellow","vanFabio"],
  types=["vehicle-graphics","wayfinding","digital-large-format-print"],
  points=[("Fleet livery","Consistent graphics across mixed vehicles."),("High visibility","Signs designed to read at a glance."),("Durable","Materials chosen for heavy use.")]),
 dict(slug="health-safety", name="health & safety", blurb="Clear, durable safety signs that keep premises compliant.", img="carpark", icon="099b1bbf6a3341969551b59b4dd00d1e",
  title="Health & Safety Signs",
  intro="Stay compliant with high-quality safety signage. Our durable, clear signs help you meet regulations and keep your premises safe and secure.",
  gallery=["carpark","fireExit","nhs_dir"],
  types=["wayfinding","vinyl-wall-graphics","digital-large-format-print"],
  points=[("Compliance","Signs that meet current safety standards."),("Durable","Built for car parks, warehouses and sites."),("Floor graphics","Anti-slip floor markings and fire exit routes.")]),
]

PROJECTS = [
 dict(name="Bar Seventy Three", k="seventy3", label="Backlit panel", url="projects/seventy-three"),
 dict(name="Vertu Motors Arena", k="vertu", label="Building signage", url="projects/vertu-motors"),
 dict(name="glow.", k="glow", label="Acrylic letters on a panel", url="projects/glow."),
 dict(name="NHS CDC", k="nhs", label="Fabricated letters on a panel", url="projects/nhs-community-diagnostics-centre"),
 dict(name="Newcastle University", k="ncl", label="Illuminated building sign", url="projects/newcastle-university"),
 dict(name="Aldi & Jaymac", k="aldi", label="Building signage", url="projects/aldi-warehouse"),
 dict(name="The Catalyst", k="catalyst", label="Building signage", url=None),
 dict(name="Cork & Coffee", k="cork", label="Fascia signage", url="projects/cork-%26-coffee"),
]
REEL_A = ["seventy3","works","vertu","neonB","dog","bowmer","arv","woodham","tesco","vault","ncl"]
REEL_B = ["glow","harbro","cork","nhs","vanPark","rolls","sunclub","kloset","alwinton","catalyst","w_red_g"]

# ===================== Revisions from Mak, 12 Nov =====================
def _new(n, c, p="50% 50%"): return ("new:"+n, c, p)
IMG.update({
 "n_jet2": _new("jet2-halo","Jet2: halo-lit fabricated 3D letters"),
 "n_jet2glow": _new("jet2-halo-glow","Jet2 letters: the halo glow up close"),
 "n_thatype": _new("thatype","Thatype: halo-lit script letters"),
 "n_court": _new("the-court","The Court, Durham: gold 3D letters"),
 "n_byre": _new("byre","BYRE: illuminated 3D letters"),
 "n_tribeca": _new("tribeca","Tribeca: 3D letters on a fascia"),
 "n_fitt": _new("fitt","Fitt: 3D letters"),
 "n_superpower": _new("superpower","Superpower: illuminated 3D letters"),
 "n_superpower_wide": _new("superpower-wide","Superpower shopfront"),
 "n_renew_close": _new("renewable-close","Renewable Energy: 3D letters on timber cladding"),
 "n_renew_bld": _new("renewable-building","Renewable Energy building sign"),
 "n_grainger": _new("grainger-market","Grainger Market: gold 3D letters"),
 "n_murphys": _new("dirty-murphys","Dirty Murphys: 3D letters"),
 "n_aqua": _new("aqua-tcg","Aqua TCG: illuminated letters"),
 "n_kosmic": _new("kosmic-kingdom","Kosmic Kingdom: high level sign"),
 "n_kosmic_close": _new("kosmic-kingdom-close","Kosmic Kingdom sign detail"),
 "n_griffin": _new("griffin-court","Griffin Court: high level letters"),
 "n_griffin_up": _new("griffin-court-up","Griffin Court letters from below"),
 "n_fitt_int": _new("fitt-interior","Fitt interior"),
 "n_jet2_ceiling": _new("jet2-ceiling","Jet2: printed LED ceiling panels"),
 "fence2": ("b37986290e6c491181d6f5316116596c~mv2.jpg","Printed mesh fence banner","50% 50%"),
})
def _cap(k, c):
    i, _, p = IMG[k]; IMG[k] = (i, c, p)
_cap("fira","Fika: flat-cut letters")
_cap("ig_pantera","Pantera Advisory Group: flat-cut foamex logo and letters")
_cap("ig_wrgroup","WR Group: fabricated 3D letters on brick")
_cap("bankhouse","Bank House: wall vinyl")
_cap("urban","eat @ urban: wayfinding wall graphic")
_cap("ig_durham","Durham University and Microsoft: flat-cut letters")
_cap("ig_workwear","Workwear Express: flat-cut letters")
_cap("ig_kier","Kier feather flag")
_cap("nhs_bld","NHS Community Diagnostic Centre: 3D letters on a panel")
_cap("ig_nhs_night","NHS Community Diagnostic Centre: 3D letters lit at night")
_cap("ig_dubliner","The Dubliner: LED neon")
_cap("st_welcome","Bar Seventy Three: backlit panel")

T = {t["slug"]: t for t in TYPES}

t = T["3d-letters"]
t["photos"] = ["n_jet2","vault","rds","dog","cell","n_court","n_thatype","nhs_bld","ig_nhs_night","ig_wrgroup","n_byre","n_tribeca",
               "n_fitt","n_superpower","n_renew_close","n_grainger","n_murphys","n_aqua","n_jet2glow","ig_maple","ig_zen","ig_atom",
               "catalyst_l","ig_goldscript","ig_mango","ig_stephenson"]
t["spec"][0] = ["Types","Fabricated (aluminium, stainless, copper or brass), Komacel, acrylic"]
t["spec"].insert(2, ["Metals","Copper and brass, including aged finishes"])
t["variants"][0]["p"] = "Built from a metal face and folded returns in aluminium, stainless steel, copper or brass, including aged finishes. The most versatile option, and the one to choose for large or high-level letters."
t["variants"][0]["tags"] = ["face-lit (rim & return)","halo-lit","non-lit","copper & brass"]
t["notes"] = ["Every letter can go straight onto the wall on stand-off locators, or onto a panel when the wall isn't suitable or you want a backdrop.",
              "The Vault: fabricated, halo-lit letters on a panel. The Cell: halo-lit stainless steel. Jet2: halo-lit fabricated letters straight onto the wall.",
              "Fabricated letters also come in copper and brass, including aged finishes.",
              "Not sure which suits your budget? We'll mock up the options on a photo of your building."]
t["desc"] = "Letters with real depth that stand proud of the wall. We make three kinds: fabricated metal letters (aluminium, stainless, copper or brass), Komacel letters and acrylic letters, fixed straight to the wall on stand-off locators or mounted on a panel."

t = T["backlit-panels"]
t["photos"] = ["st_welcome","ig_codcrust"]; t["hero"] = "st_welcome"

t = T["flat-cut-letters"]
t["photos"] = ["ig_durham","fira","ig_pantera","ig_workwear"]; t["hero"] = "ig_durham"
t["spec"][0] = ["Materials","Acrylic, foamex, aluminium composite, stainless steel"]
t["notes"] = ["Flat-cut letters cost less than 3D letters and suit interiors especially well.",
              "Pantera Advisory Group is cut from foamex, a light, rigid PVC board."]

t = T["building-signs"]
t.update(slug="high-level-signs", name="High level signs", label="high level signs", code="OS-HL",
  seo_title="High Level Signs: Large Building Signage",
  meta="Large, high-level building signs surveyed, fabricated and installed by Onesign's own IPAF and PASMA trained crews: fabricated letters, panels, printed Dibond and vinyl-wrapped panels.",
  hero="rolls",
  photos=["rolls","n_kosmic","vertu_night","n_griffin","woodham","aldi_bld","n_renew_bld","ig_urgent","ig_tms","ig_companyshop","ig_nhs_cumbria","n_griffin_up","glow"],
  desc="Large signs high on the side of buildings: big fabricated letters, letters on panels, digitally printed Dibond and vinyl-wrapped fabricated panels. Surveyed, engineered and fitted from powered access by our own crews.",
  notes=["Rolls-Royce: large high-level letters on cladding.",
         "Woodham Academy: a large building sign in digitally printed Dibond.",
         "Aldi: a large digitally printed vinyl applied to a fabricated panel."])

T["neon-led-neon"]["photos"] = ["neonB","ig_dubliner","ig_leancuisine","welcome_neon","ig_pudes","ig_neon_red","rascals_neon","ig_neon_yellow","neonA","neonC","neonD"]

t = T["vinyl-wall-graphics"]
t["photos"] = ["bankhouse","ig_lineart_install","nhs_skyline","ig_lineart","arv","univinyl","w_truetest","ig_jaymac_wall","ig_craicn"]
t["hero"] = "bankhouse"; t["variants"][0]["img"] = "bankhouse"

t = T["digital-large-format-print"]
t["photos"] = ["n_jet2_ceiling","bowmer","ig_ocado","lfPosters","lfPrint"]; t["hero"] = "n_jet2_ceiling"
t["desc"] = "Big, bold, colour-matched print from our own wide-format printers: hoardings, printed LED ceiling panels, posters, window graphics and display boards, printed and finished in-house so turnaround stays fast."

T["wayfinding"]["photos"].insert(4, "urban")

t = T["vehicle-graphics"]
t["photos"] = ["ig_park2","vanYellow"]; t["hero"] = "ig_park2"

FLAGS = dict(slug="flags-banners", name="Flags & banners", label="flags & banners", code="OS-FL",
  seo_title="Feather Flags, Mesh Banners & Pop-Up Banners",
  meta="Printed feather flags, mesh fence banners, PVC banners and pop-up banners from Onesign's in-house print room in Gateshead.",
  hero="ig_kier", photos=["ig_kier","fence_banner","fence2"],
  desc="Printed flags and banners for events, sites and shopfronts: feather and teardrop flags, mesh fence banners, PVC banners and pop-up banners, printed in-house and supplied with the hardware to put them up.",
  ideal=["events","construction sites","sports clubs","promotions"],
  spec=[["Flags","Feather and teardrop flags with poles and bases"],["Mesh banners","Wind-permeable mesh for fences and scaffolding"],
        ["PVC banners","Hemmed and eyeleted for walls and railings"],["Pop-ups","Pull-up and pop-up display banners"],["Print","Full colour, in-house"]],
  variants=[], notes=["Mesh banners let wind pass through, so they suit site fences and scaffolding."],
  faq=[("Do flags come with bases?","Yes. We supply poles and a choice of ground spike, cross base or weighted base."),
       ("Which banner suits a building site fence?","Mesh. It lets the wind through, so it stays put and doesn't strain the fence.")])
TYPES = [t for t in TYPES]
TYPES.insert([x["slug"] for x in TYPES].index("digital-large-format-print")+1, FLAGS)

S = {s["slug"]: s for s in SECTORS}
for s in SECTORS:
    s["types"] = ["high-level-signs" if x=="building-signs" else x for x in s["types"]]
    s["gallery"] = ["st_welcome" if x=="seventy3" else x for x in s["gallery"]
                    if x not in ("lfBm","hoarding","ig_salto","ig_pamper_trailer","vanFabio","vanPark","ig_park")]
S["hospitality-leisure"]["gallery"] = ["st_welcome","ig_codcrust","n_thatype","ig_dubliner","dog","n_murphys","n_grainger","ig_court","vault","ig_gavroche","ig_leancuisine","vertu_night","sunclub","n_fitt_int"]
S["retail"]["gallery"] = ["n_superpower_wide","n_kosmic","ig_companyshop","harbro","works","ig_smartvape","tesco","totW","aldi_bld"]
S["transport"]["gallery"] = ["ig_park2","vanYellow"]
S["construction"]["types"] = ["digital-large-format-print","flags-banners","high-level-signs","totems-monoliths"]

for p in PROJECTS:
    if p["k"] == "seventy3": p["k"] = "st_welcome"; p["label"] = "Backlit panel"
    if p["k"] == "nhs": p["label"] = "3D letters on a panel"
REEL_A = ["st_welcome" if k=="seventy3" else k for k in REEL_A]
REEL_A = ["n_jet2" if k=="vertu" else k for k in REEL_A]
REEL_B = ["n_thatype" if k=="vanPark" else k for k in REEL_B]

# ===================== Revisions from Mak, 12 Nov (2) =====================
_cap("ig_corner","Blacks Corner projecting sign")
_cap("rascals_proj","Rascals light box")
_cap("ig_neon_red","BYRE: 'Join the herd' LED neon")
T = {t["slug"]: t for t in TYPES}
t = T["3d-letters"]
t["photos"] = ["n_jet2","vault","rds","dog","ig_zen","n_court","n_thatype","n_byre","n_grainger","nhs_bld","ig_nhs_night","ig_wrgroup",
               "n_tribeca","n_fitt","n_superpower","n_renew_close","n_murphys","n_aqua","n_jet2glow","ig_maple","ig_atom",
               "catalyst_l","ig_goldscript","ig_mango","ig_stephenson"]
t["hero"] = "n_thatype"
t["variants"][0]["img"] = "n_jet2"
t["notes"][1] = "The Vault: fabricated, halo-lit letters on a panel. Jet2: halo-lit fabricated letters straight onto the wall. Dog & Parrot: inset brass Komacel."
t = T["projecting-signs"]
t["photos"] = ["ig_corner","ig_queenshead","ig_lane","works"]; t["hero"] = "ig_corner"
t = T["lightboxes-flex-faces"]
t["photos"] = ["ig_gavroche","n_kosmic","rascals_proj","n_kosmic_close"]
t["variants"][1]["img"] = "n_kosmic"
t["notes"] = ["Choose a light box for smaller, crisp signs and a flex face once the sign gets big.",
              "Kosmic Kingdom is a large flex face: one seamless printed skin across the whole frame."]
t = T["high-level-signs"]
t["photos"] = [k for k in t["photos"] if not k.startswith("n_kosmic")]
T["neon-led-neon"]["photos"] = ["neonB","ig_dubliner","ig_neon_red","ig_leancuisine","welcome_neon","ig_pudes","rascals_neon","ig_neon_yellow","neonA","neonC","neonD"]

S = {s["slug"]: s for s in SECTORS}
S["retail"]["gallery"] = [k for k in S["retail"]["gallery"] if k!="ig_smartvape"]
S["retail"]["img"] = "n_superpower_wide"
S["hospitality-leisure"]["img"] = "n_thatype"
S["commercial"]["img"] = "n_jet2"
S["commercial"]["gallery"] = ["n_jet2","rolls","n_renew_close","rolls_int","jaymac","rds","ig_wrgroup","ig_tms","catalyst_l"]

for p in PROJECTS:
    if p["k"] == "catalyst": p.update(name="Thatype", k="n_thatype", label="Halo-lit script letters", url=None)
    if p["k"] == "cork": p.update(name="Superpower", k="n_superpower_wide", label="Illuminated 3D letters", url=None)
    if p["k"] == "glow": p.update(name="Jet2", k="n_jet2", label="Halo-lit 3D letters", url=None)
REEL_A = ["st_welcome","n_court","works","vertu","neonB","n_byre","dog","n_kosmic","bowmer","arv","woodham","n_griffin","tesco","vault","ncl"]
REEL_B = ["n_jet2","glow","harbro","n_grainger","cork","nhs","n_superpower_wide","rolls","sunclub","n_thatype","kloset","n_renew_close","alwinton","catalyst","w_red_g"]

# ===================== Revisions from Mak, 13 Nov =====================
def _w(i, c, p="50% 50%"): return (i, c, p)
IMG.update({
 "st_sign": _w("8c2d2ed5093546149f53cd0ae455987c~mv2.jpg", "Bar Seventy Three: backlit panel"),
 "st_design": _w("aa5adf7f99b5420d9f484161b5cfe58d~mv2.jpg", "Artwork set up for production"),
 "ws_cnc": _w("1e7f8b60efbd46ce877f5f9dc46b25d7~mv2.jpg", "CNC routing"),
 "ws_cnc2": _w("7d3ef632699642aa9a3c414f8b149e11~mv2.jpg", "CNC routing"),
 "ws_weld": _w("52f2e897853b4b259826031f64646550~mv2.jpg", "Welding"),
 "ws_weld2": _w("df09a6da3107457d8f32e71b5db091b2~mv2.jpg", "Welding"),
 "ws_cut": _w("13624282660241bf96bf94b5ac232cd0~mv2.jpg", "Cutting metal"),
 "ws_spray": _w("66ed4f69326f4cb895c77054f9f2e136~mv2.jpg", "Spray finishing"),
 "ws_assembly": _w("dae564f29df34dae85dee34cae1a2e2c~mv2.jpg", "Assembly"),
 "ws_finish": _w("984f85d15fcc48388b9d0ef29f04b079~mv2.jpg", "Hand finishing"),
 "ws_built": _w("3e908f32ee0b4c2d9e77f9ba78bb6796~mv2.jpg", "A finished panel in the workshop"),
 "ws_install": _w("4400b21f555e49f79b0b929dda95a62c~mv2.jpg", "Installation"),
 "ws_print": _w("58fa4b8477b84722b984c5dd309b9902~mv2.jpg", "Flatbed printing"),
 "vg_tree": _w("29362c7056c94f13acc85fcda79df655~mv2.jpg", "Tree wall graphic"),
 "vg_birds": _w("b01038205a624f8584e800ce02b05127~mv2.jpg", "Feature wall graphics"),
 "vg_workhard": _w("0a4696f3d7d7460d9cad83341a2eebb0~mv2.jpg", "Woodham Academy: 'Work Hard' wall vinyl"),
 "way_g": _w("2e6fa9d91d184d57a366c65f8f9585a7~mv2.jpg", "Woodham Academy: floor identifier and directory"),
 "way_1": _w("0a8a02bcefd74eef9e74b1b16f50c8c0~mv2.jpg", "Woodham Academy: level 1 wayfinding"),
 "way_2": _w("3c7355517aac405996482e6b9b55a652~mv2.jpg", "Woodham Academy: level 2 wayfinding"),
 "way_dir": _w("4a3ebc2a8360406691fcc18edeb80af9~mv2.jpg", "Woodham Academy: directory sign"),
 "print_fruit": _w("27e10e97e37e4f57be72ae72c98a32be~mv2.jpg", "Large-format in-store graphics"),
 "cork_dusk": _w("f6186d4a72b54968b137c4fb3a170500~mv2.jpg", "Cork & Coffee: lit fascia at dusk"),
 "hc_cdc": _w("318f8b3f9c7d4e2f8fd1d659d9d12888~mv2.jpg", "NHS Community Diagnostic Centre: entrance signs"),
 "hc_cdc2": _w("75d8810ff05344edb74d4e4bf4d440d2~mv2.jpg", "NHS Community Diagnostic Centre: reception signs"),
 "glow_int": _w("ee64cba746784ca48e291695d52f781a~mv2.jpg", "glow.: 3D letters inside the salon"),
 "glow_int2": _w("1c22fa9d23b942c89d11f4f3bef422b9~mv2.jpg", "glow. salon interior"),
 "totem_ww": _w("e963f888b64f40cb841ecc48026c4fbd~mv2.jpg", "Workwear Express totem"),
})
_cap("hoarding", "Printed site hoarding")
_cap("glow", "glow.: 3D letters on a fascia panel")
T = {t["slug"]: t for t in TYPES}

t = T["3d-letters"]
t["photos"] = [k for k in t["photos"] if k not in ("glow",)]
t["photos"][5:5] = ["glow", "glow_int"]

t = T["high-level-signs"]
t["photos"] = [k for k in t["photos"] if k not in ("glow", "ig_nhs_cumbria")]

t = T["backlit-panels"]
t["hero"] = "st_sign"; t["photos"] = ["st_sign", "st_welcome", "ig_codcrust", "ws_built"]

t = T["vinyl-wall-graphics"]
t["hero"] = "vg_tree"
t["photos"] = ["vg_tree", "bankhouse", "vg_birds", "vg_workhard"] + [k for k in t["photos"] if k != "bankhouse"]

t = T["digital-large-format-print"]
t["hero"] = "hoarding"
t["photos"] = ["hoarding", "n_jet2_ceiling", "print_fruit", "bowmer", "ig_ocado", "lfPosters", "lfPrint"]

t = T["totems-monoliths"]
t["hero"] = "totem_ww"
t["photos"] = ["totem_ww"] + [k for k in t["photos"] if k != "totem_ww"]

t = T["wayfinding"]
t["hero"] = "way_g"
t["photos"] = ["way_g", "way_1", "way_2", "way_dir"] + [k for k in t["photos"] if k not in ("way_g",)]

S = {s["slug"]: s for s in SECTORS}
S["hair-beauty"]["img"] = "n_thatype"
S["hair-beauty"]["gallery"] = ["n_thatype", "glow", "glow_int", "glow_int2"] + [k for k in S["hair-beauty"]["gallery"] if k not in ("glow",)]
S["hospitality-leisure"]["img"] = "cork_dusk"
S["hospitality-leisure"]["gallery"] = ["cork_dusk"] + [k for k in S["hospitality-leisure"]["gallery"] if k != "n_thatype"]
S["transport"]["img"] = "ig_park"
S["transport"]["gallery"] = ["ig_park", "ig_park2", "vanYellow"]
S["healthcare"]["img"] = "hc_cdc"
S["healthcare"]["gallery"] = ["hc_cdc", "hc_cdc2"] + S["healthcare"]["gallery"]

for p in PROJECTS:
    if p["k"] == "st_welcome": p["k"] = "st_sign"

MACHINES = [
 ("Piranha CNC router", "High-precision routing for acrylic, aluminium composite, foamex and timber: letters, panels and complex shapes."),
 ("Ermak brake press", "Precision metal bending for fabricated letters, trays, totems and structural signage."),
 ("New laser cutter", "Our newest machine: precise, clean-edged cutting for metal and acrylic letters and intricate detail."),
 ("Boxford precision cutter", "Fine engraving and cutting for intricate designs and small detailed parts."),
 ("HP Latex R1000", "Large-format printing at up to 1200 x 1200 dpi, with water-based inks, straight onto board, acrylic, metal, timber and vinyl."),
 ("Epson SureColor", "Ultra-high-quality roll printing for vinyl graphics, wall graphics and print."),
 ("Mimaki cutting plotter", "Precision-cut vinyl lettering, shapes and application-ready graphics."),
 ("Rollsroller flatbed applicator", "Bubble-free application of printed graphics and vinyl onto panels."),
]
WORKSHOP = ["st_design", "ws_cnc", "ws_cut", "ws_weld", "ws_spray", "ws_assembly", "ws_finish", "ws_print", "ws_built", "ws_weld2", "ws_cnc2", "ws_install"]

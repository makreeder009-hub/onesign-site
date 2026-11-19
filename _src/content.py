# -*- coding: utf-8 -*-
"""Copy and data for the page families added in v2. Pure data: no imports from build.py.
Facts come from Mak, the old website's project pages and Onesign's own Instagram captions.
Anything not confirmed is left out rather than guessed."""

PHONE = "0191 487 6767"
REVIEWS = dict(score="4.9", count=72,
               url="https://www.google.com/maps/search/?api=1&query=Onesign+%26+Digital+Princesway+North+Gateshead+NE11+0TU")

# ---------------------------------------------------------------- case studies
# old = path on the previous website, redirected to the new page at launch
CASES = [
 dict(slug="bar-seventy-three", old="/projects/seventy-three", name="Bar Seventy Three", where=None,
      sector="hospitality-leisure", types=["backlit-panels"], hero="st_sign",
      label="Backlit panel",
      lede="A one-off backlit panel, cut to the outline of the logo and built entirely in our Team Valley factory.",
      brief="Bar Seventy Three wanted a bold sign that matched an energetic brand and worked as hard at night as it does in daylight. Nothing off the shelf would do: the sign had to be completely bespoke.",
      made=[("Fabricated front and back panels", "The sign is built in layers that house the lighting, so the finished piece looks like one clean object with no visible fixings."),
            ("Aperture-cut lettering", "We cut the lettering out of the front panel and backfilled it with white acrylic, so only the letters light up."),
            ("Printed vinyl accents", "Selected letter faces carry a digitally printed pattern that picks up the bar's branding."),
            ("LED illumination", "Internal LEDs light the lettering evenly and keep running costs low.")],
      result="A sign shaped like the brand itself, readable from down the street after dark.",
      photos=["st_sign", "st_welcome", "st_front", "st_close"],
      making=["st_design", "ws_cnc", "ws_cut", "ws_weld", "ws_spray", "ws_assembly", "ws_finish", "ws_built", "st_fit"]),
 dict(slug="newcastle-university", old="/projects/newcastle-university", name="Newcastle University", where="Newcastle upon Tyne",
      sector="education", types=["high-level-signs", "wayfinding", "vinyl-wall-graphics", "totems-monoliths"], hero="hero",
      label="Campus signage partner",
      lede="More than 15 years of building signs, wayfinding and graphics across the university's campuses.",
      brief="A university campus never stands still. New buildings open, departments move and thousands of new students arrive every September needing to find their way. Newcastle University needed one signage partner who knew the estate and could keep the brand consistent across it.",
      made=[("High-level building signs", "Fabricated external signs on key university buildings, visible across the city."),
            ("Internal wayfinding", "Directional signs that help students, staff and visitors get around each building."),
            ("External wayfinding", "Totems and entrance monoliths that guide people between buildings."),
            ("Printed window vinyls", "Decorative, digitally printed window graphics that bring colour and branding into teaching spaces."),
            ("Printed wall art", "Large-format wall graphics that carry the university's values into corridors and common areas.")],
      result="A partnership that has lasted over 15 years, with signage that reads as one family across the estate.",
      photos=["hero", "ncl", "uni_totem", "uni_entry", "univinyl"], making=[]),
 dict(slug="nhs-community-diagnostic-centre", old="/projects/nhs-community-diagnostics-centre", name="NHS Community Diagnostic Centre", where="Metrocentre, Gateshead",
      sector="healthcare", types=["backlit-panels", "3d-letters", "vinyl-wall-graphics", "wayfinding"], hero="hc_cdc",
      label="Healthcare signage scheme",
      lede="A full signage scheme for a diagnostic centre inside one of the UK's biggest shopping centres.",
      brief="Patients arrive at the Community Diagnostic Centre through the Metrocentre, so the signs had to do two jobs: stand out among the shopfronts, and stay calm, clear and unmistakably NHS once people are inside.",
      made=[("Illuminated entrance sign", "An aperture-cut, illuminated sign at the Metrocentre entrance so visitors can find the centre from the mall."),
            ("High-level 3D letters", "Fabricated letters powder-coated in NHS colours, readable from a distance outside the building."),
            ("North East wall graphics", "Printed vinyls run along the interior walls with silhouettes of regional landmarks, which makes a clinical space feel local and welcoming."),
            ("Directional signs", "Projecting and wall-mounted signs guide patients and staff through the centre.")],
      result="A clear route from the mall entrance to the right room, in a space that feels local as well as clinical.",
      photos=["hc_cdc", "nhs", "nhs_bld", "ig_nhs_night", "hc_cdc2", "nhs_skyline", "nhs_dir", "nhs_proj"], making=[]),
 dict(slug="woodham-academy", old="/projects/woodham-academy", name="Woodham Academy", where="Newton Aycliffe, County Durham",
      sector="education", types=["wayfinding", "vinyl-wall-graphics", "high-level-signs", "totems-monoliths"], hero="woodham",
      label="Whole-school signage package",
      lede="Every sign in a brand-new school, delivered with main contractor Galliford Try.",
      brief="Woodham Academy moved into a completely new building in Newton Aycliffe. Working with Galliford Try, we supplied the whole signage package so that the school opened with its branding, wayfinding and safety signs in place.",
      made=[("External building sign", "A digitally printed Dibond sign that sits with the architecture and carries the school's branding."),
            ("Values in vinyl", "Motivational quotes and artwork in cut and printed vinyl throughout the school."),
            ("Wayfinding", "Colour-coded floor identifiers and directories so students and visitors can find their way."),
            ("Classroom door signs", "A modular sign system showing class and teacher names, easy to update each year."),
            ("Safety and parking signs", "Road safety and traffic signs across the site."),
            ("Entrance totem", "External totem and directional signs at the school entrance.")],
      result="One coordinated family of signs, in place for the first day of term.",
      photos=["woodham", "w_ext_dir", "way_g", "way_dir", "w_red_g", "vg_workhard", "w_truetest", "w_nevergiveup"], making=[]),
 dict(slug="vertu-motors-arena", old="/projects/vertu-motors", name="Vertu Motors Arena", where="Newcastle upon Tyne",
      sector="hospitality-leisure", types=["high-level-signs", "3d-letters", "vinyl-wall-graphics"], hero="vertu_night",
      label="Illuminated building signage",
      lede="High-level illuminated letters for the home of the Newcastle Eagles.",
      brief="The Vertu Motors Arena is home to the Newcastle Eagles basketball team and needed external signage to match: big enough to read from a distance, and lit so the building is recognisable on game nights.",
      made=[("High-level face-illuminated letters", "Large fabricated letters on the side of the building, lit from inside so the name carries at night."),
            ("Entrance letters", "A smaller set of face-illuminated letters above the main reception entrance."),
            ("Window vinyls", "Branded window graphics at ground level.")],
      result="The arena is easy to pick out day and night.",
      photos=["vertu_night", "vertu"], making=[]),
 dict(slug="rolls-royce", old="/projects/rolls-royce", name="Rolls-Royce", where=None,
      sector="commercial", types=["high-level-signs", "3d-letters", "digital-large-format-print"], hero="rolls",
      label="Building, interior and safety signage",
      lede="Building signs, stainless steel lettering and an animated safety board for a world-renowned engineering company.",
      brief="Rolls-Royce needed a signage package that reinforced the brand across its site and also did practical work for health and safety. Every element had to meet the standard of finish the name demands.",
      made=[("Animated safety board", "An animated safety board, designed in-house, that puts health and safety messages in front of employees and visitors."),
            ("Fabricated stainless steel letters", "Small fabricated stainless steel letters and logos inside the facility."),
            ("Printed hoarding boards", "Large printed boards that show off the engineering work done on site."),
            ("Building signage", "High-level external signs that identify the facility.")],
      result="A consistent, premium finish from the building exterior to the shop floor.",
      photos=["rolls", "rolls_close", "rolls_int"], making=[]),
 dict(slug="aldi-jaymac-warehouse", old="/projects/aldi-warehouse", name="Aldi & Jaymac Solutions", where="County Durham",
      sector="commercial", types=["high-level-signs", "flat-cut-letters", "vinyl-wall-graphics"], hero="aldi",
      label="High-level warehouse signage",
      lede="Large-scale exterior signs for two brands on one new warehouse, plus the office interior.",
      brief="Aldi and Jaymac Solutions both needed a brand presence on a new warehouse facility in County Durham. The signs had to be big, accurate to each brand and built to stand up to the weather for years.",
      made=[("Aldi panels", "Folded aluminium panels with digitally printed vinyl on the face, which keeps Aldi's colours crisp at a very large size."),
            ("Jaymac high-level signs", "Aluminium composite panels, laser-cut and digitally printed: durable, highly visible and cost-effective."),
            ("Office interior", "Flat-cut logo and lettering, door vinyls and a wall graphic for the Jaymac offices."),
            ("Installed at height", "Fitted by our own IPAF-trained installers.")],
      result="Two brands, clearly signed on one building, with materials chosen for a long life and little maintenance.",
      photos=["aldi", "aldi_bld", "jaymac", "install", "n_jaymac_logo", "n_quality", "n_jaymac_door", "ig_jaymac_wall"], making=[]),
 dict(slug="northgate-hospital", old="/projects/northgate-hospital", name="Northgate Hospital", where="Morpeth, Northumberland",
      sector="healthcare", types=["totems-monoliths", "wayfinding", "vinyl-wall-graphics", "3d-letters"], hero="ng_totem",
      label="Hospital wayfinding",
      lede="External totems, ward lettering and wall art across a large hospital site, working with NTW Solutions.",
      brief="Northgate Hospital is a large site with many separate wings. Patients, staff and visitors needed a consistent system to find their way from the entrance to the right building, and each wing needed its own identity.",
      made=[("External totems", "Large totems at key points direct visitors as they arrive and move around the site."),
            ("Fabricated wing lettering", "Each wing is named in large fabricated letters, so buildings are easy to identify."),
            ("Window graphics", "Custom window vinyls add privacy without making spaces feel closed in."),
            ("Wall graphics and wooden wall art", "Each wing has its own wall graphics and wooden artwork, designed around its purpose.")],
      result="One consistent sign system across the whole site.",
      photos=["ng_totem", "alwinton", "sycamore", "wardDir", "courtyard", "northgate"], making=[]),
 dict(slug="cork-and-coffee", old="/projects/cork-%26-coffee", name="Cork & Coffee", where="Seaham, County Durham",
      sector="hospitality-leisure", types=["3d-letters", "vinyl-wall-graphics"], hero="cork_dusk",
      label="3D letters and interior branding",
      lede="A coffee house by day and a wine bar by night, with signage made to suit both.",
      brief="Cork & Coffee in Seaham changes character through the day. The signage had to feel warm for the morning coffee crowd and elegant for the evening, so we designed a package that runs from the shopfront to the bar top.",
      made=[("Komacel 3D letters", "Shopfront letters in Komacel with inset mirrored gold acrylic faces, halo-lit after dark."),
            ("Window vinyls", "Branded window graphics that add privacy and atmosphere."),
            ("Aged brass bar details", "An aged brass countertop and wine rack, made with Halman Thompson."),
            ("Engraved chopping boards", "Branded serving boards for the charcuterie menu.")],
      result="The brand carries through from the street to the table.",
      photos=["cork_dusk", "cork", "cork_night"], making=[]),
 dict(slug="glow-tanning", old="/projects/glow.", name="glow.", where=None,
      sector="hair-beauty", types=["flat-cut-letters", "3d-letters", "wayfinding"], hero="glow_night",
      label="Salon signage package",
      lede="Exterior lettering, interior branding and illuminated room numbers for a new luxury tanning studio.",
      brief="As a new studio, glow. needed signage that announced a premium brand from the street and kept the same look all the way to the tanning rooms.",
      made=[("Fascia lettering", "Bold lettering on the black fascia, lit so the studio stands out after dark."),
            ("Interior branding", "A large wall-mounted logo and a branded reception desk."),
            ("Illuminated room numbers", "Each tanning room has an illuminated number made to match the exterior sign.")],
      result="One consistent look from the pavement to the tanning rooms.",
      photos=["glow_night", "glow", "glow_ext", "n_glow_wall", "glow_int", "glow_int2"], making=[]),
 dict(slug="jet2-dawson-sanderson", old=None, name="Jet2 at Dawson & Sanderson", where=None,
      sector="retail", types=["3d-letters", "digital-large-format-print"], hero="n_jet2",
      label="Halo-lit feature wall",
      lede="“Nothing beats Jet2” in fabricated, halo-illuminated letters for a travel agent's feature wall.",
      brief="Travel agent Dawson & Sanderson wanted a feature wall for Jet2 that customers would notice the moment they walked in.",
      made=[("Fabricated aluminium letters", "Each letter is built from aluminium with folded returns and finished in Jet2's colours."),
            ("Halo illumination", "LEDs behind the letters throw a soft glow onto the wall, so the lettering appears to float."),
            ("Printed ceiling panels", "Printed panels for the illuminated ceiling complete the space.")],
      result="A wall that sells the holiday before the brochure comes out.",
      photos=["n_jet2", "n_jet2glow", "n_jet2_ceiling"], making=[]),
 dict(slug="griffin-court", old=None, name="Griffin Court", where="Hebburn, South Tyneside",
      sector="construction", types=["high-level-signs", "3d-letters"], hero="n_griffin",
      label="High-level fabricated letters",
      lede="Fabricated aluminium letters for a new residential development, working with Robertson Group.",
      brief="Griffin Court is a residential development in Hebburn. Main contractor Robertson Group needed the building named in lettering that suited the architecture and would last.",
      made=[("Fabricated aluminium letters", "Bespoke letters fabricated in aluminium and powder-coated."),
            ("Installed at height", "Fitted by our own trained installers.")],
      result="The building has a name that looks like it was always meant to be there.",
      photos=["n_griffin", "n_griffin_up"], making=[]),
 dict(slug="superpower-metrocentre", old=None, name="Superpower", where="Metrocentre, Gateshead",
      sector="retail", types=["3d-letters"], hero="n_superpower_wide",
      label="Face-illuminated 3D letters",
      lede="Face-illuminated lettering for a toy and collectibles store on The Crescent at the Metrocentre.",
      brief="Superpower was opening on The Crescent at the Metrocentre and needed a shopfront sign that carried the energy of the brand.",
      made=[("Face-illuminated letters", "Bespoke built-up letters lit through the face for a bright, even finish."),
            ("Fitted in the mall", "Installed by our own team on The Crescent.")],
      result="A shopfront that stands out in a busy mall.",
      photos=["n_superpower_wide", "n_superpower"], making=[]),
]

# ---------------------------------------------------------------- new case studies (photo shoot, Nov 2026)
_OLD={'n_codcrust_build','kloset','arv','ig_smartvape','n_savoy','n_savoy_ws','n_queens','n_vivana','n_grainger'}
def _k(k): return k if k in _OLD else 'p_'+k
def C(slug,name,where,sector,types,hero,label,lede,brief,made,result,photos,making=()):
    return dict(slug=slug,old=None,name=name,where=where,sector=sector,types=types,hero='p_'+hero,label=label,lede=lede,brief=brief,
                made=made,result=result,photos=[_k(p) for p in photos],making=[_k(m) for m in making])
NEW = [
C("company-shop-group","Company Shop Group",None,"retail",["high-level-signs","wayfinding","vinyl-wall-graphics","digital-large-format-print"],"cs_store",
  "Stores, site and head office",
  "Store fascias, site wayfinding, trolley shelters, in-store graphics and a head office fit-out.",
  "Company Shop Group needed its brand carried consistently from the road to the checkout and into the office: signs that guide members, colleagues and deliveries around busy sites, bright in-store graphics, and an office that feels like the brand.",
  [("Store fascias","Large branded fascia panels and entrance signs on the store buildings."),
   ("Site wayfinding","Post-mounted directional, visitor, parking and speed signs that separate members, colleagues and deliveries."),
   ("Printed trolley shelters and hoardings","Full-colour printed graphics wrapped around trolley shelters and site fencing."),
   ("In-store graphics","Hanging department signs and printed wall panels across the shop floor."),
   ("Head office wall graphics","Printed walls, meeting room numbers and wayfinding throughout the offices.")],
  "One brand, applied the same way across car parks, shop floors and offices.",
  ["cs_store","cs_front","cs_welcome","cs_dir","cs_trolley","cs_hoard","cs_instore","cs_deli","cs_wow","cs_great","cs_cafe","cs_canteen","cs_orange","cs_column","cs_hang"]),
C("sun-tanning","Sun Tanning",None,"hair-beauty",["3d-letters","neon-led-neon","vinyl-wall-graphics","totems-monoliths"],"sun_fascia",
  "Drive-thru salon fit-out",
  "Exterior lettering, a shared drive-thru totem, LED neon and interior branding for a tanning salon.",
  "Sun Tanning opened in a drive-thru unit and needed to be seen from the road and the car park, then carry its brand all the way inside to the tanning rooms.",
  [("3D letters on timber","Built-up letters fixed to the timber-clad fascia."),
   ("Drive-thru totem","Sun's panel on the shared site totem."),
   ("LED neon","Neon logos inside, framed with floral arches."),
   ("Reception and room graphics","A branded reception desk, window vinyls and room lettering.")],
  "A salon that is easy to spot from the road and feels branded in every room.",
  ["sun_fascia","sun_site","sun_totem2","sun_desk","sun_neon","sun_neon2","sun_vip","sun_win"],["sun_m1"]),
C("blacks-corner-tram-shelter","Blacks Corner, Tram Shelter",None,"hospitality-leisure",["3d-letters","projecting-signs"],"bc_letters",
  "Canopy letters and projecting roundel",
  "3D letters along the canopy and a round projecting sign for Blacks Corner at the tram shelter.",
  "Blacks Corner sells cheese, wine and charcuterie. Its signs needed to feel crafted and premium on a historic canopy.",
  [("3D letters on the canopy","Letters fixed along the canopy so the name reads from the street."),
   ("Round projecting sign","A double-sided roundel hung under the canopy.")],
  "A historic shelter with a brand that looks like it has always been there.",
  ["bc_letters","bc_ext","bc_letters2"]),
C("blacks-corner-fenwick","Blacks Corner, Fenwick Food Hall",None,"hospitality-leisure",["projecting-signs","vinyl-wall-graphics"],"bc_bar",
  "Bar signage in a food hall",
  "An illuminated roundel, shelf lettering and a menu panel for the Blacks Corner bar at Fenwick Food Hall.",
  "The bar needed to stand out in a busy food hall and match the Blacks Corner brand.",
  [("Illuminated roundel","A lit projecting roundel above the bar."),
   ("Shelf lettering and menu panel","Lettering across the wine shelving and a printed menu panel.")],
  "A bar you can spot from across the food hall.",
  ["bc_bar","bc_roundel","bc_bar2","bc_shelf","bc_menu","bc_night"]),
C("the-white-swan","The White Swan",None,"hospitality-leisure",["3d-letters"],"ws_front",
  "3D letters on a pub gable",
  "Built-up 3D letters and a swan logo for a pub, fixed to rough-cast render.",
  "The White Swan wanted its name and swan logo to stand proud on the white walls of the building, in a colour that sits with the pub's brand.",
  [("3D letters","Built-up letters finished in the brand colour."),
   ("Swan logo","A layered 3D swan logo above the name."),
   ("Installation on render","Letters fixed to the rough-cast walls from scaffold.")],
  "Clean lettering that reads from the road and suits the building.",
  ["ws_front","ws_close","ws_logo","ws_gable","ws_side"],["ws_m1","ws_m2","ws_m3"]),
C("cod-and-crust","Cod & Crust",None,"hospitality-leisure",["backlit-panels","projecting-signs"],"cc_main",
  "Backlit fascia and projecting sign",
  "An aperture-cut backlit fascia and a projecting sign for a fish, chip and pizza shop.",
  "Cod & Crust needed a fascia that shows the full menu at a glance and lights up for evening trade.",
  [("Backlit fascia panel","Aperture-cut lettering and menu line in the fascia, lit from behind."),
   ("Projecting sign","A double-sided projecting sign with the full logo.")],
  "A takeaway you can spot from the end of the street, day or night.",
  ["cc_main","cc_wide","cc_close","cc_side","cc_proj","cc_street"],["n_codcrust_build"]),
C("kids-kloset","Kids Kloset",None,"retail",["3d-letters","flat-cut-letters"],"kk_front",
  "Shopfront and interior lettering",
  "A 3D letter fascia and matching interior lettering for a luxury childrenswear shop.",
  "Kids Kloset wanted a premium look outside and in, with gold script lettering that matched its brand.",
  [("Fascia panel with 3D letters","Script and capital letters on a panel above the shopfront."),
   ("Interior feature walls","Lettering on the feature walls and counter inside the shop.")],
  "A shop that looks as premium as the clothes it sells.",
  ["kk_front","kk_wide","kk_int","kk_store","kk_int2","kloset"],["kk_m1","kk_m2","kk_m3"]),
C("atom","atom",None,"commercial",["vinyl-wall-graphics","flat-cut-letters","3d-letters"],"at_moss",
  "Office branding",
  "Wall graphics, glass manifestations, a moss wall logo and an illuminated logo for atom's offices.",
  "atom wanted its offices to feel like the brand: bold messages on the walls and the logo wherever people meet.",
  [("Moss wall logo","The logo fixed to a living-moss wall in the meeting room."),
   ("Illuminated logo","A lit logo by the entrance doors."),
   ("Wall graphics","Large typographic wall graphics in the open-plan office."),
   ("Glass manifestations","Frosted and printed vinyl on meeting room and kitchen glass.")],
  "An office that wears its brand on every wall.",
  ["at_moss","at_lit","at_office","at_wall","at_glass","at_manif","at_kitchen","at_bld"],["at_m1"]),
C("and-e","AND-E",None,"commercial",["vinyl-wall-graphics","flat-cut-letters","high-level-signs"],"ae_welcome",
  "Office fit-out graphics",
  "Building sign, reception lettering, printed murals and moss wall branding for AND-E's offices.",
  "AND-E moved into new offices and wanted the brand to greet visitors at reception and run right through the workspace.",
  [("Building sign","A branded panel on the building exterior."),
   ("Welcome and boardroom walls","Lettering and partner logos on the reception and boardroom walls."),
   ("Printed murals","Large printed murals across the office walls."),
   ("Branded reception desk","Logo and strapline on the front of the reception desk.")],
  "A workspace that tells visitors who they are visiting before anyone says hello.",
  ["ae_welcome","ae_rec","ae_board","ae_road","ae_office","ae_circle","ae_blossom","ae_moss","ae_bld"]),
C("arv-studio","ARV Studio",None,"hospitality-leisure",["flat-cut-letters","vinyl-wall-graphics","digital-large-format-print"],"arv_logo",
  "Fitness studio branding",
  "Flat-cut logos, wall lettering, printed panels and an external sign for a fitness studio.",
  "ARV Studio wanted a stripped-back, monochrome look that suits a reformer studio, inside and on the street.",
  [("Flat-cut logo","The logo cut and fixed to the polished plaster wall."),
   ("Wall lettering","Large cut vinyl lettering across the studio walls."),
   ("Printed acrylic panels","Graphic panels hung in the changing areas."),
   ("External sign and door plaque","A panel on the building and an acrylic plaque at the door.")],
  "A studio where the branding feels part of the space.",
  ["arv_logo","arv_gym","arv_words","arv_lit","arv_merch","arv_ext","arv_prints","arv_vinyl","arv_door","arv"]),
C("trident-fire","Trident Fire Protection & Training",None,"commercial",["3d-letters"],"tr_halo",
  "Halo-lit sign",
  "A halo-lit sign with a fabricated flame logo, made and tested in our factory.",
  "Trident wanted a sign that glows like its logo: dark letters with a halo of light, and a flame that stands out.",
  [("Halo-lit letters","Fabricated letters with LEDs that throw light onto the panel behind."),
   ("Flame logo","A built-up logo with an orange flame."),
   ("Mounting panel","A white panel that the letters stand off from.")],
  "A sign that looks sharp by day and glows after dark.",
  ["tr_halo","tr_logo","tr_glow","tr_flame"],["tr_m1","tr_m2","tr_m3"]),
C("savoy","Savoy",None,"hospitality-leisure",["high-level-signs","projecting-signs","3d-letters"],"sv_bld",
  "Restaurant signage",
  "Gold 3D letters, a projecting sign and a wall plaque for a restaurant in a stone building.",
  "Savoy needed signs with a premium feel that work with the stone and glass of the building.",
  [("3D letters","Gold letters over the entrance and on the glazed gable."),
   ("Projecting sign","A dark projecting sign with gold lettering."),
   ("Wall plaque","A matching plaque by the door.")],
  "A building that looks as good as the food.",
  ["sv_bld","sv_letters","sv_gable","sv_ent","sv_proj","sv_plaque","n_savoy"],["sv_m1","sv_m2","n_savoy_ws"]),
C("queens-head","Queens Head & Porters Bistro",None,"hospitality-leisure",["backlit-panels","projecting-signs"],"qh_front",
  "Pub fascia and projecting sign",
  "A cut fascia panel for the Queens Head and a cut-metal projecting sign for Porters Bistro.",
  "The Queens Head and Porters Bistro share a building. Each needed its own sign, in a style that suits the old frontage.",
  [("Backlit fascia panel","Lettering cut out of the fascia panel and lit from behind."),
   ("Projecting sign","A cut-metal Porters Bistro sign with an octopus motif.")],
  "Two businesses, one building, both easy to find.",
  ["qh_front","qh_side","qh_proj","qh_corner","qh_wide","qh_porters","n_queens"],["qh_m1","qh_m2","qh_m3"]),
C("grace-kellys","Grace Kelly's",None,"hospitality-leisure",["3d-letters"],"gk_front",
  "Gold 3D letters on stone",
  "Gold 3D letters fixed across the stone frontage of Grace Kelly's.",
  "Grace Kelly's wanted its name in gold across a traditional stone building, without a panel.",
  [("3D letters","Built-up letters finished in gold."),
   ("Fixed to stone","Each letter fixed directly to the stone fascia.")],
  "A frontage with presence that suits the building.",
  ["gk_front","gk_new","gk_side","gk_street"]),
C("station-espresso","Station Espresso Bar",None,"hospitality-leisure",["3d-letters","vinyl-wall-graphics"],"st_main",
  "Cafe fascia and door vinyl",
  "3D letters on a white fascia and a logo on the door for a coffee bar.",
  "Station Espresso Bar wanted a clean, bright shopfront that matches its brand.",
  [("3D letters","Letters fixed to a white fascia panel."),
   ("Door vinyl","The logo on the glass door.")],
  "A simple, bright shopfront.",
  ["st_main","st_front2","st_wide","st_angle","st_door"]),
C("smart-vape","Smart Vape",None,"retail",["projecting-signs","digital-large-format-print"],"sm_front",
  "Printed fascia and projecting sign",
  "A full-colour printed fascia, window graphics and a round projecting sign.",
  "Smart Vape wanted a colourful shopfront that shows off its dragon mascot.",
  [("Printed fascia","Full-colour print on a fascia panel."),
   ("Window graphics","Printed window panels."),
   ("Round projecting sign","A double-sided round projecting sign.")],
  "A shopfront you can't miss.",
  ["sm_front","sm_fascia","sm_wide","sm_proj","ig_smartvape"]),
C("pickle-and-peach","Pickle & Peach",None,"hospitality-leisure",["3d-letters"],"pp_front",
  "Corner fascia lettering",
  "Gold lettering around a corner shopfront.",
  "Pickle & Peach wanted gold lettering on both faces of its corner frontage.",
  [("Fascia lettering","Gold lettering on the dark fascia, on both elevations.")],
  "A corner frontage that reads from both streets.",
  ["pp_front","pp_close","pp_side","pp_wide"]),
C("the-chair","The Chair",None,"hair-beauty",["projecting-signs"],"ch_main",
  "Hanging signs",
  "Hanging signs on decorative brackets for a salon.",
  "The Chair needed signs that hang out over the street and down a lane.",
  [("Hanging signs","Panels hung from decorative brackets."),
   ("Two locations","One on the main frontage, one in the lane.")],
  "Signs that catch people walking past.",
  ["ch_main","ch_2","ch_3","ch_4"]),
C("recover3","Recover3",None,"hospitality-leisure",["neon-led-neon","3d-letters"],"r3_front",
  "Wellness studio signage",
  "Shopfront, timber wall lettering, LED neon and illuminated room signs for a recovery studio.",
  "Recover3 offers sauna and ice baths. It wanted calm, warm signage that glows in a dark space.",
  [("LED neon","A sauna and ice baths neon sign."),
   ("Lettering on timber","The logo and services on a timber-clad wall."),
   ("Illuminated room signs","Lit reception and treatment room signs."),
   ("Halo-lit plaque","A plaque at the entrance.")],
  "A space that feels as relaxing as it is.",
  ["r3_front","r3_wall","r3_neon","r3_room","r3_rec","r3_plaque"]),
C("pantera-advisory","Pantera Advisory Group",None,"commercial",["flat-cut-letters"],"pa_main",
  "Reception logos",
  "Flat-cut geometric panther logos at reception and at the top of the stairs.",
  "Pantera Advisory Group wanted its geometric logo to greet visitors as soon as they arrive.",
  [("Flat-cut logos","The logo cut and fixed to the wall, white on dark and dark on white.")],
  "A logo you see the moment you walk in.",
  ["pa_main","pa_rec","pa_stair"]),
C("vivana-lounge","Vivana Lounge",None,"hospitality-leisure",["3d-letters","high-level-signs"],"vv_ext",
  "Lounge signage",
  "Exterior fascia letters and illuminated lettering for a lounge bar.",
  "Vivana Lounge wanted a dark, upmarket look with gold and lit lettering.",
  [("Fascia letters","Letters and logo on the dark fascia."),
   ("Illuminated lettering","Lit lettering for the evening.")],
  "A lounge that looks the part after dark.",
  ["vv_ext","vv_front","vv_int","vv_int2","vv_lit","n_vivana"],["vv_m1"]),
C("the-library","The Library",None,"hospitality-leisure",["3d-letters"],"lb_front",
  "Bar fascia lettering",
  "Gold 3D letters on a navy fascia for The Library.",
  "The Library wanted gold lettering that stands out on a dark fascia and looks good lit at night.",
  [("3D letters","Gold letters on the navy fascia.")],
  "A frontage that looks smart by day and night.",
  ["lb_front","lb_2","lb_night","lb_3","lb_close"]),
C("mapleleaf-express","Mapleleaf Express",None,"retail",["3d-letters","wayfinding"],"ml_night",
  "Forecourt and shop signage",
  "Illuminated letters, in-store lettering and forecourt signs for a filling station and shop.",
  "Mapleleaf needed a forecourt that is clear at night and a shop with branded sections.",
  [("Illuminated letters","Lit letters on the forecourt building."),
   ("In-store lettering","Section lettering for chilled, frozen, coffee and the beer cave."),
   ("Forecourt signs","Entry and exit signs around the site.")],
  "A forecourt you can read from the road at night.",
  ["ml_night","ml_auto","ml_night2","ml_chilled","ml_beer","ml_frozen","ml_coffee","ml_entry"]),
C("north-shore","North Shore",None,"hospitality-leisure",["high-level-signs","3d-letters"],"ns_fascia",
  "Fascia and kiosk lettering",
  "A long fascia sign and kiosk lettering for North Shore Coffee Roasters.",
  "North Shore needed its name along the full length of the building, and branding on its coffee kiosk.",
  [("Fascia sign","Lettering along the building fascia."),
   ("Kiosk lettering","Lettering and menu panels on the coffee kiosk.")],
  "A brand visible from the car park and inside.",
  ["ns_fascia","ns_2","ns_3","ns_kiosk","ns_kiosk2"]),
C("rustic-cup","Rustic Cup",None,"hospitality-leisure",["3d-letters"],"rc_front",
  "Cafe fascia lettering",
  "3D letters on a white fascia for a cafe.",
  "Rustic Cup wanted simple, clear lettering on its frontage.",
  [("3D letters","Letters fixed to the white fascia.")],
  "A cafe you can see from across the street.",
  ["rc_front","rc_3"]),
C("just-peachy","Just Peachy",None,"hair-beauty",["3d-letters"],"jp_front",
  "Clinic fascia",
  "A fascia sign for a permanent makeup clinic and training academy.",
  "Just Peachy needed a clean fascia that lists its services.",
  [("Fascia sign","Logo and services line on the fascia.")],
  "A clean, clear frontage.",
  ["jp_front","jp_2","jp_3","jp_close"]),
C("sienna","Sienna House of Beauty",None,"hair-beauty",["vinyl-wall-graphics"],"si_front",
  "Fascia and window frosting",
  "A pink fascia and frosted window graphics for a beauty salon.",
  "Sienna wanted its pink branding on the fascia, and privacy for clients inside.",
  [("Fascia","A pink fascia with the logo and services."),
   ("Window frosting","Frosted vinyl with the brand pattern.")],
  "A salon that looks welcoming and keeps clients private.",
  ["si_front","si_2","si_close","si_win"],["si_m1"]),
C("dolled-up-luxe","Dolled Up Luxe",None,"hair-beauty",["3d-letters"],"du_front",
  "Salon fascia",
  "Gold script lettering on a white fascia for a beauty salon.",
  "Dolled Up Luxe wanted gold script lettering on its frontage.",
  [("Fascia lettering","Gold script lettering on the white fascia.")],
  "A fresh, bright frontage.",
  ["du_front","du_2","du_3"]),
C("tms-grid","TMS Grid",None,"commercial",["high-level-signs"],"tms_main",
  "Building signs",
  "Building signs on an industrial unit for TMS Grid.",
  "TMS Grid wanted its name on the front and side of its unit.",
  [("Building signs","Panels with the logo and strapline.")],
  "A unit that is easy to find.",
  ["tms_main","tms_2","tms_3"]),
C("wr-group","WR Group",None,"commercial",["3d-letters"],"wr_brick",
  "3D logo on brick",
  "A 3D logo on brick and a halo-lit version for WR Group.",
  "WR Group wanted its logo on the building in 3D.",
  [("3D logo","Built-up logo and letters on the brick wall."),
   ("Halo-lit logo","A halo-lit version of the logo.")],
  "A logo that stands out on the building.",
  ["wr_brick","wr_halo","wr_2"]),
C("recite-me","Recite Me",None,"commercial",["3d-letters"],"rm_main",
  "Office logo",
  "A 3D logo on a red feature wall for Recite Me.",
  "Recite Me wanted its logo on the office feature wall.",
  [("3D logo","Built-up logo on the red wall.")],
  "A feature wall that is all brand.",
  ["rm_main","rm_2","rm_3"]),
C("welcome-to-durham","Ward Group: Welcome to Durham","Durham","construction",["digital-large-format-print"],"du_banner",
  "Scaffold banners",
  "Large printed banners on a building under scaffold in Durham.",
  "Ward Group wanted to turn scaffold on a corner building into a welcome to the city.",
  [("Printed banners","Large-format banners on both faces of the scaffold.")],
  "Scaffold that welcomes people instead of hiding the building.",
  ["du_banner","du_banner2","du_banner3","du_banner4"]),
C("qe-facilities","QE Facilities",None,"healthcare",["3d-letters"],"qe_main",
  "Letters on glazing",
  "3D letters and NHS logo on the glazed front of QE Facilities.",
  "QE Facilities wanted its name across the glazed entrance.",
  [("3D letters","Letters and logo fixed to the glazing.")],
  "An entrance that is clearly branded.",
  ["qe_main","qe_close","qe_2"],["qe_m1"]),
C("grainger-market","Grainger Market","Newcastle upon Tyne","retail",["3d-letters"],"gm_main",
  "Gold 3D letters",
  "Gold 3D letters over an entrance to Grainger Market.",
  "Grainger Market needed lettering that suits a listed stone building.",
  [("3D letters","Gold letters fixed to the stone over the entrance.")],
  "Lettering that looks part of the building.",
  ["gm_main","gm_2","gm_3","gm_4","n_grainger"]),
C("the-works","The Works",None,"retail",["3d-letters","light-boxes"],"tw_shop",
  "Illuminated shopfronts",
  "Illuminated shopfront signs for The Works.",
  "The Works needed bright, lit shopfronts.",
  [("Illuminated signs","Lit letters and logo on yellow panels.")],
  "Shopfronts that glow.",
  ["tw_shop","tw_dusk","tw_lit","tw_lit2","tw_mall"],["tw_m1","tw_m2"]),
]

CASES += NEW

def _add(slug, photos=(), making=()):
    c = next(x for x in CASES if x["slug"] == slug)
    c["photos"] += [p for p in photos if p not in c["photos"]]
    c["making"] += [m for m in making if m not in c["making"]]
_add("nhs-community-diagnostic-centre", ["p_cdc_3d","p_cdc_wide","p_cdc_ent","p_cdc_sky","p_cdc_angel","p_cdc_corr","p_cdc_way","p_cdc_wait","p_cdc_wc"], ["p_cdc_m1","p_cdc_m2","p_cdc_m3"])
_add("woodham-academy", ["p_wd_ext","p_wd_ent","p_wd_rec","p_wd_atrium","p_wd_quote","p_wd_lvl1","p_wd_hall","p_wd_site"])
_add("aldi-jaymac-warehouse", ["p_jm_panels","p_aldi_panel"])
_add("cork-and-coffee", ["p_cork_new"])
_add("glow-tanning", ["p_gl_shop","p_gl_rec","p_gl_wall","p_gl_corr","p_gl_door","p_gl_num","p_gl_wide"])
_add("vertu-motors-arena", ["p_vt_day","p_vt_night"])
_add("newcastle-university", ["p_ncl_van"])

# ---------------------------------------------------------------- areas
AREAS = [
 dict(slug="newcastle", name="Newcastle upon Tyne", short="Newcastle", council="Newcastle City Council", hero="hero",
      lede="Shop signs, illuminated signs and building signage for Newcastle businesses, made a few miles away in Team Valley.",
      intro=["Onesign was founded in Newcastle and we have been making signs for the city since 2008. Our factory is just across the Tyne in Team Valley, so a site survey in the city centre, Jesmond, Gosforth, Heaton, Byker or out at the Airport is a short drive for us.",
             "We design, manufacture and install everything ourselves. You get one team from the first mockup to the final fixing, and nothing is sent away to be made."],
      proof=[("newcastle-university", "Campus signage partner for more than 15 years."),
             ("vertu-motors-arena", "High-level illuminated letters for the home of the Newcastle Eagles.")],
      also="We have also made the gold 3D letters at Grainger Market and signs for bars, restaurants, salons and offices across the city.",
      photos=["hero", "vertu_night", "n_grainger", "catalyst", "uni_totem", "n_murphys"],
      places=["City centre", "Quayside", "Jesmond", "Gosforth", "Heaton", "Byker", "Ouseburn", "Benton", "Kenton", "Newcastle Airport"],
      planning="Much of the city centre, including Grainger Town, is a conservation area with many listed buildings, and illuminated signs there usually need consent from Newcastle City Council. We check what applies to your building at survey and can handle the application.",
      faq=[("Do you offer free site surveys in Newcastle?", "Yes. We are based in Team Valley, a few miles from the city centre, and we survey before we quote so the price is based on real measurements."),
           ("Can you make illuminated signs for a shop in Newcastle city centre?", "Yes. We make halo-lit and face-lit 3D letters, backlit panels, light boxes and LED neon. In conservation areas such as Grainger Town illuminated signs usually need consent, which we can apply for on your behalf."),
           ("How long does a shop sign take?", "It depends on the sign and on whether consent is needed. We give you a timescale with your quote, once we have seen the building.")]),
 dict(slug="gateshead", name="Gateshead", short="Gateshead", council="Gateshead Council", hero="hc_cdc",
      lede="We are a Gateshead sign company: every sign is made in our own 10,000 sq ft factory on Princesway North, Team Valley.",
      intro=["Gateshead is home. Our factory and offices are on Team Valley, and you are welcome to visit, see signs being made and talk through your project in person.",
             "Because we make everything on site, Gateshead businesses get short lead times, quick site visits and someone local to call if anything ever needs attention."],
      proof=[("nhs-community-diagnostic-centre", "A full signage scheme for the NHS inside the Metrocentre."),
             ("superpower-metrocentre", "Face-illuminated letters on The Crescent at the Metrocentre.")],
      also="Whether you are on Team Valley, in Low Fell or out at Blaydon, we are minutes away for a survey.",
      photos=["hc_cdc", "n_superpower_wide", "nhs_bld", "ws_assembly", "nhs_skyline", "n_superpower"],
      places=["Team Valley", "Metrocentre", "Gateshead Quays", "Low Fell", "Felling", "Blaydon", "Whickham", "Birtley", "Dunston", "Ryton"],
      planning="Shopping centres such as the Metrocentre have their own shopfit rules on top of planning rules. We have fitted signs there and know how the approval process works.",
      faq=[("Where are you based?", "D86 Princesway North, Team Valley, Gateshead NE11 0TU. We are open Monday to Thursday 07:00 to 16:00 and Friday 07:00 to 12:00."),
           ("Can I visit the factory?", "Yes. Call us on 0191 487 6767 to arrange a time and we will show you materials, finishes and signs in production."),
           ("Do you fit signs in the Metrocentre?", "Yes. We have installed signage for the NHS Community Diagnostic Centre and for Superpower on The Crescent.")]),
 dict(slug="sunderland", name="Sunderland", short="Sunderland", council="Sunderland City Council", hero="cork_dusk",
      lede="Shop signs, building signs and wayfinding for Sunderland and Wearside, designed, made and fitted by one team.",
      intro=["From the city centre and the seafront at Roker and Seaburn to Washington and Houghton-le-Spring, we make and fit signs across Sunderland. Our factory in Team Valley is a short drive up the A1.",
             "We work for independent shops and bars, for national brands and for the public sector, and every job is surveyed, designed, manufactured and installed by our own people."],
      proof=[],
      also="Sunderland City Council appointed us to supply its Links with Nature signage, and we work with businesses of every size across Wearside.",
      photos=["cork_dusk", "st_sign", "n_thatype", "ig_codcrust", "way_g", "n_annas"],
      places=["City centre", "Sunniside", "Roker", "Seaburn", "Washington", "Houghton-le-Spring", "Hetton-le-Hole", "Doxford Park", "Hendon", "Southwick"],
      planning="Parts of the city centre, including Sunniside, are conservation areas where signs are more tightly controlled. We check the rules for your building with Sunderland City Council before anything is made.",
      faq=[("Do you cover Sunderland and Washington?", "Yes. We survey, deliver and install across Sunderland, Washington and the rest of Wearside from our factory in Team Valley."),
           ("Do you work for the public sector in Sunderland?", "Yes. Sunderland City Council appointed us to supply its Links with Nature signage, and we hold Constructionline, CSCS, IPAF and PASMA accreditations."),
           ("Can you replace an old shop sign?", "Yes. We remove the old sign, make good the fascia where needed and fit the new one, usually in a single visit.")]),
 dict(slug="durham", name="Durham", short="Durham", council="Durham County Council", hero="n_court",
      lede="Signs for Durham City and County Durham, from gold letters in the historic centre to whole-school signage schemes.",
      intro=["We work right across County Durham: Durham City, Chester-le-Street, Seaham, Peterlee, Newton Aycliffe, Bishop Auckland and Consett. Team Valley sits just off the A1, so most of the county is within easy reach.",
             "In a historic city the detail matters. We make traditional-looking signs in brass, copper and gold finishes as well as modern illuminated signs, and we know when each is appropriate."],
      proof=[("woodham-academy", "Every sign in a brand-new school in Newton Aycliffe."),
             ("cork-and-coffee", "Komacel 3D letters and interior branding in Seaham."),
             ("aldi-jaymac-warehouse", "High-level signs on a new warehouse in County Durham.")],
      also="In Durham City we made the gold 3D letters for The Court, halo-lit letters and window graphics for Zen, and flat-cut letters for Durham University and Microsoft.",
      photos=["n_court", "ig_zen", "ig_durham", "woodham", "cork_dusk", "ig_lineart"],
      places=["Durham City", "Chester-le-Street", "Seaham", "Peterlee", "Newton Aycliffe", "Bishop Auckland", "Consett", "Stanley", "Spennymoor", "Barnard Castle"],
      planning="Durham City centre is a conservation area and sits beside a World Heritage Site, so signs there are closely controlled and internally illuminated signs are discouraged. We design with that in mind and can prepare the application to Durham County Council.",
      faq=[("Can you make signs suitable for Durham's conservation area?", "Yes. We make non-illuminated and externally lit signs in brass, copper, gold and painted finishes that suit historic buildings, and we can handle the consent application."),
           ("Do you make signs for schools in County Durham?", "Yes. At Woodham Academy in Newton Aycliffe we supplied the whole package: building sign, wayfinding, classroom signs, wall graphics and safety signs."),
           ("How far do you travel?", "We cover the whole of County Durham as standard, and we install across the UK.")]),
 dict(slug="south-tyneside", name="South Shields & South Tyneside", short="South Tyneside", council="South Tyneside Council", hero="n_griffin",
      lede="Sign makers for South Shields, Jarrow, Hebburn and the rest of South Tyneside.",
      intro=["South Tyneside is on our doorstep. We make and fit signs for shops on King Street and Ocean Road, for businesses on the riverside estates and for developments across South Shields, Jarrow, Hebburn and Boldon.",
             "Everything is made in our Team Valley factory and fitted by our own installers, so you deal with one local team throughout."],
      proof=[("griffin-court", "Fabricated aluminium letters for a residential development in Hebburn.")],
      also="Shopfront signs, window graphics and vehicle graphics are all made in the same factory, so your brand matches everywhere.",
      photos=["n_griffin", "n_griffin_up", "ig_park2", "n_queens", "ig_corner", "n_lean"],
      places=["South Shields", "Jarrow", "Hebburn", "Boldon", "Cleadon", "Whitburn", "Harton", "Westoe"],
      planning="Seafront and town-centre locations can fall within conservation areas. We check with South Tyneside Council what your building allows before we design.",
      faq=[("Do you cover South Shields?", "Yes. We survey and install across South Shields, Jarrow, Hebburn and the Boldons."),
           ("Do you work with building contractors?", "Yes. We worked with Robertson Group on Griffin Court in Hebburn, and we hold CSCS, IPAF, PASMA and Constructionline accreditations for site work."),
           ("Can you sign-write my van as well as my shop?", "Yes. We design and fit vehicle graphics alongside shop signs, so your brand matches everywhere.")]),
 dict(slug="northumberland", name="Northumberland", short="Northumberland", council="Northumberland County Council", hero="ng_totem",
      lede="Signs for Northumberland's towns, hospitals, schools and visitor destinations.",
      intro=["From Cramlington, Blyth and Ashington to Morpeth, Hexham, Alnwick and Berwick, we make and install signs across Northumberland.",
             "The county mixes busy industrial estates with historic market towns, so we make both: large illuminated signs and totems for retail parks and factories, and hand-finished traditional signs for high streets."],
      proof=[("northgate-hospital", "Totems, ward lettering and wall art across Northgate Hospital in Morpeth.")],
      also="We also work with the NHS trust covering Cumbria, Northumberland, Tyne and Wear.",
      photos=["ng_totem", "alwinton", "sycamore", "ig_nhs_cumbria", "wardDir", "ig_totem_dir"],
      places=["Morpeth", "Cramlington", "Blyth", "Ashington", "Hexham", "Alnwick", "Berwick-upon-Tweed", "Ponteland", "Prudhoe", "Bedlington"],
      planning="Market towns such as Hexham, Alnwick and Morpeth have conservation areas, and parts of the county are protected landscapes where advertising is more tightly controlled. We check with Northumberland County Council before we design.",
      faq=[("Do you install signs in rural Northumberland?", "Yes. We cover the whole county, from the Tyne Valley to Berwick."),
           ("Do you make hospital and healthcare signs?", "Yes. At Northgate Hospital in Morpeth we supplied external totems, ward lettering, window graphics and wall art, and we are used to working on live healthcare sites."),
           ("Can you make traditional signs for a market-town shopfront?", "Yes. We make painted, gilded-effect, brass and copper signs and hanging signs that suit historic high streets.")]),
]

# ---------------------------------------------------------------- guides
GUIDES = [
 dict(slug="shop-sign-cost", title="How Much Does a Shop Sign Cost? UK Guide", h1="how much does a shop sign cost?",
      desc="What decides the price of a shop sign in the UK: size, sign type, illumination, materials, access and consent. Written by a sign manufacturer.",
      hero="ws_assembly", updated="2026-11-16", kicker="Cost guide",
      lede="The honest answer is that it depends on six things. Here is what they are, how each one moves the price and how to get an exact figure without wasting time.",
      sections=[
       ("the six things that set the price", "<ol class=\"steps-list\"><li><b>Size.</b> Material, fabrication time and the installation method all scale with the sign. A wider fascia needs more metal, more LEDs and often two fitters instead of one.</li><li><b>Sign type.</b> A printed panel is quick to make. Built-up 3D letters are fabricated one letter at a time, so they cost more. A <a href=\"{R}guides/illuminated-signs.html\">comparison of the main types</a> is in our illuminated signs guide.</li><li><b>Illumination.</b> Lighting adds LEDs, power supplies, wiring and testing. Halo-lit and face-lit letters cost more than the same letters unlit.</li><li><b>Materials and finish.</b> Painted aluminium is the everyday choice. Stainless steel, brass and copper cost more, and so do special finishes such as aged metal or mirrored acrylic. Komacel with a metallic inlay gives a brushed-metal look for less than solid metal.</li><li><b>Access and installation.</b> A ground-floor fascia can be fitted from steps or a small tower. High-level signs need powered access, more people and sometimes a road or pavement permit.</li><li><b>Design and consent.</b> If your artwork is ready, design time is short. If you need a logo redrawn or an <a href=\"{R}guides/sign-planning-permission.html\">advertisement consent application</a>, that is extra work.</li></ol>"),
       ("cheaper and dearer ways to get the same look", "<p>You can often keep the look you want and change how it is made:</p><ul><li><b>Letters on a panel instead of letters on the wall.</b> One panel is quicker to wire and fit than twenty separate letters, and it protects the wall behind.</li><li><b>A backlit panel instead of built-up letters.</b> The lettering is cut out of a single panel and lit from behind. At night it reads much like illuminated letters.</li><li><b>Komacel instead of solid metal.</b> Inset brass, copper or brushed laminates give a metal face at lower cost.</li><li><b>A flex face instead of a huge light box.</b> For very large signs, a tensioned printed skin avoids joins and can be re-skinned later for a rebrand.</li></ul>"),
       ("what a proper quote should include", "<p>Compare quotes like for like. Ours always cover:</p><ul><li>A site survey with real measurements</li><li>A scaled visual of the sign on a photo of your building</li><li>Manufacture, including LEDs and power supplies for illuminated signs</li><li>Installation by our own trained fitters, with any access equipment</li><li>Removal of the old sign where needed</li></ul><p>If a quote looks cheap, check whether installation, access and electrics are included.</p>"),
       ("how to get an exact price quickly", "<p>Send us three things and we can usually price without a second conversation:</p><ol><li>A straight-on photo of the building</li><li>The rough width of the space the sign will fill</li><li>Your logo, in any format</li></ol><p>We will send back a free mockup and a single price that covers design, manufacture and installation.</p>")],
      faq=[("Is an illuminated sign much more expensive to run?", "No. Modern signs use LEDs, which draw little power and last for years. A timer or photocell stops the sign running in daylight."),
           ("Do you charge for a survey or mockup?", "No. The site survey and the first mockup are free."),
           ("Can I pay for a sign in stages?", "Ask us when you enquire. Payment terms are confirmed with your quote."),
           ("Why not just publish a price list?", "Because two signs that look alike in a photo can differ a lot in size, materials and access. A price without a survey is a guess, and we would rather give you a figure we can stand behind.")]),
 dict(slug="sign-planning-permission", title="Do I Need Planning Permission for a Shop Sign? UK Guide", h1="do I need planning permission for a shop sign?",
      desc="When a shop sign needs advertisement consent in England, what deemed consent covers, how illuminated signs and conservation areas change things, and how to apply.",
      hero="n_grainger", updated="2026-11-16", kicker="Planning guide",
      lede="Many ordinary shop signs can go up without an application. Illuminated signs, large signs and anything on a listed building or in a conservation area are a different matter. This guide explains the rules in England in plain English.",
      sections=[
       ("signs are controlled by advertisement consent", "<p>Shop signs in England are not covered by ordinary planning permission. They come under a separate system, set out in the Town and Country Planning (Control of Advertisements) (England) Regulations 2007. Scotland, Wales and Northern Ireland have their own versions.</p><p>Under those rules every outdoor sign falls into one of three groups:</p><ul><li><b>No consent needed.</b> A small number of signs are excluded altogether, such as signs inside a building that are not lit and not close to the window.</li><li><b>Deemed consent.</b> The sign is automatically allowed, as long as it meets the conditions for its class. Many traditional, non-illuminated fascia and hanging signs fall here.</li><li><b>Express consent.</b> You need to apply to the council. This is what people usually mean by planning permission for a sign.</li></ul>"),
       ("when you can usually go ahead without applying", "<p>A sign on business premises that advertises the business carried on there often has deemed consent, provided it stays within limits on things like the size of the lettering, the height above ground and the number of signs. The exact limits are set out in the regulations, and they are tighter in some protected areas.</p><p>Whatever the class, five standard conditions always apply. The sign must be kept clean and tidy, be kept safe, have the site owner's permission, not obscure road, rail or other transport signs, and be removed carefully if the council requires it.</p>"),
       ("when you will probably need consent", "<ul><li><b>Most illuminated signs.</b> Some illuminated signs have deemed consent in limited circumstances, but the Planning Portal's own advice is that the majority need an application.</li><li><b>Large or high-level signs.</b> Signs above the limits for size or height, including most building signs high on a wall.</li><li><b>Conservation areas.</b> The limits are stricter, and illumination is more tightly controlled.</li><li><b>Listed buildings.</b> You will usually need listed building consent as well as advertisement consent, even for a small sign.</li><li><b>Signs away from your premises.</b> Totems at a site entrance, directional signs and hoardings often need consent.</li></ul><p>If you rent, check your lease too. Landlords and shopping centres often have their own approval process.</p>"),
       ("how to apply", "<ol><li><b>Drawings.</b> The council needs a location plan and scaled drawings showing the sign's size, position, materials, colours and how it is lit.</li><li><b>Application.</b> Applications are made to the local council, usually through the Planning Portal.</li><li><b>Fee.</b> The fee is set nationally and normally rises each April. The Planning Portal's fee calculator gives the current figure.</li><li><b>Decision.</b> Councils aim to decide most advertisement applications within eight weeks. Consent normally lasts five years, and the sign can usually stay up after that unless the council says otherwise.</li></ol><p>We prepare the drawings as part of our design work and can submit the application for you.</p>"),
       ("what happens if you skip it", "<p>Displaying a sign that needs consent without having it is an offence, and the council can require the sign to be removed. It is far cheaper to check first. We look at this at survey stage, before anything is made.</p><p class=\"note\">This guide is a plain-English summary, not legal advice. Rules vary by location, so always confirm with your local planning authority.</p>")],
      faq=[("Do I need permission to replace an existing shop sign?", "If the new sign is the same size, in the same position and lit in the same way, often not. If you are changing the size, adding lighting or the building is listed or in a conservation area, check first."),
           ("Do neon signs in a window need consent?", "An illuminated sign inside a window can still count as an advertisement that needs consent, particularly in conservation areas. Ask your council before you order."),
           ("How long does advertisement consent take?", "Councils aim to decide within eight weeks of a valid application. Allow time before that for drawings."),
           ("Can you apply for me?", "Yes. We produce the drawings and can submit the application as part of the job.")]),
 dict(slug="illuminated-signs", title="Illuminated Signs Explained: Halo-Lit, Face-Lit, Backlit & More", h1="illuminated signs, explained.",
      desc="Halo-lit letters, face-lit letters, backlit panels, light boxes, flex faces and LED neon: what each one is, how it looks at night and when to choose it.",
      hero="n_thatype", updated="2026-11-16", kicker="Buyer's guide",
      lede="There are six common ways to light a sign. They look very different after dark and suit different buildings. Here is how to tell them apart and choose.",
      sections=[
       ("halo-lit letters", "<p>LEDs sit behind each letter and shine backwards onto the wall. The letter face stays solid and a soft glow surrounds it, so the lettering seems to float. Halo lighting flatters metal finishes such as brass, copper and stainless steel.</p><p><b>Choose it for:</b> a premium, understated look on bars, restaurants, salons, receptions and offices. It needs a fairly light, matt wall to glow against.</p><p><a href=\"{R}signs/3d-letters.html\">See our 3D letters →</a></p>"),
       ("face-lit letters", "<p>The letter is a shallow box with an acrylic face, and the light shines out through the front. The colour of the face is the colour you see at night. Fabricated letters can also be lit through the face and the sides together, which is called rim and return.</p><p><b>Choose it for:</b> maximum brightness and legibility at a distance. It is the usual choice for retail shopfronts and high-level building signs.</p>"),
       ("backlit panels", "<p>The lettering is cut out of a single metal panel, called aperture cutting, and backed or filled with opal acrylic. At night only the lettering lights up. Acrylic can be pushed through the cut-outs so the letters stand slightly proud.</p><p><b>Choose it for:</b> a crisp illuminated fascia that is quicker to fit than individual letters, or a logo with fine detail that would be hard to build as separate letters.</p><p><a href=\"{R}signs/backlit-panels.html\">See our backlit panels →</a></p>"),
       ("light boxes", "<p>An aluminium box with a printed or vinyl-covered acrylic face, lit evenly from inside. The whole face glows.</p><p><b>Choose it for:</b> smaller signs, projecting signs and anywhere a full-colour printed design needs lighting.</p><p><a href=\"{R}signs/light-boxes.html\">See our light boxes →</a></p>"),
       ("flex faces", "<p>A printed flexible skin tensioned across a large illuminated frame. Because the skin is one piece, very large signs have no joins.</p><p><b>Choose it for:</b> big fascias on retail parks and leisure venues. When you rebrand, the skin can be replaced and the frame stays.</p><p><a href=\"{R}signs/flex-faces.html\">See our flex faces →</a></p>"),
       ("LED neon", "<p>Flexible LED tube formed into lettering or line art, mounted on clear or coloured acrylic. It gives the look of traditional glass neon, runs at low voltage and is far more robust.</p><p><b>Choose it for:</b> interiors, feature walls and windows where you want a statement piece.</p><p><a href=\"{R}signs/neon-led-neon.html\">See our LED neon →</a></p>"),
       ("how to choose", "<ul><li><b>How far away will people read it?</b> Face-lit letters and flex faces carry furthest. Halo lighting is for close and mid-range.</li><li><b>What is the wall like?</b> Halo lighting needs a wall to glow against. On glass, dark cladding or busy brickwork, face-lit letters or a panel work better.</li><li><b>What will the council allow?</b> In conservation areas, internally illuminated signs are often refused, while halo-lit or externally lit signs may be accepted. See our <a href=\"{R}guides/sign-planning-permission.html\">planning guide</a>.</li><li><b>What is the budget?</b> A backlit panel or light box usually costs less than a set of built-up illuminated letters. See our <a href=\"{R}guides/shop-sign-cost.html\">cost guide</a>.</li></ul>")],
      faq=[("What is the difference between halo-lit and backlit?", "People use both terms for letters lit from behind. We use halo-lit for individual letters that glow onto the wall, and backlit panel for a panel with cut-out lettering lit from behind."),
           ("How long do LED signs last?", "Good-quality LED modules last for many years of normal use and can be replaced without replacing the sign."),
           ("Can an existing sign be converted to LED?", "Often, yes. Older signs lit by fluorescent tubes can usually be refitted with LEDs."),
           ("Do illuminated signs need planning consent?", "Most do. We check this at survey and can apply for you.")]),
 dict(slug="accessible-wayfinding-signage", title="Accessible Wayfinding Signage: A UK Guide", h1="accessible wayfinding signage.",
      desc="How to plan wayfinding signs that work for everyone: contrast, tactile and Braille signs, mounting heights, plain wording and consistent placement.",
      hero="way_g", updated="2026-11-16", kicker="Wayfinding guide",
      lede="Good wayfinding lets a first-time visitor reach the right door without asking. Accessible wayfinding makes sure that includes people with sight loss, mobility impairments or cognitive differences. These are the principles we design to.",
      sections=[
       ("why it matters", "<p>Under the Equality Act 2010, organisations that serve the public must make reasonable adjustments so disabled people are not put at a disadvantage. Signs are a large part of that. Design guidance comes from BS 8300, the British Standard for accessible buildings, and from the Sign Design Guide published with the RNIB.</p>"),
       ("contrast first", "<p>Most people with sight loss have some vision, and contrast helps them more than anything else. Two contrasts matter: the text against the sign, and the sign against the wall behind it. BS 8300 measures this with light reflectance values and recommends a clear difference between the two surfaces. Matt finishes are better than gloss, which causes glare.</p>"),
       ("tactile and Braille signs", "<p>Signs that people can reach and touch, such as toilet, lift and room signs, should have raised lettering and Braille. The usual practice is to mount them on the wall beside the latch side of the door, at a consistent height that can be reached standing or seated, rather than on the door itself.</p>"),
       ("plain words, clear type and symbols", "<ul><li>Use sentence case. Words in capitals are harder to recognise by shape.</li><li>Choose a clear sans-serif typeface with open letter shapes.</li><li>Pair words with standard symbols, which help people who do not read English well.</li><li>Use the same name for a place on every sign, map and appointment letter.</li></ul>"),
       ("plan the journey, not the sign", "<p>A wayfinding scheme starts with routes. Walk each journey from the car park or bus stop to the destination and put a sign at every point where someone has to make a decision. Too many signs are as confusing as too few. Colour-coded floors or zones, as we used at <a href=\"{R}work/woodham-academy.html\">Woodham Academy</a>, help people remember where they are.</p>"),
       ("healthcare and NHS sites", "<p>Hospitals add their own needs: NHS identity guidelines, infection control, anti-ligature fixings in mental health settings and work on live sites. We have delivered schemes at <a href=\"{R}work/northgate-hospital.html\">Northgate Hospital</a> and the <a href=\"{R}work/nhs-community-diagnostic-centre.html\">NHS Community Diagnostic Centre</a>.</p><p class=\"note\">This guide summarises good practice. For a specific building, refer to the current edition of BS 8300 and your access consultant.</p>")],
      faq=[("Is Braille signage a legal requirement?", "The Equality Act does not list specific signs. It requires reasonable adjustments, and tactile and Braille signs on key doors are a widely accepted way to meet that duty."),
           ("Can accessible signs still match our brand?", "Yes. Brand colours, materials and type can usually be kept, provided contrast and legibility are good."),
           ("Do you survey existing buildings?", "Yes. We can walk your site, mark up routes and decision points and propose a scheme."),
           ("Do you install on live hospital and school sites?", "Yes. We plan installation around patients, pupils and staff, and our fitters hold CSCS cards.")]),
]

# ---- type and hero corrections (checked photo by photo, Nov 2026)
_FIX_TYPES = {"glow-tanning": ["3d-letters", "vinyl-wall-graphics", "wayfinding"],
              "cod-and-crust": ["backlit-panels"],
              "welcome-to-durham": ["flags-banners"],
              "dolled-up-luxe": ["flat-cut-letters"],
              "the-works": ["3d-letters", "projecting-signs"]}
_FIX_HERO = {"aldi-jaymac-warehouse": "aldi_bld", "mapleleaf-express": "p_ml_auto"}
for _c in CASES:
    if _c["slug"] in _FIX_TYPES: _c["types"] = _FIX_TYPES[_c["slug"]]
    if _c["slug"] in _FIX_HERO:
        _c["hero"] = _FIX_HERO[_c["slug"]]
        _c["photos"] = [_c["hero"]] + [p for p in _c["photos"] if p != _c["hero"]]
for _c in CASES:
    if _c["slug"] == "aldi-jaymac-warehouse":
        _wip = ["aldi", "jaymac", "install"]
        _c["photos"] = [p for p in _c["photos"] if p not in _wip]
        _c["making"] = list(_c.get("making") or []) + [p for p in _wip if p not in (_c.get("making") or [])]

# ---- jobs added from the full photo folder (Nov 2026)
NEW2 = [
 {
  "slug": "kink",
  "old": None,
  "name": "Kink",
  "where": None,
  "sector": "retail",
  "types": [
   "3d-letters"
  ],
  "hero": "p_x_kink_0",
  "label": "3D letter fascia",
  "lede": "Pink 3D letters on a new grey fascia and shopfront.",
  "brief": "A bold fascia that stands out on a busy high street.",
  "made": [
   [
    "3D letters",
    "Fabricated letters in the brand pink, fixed to the fascia."
   ],
   [
    "Fascia panel",
    "A smooth grey panel to finish the shopfront."
   ]
  ],
  "result": "A shopfront you can spot from the end of the street.",
  "photos": [
   "p_x_kink_0",
   "p_x_kink_1",
   "p_x_kink_2",
   "p_x_kink_3",
   "p_g_kink"
  ],
  "making": []
 },
 {
  "slug": "skin-and-soul",
  "old": None,
  "name": "Skin & Soul Medical",
  "where": None,
  "sector": "hair-beauty",
  "types": [
   "flat-cut-letters",
   "projecting-signs",
   "neon-led-neon"
  ],
  "hero": "p_x_skinandsou_0",
  "label": "Shopfront, projecting sign and interior",
  "lede": "Shopfront lettering, a projecting sign and interior lettering for a medical aesthetics clinic.",
  "brief": "The clinic wanted one clean brand look from the street to the treatment rooms.",
  "made": [
   [
    "Shopfront lettering",
    "Lettering on the rendered frontage."
   ],
   [
    "Projecting sign",
    "A double-sided sign so the clinic is seen from along the street."
   ],
   [
    "Interior lettering",
    "Flat-cut lettering and an LED sign inside."
   ]
  ],
  "result": "A clinic that looks the part inside and out.",
  "photos": [
   "p_x_skinandsou_0",
   "p_x_skinandsou_1",
   "p_x_skinandsou_2",
   "p_x_skinandsou_3",
   "p_x_skinandsou_4",
   "p_x_skinandsou_5",
   "n_skinsoul",
   "n_skinsoul_neon"
  ],
  "making": []
 },
 {
  "slug": "fika-aesthetics",
  "old": None,
  "name": "FIKA Aesthetics",
  "where": None,
  "sector": "hair-beauty",
  "types": [
   "flat-cut-letters"
  ],
  "hero": "p_x_fikaaesthe_0",
  "label": "Interior lettering",
  "lede": "Flat-cut logo lettering for an aesthetics clinic.",
  "brief": "A simple, elegant logo on the wall of the treatment room.",
  "made": [
   [
    "Flat-cut letters",
    "The FIKA logo cut from solid sheet and fixed to the wall."
   ]
  ],
  "result": "A calm, premium finish to the clinic.",
  "photos": [
   "p_x_fikaaesthe_0",
   "p_x_fikaaesthe_1",
   "p_x_fikaaesthe_2",
   "fira"
  ],
  "making": []
 },
 {
  "slug": "fora",
  "old": None,
  "name": "Fora Beauty and Skin Clinic",
  "where": None,
  "sector": "hair-beauty",
  "types": [
   "flat-cut-letters"
  ],
  "hero": "p_x_fora_0",
  "label": "Interior lettering",
  "lede": "Flat-cut lettering for a beauty and skin clinic.",
  "brief": "A clean logo wall for the clinic.",
  "made": [
   [
    "Flat-cut letters",
    "Black lettering cut from solid sheet and fixed to the wall."
   ]
  ],
  "result": "A crisp logo that fits the clinic's style.",
  "photos": [
   "p_x_fora_0",
   "n_fora"
  ],
  "making": []
 },
 {
  "slug": "good-lash-gang",
  "old": None,
  "name": "The Good Lash Gang",
  "where": None,
  "sector": "hair-beauty",
  "types": [
   "neon-led-neon"
  ],
  "hero": "p_x_goodlashga_0",
  "label": "LED neon",
  "lede": "An LED neon sign on a printed feature wall.",
  "brief": "A welcome sign clients would want to photograph.",
  "made": [
   [
    "LED neon",
    "Script neon fixed over the printed lettering on a pink wall."
   ]
  ],
  "result": "A feature wall made for photos.",
  "photos": [
   "p_x_goodlashga_0",
   "p_x_goodlashga_1",
   "welcome_neon"
  ],
  "making": []
 },
 {
  "slug": "camden-clinic",
  "old": None,
  "name": "The Camden Clinic",
  "where": None,
  "sector": "healthcare",
  "types": [
   "3d-letters"
  ],
  "hero": "p_x_camdenclin_0",
  "label": "3D letter fascia",
  "lede": "Chrome-effect 3D letters on a dark fascia.",
  "brief": "A smart, clinical look for the clinic frontage.",
  "made": [
   [
    "3D letters",
    "Polished letters on a dark fascia panel."
   ]
  ],
  "result": "A frontage that looks professional from the street.",
  "photos": [
   "p_x_camdenclin_0",
   "p_x_camdenclin_1",
   "p_x_camdenclin_2",
   "n_camden"
  ],
  "making": []
 },
 {
  "slug": "zen",
  "old": None,
  "name": "Zen",
  "where": None,
  "sector": "hospitality-leisure",
  "types": [
   "vinyl-wall-graphics",
   "3d-letters"
  ],
  "hero": "p_x_zen_0",
  "label": "Window graphics and lettering",
  "lede": "Line-art window graphics and lettering for a Thai and Asian restaurant.",
  "brief": "Zen wanted its windows to show off the brand without blocking the view.",
  "made": [
   [
    "Window graphics",
    "A Buddha line-art design and a city skyline across the glazing."
   ],
   [
    "Lettering",
    "Zen lettering outside and in."
   ]
  ],
  "result": "Windows that tell you what the restaurant is about.",
  "photos": [
   "p_x_zen_0",
   "ig_lineart",
   "p_x_zen_2",
   "p_x_zen_3",
   "p_x_zen_4",
   "p_x_zen_5",
   "p_x_zen_6",
   "ig_zen"
  ],
  "making": []
 },
 {
  "slug": "baxters",
  "old": None,
  "name": "Baxter's",
  "where": None,
  "sector": "retail",
  "types": [
   "3d-letters"
  ],
  "hero": "p_x_baxters_0",
  "label": "3D script letters",
  "lede": "A large script logo in 3D letters along the roofline.",
  "brief": "A big, readable logo on a plain building.",
  "made": [
   [
    "3D letters",
    "Script lettering with a red outline, fixed above the shutters."
   ]
  ],
  "result": "A plain unit with a logo you can't miss.",
  "photos": [
   "p_x_baxters_0",
   "p_x_baxters_1",
   "p_x_baxters_2",
   "p_g_baxters"
  ],
  "making": []
 },
 {
  "slug": "renewable-energy",
  "old": None,
  "name": "Renewable Energy Management",
  "where": None,
  "sector": "commercial",
  "types": [
   "3d-letters"
  ],
  "hero": "p_x_renewablee_0",
  "label": "Halo-lit 3D letters",
  "lede": "Halo-lit 3D letters and logo on timber cladding.",
  "brief": "A lit sign that works on slatted timber, day and night.",
  "made": [
   [
    "Halo-lit letters",
    "Letters and logo that glow onto the timber behind."
   ],
   [
    "Fixing",
    "Fitted to the slatted cladding."
   ]
  ],
  "result": "A building sign that glows warm after dark.",
  "photos": [
   "p_x_renewablee_0",
   "p_x_renewablee_1",
   "n_renew_close",
   "n_renew_bld"
  ],
  "making": [
   "p_x_renewablee_m0",
   "p_x_renewablee_m1"
  ]
 },
 {
  "slug": "workwear-express",
  "old": None,
  "name": "Workwear Express",
  "where": None,
  "sector": "commercial",
  "types": [
   "vinyl-wall-graphics",
   "wayfinding"
  ],
  "hero": "p_x_workwearex_0",
  "label": "Office wall graphics",
  "lede": "Printed wall graphics and room signs for a head office.",
  "brief": "Workwear Express wanted the brand on every wall of its office.",
  "made": [
   [
    "Wall graphics",
    "Large printed walls in the brand orange."
   ],
   [
    "Room signs",
    "Meeting room and office signs to match."
   ]
  ],
  "result": "An office that feels like the brand.",
  "photos": [
   "p_x_workwearex_0",
   "p_x_workwearex_1",
   "p_x_workwearex_2",
   "p_x_workwearex_3",
   "p_x_workwearex_4",
   "p_x_workwearex_5",
   "n_workwear_wall"
  ],
  "making": []
 },
 {
  "slug": "lomond",
  "old": None,
  "name": "Lomond Property Maintenance",
  "where": None,
  "sector": "transport",
  "types": [
   "vehicle-graphics"
  ],
  "hero": "p_x_lomond_0",
  "label": "Van graphics",
  "lede": "Cut vinyl graphics for a property maintenance van.",
  "brief": "Clear branding on the back and sides of the van.",
  "made": [
   [
    "Van graphics",
    "Logo and contact details in cut vinyl."
   ]
  ],
  "result": "A van that advertises the business everywhere it goes.",
  "photos": [
   "p_x_lomond_0",
   "p_g_lomond"
  ],
  "making": []
 },
 {
  "slug": "park-electrical",
  "old": None,
  "name": "Park Electrical Distributors",
  "where": None,
  "sector": "transport",
  "types": [
   "vehicle-graphics"
  ],
  "hero": "p_x_parkelectr_0",
  "label": "Van graphics",
  "lede": "Full-colour van graphics for an electrical distributor.",
  "brief": "Bold, recognisable graphics for the company vans.",
  "made": [
   [
    "Van graphics",
    "Printed and cut graphics in the brand colours."
   ]
  ],
  "result": "Vans that stand out on the road.",
  "photos": [
   "p_x_parkelectr_0",
   "ig_park2",
   "ig_park"
  ],
  "making": []
 },
 {
  "slug": "aykley-group",
  "old": None,
  "name": "Aykley Group",
  "where": None,
  "sector": "commercial",
  "types": [
   "3d-letters"
  ],
  "hero": "p_x_aykleygrou_0",
  "label": "Lettering",
  "lede": "Lit 3D lettering and wall lettering for an office.",
  "brief": "A reception sign and wall lettering for the business.",
  "made": [
   [
    "3D letters",
    "Lit lettering on a panel."
   ],
   [
    "Wall lettering",
    "Lettering beside a living wall."
   ]
  ],
  "result": "A reception that shows off the brand.",
  "photos": [
   "p_x_aykleygrou_0",
   "p_x_aykleygrou_1"
  ],
  "making": []
 },
 {
  "slug": "dunelm-food-store",
  "old": None,
  "name": "Dunelm Food Store",
  "where": None,
  "sector": "retail",
  "types": [
   "digital-large-format-print"
  ],
  "hero": "p_x_dunelmfood_0",
  "label": "Printed fascia and windows",
  "lede": "A printed fascia and window graphics for a convenience store.",
  "brief": "A clear fascia and windows that list what the shop sells.",
  "made": [
   [
    "Fascia",
    "A printed fascia panel."
   ],
   [
    "Window graphics",
    "Product lists printed on the windows."
   ]
  ],
  "result": "A shop people know what to expect from.",
  "photos": [
   "p_x_dunelmfood_0",
   "p_x_dunelmfood_1"
  ],
  "making": []
 },
 {
  "slug": "maker",
  "old": None,
  "name": "Maker",
  "where": None,
  "sector": "commercial",
  "types": [
   "vinyl-wall-graphics"
  ],
  "hero": "p_x_maker_0",
  "label": "Window graphics",
  "lede": "Window graphics for empty units in a new development.",
  "brief": "Vacant units that look inviting to new tenants.",
  "made": [
   [
    "Window graphics",
    "Printed graphics across the glazing of each unit."
   ]
  ],
  "result": "Empty units that look ready to let.",
  "photos": [
   "p_x_maker_0",
   "p_x_maker_1",
   "p_x_maker_2",
   "p_x_maker_3",
   "p_g_fab"
  ],
  "making": []
 },
 {
  "slug": "bar-marquee",
  "old": None,
  "name": "BAR marquee letters",
  "where": None,
  "sector": "hospitality-leisure",
  "types": [
   "3d-letters"
  ],
  "hero": "p_x_barmarquee_0",
  "label": "Marquee letters",
  "lede": "Red marquee letters with bulbs, mounted on a roof.",
  "brief": "A bar sign that could be seen from far away.",
  "made": [
   [
    "Marquee letters",
    "Fabricated letters with bulbs, painted red."
   ],
   [
    "Roof frame",
    "Mounted on a frame on the roof."
   ]
  ],
  "result": "A sign you can see from far away.",
  "photos": [
   "p_x_barmarquee_0",
   "p_x_barmarquee_1",
   "p_x_barmarquee_2",
   "p_x_barmarquee_3",
   "p_g_marquee"
  ],
  "making": []
 },
 {
  "slug": "le-gavroche",
  "old": None,
  "name": "Le Gavroche",
  "where": None,
  "sector": "hospitality-leisure",
  "types": [
   "light-boxes"
  ],
  "hero": "p_x_legavroche_0",
  "label": "Light box",
  "lede": "An illuminated light box sign.",
  "brief": "A light box lit evenly across the face.",
  "made": [
   [
    "Light box",
    "A box lit by LEDs with a printed face."
   ]
  ],
  "result": "A sign that glows evenly day and night.",
  "photos": [
   "p_x_legavroche_0",
   "ig_gavroche"
  ],
  "making": []
 },
 {
  "slug": "menu",
  "old": None,
  "name": "Menu",
  "where": None,
  "sector": "hospitality-leisure",
  "types": [
   "3d-letters"
  ],
  "hero": "p_x_menu_0",
  "label": "Illuminated lettering",
  "lede": "Illuminated lettering on a timber-clad restaurant front.",
  "brief": "A lit logo for the restaurant frontage.",
  "made": [
   [
    "Illuminated letters",
    "Lettering with a lit outline, fixed to timber cladding."
   ]
  ],
  "result": "A frontage that glows in the evening.",
  "photos": [
   "p_x_menu_0",
   "p_x_menu_1",
   "p_x_menu_2",
   "p_x_menu_3"
  ],
  "making": [
   "p_x_menu_m0",
   "p_x_menu_m1",
   "p_x_menu_m2",
   "p_x_menu_m3"
  ]
 },
 {
  "slug": "the-vault",
  "old": None,
  "name": "The Vault",
  "where": None,
  "sector": "hospitality-leisure",
  "types": [
   "3d-letters"
  ],
  "hero": "p_x_thevault_0",
  "label": "Halo-lit letters",
  "lede": "Halo-lit fabricated letters for a bar.",
  "brief": "Lit signage that suits a dark, moody interior.",
  "made": [
   [
    "Halo-lit letters",
    "Fabricated letters glowing onto the panel behind."
   ],
   [
    "Logo",
    "A lit V logo."
   ]
  ],
  "result": "Signs that set the mood.",
  "photos": [
   "p_x_thevault_0",
   "p_x_thevault_1",
   "vault"
  ],
  "making": []
 },
 {
  "slug": "the-cove",
  "old": None,
  "name": "The Cove",
  "where": None,
  "sector": "hospitality-leisure",
  "types": [
   "3d-letters"
  ],
  "hero": "p_x_thecove_0",
  "label": "3D letters",
  "lede": "Large white 3D letters over a bar entrance.",
  "brief": "A big, simple logo on a brick frontage.",
  "made": [
   [
    "3D letters",
    "Fabricated letters in white, fixed to the brickwork."
   ]
  ],
  "result": "A logo you can read from across the street.",
  "photos": [
   "p_x_thecove_0",
   "p_x_thecove_1",
   "p_g_cove"
  ],
  "making": [
   "p_x_thecove_m0",
   "p_x_thecove_m1",
   "p_x_thecove_m2",
   "p_x_thecove_m3",
   "p_x_thecove_m4"
  ]
 },
 {
  "slug": "bratz-salon",
  "old": None,
  "name": "Bratz Salon",
  "where": None,
  "sector": "hair-beauty",
  "types": [
   "3d-letters"
  ],
  "hero": "p_x_bratzsalon_0",
  "label": "3D letter fascia",
  "lede": "Pink and gold 3D letters for a salon fascia.",
  "brief": "A fun fascia that matches the salon brand.",
  "made": [
   [
    "3D letters",
    "Pink letters with a gold script."
   ]
  ],
  "result": "A fascia that suits the brand.",
  "photos": [
   "p_x_bratzsalon_0",
   "p_g_bratz"
  ],
  "making": []
 },
 {
  "slug": "tipsy",
  "old": None,
  "name": "Tipsy",
  "where": None,
  "sector": "hospitality-leisure",
  "types": [
   "3d-letters"
  ],
  "hero": "p_x_tipsy_0",
  "label": "3D letters",
  "lede": "Gold lettering on a white shopfront.",
  "brief": "A simple, smart fascia.",
  "made": [
   [
    "Letters",
    "Gold letters on a white frontage."
   ]
  ],
  "result": "A clean shopfront.",
  "photos": [
   "p_x_tipsy_0"
  ],
  "making": []
 },
 {
  "slug": "copeland-residential",
  "old": None,
  "name": "Copeland Residential",
  "where": None,
  "sector": "commercial",
  "types": [
   "3d-letters"
  ],
  "hero": "p_x_copelandre_0",
  "label": "3D letters on brick",
  "lede": "3D letters on brickwork for an estate agent.",
  "brief": "Lettering fixed straight onto the building.",
  "made": [
   [
    "3D letters",
    "Letters fixed to the brickwork."
   ]
  ],
  "result": "A smart sign that suits the building.",
  "photos": [
   "p_x_copelandre_0",
   "p_x_copelandre_1"
  ],
  "making": []
 },
 {
  "slug": "parm-o-rama",
  "old": None,
  "name": "Parm-o-rama",
  "where": None,
  "sector": "hospitality-leisure",
  "types": [
   "3d-letters"
  ],
  "hero": "p_x_parmorama_0",
  "label": "3D letter fascia",
  "lede": "Bright yellow 3D letters on a grey fascia.",
  "brief": "A loud, fun fascia for a takeaway.",
  "made": [
   [
    "3D letters",
    "Yellow letters and logo on a grey fascia."
   ]
  ],
  "result": "A fascia that is hard to miss.",
  "photos": [
   "p_x_parmorama_0",
   "p_g_parmo"
  ],
  "making": []
 },
 {
  "slug": "glo-studios",
  "old": None,
  "name": "Glo Studios",
  "where": None,
  "sector": "hair-beauty",
  "types": [],
  "hero": "p_x_glostudios_0",
  "label": "Fascia",
  "lede": "A fascia and window graphics for a studio.",
  "brief": "A simple frontage.",
  "made": [
   [
    "Fascia",
    "Logo on the fascia."
   ],
   [
    "Window graphics",
    "Logo on the windows."
   ]
  ],
  "result": "A clean, simple frontage.",
  "photos": [
   "p_x_glostudios_0"
  ],
  "making": []
 },
 {
  "slug": "dream-dolls",
  "old": None,
  "name": "Dream Dolls",
  "where": None,
  "sector": "hair-beauty",
  "types": [],
  "hero": "p_x_dreamdolls_0",
  "label": "Illuminated arch",
  "lede": "An illuminated arch sign.",
  "brief": "A lit feature for the salon.",
  "made": [
   [
    "Illuminated arch",
    "An arch with LED lighting around the edge."
   ]
  ],
  "result": "A feature made for photos.",
  "photos": [
   "p_x_dreamdolls_0",
   "p_x_dreamdolls_1"
  ],
  "making": []
 },
 {
  "slug": "my-car-cleaning",
  "old": None,
  "name": "My Car Cleaning",
  "where": None,
  "sector": "commercial",
  "types": [
   "3d-letters"
  ],
  "hero": "p_x_mycarclean_0",
  "label": "3D letters",
  "lede": "3D lettering for a car cleaning business.",
  "brief": "A simple sign for the business.",
  "made": [
   [
    "3D letters",
    "Fabricated lettering."
   ]
  ],
  "result": "A clear sign for the business.",
  "photos": [
   "p_x_mycarclean_0"
  ],
  "making": []
 },
 {
  "slug": "merz-court",
  "old": None,
  "name": "Merz Court",
  "where": None,
  "sector": "education",
  "types": [],
  "hero": "p_x_merzcourt_0",
  "label": "Building sign",
  "lede": "A building name sign.",
  "brief": "A clear name sign on the building.",
  "made": [
   [
    "Name sign",
    "Lettering on a panel."
   ]
  ],
  "result": "A building that is easy to find.",
  "photos": [
   "p_x_merzcourt_0"
  ],
  "making": []
 },
 {
  "slug": "originals-glow",
  "old": None,
  "name": "Originals Glow",
  "where": None,
  "sector": "hair-beauty",
  "types": [],
  "hero": "p_x_originalsg_0",
  "label": "Illuminated fascia",
  "lede": "An illuminated 3D letter fascia, built in our workshop.",
  "brief": "A lit fascia for a tanning salon.",
  "made": [
   [
    "Illuminated letters",
    "Lit letters on a black panel with a gold frame."
   ]
  ],
  "result": "Built and tested in our workshop before fitting.",
  "photos": [
   "p_x_originalsg_0",
   "p_x_originalsg_1",
   "p_x_originalsg_2"
  ],
  "making": []
 },
 {
  "slug": "black-rabbit",
  "old": None,
  "name": "Black Rabbit",
  "where": None,
  "sector": "hospitality-leisure",
  "types": [],
  "hero": "p_x_blackrabbi_0",
  "label": "Printed fascia panel",
  "lede": "A black and gold fascia panel, built in our workshop.",
  "brief": "A detailed gold illustration on a black fascia.",
  "made": [
   [
    "Fascia panel",
    "Black panel with gold artwork and lettering."
   ]
  ],
  "result": "Built in our workshop before fitting.",
  "photos": [
   "p_x_blackrabbi_0",
   "p_x_blackrabbi_1",
   "p_x_blackrabbi_2"
  ],
  "making": []
 },
 {
  "slug": "olivias",
  "old": None,
  "name": "Olivia's",
  "where": None,
  "sector": "hospitality-leisure",
  "types": [],
  "hero": "p_x_olivias_0",
  "label": "Fascia panel",
  "lede": "A fascia panel for a coffee, ice cream and dessert shop.",
  "brief": "A soft pink panel with elegant script lettering.",
  "made": [
   [
    "Fascia panel",
    "Pink panel with script lettering."
   ]
  ],
  "result": "Built in our workshop before fitting.",
  "photos": [
   "p_x_olivias_0",
   "p_x_olivias_1",
   "p_x_olivias_2"
  ],
  "making": []
 },
 {
  "slug": "kiss-me-irish",
  "old": None,
  "name": "Kiss Me I'm Irish",
  "where": None,
  "sector": "hospitality-leisure",
  "types": [],
  "hero": "p_x_kissmeiris_0",
  "label": "Illuminated sign",
  "lede": "An illuminated sign, built in our workshop.",
  "brief": "A bright green sign with a lit edge.",
  "made": [
   [
    "Illuminated sign",
    "Green panel with lettering and a lit edge."
   ]
  ],
  "result": "Built and tested in our workshop.",
  "photos": [
   "p_x_kissmeiris_0",
   "p_x_kissmeiris_1",
   "p_x_kissmeiris_2"
  ],
  "making": []
 },
 {
  "slug": "unstoppable-hq",
  "old": None,
  "name": "Unstoppable HQ",
  "where": None,
  "sector": "commercial",
  "types": [],
  "hero": "p_x_unstoppabl_0",
  "label": "3D letters",
  "lede": "Large 3D letters, built in our workshop.",
  "brief": "Big building letters for a new HQ.",
  "made": [
   [
    "3D letters",
    "Large fabricated letters."
   ]
  ],
  "result": "Built in our workshop before fitting.",
  "photos": [
   "p_x_unstoppabl_0",
   "p_x_unstoppabl_1",
   "p_x_unstoppabl_2"
  ],
  "making": []
 },
 {
  "slug": "combat-96",
  "old": None,
  "name": "Combat 96",
  "where": None,
  "sector": "hospitality-leisure",
  "types": [],
  "hero": "p_x_combat96_0",
  "label": "Illuminated sign",
  "lede": "An illuminated 3D letter sign, built in our workshop.",
  "brief": "A bold lit sign in the brand colours.",
  "made": [
   [
    "Illuminated letters",
    "Lit white and purple letters on a black panel."
   ]
  ],
  "result": "Built and tested in our workshop.",
  "photos": [
   "p_x_combat96_0",
   "p_x_combat96_1",
   "p_x_combat96_2"
  ],
  "making": []
 },
 {
  "slug": "assenheims-56",
  "old": None,
  "name": "Assenheims 56",
  "where": None,
  "sector": "hospitality-leisure",
  "types": [],
  "hero": "p_x_assenheims_0",
  "label": "Laser-cut sign",
  "lede": "A laser-cut metal sign, made in our workshop.",
  "brief": "A round cut-metal logo sign.",
  "made": [
   [
    "Laser-cut sign",
    "The logo cut from metal sheet."
   ]
  ],
  "result": "Cut and finished in our workshop.",
  "photos": [
   "p_x_assenheims_0",
   "p_x_assenheims_1"
  ],
  "making": []
 },
 {
  "slug": "aspire-health-group",
  "old": None,
  "name": "Aspire Health Group",
  "where": None,
  "sector": "healthcare",
  "types": [],
  "hero": "p_x_aspireheal_0",
  "label": "Sign panel",
  "lede": "A printed sign panel for a health group.",
  "brief": "A clean panel with the logo.",
  "made": [
   [
    "Sign panel",
    "Logo on a white panel."
   ]
  ],
  "result": "Made in our workshop before fitting.",
  "photos": [
   "p_x_aspireheal_0",
   "p_x_aspireheal_1"
  ],
  "making": []
 },
 {
  "slug": "level",
  "old": None,
  "name": "Level",
  "where": None,
  "sector": "hospitality-leisure",
  "types": [],
  "hero": "p_x_level_0",
  "label": "3D letters",
  "lede": "3D letters, built in our workshop.",
  "brief": "Fabricated letters for the business.",
  "made": [
   [
    "3D letters",
    "Fabricated letters."
   ]
  ],
  "result": "Built in our workshop before fitting.",
  "photos": [
   "p_x_level_0",
   "p_x_level_1"
  ],
  "making": []
 },
 {
  "slug": "nobles-casino",
  "old": None,
  "name": "Nobles Casino Gaming",
  "where": None,
  "sector": "hospitality-leisure",
  "types": [],
  "hero": "p_x_noblescasi_0",
  "label": "Fascia panel",
  "lede": "A fascia panel for a casino arcade.",
  "brief": "A bright fascia in the brand colours.",
  "made": [
   [
    "Fascia panel",
    "Panel with lettering in the brand colours."
   ]
  ],
  "result": "Made in our workshop before fitting.",
  "photos": [
   "p_x_noblescasi_0"
  ],
  "making": []
 }
]
for _c in NEW2: _c['made'] = [tuple(m) for m in _c['made']]
CASES += NEW2
# near-identical frames removed after a duplicate check
_DROP = {"p_x_barmarquee_0","p_x_barmarquee_1","p_x_maker_0","p_x_maker_2","p_x_thecove_1","p_x_bratzsalon_0","p_x_parmorama_0",
         "p_x_baxters_1","p_x_lomond_0","p_x_goodlashga_0","p_x_renewablee_m0","p_x_workwearex_1","p_x_combat96_1","p_x_fora_0",
         "p_x_kissmeiris_1","p_x_menu_2","n_skinsoul","p_x_originalsg_1","p_x_level_1","p_x_skinandsou_2","p_x_menu_3"}
for _c in NEW2:
    _c["photos"] = [p for p in _c["photos"] if p not in _DROP]
    _c["making"] = [p for p in _c["making"] if p not in _DROP]
    if _c["hero"] in _DROP: _c["hero"] = _c["photos"][0]

for _c in CASES:
    if _c["slug"] == "dunelm-food-store": _c["types"] = ["3d-letters"]; _c["label"] = "3D letter fascia"

# ---- Part 2 folder (Nov 2026)
NEW3 = [
 {
  "slug": "better-you",
  "old": None,
  "name": "Better You",
  "where": None,
  "sector": "hair-beauty",
  "types": [
   "3d-letters"
  ],
  "hero": "p_y_betteryou_0",
  "label": "3D logo wall",
  "lede": "3D letters and logo for a medical aesthetics and skin clinic.",
  "brief": "A logo wall that sets a premium tone in the treatment rooms.",
  "made": [
   [
    "3D logo",
    "Logo and lettering standing off the feature wall."
   ]
  ],
  "result": "A clinic that looks as polished as its treatments.",
  "photos": [
   "p_y_betteryou_0",
   "p_y_betteryou_1",
   "p_y_betteryou_2",
   "p_y_betteryou_3"
  ],
  "making": []
 },
 {
  "slug": "little-her-hair",
  "old": None,
  "name": "Little Her Hair",
  "where": None,
  "sector": "hair-beauty",
  "types": [
   "3d-letters"
  ],
  "hero": "p_y_littleherh_0",
  "label": "Shopfront lettering",
  "lede": "Lettering on a white fascia with matching window graphics.",
  "brief": "A clean, simple shopfront for a hair salon.",
  "made": [
   [
    "Fascia lettering",
    "Black letters on a white fascia."
   ],
   [
    "Window graphics",
    "Logo on the frosted glazing."
   ]
  ],
  "result": "A tidy shopfront that matches the salon.",
  "photos": [
   "p_y_littleherh_0",
   "p_y_littleherh_1"
  ],
  "making": []
 },
 {
  "slug": "fawcett-street-community-shop",
  "old": None,
  "name": "Fawcett Street Community Shop",
  "where": None,
  "sector": "retail",
  "types": [
   "vinyl-wall-graphics",
   "wayfinding"
  ],
  "hero": "p_y_fawcettstr_0",
  "label": "Wall graphics",
  "lede": "Full wall graphics, wayfinding and story panels for a community shop and kitchen supported by Ocado.",
  "brief": "The community shop wanted bright, friendly walls that tell its story.",
  "made": [
   [
    "Wall graphics",
    "Printed walls in the shop and community kitchen."
   ],
   [
    "Wayfinding",
    "Toilets and menu graphics in the same style."
   ]
  ],
  "result": "A welcoming space that tells people what it is about.",
  "photos": [
   "p_y_fawcettstr_0",
   "p_y_fawcettstr_1",
   "p_y_fawcettstr_2",
   "p_y_fawcettstr_3",
   "p_y_fawcettstr_4",
   "p_y_fawcettstr_5"
  ],
  "making": []
 },
 {
  "slug": "amethyst",
  "old": None,
  "name": "Amethyst Acupuncture & Holistics",
  "where": None,
  "sector": "hair-beauty",
  "types": [
   "3d-letters"
  ],
  "hero": "p_y_amethyst_0",
  "label": "3D logo on a fascia panel",
  "lede": "A 3D flower logo and lettering on a white fascia panel.",
  "brief": "A bright fascia that shows off the logo.",
  "made": [
   [
    "3D logo",
    "Raised purple flower logo and lettering on a panel."
   ]
  ],
  "result": "A fascia that stands out on the street.",
  "photos": [
   "p_y_amethyst_0",
   "p_y_amethyst_1",
   "p_y_amethyst_2"
  ],
  "making": []
 },
 {
  "slug": "jam-jar",
  "old": None,
  "name": "Jam Jar",
  "where": None,
  "sector": "hospitality-leisure",
  "types": [
   "vinyl-wall-graphics"
  ],
  "hero": "p_y_jamjar_0",
  "label": "Wall lettering",
  "lede": "Large cut lettering on a feature wall.",
  "brief": "A bold brand wall for a Jesmond bar.",
  "made": [
   [
    "Wall lettering",
    "Large lettering on a painted wall."
   ]
  ],
  "result": "A wall that people remember.",
  "photos": [
   "p_y_jamjar_0",
   "p_y_jamjar_1"
  ],
  "making": []
 },
 {
  "slug": "country",
  "old": None,
  "name": "Country",
  "where": None,
  "sector": "hospitality-leisure",
  "types": [
   "3d-letters"
  ],
  "hero": "p_y_country_0",
  "label": "Illuminated letters",
  "lede": "Illuminated letters above a bar stage.",
  "brief": "A lit sign for the stage area.",
  "made": [
   [
    "Illuminated letters",
    "Lit letters over the stage."
   ]
  ],
  "result": "A stage that looks the part.",
  "photos": [
   "p_y_country_0",
   "p_y_country_1",
   "p_y_country_2"
  ],
  "making": []
 },
 {
  "slug": "lean-cuisine",
  "old": None,
  "name": "Lean Cuisine",
  "where": None,
  "sector": "hospitality-leisure",
  "types": [
   "neon-led-neon"
  ],
  "hero": "p_y_leancuisin_0",
  "label": "LED neon and branding",
  "lede": "An LED neon logo, counter branding and window graphics.",
  "brief": "Lean Cuisine wanted its brand from the window to the counter.",
  "made": [
   [
    "LED neon",
    "A round neon logo on a dark wall."
   ],
   [
    "Counter and windows",
    "Logo on the counter and window frosting."
   ]
  ],
  "result": "A brand you see everywhere in the shop.",
  "photos": [
   "p_y_leancuisin_0",
   "p_y_leancuisin_1",
   "p_y_leancuisin_2"
  ],
  "making": []
 },
 {
  "slug": "craft-and-crumb",
  "old": None,
  "name": "Craft & Crumb",
  "where": None,
  "sector": "hospitality-leisure",
  "types": [
   "3d-letters",
   "vinyl-wall-graphics"
  ],
  "hero": "p_y_craftandcr_0",
  "label": "Shopfront and interior",
  "lede": "Fascia lettering, window graphics and counter branding for a coffee bar.",
  "brief": "One clean look outside and in.",
  "made": [
   [
    "Fascia lettering",
    "Lettering on the fascia."
   ],
   [
    "Interior",
    "Lit lettering, counter logo and window graphics."
   ]
  ],
  "result": "A coffee bar that looks finished in every corner.",
  "photos": [
   "p_y_craftandcr_0",
   "p_y_craftandcr_1",
   "p_y_craftandcr_2",
   "p_y_craftandcr_3",
   "p_y_craftandcr_4"
  ],
  "making": []
 },
 {
  "slug": "sunderland-eye-hospital",
  "old": None,
  "name": "Sunderland Specialist Eye Hospital",
  "where": None,
  "sector": "healthcare",
  "types": [
   "wayfinding",
   "totems-monoliths"
  ],
  "hero": "p_y_sunderland_0",
  "label": "Wayfinding and totem",
  "lede": "Directional signs and a site totem for a hospital.",
  "brief": "Clear routes for patients and ambulances.",
  "made": [
   [
    "Wayfinding",
    "Directional signs along the corridors."
   ],
   [
    "Totem",
    "A site totem with car park and drop-off directions."
   ]
  ],
  "result": "A site that is easy to find your way around.",
  "photos": [
   "p_y_sunderland_0",
   "p_y_sunderland_1",
   "p_y_sunderland_2",
   "p_y_sunderland_3"
  ],
  "making": []
 },
 {
  "slug": "temple-tacos",
  "old": None,
  "name": "Temple Tacos",
  "where": None,
  "sector": "hospitality-leisure",
  "types": [
   "neon-led-neon"
  ],
  "hero": "p_y_templetaco_0",
  "label": "LED neon",
  "lede": "A blue LED neon sign.",
  "brief": "A bright neon feature.",
  "made": [
   [
    "LED neon",
    "Blue neon lettering."
   ]
  ],
  "result": "A sign made for photos.",
  "photos": [
   "p_y_templetaco_0"
  ],
  "making": []
 },
 {
  "slug": "filto",
  "old": None,
  "name": "Filto",
  "where": None,
  "sector": "hospitality-leisure",
  "types": [
   "3d-letters",
   "digital-large-format-print"
  ],
  "hero": "p_y_filto_0",
  "label": "Fascia and hoarding",
  "lede": "3D letters on the shopfront, interior lettering and printed hoarding.",
  "brief": "Filto needed the opening hyped up and a strong shopfront.",
  "made": [
   [
    "3D letters",
    "Letters on the corner fascia."
   ],
   [
    "Hoarding",
    "Printed hoarding while the unit was fitted out."
   ]
  ],
  "result": "A launch people noticed.",
  "photos": [
   "p_y_filto_0",
   "p_y_filto_1",
   "p_y_filto_2",
   "p_y_filto_3",
   "p_y_filto_4"
  ],
  "making": []
 },
 {
  "slug": "salto",
  "old": None,
  "name": "Salto",
  "where": None,
  "sector": "transport",
  "types": [
   "vehicle-graphics"
  ],
  "hero": "p_y_salto_0",
  "label": "Van graphics",
  "lede": "Printed van graphics for a cleaning company.",
  "brief": "A fleet that looks smart on the road.",
  "made": [
   [
    "Van graphics",
    "Printed graphics across the sides and back."
   ]
  ],
  "result": "Vans that advertise the business everywhere.",
  "photos": [
   "p_y_salto_0",
   "p_y_salto_1",
   "p_y_salto_2",
   "p_y_salto_3"
  ],
  "making": []
 },
 {
  "slug": "the-lumen",
  "old": None,
  "name": "The Lumen",
  "where": None,
  "sector": "commercial",
  "types": [
   "3d-letters"
  ],
  "hero": "p_y_thelumen_0",
  "label": "3D letters",
  "lede": "3D letters on a dark wall.",
  "brief": "A clean name sign for the building.",
  "made": [
   [
    "3D letters",
    "Letters fixed to the wall."
   ]
  ],
  "result": "A smart name sign.",
  "photos": [
   "p_y_thelumen_0"
  ],
  "making": []
 },
 {
  "slug": "alba",
  "old": None,
  "name": "Alba Ristorante",
  "where": None,
  "sector": "hospitality-leisure",
  "types": [
   "projecting-signs",
   "flat-cut-letters"
  ],
  "hero": "p_y_alba_0",
  "label": "Plaque and canopy",
  "lede": "A logo plaque and canopy lettering for a restaurant.",
  "brief": "A refined look for the restaurant entrance.",
  "made": [
   [
    "Logo plaque",
    "A logo plaque beside the entrance."
   ],
   [
    "Canopy",
    "Lettering on the canopy."
   ]
  ],
  "result": "An entrance that suits the restaurant.",
  "photos": [
   "p_y_alba_0",
   "p_y_alba_1",
   "p_y_alba_2"
  ],
  "making": []
 },
 {
  "slug": "newstreet",
  "old": None,
  "name": "Newstreet Groundwork Services",
  "where": None,
  "sector": "commercial",
  "types": [
   "3d-letters"
  ],
  "hero": "p_y_newstreet_0",
  "label": "3D logo",
  "lede": "A 3D logo with halo detail on a reception wall.",
  "brief": "A reception logo for a groundworks firm.",
  "made": [
   [
    "3D logo",
    "Logo and lettering standing off the wall."
   ]
  ],
  "result": "A reception that shows off the brand.",
  "photos": [
   "p_y_newstreet_0",
   "p_y_newstreet_1",
   "p_y_newstreet_2",
   "p_y_newstreet_3"
  ],
  "making": []
 },
 {
  "slug": "fabios",
  "old": None,
  "name": "Fabio's",
  "where": None,
  "sector": "transport",
  "types": [
   "vehicle-graphics"
  ],
  "hero": "p_y_fabios_0",
  "label": "Van graphics",
  "lede": "Cut vinyl van graphics for an Italian restaurant.",
  "brief": "Branded vans for deliveries.",
  "made": [
   [
    "Van graphics",
    "Logo and contact details in cut vinyl."
   ]
  ],
  "result": "Vans that advertise the restaurant.",
  "photos": [
   "p_y_fabios_0",
   "p_y_fabios_1",
   "p_y_fabios_2"
  ],
  "making": []
 },
 {
  "slug": "the-drunken-duck",
  "old": None,
  "name": "The Drunken Duck",
  "where": None,
  "sector": "hospitality-leisure",
  "types": [
   "neon-led-neon"
  ],
  "hero": "p_y_thedrunken_0",
  "label": "LED neon",
  "lede": "A script LED neon sign.",
  "brief": "A warm neon feature for a bar.",
  "made": [
   [
    "LED neon",
    "Script neon in warm orange."
   ]
  ],
  "result": "A bar feature people photograph.",
  "photos": [
   "p_y_thedrunken_0"
  ],
  "making": []
 },
 {
  "slug": "avery-dennison",
  "old": None,
  "name": "Avery Dennison",
  "where": None,
  "sector": "commercial",
  "types": [
   "vinyl-wall-graphics"
  ],
  "hero": "p_y_averydenni_0",
  "label": "Wall mural",
  "lede": "A printed wall mural with local landmarks.",
  "brief": "A feature wall for an office.",
  "made": [
   [
    "Wall mural",
    "A printed mural with the logo and local landmarks."
   ]
  ],
  "result": "An office wall with local pride.",
  "photos": [
   "p_y_averydenni_0",
   "p_y_averydenni_1",
   "p_y_averydenni_2"
  ],
  "making": []
 },
 {
  "slug": "dog-and-parrot",
  "old": None,
  "name": "The Dog & Parrot",
  "where": None,
  "sector": "hospitality-leisure",
  "types": [
   "3d-letters",
   "vinyl-wall-graphics"
  ],
  "hero": "p_y_dogandparr_0",
  "label": "3D letters and murals",
  "lede": "Brass 3D letters and painted murals for a Newcastle pub.",
  "brief": "A frontage people stop and look at.",
  "made": [
   [
    "3D letters",
    "Brass lettering across the fascia."
   ],
   [
    "Murals",
    "Large painted murals on the building."
   ]
  ],
  "result": "A pub you can't walk past.",
  "photos": [
   "p_y_dogandparr_0",
   "p_y_dogandparr_1",
   "p_y_dogandparr_2",
   "p_y_dogandparr_3"
  ],
  "making": []
 },
 {
  "slug": "the-avenue",
  "old": None,
  "name": "The Avenue",
  "where": None,
  "sector": "hospitality-leisure",
  "types": [
   "3d-letters"
  ],
  "hero": "p_y_theavenue_0",
  "label": "3D letter fascia",
  "lede": "Gold 3D letters on a blue fascia for a café and deli.",
  "brief": "A traditional look for a corner café.",
  "made": [
   [
    "3D letters",
    "Gold letters on the fascia."
   ]
  ],
  "result": "A café that looks established.",
  "photos": [
   "p_y_theavenue_0",
   "p_y_theavenue_1",
   "p_y_theavenue_2",
   "p_y_theavenue_3"
  ],
  "making": []
 },
 {
  "slug": "street-eats",
  "old": None,
  "name": "Street Eats",
  "where": None,
  "sector": "hospitality-leisure",
  "types": [
   "3d-letters"
  ],
  "hero": "p_y_streeteats_0",
  "label": "Letters on a food trailer",
  "lede": "Gold 3D letters on the roof of a food trailer.",
  "brief": "Branding for a street food trailer.",
  "made": [
   [
    "3D letters",
    "Letters mounted on the trailer roof."
   ]
  ],
  "result": "A trailer people spot from across the event.",
  "photos": [
   "p_y_streeteats_0",
   "p_y_streeteats_1",
   "p_y_streeteats_2"
  ],
  "making": []
 },
 {
  "slug": "act-group",
  "old": None,
  "name": "ACT Group",
  "where": None,
  "sector": "commercial",
  "types": [
   "3d-letters"
  ],
  "hero": "p_y_actgroup_0",
  "label": "Building letters and plaques",
  "lede": "3D letters on the building, plaques and van branding.",
  "brief": "ACT Group wanted its brand on the building and inside.",
  "made": [
   [
    "3D letters",
    "Letters on the cladding."
   ],
   [
    "Plaques",
    "Printed plaques in reception."
   ]
  ],
  "result": "A building that looks like head office.",
  "photos": [
   "p_y_actgroup_0",
   "p_y_actgroup_1",
   "p_y_actgroup_2",
   "p_y_actgroup_3"
  ],
  "making": []
 },
 {
  "slug": "houghton-colliery",
  "old": None,
  "name": "Houghton Colliery Retail Park",
  "where": None,
  "sector": "retail",
  "types": [
   "totems-monoliths"
  ],
  "hero": "p_y_houghtonco_0",
  "label": "Retail park totem",
  "lede": "A large retail park totem, lifted in by crane.",
  "brief": "A totem listing every tenant.",
  "made": [
   [
    "Totem",
    "A tall double-sided totem with tenant panels."
   ]
  ],
  "result": "A site you can find from the road.",
  "photos": [
   "p_y_houghtonco_0"
  ],
  "making": []
 }
]
for _c in NEW3: _c['made'] = [tuple(m) for m in _c['made']]
CASES += NEW3
_ADD3 = {"company-shop-group": [["p_z_companysho_0", False], ["p_z_companysho_1", False], ["p_z_companysho_2", False], ["p_z_companysho_3", False], ["p_z_companysho_4", False]], "nhs-community-diagnostic-centre": [["p_z_nhscommuni_0", False], ["p_z_nhscommuni_1", False]], "savoy": [["p_z_savoy_0", False], ["p_z_savoy_1", False]], "my-car-cleaning": [["p_z_mycarclean_0", True]], "nobles-casino": [["p_z_noblescasi_0", True]], "fora": [["p_z_fora_0", False]], "the-chair": [["p_z_thechair_0", False]], "vivana-lounge": [["p_z_vivanaloun_0", False]], "glow-tanning": [["p_z_glowtannin_0", False], ["p_z_glowtannin_1", False]], "cork-and-coffee": [["p_z_corkandcof_0", False]], "pickle-and-peach": [["p_z_pickleandp_0", False]], "just-peachy": [["p_z_justpeachy_0", False]], "woodham-academy": [["p_z_woodhamaca_0", False]], "aldi-jaymac-warehouse": [["p_z_aldijaymac_0", False]], "camden-clinic": [["p_z_camdenclin_0", False]]}
for _c in CASES:
    for _k,_h in _ADD3.get(_c['slug'],[]):
        if _h: _c['hero']=_k; _c['photos']=[_k]+[p for p in _c['photos'] if p!=_k]
        elif _k not in _c['photos']: _c['photos'].append(_k)
# Our Work main photos: best available shot for each job (reviewed Nov 2026)
_BEST_HERO = {"nhs-community-diagnostic-centre": "p_z_nhscommuni_0", "glow-tanning": "p_z_glowtannin_0",
              "savoy": "p_z_savoy_0", "recover3": "p_r3_neon", "renewable-energy": "n_renew_close"}
for _c in CASES:
    _h = _BEST_HERO.get(_c["slug"])
    if _h:
        _c["hero"] = _h; _c["photos"] = [_h] + [p for p in _c["photos"] if p != _h]
_DROP3 = {"p_z_nhscommuni_0":"ig_nhs_night","p_y_leancuisin_0":"ig_leancuisine","p_y_jamjar_1":None,"p_z_vivanaloun_0":None,"p_y_country_2":None,
          "p_z_savoy_1":None,"p_y_littleherh_1":None,"p_y_betteryou_1":None,"p_z_aldijaymac_0":None,"p_y_actgroup_1":None,"p_y_alba_2":None}
for _c in CASES:
    _new = []
    for p in _c["photos"]:
        q = _DROP3.get(p, p) if p in _DROP3 else p
        if q and q not in _new: _new.append(q)
    _c["photos"] = _new
    if _c["hero"] in _DROP3: _c["hero"] = _DROP3[_c["hero"]] or _c["photos"][0]

# area cards on the homepage use a portrait-friendly photo
for _a in AREAS:
    _a["stage"] = {"gateshead": "n_superpower", "sunderland": "p_y_fawcettstr_0"}.get(_a["slug"], _a["hero"])
for _c in CASES:
    if _c["slug"] == "vertu-motors-arena":
        _c["hero"] = "vertu"; _c["photos"] = ["vertu"] + [p for p in _c["photos"] if p != "vertu"]

# ---- Mak's corrections, 18 Nov
CASES[:] = [c for c in CASES if c["slug"] not in ("assenheims-56", "good-lash-gang")]
def _set(_slug, hero=None, drop=(), add=(), **kw):
    for c in CASES:
        if c["slug"] != _slug: continue
        c["photos"] = [p for p in c["photos"] if p not in drop] + [p for p in add if p not in c["photos"]]
        if hero: c["hero"] = hero
        if c["hero"] in drop or c["hero"] not in c["photos"]:
            c["photos"] = [c["hero"]] + [p for p in c["photos"] if p != c["hero"]] if c["hero"] not in drop else c["photos"]
            if c["hero"] in drop: c["hero"] = c["photos"][0]
        c["photos"] = [c["hero"]] + [p for p in c["photos"] if p != c["hero"]]
        c.update(kw)
_set("kink", hero="p_x_kink_1", drop=("p_x_kink_0","p_x_kink_3"), add=("p_x_goodlashga_1","welcome_neon"),
     slug="wink", name="Wink", types=["3d-letters","neon-led-neon"], label="3D letter fascia and LED neon",
     lede="Pink 3D letters on a new grey fascia, and an LED neon feature wall for the Good Lash Gang inside.",
     brief="Wink wanted a bold shopfront and a feature wall clients would want to photograph.",
     made=[("3D letters","Fabricated letters in the brand pink, fixed to a new grey fascia."),("LED neon","Welcome to the Good Lash Gang in script neon on a printed pink wall.")],
     result="A shopfront you can spot from the end of the street, and a wall made for photos.")
_set("the-chair", hero="p_ch_2")
_set("company-shop-group", drop=("p_z_companysho_4",))
_set("woodham-academy", drop=("p_z_woodhamaca_0",))
_set("originals-glow", hero="p_x_originalsg_2")
_set("kiss-me-irish", hero="p_x_kissmeiris_2")
_set("aspire-health-group", hero="p_x_aspireheal_0", drop=("p_x_aspireheal_1",))
_set("country", hero="p_y_country_1", slug="cowgirl-and-country", name="Cowgirl & Country", where="Newcastle upon Tyne",
     lede="Illuminated letters above the stage at Cowgirl & Country, a country music bar in Newcastle.")
_set("alba", hero="p_y_alba_1", drop=("p_y_alba_0","p_y_alba_2"), types=["flat-cut-letters"], label="Cut metal sign",
     lede="A cut metal logo sign for Alba Ristorante.", brief="Alba wanted a refined metal sign at the entrance.",
     made=[("Cut metal sign","The Alba logo cut from metal and finished in gold and copper tones, mounted beside the entrance.")],
     result="An entrance sign that suits the restaurant.")
_set("act-group", hero="p_y_actgroup_3")
_set("sunderland-eye-hospital", hero="p_y_sunderland_3", drop=("p_y_sunderland_0","p_y_sunderland_1","p_y_sunderland_2"),
     types=["totems-monoliths"], label="Site totem", lede="A site totem with car park, drop-off and emergency directions for a hospital.")
_set("north-shore", types=["printed-fascia-panels"])
_set("sienna", types=["printed-fascia-panels"] + [t for t in next(c for c in CASES if c["slug"]=="sienna")["types"] if t!="printed-fascia-panels"])
for _c in CASES:
    _c["making"] = [m for m in (_c.get("making") or []) if m not in ("p_z_woodhamaca_0",)]

# ---- guides: photos inside the articles, and two new guides (18 Nov)
_GFIG = {
 "illuminated-signs": {"face-lit letters": "{FIG vertu_night|Vertu Motors Arena: face-lit letters above the entrance, bright and readable from across the car park.}",
                       "halo-lit letters": "{FIG p_tr_halo|Halo-lit 3D letters for Trident. The glow spreads onto the panel behind.}",
                       "backlit panels": "{FIG st_sign|Bar Seventy Three: a backlit panel with cut-out lettering.}",
                       "light boxes": "{FIG ig_gavroche|A Le Gavroche light box, tested in our workshop before it went out.}",
                       "flex faces": "{FIG n_kosmic|Kosmic Kingdom: one printed flex face across a large frame, with no joins.}",
                       "LED neon": "{FIG neonB|LED neon on a bar wall.}"},
 "shop-sign-cost": {"the six things that set the price": "{FIG ws_built|Built-up letters take longer to make than a printed panel, because every letter is fabricated by hand.}"},
}
for _g in GUIDES:
    if _g["slug"] in _GFIG:
        _g["sections"] = [(h, _GFIG[_g["slug"]][h] + html if h in _GFIG[_g["slug"]] else html) for h, html in _g["sections"]]
    if _g["slug"] == "shop-sign-cost": _g["card"] = "ws_cnc"

GUIDES += [
 dict(slug="3d-vs-flat-cut-letters", title="3D Letters vs Flat-Cut Letters: Which Should You Choose?", h1="3D letters or flat-cut letters?",
      desc="Built-up 3D letters and flat-cut letters compared: how each is made, how they look, where they work best, lighting options and cost.",
      hero="n_fitt", card="p_arv_logo", updated="2026-11-18", kicker="Letters guide",
      lede="Both put your name on the wall in separate letters. One is fabricated like a small box and can be lit. The other is cut from a solid sheet. Here is how to choose between them.",
      sections=[
       ("the short answer", "<ul><li><b>3D built-up letters</b> are hollow letters made from a face, a return (the sides) and often a back. They are 20mm deep or more, and they can hold LEDs, so they are the choice for illuminated shopfronts and building signs.</li><li><b>Flat-cut letters</b> are cut in one piece from solid acrylic, aluminium composite, stainless steel, brass or Komacel. They are slimmer and crisp, and usually unlit or lit from outside. They suit receptions, offices and interiors.</li></ul>"),
       ("how 3D built-up letters are made", "{FIG ws_weld|Fabricating the returns for built-up letters in our Team Valley workshop.}<p>Each letter is built individually. The face is cut on a CNC router or laser, a metal or acrylic return is formed and fixed around its edge, and the letter is finished in paint, metal or acrylic. For lit letters, LEDs and wiring go inside before the letter is sealed.</p><p>At Onesign, anything 20mm deep or more is built as a 3D letter. Depth is usually somewhere between 20mm and 100mm, and more on large building signs. That depth gives a strong shadow in daylight and room for the light at night.</p><p><a href=\"{R}signs/3d-letters.html\">See our 3D letters →</a></p>"),
       ("how flat-cut letters are made", "{FIG p_arv_logo|ARV Studio: a flat-cut logo stood off a textured wall.}<p>Flat-cut letters are cut straight from a sheet, up to 20mm thick. Anything deeper than that we build as a 3D letter. Thicker acrylic, aluminium and Komacel give a solid, chunky look. Stainless steel and brass give a fine, premium edge. Letters can be fixed flat to the wall or on stand-off locators so they cast a small shadow.</p><p><a href=\"{R}signs/flat-cut-letters.html\">See our flat-cut letters →</a></p>"),
       ("side by side", "<table class=\"cmp\"><thead><tr><th></th><th>3D built-up</th><th>Flat-cut</th></tr></thead><tbody><tr><td>Depth</td><td>20mm and deeper</td><td>Up to 20mm</td></tr><tr><td>Lighting</td><td>Face-lit, halo-lit or both</td><td>Unlit, or lit by external lights</td></tr><tr><td>Best viewed from</td><td>Across the street and further</td><td>Close to mid range</td></tr><tr><td>Typical use</td><td>Shopfronts, building signs</td><td>Receptions, offices, interiors</td></tr><tr><td>Fine detail</td><td>Limited by how small a return can be formed</td><td>Very fine detail is possible</td></tr><tr><td>Cost</td><td>Higher, every letter is fabricated</td><td>Lower, cut in one operation</td></tr></tbody></table>"),
       ("which one for your building", "<ul><li><b>Need it seen at night?</b> Choose 3D letters. Flat-cut letters cannot hold LEDs.</li><li><b>Reading distance over 20 metres?</b> The depth and size of built-up letters carry further.</li><li><b>Inside a reception or office?</b> Flat-cut letters give a clean, architectural look and cost less.</li><li><b>A thin script or fine logo?</b> Flat-cut handles very fine strokes better. We can also cut the detail out of a <a href=\"{R}signs/backlit-panels.html\">backlit panel</a> if it needs lighting.</li><li><b>Not sure?</b> Send us a photo and we will mock up both on your building.</li></ul>")],
      faq=[("Can flat-cut letters be illuminated?", "Not from inside, because they are solid. They can be lit by small spotlights or a trough light above, or mounted on a lit panel."),
           ("Which lasts longer?", "Both last for many years when made from the right materials for indoors or outdoors. Outside, we use aluminium, stainless steel or exterior-grade acrylic."),
           ("Can you match our brand colours?", "Yes. Painted letters are sprayed to your colour reference, and acrylic faces are matched as closely as the material range allows."),
           ("Do I need planning consent for 3D letters?", "Unlit letters often have deemed consent. Illuminated letters usually need an application. Our planning guide explains more.")]),
 dict(slug="how-long-does-a-shop-sign-take", title="How Long Does a Shop Sign Take? From Enquiry to Installation", h1="how long does a shop sign take?",
      desc="A realistic timeline for a new shop sign in the UK: survey, design, approvals, manufacture and installation, and what speeds it up or slows it down.",
      hero="ws_install", card="ws_spray", updated="2026-11-18", kicker="Timescale guide",
      lede="Most shop signs take a few weeks from first enquiry to the day they go up. The biggest variable is not the making. It is how quickly the design is signed off and whether the council or landlord needs to approve it.",
      sections=[
       ("a typical timeline", "<ol class=\"steps-list\"><li><b>Enquiry and quote.</b> A few days. A photo and rough measurements let us send a first price and mockup quickly.</li><li><b>Site survey.</b> Usually within a week or two. We measure, check the wall and access, and look at power for lit signs.</li><li><b>Design and sign-off.</b> As long as it takes to agree the visual. One round of changes is normal. This is where most delays happen.</li><li><b>Approvals, if needed.</b> Advertisement consent can take up to eight weeks after a valid application. Landlord approval varies.</li><li><b>Manufacture.</b> Typically one to three weeks, depending on the sign type and how busy the workshop is.</li><li><b>Installation.</b> Most shopfront signs are fitted in a single day.</li></ol><p class=\"note\">These are typical ranges, not promises. Your quote will give a date for your job.</p>"),
       ("what happens in the workshop", "{FIG ws_cnc|Cutting letter faces on the CNC router.}<p>Once the design is signed off, the drawings go to the workshop. Faces are cut on the CNC router or laser, returns are formed and welded, and everything is sprayed, assembled and wired. Illuminated signs are switched on and tested before they leave.</p>{FIG ws_spray|Spray finishing letters to the brand colour.}<p>A printed panel can be ready in days. Built-up illuminated letters take the longest, because each letter is made and wired by hand.</p>"),
       ("installation day", "{FIG install|Our fitters installing a building sign from a powered access platform.}<p>Our own fitters install every sign. A ground-floor fascia is normally a one-day job from steps or a tower. High-level signs need a platform and sometimes a pavement or road permit, which has to be booked in advance. An electrician connects illuminated signs to the supply.</p>"),
       ("what slows a sign down", "<ul><li>Waiting on logo files or brand colours</li><li>Several rounds of design changes</li><li>Advertisement consent or listed building consent</li><li>Landlord or shopping centre approval</li><li>Access permits for high-level work</li><li>Bad weather on installation day, for work at height</li></ul>"),
       ("how to get it up faster", "<ol><li>Send a straight-on photo, rough measurements and your logo with your first enquiry.</li><li>Agree who signs off the design, so there is one decision-maker.</li><li>Ask us at quote stage whether consent is needed, so the application starts straight away.</li><li>If you are opening on a fixed date, tell us the date first. We plan the job backwards from it.</li></ol><p>If the opening date is very close, a temporary printed banner or hoarding can carry the name until the permanent sign is ready. See our <a href=\"{R}signs/flags-banners.html\">flags and banners</a>.</p>")],
      faq=[("Can you make a sign in a week?", "Sometimes, for simple printed signs with artwork ready and no consent needed. Illuminated letters usually take longer. Ask us with your date."),
           ("Do I have to close the shop for installation?", "Usually not. Most fascia installs happen while you trade, and we can work early or out of hours by arrangement."),
           ("Who connects an illuminated sign to the power?", "The sign is wired and tested in our workshop. On site it is connected to a suitable supply by a qualified electrician."),
           ("When should I order a sign for a new shop?", "As soon as you have the keys and your branding. Six to eight weeks before opening is a comfortable lead time, and longer if consent is needed.")]),
]

# ---- job locations (photo GPS where available, otherwise the known venue). Jobs not listed have no known location yet.
LOC = {
"savoy": [
"Morpeth",
"northumberland",
55.16918,
-1.68964,
"gps"
],
"grace-kellys": [
"Seaham",
"durham",
54.83868,
-1.33176,
"gps"
],
"pickle-and-peach": [
"South Shields",
"south-tyneside",
55.00008,
-1.42642,
"gps"
],
"pantera-advisory": [
"Harrogate",
None,
53.97571,
-1.56591,
"gps"
],
"vivana-lounge": [
"Newcastle city centre",
"newcastle",
54.97544,
-1.62949,
"gps"
],
"the-library": [
"Whitley Bay",
None,
55.04263,
-1.44361,
"gps"
],
"mapleleaf-express": [
"Herefordshire",
None,
52.18118,
-2.52144,
"gps"
],
"the-works": [
"Herefordshire",
None,
52.18758,
-2.50438,
"gps"
],
"fora": [
"Chester-le-Street",
"durham",
54.85857,
-1.57478,
"gps"
],
"park-electrical": [
"County Durham",
"durham",
54.80184,
-1.67085,
"gps"
],
"copeland-residential": [
"Chester-le-Street",
"durham",
54.85786,
-1.57223,
"gps"
],
"parm-o-rama": [
"Heaton, Newcastle",
"newcastle",
54.98854,
-1.57757,
"gps"
],
"nobles-casino": [
"South Shields",
"south-tyneside",
54.99847,
-1.43366,
"gps"
],
"little-her-hair": [
"Low Fell, Gateshead",
"gateshead",
54.93407,
-1.59931,
"gps"
],
"fawcett-street-community-shop": [
"Sunderland city centre",
"sunderland",
54.90472,
-1.38098,
"gps"
],
"amethyst": [
"Sunderland",
"sunderland",
54.93002,
-1.37899,
"gps"
],
"jam-jar": [
"Jesmond, Newcastle",
"newcastle",
54.99196,
-1.6034,
"gps"
],
"cowgirl-and-country": [
"Newcastle city centre",
"newcastle",
54.97123,
-1.60903,
"gps"
],
"lean-cuisine": [
"Jesmond, Newcastle",
"newcastle",
54.98763,
-1.59301,
"gps"
],
"craft-and-crumb": [
"South Shields",
"south-tyneside",
54.98731,
-1.42356,
"gps"
],
"salto": [
"Gateshead",
"gateshead",
54.94068,
-1.61705,
"gps"
],
"alba": [
"London",
None,
51.50012,
-0.16305,
"gps"
],
"dog-and-parrot": [
"Newcastle city centre",
"newcastle",
54.9684,
-1.6209,
"gps"
],
"the-avenue": [
"Seghill, Northumberland",
"northumberland",
55.07374,
-1.52792,
"gps"
],
"act-group": [
"Hebburn",
"south-tyneside",
54.95482,
-1.50698,
"gps"
],
"houghton-colliery": [
"Houghton-le-Spring",
"sunderland",
54.8471,
-1.47277,
"gps"
],
"newcastle-university": [
"Newcastle University",
"newcastle",
54.979,
-1.615,
"place"
],
"vertu-motors-arena": [
"Benton, Newcastle",
"newcastle",
55.0187,
-1.5756,
"place"
],
"grainger-market": [
"Grainger Market, Newcastle",
"newcastle",
54.9718,
-1.6165,
"place"
],
"blacks-corner-fenwick": [
"Fenwick, Newcastle",
"newcastle",
54.9748,
-1.6125,
"place"
],
"superpower-metrocentre": [
"Metrocentre, Gateshead",
"gateshead",
54.9588,
-1.665,
"place"
],
"nhs-community-diagnostic-centre": [
"Metrocentre, Gateshead",
"gateshead",
54.9575,
-1.6682,
"place"
],
"woodham-academy": [
"Newton Aycliffe",
"durham",
54.629,
-1.559,
"place"
],
"northgate-hospital": [
"Morpeth",
"northumberland",
55.17,
-1.662,
"place"
],
"cork-and-coffee": [
"Seaham",
"durham",
54.8395,
-1.341,
"place"
],
"griffin-court": [
"Hebburn",
"south-tyneside",
54.973,
-1.513,
"place"
],
"welcome-to-durham": [
"Durham City",
"durham",
54.7761,
-1.5733,
"place"
],
"the-white-swan": [
"Dinnington, Newcastle",
"newcastle",
55.0556,
-1.6726,
"place"
]
}
for _c in CASES:
    if _c['slug'] in LOC and not _c.get('where'): _c['where'] = LOC[_c['slug']][0]

# ---- location corrections from address lookups (18 Nov). Postcode centroids from the ONS postcode list.
for _s in ["mapleleaf-express", "the-works", "alba", "pantera-advisory", "pickle-and-peach"]:
    LOC.pop(_s, None)   # photo GPS did not match where the sign is; left off until confirmed
LOC.update({
 "trident-fire": ["Washington", "sunderland", 54.89287, -1.50744, "address"],
 "cod-and-crust": ["Sunderland", "sunderland", 54.91687, -1.44066, "address"],
 "renewable-energy": ["Sunderland Enterprise Park", "sunderland", 54.91835, -1.41504, "address"],
 "skin-and-soul": ["Roker, Sunderland", "sunderland", 54.93000, -1.37834, "address"],
 "rustic-cup": ["Whitley Bay", None, 55.04206, -1.44876, "address"],
 "recite-me": ["Baltic Business Quarter, Gateshead", "gateshead", 54.96660, -1.59546, "address"],
 "qe-facilities": ["Queen Elizabeth Hospital, Gateshead", "gateshead", 54.93938, -1.58078, "address"],
 "north-shore": ["Grainger Market, Newcastle", "newcastle", 54.97160, -1.61600, "address"],
 "filto": ["Fenwick, Newcastle", "newcastle", 54.97604, -1.61360, "address"],
 "merz-court": ["Newcastle University", "newcastle", 54.98032, -1.61571, "address"],
 "workwear-express": ["Belmont, Durham", "durham", 54.78832, -1.53677, "address"],
 "newstreet": ["Durham", "durham", 54.77519, -1.58669, "address"],
 "fabios": ["Saddler Street, Durham", "durham", 54.77639, -1.57532, "address"],
})
for _c in CASES:
    if _c["slug"] in LOC: _c["where"] = LOC[_c["slug"]][0]
    elif _c["slug"] in ["mapleleaf-express", "the-works", "alba", "pantera-advisory", "pickle-and-peach"]: _c["where"] = None

# ---- Mak's corrections, 18 Nov (afternoon)
IMG_CAPS = {"n_fitt_int": "Filto and Thatype, Fenwick Newcastle: interior lettering"}
for _c in CASES:
    if _c["slug"] == "filto":
        _c.update(types=["flat-cut-letters", "digital-large-format-print"], label="Painted Foamex letters and hoarding",
                  lede="Painted Foamex lettering above the door and on the fascia, plus a printed hoarding while the café was fitted out.",
                  made=[["Foamex lettering", "Flat-cut Foamex letters, painted in the brand grey, above the door and on the fascia."],
                        ["Hoarding", "Large format printed hoarding announcing the opening."],
                        ["Interior", "Lettering inside the Fenwick Food Hall unit, alongside Thatype."]])
        _c["photos"] = ["p_y_filto_0", "p_y_filto_1", "n_fitt_int", "p_y_filto_3", "p_y_filto_4"]
        _c["making"] = list(_c.get("making") or []) + ["p_y_filto_2"]
    if _c["slug"] == "sunderland-eye-hospital":
        _c.update(hero="p_seh_09749", types=["wayfinding", "3d-letters", "totems-monoliths", "vinyl-wall-graphics"],
                  label="Full wayfinding scheme",
                  lede="Illuminated entrance letters, directory totems, floor directories, door and projecting signs, tactile Braille signs and glass manifestation across a new eye hospital.",
                  photos=["p_seh_09749", "p_seh_00187", "p_seh_09759", "p_seh_09774", "p_seh_09803", "p_seh_09795", "p_seh_00126",
                          "p_seh_00027", "p_seh_09896", "p_seh_09861", "p_seh_00086b", "p_seh_00084b", "p_y_sunderland_3"])
    if _c["slug"] == "fawcett-street-community-shop":
        _c["photos"] = list(dict.fromkeys(_c["photos"] + ["p_fw_08147", "p_fw_08150", "p_fw_08160", "p_fw_08170", "p_fw_08176",
                         "p_fw_08194", "p_fw_08196", "p_fw_08205", "p_fw_08222", "p_fw_08224", "p_fw_08226"]))
CASES.append(dict(slug="thatype", old=None, name="Thatype", where="Fenwick, Newcastle", sector="hospitality-leisure",
    types=["3d-letters"], hero="n_thatype", label="Halo-lit script letters",
    lede="Halo-lit 3D script lettering for Thatype, next to Filto in Fenwick Newcastle.",
    brief="A warm, premium glow that sits comfortably beside its neighbours in the food hall.",
    made=[["Halo-lit 3D letters", "Fabricated script letters with LEDs behind, glowing onto the fascia."],
          ["Interior lettering", "Matching lettering inside the unit."]],
    result="A sign that reads beautifully from across the food hall.",
    photos=["n_thatype", "n_fitt_int"], making=[]))
LOC["thatype"] = ["Fenwick, Newcastle", "newcastle", 54.97604, -1.61360, "address"]

for _c in CASES:
    if _c["slug"] == "sunderland-eye-hospital":
        _c["hero"] = "p_seh_09751"; _c["photos"] = ["p_seh_09751"] + [p for p in _c["photos"] if p != "p_seh_09751"]

# SEH: fuller gallery and higher in the Our Work list (Mak, 18 Nov)
for _c in CASES:
    if _c["slug"] == "sunderland-eye-hospital":
        _c["photos"] = list(dict.fromkeys(_c["photos"] + ['p_seh_00003', 'p_seh_00012', 'p_seh_00015', 'p_seh_00033', 'p_seh_00045', 'p_seh_00051', 'p_seh_00066', 'p_seh_00078b', 'p_seh_00095b', 'p_seh_00109b', 'p_seh_00120', 'p_seh_00122', 'p_seh_00142', 'p_seh_00153', 'p_seh_09767', 'p_seh_09787', 'p_seh_09793', 'p_seh_09822', 'p_seh_09839', 'p_seh_09893', 'p_seh_09899', 'p_seh_09971', 'p_seh_09981']))
_i = next(i for i, c in enumerate(CASES) if c["slug"] == "sunderland-eye-hospital")
CASES.insert(2, CASES.pop(_i))

# Zen is a Thai and pan-Asian restaurant on Court Lane, Durham DH1 3JS (Mak, 19 Nov)
LOC["zen"] = ["Court Lane, Durham", "durham", 54.77380, -1.56850, "address"]
for _c in CASES:
    if _c["slug"] == "zen": _c.update(where="Court Lane, Durham", sector="hospitality-leisure")

# ---- 7th guide (Mak, 19 Nov): fills the empty slot in "more guides"
GUIDES.append(dict(slug="what-to-send-for-a-sign-quote", title="What to Send for a Sign Quote: Photos, Sizes and Logo Files", h1="what to send for a sign quote.",
      desc="The photos, measurements, logo files and details that get you an accurate sign quote and mockup first time, with no back and forth.",
      hero="install2", card="st_design", updated="2026-11-19", kicker="Quote checklist",
      lede="A good quote comes from good information. Send a straight-on photo, a few rough measurements and your logo, and we can usually come back with a price and a mockup of your building within a few days.",
      sections=[
       ("the short checklist", "<ol class=\"steps-list\"><li><b>A straight-on photo</b> of the wall or window, taken from across the road if you can.</li><li><b>Rough measurements</b> of the area the sign will go on: width and height are enough to start.</li><li><b>Your logo</b>, ideally as a vector file (AI, EPS, SVG or PDF).</li><li><b>Your brand colours</b>, if you have references.</li><li><b>The site address</b> and postcode.</li><li><b>Your opening date</b> or deadline, if there is one.</li><li><b>A rough budget</b>, so we can show you the best option for it.</li></ol>"),
       ("how to take a useful photo", "{FIG p_kk_front|A straight-on view of the fascia, like this, lets us draw your sign onto the real building.}<p>Stand directly in front of the building and keep the phone level, so the fascia looks rectangular rather than tapered. Get the whole frontage in, with a little of the neighbours either side. One close photo of the fixing area helps too, so we can see whether it is brick, render, timber or an existing panel.</p><p>For a high-level sign, step back far enough to get the whole elevation. A photo taken in daylight is best, even if the sign will be illuminated.</p>"),
       ("measuring without a ladder", "<p>We do not need exact sizes to quote. Measure what you can reach, such as the width of the shopfront at ground level, and estimate the height of the fascia. Counting bricks works well: a standard brick course is about 75mm. We take exact measurements at the site survey before anything is made.</p>"),
       ("logo files that work", "{FIG st_design|Artwork being set up for production in our studio.}<p>Letters and logos are cut by machines that follow vector lines, so a vector file gives the cleanest result. Your designer or printer will usually have one. A JPEG or PNG is fine for a first quote and mockup, and if there is no vector version we can redraw the logo for you.</p>"),
       ("details that change the price", "<ul><li><b>Illumination.</b> Lit signs need LEDs, power and often planning consent.</li><li><b>Height.</b> Work above first floor needs a platform and sometimes a permit.</li><li><b>Materials.</b> Stainless steel and built-up letters cost more than acrylic or printed panels.</li><li><b>Size.</b> Bigger letters use more material and take longer to make.</li><li><b>Removal.</b> Taking down and disposing of an old sign adds time on site.</li></ul><p>Our <a href=\"{R}guides/shop-sign-cost.html\">sign cost guide</a> gives typical price ranges.</p>"),
       ("what happens next", "<p>We send a quote and a visual showing the sign on your building. Once you are happy, we book a site survey to confirm sizes and fixings, then the job goes into the workshop. Our <a href=\"{R}guides/how-long-does-a-shop-sign-take.html\">timescale guide</a> explains each stage.</p>")],
      faq=[("Do I need a site visit before getting a price?", "No. A photo and rough sizes are enough for a first quote and mockup. We survey the site before anything is made."),
           ("What if I don't have a logo yet?", "Tell us what you have in mind. Our design team can create sign artwork from your business name, or work alongside your designer."),
           ("Is the mockup free?", "Yes. Every quote comes with a visual of the sign on your building."),
           ("Can I send everything by email or WhatsApp?", "Yes. Use the enquiry form on this page, or call us and we will tell you where to send the photos.")]))

# ---- Seaham (SR7) jobs sit with Sunderland, not Durham (Mak, 19 Nov)
for _s in ("cork-and-coffee", "grace-kellys"):
    if _s in LOC: LOC[_s][0] = "Seaham"; LOC[_s][1] = "sunderland"
for _c in CASES:
    if _c["slug"] in ("cork-and-coffee", "grace-kellys"): _c["where"] = "Seaham"
    if _c["slug"] == "workwear-express":
        _c["hero"] = "p_x_workwearex_3"
        _c["photos"] = ["p_x_workwearex_3"] + [p for p in _c["photos"] if p != "p_x_workwearex_3"]
for _a in AREAS:
    if _a["slug"] == "durham":
        _a["proof"] = [p for p in _a.get("proof", []) if p[0] not in ("cork-and-coffee", "grace-kellys")]
        _a["photos"] = [p for p in _a.get("photos", []) if p not in ("cork_dusk", "p_cork_new", "gk_front", "p_gk_wide")]
        if _a.get("hero") in ("cork_dusk", "p_cork_new"): _a["hero"] = "n_court"
    if _a["slug"] == "sunderland":
        _a.setdefault("proof", [])
        if not any(p[0] == "cork-and-coffee" for p in _a["proof"]):
            _a["proof"].append(("cork-and-coffee", "Komacel 3D letters and interior branding in Seaham."))
        if not any(p[0] == "grace-kellys" for p in _a["proof"]):
            _a["proof"].append(("grace-kellys", "3D letters on the fascia of a Seaham bar."))
for _a in AREAS:
    if _a["slug"] == "durham":
        _a["intro"] = [t.replace("Durham City, Chester-le-Street, Seaham, Peterlee", "Durham City, Chester-le-Street, Peterlee") for t in _a["intro"]]
        _a["places"] = [p for p in _a["places"] if p != "Seaham"]
    if _a["slug"] == "sunderland":
        _a["intro"][0] = _a["intro"][0].replace("to Washington and Houghton-le-Spring", "to Washington, Houghton-le-Spring and down the coast to Seaham")
        if "Seaham" not in _a["places"]: _a["places"].insert(4, "Seaham")

# ---- hand-written meta descriptions where the generated one would be trimmed (SEO pass, 19 Nov)
for _g in GUIDES:
    if _g["slug"] == "sign-planning-permission":
        _g["desc"] = "When a UK shop sign needs advertisement consent, what deemed consent covers, and how lighting and conservation areas change things."
for _c in CASES:
    if _c["slug"] == "sunderland-eye-hospital":
        _c["meta"] = "A full wayfinding scheme for Sunderland Eye Hospital: lit entrance letters, totems, directories, door signs, Braille signs and glass manifestation."

# ================= new work from "Website revamp/New" (19 Nov) =================
_N2 = lambda job, n: [f"p_n2_{job}_{i}" for i in range(n)]
_BY = {c["slug"]: c for c in CASES}
# --- existing jobs: more photos, corrected places
_s = _BY["sunderland-eye-hospital"]
_s["hero"] = "p_n2_seh_0"
_s["photos"] = _N2("seh", 5) + [p for p in _s["photos"] if p not in _N2("seh", 5)]
LOC["sunderland-eye-hospital"] = ["Sunderland", "sunderland", 54.90725, -1.39077, "gps"]
_t = _BY["thatype"]
_t.update(where="Metrocentre, Gateshead", sector="retail", hero="p_n2_thatype_0", label="Halo-lit shopfront letters",
          lede="Halo-lit 3D script letters across the Thatype shopfront at the Metrocentre.",
          photos=_N2("thatype", 5) + ["n_thatype", "n_fitt_int"])
LOC["thatype"] = ["Metrocentre, Gateshead", "gateshead", 54.95640, -1.66727, "gps"]
LOC["filto"] = ["Metrocentre, Gateshead", "gateshead", 54.95640, -1.66727, "photo"]
_BY["filto"]["where"] = "Metrocentre, Gateshead"
IMG_CAPS["n_fitt_int"] = "Filto and Thatype, Metrocentre: interior lettering"
_g = _BY["glow-tanning"]; _g["photos"] = _N2("glow", 4) + _g["photos"]
LOC["glow-tanning"] = ["Team Valley, Gateshead", "gateshead", 54.93294, -1.61877, "gps"]
_b = _BY["black-rabbit"]
_b.update(name="Black Rabbit & The Warren", where="Chester-le-Street", types=["printed-fascia-panels"], hero="p_n2_br_0",
          label="Gold-lettered bar fascias",
          lede="Black fascias with gold logos and lettering for Black Rabbit and The Warren, side by side in Chester-le-Street.",
          brief="Two neighbouring venues, one look: Black Rabbit bar and restaurant and The Warren next door both wanted black fascias with gold artwork that feels classic and premium from the street.",
          made=[("Black Rabbit fascia", "A long black fascia with the gold rabbit crest, name and 'Bar & Restaurant' lettering."),
                ("The Warren fascia", "A matching black fascia with gold lettering and corner flourishes on the shopfront next door.")],
          result="The two frontages now read as a pair along the street, with the gold artwork picking up the light through the day.",
          photos=_N2("br", 6) + _b["photos"])
LOC["black-rabbit"] = ["Chester-le-Street", "durham", 54.85170, -1.57309, "gps"]
_gc = _BY["griffin-court"]
_gc.update(types=["3d-letters", "totems-monoliths", "wayfinding", "high-level-signs"], hero="p_n2_gc_0",
           label="Letters, totems and wayfinding",
           lede="Fabricated canopy letters, an entrance totem and a full internal wayfinding scheme for Griffin Court in Hebburn.",
           photos=_N2("gc", 13) + _gc["photos"])
_gc["made"] = list(_gc.get("made") or []) + [("Entrance totem", "A freestanding totem by the road directing visitors to the main entrance and car park."),
               ("Internal wayfinding", "Floor directories, directional signs, level signs and door signs in clear acrylic with stand-off fixings, with raised lettering on the directories.")]
LOC["griffin-court"] = ["Hebburn", "south-tyneside", 54.97257, -1.52125, "gps"]
_m = _BY["mapleleaf-express"]; _m["hero"] = "p_n2_ml_0"; _m["photos"] = _N2("ml", 5) + _m["photos"]
if "neon-led-neon" not in _m["types"]: _m["types"].append("neon-led-neon")

# --- new jobs
def _new(slug, name, where, sector, types, job, n, label, lede, brief, made, result, loc=None, making=()):
    ph = _N2(job, n); mk = [p for p in ph if p in making]
    CASES.append(dict(slug=slug, old=None, name=name, where=where, sector=sector, types=types, hero=ph[0], label=label, lede=lede,
                      brief=brief, made=made, result=result, photos=[p for p in ph if p not in mk], making=mk))
    if loc: LOC[slug] = loc
_new("byre", "BYRE", "East Boldon", "hospitality-leisure", ["vinyl-wall-graphics", "neon-led-neon"], "byre", 7,
     "Wall graphics, LED neon and window vinyl",
     "Painted-look wall logos, LED neon and window vinyl for BYRE, a burger restaurant in East Boldon.",
     "BYRE wanted its bold, hand-made brand all over the restaurant: big logos on the brickwork, neon to glow through the windows and graphics that carry the cow mascot from the street to the tables.",
     [("Wall graphics", "Large BYRE logos and the Little Grazers kids' graphic applied to painted brick so they look hand-painted."),
      ("LED neon", "A red BYRE cow neon in the window and a 'Join the Herd' neon behind the bar."),
      ("Window vinyl", "Cut vinyl logos on the glazing, plus takeaway menu lettering on the wall.")],
     "The brand now runs through the whole restaurant, and the neon makes it easy to spot from outside after dark.",
     ["East Boldon", "south-tyneside", 54.94529, -1.43461, "gps"])
_new("cotton-travel", "Cotton Travel", "Sunderland", "retail", ["3d-letters", "vinyl-wall-graphics", "neon-led-neon"], "cotton", 6,
     "Logo wall, world map and LED neon",
     "A 3D logo wall, a timber world map, LED neon and a new shopfront for Cotton Travel in Sunderland.",
     "Cotton Travel wanted the shop to feel like the start of a holiday: a strong brand wall, a feature to talk about and a corner for families.",
     [("3D logo wall", "The gold globe logo and lettering built up off a painted feature wall."),
      ("World map", "A cut world map with 'Explore a Bigger World' lettering above the coffee station."),
      ("LED neon", "A warm white 'Little Explorers' neon for the kids' corner."),
      ("Shopfront", "A fascia panel and full-colour window graphics.")],
     "The shop now looks the part from the street to the brochure wall.",
     ["Sunderland", "sunderland", 54.91211, -1.38802, "gps"])
_new("tribeca", "Tribeca", "Sunderland", "hair-beauty", ["3d-letters", "vinyl-wall-graphics"], "tribeca", 5,
     "Gold 3D fascia letters",
     "Gold 3D letters with a script overlay on the fascia, plus an interior logo and window lettering for Tribeca hair salon in Sunderland.",
     "Tribeca wanted a smart, high-street frontage that matched the interior of the salon.",
     [("Fascia letters", "Gold 3D capitals with the salon's script logo layered across them on a dark fascia."),
      ("Interior logo", "The same logo built up on the feature wall inside."),
      ("Window lettering", "Cut vinyl branding on the glazing.")],
     "A frontage that stands out on the street and a logo wall that customers photograph.",
     ["Sunderland", "sunderland", 54.90509, -1.38260, "gps"])
_new("durham-university-ai-skills-centre", "Durham University AI Skills Centre", "Durham", "education", ["flat-cut-letters", "vinyl-wall-graphics"], "du", 5,
     "Logo walls for a new centre",
     "Brushed-finish logo walls and a glass entrance panel for the Durham University and Microsoft AI Skills Centre of Excellence.",
     "A new centre run with Microsoft needed both brands presented clearly and consistently on arrival.",
     [("Logo walls", "Cut lettering and crests in a metallic finish on the centre's feature walls."),
      ("Entrance panel", "A printed glass-effect panel with both logos, fixed on stand-offs.")],
     "The centre opened with its branding in place from the entrance to the teaching spaces.",
     ["Durham", "durham", 54.76425, -1.57106, "gps"], making=["p_n2_du_4"])
_new("cabana-elvet-residences", "Cabana Student Living", "Durham", "commercial", ["3d-letters"], "cabana", 4,
     "Fascia and canopy letters",
     "Fascia lettering for Cabana and built-up canopy letters for Elvet Residences, student accommodation in Durham City.",
     "Two student buildings in the historic centre needed clear, understated signs that suit their streets.",
     [("Cabana fascia", "Metallic letters on the painted shopfront fascia."),
      ("Elvet Residences canopy", "Serif letters along the canopy above the entrance.")],
     "Both buildings are easy to find for students and visitors without shouting in a conservation area.",
     ["Durham City", "durham", 54.77519, -1.57222, "gps"])
_new("elring-parts", "Elring Parts", "Team Valley, Gateshead", "commercial", ["3d-letters", "high-level-signs"], "el", 5,
     "3D letters on shaped panels",
     "Shaped building signs with 3D letters for Elring Parts, made in our workshop and fitted from a scaffold tower.",
     "Elring needed its red and white logo on the building, matched to the brand shape rather than a plain rectangle.",
     [("Shaped panels", "Panels cut to the Elring logo outline and finished in brand red and white."),
      ("3D letters", "Built-up letters fixed to the panels for depth."),
      ("Installation", "Fitted by our own team from a scaffold tower.")],
     "A building sign that reads as the brand from across the estate.",
     ["Team Valley, Gateshead", "gateshead", 54.93555, -1.61892, "gps"], making=["p_n2_el_3", "p_n2_el_4"])
_new("aqua-tcg", "Aqua TCG", "Metrocentre, Gateshead", "retail", ["neon-led-neon"], "aqua", 3,
     "LED neon logo",
     "A round LED neon logo for Aqua TCG, a trading card shop in the Metrocentre.",
     "Aqua TCG wanted its logo as a neon feature that shows through the shop window.",
     [("LED neon", "The logo in blue, orange and white LED neon on a clear backing.")],
     "The neon pulls shoppers' eyes in from the mall.",
     ["Metrocentre, Gateshead", "gateshead", 54.95640, -1.66727, "gps"])
_new("fitt", "Fitt", "Newcastle", "hospitality-leisure", ["3d-letters", "digital-large-format-print", "flags-banners"], "fitt", 4,
     "3D letters, A-boards and barrier banners",
     "3D letters, printed A-boards and cafe barrier banners for Fitt and its Coffee & Matcha bar.",
     "Fitt needed its brand inside and out, including signs to bring passers-by to the new coffee bar.",
     [("3D letters", "Dark green built-up letters on a white panel."),
      ("A-boards", "Printed panels on timber A-frames for the terrace."),
      ("Barrier banners", "Printed banners on the cafe's outdoor barriers.")],
     "The coffee bar is signposted from the car park to the counter.",
     ["Newcastle", "newcastle", 54.96493, -1.62543, "gps"])
_new("scissor-guys", "Scissor Guys", "North Shields", "hair-beauty", ["printed-fascia-panels", "vinyl-wall-graphics"], "sg", 4,
     "Fascia and window graphics",
     "A new fascia and printed window graphics for Scissor Guys barber shop in North Shields.",
     "Scissor Guys wanted a sharp frontage and windows that give privacy while selling the shop.",
     [("Fascia", "A dark fascia panel with the Scissor Guys logo."),
      ("Window graphics", "Printed privacy panels with the logo, parking notice and opening hours.")],
     "A tidy, branded frontage that works on a busy road.",
     ["North Shields", None, 55.00861, -1.45558, "gps"])
_new("elysia-and-co", "Elysia & Co", None, "hair-beauty", ["flat-cut-letters"], "elysia", 3,
     "Black wall letters",
     "Large black letters across the salon wall for Elysia & Co.",
     "Elysia & Co wanted a bold logo wall that sets the tone as soon as clients walk in.",
     [("Wall letters", "Black serif letters fixed directly to the wall.")],
     "The logo wall is now the backdrop to the salon.")
_new("brow-game", "Brow Game", None, "hair-beauty", ["printed-fascia-panels", "vinyl-wall-graphics", "flat-cut-letters"], "bg", 4,
     "Fascia, window vinyl and interior logo",
     "A new fascia, window and door vinyl and an interior logo for Brow Game, a brow specialist and academy.",
     "Brow Game needed a frontage and treatment room that match its clean, premium brand.",
     [("Fascia", "A dark fascia with white lettering."),
      ("Window and door vinyl", "The BG monogram on the glazing."),
      ("Interior logo", "The monogram as cut letters on the treatment room wall.")],
     "The brand runs from the street to the treatment chair.")
_new("harbro", "Harbro", None, "retail", ["flat-cut-letters"], "harbro", 1,
     "Counter lettering",
     "The Harbro logo in cut lettering on a store counter.",
     "Harbro wanted its logo on the counter of a country store.",
     [("Counter logo", "White lettering and a red swoosh on the dark counter front.")],
     "The counter now carries the brand.")
# lead the Our Work list with strong new jobs
for _i, _sl in enumerate(["byre", "cotton-travel", "tribeca", "durham-university-ai-skills-centre"]):
    _j = next(k for k, c in enumerate(CASES) if c["slug"] == _sl); CASES.insert(3 + _i, CASES.pop(_j))
for _c in CASES:
    if _c["slug"] == "filto":
        _c["made"] = [[a, b.replace("inside the Fenwick Food Hall unit", "inside the Metrocentre unit")] for a, b in _c["made"]]
    if _c["slug"] == "thatype":
        for _f in ("brief", "result"):
            _c[_f] = _c[_f].replace("Fenwick Newcastle", "the Metrocentre").replace("Fenwick", "the Metrocentre")
        _c["made"] = [[a, b.replace("Fenwick", "the Metrocentre")] for a, b in _c["made"]]
for _c in CASES:
    if _c["slug"] == "elring-parts": _c["hero"] = "p_n2_el_1"
    if _c["slug"] == "fitt": _c["hero"] = "n_fitt"; _c["photos"] = ["n_fitt"] + _c["photos"]

# ================= "Website revamp/New 2" (19 Nov) =================
_N3 = lambda job, n: [f"p_n3_{job}_{i}" for i in range(n)]
_BY = {c["slug"]: c for c in CASES}
def _more(slug, job, n, hero=False, making=False):
    c = _BY[slug]; ks = _N3(job, n)
    if making: c["making"] = list(c.get("making") or []) + ks; return c
    c["photos"] = ks + [p for p in c["photos"] if p not in ks]
    if hero: c["hero"] = ks[0]
    return c
_more("welcome-to-durham", "wtd", 5, hero=True)
_more("pickle-and-peach", "pp", 2, hero=True)
_more("skin-and-soul", "ss", 1)
_more("nobles-casino", "nob", 4, making=True)
_more("glow-tanning", "glowm", 4, making=True)
_more("the-works", "tw", 3, making=True)
_more("just-peachy", "jp", 4, hero=True)
_more("recite-me", "rm", 1, hero=True)
_c = _more("filto", "filto", 7); _c["where"] = None
_more("the-drunken-duck", "dd", 1, hero=True)
_more("my-car-cleaning", "mcc", 2, hero=True)
_c = _BY["grainger-market"]; _c["photos"] = ["p_n3_gm_0"] + _c["photos"]; _c["making"] = list(_c.get("making") or []) + ["p_n3_gm_1", "p_n3_gm_2"]
if "neon-led-neon" not in _c["types"]: _c["types"].append("neon-led-neon")
_more("baxters", "bx", 1)
_more("better-you", "by", 1, hero=True)

def _new3(slug, name, where, sector, types, job, n, label, lede, brief, made, result, loc=None, making=()):
    ph = _N3(job, n); mk = [p for p in ph if p in making]
    CASES.append(dict(slug=slug, old=None, name=name, where=where, sector=sector, types=types, hero=ph[0], label=label, lede=lede,
                      brief=brief, made=made, result=result, photos=[p for p in ph if p not in mk], making=mk))
    if loc: LOC[slug] = loc
_new3("kurt-geiger", "Kurt Geiger", "Guildford", "retail", ["3d-letters"], "kg", 5,
      "Illuminated shopfront letters",
      "Illuminated letters above the glazed shopfront of Kurt Geiger in Guildford, made in Gateshead and fitted by our own team.",
      "A national fashion brand needed its shopfront letters made to its brand standards and installed in a busy shopping centre.",
      [("Illuminated letters", "White lit letters fixed above the full-height glazing."),
       ("Installation", "Fitted by our own crew, working around the centre's opening hours.")],
      "A crisp, evenly lit name that reads across the mall, more than 300 miles from our factory.",
      ["Guildford", None, 51.23700, -0.57649, "gps"], making=["p_n3_kg_4"])
_new3("reform-studio", "Reform Studio", None, "hospitality-leisure", ["flat-cut-letters", "vinyl-wall-graphics"], "rf", 6,
      "Studio logos and window graphics",
      "Built-up studio names and the R mark in each room, plus window and door graphics, for Reform Studio.",
      "A pilates studio wanted its calm, premium brand to carry from the front door into every studio room.",
      [("Studio logos", "'Studio One' and 'Studio Two' in built-up lettering with the R mark on each feature wall."),
       ("Window and door graphics", "A large printed window panel with the lit R logo, and frosted vinyl on the glass doors.")],
      "Each room has its own identity, and the brand is clear from the street.")
_new3("the-cell", "The Cell", None, "hospitality-leisure", ["3d-letters"], "cell", 4,
      "Halo-lit letters on a slatted wall",
      "Large halo-lit letters on a slatted feature wall for The Cell training space.",
      "The Cell wanted a statement logo that sets the tone of the gym as soon as you walk in.",
      [("Halo-lit letters", "Built-up metallic letters with LEDs behind, mounted on a slatted wall.")],
      "The logo lights the whole end wall and makes the space feel like a proper fight-camp gym.")
_new3("ward-quarters", "Ward Quarters", None, "commercial", ["3d-letters", "printed-fascia-panels"], "wq", 2,
      "Shopfront fascia and halo-lit logo",
      "A black shopfront fascia and a halo-lit WQ logo for Ward Quarters student living.",
      "Ward Quarters needed a frontage and reception logo that feel premium for student lets.",
      [("Fascia", "WQ logo and lettering on a black fascia above the shopfront."),
       ("Reception logo", "A halo-lit WQ logo on a slatted feature wall.")],
      "A smart front door and reception for the brand.")
_new3("mount-croft-care-home", "Mount Croft Care Home", None, "healthcare", ["3d-letters"], "mc", 2,
      "3D letters on brick",
      "Dark built-up letters fixed directly to the brick gable of Mount Croft Care Home.",
      "The care home wanted its name on the building so visitors can find it easily.",
      [("Building letters", "Built-up letters fixed to the brickwork on the gable end.")],
      "A clear, permanent name on the building.")
_new3("mariana-stanchevici-academy", "Mariana Stanchevici Lash & PMU Academy", None, "hair-beauty", ["3d-letters", "projecting-signs"], "ms", 3,
      "Halo-lit logo and projecting sign",
      "A halo-lit gold monogram on a slatted wall and projecting sign panels for a lash and permanent make-up academy.",
      "The academy wanted a reception logo that looks as premium as its training, plus a sign to be seen from the street.",
      [("Halo-lit logo", "A round black logo with gold monogram and lettering, lit from behind on a slatted wall."),
       ("Projecting sign", "Black panels with gold 'Beauty Salon' lettering and the academy web address.")],
      "The logo is now the backdrop to the academy's photos and training sessions.", making=["p_n3_ms_1", "p_n3_ms_2"])
_new3("east-holborn-street-signs", "East Holborn Street Signs", "South Shields", "transport", ["wayfinding"], "eh", 4,
      "Street nameplates",
      "Street nameplates with the council crest for East Holborn in South Shields.",
      "New street nameplates needed to match the council's standard design, crest and lettering.",
      [("Nameplates", "White plates with black lettering, a border and the full-colour council crest.")],
      "The plates were made, checked and packed in our workshop ready for installation.",
      ["South Shields", "south-tyneside", 54.99800, -1.43500, "place"])
_new3("frate", "Frate", "Newcastle", "hospitality-leisure", ["digital-large-format-print"], "frate", 3,
      "Printed plywood A-boards",
      "Full-colour A-boards printed straight onto natural plywood for Frate in Newcastle.",
      "Frate wanted pavement boards that feel crafted and independent, not plastic.",
      [("A-boards", "Artwork printed directly onto plywood panels on our flatbed printer, double-sided.")],
      "Boards with a natural wood finish that match Frate's independent style.", making=["p_n3_frate_2"])
_new3("cafe-barrier-banners", "We're Serving Costa", None, "hospitality-leisure", ["flags-banners", "digital-large-format-print"], "costa", 5,
      "Cafe barrier banners and roundels",
      "Printed cafe barrier banners and roundel signs for a venue serving Costa Coffee.",
      "The venue needed outdoor seating barriers and signs that show it serves Costa.",
      [("Barrier banners", "Printed banners on posts to section off the cafe seating."),
       ("Roundels", "Printed circular panels in the Costa colours.")],
      "A branded seating area that is quick to put out and take in.")
_new3("nusa", "Nusa", None, "hair-beauty", ["flat-cut-letters"], "nusa", 2,
      "Gold script wall letters",
      "The Nusa logo in gold script letters on a white feature wall.",
      "Nusa wanted a simple, elegant logo on the wall.",
      [("Wall letters", "Gold-finish script letters fixed off the wall.")],
      "A clean logo wall for the space.")
_new3("the-head-spa", "The Head Spa", None, "hair-beauty", ["flat-cut-letters"], "hs", 2,
      "Built-up logo on the wall",
      "The Head Spa logo in tone-on-tone built-up letters for The Head Spa at Pure Bliss.",
      "The Head Spa wanted a subtle logo that suits a relaxing treatment room.",
      [("Wall logo", "The sunburst logo and lettering cut and fixed to the wall in a matching colour.")],
      "A quiet, textured logo that suits the room.")
for _i, _sl in enumerate(["kurt-geiger", "reform-studio"]):
    _j = next(k for k, c in enumerate(CASES) if c["slug"] == _sl); CASES.insert(7 + _i, CASES.pop(_j))
for _c in CASES:
    if _c["slug"] == "cafe-barrier-banners": _c["hero"] = "p_n3_costa_1"

# ================= deeper pass: photos previously left out (19 Nov) =================
import json as _json
_C4 = _json.load(open("/home/claude/new3/pick4_counts.json"))
_N4 = lambda job: [f"p_n4_{job}_{i}" for i in range(_C4[job])]
_BY = {c["slug"]: c for c in CASES}
for _slug, _job in [("sunderland-eye-hospital","x_seh"),("thatype","x_thatype"),("black-rabbit","x_br"),("griffin-court","x_gc"),("glow-tanning","x_glow"),
                    ("aqua-tcg","x_aqua"),("elring-parts","x_el"),("tribeca","x_tribeca"),("byre","x_byre"),("fitt","x_fitt"),("filto","x_filto"),
                    ("welcome-to-durham","x_wtd"),("just-peachy","x_jp"),("my-car-cleaning","x_mcc"),("cafe-barrier-banners","x_costa"),
                    ("east-holborn-street-signs","x_eh"),("reform-studio","x_rf")]:
    _c = _BY[_slug]; _c["photos"] = _c["photos"] + [p for p in _N4(_job) if p not in _c["photos"]]
for _slug, _job in [("elring-parts","m_el"),("the-works","m_tw"),("nobles-casino","m_nob"),("grainger-market","m_gm"),("glow-tanning","m_glow")]:
    _c = _BY[_slug]; _c["making"] = list(_c.get("making") or []) + _N4(_job)
CASES.append(dict(slug="sir-bobby-robson-foundation", old=None, name="Sir Bobby Robson Foundation", where="Newcastle", sector="healthcare",
    types=["digital-large-format-print"], hero="p_n4_sbr_0", label="Framed ceremonial spade",
    lede="A deep box frame holding the ceremonial spade from the groundbreaking of the Sir Bobby Robson Institute, for the Sir Bobby Robson Foundation and Newcastle Hospitals Charity.",
    brief="The spade used to break ground on the new institute in April 2026 needed to be kept and presented as a keepsake worthy of the occasion.",
    made=[("Box frame", "A deep white frame built to hold the full-size spade securely."),
          ("Printed backing", "A full-colour printed panel with Sir Bobby's portrait, the foundation and charity logos and the event details.")],
    result="A presentation piece that records the day and the people behind the institute.",
    photos=_N4("sbr"), making=[]))
LOC["sir-bobby-robson-foundation"] = ["Newcastle", "newcastle", 54.98000, -1.61900, "place"]
CASES.append(dict(slug="bags-jamz", old=None, name="Bägs Jamz", where=None, sector="retail",
    types=["light-boxes"], hero="p_n4_bj_0", label="Illuminated light boxes",
    lede="Two blue illuminated light boxes with the Bägs Jamz graffiti logo in hot pink.",
    brief="Bägs Jamz wanted its hand-drawn logo kept exactly as drawn and lit up so it pops at night.",
    made=[("Light boxes", "A long box and a square box, each with a printed face and even LED lighting inside.")],
    result="The bright pink logo glows exactly as drawn.",
    photos=_N4("bj"), making=[]))
_OA = _json.load(open("/home/claude/new3/old_added.json"))
for _c in CASES:
    if _c["slug"] == "sunderland-eye-hospital":
        _c["photos"] = _c["photos"][:3] + _OA["seh"][:4] + _c["photos"][3:] + _OA["seh"][4:]
    if _c["slug"] == "fawcett-street-community-shop":
        _c["photos"] = _c["photos"][:2] + _OA["fw"][:5] + _c["photos"][2:] + _OA["fw"][5:]

# ================= audit: every catalogued photo not yet live (19 Nov) =================
_ADD5 = {
 "the-cell": ["cell"], "company-shop-group": ["fence2"], "aldi-jaymac-warehouse": ["jaymac_close","n_jaymac_close","n_jaymac_office","n_quality_close","p_z_aldijaymac_0"],
 "atom": ["n_atom","p_at_wall2"], "camden-clinic": ["n_camden_close","p_g_camden"], "savoy": ["n_savoy_ent","p_z_savoy_1"],
 "skin-and-soul": ["n_skinsoul_feel","p_x_skinandsou_2"], "nhs-community-diagnostic-centre": ["p_z_nhscommuni_0","p_z_woodhamaca_0","nhs_skyline2"],
 "copeland-residential": ["p_g_copeland"], "grace-kellys": ["p_gk_wide"], "pantera-advisory": ["p_pa_view"], "rustic-cup": ["p_rc_2"],
 "bar-marquee": ["p_x_barmarquee_1"], "baxters": ["p_x_baxters_1"], "bratz-salon": ["p_x_bratzsalon_0"], "combat-96": ["p_x_combat96_1"],
 "fora": ["p_x_fora_0"], "wink": ["p_x_goodlashga_0"], "kiss-me-irish": ["p_x_kissmeiris_1"], "level": ["p_x_level_1"], "lomond": ["p_x_lomond_0"],
 "maker": ["p_x_maker_0","p_x_maker_2"], "menu": ["p_x_menu_2","p_x_menu_3"], "originals-glow": ["p_x_originalsg_1"], "parm-o-rama": ["p_x_parmorama_0"],
 "the-cove": ["p_x_thecove_1"], "act-group": ["p_y_actgroup_1"], "better-you": ["p_y_betteryou_1"], "cowgirl-and-country": ["p_y_country_2"],
 "jam-jar": ["p_y_jamjar_1"], "lean-cuisine": ["p_y_leancuisin_0"], "little-her-hair": ["p_y_littleherh_1"], "vivana-lounge": ["p_z_vivanaloun_0"],
 "bar-seventy-three": ["seventy3","p_n4_s73_0"], "workwear-express": ["totW","totem_ww"], "fabios": ["vanFabio"], "park-electrical": ["vanPark"],
 "woodham-academy": ["w_logo","way_1","way_2"],
}
_MAKE5 = {"blacks-corner-tram-shelter": ["p_bc_m1"], "renewable-energy": ["p_x_renewablee_m0"], "bar-seventy-three": ["st_bench","st_cnc","st_weld","ws_cnc2"]}
for _c in CASES:
    _have = set([_c["hero"]] + list(_c["photos"]) + list(_c.get("making") or []))
    _c["photos"] = list(_c["photos"]) + [p for p in _ADD5.get(_c["slug"], []) if p not in _have]
    _c["making"] = list(_c.get("making") or []) + [p for p in _MAKE5.get(_c["slug"], []) if p not in _have]
    if _c["slug"] == "sir-bobby-robson-foundation":
        _c.update(hero="p_z_companysho_4", photos=["p_z_companysho_4"] + [p for p in _c["photos"] if p != "p_z_companysho_4"],
                  label="Institute hoarding and framed spade", types=["digital-large-format-print"],
                  lede="A printed site hoarding for the new Sir Bobby Robson Institute, and a box frame holding the ceremonial spade from its groundbreaking, for the Sir Bobby Robson Foundation and Newcastle Hospitals Charity.",
                  brief="The foundation's appeal for the new institute needed a hoarding that tells the story on site, and the spade from the April 2026 groundbreaking needed keeping as a presentation piece.",
                  made=[("Site hoarding", "A long run of printed hoarding panels with the 'Last & Greatest Team' appeal, staff photography and the plans for the institute."),
                        ("Box frame", "A deep white frame built to hold the full-size spade securely."),
                        ("Printed backing", "A full-colour panel with Sir Bobby's portrait, the foundation and charity logos and the event details.")],
                  result="The appeal is visible to everyone passing the site, and the groundbreaking is recorded in a piece worth keeping.")
    if _c["slug"] == "my-car-cleaning":
        _c["hero"] = "p_n3_mcc_1"; _c["photos"] = ["p_n3_mcc_1"] + [p for p in _c["photos"] if p != "p_n3_mcc_1"]
for _c in CASES:
    if _c["slug"] == "grainger-market" and "p_gm_2" not in _c["photos"]: _c["photos"].append("p_gm_2")
    if _c["slug"] == "nhs-community-diagnostic-centre" and "p_cdc_ent" not in _c["photos"]: _c["photos"].append("p_cdc_ent")

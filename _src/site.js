/* scroll a horizontal strip to show an item, without moving the page */
function stripTo(c,el){if(!c||!el)return;const cr=c.getBoundingClientRect(),er=el.getBoundingClientRect(),l=c.scrollLeft+(er.left-cr.left)-(c.clientWidth-er.width)/2;c.scrollTo({left:Math.max(0,l),behavior:matchMedia("(prefers-reduced-motion: reduce)").matches?"auto":"smooth"})}
/* Onesign & Digital — shared site behaviour */
(function(){
"use strict";
const $ = (s,r=document)=>r.querySelector(s);
const $$ = (s,r=document)=>[...r.querySelectorAll(s)];
const el = (tag,attrs={},html="")=>{const e=document.createElement(tag);for(const[k,v] of Object.entries(attrs)){if(v!=null)e.setAttribute(k,v)}if(html)e.innerHTML=html;return e};
const esc = s=>String(s).replace(/[&<>"]/g,c=>({"&":"&amp;","<":"&lt;",">":"&gt;",'"':"&quot;"}[c]));
const reduce = matchMedia("(prefers-reduced-motion: reduce)").matches;

/* ---------- NAV ---------- */
const nav=$("#nav"), megaBtn=$("#megaBtn"), mega=$("#mega"), burger=$("#burger"), drawer=$("#drawer");
let lastY=0;
function closeMega(){if(!mega)return;mega.classList.remove("open");nav.classList.remove("mega-on");megaBtn.setAttribute("aria-expanded","false")}
if(megaBtn) megaBtn.addEventListener("click",()=>{const o=!mega.classList.contains("open");mega.classList.toggle("open",o);nav.classList.toggle("mega-on",o);megaBtn.setAttribute("aria-expanded",String(o))});
document.addEventListener("click",e=>{if(nav&&!nav.contains(e.target))closeMega()});
document.addEventListener("keydown",e=>{if(e.key==="Escape"){closeMega();setDrawer(false);closeLb()}});
function setDrawer(o){if(!drawer)return;drawer.classList.toggle("open",o);nav.classList.toggle("drawer-on",o);burger.setAttribute("aria-expanded",String(o));burger.setAttribute("aria-label",o?"Close menu":"Open menu");document.body.style.overflow=o?"hidden":""}
if(burger) burger.addEventListener("click",()=>setDrawer(!drawer.classList.contains("open")));
if(drawer) drawer.addEventListener("click",e=>{if(e.target.closest("a"))setDrawer(false)});
const mob=$("#mobCta"), prog=$("#progress");
let ticking=false;
function onScroll(){
  const y=scrollY;
  nav.classList.toggle("scrolled",y>40);
  nav.classList.toggle("hide",y>lastY&&y>600&&!(mega&&mega.classList.contains("open"))&&!(drawer&&drawer.classList.contains("open")));
  lastY=y;
  if(mob) mob.classList.toggle("show",y>500&&y<document.body.scrollHeight-innerHeight-500);
  if(prog) prog.style.transform=`scaleX(${y/(document.documentElement.scrollHeight-innerHeight||1)})`;
  ticking=false;
}
addEventListener("scroll",()=>{if(!ticking){ticking=true;requestAnimationFrame(onScroll)}},{passive:true});
onScroll();

/* ---------- client logos: cursor magnifies + colours nearby logos ---------- */
const mqBox=$("#marqueeBox");
if(mqBox&&matchMedia("(hover:hover)").matches&&!reduce){
  const logos=$$("img",mqBox);
  let mx=-9999,my=-9999,active=false,raf=0;const R=170;
  function tick(){
    for(const l of logos){
      const b=l.getBoundingClientRect();
      const d=Math.hypot(b.left+b.width/2-mx,b.top+b.height/2-my);
      const f=active?Math.max(0,1-d/R):0, e=f*f*(3-2*f);
      l.style.transform=`scale(${(1+e*.28).toFixed(3)})`;
      l.style.filter=`grayscale(${(1-e).toFixed(2)})`;
      l.style.opacity=(.55+e*.45).toFixed(2);
    }
    raf=active?requestAnimationFrame(tick):0;
  }
  mqBox.addEventListener("mousemove",e=>{mx=e.clientX;my=e.clientY;if(!active){active=true;tick()}});
  mqBox.addEventListener("mouseleave",()=>{active=false;cancelAnimationFrame(raf);raf=0;tick()});
}

/* ---------- image preloading ---------- */
const cache=new Map();
function load(url){
  if(cache.has(url)) return cache.get(url);
  const im=new Image(); im.decoding="async"; im.src=url;
  const p=(im.decode?im.decode():new Promise((r,j)=>{im.onload=r;im.onerror=j})).then(()=>url,()=>url);
  cache.set(url,p); return p;
}

/* ---------- SIGN TYPES explorer (home) ---------- */
const dataEl=$("#typesData");
const TYPES=dataEl?JSON.parse(dataEl.textContent):[];
const list=$("#typeList");
if(list&&TYPES.length){
  const stage=$("#typeStage"), body=$("#typeBody");
  const tabs=$$("button",list);
  let cur=0, req=0;
  function layerFor(p){
    const L=el("div",{class:"layer frame"});
    L.innerHTML=`<img class="b" alt="" src="${p.bg}"><img class="f" alt="${esc(p.cap)}" src="${p.full}">`;
    return L;
  }
  function soonLayer(t){
    const L=el("div",{class:"layer"});
    L.innerHTML=`<div class="soon"><div><span>${esc(t.code)}</span><b>Project photos coming soon</b><p>We make these regularly. Ask us and we'll send examples of recent jobs.</p></div></div>`;
    return L;
  }
  function swapIn(L){
    $$(".layer",stage).forEach(o=>{if(o!==L){o.classList.remove("on");setTimeout(()=>o.remove(),400)}});
    stage.prepend(L);
    requestAnimationFrame(()=>L.classList.add("on"));
  }
  function setPhoto(t,i){
    const my=++req; const p=t.photos[i];
    $("#typeCap").textContent=p?p.cap:"";
    $("#typeCap").hidden=!p;
    if(!p){swapIn(soonLayer(t));return}
    Promise.all([load(p.full),load(p.bg)]).then(()=>{if(my===req)swapIn(layerFor(p))});
  }
  function show(n,force){
    const t=TYPES[n]; if(!t||(n===cur&&!force)) return;
    cur=n;
    tabs.forEach((b,i)=>{b.setAttribute("aria-selected",String(i===n));b.tabIndex=i===n?0:-1});
    $("#typePanel").setAttribute("aria-labelledby",tabs[n].id);
    setPhoto(t,0);
    stage.classList.toggle("has-thumbs",t.photos.length>1);
    const th=$("#typeThumbs"); th.innerHTML="";
    if(t.photos.length>1) t.photos.forEach((p,i)=>{
      const b=el("button",{"aria-pressed":String(i===0),"aria-label":"Show "+p.cap},`<img alt="" src="${p.thumb}">`);
      b.addEventListener("click",()=>{$$("button",th).forEach(x=>x.setAttribute("aria-pressed","false"));b.setAttribute("aria-pressed","true");setPhoto(t,i);stripTo(th,b)});
      th.appendChild(b);
    });
    $("#typeTitle").textContent=t.label;
    $("#typeDesc").textContent=t.desc;
    $("#typeCode").textContent=t.code;
    $("#typeIdeal").innerHTML=t.ideal.map(x=>`<span class="tag">${esc(x)}</span>`).join("");
    $("#typeSpec").innerHTML=t.spec.map(([a,b])=>`<dt>${esc(a)}</dt><dd>${esc(b)}</dd>`).join("");
    const more=$("#typeMore"); more.href=t.url; more.innerHTML=`everything about ${esc(t.label)} <span aria-hidden="true">→</span>`;
    if(!reduce){body.classList.remove("swap");void body.offsetWidth;body.classList.add("swap")}
    if(innerWidth<1100) stripTo(tabs[n].parentElement,tabs[n]);
    t.photos.slice(1).forEach(p=>load(p.full));
  }
  tabs.forEach((b,n)=>{
    b.addEventListener("click",()=>show(n));
    b.addEventListener("mouseenter",()=>TYPES[n].photos.slice(0,2).forEach(p=>{load(p.full);load(p.bg)}),{once:true});
  });
  list.addEventListener("keydown",e=>{const k=e.key;if(!["ArrowDown","ArrowUp","ArrowLeft","ArrowRight","Home","End"].includes(k))return;e.preventDefault();const n=k==="Home"?0:k==="End"?TYPES.length-1:(cur+((k==="ArrowDown"||k==="ArrowRight")?1:-1)+TYPES.length)%TYPES.length;show(n);tabs[n].focus()});
  const thBox=$("#typeThumbs");
  thBox.addEventListener("wheel",e=>{if(thBox.scrollWidth>thBox.clientWidth&&Math.abs(e.deltaY)>Math.abs(e.deltaX)){thBox.scrollLeft+=e.deltaY;e.preventDefault()}},{passive:false});
  show(0,true);
  $("#typeQuote").addEventListener("click",()=>{const s=$("#f-type");if(s)s.value=TYPES[cur].name});
  addEventListener("load",()=>{const all=TYPES.filter(t=>t.photos[0]).map(t=>t.photos[0]);let i=0;(function next(){if(i>=all.length)return;const p=all[i++];Promise.all([load(p.full),load(p.bg)]).then(()=>setTimeout(next,60))})()});
}

/* sign-type photo box: swipe left/right on phones to change photo (desktop keeps click-only thumbnails) */
(()=>{const st=$("#typeStage"),th=$("#typeThumbs");if(!st||!th)return;
  const mob=matchMedia("(max-width:900px)");let sx=0,sy=0,on=false;
  st.addEventListener("touchstart",e=>{if(!mob.matches)return;on=true;sx=e.touches[0].clientX;sy=e.touches[0].clientY},{passive:true});
  st.addEventListener("touchend",e=>{if(!on)return;on=false;const dx=e.changedTouches[0].clientX-sx,dy=e.changedTouches[0].clientY-sy;
    if(Math.abs(dx)<40||Math.abs(dx)<Math.abs(dy)*1.3)return;
    const bs=$$("button",th);if(bs.length<2)return;let i=bs.findIndex(b=>b.getAttribute("aria-pressed")==="true");
    i=(i+(dx<0?1:-1)+bs.length)%bs.length;bs[i].click();
    st.classList.remove("swipe-l","swipe-r");void st.offsetWidth;st.classList.add(dx<0?"swipe-l":"swipe-r")},{passive:true});
})();
/* ---------- gallery lightbox ---------- */
let lb=null, lbItems=[], lbIdx=0;
function openLb(items,i){
  if(!lb){
    lb=el("div",{class:"lb",role:"dialog","aria-modal":"true","aria-label":"Photo viewer"},`<img alt=""><div class="lb-cap"></div><button class="x" aria-label="Close">✕</button><button class="pv" aria-label="Previous photo">←</button><button class="nx" aria-label="Next photo">→</button>`);
    document.body.appendChild(lb);
    lb.addEventListener("click",e=>{if(e.target===lb)closeLb()});
    $(".x",lb).addEventListener("click",closeLb);
    $(".pv",lb).addEventListener("click",()=>stepLb(-1));
    $(".nx",lb).addEventListener("click",()=>stepLb(1));
    document.addEventListener("keydown",e=>{if(!lb.classList.contains("open"))return;if(e.key==="ArrowLeft")stepLb(-1);if(e.key==="ArrowRight")stepLb(1)});
    let sx=0;lb.addEventListener("touchstart",e=>{sx=e.touches[0].clientX},{passive:true});
    lb.addEventListener("touchend",e=>{const dx=e.changedTouches[0].clientX-sx;if(Math.abs(dx)>50)stepLb(dx<0?1:-1)});
  }
  lbItems=items; lbIdx=i; renderLb();
  lb.classList.add("open"); document.body.style.overflow="hidden"; $(".x",lb).focus();
}
function renderLb(){const it=lbItems[lbIdx];const im=$("img",lb);im.src=it.src;im.alt=it.cap;$(".lb-cap",lb).textContent=`${it.cap}  ·  ${lbIdx+1} / ${lbItems.length}`;$(".pv",lb).hidden=$(".nx",lb).hidden=lbItems.length<2}
function stepLb(d){lbIdx=(lbIdx+d+lbItems.length)%lbItems.length;renderLb()}
function closeLb(){if(lb&&lb.classList.contains("open")){lb.classList.remove("open");document.body.style.overflow=""}}
$$(".gallery").forEach(g=>{
  const figs=$$("figure",g);
  const items=figs.map(f=>({src:f.dataset.full,cap:f.dataset.cap||""}));
  figs.forEach((f,i)=>{f.tabIndex=0;f.setAttribute("role","button");f.setAttribute("aria-label","Enlarge: "+(f.dataset.cap||"photo"));
    f.addEventListener("click",()=>openLb(items,i));
    f.addEventListener("keydown",e=>{if(e.key==="Enter"||e.key===" "){e.preventDefault();openLb(items,i)}});
  });
});

/* ---------- FORM ---------- */
const form=$("#mockForm");
if(form){
  /* live "next available call": the next half hour at least 30 minutes away, inside opening hours (Mon-Thu 07-16, Fri 07-12) */
  const slotEl=$("#liveSlotTime");
  if(slotEl){
    const open={1:[7,16],2:[7,16],3:[7,16],4:[7,16],5:[7,12]};
    const fmt=d=>d.toLocaleTimeString("en-GB",{hour:"2-digit",minute:"2-digit",hour12:false});
    const next=()=>{const now=new Date(new Date().toLocaleString("en-US",{timeZone:"Europe/London"}));let d=new Date(now.getTime()+30*60000);d.setSeconds(0,0);d.setMinutes(d.getMinutes()<=30?(d.getMinutes()===0?0:30):60);
      for(let i=0;i<10;i++){const h=open[d.getDay()];if(h){const st=new Date(d);st.setHours(h[0]+1,0,0,0);const en=new Date(d);en.setHours(h[1],0,0,0);if(d<st)d=st;if(d<en){const sameDay=d.toDateString()===now.toDateString();const tm=new Date(now);tm.setDate(tm.getDate()+1);
        return (sameDay?"today":d.toDateString()===tm.toDateString()?"tomorrow":d.toLocaleDateString("en-GB",{weekday:"long"}))+" from "+fmt(d)}}
        d.setDate(d.getDate()+1);d.setHours(0,0,0,0)}return "soon"};
    const set=()=>{window.OS_SLOT=slotEl.textContent=next()};set(); setInterval(set,60000);
  }
  const call=$("#f-call"),sl=$("#sendLabel");
  if(call&&sl){const u=()=>{sl.textContent=call.checked?"send & call me back":"send my enquiry";$("#liveSlot").classList.toggle("off",!call.checked)};call.addEventListener("change",u);u()}
  const pre=document.body.dataset.signtype; if(pre&&$("#f-type"))$("#f-type").value=pre;
  const drop=$("#drop"), file=$("#f-file");
  ["dragenter","dragover"].forEach(ev=>drop.addEventListener(ev,e=>{e.preventDefault();drop.classList.add("over")}));
  ["dragleave","drop"].forEach(ev=>drop.addEventListener(ev,e=>{e.preventDefault();drop.classList.remove("over")}));
  drop.addEventListener("drop",e=>{if(e.dataTransfer.files.length){try{file.files=e.dataTransfer.files}catch(_){}showFiles(e.dataTransfer.files)}});
  file.addEventListener("change",()=>showFiles(file.files));
  function showFiles(f){if(!f.length)return;$("#dropText").textContent=`${f.length} photo${f.length>1?"s":""} added: ${[...f].map(x=>x.name).join(", ")}`}
  form.addEventListener("submit",e=>{
    e.preventDefault();
    const nm=$("#f-name"), em=$("#f-email");
    const okN=nm.value.trim().length>1, okE=/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(em.value.trim());
    $("#f-name-wrap").classList.toggle("invalid",!okN);
    $("#f-email-wrap").classList.toggle("invalid",!okE);
    if(!okN){nm.focus();return} if(!okE){em.focus();return}
    const v=id=>($(id)&&$(id).value||"").trim();
    const first=nm.value.trim().split(" ")[0], nfiles=file.files?file.files.length:0;
    const pick=n=>{const r=form.querySelector(`input[name=${n}]:checked`);return r?r.value:""};
    const lines=["Call back: "+($("#f-call")&&$("#f-call").checked?"Yes":"No"),"When: "+(pick("when")||"Not said"),"Budget: "+(pick("budget")||"Not said"),"Name: "+v("#f-name"),"Business: "+v("#f-biz"),"Email: "+v("#f-email"),"Phone: "+v("#f-tel"),"Sign type: "+(v("#f-type")||"Not sure yet"),"Site postcode: "+v("#f-post"),"","What I need:",v("#f-msg"),"","Sent from "+location.href];
    const done=(head,msg)=>{$("#doneName").parentNode.firstChild.textContent=head;$("#doneName").textContent=first;if(msg)$("#doneMsg").textContent=msg;form.classList.add("sent")};
    const byEmail=()=>{
      location.href="mailto:sales@onesignanddigital.com?subject="+encodeURIComponent("Sign enquiry from "+v("#f-name")+(v("#f-biz")?" ("+v("#f-biz")+")":""))+"&body="+encodeURIComponent(lines.join("\n"));
      done("one more step, ","Your email app should now be open with your enquiry filled in. Press send"+(nfiles?" and attach your photo":"")+" and it will reach us. If nothing opened, email sales@onesignanddigital.com or call 0191 487 6767.");
    };
    /* When HubSpot is connected (window.OS_FORM = {portal, form}) enquiries post straight to the Forms API. Until then the visitor's email app sends it. */
    const cfg=window.OS_FORM||{};
    if(cfg.portal&&cfg.form){
      const btn=form.querySelector("button[type=submit]"); btn.disabled=true;
      fetch("https://api.hsforms.com/submissions/v3/integration/submit/"+cfg.portal+"/"+cfg.form,{method:"POST",headers:{"Content-Type":"application/json"},
        body:JSON.stringify({fields:[["firstname",first],["lastname",nm.value.trim().split(" ").slice(1).join(" ")],["email",v("#f-email")],["phone",v("#f-tel")],["company",v("#f-biz")],["zip",v("#f-post")],
          ["website_sign_type",v("#f-type")||"Not sure yet"],["website_timescale",pick("when")||"Not said"],["website_budget",pick("budget")||"Not said"],["website_call_back",$("#f-call")&&$("#f-call").checked?"Yes":"No"],["website_call_slot",$("#f-call")&&$("#f-call").checked?(window.OS_SLOT||""):""],["message",v("#f-msg")]]
          .filter(([,x])=>x).map(([name,value])=>({objectTypeId:"0-1",name,value})),context:{pageUri:location.href,pageName:document.title}})})
        .then(r=>{if(!r.ok)throw 0;done("thanks, ",$("#f-call")&&$("#f-call").checked?"Your enquiry is in and we will call you back"+(window.OS_SLOT?" "+window.OS_SLOT:"")+"."+(nfiles?" Reply to our email with your building photo attached and we will start your mockup.":""):nfiles?"Your enquiry is in. Reply to our email with your building photo attached and we will start your mockup.":"")})
        .catch(()=>{btn.disabled=false;byEmail()});
    } else byEmail();
  });
}

/* ---------- HERO SHOWCASE ---------- */
const hs=$$("#heroMedia .hs"), hn=$$("#heroNow .hn");
if(hs.length>1){
  let i=0,t;
  const go=n=>{hs[i].classList.remove("on");hn[i].classList.remove("on");i=(n+hs.length)%hs.length;hs[i].classList.add("on");hn[i].classList.add("on")};
  const start=()=>{clearInterval(t);if(!reduce)t=setInterval(()=>go(i+1),6500)};
  hn.forEach((a,k)=>["mouseenter","focus"].forEach(ev=>a.addEventListener(ev,()=>{if(k!==i){go(k);start()}})));
  document.addEventListener("visibilitychange",()=>document.hidden?clearInterval(t):start());
  start();
}
/* ---------- AREAS: photo follows the hovered row ---------- */
const stage=$("#areaStage");
if(stage){
  let cur=stage.querySelector("img");
  $$("#areaList .arow").forEach(a=>["mouseenter","focus"].forEach(ev=>a.addEventListener(ev,()=>{
    const src=a.dataset.img; if(!src||cur.getAttribute("src")===src)return;
    const nx=el("img",{alt:"",src});nx.className="out";stage.appendChild(nx);
    const old=cur;cur=nx;requestAnimationFrame(()=>requestAnimationFrame(()=>{nx.classList.remove("out");old.classList.add("out")}));
    setTimeout(()=>old.remove(),700);
  })));
}
/* ---------- CASE STUDY FILTERS ---------- */
const filt=$("#filters");
if(filt){
  filt.addEventListener("click",e=>{const b=e.target.closest("button");if(!b)return;
    $$("button",filt).forEach(x=>x.classList.toggle("on",x===b));
    $$("#caseGrid .cc-wrap").forEach(c=>{c.hidden=b.dataset.f!=="all"&&c.dataset.sector!==b.dataset.f});
  });
}

/* ---------- MOTION ---------- */
const h1=$("#heroTitle");
if(!window.gsap||reduce){if(h1)h1.classList.add("revealed");return}
gsap.registerPlugin(ScrollTrigger);
document.documentElement.classList.add("js");

if(h1){
  const ex=$("#extrude");
  const extrude=(d,col)=>{let s=[];for(let i=1;i<=d;i++)s.push(`${(i*.5).toFixed(1)}px ${i}px 0 ${col}`);s.push(`${d*.5}px ${d+4}px 14px rgba(0,0,0,.28)`);return s.join(",")};
  const tl=gsap.timeline({defaults:{ease:"expo.out"}});
  tl.from("#heroTitle .line > span",{yPercent:110,duration:1.1,stagger:.11,onComplete:()=>h1.classList.add("revealed")})
    .from(".hero .eyebrow,.hero-sub,.hero-cta,.hero-card",{y:24,opacity:0,duration:1,stagger:.08},"-=.75")
    .to({d:0},{d:9,duration:1.2,ease:"power3.out",onUpdate(){ex.style.textShadow=extrude(Math.round(this.targets()[0].d),"#517d90")}},"-=.5")
    .add(()=>ex.classList.add("lit"),"-=.3");
  gsap.to("#heroMedia",{yPercent:14,ease:"none",scrollTrigger:{trigger:".hero",start:"top top",end:"bottom top",scrub:true}});
}
if($(".phero")){
  gsap.from(".phero-in > *",{y:26,opacity:0,duration:1,stagger:.08,ease:"expo.out"});
  if($(".phero .bgimg img")) gsap.fromTo(".phero .bgimg img",{scale:1.12},{scale:1,duration:2.2,ease:"power2.out"});
}
/* scroll reveals: soft fade and a short rise, rows come in together, no jump or flash */
const pending=[];let rq=0;
const check=()=>{clearTimeout(rq);rq=0;const line=innerHeight*.94,go=new Map();
  for(let i=pending.length-1;i>=0;i--){const p=pending[i];if(p.el.getBoundingClientRect().top<line){(go.get(p.o)||go.set(p.o,[]).get(p.o)).push(p.el);pending.splice(i,1)}}
  go.forEach((els,o)=>{els.reverse();gsap.to(els,{opacity:1,y:0,duration:o.d,ease:"power3.out",stagger:{each:o.each,ease:"power1.in"},overwrite:true})});
};
let lastQ=0;const queue=()=>{if(!pending.length)return;const n=Date.now();if(n-lastQ>50){lastQ=n;check()}else if(!rq)rq=setTimeout(check,60)};
addEventListener("scroll",queue,{passive:true});addEventListener("resize",queue);addEventListener("load",queue);
const reveal=(sel,{y=14,d=1.15,each=.07}={})=>{
  // live position check on every scroll frame: shows anything that has reached the bottom of the screen
  // or been scrolled past, so fast flicks on phones never leave a section blank
  const els=$$(sel); if(!els.length) return;
  gsap.set(els,{opacity:0,y}); const o={d,each};
  els.forEach(el=>pending.push({el,o})); queue();
};
reveal(".rv",{y:18,each:0});
if($(".explorer")) reveal(".type-stage,.spec",{y:20});
reveal(".tile",{y:16,d:1.3,each:.09});
reveal(".sector",{y:12,each:.06});
reveal(".step",{y:16,d:1.3,each:.1});
reveal(".variant,.point",{y:10});
reveal(".ccard,.gcard",{y:0,d:1.1,each:.06});
reveal(".made li",{y:10});
reveal(".arow",{y:0,d:.9,each:.04});
if($("#stepsBar")) gsap.to("#stepsBar",{scaleX:1,duration:1.6,ease:"power2.inOut",scrollTrigger:{trigger:"#steps",start:"top 80%",once:true}});
$$("[data-count]").forEach(e=>{const to=+e.dataset.count,o={v:0};gsap.to(o,{v:to,duration:1.6,ease:"power3.out",scrollTrigger:{trigger:e,start:"top 92%",once:true},onUpdate(){e.textContent=Math.round(o.v)}})});
addEventListener("load",()=>ScrollTrigger.refresh());
})();

/* ---------- job maps: MapLibre vector map (OpenFreeMap tiles, no key), recoloured to the Onesign palette ---------- */
(()=>{const maps=[...document.querySelectorAll(".jobmap[data-map]")];if(!maps.length)return;
  let loading=null;
  const need=()=>loading||(loading=new Promise((ok,no)=>{
    const css=document.createElement("link");css.rel="stylesheet";css.href="https://unpkg.com/maplibre-gl@4.7.1/dist/maplibre-gl.css";document.head.appendChild(css);
    const s=document.createElement("script");s.src="https://unpkg.com/maplibre-gl@4.7.1/dist/maplibre-gl.js";s.onload=ok;s.onerror=no;document.head.appendChild(s)}));
  const esc2=x=>String(x).replace(/[&<>"]/g,c=>({"&":"&amp;","<":"&lt;",">":"&gt;",'"':"&quot;"}[c]));
  const MARK='<svg viewBox="0 0 64 64" aria-hidden="true"><circle cx="32" cy="32" r="20" fill="none" stroke="#fff" stroke-width="7"/><path d="M28 22h8v22h-8z" fill="#9cc6d6"/></svg>';
  /* brand palette applied over the Positron style */
  const paint=m=>{const set=(id,p,v)=>{try{if(m.getLayer(id))m.setPaintProperty(id,p,v)}catch(_){}};
    m.getStyle().layers.forEach(l=>{
      if(l.id==="background")set(l.id,"background-color","#eef0ee");
      else if(l.id==="water")set(l.id,"fill-color","#c9dde5");
      else if(l.id==="waterway")set(l.id,"line-color","#c9dde5");
      else if(l.id==="park"||l.id==="landcover_wood")set(l.id,"fill-color","#e2e8e1");
      else if(l.id==="landuse_residential")set(l.id,"fill-color","#e9ebe8");
      else if(l.id==="building")set(l.id,"fill-color","#e1e4e2");
      else if(/^highway_(motorway|major)_inner|highway_motorway_bridge_inner/.test(l.id))set(l.id,"line-color","#ffffff");
      else if(/casing/.test(l.id))set(l.id,"line-color","#d9dedd");
      else if(/^highway_minor|highway_path/.test(l.id))set(l.id,"line-color","#fbfbfa");
      else if(/^boundary/.test(l.id))set(l.id,"line-color","#b9c6cb");
      else if(l.type==="symbol"){set(l.id,"text-color","#5d6b70");set(l.id,"text-halo-color","#eef0ee")}
    })};
  const build=box=>{const d=JSON.parse(box.dataset.map);box.innerHTML="";
    const isHQ=box.classList.contains("hq");
    const m=new maplibregl.Map({container:box,style:"https://tiles.openfreemap.org/styles/positron",center:d.hq||[54.97,-1.61].reverse(),zoom:isHQ?13.2:9,
      attributionControl:{compact:true},cooperativeGestures:true,dragRotate:false,pitchWithRotate:false});
    if(d.hq)m.setCenter([d.hq[1],d.hq[0]]);
    m.addControl(new maplibregl.NavigationControl({showCompass:false}),"top-right");
    m.on("styledata",()=>paint(m));
    const bounds=new maplibregl.LngLatBounds();
    /* job cards always open ABOVE their pin, and the map slides so the whole card and pin sit inside the map box.
       Short or narrow maps get a compact side-by-side card so it always has room. */
    const popCls="jm-popup"+(box.clientHeight<440||box.clientWidth<480?" compact":"");
    const keepIn=(pop,pin)=>pop.on("open",()=>{
      pop.setOffset(pin.offsetHeight+8);
      requestAnimationFrame(()=>{const p=pop.getElement();if(!p)return;
        const c=box.getBoundingClientRect(),r=p.getBoundingClientRect(),pt=m.project(pop.getLngLat()),pad=14;
        const top=r.top-c.top,left=r.left-c.left,right=r.right-c.left;let dx=0,dy=0;
        if(top<pad)dy=top-pad;else if(pt.y>c.height-pad)dy=pt.y-(c.height-pad);
        if(left<pad)dx=left-pad;else if(right>c.width-pad)dx=right-(c.width-pad);
        if(dx||dy)m.panBy([dx,dy],{duration:matchMedia("(prefers-reduced-motion:reduce)").matches?0:380})})});
    d.jobs.forEach(j=>{
      const el=document.createElement("button");el.type="button";el.className="jm-photo";el.setAttribute("aria-label",j.n+", "+j.p);
      el.innerHTML=`<img src="${esc2(j.i)}" alt="" loading="lazy"><i></i>`;
      const pop=new maplibregl.Popup({anchor:"bottom",offset:62,closeButton:true,maxWidth:"320px",className:popCls})
        .setHTML(`<a class="jm-pop" href="${esc2(j.u)}"><img src="${esc2(j.i)}" alt=""><span><small>${esc2(j.t)}</small><b>${esc2(j.n)}</b><em>${esc2(j.p)}</em><u>see the job →</u></span></a>`);
      new maplibregl.Marker({element:el,anchor:"bottom"}).setLngLat([j.lng,j.lat]).setPopup(pop).addTo(m);keepIn(pop,el);
      if(d.area?j.a===d.area:(j.lat>54.3&&j.lat<55.8&&j.lng>-2.6&&j.lng<-1))bounds.extend([j.lng,j.lat]);
    });
    if(d.hq){const el=document.createElement("button");el.type="button";el.className="jm-hq2";el.setAttribute("aria-label","Onesign & Digital HQ, Team Valley");
      el.innerHTML=`<span class="jm-hq2-badge">${MARK}<span><b>Onesign HQ</b><small>Team Valley, Gateshead</small></span></span><span class="jm-hq2-dot"></span>`;
      const pop=new maplibregl.Popup({anchor:"bottom",offset:70,maxWidth:"320px",className:popCls}).setHTML('<div class="jm-pop hq"><span><small>Our workshop &amp; showroom</small><b>Onesign &amp; Digital</b><em>D86 Princesway North, Team Valley, Gateshead NE11 0TU</em><em>Mon–Thu 7:00–16:00 · Fri 7:00–12:00</em><a href="https://www.google.com/maps/dir/?api=1&destination=54.9330,-1.6237" target="_blank" rel="noopener">get directions →</a></span></div>');
      new maplibregl.Marker({element:el,anchor:"bottom"}).setLngLat([d.hq[1],d.hq[0]]).setPopup(pop).addTo(m);keepIn(pop,el);
      if(!d.area)bounds.extend([d.hq[1],d.hq[0]])}
    m.on("load",()=>{paint(m);if(!isHQ&&!bounds.isEmpty())m.fitBounds(bounds,{padding:{top:60,bottom:30,left:40,right:40},maxZoom:13.5,duration:0})});
    if(!isHQ){const tag=document.createElement("div");tag.className="jm-count";const here=d.area?d.jobs.filter(x=>x.a===d.area).length:0;tag.innerHTML=d.area?`<b>${here}</b> here · <b>${d.jobs.length}</b> across the map · tap a photo`:`<b>${d.jobs.length}</b> jobs on the map · tap a photo`;box.appendChild(tag)}
  };
  const io=new IntersectionObserver(es=>es.forEach(e=>{if(!e.isIntersecting)return;io.unobserve(e.target);
    need().then(()=>build(e.target)).catch(()=>{const f=e.target.querySelector(".jm-fallback span");if(f)f.textContent="The map could not load. Our address is D86 Princesway North, Team Valley, Gateshead NE11 0TU."})}),{rootMargin:"300px"});
  maps.forEach(b=>io.observe(b));
})();

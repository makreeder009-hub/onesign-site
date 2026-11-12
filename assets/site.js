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
    stage.insertBefore(L,stage.firstChild);
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
      b.addEventListener("click",()=>{$$("button",th).forEach(x=>x.setAttribute("aria-pressed","false"));b.setAttribute("aria-pressed","true");setPhoto(t,i);b.scrollIntoView({block:"nearest",inline:"nearest",behavior:reduce?"auto":"smooth"})});
      th.appendChild(b);
    });
    $("#typeTitle").textContent=t.label;
    $("#typeDesc").textContent=t.desc;
    $("#typeCode").textContent=t.code;
    $("#typeIdeal").innerHTML=t.ideal.map(x=>`<span class="tag">${esc(x)}</span>`).join("");
    $("#typeSpec").innerHTML=t.spec.map(([a,b])=>`<dt>${esc(a)}</dt><dd>${esc(b)}</dd>`).join("");
    const more=$("#typeMore"); more.href=t.url; more.innerHTML=`everything about ${esc(t.label)} <span aria-hidden="true">→</span>`;
    if(!reduce){body.classList.remove("swap");void body.offsetWidth;body.classList.add("swap")}
    if(innerWidth<1100) tabs[n].scrollIntoView({block:"nearest",inline:"center",behavior:reduce?"auto":"smooth"});
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
    /* HubSpot hook: post to the Forms API here and subscribe the contact to "Marketing Information". */
    $("#doneName").textContent=nm.value.trim().split(" ")[0];
    form.classList.add("sent");
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
    .from("#heroImg",{scale:1.18,duration:2.4,ease:"power2.out"},0);
  gsap.to("#heroMedia",{yPercent:14,ease:"none",scrollTrigger:{trigger:".hero",start:"top top",end:"bottom top",scrub:true}});
}
if($(".phero")){
  gsap.from(".phero-in > *",{y:26,opacity:0,duration:1,stagger:.08,ease:"expo.out"});
  if($(".phero .bgimg img")) gsap.fromTo(".phero .bgimg img",{scale:1.12},{scale:1,duration:2.2,ease:"power2.out"});
}
$$(".rv").forEach(e=>gsap.to(e,{opacity:1,y:0,duration:1,ease:"expo.out",scrollTrigger:{trigger:e,start:"top 90%",once:true}}));
if($(".explorer")) gsap.from(".type-stage,.spec",{y:36,opacity:0,duration:1,stagger:.1,ease:"expo.out",scrollTrigger:{trigger:".explorer",start:"top 82%",once:true}});
const batch=(sel,vars)=>{if($(sel))ScrollTrigger.batch(sel,{once:true,start:"top 92%",onEnter:els=>gsap.from(els,vars)})};
batch(".tile",{y:40,opacity:0,duration:.9,stagger:.06,ease:"expo.out"});
batch(".sector",{opacity:0,duration:.8,stagger:.06,ease:"power2.out"});
batch(".step",{y:40,opacity:0,duration:.9,stagger:.12,ease:"expo.out"});
batch(".variant",{opacity:0,duration:.8,stagger:.08,ease:"power2.out"});
batch(".point",{opacity:0,duration:.8,stagger:.08,ease:"power2.out"});
if($("#stepsBar")) gsap.to("#stepsBar",{scaleX:1,duration:1.6,ease:"power2.inOut",scrollTrigger:{trigger:"#steps",start:"top 80%",once:true}});
$$("[data-count]").forEach(e=>{const to=+e.dataset.count,o={v:0};gsap.to(o,{v:to,duration:1.6,ease:"power3.out",scrollTrigger:{trigger:e,start:"top 92%",once:true},onUpdate(){e.textContent=Math.round(o.v)}})});
addEventListener("load",()=>ScrollTrigger.refresh());
})();

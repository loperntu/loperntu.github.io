// JS port of build.py for previewing inside the design tool. Keep in sync with build.py.
const UI = {
  en: {html_lang:"en", cover:"Cover", chapter:"Chapter {n}", appendix:"Appendix {x}", intuition:"Intuition", deep_dive:"Deep dive", q_open:"\u201c", q_close:"\u201d", book:"Book", nav_aria:"Toggle navigation", top_aria:"Back to top", source:"Source", page:"book.html"},
  zh: {html_lang:"zh-Hant", cover:"封面", chapter:"第 {n} 章", appendix:"附錄 {x}", intuition:"直覺", deep_dive:"深入", q_open:"「", q_close:"」", book:"本書", nav_aria:"切換目錄", top_aria:"回到頂端", source:"原始檔", page:"book-zh.html"},
};
const RAW_TAGS = ["div","figure","table","section","style","script","svg","details"];
function inline(text){
  const saved=[]; const keep=s=>{saved.push(s); return `\x00K${saved.length-1}\x00`;};
  text=text.replace(/\$\$[\s\S]*?\$\$/g, m=>keep(m));
  text=text.replace(/(?<!\\)\$(?!\$).+?(?<!\\)\$/g, m=>keep(m));
  text=text.replace(/`([^`]+?)`/g,(m,a)=>keep("<code>"+a.replace(/&/g,"&amp;").replace(/</g,"&lt;")+"</code>"));
  text=text.replace(/\[([^\]]+)\]\(([^)\s]+)\)/g,'<a href="$2">$1</a>');
  text=text.replace(/\*\*([\s\S]+?)\*\*/g,"<strong>$1</strong>");
  text=text.replace(/(?<![A-Za-z0-9*\\])\*(?![\s*])([\s\S]+?)(?<![\s*])\*(?![A-Za-z0-9*])/g,"<em>$1</em>");
  for(let k=0;k<2;k++) text=text.replace(/\x00K(\d+)\x00/g,(m,i)=>saved[+i]);
  return text;
}
function protectBlocks(content){
  const lines=content.split("\n"); const out=[], saved=[]; let i=0;
  const tagRe=new RegExp("^<("+RAW_TAGS.join("|")+")\\b");
  while(i<lines.length){
    const line=lines[i];
    if(line.startsWith("```")){
      const lang=line.slice(3).trim(); let j=i+1;
      while(j<lines.length && !lines[j].startsWith("```")) j++;
      const code=lines.slice(i+1,j).join("\n").replace(/&/g,"&amp;").replace(/</g,"&lt;").replace(/>/g,"&gt;");
      saved.push(`<pre><code${lang?` class="language-${lang}"`:""}>${code}</code></pre>`);
      out.push("",`\x00B${saved.length-1}\x00`,""); i=j+1; continue;
    }
    const m=line.match(tagRe);
    if(m){
      const tag=m[1]; let depth=0, j=i;
      while(j<lines.length){
        depth+=(lines[j].match(new RegExp("<"+tag+"\\b","g"))||[]).length-(lines[j].match(new RegExp("</"+tag+">","g"))||[]).length;
        if(depth<=0) break; j++;
      }
      let block=lines.slice(i,j+1).join("\n");
      if(tag==="table") block=`<div class="tbl-wrap">${block}</div>`;
      saved.push(block); out.push("",`\x00B${saved.length-1}\x00`,""); i=j+1; continue;
    }
    out.push(line); i++;
  }
  return [out.join("\n"), saved];
}
function renderList(block, ordered){
  const pat= ordered? /\n\s*\d+\.\s/ : /\n\s*[-*•]\s/;
  const items=("\n"+block).split(pat).map(s=>s.trim()).filter(Boolean);
  const tag=ordered?"ol":"ul";
  return `<${tag}>\n`+items.map(it=>"  <li>"+inline(it.replace(/\s*\n\s*/g," "))+"</li>").join("\n")+`\n</${tag}>`;
}
function renderBlocks(content, ui, saved, firstIsEpigraph=false){
  const html=[]; const blocks=content.split(/\n\s*\n/).map(b=>b.trim()).filter(Boolean);
  blocks.forEach((block,idx)=>{
    let m=block.match(/^\x00B(\d+)\x00$/); if(m){html.push(saved[+m[1]]);return;}
    const img=block.match(/^!\[([^\]]*)\]\(([^)]+)\)\s*$/);
    if(img){const cap=img[1]?`<figcaption>${inline(img[1])}</figcaption>`:"";html.push(`<figure class="fig"><img src="${img[2]}" alt="${img[1]}" loading="lazy">${cap}</figure>`);return;}
    if(block.startsWith("$$")&&block.endsWith("$$")){html.push(block);return;}
    if(block.startsWith(">")){html.push(renderQuote(block,ui,saved,firstIsEpigraph&&idx===0));return;}
    const h=block.match(/^(#{3,4})\s+(.+)$/);
    if(h && !block.includes("\n")){
      const title=h[2].trim();
      if(h[1].length===4){html.push(`<h4>${inline(title)}</h4>`);return;}
      const num=title.match(/^(\d+\.\d+)\s+(.*)/);
      if(num) html.push(`<h3 id="sec-${num[1].replace(".","-")}"><span class="section-num">${num[1]}</span> ${inline(num[2])}</h3>`);
      else html.push(`<h3>${inline(title)}</h3>`);
      return;
    }
    if(/^[-*•]\s/.test(block)){html.push(renderList(block,false));return;}
    if(/^\d+\.\s/.test(block)){html.push(renderList(block,true));return;}
    html.push(`<p>${inline(block)}</p>`);
  });
  return html.join("\n");
}
function renderQuote(block, ui, saved, isFirst){
  let tagLine=""; const body=[];
  for(const bl of block.split("\n")){const s=bl.trim(); if(s.startsWith("{.")&&s.endsWith("}")) tagLine=s; else body.push(bl.replace(/^>\s?/,""));}
  const text=body.join("\n").trim();
  const tm=tagLine.match(/\{\.([\w-]+)(?::\s*(.+?))?\}/);
  const kind=tm?tm[1]:(isFirst?"epigraph":"quote"); const title=tm&&tm[2]?tm[2]:"";
  if(kind==="deep-dive"||kind==="intuition"){
    const label=title||(kind==="intuition"?ui.intuition:ui.deep_dive);
    return `<div class="${kind}"><div class="box-label">${inline(label)}</div>\n${renderBlocks(text,ui,saved)}\n</div>`;
  }
  if(kind==="example") return `<div class="example-block"><p>${inline(text)}</p></div>`;
  if(kind==="epigraph"){
    const am=text.match(/\n\s*[—–]\s*(.+)$/);
    let quote=am?text.slice(0,am.index):text; const attr=am?am[1].trim():"";
    quote=quote.trim().replace(/^["\u201c\u201d\u300c\u300d]+|["\u201c\u201d\u300c\u300d]+$/g,"").trim();
    let out=`<div class="epigraph">\n  <p>${ui.q_open}${inline(quote)}${ui.q_close}</p>\n`;
    if(attr) out+=`  <div class="attribution">— ${inline(attr)}</div>\n`;
    return out+"</div>";
  }
  return `<blockquote>${renderBlocks(text,ui,saved)}</blockquote>`;
}
function buildBook(md, template, lang, srcName){
  const ui=UI[lang]; const meta={};
  const fm=md.match(/^---\n([\s\S]*?)\n---\n/);
  if(fm){ for(const line of fm[1].split("\n")){ if(line.includes(":")&&!line.startsWith(" ")){const k=line.slice(0,line.indexOf(":")).trim();let v=line.slice(line.indexOf(":")+1).trim().replace(/^["']|["']$/g,"");meta[k]=v;} } md=md.slice(fm[0].length); }
  md=md.replace(/<!--(?!\s*part:)[\s\S]*?-->/g,"");
  let saved; [md,saved]=protectBlocks(md);
  const parts=md.split(/^(<!--\s*part:.*?-->|# .*)$/m);
  const nav=[`    <a class="nav-link" href="#cover">${ui.cover}</a>`]; const body=[];
  for(let i=1;i<parts.length;i+=2){
    const sep=parts[i], content=parts[i+1]||"";
    const pm=sep.match(/<!--\s*part:\s*(.+?)\s*-->/); if(pm){nav.push(`    <div class="nav-part-label">${pm[1]}</div>`);continue;}
    const hm=sep.match(/^#\s+(.+?)(?:\s*\{([^}]*)\})?\s*$/); if(!hm) continue;
    const raw=hm[1].trim(), attrs=hm[2]||""; const idm=attrs.match(/#([\w-]+)/); const unnum=attrs.includes(".unnumbered");
    const ch=raw.match(/^Chapter\s+(\d+)\.\s*(.*)/), ap=raw.match(/^Appendix\s+(\w+)\.\s*(.*)/);
    let title,cid,label,navText;
    if(ch){title=ch[2].trim();cid=idm?idm[1]:"ch"+ch[1];label=ui.chapter.replace("{n}",ch[1]);navText=`<span class="ch-num">${ch[1]}</span> ${inline(title)}`;}
    else if(ap){title=ap[2].trim();cid=idm?idm[1]:"appendix-"+ap[1].toLowerCase();label=ui.appendix.replace("{x}",ap[1]);navText=inline(title);}
    else {title=raw;cid=idm?idm[1]:raw.toLowerCase().replace(/\W+/g,"-").replace(/^-|-$/g,"");label=unnum?raw:"";navText=inline(title);}
    nav.push(`    <a class="nav-link" href="#${cid}">${navText}</a>`);
    const isBib=cid.toLowerCase().includes("bibliography")||raw.toLowerCase().includes("bibliography");
    let h=`<article class="${isBib?"chapter bib-section":"chapter"}" id="${cid}">\n`;
    if(label) h+=`  <div class="chapter-label">${label}</div>\n`;
    h+=`  <h2 class="chapter-title">${inline(title)}</h2>\n`+renderBlocks(content.trim(),ui,saved,true)+"\n</article>\n";
    body.push(h);
  }
  const fills={TITLE:meta.title||"Untitled",SUBTITLE:meta.subtitle||"",AUTHOR:meta.author||"",DATE:meta.date||"",NAV:nav.join("\n"),BODY:body.join("\n\n"),HTML_LANG:ui.html_lang,LANG:lang,UI_BOOK:ui.book,UI_NAV_ARIA:ui.nav_aria,UI_TOP_ARIA:ui.top_aria,UI_SOURCE:ui.source,SRC_NAME:srcName,EN_CURRENT:lang==="en"?"current":"",ZH_CURRENT:lang==="zh"?"current":"",EN_PAGE:UI.en.page,ZH_PAGE:UI.zh.page};
  let out=template; for(const k in fills) out=out.split("{{"+k+"}}").join(fills[k]);
  return {html:out, chapters:body.length};
}

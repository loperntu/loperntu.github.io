const S_SEC = 'max-width:720px;margin:0 auto 28px;background:var(--color-neutral-100);border:1px solid var(--color-divider);box-shadow:var(--shadow-sm);padding:clamp(22px,5vw,52px) clamp(18px,6vw,60px) 26px;text-align:justify';
const HEADF = "font-family:'Cormorant Garamond','Noto Serif TC',serif;font-weight:600";
const md = s => s.replace(/\$([A-Za-zα-ω]+′?\*?)(?:_([A-Za-z0-9]+))?\$/g, (m, a, b) => `<var>${a}${b ? `<sub>${b}</sub>` : ''}</var>`);
const sv = s => s.replace(/§([^§]+)§/g, '<tspan style="font-family:TeXVar,TeXSym,serif">$1</tspan>');
const SEC = (label, run, inner) => `<section data-screen-label="@@N@@ ${label}" style="${S_SEC}">
<header style="display:flex;justify-content:space-between;gap:12px;font-size:12px;letter-spacing:.16em;color:var(--color-neutral-700);border-bottom:1px solid var(--color-divider);padding-bottom:8px;margin-bottom:24px"><span>語意學的圖論基礎</span><span>${run}</span></header>
${md(inner)}
<footer style="text-align:center;font-size:12px;color:var(--color-neutral-600);margin-top:28px">@@F@@</footer>
</section>
`;
const CH = (n, t, en, src) => `<div style="display:grid;grid-template-columns:auto minmax(0,1fr);gap:0 22px;align-items:center;border-top:1px solid var(--color-text);border-bottom:1px solid var(--color-divider);padding:14px 0 16px;margin:0 0 20px;text-align:left"><div style="font-family:'Cormorant Garamond',serif;font-weight:400;font-size:76px;line-height:1;color:var(--color-accent);font-variant-numeric:tabular-nums">${n}</div><div><div style="font-size:12px;letter-spacing:.2em;color:var(--color-accent-700)">第 ${n} 章</div><h2 style="${HEADF};font-size:30px;letter-spacing:.08em;margin:2px 0 0;line-height:1.3">${t}</h2><div style="font-family:'Cormorant Garamond',serif;font-style:italic;font-size:17px;color:var(--color-neutral-700)">${en}</div>${src ? `<sc-if value="{{ showSources }}" hint-placeholder-val="{{ true }}"><div style="font-size:12px;color:var(--color-neutral-600);margin-top:2px">${src}</div></sc-if>` : ''}</div></div>
`;
const H3 = (n, t, top = 30) => `<h3 style="${HEADF};font-size:22px;line-height:1.35;margin:${top}px 0 4px;text-align:left"><span style="color:var(--color-accent);font-variant-numeric:tabular-nums;margin-right:.7em">${n}</span>${t}</h3>
`;
const SUB = t => `<p style="font-style:italic;color:var(--color-neutral-700);margin:0 0 10px">${t}</p>\n`;
const C = (t, en) => `<span style="color:var(--color-accent-700);font-weight:600;white-space:nowrap"><span style="display:inline-block;width:.6em;height:.6em;border:1.2px solid var(--color-accent);margin-right:.4em;vertical-align:.05em"></span>${t}</span>${en ? `（<i>${en}</i>）` : ''}`;
const R = (t, en) => `<span style="color:var(--color-accent-700);font-weight:600;white-space:nowrap"><span style="display:inline-block;width:.55em;height:.55em;border:1.2px solid var(--color-accent);margin-right:.45em;vertical-align:.1em;transform:rotate(45deg)"></span>${t}</span>${en ? `（<i>${en}</i>）` : ''}`;
const DP = t => `<p style="margin:12px 0 6px">${t}</p>\n`;
const P = t => `<p>${t}</p>\n`;
const BOX = (t, wrap) => `<div style="text-align:center;margin:14px 0 16px;font-size:16px;line-height:1.9;overflow-x:auto"><span style="display:inline-block;border:1px solid var(--color-accent);padding:8px 18px;text-align:left;${wrap ? 'max-width:100%;box-sizing:border-box' : 'white-space:nowrap'}">${t}</span></div>\n`;
const NOTE = t => `<p style="font-size:14px;font-style:italic;color:var(--color-neutral-700);margin:8px 0">附註：${t}</p>\n`;
const LV = t => `<sc-if value="{{ showNotes }}" hint-placeholder-val="{{ true }}"><div style="position:relative;border:1px solid var(--color-accent);padding:18px 16px 10px;margin:26px 0 12px"><span style="position:absolute;top:-.85em;left:12px;background:var(--color-neutral-100);padding:0 6px;font-size:12.5px;letter-spacing:.14em;color:var(--color-accent-700);font-weight:600">語言學視角</span><p style="margin:0 0 6px;text-align:left;font-size:14.5px;line-height:1.8">${t}</p></div></sc-if>\n`;
const DL = (rows, w = '7em') => `<div style="display:grid;grid-template-columns:minmax(0,1fr);border-top:1px solid var(--color-text);margin:12px 0 14px">${rows.map(([a, b]) => `<div style="display:grid;grid-template-columns:${w} minmax(0,1fr);gap:14px;padding:10px 0;border-bottom:1px solid var(--color-divider)"><div style="font-weight:600">${a}</div><div>${b}</div></div>`).join('')}</div>\n`;
const TBL = (heads, rows, minw = 480, hl = -1) => `<div style="overflow-x:auto;margin:10px 0 14px"><table class="table" style="font-size:14px;line-height:1.6;min-width:${minw}px"><thead><tr>${heads.map(h => `<th style="text-transform:none;font-size:12px">${h}</th>`).join('')}</tr></thead><tbody>${rows.map((r, i) => `<tr${i === hl ? ' style="background:var(--color-accent-100)"' : ''}>${r.map(c => `<td>${c}</td>`).join('')}</tr>`).join('')}</tbody></table></div>\n`;
const FIG = (svg, cap) => `<figure style="margin:16px 0 18px">${svg}${cap ? `<figcaption style="text-align:center;font-size:12px;color:var(--color-neutral-700);margin-top:8px">${cap}</figcaption>` : ''}</figure>\n`;
const FORM = (rows) => `<div style="font-size:15px;line-height:1.95;margin:8px 0 12px;overflow-x:auto"><div style="display:grid;grid-template-columns:max-content max-content;gap:0 16px;justify-content:center;white-space:nowrap;text-align:left">${rows.map(([a, b]) => `<span>${a}</span><span style="color:var(--color-neutral-700);font-size:13.5px">${b || ''}</span>`).join('')}</div></div>\n`;
const EX = (n, title, q, ans) => `<div style="border-top:1px solid var(--color-text);margin:22px 0 10px;padding-top:10px"><div style="display:flex;justify-content:space-between;align-items:center;gap:12px"><span style="font-size:12.5px;letter-spacing:.16em;color:var(--color-accent-700);font-weight:600">練習 ${n}　${title}</span><button class="btn btn-ghost" onClick="{{ tog${n} }}" style="font-size:13px">{{ lab${n} }}</button></div><p style="margin:8px 0 6px">${q}</p><sc-if value="{{ ans${n} }}" hint-placeholder-val="{{ false }}"><div style="position:relative;border:1px solid var(--color-divider);padding:16px 16px 8px;margin:16px 0 8px;background:var(--color-bg)"><span style="position:absolute;top:-.8em;left:12px;background:var(--color-bg);padding:0 6px;font-size:12px;letter-spacing:.14em;color:var(--color-neutral-700)">解答</span><div style="font-size:14.5px;line-height:1.85">${ans}</div></div></sc-if></div>\n`;
const SVG = (vb, maxw, aria, inner) => `<svg viewBox="${vb}" style="display:block;width:100%;height:auto;max-width:${maxw}px;margin:0 auto;overflow:visible" role="img" aria-label="${aria}">${sv(inner)}</svg>`;
const T = (x, y, s, st = '') => `<text x="${x}" y="${y}" fill="currentColor" style="font-size:13px;text-anchor:middle;${st}">${s}</text>`;
const tw = l => { const s = l.replace(/<[^>]+>|§/g, ''); let w = 0; for (const ch of s) w += /[\u3000-\u9fff\uff00-\uffef]/.test(ch) ? 13.5 : 7.6; return w; };
const G = (o) => {
  const N = {};
  o.nodes.forEach(n => { const w = tw(n[3]) + 16; N[n[0]] = { x: n[1], y: n[2], l: n[3], c: n[4] || '', hw: w / 2, hh: 13, ex: n[5] }; });
  const cut = (a, b) => { const dx = b.x - a.x, dy = b.y - a.y; const t = Math.min(dx ? a.hw / Math.abs(dx) : 1e9, dy ? a.hh / Math.abs(dy) : 1e9); return [a.x + dx * t, a.y + dy * t]; };
  let out = '';
  for (const e of (o.edges || [])) {
    const [ia, ib, f = '', lab, lpos] = e; const A = N[ia], B = N[ib];
    const p1 = cut(A, B), p2 = cut(B, A);
    const col = f.includes('h') ? 'var(--color-accent)' : f.includes('m') ? 'var(--color-neutral-400)' : 'currentColor';
    const sw = f.includes('h') ? 1.4 : .9;
    out += `<line x1="${p1[0].toFixed(1)}" y1="${p1[1].toFixed(1)}" x2="${p2[0].toFixed(1)}" y2="${p2[1].toFixed(1)}" style="stroke:${col};stroke-width:${sw}${f.includes('-') ? ';stroke-dasharray:4 3' : ''}"></line>`;
    const arrow = (P, Q) => { const dx = P[0] - Q[0], dy = P[1] - Q[1], L = Math.hypot(dx, dy) || 1, ux = dx / L, uy = dy / L; const bx = P[0] - ux * 8, by = P[1] - uy * 8; return `<polygon points="${P[0].toFixed(1)},${P[1].toFixed(1)} ${(bx - uy * 3.5).toFixed(1)},${(by + ux * 3.5).toFixed(1)} ${(bx + uy * 3.5).toFixed(1)},${(by - ux * 3.5).toFixed(1)}" style="fill:${col}"></polygon>`; };
    if (f.includes('>')) out += arrow(p2, p1);
    if (f.includes('<')) out += arrow(p1, p2);
    if (lab) { const mx = (p1[0] + p2[0]) / 2, my = (p1[1] + p2[1]) / 2; const dx = p2[0] - p1[0], dy = p2[1] - p1[1], L = Math.hypot(dx, dy) || 1; const k = lpos ?? 0; out += `<text x="${(mx - dy / L * k).toFixed(1)}" y="${(my + dx / L * k + 4).toFixed(1)}" style="font-size:11.5px;text-anchor:middle;fill:${f.includes('h') ? 'var(--color-accent-800)' : 'var(--color-neutral-700)'};paint-order:stroke;stroke:var(--color-neutral-100);stroke-width:4px">${lab}</text>`; }
  }
  for (const k in N) {
    const n = N[k];
    const rs = n.c === 'f' ? 'fill:var(--color-accent-100);stroke:var(--color-accent);stroke-width:1.3' : n.c === 'a' ? 'fill:var(--color-neutral-100);stroke:var(--color-accent);stroke-width:1.3' : n.c === 'm' ? 'fill:var(--color-neutral-100);stroke:var(--color-neutral-400);stroke-width:.8' : 'fill:var(--color-neutral-100);stroke:currentColor;stroke-width:.8';
    if (n.c !== 'p') out += `<rect x="${(n.x - n.hw).toFixed(1)}" y="${n.y - n.hh}" width="${(n.hw * 2).toFixed(1)}" height="${n.hh * 2}" rx="2" style="${rs}"></rect>`;
    out += `<text x="${n.x}" y="${n.y + 4.5}" fill="currentColor" style="font-size:13px;text-anchor:middle;${n.c === 'm' ? 'fill:var(--color-neutral-600)' : ''}">${n.l}</text>`;
    if (n.ex) out += `<text x="${(n.x + n.hw + 3).toFixed(1)}" y="${n.y - 10}" style="font-size:11.5px;fill:var(--color-accent-700)">${n.ex}</text>`;
  }
  return SVG(`0 0 ${o.w} ${o.h}`, o.maxw || o.w, o.aria, out + (o.extra || ''));
};

return {S_SEC,HEADF,md,sv,SEC,CH,H3,SUB,C,R,DP,P,BOX,NOTE,LV,DL,TBL,FIG,FORM,EX,SVG,T,tw,G};

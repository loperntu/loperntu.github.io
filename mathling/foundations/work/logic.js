class Component extends DCLogic {
  state = { ans: {}, toc: [], act: '', actCh: '', vw: 1400, tocOpen: false, bfsStart: 'dog', bfsStep: 0, wa: 'dog', wb: 'cat', pick: 'A' };
  componentDidMount() {
    this._onScroll = () => { cancelAnimationFrame(this._raf); this._raf = requestAnimationFrame(() => this.trackActive()); };
    this._onResize = () => { this.setState({ vw: window.innerWidth }); this._onScroll(); };
    document.addEventListener('scroll', this._onScroll, true);
    window.addEventListener('resize', this._onResize);
    this._t = setTimeout(() => this.buildToc(), 400);
    this.setState({ vw: window.innerWidth });
  }
  componentWillUnmount() {
    document.removeEventListener('scroll', this._onScroll, true);
    window.removeEventListener('resize', this._onResize);
    clearTimeout(this._t);
  }
  buildToc() {
    const hs = [...document.querySelectorAll('section h2, section h3')];
    const toc = []; let cur = null; let i = 0;
    hs.forEach(h => {
      const id = 'toc-' + (i++);
      h.setAttribute('data-toc', id);
      if (h.tagName === 'H2') {
        const g = h.closest('div') && h.closest('div').parentElement;
        const num = g && g.firstElementChild ? g.firstElementChild.textContent.trim() : '';
        cur = { id, num, label: h.textContent.trim(), subs: [] };
        toc.push(cur);
      } else {
        const sp = h.querySelector('span');
        const num = sp ? sp.textContent.trim() : '';
        const label = h.textContent.trim().slice(num.length).trim();
        if (num === '·' || !cur) { cur = { id, num: '·', label, subs: [] }; toc.push(cur); }
        else cur.subs.push({ id, num, label });
      }
    });
    this.setState({ toc }, () => this.trackActive());
  }
  trackActive() {
    const els = [...document.querySelectorAll('[data-toc]')];
    let act = els.length ? els[0].getAttribute('data-toc') : '';
    for (const el of els) { if (el.getBoundingClientRect().top < 140) act = el.getAttribute('data-toc'); else break; }
    let actCh = '';
    for (const c of this.state.toc) { if (c.id === act || c.subs.some(s => s.id === act)) { actCh = c.id; break; } }
    if (act !== this.state.act || actCh !== this.state.actCh) this.setState({ act, actCh });
  }
  scrollerOf(el) {
    let p = el.parentElement;
    while (p && p !== document.body) {
      const o = getComputedStyle(p).overflowY;
      if ((o === 'auto' || o === 'scroll') && p.scrollHeight > p.clientHeight) return p;
      p = p.parentElement;
    }
    return document.scrollingElement || document.documentElement;
  }
  goTo(id) {
    const el = document.querySelector('[data-toc="' + id + '"]');
    if (!el) return;
    const sc = this.scrollerOf(el);
    const base = sc === document.scrollingElement || sc === document.documentElement ? 0 : sc.getBoundingClientRect().top;
    sc.scrollTo({ top: sc.scrollTop + el.getBoundingClientRect().top - base - 28, behavior: 'smooth' });
    if (this.state.vw < 1240) this.setState({ tocOpen: false });
  }
  tw(l) { let w = 0; for (const ch of l) w += /[\u3000-\u9fff]/.test(ch) ? 13.5 : 7.6; return w; }
  // ---------- BFS demo ----------
  bfsN = { ani: ['動物', 70, 110], cat: ['貓', 190, 50], pet: ['寵物', 190, 170], dog: ['狗', 310, 110], bone: ['骨頭', 430, 40], tail: ['尾巴', 430, 180], lion: ['獅子', 550, 110], grass: ['草原', 610, 200] };
  bfsE = [['dog', 'cat'], ['dog', 'pet'], ['cat', 'pet'], ['dog', 'bone'], ['dog', 'tail'], ['cat', 'ani'], ['tail', 'lion'], ['lion', 'grass']];
  bfsDist(s) {
    const adj = {}; Object.keys(this.bfsN).forEach(k => adj[k] = []);
    this.bfsE.forEach(([a, b]) => { adj[a].push(b); adj[b].push(a); });
    const d = { [s]: 0 }; const q = [s];
    while (q.length) { const u = q.shift(); for (const v of adj[u]) if (!(v in d)) { d[v] = d[u] + 1; q.push(v); } }
    return d;
  }
  bfsVals() {
    const { bfsStart, bfsStep } = this.state;
    const d = this.bfsDist(bfsStart);
    const maxD = Math.max(...Object.values(d));
    const nodes = Object.entries(this.bfsN).map(([k, [l, x, y]]) => {
      const w = this.tw(l) + 16; const dk = d[k];
      const done = dk < bfsStep, front = dk === bfsStep;
      return {
        label: l, x, ty: y + 4.5, rx: x - w / 2, ry: y - 13, rw: w,
        rst: { fill: done ? 'var(--color-accent-100)' : 'var(--color-neutral-100)', stroke: done || front ? 'var(--color-accent)' : 'currentColor', strokeWidth: done || front ? 1.4 : .8, cursor: 'pointer' },
        dist: dk <= bfsStep ? String(dk) : '', dx: x + w / 2 + 3, dy: y - 10,
        pick: () => this.setState({ bfsStart: k, bfsStep: 0 })
      };
    });
    const edges = this.bfsE.map(([a, b]) => {
      const A = this.bfsN[a], B = this.bfsN[b];
      const on = Math.abs(d[a] - d[b]) === 1 && Math.max(d[a], d[b]) <= bfsStep;
      return { x1: A[1], y1: A[2], x2: B[1], y2: B[2], st: { stroke: on ? 'var(--color-accent)' : 'var(--color-neutral-400)', strokeWidth: on ? 1.4 : .8 } };
    });
    const layer = Object.entries(d).filter(([, v]) => v === bfsStep).map(([k]) => this.bfsN[k][0]).join('、');
    return {
      bfsNodes: nodes, bfsEdges: edges,
      bfsText: React.createElement('g', { style: { pointerEvents: 'none' } }, ...nodes.flatMap((n, i) => [
        React.createElement('text', { key: 'l' + i, x: n.x, y: n.ty, fill: 'currentColor', style: { fontSize: '13px', textAnchor: 'middle' } }, n.label),
        React.createElement('text', { key: 'd' + i, x: n.dx, y: n.dy, style: { fontSize: '12px', fill: 'var(--color-accent-700)' } }, n.dist)])),
      bfsInfo: bfsStep === 0 ? `起點「${this.bfsN[bfsStart][0]}」，距離 0。` : `第 ${bfsStep} 層（距離 ${bfsStep}）：${layer}`,
      bfsDone: bfsStep >= maxD,
      bfsNext: () => this.setState(s => ({ bfsStep: Math.min(maxD, s.bfsStep + 1) })),
      bfsReset: () => this.setState({ bfsStep: 0 })
    };
  }
  // ---------- mini wordnet ----------
  W = {
    ent: { l: ['實體'], g: '一切存在的事物', p: [], f: 5 },
    obj: { l: ['物體'], g: '具有實體、占有空間的東西', p: ['ent'], f: 20 },
    abs: { l: ['抽象事物'], g: '不具實體的概念或內容', p: ['ent'], f: 10 },
    liv: { l: ['生物'], g: '具有生命的個體', p: ['obj'], f: 30 },
    art: { l: ['人工物'], g: '由人製造的物品', p: ['obj'], f: 15 },
    ani: { l: ['動物'], g: '能自主移動、攝取食物維生的生物', p: ['liv'], f: 120 },
    pla: { l: ['植物'], g: '能行光合作用、通常固定生長的生物', p: ['liv'], f: 60 },
    mam: { l: ['哺乳動物'], g: '以乳汁哺育幼體的動物', p: ['ani'], f: 25 },
    bir: { l: ['鳥'], g: '有羽毛、卵生的動物，多數會飛', p: ['ani'], f: 80 },
    dog: { l: ['狗', '犬'], g: '常被人飼養、嗅覺靈敏的哺乳動物', p: ['mam'], f: 150, para: ['cat'] },
    cat: { l: ['貓'], g: '常被人飼養、善於捕鼠的哺乳動物', p: ['mam'], f: 110, para: ['dog'] },
    wha: { l: ['鯨', '鯨魚'], g: '生活在海中的大型哺乳動物', p: ['mam'], f: 20 },
    pen: { l: ['企鵝'], g: '不會飛、善於游泳的海鳥', p: ['bir'], f: 12 },
    spa: { l: ['麻雀'], g: '常見於住家附近的小型鳥類', p: ['bir'], f: 18 },
    tre: { l: ['樹', '樹木'], g: '有木質主幹的多年生植物', p: ['pla'], f: 90 },
    flo: { l: ['花'], g: '植物的繁殖器官，常有鮮豔的顏色', p: ['pla'], f: 100 },
    too: { l: ['工具'], g: '工作時必須使用的具有特定功能的器具', p: ['art'], f: 40 },
    veh: { l: ['交通工具'], g: '用來載運人或貨物的器具', p: ['art'], f: 30 },
    car: { l: ['汽車', '車子'], g: '以引擎驅動、在道路上行駛的四輪交通工具', p: ['veh'], f: 140 },
    bik: { l: ['腳踏車', '自行車', '單車'], g: '以人力踩踏驅動的兩輪交通工具', p: ['veh'], f: 45 },
    whe: { l: ['輪子'], g: '可繞軸轉動的圓形零件', p: ['art'], f: 25, part: ['car', 'bik'] },
    kni: { l: ['刀', '刀子'], g: '用來切割的工具', p: ['too'], f: 50 },
    com: { l: ['電腦'], g: '能自動接受、儲存並處理資料的裝置', p: ['too'], f: 160, fac: ['功能：程式、軟體等', '實體：螢幕、鍵盤、主機等'] },
    inf: { l: ['資訊'], g: '經過整理、可以傳遞的內容', p: ['abs'], f: 70 },
    boo: { l: ['書', '書本'], g: '裝訂成冊、記載文字或圖畫的著作', p: ['art', 'inf'], f: 130, fac: ['實體：紙張、封面', '內容：文字、知識'] }
  };
  wnPrep() {
    if (this._wn) return this._wn;
    const W = this.W, ids = Object.keys(W);
    const anc = {};
    for (const id of ids) {
      const d = { [id]: 0 }, prev = {}; const q = [id];
      while (q.length) { const u = q.shift(); for (const v of W[u].p) if (!(v in d)) { d[v] = d[u] + 1; prev[v] = u; q.push(v); } }
      anc[id] = { d, prev };
    }
    const depth = {}; ids.forEach(id => depth[id] = anc[id].d.ent + 1);
    const D = Math.max(...Object.values(depth));
    const cum = {}; ids.forEach(c => cum[c] = ids.filter(x => c in anc[x].d).reduce((s, x) => s + W[x].f, 0));
    const ic = {}; ids.forEach(c => ic[c] = -Math.log(cum[c] / cum.ent));
    const kids = {}; ids.forEach(id => kids[id] = []);
    ids.forEach(id => { if (W[id].p.length) kids[W[id].p[0]].push(id); });
    const pos = {}; let leaf = 0;
    const lay = id => { if (!kids[id].length) { pos[id] = { x: 16 + (depth[id] - 1) * 116, y: 20 + leaf++ * 25 }; return; } kids[id].forEach(lay); const ys = kids[id].map(k => pos[k].y); pos[id] = { x: 16 + (depth[id] - 1) * 116, y: (Math.min(...ys) + Math.max(...ys)) / 2 }; };
    lay('ent');
    this._wn = { anc, depth, D, cum, ic, kids, pos, H: 20 + leaf * 25 };
    return this._wn;
  }
  chain(a, c) { const { anc } = this.wnPrep(); const out = [c]; let u = c; while (u !== a) { u = anc[a].prev[u]; out.push(u); } return out.reverse(); }
  wnVals() {
    const W = this.W; const { anc, depth, D, ic, kids, pos, H } = this.wnPrep();
    const { wa, wb, pick } = this.state;
    const A = anc[wa].d, B = anc[wb].d;
    const common = Object.keys(A).filter(c => c in B);
    let lcs = common[0];
    for (const c of common) { const s = A[c] + B[c], s0 = A[lcs] + B[lcs]; if (s < s0 || (s === s0 && depth[c] > depth[lcs])) lcs = c; }
    let lcsIC = common.reduce((m, c) => ic[c] > ic[m] ? c : m, common[0]);
    const d = A[lcs] + B[lcs];
    const name = id => W[id].l[0];
    const ca = this.chain(wa, lcs), cb = this.chain(wb, lcs);
    const onPath = new Set([...ca, ...cb]);
    const pathEdges = new Set();
    for (const ch of [ca, cb]) for (let i = 0; i + 1 < ch.length; i++) pathEdges.add(ch[i] + '>' + ch[i + 1]);
    const f3 = x => (Math.round(x * 1000) / 1000).toFixed(3);
    const icA = ic[wa], icB = ic[wb], r = ic[lcsIC];
    const pathSim = 1 / (d + 1), lch = -Math.log((d + 1) / (2 * D)), wup = 2 * depth[lcs] / (depth[wa] + depth[wb]);
    const lin = icA + icB === 0 ? 1 : 2 * r / (icA + icB), jd = icA + icB - 2 * r;
    const tagOf = id => id === wa && id === wb ? 'A=B' : id === wa ? 'A' : id === wb ? 'B' : id === lcs ? 'LCS' : '';
    const nodeW = id => this.tw(name(id)) + 14 + (tagOf(id) ? this.tw(tagOf(id)) + 6 : 0);
    const treeNodes = Object.keys(W).map(id => {
      const p = pos[id], w = nodeW(id), isA = id === wa, isB = id === wb, isL = id === lcs;
      return {
        label: name(id), tx: p.x + 7, ty: p.y + 4.5, rx: p.x, ry: p.y - 11, rw: w,
        rst: { fill: isL ? 'var(--color-accent-200)' : onPath.has(id) ? 'var(--color-accent-100)' : 'var(--color-neutral-100)', stroke: isA || isB || isL ? 'var(--color-accent-700)' : onPath.has(id) ? 'var(--color-accent)' : 'var(--color-neutral-500)', strokeWidth: isA || isB ? 2 : onPath.has(id) ? 1.3 : .7, cursor: 'pointer' },
        tag: tagOf(id), gx: p.x + w - 6, gy: p.y + 4,
        pickIt: () => this.setState(s => s.pick === 'A' ? { wa: id } : { wb: id })
      };
    });
    const treeEdges = [];
    Object.keys(W).forEach(id => W[id].p.forEach((par, i) => {
      const a = pos[id], b = pos[par], on = pathEdges.has(id + '>' + par);
      treeEdges.push({ d: `M${b.x + nodeW(par)},${b.y} C${b.x + nodeW(par) + 24},${b.y} ${a.x - 24},${a.y} ${a.x},${a.y}`, st: { fill: 'none', stroke: on ? 'var(--color-accent)' : 'var(--color-neutral-400)', strokeWidth: on ? 1.8 : .8, strokeDasharray: i > 0 ? '4 3' : 'none' } });
    }));
    const hyper = id => W[id].p.map(name).join('、') || '（無，為根節點）';
    const hypo = id => Object.keys(W).filter(x => W[x].p.includes(id)).map(name).join('、') || '（無）';
    const rels = id => {
      const w = W[id], out = [];
      out.push({ k: '同義詞集', v: '{' + w.l.join('，') + '}' });
      out.push({ k: '釋義', v: w.g });
      out.push({ k: '上位詞', v: hyper(id) });
      out.push({ k: '下位詞', v: hypo(id) });
      if (w.part) out.push({ k: '部分（整體為）', v: w.part.map(name).join('、') });
      const holo = Object.keys(W).filter(x => (W[x].part || []).includes(id)).map(name);
      if (holo.length) out.push({ k: '有部分', v: holo.join('、') });
      if (w.para) out.push({ k: '類義詞', v: w.para.map(name).join('、') });
      if (w.fac) out.push({ k: '義面', v: w.fac.join('；') });
      out.push({ k: '深度／IC', v: `${depth[id]}／${f3(ic[id])}` });
      return out;
    };
    return {
      wnOptsA: Object.keys(W).map(id => ({ id, sel: id === wa, label: name(id) + (W[id].l.length > 1 ? `（${W[id].l.slice(1).join('、')}）` : '') })),
      wnOptsB: Object.keys(W).map(id => ({ id, sel: id === wb, label: name(id) + (W[id].l.length > 1 ? `（${W[id].l.slice(1).join('、')}）` : '') })),
      wa, wb, wnH: H, wnVB: `0 0 720 ${H}`,
      setA: e => this.setState({ wa: e.target.value }), setB: e => this.setState({ wb: e.target.value }),
      swapAB: () => this.setState(s => ({ wa: s.wb, wb: s.wa })),
      pickA: () => this.setState({ pick: 'A' }), pickB: () => this.setState({ pick: 'B' }),
      pickAst: { background: pick === 'A' ? 'var(--color-accent-100)' : 'transparent', fontWeight: pick === 'A' ? 600 : 400 },
      pickBst: { background: pick === 'B' ? 'var(--color-accent-100)' : 'transparent', fontWeight: pick === 'B' ? 600 : 400 },
      treeNodes, treeEdges,
      treeText: React.createElement('g', { style: { pointerEvents: 'none' } }, ...treeNodes.flatMap((n, i) => [
        React.createElement('text', { key: 'l' + i, x: n.tx, y: n.ty, fill: 'currentColor', style: { fontSize: '12.5px' } }, n.label),
        React.createElement('text', { key: 't' + i, x: n.gx, y: n.gy, style: { fontSize: '10.5px', fontWeight: 600, textAnchor: 'end', fill: 'var(--color-accent-800)' } }, n.tag)])),
      relA: rels(wa), relB: rels(wb), nameA: name(wa), nameB: name(wb),
      pathStr: [...ca.map(name), ...cb.slice(0, -1).reverse().map(name)].join(' — '),
      lcsName: name(lcs), lcsICName: name(lcsIC), dVal: String(d), Dval: String(D),
      depA: String(depth[wa]), depB: String(depth[wb]), depL: String(depth[lcs]),
      icAv: f3(icA), icBv: f3(icB), icLv: f3(r),
      simPath: f3(pathSim), simLch: f3(lch), simWup: f3(wup), simRes: f3(r), simLin: f3(lin), simJcn: jd === 0 ? '∞' : f3(1 / jd),
      fPath: `1 / (${d} + 1)`, fLch: `−log((${d} + 1) / (2 × ${D}))`, fWup: `2 × ${depth[lcs]} / (${depth[wa]} + ${depth[wb]})`,
      fRes: `IC(${name(lcsIC)})`, fLin: `2 × ${f3(r)} / (${f3(icA)} + ${f3(icB)})`, fJcn: jd === 0 ? '距離為 0' : `1 / (${f3(icA)} + ${f3(icB)} − 2 × ${f3(r)})`
    };
  }
  renderVals() {
    const { toc, act, actCh, vw, tocOpen } = this.state;
    const showToc = (this.props.showToc ?? true) && toc.length > 0;
    const wide = vw >= 1240;
    const linkBase = { display: 'flex', gap: '4px', textDecoration: 'none', lineHeight: 1.45, textAlign: 'left' };
    const tocList = toc.map(c => {
      const on = c.id === actCh;
      return {
        num: c.num, label: c.label, open: on && c.subs.length > 0,
        st: { ...linkBase, padding: '6px 0', fontSize: '14px', color: on ? 'var(--color-accent-800)' : 'var(--color-text)', fontWeight: on ? 600 : 400 },
        go: e => { e.preventDefault(); this.goTo(c.id); },
        subs: c.subs.map(s => ({
          num: s.num, label: s.label,
          st: { display: 'block', textDecoration: 'none', textAlign: 'left', fontSize: '12.5px', lineHeight: 1.45, padding: '3px 0 3px 8px', borderLeft: s.id === act ? '1.5px solid var(--color-accent)' : '1.5px solid transparent', color: s.id === act ? 'var(--color-accent-800)' : 'var(--color-neutral-700)' },
          go: e => { e.preventDefault(); this.goTo(s.id); }
        }))
      };
    });
    const curCh = toc.find(c => c.id === actCh);
    const navBase = { position: 'fixed', zIndex: 21, overflowY: 'auto', fontFamily: "'Noto Serif TC',serif", background: 'var(--color-neutral-100)', boxSizing: 'border-box' };
    const tocNavStyle = wide
      ? { ...navBase, top: '28px', left: 'max(12px, calc(50% - 360px - 268px))', width: '240px', maxHeight: 'calc(100vh - 56px)', padding: '14px 16px', border: '1px solid var(--color-divider)', boxShadow: 'var(--shadow-sm)' }
      : { ...navBase, top: 0, right: 0, bottom: 0, width: 'min(300px, 86vw)', padding: '18px 18px', borderLeft: '1px solid var(--color-divider)', boxShadow: 'var(--shadow-lg)' };
    return {
      toc: tocList,
      tocVisible: showToc && (wide || tocOpen),
      tocNarrow: !wide,
      tocNarrowClosed: showToc && !wide && !tocOpen,
      tocCur: curCh ? (curCh.num === '·' ? curCh.label : '第 ' + curCh.num + ' 章') : '封面',
      tocNavStyle,
      tocOpen: () => this.setState({ tocOpen: true }),
      tocClose: () => this.setState({ tocOpen: false }),
      showNotes: this.props.showNotes ?? true,
      showSources: this.props.showSources ?? true,
      ...this.bfsVals(),
      ...this.wnVals(),
      ...this.exerciseVals()
    };
  }
  exerciseVals() {
    const all = this.props.showAnswers ?? false;
    const out = {};
    for (let i = 1; i <= 16; i++) {
      const open = all || !!this.state.ans[i];
      out['ans' + i] = open;
      out['lab' + i] = open ? '收起解答' : '看解答';
      out['tog' + i] = () => this.setState(s => ({ ans: { ...s.ans, [i]: !(all || s.ans[i]) } }));
    }
    return out;
  }
}

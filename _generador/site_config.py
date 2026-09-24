# -*- coding: utf-8 -*-
"""Configurador 3D a pantalla completa (usa el mismo visor que la página de carpas)."""
from site_parts import *

CSS = '''
    html, body { height: 100%; }
    body { display: flex; flex-direction: column; overflow: hidden; background: var(--paper); }
    .cfg-bar { flex: none; height: 4rem; display: flex; align-items: center; gap: 1.25rem; padding-inline: var(--gutter); background: var(--card); border-bottom: 1px solid var(--line); }
    .cfg-bar .nav-logo img { height: 1.55rem; }
    .cfg-sep { width: 1px; height: 1.6rem; background: var(--line); }
    .cfg-title { font-size: .95rem; font-weight: 500; line-height: 1.25; }
    .cfg-title small { display: block; font-family: var(--mono); font-size: .64rem; letter-spacing: .06em; text-transform: uppercase; font-weight: 400; color: var(--muted); }
    .cfg-right { margin-left: auto; display: flex; align-items: center; gap: 1rem; }
    .cfg-back { display: inline-flex; align-items: center; gap: .45rem; font-size: .9rem; font-weight: 500; color: var(--ink-2); }
    .cfg-back:hover { color: var(--ink); }
    .cfg-back svg { width: 1rem; height: 1rem; }
    .cfg-main { flex: 1; display: flex; min-height: 0; }
    .cfg-stage { flex: 1; position: relative; min-width: 0; border-radius: 0; aspect-ratio: auto; margin: 0; }
    .ui-section .ctrl-label { margin-bottom: .8rem; }
    .ui-section .toggle-row { padding: 0; border: 0; background: none; }
    #ui { width: 25rem; flex: none; background: var(--card); border-left: 1px solid var(--line); display: flex; flex-direction: column; min-height: 0; }
    .ui-scroll { flex: 1; overflow-y: auto; }
    .ui-head { padding: 1.5rem 1.6rem 1.25rem; border-bottom: 1px solid var(--line); }
    .ui-head .eyebrow { margin-bottom: .2rem; }
    .ui-head h1 { font-size: 2.4rem; font-weight: 500; letter-spacing: -.04em; line-height: 1; }
    .ui-head p { font-size: .9rem; color: var(--ink-2); margin-top: .4rem; }
    .ui-section { padding: 1.25rem 1.6rem; border-bottom: 1px solid var(--line); }
    .ui-foot { flex: none; padding: 1.25rem 1.6rem 1.5rem; border-top: 1px solid var(--line); background: var(--card); }
    .price-label { font-family: var(--mono); font-size: .66rem; letter-spacing: .06em; text-transform: uppercase; color: var(--muted); }
    .price-val { font-size: 2.2rem; font-weight: 500; letter-spacing: -.04em; line-height: 1.1; margin-top: .15rem; font-variant-numeric: tabular-nums; }
    .price-note { font-size: .8rem; color: var(--muted); margin-top: .25rem; }
    .cfg-summary { font-size: .85rem; color: var(--ink-2); margin-top: .8rem; }
    .quote-btn { width: 100%; margin-top: 1rem; }
    #ui .sides { grid-template-columns: 1fr; }
    #ui .side-field { display: grid; grid-template-columns: 5.5rem 1fr; align-items: center; gap: .6rem; }
    #ui .side-field label { margin: 0; }
    @media (max-width: 860px) {
      body { overflow: auto; height: auto; }
      .cfg-main { flex-direction: column; }
      .cfg-stage { height: 60vh; flex: none; }
      #ui { width: 100%; border-left: 0; border-top: 1px solid var(--line); }
      .ui-scroll { overflow: visible; }
      .ui-foot { position: sticky; bottom: 0; box-shadow: 0 -12px 30px -20px rgba(15,24,32,.35); }
      .cfg-title small, .cfg-sep, .cfg-back span, .cfg-right .lang { display: none; }
    }
'''

JS = r'''
  <script>
  (function () {
    const T = k => (window.OK_I18N ? OK_I18N.t(k) : k);
    const COLORS = [
      { id: 'azul', hex: '#1B4A8C' }, { id: 'verde', hex: '#006A50' }, { id: 'menta', hex: '#74C9B0' },
      { id: 'lima', hex: '#D2DB6A' }, { id: 'amarillo', hex: '#F2C106' }, { id: 'naranja', hex: '#F17201' },
      { id: 'rojo', hex: '#B3372A' }, { id: 'malva', hex: '#9A6B6F' }, { id: 'gris', hex: '#7E807B' },
      { id: 'crema', hex: '#D8CFB8' }, { id: 'blanco', hex: '#F4F4F2' }, { id: 'negro', hex: '#1E1F21' },
    ];
    const SIDES = ['back', 'left', 'right', 'front'];
    const TYPES = ['', 'liso', 'ventana', 'puerta', 'medio'];
    const TYPE3D = { liso: 'lisa', ventana: 'ventana', puerta: 'puerta', medio: 'medio' };
    // Precio base del configurador original; paredes de 3 m según la tarifa de complementos.
    // La media pared y la visera no tienen precio publicado: se piden a consulta.
    const BASE = 890;
    const PRICE = { liso: 106, ventana: 202, puerta: 214, medio: null };

    const p = new URLSearchParams(location.search);
    const state = {
      color: COLORS.some(c => c.id === p.get('color')) ? p.get('color') : 'azul',
      walls: {}, awning: p.get('awning') === '1'
    };
    SIDES.forEach(s => { state.walls[s] = TYPES.includes(p.get(s)) ? p.get(s) : ''; });

    const hexOf = id => COLORS.find(c => c.id === id).hex;
    const walls3d = () => { const o = {}; SIDES.forEach(s => { if (state.walls[s]) o[s] = TYPE3D[state.walls[s]]; }); return o; };
    const stage = document.getElementById('stage');
    const visor = window.OkatentVisor ? OkatentVisor(stage, { color: hexOf(state.color), walls: walls3d(), awning: state.awning, camera: [6.2, 3.1, 7.2] }) : {};
    document.getElementById('stage-reset').addEventListener('click', () => visor.resetView && visor.resetView());

    const eur = n => n.toLocaleString('es-ES') + ' €';
    const swatches = document.getElementById('swatches');
    COLORS.forEach(c => {
      const b = document.createElement('button');
      b.type = 'button'; b.className = 'swatch'; b.style.background = c.hex; b.dataset.color = c.id;
      b.addEventListener('click', () => { state.color = c.id; visor.setColor && visor.setColor(c.hex); render(); });
      swatches.appendChild(b);
    });

    const selects = SIDES.map(s => document.getElementById('side-' + s));
    selects.forEach(sel => sel.addEventListener('change', () => { state.walls[sel.dataset.side] = sel.value; visor.setWalls && visor.setWalls(walls3d()); render(); }));
    function fillSelects() {
      selects.forEach(sel => {
        sel.innerHTML = TYPES.map(tp => {
          if (!tp) return `<option value="">${T('vw.nowall')}</option>`;
          const extra = PRICE[tp] ? ` (+${eur(PRICE[tp])})` : '';
          return `<option value="${tp}">${T('vw.' + tp)}${extra}</option>`;
        }).join('');
        sel.value = state.walls[sel.dataset.side];
      });
    }

    const awning = document.getElementById('awning');
    awning.setAttribute('aria-checked', state.awning);
    awning.addEventListener('click', () => { state.awning = !state.awning; awning.setAttribute('aria-checked', state.awning); visor.setAwning && visor.setAwning(state.awning); render(); });

    function render() {
      swatches.querySelectorAll('.swatch').forEach(b => {
        b.setAttribute('aria-pressed', b.dataset.color === state.color);
        b.setAttribute('aria-label', T('c.' + b.dataset.color)); b.title = T('c.' + b.dataset.color);
      });
      document.getElementById('color-name').textContent = T('c.' + state.color);
      let total = BASE, ask = state.awning;
      SIDES.forEach(s => { const tp = state.walls[s]; if (!tp) return; if (PRICE[tp]) total += PRICE[tp]; else ask = true; });
      document.getElementById('price-val').textContent = `${T('cfg.from')} ${eur(total)}${ask ? ' +' : ''}`;
      const parts = SIDES.filter(s => state.walls[s]).map(s => `${T('vw.side.' + s).toLowerCase()}: ${T('vw.' + state.walls[s]).toLowerCase()}`);
      let text = `Cebú 3×3 · ${T('c.' + state.color)} · ${parts.length ? parts.join(', ') : T('vw.sum.none')}`;
      if (state.awning) text += ' · ' + T('vw.awning').toLowerCase();
      document.getElementById('cfg-summary').textContent = text;
      const q = new URLSearchParams({ model: 'Cebú', size: '3×3 m', color: state.color, config: text });
      document.getElementById('quote-btn').href = 'okatent-contacto.html?' + q.toString() + '#formulario';
    }
    fillSelects(); render();
    document.addEventListener('okatent:lang', () => { fillSelects(); render(); });
  })();
  </script>
'''

def page_configurador():
    h = head('Configurador 3D de la carpa Cebú | OKATENT', 'Configura en 3D tu carpa plegable Okatent Cebú 3×3: paredes, visera y color de la lona, y pide presupuesto.', inline_css=CSS)
    side = lambda s, k, l: f'<div class="side-field"><label for="side-{s}" data-i18n="{k}">{l}</label><select class="select" id="side-{s}" data-side="{s}"></select></div>'
    body = f'''
  <header class="cfg-bar">
    <a href="okatent-carpas.html" class="nav-logo" aria-label="OKATENT"><img src="imgs/logo-okatent.png" alt="OKATENT" width="250" height="60"></a>
    <span class="cfg-sep"></span>
    <div class="cfg-title"><span data-i18n="nav.config">Configurador 3D</span><small data-i18n="cfg.sub">Carpa plegable Cebú 3×3</small></div>
    <div class="cfg-right">
      <select class="lang" aria-label="Idioma" data-lang-select>{LANG_OPTIONS}</select>
      <a href="okatent-carpas-plegables.html" class="cfg-back"><svg viewBox="0 0 20 20" fill="none" stroke="currentColor" stroke-width="1.8"><path d="M16 10H4M9 5l-5 5 5 5"/></svg><span data-i18n="cfg.back">Volver a la web</span></a>
    </div>
  </header>

  <div class="cfg-main">
    <div class="stage3d cfg-stage" id="stage" role="img" aria-label="Carpa Cebú 3×3 en 3D">
      <div class="stage3d-loading"><span data-i18n="vw.loading">Cargando modelo 3D…</span></div>
      <div class="stage3d-bar">
        <span class="stage3d-hint">{DRAG}<span data-i18n="cfg.hint">Arrastra para girar · rueda o dos dedos para acercar</span></span>
        <button class="stage3d-btn" id="stage-reset" type="button">{RESET}<span data-i18n="vw.reset">Centrar</span></button>
      </div>
    </div>

    <aside id="ui">
      <div class="ui-scroll">
        <div class="ui-head">
          <span class="eyebrow" data-i18n="cebu.tag">Gama profesional</span>
          <h1>Cebú 3×3</h1>
          <p data-i18n="cfg.p">Elige paredes, visera y color, y pide tu presupuesto.</p>
        </div>
        <div class="ui-section">
          <div class="ctrl-label"><span data-i18n="vw.walls">Paredes</span></div>
          <div class="sides">
            {side('back', 'vw.side.back', 'Fondo')}
            {side('left', 'vw.side.left', 'Izquierda')}
            {side('right', 'vw.side.right', 'Derecha')}
            {side('front', 'vw.side.front', 'Frente')}
          </div>
        </div>
        <div class="ui-section">
          <div class="toggle-row"><span><span data-i18n="vw.awning">Visera frontal</span><small data-i18n="cfg.ask">Precio a consultar</small></span><button class="toggle" id="awning" type="button" role="switch" aria-checked="false" aria-label="Visera frontal" data-i18n-aria="vw.awning"></button></div>
        </div>
        <div class="ui-section">
          <div class="ctrl-label"><span data-i18n="vw.color">Color de la lona</span><em id="color-name">Azul</em></div>
          <div class="swatches" id="swatches"></div>
          <p class="ctrl-note" data-i18n="vw.colornote">También en lona transparente.</p>
        </div>
      </div>
      <div class="ui-foot">
        <div class="price-label" data-i18n="cfg.price">Precio orientativo</div>
        <div class="price-val" id="price-val">Desde 890 €</div>
        <div class="price-note" data-i18n="cfg.note">IVA no incluido · presupuesto personalizado en 48 h laborables</div>
        <p class="cfg-summary" id="cfg-summary"></p>
        <a class="btn btn-primary quote-btn" id="quote-btn" href="okatent-contacto.html"><span data-i18n="vw.cta1">Pedir presupuesto de esta carpa</span>{ARROW}</a>
      </div>
    </aside>
  </div>
'''
    return h + body + scripts('configurador', after=THREE_LIBS + JS)

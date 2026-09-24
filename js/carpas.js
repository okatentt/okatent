/* OKATENT — página de carpas: visor 3D con colores y paredes, y tabla de medidas */
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

  const SIZES = [
    ['2×2', 4, 22, 7], ['2×3', 6, 23, 9], ['2×4', 8, 24, 10], ['3×3', 9, 24, 11], ['3×4,5', 13.5, 33, 15],
    ['3×6', 18, 44, 19], ['4×4', 16, 33, 17], ['4×6', 24, 42, 22], ['4×8', 32, 56, 32], ['5×5', 25, 41, 25],
  ];
  const rows = document.getElementById('size-rows');
  if (rows) rows.innerHTML = SIZES.map(([l, a, s, c]) => `<tr><td>${l} m</td><td>${String(a).replace('.', ',')} m²</td><td>${s}</td><td>${c}</td></tr>`).join('');

  const stage = document.getElementById('stage');
  if (!stage) return;

  const state = { color: 'azul', walls: { back: 'liso', left: '', right: '', front: '' }, awning: false };
  const hexOf = id => COLORS.find(c => c.id === id).hex;
  const walls3d = () => { const o = {}; SIDES.forEach(s => { if (state.walls[s]) o[s] = TYPE3D[state.walls[s]]; }); return o; };

  const visor = window.OkatentVisor ? OkatentVisor(stage, { color: hexOf(state.color), walls: walls3d(), camera: [6.3, 3.3, 7.4] }) : {};
  document.getElementById('stage-reset').addEventListener('click', () => visor.resetView && visor.resetView());

  // colores
  const swatches = document.getElementById('swatches');
  COLORS.forEach(c => {
    const b = document.createElement('button');
    b.type = 'button'; b.className = 'swatch'; b.style.background = c.hex; b.dataset.color = c.id;
    b.addEventListener('click', () => { state.color = c.id; visor.setColor && visor.setColor(c.hex); render(); });
    swatches.appendChild(b);
  });

  // paredes por lado
  const selects = SIDES.map(side => document.getElementById('side-' + side));
  selects.forEach(sel => sel.addEventListener('change', () => {
    state.walls[sel.dataset.side] = sel.value;
    visor.setWalls && visor.setWalls(walls3d());
    render();
  }));
  function fillSelects() {
    selects.forEach(sel => {
      const side = sel.dataset.side;
      sel.innerHTML = TYPES.map(tp => `<option value="${tp}">${tp ? T('vw.' + tp) : T('vw.nowall')}</option>`).join('');
      sel.value = state.walls[side];
    });
  }

  // visera
  const awning = document.getElementById('awning');
  awning.addEventListener('click', () => {
    state.awning = !state.awning;
    awning.setAttribute('aria-checked', state.awning);
    visor.setAwning && visor.setAwning(state.awning);
    render();
  });

  function summary() {
    const parts = SIDES.filter(s => state.walls[s]).map(s => `${T('vw.side.' + s).toLowerCase()}: ${T('vw.' + state.walls[s]).toLowerCase()}`);
    let txt = `Cebú 3×3 · ${T('c.' + state.color)} · ${parts.length ? parts.join(', ') : T('vw.sum.none')}`;
    if (state.awning) txt += ' · ' + T('vw.awning').toLowerCase();
    return txt;
  }

  function render() {
    swatches.querySelectorAll('.swatch').forEach(b => {
      b.setAttribute('aria-pressed', b.dataset.color === state.color);
      b.setAttribute('aria-label', T('c.' + b.dataset.color));
      b.title = T('c.' + b.dataset.color);
    });
    document.getElementById('color-name').textContent = T('c.' + state.color);
    const text = summary();
    document.getElementById('viewer-summary').textContent = text;
    stage.setAttribute('aria-label', text);
    const q = new URLSearchParams({ model: 'Cebú', size: '3×3 m', color: state.color, config: text });
    document.getElementById('viewer-quote').href = 'okatent-contacto.html?' + q.toString() + '#formulario';
    const f = new URLSearchParams({ color: state.color });
    SIDES.forEach(s => { if (state.walls[s]) f.set(s, state.walls[s]); });
    if (state.awning) f.set('awning', '1');
    document.getElementById('viewer-full').href = 'okatent-configurador.html?' + f.toString();
  }

  fillSelects();
  render();
  document.addEventListener('okatent:lang', () => { fillSelects(); render(); });
})();

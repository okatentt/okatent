/* OKATENT — inicio: sala 3D con la Cebú (se carga al acercarse a la sección) */
(function () {
  const stage = document.getElementById('home-stage');
  if (!stage) return;
  const T = k => (window.OK_I18N ? OK_I18N.t(k) : k);

  const COLORS = [
    { id: 'azul', hex: '#1B4A8C' }, { id: 'verde', hex: '#006A50' }, { id: 'menta', hex: '#74C9B0' },
    { id: 'lima', hex: '#D2DB6A' }, { id: 'amarillo', hex: '#F2C106' }, { id: 'naranja', hex: '#F17201' },
    { id: 'rojo', hex: '#B3372A' }, { id: 'malva', hex: '#9A6B6F' }, { id: 'gris', hex: '#7E807B' },
    { id: 'crema', hex: '#D8CFB8' }, { id: 'blanco', hex: '#F4F4F2' }, { id: 'negro', hex: '#1E1F21' },
  ];
  let color = 'azul';
  let visor = null;
  const hexOf = id => COLORS.find(c => c.id === id).hex;

  const swatches = document.getElementById('home-swatches');
  const label = document.getElementById('home-color');
  const full = document.getElementById('home-full');

  COLORS.forEach(c => {
    const b = document.createElement('button');
    b.type = 'button'; b.className = 'swatch'; b.style.background = c.hex; b.dataset.color = c.id;
    b.addEventListener('click', () => { color = c.id; if (visor && visor.setColor) visor.setColor(c.hex); render(); });
    swatches.appendChild(b);
  });

  function render() {
    swatches.querySelectorAll('.swatch').forEach(b => {
      b.setAttribute('aria-pressed', b.dataset.color === color);
      b.setAttribute('aria-label', T('c.' + b.dataset.color));
      b.title = T('c.' + b.dataset.color);
    });
    label.textContent = T('c.' + color);
    full.href = 'okatent-configurador.html?color=' + color + '&back=liso';
  }

  function init() {
    if (visor || !window.OkatentVisor) return;
    visor = OkatentVisor(stage, { color: hexOf(color), walls: { back: 'lisa' }, camera: [6.8, 3.3, 7.8] });
    document.getElementById('home-reset').addEventListener('click', () => visor.resetView && visor.resetView());
  }

  render();
  document.addEventListener('okatent:lang', render);

  if ('IntersectionObserver' in window) {
    const io = new IntersectionObserver(entries => {
      if (entries.some(e => e.isIntersecting)) { init(); io.disconnect(); }
    }, { rootMargin: '400px 0px' });
    io.observe(stage);
  } else {
    init();
  }
})();

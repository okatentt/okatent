/* OKATENT — comportamiento común: menú móvil, año del pie, aparición al hacer scroll, subnavegación y efectos */
(function () {
  const reduce = window.matchMedia && matchMedia('(prefers-reduced-motion: reduce)').matches;
  if (!reduce) document.documentElement.classList.add('fx');

  const nav = document.getElementById('nav');
  const burger = document.getElementById('burger');
  if (nav && burger) {
    const close = () => { nav.classList.remove('open'); burger.setAttribute('aria-expanded', 'false'); document.body.style.overflow = ''; };
    burger.addEventListener('click', () => {
      nav.style.setProperty('--menu-top', nav.getBoundingClientRect().bottom + 'px');
      const open = nav.classList.toggle('open');
      burger.setAttribute('aria-expanded', open);
      document.body.style.overflow = open ? 'hidden' : '';
    });
    document.querySelectorAll('#mobile-menu a').forEach(a => a.addEventListener('click', close));
    window.addEventListener('resize', () => { if (window.innerWidth > 1080) close(); });
  }

  const year = document.getElementById('year');
  if (year) year.textContent = new Date().getFullYear();

  // ---------- aparición al hacer scroll, escalonada dentro de cada rejilla ----------
  const rvEls = document.querySelectorAll('.rv');
  rvEls.forEach(el => {
    const sibs = [...el.parentElement.children].filter(c => c.classList.contains('rv'));
    if (sibs.length > 1 && !reduce) el.style.transitionDelay = Math.min(sibs.indexOf(el), 6) * 90 + 'ms';
  });
  if ('IntersectionObserver' in window) {
    const io = new IntersectionObserver(entries => {
      entries.forEach(e => {
        if (!e.isIntersecting) return;
        e.target.classList.add('in');
        io.unobserve(e.target);
        // el retraso solo sirve para la entrada; luego no debe frenar los hover
        setTimeout(() => { e.target.style.transitionDelay = ''; }, 1800);
      });
    }, { threshold: .12, rootMargin: '0px 0px -6% 0px' });
    rvEls.forEach(el => io.observe(el));
  } else {
    rvEls.forEach(el => el.classList.add('in'));
  }

  // Subnavegación: marca la sección visible
  const sublinks = [...document.querySelectorAll('.subnav a[href^="#"]')];
  if (sublinks.length && 'IntersectionObserver' in window) {
    const map = new Map(sublinks.map(a => [document.querySelector(a.getAttribute('href')), a]));
    const so = new IntersectionObserver(entries => {
      entries.forEach(e => {
        if (e.isIntersecting) {
          sublinks.forEach(a => a.classList.remove('active'));
          const a = map.get(e.target);
          if (a) { a.classList.add('active'); const box = a.parentElement; if (box.scrollWidth > box.clientWidth) box.scrollTo({ left: a.offsetLeft - box.clientWidth / 2 + a.clientWidth / 2, behavior: 'smooth' }); }
        }
      });
    }, { rootMargin: '-40% 0px -55% 0px' });
    map.forEach((a, sec) => sec && so.observe(sec));
  }

  if (reduce || !('IntersectionObserver' in window)) return;

  /* =========================================================
     EFECTOS
     1. Titulares que se escriben letra a letra con cursor
     2. Subtítulos que suben palabra a palabra
     3. Frase grande que se ilumina al hacer scroll
     4. Números que cuentan
     5. Fotos con paralaje y barra de progreso en el menú
     ========================================================= */
  const TYPE_SEL = '.hero h1 > [data-i18n]:not(.kicker), .page-head h1, .h2, .cta-in h2';
  const WORD_SEL = '.h3, .model-title h3, .case-row h2, .compare h3, .footer-claim > span, .quote-card p';
  const LIGHT_SEL = '.statement';

  // Parte el texto de un elemento (respetando <span>, <b>, <br>) en palabras y, si hace falta, letras
  function split(el, mode) {
    if (el.querySelector('[data-i18n]') && !el.hasAttribute('data-i18n')) return false;
    if (el.querySelector('.ch, .wi, .sw')) return true;
    el._okSrc = el.innerHTML;
    let n = 0;
    const walk = node => {
      [...node.childNodes].forEach(child => {
        if (child.nodeType === 3) {
          const frag = document.createDocumentFragment();
          child.textContent.split(/(\s+)/).forEach(part => {
            if (!part) return;
            if (/^\s+$/.test(part)) { frag.appendChild(document.createTextNode(' ')); return; }
            if (mode === 'type') {
              const w = document.createElement('span'); w.className = 'tw';
              for (const c of part) { const s = document.createElement('span'); s.className = 'ch'; s.textContent = c; w.appendChild(s); }
              frag.appendChild(w);
            } else if (mode === 'word') {
              const w = document.createElement('span'); w.className = 'w';
              const i = document.createElement('span'); i.className = 'wi'; i.style.setProperty('--i', n++); i.textContent = part;
              w.appendChild(i); frag.appendChild(w);
            } else {
              const s = document.createElement('span'); s.className = 'sw'; s.textContent = part; frag.appendChild(s);
            }
          });
          child.replaceWith(frag);
        } else if (child.nodeType === 1 && child.tagName !== 'BR') {
          walk(child);
        }
      });
    };
    walk(el);
    const heading = el.closest('h1, h2, h3');
    if (heading) heading.setAttribute('aria-label', [...heading.childNodes].map(n => n.textContent + (n.classList && n.classList.contains('kicker') ? ' · ' : '')).join('').replace(/\s+/g, ' ').trim());
    el.classList.add('fx-split');
    return true;
  }

  // Escritura con cursor. Devuelve una promesa que se resuelve al terminar.
  function typeOut(el, instant) {
    const chars = [...el.querySelectorAll('.ch')];
    if (instant) { chars.forEach(c => c.classList.add('on')); return Promise.resolve(); }
    el.dataset.fx = 'done';
    const caret = document.createElement('span');
    caret.className = 'caret typing'; caret.setAttribute('aria-hidden', 'true');
    const base = Math.max(16, Math.min(52, 1350 / Math.max(chars.length, 1)));
    let i = 0;
    return new Promise(resolve => {
      (function step() {
        if (i >= chars.length) {
          caret.classList.remove('typing');
          setTimeout(() => { caret.classList.add('gone'); setTimeout(() => caret.remove(), 500); }, 1600);
          resolve();
          return;
        }
        const c = chars[i++];
        c.classList.add('on');
        c.after(caret);
        const pause = /[.,;:!?¿¡»]/.test(c.textContent) ? 170 : 0;
        const next = chars[i];
        const gap = next && c.parentElement !== next.parentElement ? base * .9 : 0;
        setTimeout(step, base * (.65 + Math.random() * .7) + pause + gap);
      })();
    });
  }

  const typeTargets = () => [...document.querySelectorAll(TYPE_SEL)];
  const wordTargets = () => [...document.querySelectorAll(WORD_SEL)];
  const lightTargets = () => [...document.querySelectorAll(LIGHT_SEL)];

  const typeIO = new IntersectionObserver(entries => {
    entries.forEach(e => {
      if (!e.isIntersecting) return;
      typeIO.unobserve(e.target);
      const heroSpan = e.target.closest('.hero-in');
      const p = typeOut(e.target, e.target.dataset.fx === 'done');
      if (heroSpan) p.then(() => { heroSpan.classList.add('typed'); heroSpan.querySelectorAll('.hero-stats b').forEach(countUp); });
    });
  }, { threshold: .55, rootMargin: '0px 0px -8% 0px' });

  const wordIO = new IntersectionObserver(entries => {
    entries.forEach(e => { if (e.isIntersecting) { e.target.classList.add('fx-in'); e.target.dataset.fx = 'done'; wordIO.unobserve(e.target); } });
  }, { threshold: .4 });

  function prepare(initial) {
    typeTargets().forEach(el => {
      if (el.querySelector('.ch')) return;
      if (!split(el, 'type')) return;
      if (el.dataset.fx === 'done') typeOut(el, true);
      else typeIO.observe(el);
    });
    wordTargets().forEach(el => {
      if (el.querySelector('.wi')) return;
      if (!split(el, 'word')) return;
      if (el.dataset.fx === 'done') el.classList.add('fx-in');
      else wordIO.observe(el);
    });
    lightTargets().forEach(el => { if (!el.querySelector('.sw')) split(el, 'light'); });
    if (!initial) onScroll();
  }

  // El texto ya está en el HTML: se parte antes de pintar para que no parpadee
  prepare(true);
  // Al cambiar de idioma el motor de traducción repone el texto: se vuelve a partir (sin repetir la animación)
  document.addEventListener('okatent:lang', () => prepare(false));

  // Entrada del hero
  const hero = document.querySelector('.hero-in');
  if (hero) requestAnimationFrame(() => requestAnimationFrame(() => hero.classList.add('loaded')));

  // ---------- números que cuentan ----------
  function countUp(b) {
    if (b.dataset.counted) return;
    const m = (b.dataset.final || b.textContent).match(/^([+]?)(\d+)(\D*)$/);
    if (!m) return;
    b.dataset.counted = '1';
    const [, pre, num, suf] = m;
    const target = +num, t0 = performance.now(), dur = 1400;
    (function frame(now) {
      const p = Math.min(1, (now - t0) / dur);
      const e = 1 - Math.pow(1 - p, 3);
      b.textContent = pre + Math.round(target * e) + suf;
      if (p < 1) requestAnimationFrame(frame);
    })(t0);
  }
  const counters = [...document.querySelectorAll('.stat b, .case-metric b')].filter(b => /^[+]?\d+\D*$/.test(b.textContent));
  // empiezan en 0 para que no se vea el número final antes de contar
  [...counters, ...document.querySelectorAll('.hero-stats b')].forEach(b => { if (/^[+]?\d+\D*$/.test(b.textContent)) { b.dataset.final = b.textContent; b.textContent = b.textContent.replace(/\d+/, '0'); } });
  const countIO = new IntersectionObserver(entries => {
    entries.forEach(e => { if (e.isIntersecting) { countUp(e.target); countIO.unobserve(e.target); } });
  }, { threshold: .6 });
  counters.forEach(b => countIO.observe(b));

  // ---------- paralaje, frase que se ilumina y barra de progreso ----------
  const pxImgs = [...document.querySelectorAll('.hero-img img, .ph-media img, .cta-in > img, .feature figure img, .photo-marquee > img')];
  pxImgs.forEach(img => img.classList.add('px'));

  let bar = null;
  if (nav) {
    bar = document.createElement('span');
    bar.className = 'nav-progress'; bar.setAttribute('aria-hidden', 'true');
    nav.querySelector('.wrap').appendChild(bar);
  }

  let ticking = false;
  function onScroll() {
    const vh = window.innerHeight;
    pxImgs.forEach(img => {
      const r = img.parentElement.getBoundingClientRect();
      if (r.bottom < -100 || r.top > vh + 100) return;
      const p = (r.top + r.height / 2 - vh / 2) / (vh / 2 + r.height / 2);
      img.style.setProperty('--py', (p * -4.5).toFixed(2) + '%');
    });
    lightTargets().forEach(el => {
      const r = el.getBoundingClientRect();
      if (r.bottom < 0 || r.top > vh) return;
      const words = el.querySelectorAll('.sw');
      const p = Math.min(1, Math.max(0, (vh * .88 - r.top) / (r.height + vh * .38)));
      const lit = Math.round(p * words.length);
      words.forEach((w, i) => w.classList.toggle('lit', i < lit));
    });
    if (bar) {
      const max = document.documentElement.scrollHeight - vh;
      bar.style.setProperty('--p', max > 0 ? (window.scrollY / max).toFixed(4) : 0);
      nav.classList.toggle('scrolled', window.scrollY > 24);
    }
    ticking = false;
  }
  window.addEventListener('scroll', () => { if (!ticking) { ticking = true; requestAnimationFrame(onScroll); } }, { passive: true });
  window.addEventListener('resize', onScroll);
  onScroll();
})();

/* OKATENT — idiomas.
   El español se lee del propio HTML; el resto sale de los diccionarios de js/i18n/.
   Uso: data-i18n="clave" (contenido), data-i18n-ph="clave" (placeholder), data-i18n-aria="clave" (aria-label). */
(function () {
  const LANGS = ['ES', 'CA', 'EN', 'FR', 'IT'];
  const dict = { ES: {}, CA: {}, EN: {}, FR: {}, IT: {} };
  const esHTML = {}, esPH = {}, esAria = {};
  let lang = 'ES';
  let esTitle = document.title;

  function t(key) {
    if (dict[lang] && key in dict[lang]) return dict[lang][key];
    if (key in dict.ES) return dict.ES[key];
    if (key in esHTML) return esHTML[key];
    if (key in esPH) return esPH[key];
    if (key in esAria) return esAria[key];
    return key;
  }

  function harvest(root) {
    // _okSrc: texto original de un titular que okatent.js ha partido en letras para animarlo
    root.querySelectorAll('[data-i18n]').forEach(el => { const k = el.dataset.i18n; if (!(k in esHTML)) esHTML[k] = el._okSrc != null ? el._okSrc : el.innerHTML; });
    root.querySelectorAll('[data-i18n-ph]').forEach(el => { const k = el.dataset.i18nPh; if (!(k in esPH)) esPH[k] = el.getAttribute('placeholder'); });
    root.querySelectorAll('[data-i18n-aria]').forEach(el => { const k = el.dataset.i18nAria; if (!(k in esAria)) esAria[k] = el.getAttribute('aria-label'); });
  }

  function apply(root) {
    root.querySelectorAll('[data-i18n]').forEach(el => {
      const k = el.dataset.i18n;
      const v = lang === 'ES' ? (k in dict.ES ? dict.ES[k] : esHTML[k]) : (dict[lang][k] ?? esHTML[k]);
      const cur = el._okSrc != null ? el._okSrc : el.innerHTML;
      if (v != null && cur !== v) { el.innerHTML = v; el._okSrc = null; }
    });
    root.querySelectorAll('[data-i18n-ph]').forEach(el => el.setAttribute('placeholder', t(el.dataset.i18nPh)));
    root.querySelectorAll('[data-i18n-aria]').forEach(el => el.setAttribute('aria-label', t(el.dataset.i18nAria)));
  }

  function setLang(next) {
    lang = LANGS.includes(next) ? next : 'ES';
    document.documentElement.lang = lang.toLowerCase();
    try { localStorage.setItem('okatent_lang', lang); } catch (e) {}
    apply(document);
    document.querySelectorAll('[data-lang-select]').forEach(s => { s.value = lang; });
    document.title = (lang !== 'ES' && dict[lang].title) ? dict[lang].title : esTitle;
    document.dispatchEvent(new CustomEvent('okatent:lang', { detail: lang }));
  }

  function start() {
    harvest(document);
    document.querySelectorAll('[data-lang-select]').forEach(s => s.addEventListener('change', () => setLang(s.value)));
    let initial = '';
    try { initial = localStorage.getItem('okatent_lang') || ''; } catch (e) {}
    if (!initial) {
      const nl = (navigator.language || '').toLowerCase();
      initial = nl.startsWith('ca') ? 'CA' : nl.startsWith('fr') ? 'FR' : nl.startsWith('it') ? 'IT' : nl.startsWith('en') ? 'EN' : 'ES';
    }
    setLang(initial);
  }

  window.OK_I18N = {
    add(obj) { for (const L in obj) Object.assign(dict[L] = dict[L] || {}, obj[L]); },
    t,
    set: setLang,
    get lang() { return lang; },
    // para contenido creado después de cargar (se registra su español y se traduce)
    refresh(root) { harvest(root); apply(root); }
  };

  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', start);
  else start();
})();

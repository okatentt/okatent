/* OKATENT — formulario de presupuesto (se envía por correo o por WhatsApp) */
(function () {
  const T = k => (window.OK_I18N ? OK_I18N.t(k) : k);
  const SIZES = ['2×2', '2×3', '2×4', '3×3', '3×4,5', '3×6', '4×4', '4×6', '4×8', '5×5'];
  const COLORS = ['blanco', 'crema', 'gris', 'amarillo', 'lima', 'naranja', 'rojo', 'malva', 'menta', 'verde', 'azul', 'negro', 'transparente'];

  const $ = id => document.getElementById(id);
  const form = $('quote-form');
  if (!form) return;
  const fSize = $('f-size'), fColor = $('f-color'), fModel = $('f-model'), fUse = $('f-use'), fQty = $('f-qty'), fLogo = $('f-logo'), fMsg = $('f-msg');
  const msg = $('form-msg'), nameEl = $('f-name'), emailEl = $('f-email');

  SIZES.forEach(s => { const o = document.createElement('option'); o.value = s + ' m'; o.textContent = s + ' m'; fSize.appendChild(o); });
  function buildColors() {
    const prev = fColor.value;
    [...fColor.querySelectorAll('option:not([data-i18n])')].forEach(o => o.remove());
    COLORS.forEach(id => { const o = document.createElement('option'); o.value = id; o.textContent = T('c.' + id); fColor.appendChild(o); });
    fColor.value = prev;
  }
  buildColors();
  document.addEventListener('okatent:lang', buildColors);

  // datos que llegan desde otras páginas
  const p = new URLSearchParams(location.search);
  if (p.get('model') && [...fModel.options].some(o => o.value === p.get('model'))) fModel.value = p.get('model');
  if (p.get('size')) fSize.value = p.get('size');
  if (p.get('color') && COLORS.includes(p.get('color'))) fColor.value = p.get('color');
  if (p.get('use')) fUse.value = p.get('use');
  if (p.get('logo')) fLogo.checked = true;
  if (p.get('config')) fMsg.value = p.get('config');

  function collect() {
    const name = nameEl.value.trim();
    const email = emailEl.value.trim();
    const okEmail = /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email);
    nameEl.classList.toggle('bad', !name);
    emailEl.classList.toggle('bad', !okEmail);
    if (!name || !okEmail) {
      msg.hidden = false; msg.className = 'form-msg err'; msg.textContent = T('f.err');
      (!name ? nameEl : emailEl).focus();
      return null;
    }
    const lines = [
      T('mail.hello'), '',
      `${T('f.use')}: ${fUse.value ? T('use.' + fUse.value) : '—'}`,
      `${T('f.qty')}: ${fQty.value || '—'}`,
      `${T('f.model')}: ${fModel.value === '?' ? T('f.model.any') : fModel.value}`,
      `${T('f.size')}: ${fSize.value || '—'}`,
      `${T('f.color')}: ${fColor.value ? T('c.' + fColor.value) : '—'}`,
      `Logo: ${fLogo.checked ? T('f.yes') : T('f.no')}`,
      '', fMsg.value.trim(), '',
      name, $('f-company').value.trim(), email, $('f-phone').value.trim()
    ].filter((l, i, arr) => !(l === '' && arr[i - 1] === ''));
    return { name, text: lines.join('\n').trim() };
  }

  form.addEventListener('submit', e => {
    e.preventDefault();
    const data = collect();
    if (!data) return;
    const subject = `${T('mail.subject')} · ${data.name}`;
    window.location.href = `mailto:info@okatent.com?subject=${encodeURIComponent(subject)}&body=${encodeURIComponent(data.text)}`;
    msg.hidden = false; msg.className = 'form-msg ok'; msg.textContent = T('f.ok');
  });
  $('f-wa').addEventListener('click', () => {
    const data = collect();
    if (!data) return;
    msg.hidden = true;
    window.open(`https://wa.me/34933231974?text=${encodeURIComponent(data.text)}`, '_blank', 'noopener');
  });
})();

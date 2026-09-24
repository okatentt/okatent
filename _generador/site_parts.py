# -*- coding: utf-8 -*-
"""Piezas comunes de todas las páginas: cabecera, menú, pie, franja de llamada y scripts."""

ARROW = '<svg viewBox="0 0 20 20" fill="none" stroke="currentColor" stroke-width="1.8"><path d="M4 10h12M11 5l5 5-5 5"/></svg>'
CHECK = '<svg viewBox="0 0 20 20" fill="none" stroke="currentColor" stroke-width="2"><path d="M4 10.5l4 4 8-9"/></svg>'
CHEV = '<svg viewBox="0 0 12 12" fill="none" stroke="currentColor" stroke-width="1.6"><path d="M3 4.5l3 3 3-3"/></svg>'
CART = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7"><circle cx="9" cy="20" r="1.3"/><circle cx="18" cy="20" r="1.3"/><path d="M2 3h3l2.4 12.2a2 2 0 0 0 2 1.6h8.4a2 2 0 0 0 2-1.5L21.5 7H6"/></svg>'
DRAG = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6"><path d="M7 12h10M7 12l3-3M7 12l3 3M17 12l-3-3M17 12l-3 3"/></svg>'
RESET = '<svg viewBox="0 0 20 20" fill="none" stroke="currentColor" stroke-width="1.8"><path d="M4 10a6 6 0 1 0 2-4.5M4 4v3h3"/></svg>'
EXPAND = '<svg viewBox="0 0 20 20" fill="none" stroke="currentColor" stroke-width="1.8"><path d="M12 4h4v4M8 16H4v-4M16 4l-5 5M4 16l5-5"/></svg>'
PHONE = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7"><path d="M5 4h4l2 5-2.5 1.5a11 11 0 0 0 5 5L15 13l5 2v4a2 2 0 0 1-2 2A16 16 0 0 1 3 6a2 2 0 0 1 2-2"/></svg>'
CHAT = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7"><path d="M4 20l1.3-4A8 8 0 1 1 8 18.7z"/></svg>'
MAIL = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7"><rect x="3" y="5" width="18" height="14" rx="2"/><path d="M3 7l9 6 9-6"/></svg>'
PIN = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7"><path d="M12 21s-7-6.2-7-11.5A7 7 0 0 1 19 9.5C19 14.8 12 21 12 21z"/><circle cx="12" cy="9.5" r="2.5"/></svg>'
CLOCK = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7"><circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 2"/></svg>'
WA_PATH = 'M17.5 14.4c-.3-.1-1.8-.9-2-1-.3-.1-.5-.1-.7.1-.2.3-.8 1-.9 1.2-.2.2-.3.2-.6.1-.3-.1-1.3-.5-2.4-1.5-.9-.8-1.5-1.8-1.7-2.1-.2-.3 0-.5.1-.6l.4-.5c.2-.2.2-.3.3-.5.1-.2 0-.4 0-.5l-.9-2.2c-.2-.6-.5-.5-.7-.5h-.6c-.2 0-.5.1-.8.4-.3.3-1 1-1 2.5s1.1 2.9 1.2 3.1c.1.2 2.1 3.2 5.1 4.5.7.3 1.3.5 1.7.6.7.2 1.4.2 1.9.1.6-.1 1.8-.7 2-1.4.2-.7.2-1.3.2-1.4-.1-.1-.3-.2-.6-.4zM12 21.8c-1.8 0-3.5-.5-5-1.4l-.4-.2-3.7 1 1-3.6-.2-.4a9.9 9.9 0 1 1 8.3 4.6zM20.5 3.5A11.8 11.8 0 0 0 12 0C5.5 0 .2 5.3.2 11.9c0 2.1.5 4.1 1.6 5.9L.1 24l6.3-1.7a11.9 11.9 0 0 0 5.7 1.4c6.6 0 11.9-5.3 11.9-11.9 0-3.2-1.2-6.2-3.5-8.3z'

FAVICON = "data:image/svg+xml,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 32 32'><rect width='32' height='32' rx='6' fill='%230F1820'/><rect x='9' y='9' width='4' height='14' fill='%23232F5D'/><rect x='14' y='9' width='4' height='14' fill='%230075BE'/><rect x='19' y='9' width='4' height='14' fill='%23ADCCED'/></svg>"

THREE_LIBS = '''  <script src="https://cdn.jsdelivr.net/npm/three@0.128.0/build/three.min.js"></script>
  <script src="https://cdn.jsdelivr.net/npm/three@0.128.0/examples/js/loaders/GLTFLoader.js"></script>
  <script src="https://cdn.jsdelivr.net/npm/three@0.128.0/examples/js/loaders/DRACOLoader.js"></script>
  <script src="https://cdn.jsdelivr.net/npm/three@0.128.0/examples/js/controls/OrbitControls.js"></script>
  <script src="https://cdn.jsdelivr.net/npm/three@0.128.0/examples/js/environments/RoomEnvironment.js"></script>
  <script src="js/visor3d.js"></script>
'''

LANG_OPTIONS = '<option value="ES">ES</option><option value="CA">CA</option><option value="EN">EN</option><option value="FR">FR</option><option value="IT">IT</option>'


def head(title, desc, extra_css='', og_image='imgs/web/hero-montserrat.jpg', inline_css=''):
    css_links = '  <link rel="stylesheet" href="css/okatent.css">\n' + ''.join(f'  <link rel="stylesheet" href="{c}">\n' for c in ([extra_css] if extra_css else []))
    style = f'  <style>\n{inline_css}\n  </style>\n' if inline_css else ''
    return f'''<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{title}</title>
  <meta name="description" content="{desc}">
  <meta property="og:title" content="{title}">
  <meta property="og:description" content="{desc}">
  <meta property="og:image" content="{og_image}">
  <meta property="og:type" content="website">
  <meta name="twitter:card" content="summary_large_image">
  <link rel="icon" type="image/svg+xml" href="{FAVICON}">
  <script>if(!(window.matchMedia&&matchMedia('(prefers-reduced-motion: reduce)').matches))document.documentElement.classList.add('fx')</script>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter+Tight:wght@400;500;600&family=IBM+Plex+Mono:wght@400;500&display=swap" rel="stylesheet">
{css_links}{style}</head>
<body>
'''


def header(active='', cart=False):
    def cur(key):
        return ' aria-current="page"' if key == active else ''
    cart_btn = f'<button class="nav-cart" type="button" onclick="openCart()" aria-label="Pedido" data-i18n-aria="sh.cart.h">{CART}<span class="nav-cart-badge" id="navCartBadge">0</span></button>\n        ' if cart else ''
    return f'''
  <header class="nav" id="nav">
    <div class="wrap">
      <a href="okatent-carpas.html" class="nav-logo" aria-label="OKATENT"><img src="imgs/logo-okatent.png" alt="OKATENT" width="250" height="60"></a>
      <nav class="nav-links" aria-label="Principal">
        <div class="nav-item">
          <a class="nav-link" href="okatent-carpas-plegables.html"{cur('carpas')}><span data-i18n="nav.carpas">Carpas plegables</span>{CHEV}</a>
          <div class="nav-drop">
            <a href="okatent-carpas-plegables.html#modelos"><span data-i18n="nav.modelos">Modelos Cebú y Borneo</span><small data-i18n="nav.modelos.sub">Gama profesional y de iniciación</small></a>
            <a href="okatent-carpas-plegables.html#visor"><span data-i18n="vw.eyebrow">Colores y paredes</span><small data-i18n="nav.visor.sub">Pruébala en 3D</small></a>
            <a href="okatent-carpas-plegables.html#medidas"><span data-i18n="nav.ficha">Medidas y ficha técnica</span><small data-i18n="nav.ficha.sub">Pesos y especificaciones</small></a>
            <a href="okatent-configurador.html"><span data-i18n="nav.config">Configurador 3D</span><small data-i18n="nav.config.sub">Configúrala a pantalla completa</small></a>
          </div>
        </div>
        <div class="nav-item"><a class="nav-link" href="okatent-personalizacion.html"{cur('personal')} data-i18n="nav.personal">Personalización</a></div>
        <div class="nav-item">
          <a class="nav-link" href="okatent-complementos.html"{cur('accesorios')}><span data-i18n="nav.accesorios">Accesorios</span>{CHEV}</a>
          <div class="nav-drop">
            <a href="okatent-complementos.html"><span data-i18n="nav.comp">Complementos</span><small data-i18n="nav.comp.sub">Paredes, pesos y sacos</small></a>
            <a href="okatent-recambios.html"><span data-i18n="nav.rec">Recambios</span><small data-i18n="nav.rec.sub">Cada pieza por separado</small></a>
          </div>
        </div>
        <div class="nav-item"><a class="nav-link" href="okatent-casos.html"{cur('casos')} data-i18n="nav.casos">Casos</a></div>
        <div class="nav-item"><a class="nav-link" href="okatent-empresa.html"{cur('empresa')} data-i18n="nav.empresa">Empresa</a></div>
      </nav>
      <div class="nav-right">
        {cart_btn}<select class="lang" aria-label="Idioma" data-lang-select>{LANG_OPTIONS}</select>
        <a href="okatent-contacto.html" class="btn btn-primary" data-i18n="nav.cta">Pedir presupuesto</a>
        <button class="burger" id="burger" aria-expanded="false" aria-controls="mobile-menu" aria-label="Menú"><span></span></button>
      </div>
    </div>
    <div class="mobile-menu" id="mobile-menu">
      <a href="okatent-carpas-plegables.html" data-i18n="nav.carpas">Carpas plegables</a>
      <div class="sub">
        <a href="okatent-carpas-plegables.html#modelos" data-i18n="nav.modelos">Modelos Cebú y Borneo</a>
        <a href="okatent-carpas-plegables.html#visor" data-i18n="vw.eyebrow">Colores y paredes</a>
        <a href="okatent-carpas-plegables.html#medidas" data-i18n="nav.ficha">Medidas y ficha técnica</a>
      </div>
      <a href="okatent-personalizacion.html" data-i18n="nav.personal">Personalización</a>
      <a href="okatent-complementos.html" data-i18n="nav.comp">Complementos</a>
      <a href="okatent-recambios.html" data-i18n="nav.rec">Recambios</a>
      <a href="okatent-casos.html" data-i18n="nav.casos">Casos</a>
      <a href="okatent-empresa.html" data-i18n="nav.empresa">Empresa</a>
      <a href="okatent-contacto.html" data-i18n="nav.contacto">Contacto</a>
      <select class="lang" aria-label="Idioma" data-lang-select>{LANG_OPTIONS}</select>
      <a href="okatent-contacto.html" class="btn btn-primary" data-i18n="nav.cta">Pedir presupuesto</a>
    </div>
  </header>
'''


def crumbs(items):
    parts = ['<a href="okatent-carpas.html" data-i18n="crumb.home">Inicio</a>']
    for label, key in items:
        parts.append('<span>/</span>')
        parts.append(f'<span data-i18n="{key}">{label}</span>')
    return '<nav class="crumbs" aria-label="Migas de pan">' + ''.join(parts) + '</nav>'


STAR = '<svg viewBox="0 0 20 20"><path d="M10 1.5l2.6 5.6 6.1.7-4.5 4.2 1.2 6-5.4-3-5.4 3 1.2-6L1.3 7.8l6.1-.7z"/></svg>'
SOCIAL = '''<a href="https://instagram.com/okatent_official" target="_blank" rel="noopener" aria-label="Instagram"><svg viewBox="0 0 24 24"><path d="M12 2.2c3.2 0 3.6 0 4.8.1 3.3.1 4.8 1.7 4.9 4.9.1 1.3.1 1.6.1 4.8s0 3.6-.1 4.8c-.1 3.2-1.7 4.8-4.9 4.9-1.3.1-1.6.1-4.8.1s-3.6 0-4.8-.1c-3.3-.1-4.8-1.7-4.9-4.9C2.2 15.6 2.2 15.2 2.2 12s0-3.6.1-4.8C2.4 3.9 3.9 2.4 7.2 2.3 8.4 2.2 8.8 2.2 12 2.2zM12 0C8.7 0 8.3 0 7.1.1 2.7.3.3 2.7.1 7.1 0 8.3 0 8.7 0 12s0 3.7.1 4.9c.2 4.4 2.6 6.8 7 7C8.3 24 8.7 24 12 24s3.7 0 4.9-.1c4.4-.2 6.8-2.6 7-7 .1-1.2.1-1.6.1-4.9s0-3.7-.1-4.9c-.2-4.4-2.6-6.8-7-7C15.7 0 15.3 0 12 0zm0 5.8a6.2 6.2 0 1 0 0 12.4 6.2 6.2 0 0 0 0-12.4zM12 16a4 4 0 1 1 0-8 4 4 0 0 1 0 8zm6.4-11.8a1.4 1.4 0 1 0 0 2.9 1.4 1.4 0 0 0 0-2.9z"/></svg></a>
          <a href="https://es.linkedin.com/company/okatent" target="_blank" rel="noopener" aria-label="LinkedIn"><svg viewBox="0 0 24 24"><path d="M20.4 20.5h-3.6v-5.6c0-1.3 0-3-1.9-3s-2.1 1.4-2.1 2.9v5.7H9.4V9h3.4v1.6c.5-.9 1.6-1.9 3.4-1.9 3.6 0 4.3 2.4 4.3 5.5v6.3zM5.3 7.4a2.1 2.1 0 1 1 0-4.1 2.1 2.1 0 0 1 0 4.1zm1.8 13.1H3.6V9h3.5v11.5zM22.2 0H1.8C.8 0 0 .8 0 1.7v20.5c0 1 .8 1.8 1.8 1.8h20.4c1 0 1.8-.8 1.8-1.8V1.7C24 .8 23.2 0 22.2 0z"/></svg></a>
          <a href="https://www.youtube.com/@okatent" target="_blank" rel="noopener" aria-label="YouTube"><svg viewBox="0 0 24 24"><path d="M23.5 6.2a3 3 0 0 0-2.1-2.1C19.5 3.6 12 3.6 12 3.6s-7.5 0-9.4.5A3 3 0 0 0 .5 6.2 31 31 0 0 0 0 12a31 31 0 0 0 .5 5.8 3 3 0 0 0 2.1 2.1c1.9.5 9.4.5 9.4.5s7.5 0 9.4-.5a3 3 0 0 0 2.1-2.1A31 31 0 0 0 24 12a31 31 0 0 0-.5-5.8zM9.6 15.6V8.4l6.3 3.6z"/></svg></a>'''


def cta_band(h2_key='cta.h2', h2='¿Qué carpa necesitas?', p_key='cta.p', p='Cuéntanos para qué la vas a usar, la medida y la fecha. Te respondemos en menos de 48 horas laborables.', href='okatent-contacto.html', img='imgs/web/noche-plaza.jpg'):
    return f'''
    <section class="cta-photo" aria-labelledby="cta-title">
      <div class="cta-in">
        <img src="{img}" alt="" loading="lazy">
        <div class="wrap">
          <span class="eyebrow" data-i18n="cta.eyebrow">Presupuesto en 48 h</span>
          <h2 id="cta-title" data-i18n="{h2_key}">{h2}</h2>
          <p data-i18n="{p_key}">{p}</p>
          <div class="btn-row">
            <a href="{href}" class="btn btn-white"><span data-i18n="nav.cta">Pedir presupuesto</span>{ARROW}</a>
            <a href="https://wa.me/34933231974" target="_blank" rel="noopener" class="btn btn-light">WhatsApp</a>
          </div>
        </div>
      </div>
    </section>
'''


def footer():
    return f'''
  <footer class="footer">
    <div class="wrap">
      <div class="footer-top">
        <p class="footer-claim"><span data-i18n="ft.claim1">Carpas plegables hechas para durar.</span> <span class="dim" data-i18n="ft.claim2">Fabricadas en Olesa de Montserrat desde hace más de 20 años.</span></p>
        <nav class="footer-products" aria-label="Productos">
          <a href="okatent-carpas-plegables.html#modelos"><span class="mono">01</span><b>Cebú</b><small data-i18n="ft.p1">Gama profesional · desde 890 €</small></a>
          <a href="okatent-carpas-plegables.html#modelos"><span class="mono">02</span><b>Borneo</b><small data-i18n="ft.p2">Gama de iniciación · desde 590 €</small></a>
          <a href="okatent-personalizacion.html"><span class="mono">03</span><b data-i18n="nav.personal">Personalización</b><small data-i18n="ft.p3">Con tu marca</small></a>
          <a href="okatent-configurador.html"><span class="mono">3D</span><b data-i18n="nav.config">Configurador 3D</b><small data-i18n="ft.p4">Pruébala antes de pedirla</small></a>
        </nav>
      </div>
      <div class="footer-grid">
        <div>
          <h4 data-i18n="ft.carpas">Carpas</h4>
          <ul>
            <li><a href="okatent-carpas-plegables.html#modelos" data-i18n="nav.modelos">Modelos Cebú y Borneo</a></li>
            <li><a href="okatent-carpas-plegables.html#visor" data-i18n="vw.eyebrow">Colores y paredes</a></li>
            <li><a href="okatent-carpas-plegables.html#medidas" data-i18n="nav.ficha">Medidas y ficha técnica</a></li>
            <li><a href="okatent-personalizacion.html" data-i18n="nav.personal">Personalización</a></li>
          </ul>
        </div>
        <div>
          <h4 data-i18n="ft.accesorios">Accesorios</h4>
          <ul>
            <li><a href="okatent-complementos.html" data-i18n="nav.comp">Complementos</a></li>
            <li><a href="okatent-recambios.html" data-i18n="nav.rec">Recambios</a></li>
          </ul>
        </div>
        <div>
          <h4 data-i18n="ft.empresa">Empresa</h4>
          <ul>
            <li><a href="okatent-empresa.html" data-i18n="em.story.eyebrow">Quiénes somos</a></li>
            <li><a href="okatent-casos.html" data-i18n="nav.casos">Casos</a></li>
            <li><a href="okatent-carpas-plegables.html#preguntas" data-i18n="faq.eyebrow">Preguntas frecuentes</a></li>
            <li><a href="https://okatent.com" target="_blank" rel="noopener" data-i18n="ft.pabellones">Pabellones modulares</a></li>
          </ul>
        </div>
        <div>
          <h4 data-i18n="ft.contacto">Contacto</h4>
          <ul>
            <li><a href="tel:+34933231974">93 323 19 74</a></li>
            <li><a href="mailto:info@okatent.com">info@okatent.com</a></li>
            <li>Polígon Can Singla, 08640 Olesa de Montserrat</li>
          </ul>
        </div>
        <div class="social">
          {SOCIAL}
        </div>
      </div>
      <div class="footer-bottom">
        <span>© <span id="year">2026</span> OKATENT S.L. · CIF B-63802078</span>
        <span data-i18n="ft.rights">Todos los derechos reservados.</span>
      </div>
      <div class="wordmark" aria-hidden="true"><span>OKATENT</span><i></i></div>
    </div>
  </footer>

  <a class="wa-float" href="https://wa.me/34933231974" target="_blank" rel="noopener" aria-label="WhatsApp"><svg viewBox="0 0 24 24"><path d="{WA_PATH}"/></svg></a>
'''


def page_head(crumb, h1_key, h1, lead_key, lead, buttons='', media='', media_alt='', media_pos='', caption='', extra=''):
    fig = ''
    if media:
        cap = f'<figcaption>{caption}</figcaption>' if caption else ''
        pos = f' style="object-position:{media_pos}"' if media_pos else ''
        fig = f'\n        <figure class="ph-media rv"><img src="{media}" alt="{media_alt}" fetchpriority="high"{pos}>{cap}</figure>'
    btns = f'<div class="btn-row">{buttons}</div>' if buttons else '<div></div>'
    return f'''
    <section class="page-head">
      <div class="wrap">
        {crumbs(crumb)}
        <h1 data-i18n="{h1_key}">{h1}</h1>
        <div class="ph-row">
          <p class="lead" data-i18n="{lead_key}">{lead}</p>
          {btns}
        </div>{extra}{fig}
      </div>
    </section>
'''


def subnav(items):
    links = ''.join(f'<a href="#{i}" data-i18n="{k}">{t}</a>' for i, k, t in items)
    return f'''
    <nav class="subnav" aria-label="Secciones">
      <div class="wrap"><div class="subnav-in">{links}</div></div>
    </nav>
'''


def scripts(page_dict, before='', after=''):
    return f'''
{before}  <script src="js/i18n.js"></script>
  <script src="js/i18n/comun.js"></script>
  <script src="js/i18n/{page_dict}.js"></script>
  <script src="js/okatent.js"></script>
{after}</body>
</html>
'''


def checks(items):
    return '<ul class="checks">' + ''.join(f'<li>{CHECK}<span data-i18n="{k}">{t}</span></li>' for k, t in items) + '</ul>'

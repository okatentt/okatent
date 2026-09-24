# -*- coding: utf-8 -*-
"""Genera las páginas, los diccionarios de idioma y actualiza tiendas y configurador."""
import json, os, re, sys
os.chdir(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, '.')
from site_parts import *
from site_pages import *
from site_i18n import NEW
from site_i18n2 import NEW2
NEW.update(NEW2)

# la web está en la carpeta de arriba (este script vive en _generador/)
ROOT = os.path.abspath('..')
PREV = json.load(open('prev_i18n.json', encoding='utf-8'))
LANGS = ['CA', 'EN', 'FR', 'IT']

# textos extra de las tiendas
NEW.update({
 'sh.filter.size': {'CA': 'Filtrar per mida:', 'EN': 'Filter by size:', 'FR': 'Filtrer par taille :', 'IT': 'Filtra per misura:'},
 'sh.filter.type': {'CA': 'Filtrar per tipus:', 'EN': 'Filter by type:', 'FR': 'Filtrer par type :', 'IT': 'Filtra per tipo:'},
 'sh.all.f': {'CA': 'Totes', 'EN': 'All', 'FR': 'Toutes', 'IT': 'Tutte'},
 'sh.all.m': {'CA': 'Tots', 'EN': 'All', 'FR': 'Tous', 'IT': 'Tutti'},
 'sh.universal': {'CA': 'Universal', 'EN': 'Universal', 'FR': 'Universel', 'IT': 'Universale'},
 'cm.f.lateral': {'CA': 'Laterals', 'EN': 'Walls', 'FR': 'Parois', 'IT': 'Pareti'},
 'cm.f.toldo': {'CA': 'Tendals', 'EN': 'Awnings', 'FR': 'Auvents', 'IT': 'Tettoie'},
 'cm.f.transporte': {'CA': 'Transport', 'EN': 'Transport', 'FR': 'Transport', 'IT': 'Trasporto'},
 'cm.f.fijacion': {'CA': 'Fixació', 'EN': 'Anchoring', 'FR': 'Fixation', 'IT': 'Fissaggio'},
 'cm.f.accesorio': {'CA': 'Accessoris', 'EN': 'Accessories', 'FR': 'Accessoires', 'IT': 'Accessori'},
 'rc.search': {'CA': 'Cerca peça o referència…', 'EN': 'Search part or reference…', 'FR': 'Rechercher une pièce ou une référence…', 'IT': 'Cerca pezzo o codice…'},
 'rc.title': {'CA': 'Recanvis per a carpes plegables Cebú i Borneo | OKATENT', 'EN': 'Spare parts for Cebú and Borneo folding tents | OKATENT', 'FR': 'Pièces détachées pour tentes pliantes Cebú et Borneo | OKATENT', 'IT': 'Ricambi per gazebo pieghevoli Cebú e Borneo | OKATENT'},
 'cm.title': {'CA': 'Complements per a carpes plegables: parets, pesos i sacs | OKATENT', 'EN': 'Folding tent accessories: walls, weights and bags | OKATENT', 'FR': 'Accessoires pour tentes pliantes : parois, lests et sacs | OKATENT', 'IT': 'Accessori per gazebo pieghevoli: pareti, pesi e sacche | OKATENT'},
 'cm.search': {'CA': 'Cerca complement…', 'EN': 'Search accessories…', 'FR': 'Rechercher un accessoire…', 'IT': 'Cerca accessorio…'},
})

JS_KEYS = {
    'comun': [],
    'inicio': ['c.*'],
    'carpas': ['c.*', 'vw.liso', 'vw.ventana', 'vw.puerta', 'vw.medio', 'vw.nowall', 'vw.side.*', 'vw.sum.none', 'vw.awning'],
    'contacto': ['c.*', 'use.*', 'f.use', 'f.qty', 'f.model', 'f.model.any', 'f.size', 'f.color', 'f.yes', 'f.no', 'f.ok', 'f.err', 'mail.subject', 'mail.hello'],
    'configurador': ['c.*', 'vw.liso', 'vw.ventana', 'vw.puerta', 'vw.medio', 'vw.nowall', 'vw.side.*', 'vw.sum.none', 'vw.awning', 'cfg.ask', 'cfg.from', 'cfg.unit'],
    'personalizacion': [], 'casos': [], 'empresa': [], 'tienda': [],
}
TITLE_KEYS = {'recambios': 'rc.title', 'complementos': 'cm.title', 'inicio': 'title', 'carpas': 'cp.title', 'personalizacion': 'pz.title', 'casos': 'cs.title', 'empresa': 'em.title', 'contacto': 'ct.title', 'configurador': 'cfg.title'}

ES_EXTRA = {
    'vw.liso': 'Lisa', 'vw.ventana': 'Con ventana', 'vw.puerta': 'Con puerta', 'vw.medio': 'Media pared',
    'vw.nowall': 'Sin pared', 'vw.sum.none': 'sin paredes', 'vw.awning': 'Visera frontal',
    'vw.side.back': 'Fondo', 'vw.side.left': 'Izquierda', 'vw.side.right': 'Derecha', 'vw.side.front': 'Frente',
    'cfg.from': 'Desde', 'cfg.unit': 'unidad', 'cfg.ask': 'Precio a consultar',
    'use.mercado': 'Mercados y ferias', 'use.deporte': 'Eventos deportivos', 'use.hosteleria': 'Hostelería y street food',
    'use.empresa': 'Eventos de empresa', 'use.marca': 'Promoción de marca', 'use.particular': 'Uso particular', 'use.otro': 'Otro',
    'f.use': '¿Para qué la vas a usar?', 'f.qty': 'Cantidad', 'f.model': 'Modelo', 'f.model.any': 'Todavía no lo sé', 'f.size': 'Medida', 'f.color': 'Color',
}
ALL_KEYS = set(NEW) | set(PREV['EN']) | set(PREV['ES'])

def expand(patterns):
    out = []
    for pat in patterns:
        if pat.endswith('*'):
            out += [k for k in sorted(ALL_KEYS) if k.startswith(pat[:-1])]
        else:
            out.append(pat)
    return out

def value(key, L):
    if key in NEW and L in NEW[key]:
        return NEW[key][L]
    if key in PREV[L]:
        return PREV[L][key]
    return None

missing = {}

def keys_in(html):
    ks = set(re.findall(r'data-i18n="([^"]+)"', html)) | set(re.findall(r'data-i18n-ph="([^"]+)"', html)) | set(re.findall(r'data-i18n-aria="([^"]+)"', html))
    return ks

COMMON_HTML = header() + footer() + cta_band()
COMMON_KEYS = keys_in(COMMON_HTML)

def write_dict(name, html, extra_es=None):
    ks = (keys_in(html) - COMMON_KEYS) | set(expand(JS_KEYS.get(name, [])))
    d = {L: {} for L in ['ES'] + LANGS}
    for k in sorted(ks):
        for L in LANGS:
            v = value(k, L)
            if v is None:
                missing.setdefault(name, set()).add(k)
            else:
                d[L][k] = v
        es_val = ES_EXTRA.get(k) or PREV['ES'].get(k)
        if es_val is not None and k in set(expand(JS_KEYS.get(name, []))):
            d['ES'][k] = es_val
    tk = TITLE_KEYS.get(name)
    if tk:
        for L in LANGS:
            v = value(tk, L)
            if v: d[L]['title'] = v
    if not d['ES']:
        del d['ES']
    js = '/* Textos de la página (' + name + '). El español se lee del HTML. */\nOK_I18N.add(' + json.dumps(d, ensure_ascii=False, indent=1) + ');\n'
    os.makedirs(ROOT + r'\js\i18n', exist_ok=True)
    open(ROOT + rf'\js\i18n\{name}.js', 'w', encoding='utf-8').write(js)

def write_common():
    ks = COMMON_KEYS | {'c.azul'}
    d = {L: {} for L in LANGS}
    for k in sorted(ks):
        for L in LANGS:
            v = value(k, L)
            if v is None: missing.setdefault('comun', set()).add(k)
            else: d[L][k] = v
    js = '/* Textos comunes: barra superior, menú, pie y franja de llamada. */\nOK_I18N.add(' + json.dumps(d, ensure_ascii=False, indent=1) + ');\n'
    open(ROOT + r'\js\i18n\comun.js', 'w', encoding='utf-8').write(js)

def save(fname, html):
    open(ROOT + '\\' + fname, 'w', encoding='utf-8').write(html)

# ------------------------------------------------------------------ páginas nuevas
pages = {
    'okatent-carpas.html': ('inicio', page_inicio()),
    'okatent-carpas-plegables.html': ('carpas', page_carpas()),
    'okatent-personalizacion.html': ('personalizacion', page_personalizacion()),
    'okatent-casos.html': ('casos', page_casos()),
    'okatent-empresa.html': ('empresa', page_empresa()),
    'okatent-contacto.html': ('contacto', page_contacto()),
}
for fname, (dname, html) in pages.items():
    save(fname, html)
    write_dict(dname, html)
write_common()

save('index.html', '<!DOCTYPE html><html lang="es"><head><meta charset="UTF-8"><meta http-equiv="refresh" content="0; url=okatent-carpas.html"><link rel="canonical" href="okatent-carpas.html"><title>OKATENT</title></head><body><a href="okatent-carpas.html">OKATENT</a></body></html>\n')

# ------------------------------------------------------------------ tiendas
def shop(fname, dname, current_label, crumb_key, eyebrow, h1, lead, points):
    s = open(ROOT + '\\' + fname, encoding='utf-8').read()
    a = s.index('  <header class="nav" id="nav">') if '<div class="topbar">' not in s else s.index('  <div class="topbar">')
    b = s.index('</section>', s.index('class="page-head')) + len('</section>')
    pts = ''.join(f'<li>{CHECK}<span data-i18n="{k}">{t}</span></li>' for k, t in points)
    ph = f'''
  <section class="page-head compact">
    <div class="wrap">
      {crumbs([(current_label, crumb_key)])}
      <span class="eyebrow" data-i18n="{eyebrow[0]}">{eyebrow[1]}</span>
      <h1 data-i18n="{h1[0]}">{h1[1]}</h1>
      <p class="lead" data-i18n="{lead[0]}">{lead[1]}</p>
      <ul class="page-points">{pts}</ul>
    </div>
  </section>'''
    s = s[:a] + header('accesorios', cart=True).lstrip('\n') + ph + s[b:]
    # pie
    a = s.index('  <footer class="footer">')
    b = s.index('</a>', s.index('class="wa-float"')) + len('</a>')
    s = s[:a] + footer().strip('\n') + s[b:]
    s = re.sub(r'[ ]*<script src="js/(?:i18n\.js|i18n/[a-z]+\.js|okatent\.js)"></script>\n', '', s)
    if "classList.add('fx')" not in s:
        s = s.replace('</head>', "  <script>if(!(window.matchMedia&&matchMedia('(prefers-reduced-motion: reduce)').matches))document.documentElement.classList.add('fx')</script>\n</head>", 1)
    s = s.replace('</body>', f'''  <script src="js/i18n.js"></script>
  <script src="js/i18n/comun.js"></script>
  <script src="js/i18n/{dname}.js"></script>
  <script src="js/okatent.js"></script>
</body>''')
    # textos de la tienda
    rep = [
        ('<div class="model-select-card-desc">Gama profesional. Aluminio anodizado, certificado T2 APPLUS.</div>', '<div class="model-select-card-desc" data-i18n="sh.cebu.desc">Gama profesional. Aluminio anodizado, certificado T2 APPLUS.</div>'),
        ('<div class="model-select-card-desc">Gama de iniciación. Ligera y económica.</div>', '<div class="model-select-card-desc" data-i18n="sh.borneo.desc">Gama de iniciación. Ligera y económica.</div>'),
        ('<span class="filters-label">Filtrar por medida:</span>', '<span class="filters-label" data-i18n="sh.filter.size">Filtrar por medida:</span>'),
        ('<span class="filters-label">Filtrar por tipo:</span>', '<span class="filters-label" data-i18n="sh.filter.type">Filtrar por tipo:</span>'),
        ('<button class="filter-btn active" data-filter="all">Todas</button>', '<button class="filter-btn active" data-filter="all" data-i18n="sh.all.f">Todas</button>'),
        ('<button class="filter-btn active" data-filter="all">Todos</button>', '<button class="filter-btn active" data-filter="all" data-i18n="sh.all.m">Todos</button>'),
        ('<button class="filter-btn" data-filter="universal">Universal</button>', '<button class="filter-btn" data-filter="universal" data-i18n="sh.universal">Universal</button>'),
        ('<button class="filter-btn" data-filter="lateral">Laterales</button>', '<button class="filter-btn" data-filter="lateral" data-i18n="cm.f.lateral">Laterales</button>'),
        ('<button class="filter-btn" data-filter="toldo">Toldos</button>', '<button class="filter-btn" data-filter="toldo" data-i18n="cm.f.toldo">Toldos</button>'),
        ('<button class="filter-btn" data-filter="transporte">Transporte</button>', '<button class="filter-btn" data-filter="transporte" data-i18n="cm.f.transporte">Transporte</button>'),
        ('<button class="filter-btn" data-filter="fijacion">Fijación</button>', '<button class="filter-btn" data-filter="fijacion" data-i18n="cm.f.fijacion">Fijación</button>'),
        ('<button class="filter-btn" data-filter="accesorio">Accesorios</button>', '<button class="filter-btn" data-filter="accesorio" data-i18n="cm.f.accesorio">Accesorios</button>'),
        ('placeholder="Buscar pieza o referencia..."', 'placeholder="Buscar pieza o referencia…" data-i18n-ph="rc.search"'),
        ('placeholder="Buscar complemento..."', 'placeholder="Buscar complemento…" data-i18n-ph="cm.search"'),
        ('<span class="fab-label">Mi pedido</span>', '<span class="fab-label" data-i18n="sh.fab">Mi pedido</span>'),
        ('<h3>Tu pedido</h3>', '<h3 data-i18n="sh.cart.h">Tu pedido</h3>'),
        ('<span class="cart-total-label">Total estimado</span>', '<span class="cart-total-label" data-i18n="sh.cart.total">Total estimado</span>'),
        ('<p class="cart-note">Precios sin IVA. Te confirmamos el pedido por WhatsApp o correo.</p>', '<p class="cart-note" data-i18n="sh.cart.note">Precios sin IVA. Te confirmamos el pedido por WhatsApp o correo.</p>'),
        ('\n        Pedir por WhatsApp\n', '\n        <span data-i18n="sh.cart.wa">Pedir por WhatsApp</span>\n'),
        ('Pedir por correo\n', '<span data-i18n="sh.cart.mail">Pedir por correo</span>\n'),
        ('<h2>¿No encuentras la pieza?</h2>', '<h2 data-i18n="rc.cta.h2">¿No encuentras la pieza?</h2>'),
        ('<p>Mándanos una foto por WhatsApp y te localizamos el recambio de tu carpa.</p>', '<p data-i18n="rc.cta.p">Mándanos una foto por WhatsApp y te localizamos el recambio de tu carpa.</p>'),
        ('class="btn btn-primary">Enviar foto por WhatsApp', 'class="btn btn-primary"><span data-i18n="rc.cta.b1">Enviar foto por WhatsApp</span>'),
        ('<a href="mailto:info@okatent.com" class="btn btn-light">Escribirnos</a>', '<a href="mailto:info@okatent.com" class="btn btn-light" data-i18n="rc.cta.b2">Escribirnos</a>'),
        ('<h2>¿Dudas sobre la compatibilidad?</h2>', '<h2 data-i18n="cm.cta.h2">¿Dudas sobre la compatibilidad?</h2>'),
        ('<p>Dinos tu modelo y medida y te decimos qué complemento necesitas.</p>', '<p data-i18n="cm.cta.p">Dinos tu modelo y medida y te decimos qué complemento necesitas.</p>'),
        ('class="btn btn-primary">Preguntar por WhatsApp', 'class="btn btn-primary"><span data-i18n="cm.cta.b1">Preguntar por WhatsApp</span>'),
        ('<a href="okatent-carpas.html#contacto" class="btn btn-light">Pedir presupuesto</a>', '<a href="okatent-contacto.html" class="btn btn-light" data-i18n="nav.cta">Pedir presupuesto</a>'),
    ]
    for x, y in rep:
        s = s.replace(x, y)
    if fname == 'okatent-recambios.html':
        s = s.replace('<div class="model-select-title">Recambios para tu carpa</div>', '<div class="model-select-title" data-i18n="sh.which">¿Qué carpa tienes?</div>')
        s = s.replace('<p class="model-select-sub">Elige tu modelo para ver las piezas y medidas disponibles.</p>', '<p class="model-select-sub" data-i18n="rc.which.sub">Te enseñamos solo las piezas que le sirven.</p>')
    else:
        s = s.replace('<div class="model-select-title">Complementos para tu carpa</div>', '<div class="model-select-title" data-i18n="sh.which">¿Qué carpa tienes?</div>')
        s = s.replace('<p class="model-select-sub">Elige tu modelo para ver los accesorios disponibles.</p>', '<p class="model-select-sub" data-i18n="cm.which.sub">Te enseñamos solo los complementos compatibles.</p>')
    s = s.replace('okatent-carpas.html#contacto', 'okatent-contacto.html')
    save(fname, s)
    return s

rec = shop('okatent-recambios.html', 'recambios', 'Recambios', 'nav.rec', ('rc.eyebrow', 'Recambios originales'), ('rc.h1', 'Recambios para tu carpa Cebú o Borneo'),
           ('rc.lead', 'Una pieza rota no significa comprar una carpa nueva. Busca la tuya por medida o referencia, añádela al pedido y envíanoslo por WhatsApp o correo.'),
           [('rc.pt1', 'Piezas originales de fábrica'), ('rc.pt2', 'Con referencia de catálogo'), ('rc.pt3', 'Envío en 48–72 h'), ('rc.pt4', 'Garantía de fabricante')])
com = shop('okatent-complementos.html', 'complementos', 'Complementos', 'nav.comp', ('cm.eyebrow', 'Complementos originales'), ('cm.h1', 'Complementos para tu carpa plegable'),
           ('cm.lead', 'Paredes, visera, pesos, canal de desagüe, sacos y abrazaderas para Cebú y Borneo. Elige la medida, añádelos a tu pedido y te confirmamos precio y plazo por WhatsApp o correo.'),
           [('cm.pt1', 'Compatibles con Cebú y Borneo'), ('cm.pt2', 'Materiales originales de fábrica'), ('top.2', 'Envío a toda España'), ('rc.pt4', 'Garantía de fabricante')])
write_dict('recambios', rec)
write_dict('complementos', com)

# ------------------------------------------------------------------ configurador
from site_config import page_configurador
cfg = page_configurador()
save('okatent-configurador.html', cfg)
write_dict('configurador', cfg)

for k, v in missing.items():
    print('FALTAN', k, sorted(v))
print('ok')

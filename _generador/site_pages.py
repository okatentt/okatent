# -*- coding: utf-8 -*-
"""Cuerpos de las páginas (v2: identidad Lightship × Okatent).
Los casos, opiniones, precios «desde», garantía, viento y plazos de personalización son DE EJEMPLO
(marcados con data-demo en el HTML): hay que sustituirlos por datos reales antes de publicar."""
from site_parts import *

W = 'imgs/web/'
COLORS_NOTE = ''

# ---------------------------------------------------------------- casos de ejemplo
CASES = [
    dict(id='serra-alta', img=W + 'caso-mercado.jpg', brand='Formatges Serra Alta', pos='50% 50%',
         tags=('v2.c1.tags', 'Mercados · Cebú 3×3 · Berguedà'),
         title=('v2.c1.t', 'Tres mercados a la semana y ni una pieza cambiada en dos temporadas'),
         need=('v2.c1.n', 'Montar y desmontar tres veces por semana, con viento y con lluvia. Su carpa anterior no aguantó un invierno.'),
         did=('v2.c1.d', 'Cebú 3×3 color crema con el nombre impreso en el faldón, pared de fondo lisa y pesos de 10 kg.'),
         res=('v2.c1.r', 'Más de 300 montajes en dos temporadas sin cambiar ninguna pieza.'),
         metrics=[('300+', 'v2.c1.m1', 'montajes'), ('5 min', 'v2.c1.m2', 'para montarla')],
         quote=('v2.c1.q', '«Antes montábamos con miedo cada vez que soplaba. Ahora la abrimos en cinco minutos y nos olvidamos.»'),
         who='Montse Serra', role=('v2.c1.w', 'Quesera · Formatges Serra Alta')),
    dict(id='trail-serralada', img=W + 'caso-trail.jpg', brand='Trail Serralada 42K', pos='50% 50%',
         tags=('v2.c2.tags', 'Deporte · 4 × Cebú 3×3 · Vallès'),
         title=('v2.c2.t', 'La zona de meta, montada por dos voluntarios en 25 minutos'),
         need=('v2.c2.n', 'Cronometraje, meta y avituallamientos que se montan de madrugada y con poca gente.'),
         did=('v2.c2.d', 'Cuatro Cebú 3×3 rojas con el nombre de la carrera en el faldón, dos paredes laterales y sacos con ruedas.'),
         res=('v2.c2.r', 'La meta queda lista antes de la salida con dos personas, y las carpas viajan en una furgoneta.'),
         metrics=[('25 min', 'v2.c2.m1', 'zona de meta'), ('4', 'v2.c2.m2', 'carpas')],
         quote=('v2.c2.q', '«Dos voluntarios, cuatro carpas y la meta lista antes de que salga el sol.»'),
         who='Jordi Puig', role=('v2.c2.w', 'Director de carrera · Trail Serralada 42K')),
    dict(id='brasa-nomada', img=W + 'caso-brasa.jpg', brand='Brasa Nòmada', pos='50% 50%',
         tags=('v2.c3.tags', 'Street food · Cebú 3×4,5 · Barcelona'),
         title=('v2.c3.t', 'Pasa la inspección de cada festival a la primera, con humo y brasas debajo'),
         need=('v2.c3.n', 'Una carpa negra para cocinar con fuego en festivales, donde la organización exige lona ignífuga certificada.'),
         did=('v2.c3.d', 'Cebú 3×4,5 negra con lona certificada T2, nombre impreso en el faldón y canal de desagüe.'),
         res=('v2.c3.r', '18 festivales en la última temporada enseñando el certificado de la lona en cada control.'),
         metrics=[('18', 'v2.c3.m1', 'festivales en un año'), ('T2', 'v2.c3.m2', 'lona certificada')],
         quote=('v2.c3.q', '«En cada festival nos piden el certificado de la lona. Lo enseñamos y seguimos cocinando.»'),
         who='Àlex Ferrer', role=('v2.c3.w', 'Cofundador · Brasa Nòmada')),
    dict(id='masia-roure', img=W + 'caso-masia.jpg', brand='Masia Roure', pos='50% 50%',
         tags=('v2.c4.tags', 'Eventos · 4 × Cebú 3×3 · Penedès'),
         title=('v2.c4.t', '120 invitados a cubierto en el jardín, sin montar una carpa fija'),
         need=('v2.c4.n', 'Espacio cubierto para catas y bodas en el jardín de la bodega, que se pueda recoger entre evento y evento.'),
         did=('v2.c4.d', 'Cuatro Cebú 3×3 blancas unidas con abrazaderas y canal de desagüe, con paredes con ventana.'),
         res=('v2.c4.r', 'Montan y desmontan con su propio equipo y alquilan el espacio para eventos de hasta 120 personas.'),
         metrics=[('120', 'v2.c4.m1', 'invitados'), ('4', 'v2.c4.m2', 'carpas unidas')],
         quote=('v2.c4.q', '«Parece una instalación fija, pero el lunes está recogida en el almacén.»'),
         who='Laia Roure', role=('v2.c4.w', 'Responsable de eventos · Masia Roure')),
    dict(id='ce-la-riera', img=W + 'caso-club.jpg', brand='CE La Riera', pos='50% 50%',
         tags=('v2.c5.tags', 'Fútbol base · 2 × Cebú 3×3 · Bages'),
         title=('v2.c5.t', 'La pared de patrocinadores pagó las dos carpas en una temporada'),
         need=('v2.c5.n', 'Sombra en los banquillos durante los torneos y un sitio visible para los patrocinadores del club.'),
         did=('v2.c5.d', 'Dos Cebú 3×3 verdes con el nombre del club en el faldón y pared de fondo impresa con los patrocinadores.'),
         res=('v2.c5.r', 'Los patrocinadores de la pared cubrieron el coste de las carpas en la primera temporada.'),
         metrics=[('1', 'v2.c5.m1', 'temporada para amortizarlas'), ('2', 'v2.c5.m2', 'carpas')],
         quote=('v2.c5.q', '«La pared de patrocinadores pagó las dos carpas. Ahora nos piden sitio para la próxima.»'),
         who='Marc Vidal', role=('v2.c5.w', 'Coordinador · Club Esportiu La Riera')),
    dict(id='fira-llibre', img=W + 'caso-fira.jpg', brand='Fira del Llibre', pos='50% 50%',
         tags=('v2.c6.tags', 'Cultura · Cebú 3×6 · Bages'),
         title=('v2.c6.t', 'La misma carpa cuatro ediciones: solo cambian la pared cada año'),
         need=('v2.c6.n', 'Una carpa grande para la feria del libro, con paredes ilustradas que se puedan renovar sin comprar otra carpa.'),
         did=('v2.c6.d', 'Cebú 3×6 blanca con faldón impreso y paredes ilustradas a todo color, intercambiables.'),
         res=('v2.c6.r', 'Cuatro ediciones con la misma estructura y la misma lona; cada año solo se imprime la pared nueva.'),
         metrics=[('4', 'v2.c6.m1', 'ediciones'), ('3×6', 'v2.c6.m2', 'metros')],
         quote=('v2.c6.q', '«Cada primavera estrenamos ilustración y reutilizamos todo lo demás.»'),
         who='Núria Soler', role=('v2.c6.w', 'Organización · Fira del Llibre')),
    dict(id='nomada-coffee', img=W + 'caso-nomada.jpg', brand='Nòmada Coffee', pos='50% 50%',
         tags=('v2.c7.tags', 'Marca · Cebú 3×3 · Costa Brava'),
         title=('v2.c7.t', 'Doce fines de semana de ruta por la costa con una carpa que es un anuncio'),
         need=('v2.c7.n', 'Un stand de promoción que se reconozca desde lejos en paseos marítimos y festivales de verano.'),
         did=('v2.c7.d', 'Cebú 3×3 naranja totalmente impresa: logotipo en el techo, nombre en el faldón y media pared de fondo.'),
         res=('v2.c7.r', 'Doce fines de semana de ruta en un verano, montándola cada vez en un sitio distinto.'),
         metrics=[('12', 'v2.c7.m1', 'fines de semana'), ('100 %', 'v2.c7.m2', 'impresa')],
         quote=('v2.c7.q', '«La gente se acerca por la carpa y se queda por el café.»'),
         who='Pau Riba', role=('v2.c7.w', 'Marketing · Nòmada Coffee')),
]
CASE = {c['id']: c for c in CASES}


def story(c, featured=False, wide=False):
    t_key, t = c['title']
    g_key, g = c['tags']
    if featured:
        return f'''
          <a class="story featured{' wide' if wide else ''} rv" href="okatent-casos.html#{c['id']}" data-demo>
            <figure><img src="{c['img']}" alt="{c['brand']}" loading="lazy" style="object-position:{c['pos']}"><span class="story-brand">{c['brand']}</span>
              <div class="story-over"><h3 data-i18n="{t_key}">{t}</h3><p class="story-tags" data-i18n="{g_key}">{g}</p></div>
            </figure>
          </a>'''
    return f'''
          <a class="story rv" href="okatent-casos.html#{c['id']}" data-demo>
            <figure><img src="{c['img']}" alt="{c['brand']}" loading="lazy" style="object-position:{c['pos']}"><span class="story-brand">{c['brand']}</span></figure>
            <h3 data-i18n="{t_key}">{t}</h3>
            <p class="story-tags" data-i18n="{g_key}">{g}</p>
          </a>'''


def case_row(c):
    m = ''.join(f'<div><b>{v}</b><span data-i18n="{k}">{l}</span></div>' for v, k, l in c['metrics'])
    return f'''
        <article class="case-row rv" id="{c['id']}" data-demo>
          <figure><img src="{c['img']}" alt="{c['brand']}" loading="lazy"><span class="story-brand">{c['brand']}</span></figure>
          <div>
            <p class="story-tags" data-i18n="{c['tags'][0]}">{c['tags'][1]}</p>
            <h2 data-i18n="{c['title'][0]}">{c['title'][1]}</h2>
            <div class="case-metric">{m}</div>
            <dl>
              <div><dt data-i18n="case.need">Qué necesitaba</dt><dd data-i18n="{c['need'][0]}">{c['need'][1]}</dd></div>
              <div><dt data-i18n="case.did">Qué hicimos</dt><dd data-i18n="{c['did'][0]}">{c['did'][1]}</dd></div>
              <div><dt data-i18n="case.res">Resultado</dt><dd data-i18n="{c['res'][0]}">{c['res'][1]}</dd></div>
            </dl>
            <blockquote><span data-i18n="{c['quote'][0]}">{c['quote'][1]}</span><cite>{c['who']} · <span data-i18n="{c['role'][0]}">{c['role'][1]}</span></cite></blockquote>
          </div>
        </article>'''


QUOTES = [
    (W + 'caso-mercado.jpg', 'v2.r1', '«Dos temporadas montándola tres veces por semana y la estructura está como el primer día.»', 'Montse Serra', 'Formatges Serra Alta · Berguedà'),
    (W + 'caso-trail.jpg', 'v2.r2', '«Pedimos cuatro rojas con el nombre de la carrera. Llegaron a tiempo y el rojo es exactamente el de nuestros dorsales.»', 'Jordi Puig', 'Trail Serralada 42K · Vallès'),
    (W + 'caso-brasa.jpg', 'v2.r3', '«Se nos rompió una junta en pleno festival. Mandamos una foto por WhatsApp y a los dos días teníamos la pieza.»', 'Àlex Ferrer', 'Brasa Nòmada · Barcelona'),
]


def quotes_block():
    stars = STAR * 5
    items = ''.join(f'''
          <figure class="quote rv" data-demo>
            <div class="stars" aria-label="5/5">{stars}</div>
            <p data-i18n="{k}">{q}</p>
            <figcaption class="quote-who"><img src="{img}" alt="" loading="lazy"><span><b>{name}</b><small>{biz}</small></span></figcaption>
          </figure>''' for img, k, q, name, biz in QUOTES)
    return f'<div class="quotes">{items}\n        </div>'


LOGOS = '''
    <section class="logos" aria-label="Clientes">
      <div class="wrap">
        <span class="logos-label" data-i18n="v2.logos">Han llevado su marca en una Okatent</span>
        <div class="logos-row">
          <span class="logo-word serif">El Capricho de Gaudí</span>
          <span class="logo-word caps">Ciutat de les Arts i les Ciències</span>
          <span class="logo-word tight">playitas</span>
          <span class="logo-word caps">Maquina Motors</span>
          <span class="logo-word mono">BILLY BULLDOG</span>
        </div>
      </div>
    </section>
'''

SHOP_CARDS = f'''
        <div class="shop">
          <a href="okatent-complementos.html" class="shop-card rv">
            <div class="shop-copy">
              <span class="eyebrow" data-i18n="shop.comp.eyebrow">Complementos</span>
              <h3 data-i18n="shop.comp.h3">Todo lo que le falta a tu carpa</h3>
              <p data-i18n="shop.comp.p">Paredes lisas, con ventana o con puerta, pesos, canal de desagüe, abrazaderas y sacos de transporte.</p>
              <span class="link-arrow"><span data-i18n="shop.comp.cta">Ver complementos</span>{ARROW}</span>
            </div>
            <div class="shop-img" aria-hidden="true">
              <img class="c1" src="imgs/complementos/pared-ventana.png" alt="" loading="lazy">
              <img class="c2" src="imgs/complementos/peanas.png" alt="" loading="lazy">
            </div>
          </a>
          <a href="okatent-recambios.html" class="shop-card rv">
            <div class="shop-copy">
              <span class="eyebrow" data-i18n="shop.rec.eyebrow">Recambios</span>
              <h3 data-i18n="shop.rec.h3">Una pieza rota no es una carpa nueva</h3>
              <p data-i18n="shop.rec.p">Juntas, fijadores, tapones y tornillería con su referencia, desde 1,50 €. Envío a toda España.</p>
              <span class="link-arrow"><span data-i18n="shop.rec.cta">Ver recambios</span>{ARROW}</span>
            </div>
            <div class="shop-img" aria-hidden="true">
              <img class="r1" src="imgs/accesorios/junta-superior-tres-varillas-CA5080@4x.webp" alt="" loading="lazy">
              <img class="r2" src="imgs/accesorios/union-con-bulon-de-apertura-CA5100@4x.webp" alt="" loading="lazy">
              <img class="r3" src="imgs/accesorios/fijador-de-altura-CA5050@4x.webp" alt="" loading="lazy">
            </div>
          </a>
        </div>'''


def faq(items):
    out = []
    for q, qt, a, at, demo in items:
        d = ' data-demo' if demo else ''
        out.append(f'<details{d}><summary><span data-i18n="{q}">{qt}</span><i></i></summary><p class="faq-a" data-i18n="{a}">{at}</p></details>')
    return '\n          '.join(out)


PRODUCT_FAQ = [
    ('q1', '¿Cuánto se tarda en montarla?', 'a1', 'Unos minutos, y sin herramientas. La estructura de tijera se despliega de una vez: solo hay que abrirla y fijar la altura de las patas.', False),
    ('q2', '¿Qué diferencia hay entre la Cebú y la Borneo?', 'a2', 'La Cebú es la gama profesional: perfil de aluminio de mayor sección, lona con certificación T2 y 10 medidas, de 2×2 a 4×8 m. La Borneo es la gama de iniciación: más ligera y económica, pensada para un uso ocasional.', False),
    ('q8', '¿Qué garantía tienen?', 'v2.a8', 'Tres años de garantía de fabricante en la estructura y la lona. Y fuera de garantía, tienes el recambio de cada pieza.', True),
    ('q3', '¿Puedo poner el logotipo de mi empresa?', 'a3', 'Sí. Imprimimos logotipos, textos o diseños completos en el techo, los faldones y las paredes, con impresión de alta durabilidad.', False),
    ('q4', '¿Qué colores hay?', 'a4', '13: blanco, crema, gris, amarillo, lima, naranja, rojo, malva, menta, verde, azul, negro y transparente. Si buscas otro color, pregúntanos.', False),
    ('q5', '¿Se pueden unir varias carpas?', 'a5', 'Sí. Con abrazaderas de unión y canal de desagüe se unen lado con lado para cubrir espacios grandes en ferias y eventos.', False),
    ('v2.q9', '¿Aguanta el viento?', 'v2.a9', 'Con pesos de 10 kg en cada pata aguanta rachas de hasta 50 km/h. Con más viento, hay que desmontarla: ninguna carpa plegable está pensada para un temporal.', True),
    ('q6', '¿Cuánto tarda en llegar?', 'a6', '3–5 días laborables a la península. Para Baleares y Canarias, consúltanos. Envíos internacionales: 7–15 días laborables según el destino.', False),
    ('q7', '¿Tenéis recambios?', 'a7', 'Sí, de cada pieza, con su referencia. Puedes pedirlos en nuestra <a href="okatent-recambios.html">página de recambios</a> o escribirnos si no sabes cuál necesitas.', False),
]


def models_block():
    return f'''
        <div class="models">
          <article class="model-card rv">
            <figure><img src="{W}caso-mercado.jpg" alt="Carpa plegable Cebú en un mercado semanal" loading="lazy"><span class="tag" data-i18n="cebu.tag">Gama profesional</span></figure>
            <div class="model-title"><h3>Cebú</h3><span class="from" data-demo data-i18n="v2.from.c">Desde <b>890 €</b> + IVA · 3×3 m</span></div>
            <p class="model-for" data-i18n="cebu.for">Para quien la monta cada semana: ferias, mercados, eventos y uso intensivo.</p>
            <dl class="model-specs">
              <div><dt data-i18n="cmp.use">Uso recomendado</dt><dd data-i18n="cmp.use.c">Profesional e intensivo</dd></div>
              <div><dt data-i18n="sp.1">Estructura</dt><dd data-i18n="v2.ms.c1">Aluminio 6063 T5 anodizado, de mayor sección</dd></div>
              <div><dt data-i18n="cmp.cert">Lona</dt><dd data-i18n="v2.ms.c2">Poliéster 420 g/m², certificada T2</dd></div>
              <div><dt data-i18n="cmp.sizes">Medidas</dt><dd data-i18n="cmp.sizes.c">10, de 2×2 a 4×8 m</dd></div>
            </dl>
            <div class="btn-row">
              <a href="okatent-configurador.html" class="btn btn-dark"><span data-i18n="v2.cfg3d">Configurar en 3D</span>{ARROW}</a>
              <a href="okatent-contacto.html?model=Cebú" class="btn btn-soft" data-i18n="cebu.cta2">Pedir precio</a>
            </div>
          </article>
          <article class="model-card rv">
            <figure><img src="{W}caso-club.jpg" alt="Carpas plegables en un torneo de fútbol base" loading="lazy"><span class="tag" data-i18n="borneo.tag">Gama de iniciación</span></figure>
            <div class="model-title"><h3>Borneo</h3><span class="from" data-demo data-i18n="v2.from.b">Desde <b>590 €</b> + IVA · 3×3 m</span></div>
            <p class="model-for" data-i18n="borneo.for">Para uso ocasional: hostelería, eventos puntuales o tu primera carpa plegable.</p>
            <dl class="model-specs">
              <div><dt data-i18n="cmp.use">Uso recomendado</dt><dd data-i18n="cmp.use.b">Ocasional</dd></div>
              <div><dt data-i18n="sp.1">Estructura</dt><dd data-i18n="v2.ms.b1">Aluminio, perfil más ligero</dd></div>
              <div><dt data-i18n="cmp.cert">Lona</dt><dd data-i18n="v2.ms.b2">Poliéster impermeable</dd></div>
              <div><dt data-i18n="cmp.sizes">Medidas</dt><dd data-demo data-i18n="v2.ms.b3">3×3, 3×4,5 y 3×6 m</dd></div>
            </dl>
            <div class="btn-row">
              <a href="okatent-contacto.html?model=Borneo" class="btn btn-dark"><span data-i18n="borneo.cta">Pedir precio</span>{ARROW}</a>
              <a href="okatent-carpas-plegables.html#modelos" class="btn btn-soft" data-i18n="v2.compare">Comparar modelos</a>
            </div>
          </article>
        </div>'''


# =====================================================================
# INICIO
# =====================================================================
def page_inicio():
    h = head('Carpas plegables profesionales fabricadas en Barcelona | OKATENT',
             'Fabricantes de carpas plegables profesionales en Olesa de Montserrat (Barcelona): aluminio anodizado, lona ignífuga certificada T2, personalización con tu marca y recambio de cada pieza.')
    mq_words = [('v2.mq1', 'Aluminio 6063 T5'), ('v2.mq2', 'Lona ignífuga T2'), ('v2.mq3', 'Hecha en Olesa de Montserrat'), ('v2.mq4', 'Recambio de cada pieza')]
    mq = ''.join(f'<span data-i18n="{k}">{t}</span>' for k, t in mq_words) * 2
    feats = [
        ('01', 'why.2t', 'Aluminio que no se oxida', 'why.2p', 'Perfiles de aluminio 6063 T5 anodizado. Aguantan sol, lluvia, salitre y humedad sin pintura que se descascarille.', 'detalle-union.jpg', 'Unión de la estructura de aluminio anodizado', ''),
        ('02', 'why.3t', 'Lona ignífuga certificada', 'why.3p', 'Poliéster de 420 g/m² con recubrimiento de PVC. Impermeable y con certificación T2 según la norma UNE-EN 15619.', 'detalle-lona.jpg', 'Gotas de agua sobre la lona azul de una carpa', ' flip'),
        ('03', 'why.4t', 'Se monta en minutos', 'why.4p', 'Estructura de tijera tipo acordeón: se despliega, se fija la altura y lista. Sin herramientas.', 'montaje-campo.jpg', 'Dos personas desplegando una carpa plegable', ''),
        ('04', 'why.5t', 'Recambio de cada pieza', 'why.5p', 'Si se rompe una junta o un pie, cambias esa pieza y no la carpa. Todas tienen referencia y se venden por separado.', 'taller-perfiles.jpg', 'Montaje de la estructura de tijera en el taller', ' flip'),
    ]
    feat_html = ''
    for n, tk, t, pk, p, img, alt, flip in feats:
        link = f'<a class="link-arrow" href="okatent-recambios.html"><span data-i18n="shop.rec.cta">Ver recambios</span>{ARROW}</a>' if n == '04' else ''
        feat_html += f'''
          <div class="feature{flip} rv">
            <div class="feature-copy"><span class="mono">{n}</span><h3 class="h3" data-i18n="{tk}">{t}</h3><p data-i18n="{pk}">{p}</p>{link}</div>
            <figure><img src="{W}{img}" alt="{alt}" loading="lazy"></figure>
          </div>'''
    tiles = [('mercado', 'u1t', 'Mercados y ferias', 'u1p', 'Montaje y desmontaje cada semana, con sol o con lluvia.'),
             ('deporte', 'u2t', 'Eventos deportivos', 'u2p', 'Salidas, metas, avituallamientos y zonas de organización.'),
             ('hosteleria', 'u3t', 'Hostelería y street food', 'u3p', 'Terrazas, barras y puestos de comida en festivales.'),
             ('empresa', 'u4t', 'Eventos de empresa', 'u4p', 'Carpas unidas con paredes para acoger a tus invitados.')]
    tiles_html = ''.join(f'''
          <a class="tile rv" href="okatent-casos.html"><img src="imgs/usos/{i}.jpg" alt="" loading="lazy"><div class="tile-body"><h3 data-i18n="{tk}">{t}</h3><p data-i18n="{pk}">{p}</p></div></a>''' for i, tk, t, pk, p in tiles)

    body = header() + f'''
  <main>
    <section class="hero" aria-labelledby="hero-title">
      <div class="hero-in">
        <div class="hero-img"><img src="{W}hero-montserrat.jpg" alt="Tres carpas plegables Okatent azules frente a la montaña de Montserrat" fetchpriority="high"></div>
        <div class="wrap">
          <h1 id="hero-title"><span class="kicker" data-i18n="v2.kicker">Carpas plegables profesionales · Fabricadas en Barcelona</span><span data-i18n="v2.h1">Hechas para durar.</span></h1>
          <div class="hero-foot">
            <div>
              <p class="hero-sub" data-i18n="hero.sub">Estructura de aluminio anodizado que no se oxida, lona ignífuga certificada y recambio de cada pieza. La montas en minutos y sin herramientas.</p>
              <p class="hero-stats"><span><b>+20</b> <span data-i18n="v2.hs1">años fabricando</span></span><span><b>10</b> <span data-i18n="v2.hs2">medidas</span></span><span><b>13</b> <span data-i18n="v2.hs3">colores</span></span><span><b>T2</b> UNE-EN 15619</span></p>
            </div>
            <div class="btn-row">
              <a href="okatent-contacto.html" class="btn btn-white"><span data-i18n="hero.cta1">Pedir presupuesto</span>{ARROW}</a>
              <a href="#sala-3d" class="btn btn-light" data-i18n="cp.cta3d">Pruébala en 3D</a>
            </div>
          </div>
        </div>
      </div>
    </section>
{LOGOS}
    <section class="sec" aria-labelledby="st-title">
      <div class="wrap">
        <span class="eyebrow rv" data-i18n="v2.st.eyebrow">El taller</span>
        <p class="statement rv" id="st-title" data-i18n="v2.st">Fabricamos carpas plegables en Olesa de Montserrat desde hace más de 20 años. <span class="dim">Del perfil de aluminio a la última costura, todo pasa por nuestro taller. Por eso podemos venderte cada pieza por separado.</span></p>
        <div class="duo">
          <figure class="quote-card rv">
            <span class="bars" aria-hidden="true"></span>
            <blockquote><p data-i18n="v2.qc">«Una carpa buena no es la que aguanta un evento. Es la que se monta igual el quinto año.»</p></blockquote>
            <figcaption><cite><span data-i18n="v2.qc.who">El equipo del taller</span><small>Okatent · Olesa de Montserrat</small></cite></figcaption>
          </figure>
          <div class="photo-marquee rv">
            <img src="{W}taller-costura.jpg" alt="Costura de la lona de una carpa en el taller de Okatent" loading="lazy">
            <div class="marquee" aria-hidden="true"><div class="marquee-track">{mq}</div></div>
          </div>
        </div>
      </div>
    </section>

    <section class="sec sec-alt" id="modelos" aria-labelledby="mod-title">
      <div class="wrap">
        <div class="sec-head center rv">
          <span class="eyebrow" data-i18n="mod.eyebrow">Nuestras carpas</span>
          <h2 class="h2" id="mod-title" data-i18n="v2.mod.h2">Una carpa para cada ritmo.</h2>
          <p class="lead" data-i18n="mod.sub">Las dos tienen estructura de aluminio y se fabrican en nuestro taller. Cambian el perfil, la certificación y las medidas disponibles.</p>
        </div>
{models_block()}
      </div>
    </section>

    <section class="sec" id="sala-3d" aria-labelledby="sr-title">
      <div class="wrap">
        <div class="head-row rv">
          <div class="sec-head">
            <span class="eyebrow" data-i18n="nav.config">Configurador 3D</span>
            <h2 class="h2" id="sr-title" data-i18n="v2.sr.h2">Gírala y cámbiale el color. <span class="dim">Antes de pedirla.</span></h2>
          </div>
          <p class="lead" style="margin-top:0;max-width:26rem" data-i18n="v2.sr.p">Es la Cebú 3×3 en 3D, no una foto. Arrástrala para verla por todos los lados y prueba los 12 colores de lona.</p>
        </div>
        <div class="showroom rv">
          <div class="stage3d" id="home-stage" role="img" aria-label="Carpa Cebú 3×3 en 3D">
            <div class="stage3d-loading"><span data-i18n="vw.loading">Cargando modelo 3D…</span></div>
          </div>
          <div class="showroom-top">
            <div class="showroom-name"><b>Cebú 3×3</b><small data-i18n="v2.sr.model">Modelo 3D orientativo</small></div>
            <button class="stage3d-btn" id="home-reset" type="button">{RESET}<span data-i18n="vw.reset">Centrar</span></button>
          </div>
          <div class="showroom-bar">
            <span class="color-label" id="home-color">Azul</span>
            <div class="swatches" id="home-swatches"></div>
            <a class="btn btn-white" id="home-full" href="okatent-configurador.html"><span data-i18n="v2.sr.cta">Añadir paredes</span>{ARROW}</a>
          </div>
        </div>
      </div>
    </section>

    <section class="sec grid-bg" aria-labelledby="ft-title">
      <div class="wrap">
        <div class="sec-head center rv">
          <span class="eyebrow" data-i18n="why.eyebrow">Por qué Okatent</span>
          <h2 class="h2" id="ft-title" data-i18n="v2.feat.h2">Diseñada para resistir. <span class="dim">Pensada para repararse.</span></h2>
        </div>
        <div class="features">{feat_html}
        </div>
      </div>
    </section>

    <section class="sec" aria-labelledby="uses-title">
      <div class="wrap">
        <div class="head-row rv">
          <div class="sec-head">
            <span class="eyebrow" data-i18n="uses.eyebrow">Dónde se usan</span>
            <h2 class="h2" id="uses-title" data-i18n="uses.h2">Pensadas para trabajar al aire libre</h2>
          </div>
        </div>
        <div class="tiles">{tiles_html}
        </div>
      </div>
    </section>

    <section class="sec sec-alt" aria-labelledby="cases-title">
      <div class="wrap">
        <div class="head-row rv">
          <div class="sec-head">
            <span class="eyebrow" data-i18n="cases.eyebrow">Casos de éxito</span>
            <h2 class="h2" id="cases-title" data-i18n="v2.cases.h2">Clientes que la montan cada semana.</h2>
          </div>
          <a class="link-arrow" href="okatent-casos.html"><span data-i18n="cases.all">Ver todos los casos</span>{ARROW}</a>
        </div>
        <div class="stories">{story(CASES[0], True)}{story(CASES[1])}{story(CASES[2])}{story(CASES[3])}{story(CASES[4])}
        </div>
      </div>
    </section>

    <section class="sec" aria-labelledby="rev-title">
      <div class="wrap">
        <div class="sec-head center rv">
          <span class="eyebrow" data-i18n="reviews.eyebrow">Opiniones</span>
          <h2 class="h2" id="rev-title" data-i18n="reviews.h2">Lo que dicen quienes ya la usan</h2>
        </div>
        {quotes_block()}
      </div>
    </section>

    <section class="sec-tight" aria-labelledby="band-title">
      <div class="wrap">
        <div class="band rv">
          <div class="band-copy">
            <div>
              <span class="eyebrow" data-i18n="pers.eyebrow">Personalización</span>
              <h2 class="h2" id="band-title" data-i18n="v2.band.h2">Tu marca, a tres metros de altura.</h2>
              <p data-i18n="v2.band.p">Imprimimos tu logotipo o un diseño completo en el techo, los faldones y las paredes. Antes de imprimir, te enviamos un boceto para que lo apruebes.</p>
              <ul class="band-list">
                <li>{CHECK}<span data-i18n="pers.li1">Logotipo, texto o diseño a todo color</span></li>
                <li>{CHECK}<span data-i18n="pers.li2">En techo, faldones y paredes</span></li>
                <li>{CHECK}<span data-i18n="v2.band.li3">Desde una sola carpa</span></li>
              </ul>
            </div>
            <div class="btn-row"><a href="okatent-personalizacion.html" class="btn btn-white"><span data-i18n="do.2l">Ver personalización</span>{ARROW}</a></div>
          </div>
          <div class="band-media">
            <img src="{W}caso-nomada.jpg" alt="Carpa naranja totalmente personalizada con una marca de café" loading="lazy">
            <img src="{W}taller-impresion.jpg" alt="Impresión de una lona personalizada" loading="lazy">
            <img src="imgs/proceso-carpa-cliente.jpg" alt="Carpa personalizada de El Capricho de Gaudí" loading="lazy" style="object-position:50% 45%">
          </div>
        </div>
      </div>
    </section>

    <section class="sec" aria-labelledby="acc-title">
      <div class="wrap">
        <div class="head-row rv">
          <div class="sec-head">
            <span class="eyebrow" data-i18n="acc.eyebrow">Accesorios</span>
            <h2 class="h2" id="acc-title" data-i18n="v2.acc.h2">Si algo se rompe, cambias la pieza. <span class="dim">No la carpa.</span></h2>
          </div>
        </div>
{SHOP_CARDS}
      </div>
    </section>
{cta_band()}
  </main>
''' + footer() + scripts('inicio', after=THREE_LIBS + '  <script src="js/inicio.js"></script>\n')
    return h + body


# =====================================================================
# CARPAS PLEGABLES
# =====================================================================
def page_carpas():
    h = head('Carpas plegables Cebú y Borneo: modelos, medidas y colores | OKATENT',
             'Carpas plegables Cebú (gama profesional) y Borneo (gama de iniciación): estructura de aluminio, lona certificada T2, 10 medidas y 13 colores. Pruébala en 3D y pide presupuesto.')
    walls_select = lambda side, label_key, label: f'''<div class="side-field"><label for="side-{side}" data-i18n="{label_key}">{label}</label><select class="select" id="side-{side}" data-side="{side}"></select></div>'''
    steps = [('01', 'q.1t', 'Perfiles de aluminio', 'q.1p', 'Perfiles extruidos en aluminio de alta resistencia: más ligero que el acero e igual de resistente.', 'taller-perfiles.jpg'),
             ('02', 'q.2t', 'Anodizado', 'q.2p', 'Un baño que protege el aluminio del sol, la lluvia, la sal y la humedad. Sin pintura que se descascarille.', 'detalle-union.jpg'),
             ('03', 'q.3t', 'Corte y confección', 'q.3p', 'La lona se corta y se cose a mano en nuestro taller de Olesa de Montserrat.', 'taller-costura.jpg'),
             ('04', 'q.4t', 'Control de calidad', 'q.4p', 'Revisamos cada carpa antes de que salga del taller. Si no pasa todos los controles, no sale.', 'taller-control.jpg')]
    steps_html = ''.join(f'''
          <li class="step rv"><figure><img src="{W}{img}" alt="" loading="lazy"></figure><span class="step-n">{n}</span><h3 data-i18n="{tk}">{t}</h3><p data-i18n="{pk}">{p}</p></li>''' for n, tk, t, pk, p, img in steps)
    spec_rows = [('sp.1', 'Estructura', 'spv.1', 'Aluminio 6063 T5 extruido', False), ('sp.2', 'Acabado', 'spv.2', 'Anodizado', False),
                 ('sp.3', 'Lona', 'spv.3', 'Poliéster 420 g/m² con recubrimiento de PVC', False), ('sp.4', 'Propiedades', 'spv.4', 'Impermeable e ignífuga', False),
                 ('sp.5', 'Certificación', None, 'T2 · UNE-EN 15619', False), ('sp.9', 'Resistencia al viento', 'v2.wind', 'Rachas de hasta 50 km/h, con pesos de 10 kg por pata', True),
                 ('sp.6', 'Montaje', 'spv.6', 'Sin herramientas', False), ('sp.7', 'Colores', None, '13', False),
                 ('v2.sp.war', 'Garantía', 'v2.war', '3 años en estructura y lona', True), ('sp.8', 'Fabricación', 'spv.8', 'Olesa de Montserrat (Barcelona)', False)]
    spec_html = ''.join(f'''
              <div{' data-demo' if demo else ''}><dt data-i18n="{dk}">{dt}</dt><dd{f' data-i18n="{vk}"' if vk else ''}>{v}</dd></div>''' for dk, dt, vk, v, demo in spec_rows)

    body = header('carpas') + page_head([('Carpas plegables', 'nav.carpas')], 'cp.h1', 'Carpas plegables Cebú y Borneo', 'cp.lead',
        'Dos modelos con estructura de aluminio, fabricados en nuestro taller de Olesa de Montserrat. Elige según cuánto la vayas a usar, pruébala en 3D y pide presupuesto.',
        buttons=f'<a href="okatent-contacto.html" class="btn btn-primary"><span data-i18n="nav.cta">Pedir presupuesto</span>{ARROW}</a><a href="#visor" class="btn btn-line" data-i18n="cp.cta3d">Pruébala en 3D</a>',
        media=W + 'hero-montserrat.jpg', media_alt='Carpas plegables Okatent Cebú azules frente a Montserrat', media_pos='60% 60%') + subnav([
        ('modelos', 'tab.modelos', 'Modelos'), ('visor', 'vw.eyebrow', 'Colores y paredes'), ('medidas', 'tab.medidas', 'Medidas'),
        ('calidad', 'tab.calidad', 'Calidad'), ('accesorios', 'nav.accesorios', 'Accesorios'), ('preguntas', 'tab.faq', 'Preguntas')]) + f'''
  <main>
    <section class="sec" id="modelos" aria-labelledby="mod-title" style="padding-top:clamp(3rem,6vw,6rem)">
      <div class="wrap">
        <div class="sec-head center rv">
          <span class="eyebrow" data-i18n="mod.eyebrow">Nuestras carpas</span>
          <h2 class="h2" id="mod-title" data-i18n="v2.mod.h2">Una carpa para cada ritmo.</h2>
          <p class="lead" data-i18n="mod.sub">Las dos tienen estructura de aluminio y se fabrican en nuestro taller. Cambian el perfil, la certificación y las medidas disponibles.</p>
        </div>
{models_block()}
        <div class="compare rv">
          <h3 data-i18n="cmp.h3">Cebú o Borneo, de un vistazo</h3>
          <div class="table-wrap">
            <table>
              <thead><tr><th></th><th>Cebú</th><th>Borneo</th></tr></thead>
              <tbody>
                <tr><td data-i18n="cmp.use">Uso recomendado</td><td data-i18n="cmp.use.c">Profesional e intensivo</td><td data-i18n="cmp.use.b">Ocasional</td></tr>
                <tr><td data-i18n="sp.1">Estructura</td><td data-i18n="cebu.li1">Aluminio 6063 T5 anodizado, de mayor sección</td><td data-i18n="v2.ms.b1">Aluminio, perfil más ligero</td></tr>
                <tr><td data-i18n="cmp.cert">Lona</td><td data-i18n="cebu.li3">Certificación T2 según UNE-EN 15619</td><td data-i18n="v2.ms.b2">Poliéster impermeable</td></tr>
                <tr><td data-i18n="cmp.sizes">Medidas</td><td data-i18n="cmp.sizes.c">10, de 2×2 a 4×8 m</td><td data-demo data-i18n="v2.ms.b3">3×3, 3×4,5 y 3×6 m</td></tr>
                <tr><td data-i18n="nav.rec">Recambios</td><td data-i18n="cmp.spares.v">Con referencia, por separado</td><td data-i18n="cmp.spares.v">Con referencia, por separado</td></tr>
                <tr data-demo><td data-i18n="cmp.price">Precio</td><td data-i18n="v2.price.c">Desde 890 € + IVA (3×3)</td><td data-i18n="v2.price.b">Desde 590 € + IVA (3×3)</td></tr>
              </tbody>
            </table>
          </div>
        </div>
      </div>
    </section>

    <section class="sec sec-alt" id="visor" aria-labelledby="vw-title">
      <div class="wrap viewer">
        <div class="stage3d rv" id="stage" role="img" aria-label="Carpa Cebú 3×3 en 3D">
          <div class="stage3d-loading"><span data-i18n="vw.loading">Cargando modelo 3D…</span></div>
          <div class="stage3d-bar">
            <span class="stage3d-hint">{DRAG}<span data-i18n="vw.drag">Arrastra para girar</span></span>
            <button class="stage3d-btn" id="stage-reset" type="button">{RESET}<span data-i18n="vw.reset">Centrar</span></button>
          </div>
        </div>
        <div class="rv">
          <span class="eyebrow" data-i18n="vw.eyebrow">Colores y paredes</span>
          <h2 class="h2" id="vw-title" style="font-size:clamp(2.2rem,3.8vw,4rem)" data-i18n="v2.vw.h2">Hazla tuya.</h2>
          <p class="lead" data-i18n="vw.sub3">Modelo 3D orientativo de la Cebú 3×3. Arrástrala para girarla y acércate con la rueda o con dos dedos.</p>
          <div style="margin-top:2rem">
            <div class="ctrl">
              <div class="ctrl-label"><span data-i18n="vw.color">Color de la lona</span><em id="color-name">Azul</em></div>
              <div class="swatches" id="swatches"></div>
              <p class="ctrl-note" data-i18n="vw.colornote">También en lona transparente.</p>
            </div>
            <div class="ctrl">
              <div class="ctrl-label"><span data-i18n="vw.walls">Paredes</span></div>
              <div class="sides">
                {walls_select('back', 'vw.side.back', 'Fondo')}
                {walls_select('left', 'vw.side.left', 'Izquierda')}
                {walls_select('right', 'vw.side.right', 'Derecha')}
                {walls_select('front', 'vw.side.front', 'Frente')}
              </div>
            </div>
            <div class="ctrl" style="border-bottom:1px solid var(--line);margin-bottom:1.4rem">
              <div class="toggle-row"><span><span data-i18n="vw.awning">Visera frontal</span><small data-i18n="vw.awning.sub">Alarga la cubierta por delante</small></span><button class="toggle" id="awning" type="button" role="switch" aria-checked="false" aria-label="Visera frontal" data-i18n-aria="vw.awning"></button></div>
            </div>
          </div>
          <p class="mono" style="color:var(--muted);margin-bottom:.5rem" data-i18n="v2.yourcfg">Tu configuración</p>
          <p class="viewer-summary" id="viewer-summary">Cebú 3×3</p>
          <div class="btn-row">
            <a href="okatent-contacto.html" class="btn btn-primary" id="viewer-quote"><span data-i18n="vw.cta1">Pedir presupuesto de esta carpa</span>{ARROW}</a>
            <a href="okatent-configurador.html" class="btn btn-line" id="viewer-full">{EXPAND}<span data-i18n="vw.full">Pantalla completa</span></a>
          </div>
        </div>
      </div>
    </section>

    <section class="sec grid-bg" id="medidas" aria-labelledby="spec-title">
      <div class="wrap spec">
        <div class="rv">
          <span class="eyebrow" data-i18n="spec.eyebrow">Ficha técnica</span>
          <h2 class="h2" id="spec-title" data-i18n="spec.h2">Cebú, en números</h2>
          <dl class="spec-rows" style="margin-top:2.5rem">{spec_html}
          </dl>
        </div>
        <div class="rv">
          <div class="table-wrap">
            <table class="sizes-table">
              <thead><tr><th data-i18n="t.medida">Medida</th><th data-i18n="t.sup">Superficie</th><th data-i18n="t.est">Estructura</th><th data-i18n="t.techo">Techo</th></tr></thead>
              <tbody id="size-rows"></tbody>
            </table>
          </div>
          <p class="table-note" data-i18n="spec.note">Pesos aproximados en kg.</p>
        </div>
      </div>
    </section>

    <section class="sec" id="calidad" aria-labelledby="q-title">
      <div class="wrap">
        <div class="head-row rv">
          <div class="sec-head">
            <span class="eyebrow" data-i18n="q.eyebrow">Calidad</span>
            <h2 class="h2" id="q-title" data-i18n="q.h2">Así fabricamos cada carpa</h2>
          </div>
          <a class="link-arrow" href="okatent-empresa.html"><span data-i18n="q.link">Conoce la empresa</span>{ARROW}</a>
        </div>
        <ol class="steps">{steps_html}
        </ol>
      </div>
    </section>

    <section class="sec sec-alt" id="accesorios" aria-labelledby="acc-title">
      <div class="wrap">
        <div class="head-row rv">
          <div class="sec-head">
            <span class="eyebrow" data-i18n="acc.eyebrow">Accesorios</span>
            <h2 class="h2" id="acc-title" data-i18n="v2.acc.h2">Si algo se rompe, cambias la pieza. <span class="dim">No la carpa.</span></h2>
          </div>
        </div>
{SHOP_CARDS}
      </div>
    </section>

    <section class="sec" id="preguntas" aria-labelledby="faq-title">
      <div class="wrap faq">
        <div class="rv">
          <span class="eyebrow" data-i18n="faq.eyebrow">Preguntas frecuentes</span>
          <h2 class="h2" id="faq-title" data-i18n="faq.h2">Lo que más nos preguntan</h2>
        </div>
        <div class="faq-list rv">
          {faq(PRODUCT_FAQ)}
        </div>
      </div>
    </section>
{cta_band()}
  </main>
''' + footer() + scripts('carpas', after=THREE_LIBS + '  <script src="js/carpas.js"></script>\n')
    return h + body


# =====================================================================
# PERSONALIZACIÓN
# =====================================================================
def page_personalizacion():
    h = head('Carpas plegables personalizadas con tu logotipo | OKATENT',
             'Carpas plegables personalizadas: imprimimos tu logotipo o un diseño completo en el techo, los faldones y las paredes de una carpa profesional Okatent.')
    zones = [('01', 'pz.z1t', 'Techo', 'pz.z1p', 'Logotipo o diseño completo en el techo, para que la carpa se reconozca desde lejos.', 'caso-nomada.jpg'),
             ('02', 'pz.z2t', 'Faldones', 'pz.z2p', 'La franja que rodea el techo, a la altura de la vista. El sitio habitual para el nombre de la marca.', 'caso-brasa.jpg'),
             ('03', 'pz.z3t', 'Paredes', 'pz.z3p', 'Paredes impresas a todo color para el fondo del stand, un photocall o información de producto.', 'caso-fira.jpg')]
    zones_html = ''.join(f'''
          <div class="card rv"><figure><img src="{W}{img}" alt="" loading="lazy"></figure><span class="card-n">{n}</span><h3 data-i18n="{tk}">{t}</h3><p data-i18n="{pk}">{p}</p></div>''' for n, tk, t, pk, p, img in zones)
    steps = [('01', 'pz.s1t', 'Envíanos tu diseño', 'pz.s1p', 'Tu logotipo o tu diseño, la medida y cuántas carpas necesitas, por el formulario o por WhatsApp.', False),
             ('02', 's2t', 'Recibe tu presupuesto', 'pz.s2p', 'Te respondemos en menos de 48 horas laborables.', False),
             ('03', 'pz.s3t', 'Validamos el diseño', 'v2.pz.s3p', 'Te enviamos un boceto con tu diseño sobre la carpa. Imprimimos cuando nos das el visto bueno.', True),
             ('04', 'pz.s4t', 'Impresión y envío', 'v2.pz.s4p', 'Entre 10 y 15 días laborables desde que apruebas el boceto, más 3–5 días de envío a la península.', True)]
    steps_html = ''.join(f'''
          <li class="step rv"{' data-demo' if d else ''}><span class="step-n">{n}</span><h3 data-i18n="{tk}">{t}</h3><p data-i18n="{pk}">{p}</p></li>''' for n, tk, t, pk, p, d in steps)
    body = header('personal') + page_head([('Personalización', 'nav.personal')], 'pz.h1', 'Carpas plegables personalizadas con tu marca', 'pz.lead',
        'Imprimimos tu logotipo, tus colores o un diseño completo sobre la misma carpa profesional. Tu marca, a la vista en cada feria, cada partido y cada evento.',
        buttons=f'<a href="okatent-contacto.html?logo=1&amp;use=marca" class="btn btn-primary"><span data-i18n="pers.cta">Pedir presupuesto con mi logo</span>{ARROW}</a>',
        media='imgs/proceso-carpa-cliente.jpg', media_alt='Carpa plegable Okatent 3×6 totalmente personalizada con paredes impresas', media_pos='50% 42%',
        caption='El Capricho de Gaudí · Comillas') + f'''
  <main>
    <section class="sec" aria-labelledby="zones-title">
      <div class="wrap">
        <div class="sec-head center rv">
          <span class="eyebrow" data-i18n="pz.zones.eyebrow">Qué se puede imprimir</span>
          <h2 class="h2" id="zones-title" data-i18n="pz.zones.h2">Tres zonas para tu marca</h2>
        </div>
        <div class="cards3">{zones_html}
        </div>
      </div>
    </section>

    <section class="sec-tight grid-bg" aria-labelledby="sub-title">
      <div class="wrap">
        <div class="feature rv" data-demo>
          <div class="feature-copy"><span class="mono" data-i18n="v2.sub.eyebrow">Cómo imprimimos</span><h2 class="h3" id="sub-title" data-i18n="v2.sub.h3">La tinta entra en el tejido. No se cuartea ni se despega.</h2><p data-i18n="v2.sub.p">Imprimimos por sublimación sobre la misma lona de la carpa: los colores aguantan el sol y el uso, y la lona sigue siendo impermeable e ignífuga.</p></div>
          <figure><img src="{W}taller-impresion.jpg" alt="Impresora de gran formato imprimiendo una lona personalizada" loading="lazy"></figure>
        </div>
      </div>
    </section>

    <section class="sec" aria-labelledby="gal-title">
      <div class="wrap">
        <div class="head-row rv">
          <div class="sec-head">
            <span class="eyebrow" data-i18n="pz.gal.eyebrow">Trabajos</span>
            <h2 class="h2" id="gal-title" data-i18n="pz.gal.h2">Carpas que ya llevan la marca de su cliente</h2>
          </div>
          <a class="link-arrow" href="okatent-casos.html"><span data-i18n="cases.all">Ver todos los casos</span>{ARROW}</a>
        </div>
        <div class="gallery rv">
          <figure class="wide"><img src="imgs/carpas-clientes.webp" alt="Carpas rotuladas con marcas de clientes" loading="lazy" style="object-position:30% 50%"><figcaption>Playitas · Ciutat de les Arts i les Ciències</figcaption></figure>
          <figure><img src="{W}caso-club.jpg" alt="Carpas verdes de un club de fútbol" loading="lazy"><figcaption>CE La Riera</figcaption></figure>
          <figure><img src="{W}caso-trail.jpg" alt="Carpas rojas de una carrera de montaña" loading="lazy"><figcaption>Trail Serralada 42K</figcaption></figure>
          <figure class="wide"><img src="imgs/carpas-clientes.webp" alt="Carpas rotuladas de marcas del motor" loading="lazy" style="object-position:88% 50%"><figcaption>Maquina Motors · Billy Bulldog</figcaption></figure>
        </div>
      </div>
    </section>

    <section class="sec sec-alt" aria-labelledby="pzs-title">
      <div class="wrap">
        <div class="sec-head rv">
          <span class="eyebrow" data-i18n="pz.steps.eyebrow">Cómo se pide</span>
          <h2 class="h2" id="pzs-title" data-i18n="pz.steps.h2">Tu carpa personalizada, paso a paso</h2>
        </div>
        <ol class="steps plain">{steps_html}
        </ol>
      </div>
    </section>

    <section class="sec" aria-labelledby="pzfaq-title">
      <div class="wrap faq">
        <div class="rv">
          <span class="eyebrow" data-i18n="faq.eyebrow">Preguntas frecuentes</span>
          <h2 class="h2" id="pzfaq-title" data-i18n="pz.faq.h2">Dudas sobre la personalización</h2>
        </div>
        <div class="faq-list rv">
          {faq([('pz.q1', '¿En qué formato envío el logotipo?', 'v2.pz.a1', 'Mejor en vectorial (AI, PDF o SVG). Si no lo tienes, un PNG a 300 ppp; si hace falta, lo redibujamos nosotros.', True),
                ('pz.q2', '¿Hay un pedido mínimo?', 'v2.pz.a2', 'No. Personalizamos desde una sola carpa.', True),
                ('pz.q3', '¿Aguanta la impresión el uso diario?', 'v2.pz.a3', 'Sí. Imprimimos por sublimación: la tinta forma parte del tejido, así que no se cuartea ni se despega al plegar la carpa.', True),
                ('q5', '¿Se pueden unir varias carpas?', 'a5', 'Sí. Con abrazaderas de unión y canal de desagüe se unen lado con lado para cubrir espacios grandes en ferias y eventos.', False)])}
        </div>
      </div>
    </section>
{cta_band('pz.cta.h2', '¿Tienes el logotipo a mano?', 'pz.cta.p', 'Envíanoslo con la medida que necesitas y te preparamos el presupuesto.', 'okatent-contacto.html?logo=1&amp;use=marca', W + 'caso-nomada.jpg')}
  </main>
''' + footer() + scripts('personalizacion')
    return h + body


# =====================================================================
# CASOS
# =====================================================================
def page_casos():
    h = head('Casos de éxito: carpas plegables Okatent en uso | OKATENT',
             'Clientes que trabajan con carpas plegables Okatent: qué necesitaban, qué carpa elegimos con ellos y qué han conseguido.')
    body = header('casos') + page_head([('Casos', 'nav.casos')], 'v2.cases.h2', 'Clientes que la montan cada semana.', 'cases.lead',
        'Qué necesitaban, qué hicimos y qué han conseguido.') + LOGOS + f'''
  <main>
    <section class="sec" aria-label="Resumen de casos">
      <div class="wrap">
        <div class="stories">{story(CASES[0], True)}{''.join(story(c) for c in CASES[1:6])}{story(CASES[6], True, True)}
        </div>
      </div>
    </section>

    <section class="sec sec-alt" aria-label="Casos en detalle">
      <div class="wrap">
        <div class="case-rows">{''.join(case_row(c) for c in CASES)}
        </div>
      </div>
    </section>

    <section class="sec" aria-labelledby="rev-title">
      <div class="wrap">
        <div class="sec-head center rv">
          <span class="eyebrow" data-i18n="reviews.eyebrow">Opiniones</span>
          <h2 class="h2" id="rev-title" data-i18n="reviews.h2">Lo que dicen quienes ya la usan</h2>
        </div>
        {quotes_block()}
      </div>
    </section>
{cta_band('cs.cta.h2', '¿Tienes un proyecto parecido?', 'cs.cta.p', 'Cuéntanos qué necesitas y te decimos qué carpa encaja.', img=W + 'caso-masia.jpg')}
  </main>
''' + footer() + scripts('casos')
    return h + body


# =====================================================================
# EMPRESA
# =====================================================================
def page_empresa():
    h = head('Empresa: fabricantes de carpas plegables en Olesa de Montserrat | OKATENT',
             'Okatent fabrica carpas plegables en Olesa de Montserrat (Barcelona) desde hace más de 20 años: perfiles de aluminio, lona cosida en nuestro taller y certificación T2.')
    how = [('why.1t', 'Fabricamos, no revendemos', 'why.1p', 'La estructura, la lona y el montaje salen de nuestro taller de Olesa de Montserrat. Controlamos cada pieza porque la hacemos nosotros.'),
           ('v2.how2t', 'Un interlocutor de principio a fin', 'v2.how2p', 'La misma persona te prepara el presupuesto, sigue la fabricación y te avisa del envío.'),
           ('why.5t', 'Recambio de cada pieza', 'why.5p', 'Si se rompe una junta o un pie, cambias esa pieza y no la carpa. Todas tienen referencia y se venden por separado.'),
           ('v2.how4t', 'Envíos a toda España y Francia', 'v2.how4p', '3–5 días laborables a la península. Para otros destinos, consúltanos.')]
    how_html = ''.join(f'''
            <div><h3 data-i18n="{tk}">{t}</h3><p data-i18n="{pk}">{p}</p></div>''' for tk, t, pk, p in how)
    body = header('empresa') + page_head([('Empresa', 'nav.empresa')], 'v2.em.h1', 'Fabricantes, no revendedores.', 'v2.em.lead',
        'Fabricamos carpas plegables en Olesa de Montserrat desde hace más de 20 años. Desde el perfil de aluminio hasta la costura de la lona, todo pasa por nuestro taller.',
        media=W + 'equipo.jpg', media_alt='El equipo de Okatent en el taller de Olesa de Montserrat', media_pos='50% 55%') + f'''
  <main>
    <section class="sec" aria-labelledby="story-title">
      <div class="wrap split">
        <div class="rv">
          <span class="eyebrow" data-i18n="em.story.eyebrow">Quiénes somos</span>
          <h2 class="h2" id="story-title" data-i18n="em.story.h2">Especialistas en estructuras plegables</h2>
        </div>
        <div class="prose rv">
          <p data-i18n="em.p1">Nuestra especialidad son las carpas portátiles y desmontables, pensadas para aguantar el ritmo profesional: una feria cada semana, un mercado o un evento al aire libre.</p>
          <p data-i18n="em.p2">Fabricamos dos modelos, Cebú y Borneo, y acompañamos a cada cliente desde la primera consulta hasta la instalación. Enviamos a toda España, a Francia y a otros países.</p>
          <p data-i18n="em.p3">Además de carpas plegables, fabricamos pabellones modulares para pistas de pádel, naves industriales y otras superficies.</p>
          <p style="margin-top:1.6rem"><a class="link-arrow" href="https://okatent.com" target="_blank" rel="noopener"><span data-i18n="em.p3.link">Ver pabellones modulares</span>{ARROW}</a></p>
        </div>
      </div>
      <div class="wrap" style="margin-top:clamp(3.5rem,7vw,6rem)">
        <div class="stats rv">
          <div class="stat"><b>+20</b><span data-i18n="stat.1">años fabricando carpas</span></div>
          <div class="stat"><b>2</b><span data-i18n="em.stat.2">modelos de carpa plegable</span></div>
          <div class="stat"><b>T2</b><span data-i18n="stat.4">lona certificada UNE-EN 15619</span></div>
          <div class="stat"><b>ES · FR</b><span data-i18n="em.stat.4">y envíos internacionales</span></div>
        </div>
      </div>
    </section>

    <section class="sec sec-alt" aria-labelledby="taller-title">
      <div class="wrap">
        <div class="head-row rv">
          <div class="sec-head">
            <span class="eyebrow" data-i18n="em.taller.eyebrow">El taller</span>
            <h2 class="h2" id="taller-title" data-i18n="em.taller.h2">Donde se hace cada carpa</h2>
          </div>
          <p class="lead" style="margin-top:0;max-width:28rem" data-i18n="em.taller.p">En nuestro taller fabricamos los perfiles, los anodizamos, cortamos y cosemos la lona y revisamos cada carpa antes de enviarla.</p>
        </div>
        <div class="gallery rv">
          <figure class="wide"><img src="{W}taller-costura.jpg" alt="Costura de la lona" loading="lazy"><figcaption data-i18n="q.3t">Corte y confección</figcaption></figure>
          <figure><img src="{W}taller-perfiles.jpg" alt="Perfiles de aluminio" loading="lazy"><figcaption data-i18n="q.1t">Perfiles de aluminio</figcaption></figure>
          <figure><img src="{W}taller-control.jpg" alt="Control de calidad de una carpa" loading="lazy"><figcaption data-i18n="q.4t">Control de calidad</figcaption></figure>
          <figure class="wide"><img src="{W}taller-impresion.jpg" alt="Impresión de lonas personalizadas" loading="lazy"><figcaption data-i18n="v2.cap.print">Impresión</figcaption></figure>
        </div>
      </div>
    </section>

    <section class="sec grid-bg" aria-labelledby="how-title">
      <div class="wrap spec-list">
        <h2 class="h2 rv" id="how-title" data-i18n="v2.how.h2">Cómo trabajamos</h2>
        <div class="spec-rows rv">{how_html}
        </div>
      </div>
    </section>

    <section class="sec" aria-label="Certificación y ubicación">
      <div class="wrap cards3" style="grid-template-columns:repeat(auto-fit,minmax(min(100%,22rem),1fr))">
        <div class="card rv">
          <span class="eyebrow" data-i18n="em.cert.eyebrow">Certificación</span>
          <h3 class="h3" data-i18n="em.cert.h2">Lona certificada T2</h3>
          <p data-i18n="em.cert.p">La lona de la Cebú tiene la certificación T2 según la norma UNE-EN 15619, emitida por el laboratorio APPLUS.</p>
        </div>
        <div class="card rv">
          <span class="eyebrow" data-i18n="em.loc.eyebrow">Dónde estamos</span>
          <h3 class="h3" data-i18n="em.loc.h2">Olesa de Montserrat, Barcelona</h3>
          <p data-i18n="em.loc.p">El taller está en el polígono Can Singla, a los pies de Montserrat.</p>
          <p style="margin-top:1.4rem"><a class="link-arrow" href="https://maps.google.com/?q=Okatent+Olesa+de+Montserrat" target="_blank" rel="noopener"><span data-i18n="em.loc.link">Cómo llegar</span>{ARROW}</a></p>
        </div>
      </div>
    </section>
{cta_band()}
  </main>
''' + footer() + scripts('empresa')
    return h + body


# =====================================================================
# CONTACTO
# =====================================================================
def page_contacto():
    h = head('Contacto y presupuesto | OKATENT',
             'Pide presupuesto de tu carpa plegable Okatent: te respondemos en menos de 48 horas laborables. Teléfono 93 323 19 74, WhatsApp e info@okatent.com.')
    body = header() + page_head([('Contacto', 'nav.contacto')], 'ct.h2', 'Pide tu presupuesto', 'ct.p',
        'Cuéntanos qué carpa necesitas y te respondemos en menos de 48 horas laborables. Si lo prefieres, llámanos o escríbenos por WhatsApp.') + f'''
  <main>
    <section class="sec" id="formulario" aria-label="Formulario de presupuesto" style="padding-top:clamp(1rem,2vw,2rem)">
      <div class="wrap contact">
        <div class="rv">
          <div class="contact-list">
            <a href="tel:+34933231974"><span class="contact-ico">{PHONE}</span><span><small data-i18n="ct.phone">Teléfono</small><b>93 323 19 74</b></span></a>
            <a href="https://wa.me/34933231974" target="_blank" rel="noopener"><span class="contact-ico">{CHAT}</span><span><small>WhatsApp</small><b>+34 933 231 974</b></span></a>
            <a href="mailto:info@okatent.com"><span class="contact-ico">{MAIL}</span><span><small data-i18n="ct.mail">Correo</small><b>info@okatent.com</b></span></a>
            <a href="https://maps.google.com/?q=Okatent+Olesa+de+Montserrat" target="_blank" rel="noopener"><span class="contact-ico">{PIN}</span><span><small data-i18n="ct.addr">Taller</small><b>Carrer dels Tintorers, Polígon Can Singla, 08640 Olesa de Montserrat</b></span></a>
            <div data-demo><span class="contact-ico">{CLOCK}</span><span><small data-i18n="ct.hours">Horario</small><b data-i18n="v2.hours">Lunes a viernes, de 8:00 a 17:00</b></span></div>
          </div>
          <div class="map"><iframe src="https://www.google.com/maps?q=Okatent%2C%20Pol%C3%ADgon%20Can%20Singla%2C%20Olesa%20de%20Montserrat&amp;output=embed" loading="lazy" referrerpolicy="no-referrer-when-downgrade" title="Mapa del taller de Okatent" data-i18n-aria="ct.map"></iframe></div>
        </div>

        <div class="form-card rv">
          <h2 data-i18n="f.h2">Solicitud de presupuesto</h2>
          <form id="quote-form" novalidate>
            <div class="form-grid">
              <div class="field"><label for="f-name"><span data-i18n="f.name">Nombre y apellidos</span> <span class="req">*</span></label><input id="f-name" name="name" autocomplete="name" required data-i18n-ph="f.name.ph" placeholder="Nombre completo"></div>
              <div class="field"><label for="f-company" data-i18n="f.company">Empresa (opcional)</label><input id="f-company" name="company" autocomplete="organization"></div>
              <div class="field"><label for="f-email"><span data-i18n="f.email">Correo electrónico</span> <span class="req">*</span></label><input id="f-email" name="email" type="email" autocomplete="email" required data-i18n-ph="f.email.ph" placeholder="nombre@empresa.com"></div>
              <div class="field"><label for="f-phone" data-i18n="f.phone">Teléfono</label><input id="f-phone" name="phone" type="tel" autocomplete="tel" data-i18n-ph="f.phone.ph" placeholder="600 000 000"></div>
              <div class="field"><label for="f-use" data-i18n="f.use">¿Para qué la vas a usar?</label>
                <select id="f-use" name="use">
                  <option value="" data-i18n="f.select">Selecciona</option>
                  <option value="mercado" data-i18n="use.mercado">Mercados y ferias</option>
                  <option value="deporte" data-i18n="use.deporte">Eventos deportivos</option>
                  <option value="hosteleria" data-i18n="use.hosteleria">Hostelería y street food</option>
                  <option value="empresa" data-i18n="use.empresa">Eventos de empresa</option>
                  <option value="marca" data-i18n="use.marca">Promoción de marca</option>
                  <option value="particular" data-i18n="use.particular">Uso particular</option>
                  <option value="otro" data-i18n="use.otro">Otro</option>
                </select>
              </div>
              <div class="field"><label for="f-qty" data-i18n="f.qty">Cantidad</label><input id="f-qty" name="qty" type="number" min="1" step="1" value="1" inputmode="numeric"></div>
              <div class="field"><label for="f-model" data-i18n="f.model">Modelo</label>
                <select id="f-model" name="model">
                  <option value="Cebú">Cebú</option>
                  <option value="Borneo">Borneo</option>
                  <option value="?" data-i18n="f.model.any">Todavía no lo sé</option>
                </select>
              </div>
              <div class="field"><label for="f-size" data-i18n="f.size">Medida</label><select id="f-size" name="size"><option value="" data-i18n="f.select">Selecciona</option></select></div>
              <div class="field full"><label for="f-color" data-i18n="f.color">Color</label><select id="f-color" name="color"><option value="" data-i18n="f.select">Selecciona</option></select></div>
              <label class="check"><input type="checkbox" id="f-logo" name="logo"><span data-i18n="f.logo">Quiero la carpa con mi logotipo</span></label>
              <div class="field full"><label for="f-msg" data-i18n="f.msg">Mensaje</label><textarea id="f-msg" name="message" data-i18n-ph="f.msg.ph" placeholder="Uso, cantidad, fecha en la que la necesitas…"></textarea></div>
            </div>
            <div class="form-actions">
              <button type="submit" class="btn btn-primary"><span data-i18n="f.send">Enviar solicitud</span>{ARROW}</button>
              <button type="button" class="btn btn-line" id="f-wa" data-i18n="f.wa">Enviar por WhatsApp</button>
            </div>
            <p class="form-msg" id="form-msg" role="status" hidden></p>
            <p class="form-privacy" data-i18n="f.privacy">OKATENT S.L. (CIF B-63802078) usará estos datos solo para responder a tu solicitud, de acuerdo con el RGPD.</p>
          </form>
        </div>
      </div>
    </section>

    <section class="sec sec-alt" aria-labelledby="steps-title">
      <div class="wrap">
        <div class="sec-head rv">
          <span class="eyebrow" data-i18n="steps.eyebrow">Cómo pedirla</span>
          <h2 class="h2" id="steps-title" data-i18n="steps.h2">Tu carpa, en cuatro pasos</h2>
        </div>
        <ol class="steps plain">
          <li class="step rv"><span class="step-n">01</span><h3 data-i18n="s1t">Elige</h3><p data-i18n="s1p">Modelo, medida, color y paredes. Pruébala en 3D en la página de carpas o cuéntanoslo por teléfono o WhatsApp.</p></li>
          <li class="step rv"><span class="step-n">02</span><h3 data-i18n="s2t">Recibe tu presupuesto</h3><p data-i18n="s2p">Te respondemos en menos de 48 horas laborables con el precio y el plazo.</p></li>
          <li class="step rv"><span class="step-n">03</span><h3 data-i18n="s3t">La preparamos</h3><p data-i18n="s3p">En nuestro taller, con tu impresión si la has pedido, y la revisamos antes de enviarla.</p></li>
          <li class="step rv"><span class="step-n">04</span><h3 data-i18n="s4t">Te llega</h3><p data-i18n="s4p">El envío tarda 3–5 días laborables a la península. Para Baleares, Canarias y fuera de España, consúltanos.</p></li>
        </ol>
      </div>
    </section>

    <section class="sec" aria-labelledby="cfaq-title">
      <div class="wrap faq">
        <div class="rv">
          <span class="eyebrow" data-i18n="faq.eyebrow">Preguntas frecuentes</span>
          <h2 class="h2" id="cfaq-title" data-i18n="faq.h2">Lo que más nos preguntan</h2>
        </div>
        <div class="faq-list rv">
          {faq([PRODUCT_FAQ[7], PRODUCT_FAQ[2], PRODUCT_FAQ[8], PRODUCT_FAQ[5]])}
        </div>
      </div>
    </section>
  </main>
''' + footer() + scripts('contacto', after='  <script src="js/contacto.js"></script>\n')
    return h + body

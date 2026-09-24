# OKATENT · web de carpas plegables (v2)

## Verla en local

Hace falta un servidor (abrir el HTML con doble clic no carga el 3D). Desde esta carpeta:

```
python -m http.server 5173
```

y abrir http://localhost:5173/okatent-carpas.html

## Páginas

| Archivo | Página |
|---|---|
| `okatent-carpas.html` | Inicio (`index.html` redirige aquí) |
| `okatent-carpas-plegables.html` | Modelos, visor 3D, ficha técnica, calidad y preguntas |
| `okatent-personalizacion.html` | Personalización |
| `okatent-complementos.html` · `okatent-recambios.html` | Tiendas |
| `okatent-casos.html` | Casos de éxito |
| `okatent-empresa.html` | Empresa |
| `okatent-contacto.html` | Formulario de presupuesto (abre el correo o WhatsApp) |
| `okatent-configurador.html` | Configurador 3D a pantalla completa |

`okatent-cebu.html`, `okatent-debug.html` y `okatent-visor360.html` son borradores anteriores, sin tocar.
Los archivos originales del proyecto están en `_original/`.

## ⚠️ Contenido de ejemplo: cambiar antes de publicar

Todo lo inventado está marcado en el HTML con el atributo `data-demo` (buscar `data-demo`):

- Los 7 casos y las 3 opiniones (empresas, personas, citas y cifras).
- Precios «desde»: Cebú 890 € (sale del configurador antiguo, sin confirmar) y **Borneo 590 € (inventado)**.
- Medidas de la Borneo, garantía de 3 años, **resistencia al viento de 50 km/h** (dato de seguridad: confirmar sí o sí).
- Horario, plazos y formatos de personalización e impresión por sublimación.
- Las fotos de `imgs/web/` están generadas con IA: son ilustrativas (no son el equipo ni el taller reales).
- La fila de marcas usa nombres reales que aparecen en fotos del proyecto: confirmar que se pueden citar.

Publicar opiniones o casos inventados es una práctica desleal: hay que sustituirlos por reales o quitarlos.

## Datos que no cuadraban en el proyecto original

- Paredes a 89/119/139 € en el configurador antiguo y a 106/202/214 € en complementos (se usa el catálogo).
- Renders de color `amarillo` y `lima` intercambiados; `blanco` igual que `crema`.
- `roof.glb` está roto: el techo del visor 3D se dibuja por código.
- La norma correcta es UNE-EN 15619 T2.

## Editar textos

Las páginas se generan con los scripts de `_generador/` (hace falta Python 3):

```
cd _generador
python site_build.py
```

- Textos en español: `site_pages.py` (páginas) y `site_parts.py` (menú, pie, llamada final).
- Traducciones (CA, EN, FR, IT): `site_i18n.py` y `site_i18n2.py`.
- Estilos: `css/okatent.css`. Efectos y animaciones: `js/okatent.js`. Visor 3D: `js/visor3d.js`.

Si se edita un HTML a mano y luego se ejecuta `site_build.py`, el cambio se pierde.

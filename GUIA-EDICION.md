# 📚 Guía de Edición del Sitio Web - Parque de la Bellota

Esta guía explica cómo editar y añadir contenido al sitio web del Parque de la Bellota.

---

## 📚 Índice

1. [📄 Archivos de Páginas](#-archivos-de-páginas-_pagesmd)
   - [Estructura de un archivo](#estructura-de-un-archivo-de-página)
   - [Campos del Front Matter](#campos-del-front-matter-cabecera)

2. [✏️ Formato Markdown Básico](#️-formato-markdown-básico)
   - [Encabezados](#encabezados)
   - [Texto](#texto)
   - [Listas](#listas)
   - [Enlaces e imágenes](#enlaces-e-imágenes)

3. [🅰️ Letra Capitular (Drop Cap)](#️-letra-capitular-drop-cap)

4. [🐦 Añadir Nuevas Aves](#-añadir-nuevas-aves)
   - [Paso 1: Crear archivo](#paso-1-crear-archivo-de-ave)
   - [Paso 2: Añadir al listado](#paso-2-añadir-al-listado)

5. [🖼️ Subir y Usar Imágenes](#️-subir-y-usar-imágenes)
   - [Dónde subir imágenes](#dónde-subir-imágenes)
   - [Usar imágenes en páginas](#usar-imágenes-en-páginas)
   - [Usar imágenes en noticias](#usar-imágenes-en-noticias)

6. [📰 Añadir Noticias](#-añadir-noticias)

7. [📚 Actualizar Recursos Descargables](#-actualizar-recursos-descargables)
   - [Opción A: PDF con vista previa](#opción-a-pdf-con-vista-previa)
   - [Opción B: Imagen descargable](#opción-b-imagen-descargable)
   - [Opción C: Descarga directa](#opción-c-descarga-directa-sin-vista-previa)

8. [🎨 Personalizar Colores de Sección](#-personalizar-colores-de-sección)

9. [🎨 Configuración Avanzada de Colores](#-configuración-avanzada-de-colores)
   - [Añadir nuevos colores](#añadir-nuevos-colores)
   - [Cambiar colores de la letra capitular](#cambiar-colores-de-la-letra-capitular)

10. [🔧 Comandos Útiles](#-comandos-útiles)

11. [❓ Preguntas Frecuentes](#-preguntas-frecuentes)

---

## 📚 Índice

1. [📄 Archivos de Páginas](#-archivos-de-páginas-_pagesmd)
   - [Estructura de un archivo](#estructura-de-un-archivo-de-página)
   - [Campos del Front Matter](#campos-del-front-matter-cabecera)

2. [✏️ Formato Markdown Básico](#%EF%B8%8F-formato-markdown-básico)
   - [Encabezados](#encabezados)
   - [Texto](#texto)
   - [Listas](#listas)
   - [Enlaces e imágenes](#enlaces-e-imágenes)

3. [🅰️ Letra Capitular (Drop Cap)](#%EF%B8%8F-letra-capitular-drop-cap)

4. [🐦 Añadir Nuevas Aves](#-añadir-nuevas-aves)
   - [Paso 1: Crear archivo](#paso-1-crear-archivo-de-ave)
   - [Paso 2: Añadir al listado](#paso-2-añadir-al-listado)

5. [🖼️ Subir y Usar Imágenes](#%EF%B8%8F-subir-y-usar-imágenes)
   - [Dónde subir imágenes](#dónde-subir-imágenes)
   - [Usar imágenes en páginas](#usar-imágenes-en-páginas)
   - [Usar imágenes en noticias](#usar-imágenes-en-noticias)

6. [📰 Añadir Noticias](#-añadir-noticias)

7. [📚 Actualizar Recursos Descargables](#-actualizar-recursos-descargables)
   - [Opción A: PDF con vista previa](#opción-a-pdf-con-vista-previa)
   - [Opción B: Imagen descargable](#opción-b-imagen-descargable)
   - [Opción C: Descarga directa](#opción-c-descarga-directa-sin-vista-previa)

8. [🎨 Personalizar Colores de Sección](#-personalizar-colores-de-sección)

9. [🎨 Configuración Avanzada de Colores](#-configuración-avanzada-de-colores)
   - [Añadir nuevos colores](#añadir-nuevos-colores)
   - [Cambiar colores de la letra capitular](#cambiar-colores-de-la-letra-capitular)

10. [🔧 Comandos Útiles](#-comandos-útiles)

11. [❓ Preguntas Frecuentes](#-preguntas-frecuentes)

---

## 📄 Archivos de Páginas (`_pages/*.md`)

Las páginas del sitio están en la carpeta `_pages/`. Cada archivo `.md` (Markdown) es una página.

### Estructura de un archivo de página

```markdown
---
layout: page
title: Título de la Página
description: 📝 Descripción breve
image: assets/images/imagen.png
show-display-image: false  # opcional: oculta imagen en la página (pero se ve en home)
show_tile: true             # opcional: muestra/oculta en home
nav-menu: true
use-initials: true
accent: color-bosque
permalink: /url-de-la-pagina
---

<p id="initial-paragraph">Primera frase con letra capitular</p>

## Tu contenido aquí

Texto normal...
```

### Campos del Front Matter (cabecera)

| Campo | Descripción | Valores |
|-------|-------------|---------|
| **layout** | Tipo de plantilla | `page` para páginas normales |
| **title** | Título de la página | Texto libre |
| **description** | Descripción breve | Texto corto (aparece en home) |
| **image** | Ruta a imagen | `assets/images/nombre.png` |
| **show-display-image** | Mostrar imagen en página | `true` (default) / `false` |
| **show_tile** | Mostrar en tiles del home | `true` (default) / `false` |
| **nav-menu** | Aparece en menú navegación | `true` / `false` |
| **use-initials** | Activa letra capitular | `true` / `false` |
| **accent** | Color del tema | Ver lista abajo |
| **permalink** | URL de la página | `/url-pagina` |

**Colores disponibles (`accent`):**
- `color-bosque` (verde oscuro)
- `color-agua` (azul)
- `color-tierra` (marrón)
- `color-piedra` (gris)
- `color-pradera` (verde claro)
- `color-bellota` (naranja)

---

## ✏️ Formato Markdown Básico

### Encabezados

```markdown
# Encabezado 1 (H1)
## Encabezado 2 (H2)
### Encabezado 3 (H3)
```

### Texto

```markdown
**Negrita**
*Cursiva*
~~Tachado~~
```

### Listas

```markdown
- Lista sin orden
- Otro elemento
  - Subelemento

1. Lista ordenada
2. Segundo elemento
```

### Enlaces e imágenes

```markdown
[Texto del enlace](https://url.com)

![Texto alternativo](ruta/imagen.jpg)

[![Imagen con enlace](imagen.jpg)](https://url.com)
```

### Citas y código

```markdown
> Esto es una cita

`código inline`
```

### Líneas horizontales

```markdown
---
```

---

## 🅰️ Letra Capitular (Drop Cap)

Para que la **primera letra** del párrafo sea grande (estilo decorativo):

```markdown
<p id="initial-paragraph">Tu primera frase aquí</p>
```

**Importante:** 
- Solo funciona si `use-initials: true` en el front matter
- Solo un párrafo por página debe tener `id="initial-paragraph"`
- Debe ser el primer párrafo de contenido (después de la cabecera)

**Ejemplo:**

```markdown
---
layout: page
title: Mi Página
use-initials: true
---

<p id="initial-paragraph">Esta primera letra será grande y decorativa.</p>

El resto del contenido continúa normalmente.
```

---

## 🐦 Añadir Nuevas Aves

### Paso 1: Crear archivo de ave

Crea un nuevo archivo en `_pages/aves/` con el nombre: `nombre-comun.md`

**Ejemplo:** `_pages/aves/milano-real.md`

```markdown
---
layout: redirect
title: Milano Real
redirect_to: https://es.wikipedia.org/wiki/Milvus_milvus
description: Ave rapaz de gran tamaño
nav-menu: false
show_tile: false
permalink: /ave/milano-real
---
```

**Campos importantes:**
- `layout: redirect` - redirige automáticamente a otra URL
- `title:` - Nombre común del ave
- `redirect_to:` - URL de destino (Wikipedia, eBird, SEO/BirdLife, etc.)
- `permalink:` - URL interna (debe empezar con `/ave/`)
- `nav-menu: false` - No aparece en menú
- `show_tile: false` - No aparece en home

### Paso 2: Añadir al listado

Edita `_pages/wildlife.md` y añade a la lista:

```markdown
- [Milano Real](/ave/milano-real)
```

**Orden alfabético recomendado:**

```markdown
- [Abubilla](/ave/abubilla-comun)
- [Buitre negro](/ave/buitre-negro)
- [Milano Real](/ave/milano-real)  ← Nueva
- [Paloma torcaz](/ave/paloma-torcaz)
```

### Ejemplo completo

1. **Crear** `_pages/aves/carbonero-comun.md`:

```markdown
---
layout: redirect
title: Carbonero Común
redirect_to: https://es.wikipedia.org/wiki/Parus_major
description: Pequeño pájaro muy común en parques y jardines
nav-menu: false
show_tile: false
permalink: /ave/carbonero-comun
---
```

2. **Añadir** en `_pages/wildlife.md`:

```markdown
- [Carbonero Común](/ave/carbonero-comun)
```

---

## 🖼️ Subir y Usar Imágenes

### Dónde subir imágenes

| Tipo de imagen | Carpeta | Ejemplo |
|----------------|---------|---------|
| Imágenes generales | `/assets/images/` | `fauna_y_flora.png` |
| Imágenes de noticias | `/assets/images/news/` | `apertura-2026.jpg` |
| Recursos descargables | `/assets/resources/` | `mapa-detallado.jpg` |
| Iconos | `/assets/icons/` | `icono_basura.png` |

### Usar imágenes en páginas

**Imagen simple:**

```markdown
![Descripción de la imagen]({{ site.baseurl }}/assets/images/nombre.jpg)
```

**Imagen ampliable (con enlace):**

```markdown
[![Descripción]({{ site.baseurl }}/assets/images/foto.jpg)]({{ site.baseurl }}/assets/images/foto.jpg)
```

### Usar imágenes en noticias

En el front matter de la noticia (`_news/YYYY-MM-DD-titulo.md`):

```markdown
---
layout: post
title: Título de la Noticia
date: 2026-04-04
image: assets/images/news/foto-noticia.jpg
show-display-image: true  # false para NO mostrar en la página de noticia
---

Contenido de la noticia...
```

- Si `show-display-image: true` → la imagen se ve en la página de noticia
- Si `show-display-image: false` → la imagen solo se ve en el listado de noticias
- Si no pones `show-display-image` → por defecto es `true` (se muestra)

### Imagen en cabecera de página

En el front matter de cualquier página:

```markdown
---
layout: page
title: Mi Página
image: assets/images/mi-foto.jpg
show-display-image: true   # true para mostrar en página
---
```

### Recomendaciones de imágenes

- **Nombres**: usa nombres descriptivos sin espacios ni acentos
  - ✅ `foto-aves-primavera-2026.jpg`
  - ❌ `Foto Aves (primavera).jpg`
- **Tamaños**: optimiza antes de subir
  - Fotos: < 1-2 MB
  - Iconos: < 100 KB
- **Formatos**:
  - `.jpg` para fotografías
  - `.png` para gráficos, logos, imágenes con transparencia
  - `.svg` para iconos vectoriales

---

## 📰 Añadir Noticias

Las noticias se guardan en `_news/` con el formato: `YYYY-MM-DD-titulo.md`

### Crear una noticia

1. Crea archivo: `_news/2026-04-15-nueva-ruta.md`
2. Añade contenido:

```markdown
---
layout: post
title: Nueva Ruta del Mirador
date: 2026-04-15
image: assets/images/news/mirador.jpg
show-display-image: true
---

¡Tenemos una nueva ruta! El **Sendero del Mirador** ya está abierto al público.

## Características

- Longitud: 2.5 km
- Dificultad: Media
- Duración: 1 hora

Más información en nuestra [sección de rutas](/rutas).
```

### Campos importantes

- **date**: fecha en formato `YYYY-MM-DD` (determina el orden)
- **image**: imagen de la noticia (opcional)
- **show-display-image**: mostrar imagen en la página de noticia

### Orden de noticias

Las noticias aparecen automáticamente en `/noticias` ordenadas por fecha (más recientes primero).

---

## 📚 Actualizar Recursos Descargables

### Paso 1: Subir archivo

Sube tu archivo (PDF, imagen, etc.) a: `/assets/resources/`

**Ejemplo:** `/assets/resources/guia-aves-primavera.pdf`

### Paso 2: Añadir enlace en `resources.md`

Edita `_pages/resources.md` y elige uno de estos formatos:

#### Opción A: PDF con vista previa

```markdown
### 📝 Guía de Aves de Primavera

**Descripción:** Guía ilustrada de las aves que puedes observar en primavera en el parque.

<iframe src="{{ site.baseurl }}/assets/resources/guia-aves-primavera.pdf" width="100%" height="600px" style="border: 1px solid #ccc; border-radius: 8px; margin: 1em 0;"></iframe>

[📥 Descargar PDF]({{ site.baseurl }}/assets/resources/guia-aves-primavera.pdf){: .button .special}

---
```

#### Opción B: Imagen descargable

```markdown
### 🖼️ Mapa en Alta Resolución

**Descripción:** Mapa detallado del parque para imprimir.

[![Mapa del Parque]({{ site.baseurl }}/assets/resources/mapa-grande.jpg)]({{ site.baseurl }}/assets/resources/mapa-grande.jpg)

[📥 Descargar Imagen]({{ site.baseurl }}/assets/resources/mapa-grande.jpg){: .button download="mapa-parque.jpg"}

---
```

#### Opción C: Descarga directa (sin vista previa)

```markdown
### 📄 Ficha de Actividad: Huellas

**Descripción:** Actividad educativa para identificar huellas de animales.

[📥 Descargar PDF]({{ site.baseurl }}/assets/resources/actividad-huellas.pdf){: .button .special}

---
```

### Estructura recomendada

Cada recurso debe tener:
1. **Título** (con emoji opcional)
2. **Descripción** en negrita
3. **Vista previa** (opcional, iframe o imagen)
4. **Botón de descarga**
5. **Separador** `---`

### Consulta adicional

Ver `/assets/resources/README.md` para más ejemplos y detalles.

---

## 🎨 Personalizar Colores de Sección

Cada página puede tener un color de acento diferente. Edita el campo `accent` en el front matter:

```markdown
---
accent: color-bosque
---
```

**Colores disponibles:**

| Valor | Color | Uso sugerido |
|-------|-------|--------------|
| `color-bosque` | Verde oscuro | Descubre, naturaleza |
| `color-agua` | Azul | Actividades, agua |
| `color-tierra` | Marrón | Recursos, educación |
| `color-piedra` | Gris | Rutas, senderos |
| `color-pradera` | Verde claro | Fauna y flora |
| `color-bellota` | Naranja | Mapa, ubicación |
| `color-hoja` | Verde claro | Hojas, vegetación |

---

## 🎨 Configuración Avanzada de Colores

### Añadir nuevos colores

Si quieres añadir nuevos colores personalizados (como `color-rio`, `color-cielo`, etc.), sigue estos pasos:

#### Paso 1: Editar el archivo de variables

Abre el archivo `_sass/libs/_vars.scss` y busca la sección `Palette`.

**Añade tu nuevo color** dentro del mapa `$palette`:

```scss
$palette: (
    bg:                 #1a2017,
    bg-alt:             #2d472e,
    fg:                 #ebe0d8,
    // ... otros colores ...
    
    // Colores de acento — tiles y secciones
    color-tierra:       #8e6237,
    color-bosque:       #2d472e,
    color-agua:         #1e5773,
    color-piedra:       #4a4038,
    color-pradera:      #3d5220,
    color-bellota:      #5c4a3a,
    color-hoja:         #dde0b9,
    color-rio:          #4a8fa6,        // ← Nuevo color (azul río)
    color-cielo:        #6b95b8,        // ← Nuevo color (azul cielo)
    color-sol:          #d4a259,        // ← Nuevo color (amarillo dorado)
);
```

**Elige colores oscuros** para mantener la coherencia visual con el fondo oscuro del sitio.

#### Paso 2: Usar el nuevo color

Una vez añadido, úsalo en cualquier página:

```markdown
---
accent: color-rio
---
```

### Cambiar colores de la letra capitular

La letra capitular tiene dos elementos que puedes personalizar:
1. **Fondo/marco decorativo** - El fondo con motivos vegetales
2. **La letra en sí** - El carácter tipográfico

#### Cambiar el color del fondo decorativo

Edita `_sass/components/_initial.scss` y busca la sección `Marco / fondo de la capitular`:

```scss
// Marco / fondo de la capitular
.initial-svg svg path {
    fill: #505d83;              // ← Cambia este color (fondo decorativo)
    stroke: _palette(fg-light);
    stroke-width: 0.5;
}
```

**Recomendaciones:**
- Usa un tono **intermedio**: más oscuro que la letra, más claro que el fondo del sitio
- Colores sugeridos:
  - `#505d83` - Azul grisáceo (actual)
  - `#4a5d4a` - Verde grisáceo
  - `#5d4a4a` - Marrón grisáceo
  - `#3d4a56` - Gris azulado

#### Cambiar el color de la letra

En el mismo archivo, busca `La letra en sí`:

```scss
// La letra en sí
.initial-svg svg path.letter {
    fill: _palette(fg);         // ← Color de la letra (usa variable del tema)
    stroke: none;
}
```

**Opciones:**
- `_palette(fg)` - Blanco beis claro (predeterminado)
- `_palette(fg-bold)` - Verde clarito
- `_palette(highlight)` - Azul clarito
- `#ffffff` - Blanco puro
- Cualquier color hexadecimal personalizado

#### Ejemplo completo de personalización

```scss
// Marco / fondo de la capitular
.initial-svg svg path {
    fill: #3d5220;                  // Verde pradera para temática de naturaleza
    stroke: _palette(fg-light);
    stroke-width: 0.5;
}

// La letra en sí
.initial-svg svg path.letter {
    fill: #dde0b9;                  // Verde claro que contrasta con el fondo
    stroke: none;
}
```

**💡 Consejo:** Después de cambiar colores, ejecuta `bundle exec jekyll serve` para ver los cambios en tiempo real en `http://localhost:4000`.

---

## 🔧 Comandos Útiles

### Ejecutar el sitio localmente

```bash
bundle exec jekyll serve
```

Ver en: `http://localhost:4000`

### Limpiar caché

```bash
bundle exec jekyll clean
```

---

## ❓ Preguntas Frecuentes

### ¿Cómo cambio el orden de las páginas en el menú?

Edita `_config.yml` en la sección `navigation`:

```yaml
navigation:
  - discover
  - map
  - wildlife
  - activities
  - resources
  - routes
  - news
```

El orden aquí determina el orden en el menú superior.

### ¿Cómo oculto una página del menú pero la mantengo accesible?

En el front matter de la página:

```markdown
---
nav-menu: false
---
```

### ¿Puedo usar HTML en archivos Markdown?

Sí, puedes mezclar Markdown y HTML:

```markdown
## Título en Markdown

<div style="background: #f0f0f0; padding: 1em;">
  Contenido HTML personalizado
</div>

Volver a Markdown normal.
```

### ¿Cómo añado un botón?

```markdown
[Texto del botón](url){: .button .special}
```

**Estilos disponibles:**
- `.button` - botón básico
- `.button .special` - botón destacado (color)

---

## 📞 Soporte

Para dudas adicionales, consulta:
- Documentación de Markdown: https://www.markdownguide.org/
- Jekyll: https://jekyllrb.com/docs/

O contacta con el administrador del sitio: administracion@encinardelalberche.es

---

**Última actualización:** Abril 2026

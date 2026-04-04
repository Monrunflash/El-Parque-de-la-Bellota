# 📚 Recursos Descargables

Esta carpeta contiene todos los recursos descargables de la sección **Recursos** del sitio.

## 💾 Cómo añadir un nuevo recurso

### 1. Subir el archivo

Copia tu archivo (PDF, imagen, etc.) a esta carpeta: `/assets/resources/`

### 2. Añadir el enlace en la página

Edita el archivo `/_pages/resources.md` y añade un bloque como este:

#### Para PDFs con previsualización:

```markdown
### 📝 Título del Recurso

**Descripción:** Breve descripción del contenido.

<iframe src="{{ site.baseurl }}/assets/resources/nombre-archivo.pdf" width="100%" height="600px" style="border: 1px solid #ccc; border-radius: 8px; margin: 1em 0;"></iframe>

[📥 Descargar PDF]({{ site.baseurl }}/assets/resources/nombre-archivo.pdf){: .button .special}

---
```

#### Para imágenes con descarga:

```markdown
### 🖼️ Título del Recurso

**Descripción:** Breve descripción.

[![Descripción de la imagen]({{ site.baseurl }}/assets/resources/imagen.jpg)]({{ site.baseurl }}/assets/resources/imagen.jpg)

[📥 Descargar Imagen]({{ site.baseurl }}/assets/resources/imagen.jpg){: .button download="imagen.jpg"}

---
```

#### Para descarga directa (sin vista previa):

```markdown
### 📄 Título del Recurso

**Descripción:** Breve descripción.

[📥 Descargar]({{ site.baseurl }}/assets/resources/archivo.pdf){: .button .special}

---
```

## 📋 Ejemplos de archivos

- `guia-aves.pdf` - Guía de identificación de aves
- `mapa-grande.jpg` - Mapa en alta resolución
- `actividad-huellas.pdf` - Ficha de actividad educativa

## ⚠️ Recomendaciones

- Usa nombres de archivo descriptivos y sin espacios (usa guiones: `-`)
- Mantén tamaños razonables (PDFs < 5MB, imágenes < 2MB)
- Optimiza imágenes antes de subirlas
- Añade descripciones claras en la página
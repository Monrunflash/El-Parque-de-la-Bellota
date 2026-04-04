# 🌳 Parque de la Bellota 

Bienvenido al rincón del **Parque de la Bellota**, un entorno natural situado en la Sierra Oeste de Madrid, en las estribaciones del Sistema Central.

Este espacio reúne todos los recursos interactivos, mapas, actividades y contenidos educativos relacionados con el parque. Aquí podrás encontrar materiales descargables, información sobre flora y fauna, eventos locales. A lo largo de tu paseo por el parque encontrarás QRs distribuidos en los paneles interpretativos, que te llevarán a los recursos alojados en este [rincón](https://elencinardelalberche.github.io/El-Parque-de-la-Bellota/). 

---

## 📍 Sobre el parque

A la sombra del Parque Nacional de la Sierra de Guadarrama, la **Sierra Oeste** de Madrid es la hermana pequeña de la naturaleza montañosa de la región. Nuestra urbanización, **el Encinar del Alberche**, se encuentra en la zona de transición entre las Sierras de Gredos y Guadarrama.

El Parque de la Bellota limita al norte y al este con la **ZEPA nº 56** (Zona de Especial Protección para las Aves) "Encinares del río Alberche y río Cofio", un área de gran valor ecológico.

Este espacio alberga una biodiversidad extraordinaria, con aves migratorias, encinares, estanques y senderos señalizados.

**Puedes visitarnos todos los días de 9:00 a 21:00h. ¡Ven a descubrirlo!**

---

## 📚 Estructura del sitio web

El sitio está construido con **Jekyll** y organizado de la siguiente manera:

### 📄 Páginas principales (`_pages/`)
- **Descubre** - Introducción al parque
- **Mapa** - Mapa interactivo con puntos de interés
- **Fauna y Flora** - Listado de especies (aves)
- **Actividades** - Actividades educativas
- **Recursos** - Materiales descargables
- **Rutas** - Senderos y rutas del parque
- **Noticias** - Novedades y actualizaciones

### 🐦 Fichas de aves (`_pages/aves/`)
Cada ave tiene su propia ficha que redirige a información detallada.

### 📰 Noticias (`_news/`)
Noticias cronológicas sobre el parque (formato: `YYYY-MM-DD-titulo.md`).

### 🖼️ Recursos estáticos (`assets/`)
- `/images/` - Imágenes generales
- `/images/news/` - Imágenes de noticias
- `/resources/` - PDFs, imágenes descargables
- `/routes/` - Archivos GPX de rutas
- `/icons/` - Iconos
- `/initials/` - Letras capitulares decorativas

---

## ✏️ ¿Cómo editar el contenido?

📚 **Consulta la [Guía de Edición](GUIA-EDICION.md)** para aprender a:

- 📝 Editar páginas y crear contenido
- 🐦 Añadir nuevas especies de aves
- 🖼️ Subir imágenes y recursos
- 📰 Publicar noticias
- 🎨 Usar formato Markdown
- 🔤 Configurar letras capitulares

La guía incluye ejemplos paso a paso y plantillas listas para copiar.

---

## 📱 Acceso móvil y códigos QR

Muchos de los recursos están vinculados mediante **códigos QR** integrados en los **paneles interpretativos** repartidos por el parque. Escanéalos con tu teléfono para acceder directamente a:

- Información sobre puntos de interés
- Fichas de especies
- Mapas y rutas
- Recursos educativos

---

## 🛠️ Desarrollo local

### Requisitos
- Ruby 2.7+
- Bundler
- Jekyll

### Instalación

```bash
# Clonar el repositorio (primera vez)
git clone https://github.com/elencinardelalberche/El-Parque-de-la-Bellota.git
cd El-Parque-de-la-Bellota

# Instalar dependencias
bundle install

# Ejecutar servidor local
bundle exec jekyll serve

# Ver en: http://localhost:4000
```

### Mantener tu copia actualizada

```bash
# Actualizar tu repositorio local con los últimos cambios
git pull origin main

# Si trabajas en una rama específica, actualiza primero main
git checkout main
git pull origin main

# Luego vuelve a tu rama y actualiza
git checkout tu-rama
git merge main
```

### Comandos útiles

```bash
# Limpiar caché
bundle exec jekyll clean

# Construir sitio estático
bundle exec jekyll build
```

---

## 🤝 Colabora

Este proyecto está abierto a colaboración. Si deseas contribuir:

1. **Contenidos**: Añade información sobre especies, rutas o actividades
2. **Recursos**: Comparte guías, mapas o materiales educativos
3. **Mejoras técnicas**: Optimizaciones, nuevas funcionalidades
4. **Reportar problemas**: Abre un issue para reportar errores

### Cómo contribuir

1. Haz un fork del repositorio
2. Clona tu fork: `git clone https://github.com/tu-usuario/El-Parque-de-la-Bellota.git`
3. Añade el repositorio original como remoto: `git remote add upstream https://github.com/elencinardelalberche/El-Parque-de-la-Bellota.git`
4. Antes de empezar, actualiza desde el original: `git pull upstream main`
5. Crea una rama para tu cambio: `git checkout -b nueva-funcionalidad`
6. Realiza tus cambios siguiendo la [Guía de Edición](GUIA-EDICION.md)
7. Haz commit: `git commit -m "Descripción del cambio"`
8. Push a tu fork: `git push origin nueva-funcionalidad`
9. Abre un Pull Request desde GitHub

---

## 📧 Contacto

**Email**: administracion@encinardelalberche.es

**Dirección**:  
Calle Pinos 160, Fase 1  
Villa del Prado, Madrid 28630  
España

**Teléfono**: 91 867 40 03

---

## 🐦 Licencia

Todo el contenido de este repositorio se publica bajo una licencia [Creative Commons CC-BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/), salvo que se indique lo contrario.

Esto significa que puedes:
- ✅ Compartir y adaptar el contenido
- ✅ Usarlo para fines educativos
- ⚠️ Debes dar crédito apropiado
- ⚠️ Compartir bajo la misma licencia

---

**Parque de la Bellota** — Sierra Oeste de Madrid  
Una iniciativa comunitaria para conectar con la naturaleza.

🌳 [Visita el sitio web](https://elencinardelalberche.github.io/El-Parque-de-la-Bellota/)

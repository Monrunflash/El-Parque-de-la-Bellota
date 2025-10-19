---
layout: post
title: Rutas
nav-menu: true
show_tile: true
description: 🥾 Descubre nuestras rutas
image: assets/images/pic01.jpg
---



<script>
document.addEventListener('DOMContentLoaded', async () => {
  const paragraph = document.querySelector('#initial-paragraph')
  if (!paragraph) return

  const initial = paragraph.innerText.substring(0, 1)
  if (!initial.match(/[A-Z]/)) return

  const path = `{{ site.baseurl }}/assets/initials/${initial.toLowerCase()}.svg`
  
  try {
    const response = await fetch(path)
    const svgText = await response.text()
    
    paragraph.innerHTML = `
      <div class="initial-svg">${svgText}</div>
      ${paragraph.innerHTML.replace(/^\s*(\w)/, '<span class="hidden">$1</span>')}
    `
  } catch (error) {
    console.error('Error loading initial:', error)
  }
})
</script>

## Rutas del Parque

<p id="initial-paragraph">Además del Parque de la Bellota, El Encinar del Alberche cuenta con otras rutas que permiten explorar este maravilloso entorno de formas distintas.</p>

Hay caminos de diferentes longitudes e intensidades, adaptados tanto para quienes buscan un recorrido tranquilo como para quienes prefieren una caminata más exigente. Todas ellas invitan a disfrutar del paisaje, la biodiversidad y la calma de este espacio natural.

## Recomendaciones

- Lleva agua suficiente
- Usa calzado adecuado para senderismo
- Consulta el tiempo antes de salir
- Respeta las señalizaciones del camino
- No abandones los senderos marcados

---

### 🐘 Senda de los Elefantes
**Recorrido:** Ida y vuelta 2 km  
**Intensidad:** 🟡 Moderada

Recomendado para caminantes con algo de experiencia. Encuentra el mirador, punto de observación de aves.

[📥 Descargar GPX]({{ site.baseurl }}/assets/routes/ruta01.gpx){: .button .special}

<iframe frameBorder="0" scrolling="no" src="https://es.wikiloc.com/wikiloc/embedv2.do?id=69561037&elevation=off&images=off&maptype=H" width="100%" height="400" style="border-radius: 8px; margin: 1em 0;"></iframe>


---

### 🍓 Caminos de los Madroños
**Recorrido:** 1 km el circular y 0.7 km el lineal  
**Intensidad:** 🟢 Baja

Adecuado para toda la familia. Ideal para paseos cortos y reconocer la flora autóctona de El Encinar.

[📥 Descargar GPX]({{ site.baseurl }}/assets/routes/caminos-madronos.gpx){: .button .special}

---

### 🔥 Pista del Cortafuegos
**Recorrido:** Lineal, ida y vuelta 9.6 km  
**Intensidad:** 🔴 Alta

Solo para senderistas experimentados. Prepárate para un desafío físico y disfruta del hermoso paisaje.

[📥 Descargar GPX]({{ site.baseurl }}/assets/routes/pista-cortafuegos.gpx){: .button .special}

---

### 🐐 Camino del Cabrero
**Recorrido:** Circular, compartido con Pista del Cortafuegos; 2.5 km  
**Intensidad:** 🟡 Moderada

Recomendado para caminantes con algo de experiencia. Disfruta de vistas panorámicas durante el recorrido.

[📥 Descargar GPX]({{ site.baseurl }}/assets/routes/camino-cabrero.gpx){: .button .special}

---

### 🗼 Ruta Circular de la Torreta
**Recorrido:** Circular de 3.8 km  
**Intensidad:** 🔴 Alta

Entre pinares, con tramos exigentes y paisajes que recompensan a los amantes del senderismo más auténtico.

[📥 Descargar GPX]({{ site.baseurl }}/assets/routes/ruta-torreta.gpx){: .button .special}

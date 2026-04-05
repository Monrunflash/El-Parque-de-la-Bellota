#!/usr/bin/env python3
"""
Generador de códigos QR a partir de una lista de URLs.
Lee un archivo urls.txt y genera un código QR por cada URL.
Los archivos se guardan en assets/qr/ con nombres descriptivos.

Uso:
    python3 generate_qr.py

Requisitos:
    pip install qrcode[pil]
"""

import qrcode
import re
from pathlib import Path
from urllib.parse import urlparse

def sanitize_filename(text):
    """Convierte texto en nombre de archivo válido"""
    # Reemplazar caracteres no válidos por guiones
    text = re.sub(r'[^\w\s-]', '', text)
    # Reemplazar espacios y múltiples guiones por un solo guión
    text = re.sub(r'[-\s]+', '-', text)
    return text.lower().strip('-')

def generate_qr_code(url, output_path):
    """Genera un código QR para la URL dada"""
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(url)
    qr.make(fit=True)
    
    img = qr.make_image(fill_color="black", back_color="white")
    img.save(output_path)
    return output_path

def process_urls(input_file='urls.txt', output_dir='assets/qr'):
    """Procesa el archivo de URLs y genera los códigos QR"""
    
    # Crear directorio de salida si no existe
    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)
    
    # Leer URLs del archivo
    try:
        with open(input_file, 'r', encoding='utf-8') as f:
            urls = [line.strip() for line in f if line.strip() and not line.startswith('#')]
    except FileNotFoundError:
        print(f"❌ Error: No se encontró el archivo '{input_file}'")
        print(f"Crea un archivo '{input_file}' con una URL por línea.")
        return
    
    if not urls:
        print(f"⚠️  No se encontraron URLs en '{input_file}'")
        return
    
    print(f"📋 Procesando {len(urls)} URLs...\n")
    
    generated = []
    for url in urls:
        try:
            # Parsear URL
            parsed = urlparse(url)
            domain = parsed.netloc.replace('www.', '')
            path = parsed.path.strip('/')
            fragment = parsed.fragment  # Capturar ancla (#topografía, etc.)
            
            # Generar nombre de archivo descriptivo
            if fragment:
                # Si hay ancla, incluirla en el nombre
                filename = f"{sanitize_filename(domain)}_{sanitize_filename(path)}_{sanitize_filename(fragment)}.png"
            elif path:
                filename = f"{sanitize_filename(domain)}_{sanitize_filename(path)}.png"
            else:
                filename = f"{sanitize_filename(domain)}_home.png"
            
            # Ruta completa de salida
            qr_path = output_path / filename
            
            # Generar QR
            generate_qr_code(url, qr_path)
            generated.append((url, filename))
            
            print(f"✅ {filename}")
            print(f"   {url}\n")
            
        except Exception as e:
            print(f"❌ Error procesando {url}: {e}\n")
    
    # Resumen
    print(f"\n{'='*60}")
    print(f"✨ Generados {len(generated)} códigos QR en '{output_dir}/'")
    print(f"{'='*60}\n")
    
    # Crear archivo índice
    index_path = output_path / 'README.md'
    with open(index_path, 'w', encoding='utf-8') as f:
        f.write("# 📱 Códigos QR del Parque de la Bellota\n\n")
        f.write("Códigos QR generados automáticamente para enlaces del sitio.\n\n")
        f.write("## Códigos disponibles\n\n")
        
        for url, filename in generated:
            f.write(f"### `{filename}`\n\n")
            f.write(f"**URL:** {url}\n\n")
            f.write(f"![QR Code]({filename})\n\n")
            f.write("---\n\n")
    
    print(f"📄 Índice creado en '{index_path}'")

if __name__ == '__main__':
    process_urls()


from pdftoimage import convert_from_path

# Ruta del archivo PDF
pdf_path = "faxihorario.pdf"

# Convertir PDF a imágenes (una imagen por cada página del PDF)
imagenes = convert_from_path(pdf_path)

# Guardar cada página como una imagen JPG
for i, imagen in enumerate(imagenes):
    imagen.save(f'pagina_{i+1}.jpg', 'JPEG')

print("Conversión completada.")

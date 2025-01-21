from PIL import Image
import os

def convert_png_to_pdf(input_folder, output_pdf):
    """
    Convierte todas las imágenes PNG en una carpeta a un único archivo PDF.
    
    Parámetros:
        input_folder (str): Ruta de la carpeta que contiene las imágenes PNG.
        output_pdf (str): Ruta y nombre del archivo PDF de salida.
    """
    png_files = [f for f in os.listdir(input_folder) if f.lower().endswith('.jpg')]
    
    if not png_files:
        print("No se encontraron archivos PNG en la carpeta proporcionada.")
        return
    
    images = []
    for file in png_files:
        file_path = os.path.join(input_folder, file)
        img = Image.open(file_path)
        img = img.convert("RGB")  # Convertir a modo RGB si es necesario
        images.append(img)
    
    # Guardar las imágenes en un archivo PDF
    images[0].save(output_pdf, save_all=True, append_images=images[1:])
    print(f"Archivo PDF creado exitosamente: {output_pdf}")

# Ejemplo de uso:
input_folder = "img"  # Reemplaza con la ruta de tu carpeta
output_pdf = "Datos BBVA.pdf"  # Reemplaza con el nombre del PDF deseado
convert_png_to_pdf(input_folder, output_pdf)

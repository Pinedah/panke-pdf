import PyPDF2

def join_pdfs(pdf1_path, pdf2_path, output_path):
    # Crear un lector de archivos PDF para cada archivo
    pdf1 = open(pdf1_path, 'rb')
    pdf2 = open(pdf2_path, 'rb')
    
    pdf1_reader = PyPDF2.PdfReader(pdf1)
    pdf2_reader = PyPDF2.PdfReader(pdf2)
    
    # Crear un escritor de archivos PDF
    pdf_writer = PyPDF2.PdfWriter()
    
    # Añadir todas las páginas del primer PDF
    for page_num in range(len(pdf1_reader.pages)):
        page = pdf1_reader.pages[page_num]
        pdf_writer.add_page(page)
    
    # Añadir todas las páginas del segundo PDF
    for page_num in range(len(pdf2_reader.pages)):
        page = pdf2_reader.pages[page_num]
        pdf_writer.add_page(page)
    
    # Guardar el archivo combinado en el destino especificado
    with open(output_path, 'wb') as output_pdf:
        pdf_writer.write(output_pdf)
    
    # Cerrar los archivos abiertos
    pdf1.close()
    pdf2.close()

# Rutas de los archivos PDF a unir
pdf1_path = 'file1.pdf'
pdf2_path = 'file2.pdf'
output_path = 'merged_pdf.pdf'

# Llamar a la función para unir los PDFs
join_pdfs(pdf1_path, pdf2_path, output_path)

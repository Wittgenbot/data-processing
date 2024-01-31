import os
from dotenv import load_dotenv
from PyPDF2 import PdfReader, PdfWriter
load_dotenv()

def delete_first_page(pdf_path, output_dir):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    with open(pdf_path, 'rb') as pdf_file:
        pdf_reader = PdfReader(pdf_file)
        pdf_writer = PdfWriter()

        for page_num in range(1, len(pdf_reader.pages)):
            page = pdf_reader.pages[page_num]
            pdf_writer.add_page(page)

        output_filename = os.path.join(output_dir, os.path.basename(pdf_path))
        with open(output_filename, 'wb') as output_file:
            pdf_writer.write(output_file)

        print(f"First page deleted and saved to: {output_filename}")

input_folder = os.getenv('pdfs_to_delete_first_page')
output_folder = os.getenv('pdfs_first_page_deleted')

#loop through all PDFs in input folder
for filename in os.listdir(input_folder):
    if filename.endswith(".pdf"):
        pdf_path = os.path.join(input_folder, filename)
        delete_first_page(pdf_path, output_folder)
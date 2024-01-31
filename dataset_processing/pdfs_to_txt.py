import os
from dotenv import load_dotenv
from PyPDF2 import PdfReader
load_dotenv()

def pdfs_to_txt(input_folder, output_folder):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for filename in os.listdir(input_folder):
        if filename.endswith(".pdf"):
            pdf_path = os.path.join(input_folder, filename)

            with open(pdf_path, 'rb') as pdf_file:
                pdf_reader = PdfReader(pdf_file)

                text = ""
                for page_num in range(len(pdf_reader.pages)):
                    page = pdf_reader.pages[page_num]
                    text += page.extract_text()

                txt_filename = os.path.join(output_folder, os.path.splitext(filename)[0] + ".txt")
                with open(txt_filename, 'w', encoding='utf-8') as txt_file:
                    txt_file.write(text)

                print(f"Text extracted from {filename} and saved to: {txt_filename}")


input_folder = os.getenv('pdfs_cleaned_pages')
output_folder = os.getenv('pdfs_as_txts')

pdfs_to_txt(input_folder, output_folder)

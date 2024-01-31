import os

def get_pdf_names(folder_path):
    files = os.listdir(folder_path)
    pdf_files = [file for file in files if file.lower().endswith(".pdf")]
    return pdf_files

pdf_folder = "D:\AUB\FYP\Code\PDF to TXT + Clean up\PDFs\Temporary"
pdf_names = get_pdf_names(pdf_folder)

print("PDF files in the folder:")
for pdf_name in pdf_names:
    #print(pdf_name)
    print(f"delete_custom_pages(\"{pdf_name}\", 1, -1)")


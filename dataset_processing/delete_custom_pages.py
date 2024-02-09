import os
from dotenv import load_dotenv
from PyPDF2 import PdfReader, PdfWriter
load_dotenv()

input_folder = os.getenv('pdfs_first_page_deleted')
output_folder = os.getenv('pdfs_cleaned_pages')

def delete_custom_pages(pdf_filename, start_page, end_page):
    pdf_path = os.path.join(input_folder, pdf_filename)

    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    with open(pdf_path, 'rb') as pdf_file:
        pdf_reader = PdfReader(pdf_file)
        pdf_writer = PdfWriter()

        if end_page == -1:
            end_page = len(pdf_reader.pages) + 1

        for page_num in range(start_page - 1, min(end_page, len(pdf_reader.pages))):
            page = pdf_reader.pages[page_num]
            pdf_writer.add_page(page)

        output_filename = os.path.join(output_folder, f"{pdf_filename}")
        with open(output_filename, 'wb') as output_file:
            pdf_writer.write(output_file)

        print(f"Pages {start_page} to {end_page} extracted and saved to: {output_filename}")


# calls unique to each file
# delete_custom_pages("BLACK-WittgensteinsLanguagegames-1979.pdf", 1, -1)
# delete_custom_pages("Feyerabend-WittgensteinsPhilosophicalInvestigations-1955.pdf", 1, -1)
# delete_custom_pages("Findlay-WittgensteinsPhilosophicalInvestigations-1953.pdf", 1, -1)
# delete_custom_pages("Gill-WITTGENSTEINFUNCTIONPHILOSOPHY-1971.pdf", 1, -1)
# delete_custom_pages("Hunter-FormsLifeWittgensteins-1968.pdf", 1, -1)
# delete_custom_pages("JACQUETTE-LaterWittgensteinsAntiPhilosophical-2014.pdf", 1, -1)
# delete_custom_pages("Malcolm-WittgensteinLanguageRules-1989.pdf", 1, -1)
# delete_custom_pages("Malcolm-WittgensteinsPhilosophicalInvestigations-1954.pdf", 1, -1)
# delete_custom_pages("Dromm-WittgensteinLanguageLearning-2006.pdf", 1, 13)
# delete_custom_pages("G. P. Baker, P. M. S. Hacker - Wittgenstein Understanding and Meaning Part I Essays.pdf", 23, 401)
# delete_custom_pages("G. P. Baker, P. M. S. Hacker - Wittgenstein_ Understanding and Meaning (Analytical Commentary on the Philosophical Investgations Vol. 1, Part II) (2005).pdf", 21, 376)
# delete_custom_pages("Haack-WittgensteinsPragmatism-1982.pdf", 1, 8)
# delete_custom_pages("Mari McGinn - Guidebook to Wittgenstein's Philosophical Investigations.pdf", 17, 342)
# delete_custom_pages("McDowell-WittgensteinfollowingRule-1984.pdf", 1, 34)
# delete_custom_pages("Wittgenstein's Conception of Philosophy Dissertation.pdf", 1, 130)
delete_custom_pages("THE NEW WITTGENSTEIN Book.pdf", 31, 391)
delete_custom_pages("Wittgenstein Key Concepts Book.pdf", 25, 206)
delete_custom_pages("Wittgenstein on Aesthetics and Philosophy.pdf", 1, 9)
delete_custom_pages("Wittgenstein on Understanding and Emotion.pdf", 1, 12)

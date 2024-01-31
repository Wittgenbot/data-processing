import os
import re
from dotenv import load_dotenv
load_dotenv()

def remove_string_from_txt_files(input_folder, pattern_to_remove):
    if not os.path.exists(input_folder):
        print(f"Error: The input folder '{input_folder}' does not exist.")
        return

    for filename in os.listdir(input_folder):
        if filename.endswith(".txt"):
            txt_path = os.path.join(input_folder, filename)

            with open(txt_path, 'r', encoding='utf-8') as txt_file:
                content = txt_file.read()

            modified_content = re.sub(pattern_to_remove, '', content)

            with open(txt_path, 'w', encoding='utf-8') as txt_file:
                txt_file.write(modified_content)

            print(f"String removed from {filename}")

input_folder = os.getenv('pdfs_as_txts')
pattern_to_remove = r"This content downloaded from[\s\S]*?All use subject to https://about.jstor.org/terms"

remove_string_from_txt_files(input_folder, pattern_to_remove)

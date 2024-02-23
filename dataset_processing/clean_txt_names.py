import os
import re
from titlecase import titlecase
from dotenv import load_dotenv
load_dotenv()

def correct_capitalization(title):
    return titlecase(title)

def format_author_name(author):
    if ',' in author:
        last, first = author.split(', ')
        return f"{first} {last}"
    return author

def replace_underscores_with_space(filename):
    return re.sub(r'_+', ' ', filename)

def rename_files_in_directory(directory):
    for filename in os.listdir(directory):
        if filename.endswith(".txt"):
            base_name, _ = os.path.splitext(filename)
            title_author = replace_underscores_with_space(base_name)
            try:
                title, author = title_author.split(' by ')
                corrected_title = correct_capitalization(title)
                corrected_author = format_author_name(author)
                new_filename = f"{corrected_title} by {corrected_author}.txt"
                os.rename(os.path.join(directory, filename), os.path.join(directory, new_filename))
                print(f"Renamed '{filename}' to '{new_filename}'")
            except ValueError:
                print(f"Skipping file with unexpected format: '{filename}'")

directory_path = 'core_api_results'
rename_files_in_directory(directory_path)

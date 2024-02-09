import requests
import os
from dotenv import load_dotenv
load_dotenv()

def get_papers_core_api(query, limit, offset=0):

    base_url = "https://api.core.ac.uk/v3/search/works"
    core_api_key = os.getenv('core_api_key')
    
    params = {
        'q': {query},
        'limit': {limit},
        'offset': {offset},
    }
    headers = {
        'Authorization': f'Bearer {core_api_key}',
    }
    
    result = []
    
    response = requests.get(base_url, params=params, headers=headers)
    
    if response.status_code == 200:
        data = response.json()
        
        for paper in data['results']:
            language_code = paper.get('language', {}).get('code') if paper.get('language') else None
            if language_code == 'en':
                title = paper.get('title', '')
                authors = [author['name'] for author in paper.get('authors', [])]
                pdf_link = paper.get('downloadUrl', '')
                full_text = paper.get('fullText', '')
                
                result.append({
                    'title': title,
                    'authors': authors,
                    'pdf_link': pdf_link,
                    'full_text': full_text
                })
            
    else:
        print("Failed to retrieve data:", response.status_code)
    
    return result

def save_core_results_as_text(results):
    results_dir = "core_api_results"
    
    if not os.path.exists(results_dir):
        os.makedirs(results_dir)
    
    for paper in results:
        first_author_name = paper['authors'][0] if paper['authors'] else 'Unknown'
        file_name = f"{paper['title']} by {first_author_name}.txt"
        file_name_safe = clean_file_name(file_name)
        
        full_path = os.path.join(results_dir, file_name_safe)
        
        with open(full_path, 'w', encoding='utf-8') as file:
            file.write(paper['full_text'])

def clean_file_name(filename):
    invalid_chars = ['<', '>', ':', '"', '/', '\\', '|', '?', '*', '\n']
    for char in invalid_chars:
        filename = filename.replace(char, '_')
    return filename

def print_papers_with_head_text(papers, num_chars=30):
    for paper in papers:
        print(f"Title: {paper['title']}")
        print(f"Authors: {', '.join(paper['authors'])}")
        print(f"PDF Link: {paper['pdf_link']}")
        head_text = paper['full_text'][:num_chars] + "..." if paper['full_text'] else "No full text available"
        print(f"Full Text (head): {head_text}")
        print("---")

query = "(Wittgenstein+Philosophical+Investigations)OR(Wittgenstein on)"
limit = 80

papers = get_papers_core_api(query, limit)

save_core_results_as_text(papers)

print_papers_with_head_text(papers)

import os
import requests
from datetime import date

README_PATH = "README.md"
FACT_API_URL = "https://uselessfacts.jsph.pl/random.json"
MARKER_START = ""
MARKER_END = ""
FACT_PREFIX = "-  Fun fact of today: "

def fetch_random_fact():
    try:
        response = requests.get(FACT_API_URL)
        response.raise_for_status() 
        data = response.json()
        fact_text = data.get("text")
        
        if not fact_text:
            return None
            
        formatted_fact_line = f"{FACT_PREFIX}{fact_text}"
        return formatted_fact_line
        
    except requests.exceptions.RequestException:
        return None

def update_readme(new_fact_line):
    if not new_fact_line:
        return False

    try:
        with open(README_PATH, 'r', encoding='utf-8') as f:
            content = f.read()
    except FileNotFoundError:
        return False

    start_index = content.find(MARKER_START)
    end_index = content.find(MARKER_END)

    if start_index == -1 or end_index == -1:
        return False
    
    content_start = start_index + len(MARKER_START)
    
    before_content = content[:content_start]
    after_content = content[end_index:]

    new_readme_content = f"{before_content}\n{new_fact_line}\n{after_content}"

    with open(README_PATH, 'w', encoding='utf-8') as f:
        f.write(new_readme_content)
        
    return True

if __name__ == "__main__":
    fact_line = fetch_random_fact()
    if fact_line:
        update_readme(fact_line)

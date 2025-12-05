import json
from datetime import date
import os

with open("AKJV.json", "r", encoding="utf-8") as f:
    bible_data = json.load(f)

verses_list = []
for book in bible_data["books"]:
    book_name = book["name"]
    for chapter in book["chapters"]:
        chapter_num = chapter["chapter"]
        for verse in chapter["verses"]:
            verse_num = verse["verse"]
            verse_text = verse["text"].strip()
            verses_list.append({
                "book": book_name,
                "chapter": chapter_num,
                "verse": verse_num,
                "text": verse_text
            })

today = date.today()
index = today.toordinal() % len(verses_list)
verse_of_the_day = verses_list[index]

verse_text = verse_of_the_day["text"]
verse_ref = f"{verse_of_the_day['book']} {verse_of_the_day['chapter']}:{verse_of_the_day['verse']}"
new_verse_md = f'Bible verse of today: "{verse_text}" — *{verse_ref}*'

readme_file = "README.md"

if not os.path.isfile(readme_file):
    raise FileNotFoundError(f"{readme_file} not found! Make sure it exists in the repo root.")

with open(readme_file, "r", encoding="utf-8") as f:
    lines = f.readlines()

for i, line in enumerate(lines):
    if line.startswith("Bible verse of today:"):
        lines[i] = new_verse_md + "\n"
        break

with open(readme_file, "w", encoding="utf-8") as f:
    f.writelines(lines)

print("README updated with today's verse!")

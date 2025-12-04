import json
from datetime import date

# --- Load the Bible JSON ---
with open("AKJV.json", "r", encoding="utf-8") as f:
    bible_data = json.load(f)

# --- Flatten the nested structure into a list of verses ---
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

# --- Pick verse of the day based on the date ---
today = date.today()
index = today.toordinal() % len(verses_list)  # cycles through all verses
verse_of_the_day = verses_list[index]

# --- Format for README ---
verse_text = verse_of_the_day["text"]
verse_ref = f"{verse_of_the_day['book']} {verse_of_the_day['chapter']}:{verse_of_the_day['verse']}"
new_verse_md = f'Bible verse of today: "{verse_text}" — *{verse_ref}*'

# --- Update README ---
readme_file = "READMe.md"  # adjust to your file name
with open(readme_file, "r", encoding="utf-8") as f:
    lines = f.readlines()

for i, line in enumerate(lines):
    if line.startswith("Bible verse of today:"):
        lines[i] = new_verse_md + "\n"
        break

with open(readme_file, "w", encoding="utf-8") as f:
    f.writelines(lines)

print("README updated with today's verse!")

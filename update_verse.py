import requests

# Fetch the daily verse
url = "https://beta.ourmanna.com/api/v1/get?format=json&order=daily"
headers = {"accept": "application/json"}
response = requests.get(url, headers=headers)
data = response.json()

verse_text = data["verse"]["details"]["text"]
verse_ref = data["verse"]["details"]["reference"]
verse_version = data["verse"]["details"]["version"]

# Format the verse for Markdown
new_verse_md = f"Bible verse of today: \"{verse_text}\" — *{verse_ref} ({verse_version})*"

# Read the current README
with open("README.md", "r", encoding="utf-8") as f:
    lines = f.readlines()

# Update the line containing 'Bible verse of today:'
for i, line in enumerate(lines):
    if line.startswith("Bible verse of today:"):
        lines[i] = new_verse_md + "\n"
        break

# Write back to README.md
with open("README.md", "w", encoding="utf-8") as f:
    f.writelines(lines)

print("Updated the Bible verse of the day!")

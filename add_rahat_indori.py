#!/usr/bin/env python3
"""Add Rahat Indori shayari to the collection"""

import re

# Read the file
with open('shayari.js', 'r', encoding='utf-8') as f:
    content = f.read()

# Find the last ID
ids = re.findall(r'id:\s*(\d+),', content)
last_id = max([int(id) for id in ids]) if ids else 0
print(f"Last ID found: {last_id}")

# New shayari by Rahat Indori
new_shayari = [
    {'category': 'life', 'text': '''रोज़ तारों को नुमाइश में ख़लल पड़ता है
चाँद पागल है अँधेरे में निकल पड़ता है'''},
    {'category': 'romantic', 'text': '''सूरज सितारे चाँद मिरे साथ में रहे
जब तक तुम्हारे हाथ मिरे हाथ में रहे'''},
    {'category': 'life', 'text': '''रात की धड़कन जब तक जारी रहती है
सोते नहीं हम ज़िम्मेदारी रहती है'''},
    {'category': 'life', 'text': '''सोए रहते हैं ओढ़ कर ख़ुद को
अब ज़रूरत नहीं रज़ाई की'''},
    {'category': 'life', 'text': '''सितारो आओ मिरी राह में बिखर जाओ
ये मेरा हुक्म है हालाँकि कुछ नहीं हूँ मैं'''},
    {'category': 'life', 'text': '''चराग़ों का घराना चल रहा है
हवा से दोस्ताना चल रहा है'''},
    {'category': 'life', 'text': '''अब इतनी सारी शबों का हिसाब कौन रखे
बड़े सवाब कमाए गए जवानी में'''},
    {'category': 'life', 'text': '''चाँद सूरज मिरी चौखट पे कई सदियों से
रोज़ लिक्खे हुए चेहरे पे सवाल आते हैं'''},
    {'category': 'life', 'text': '''जा-नमाज़ों की तरह नूर में उज्लाई सहर
रात भर जैसे फ़रिश्तों ने इबादत की है'''},
    {'category': 'romantic', 'text': '''शाम ने जब पलकों पे आतिश-दान लिया
कुछ यादों ने चुटकी में लोबान लिया'''}
]

# Find the position to insert
pattern = r'(const hindiShayari = \[.*?)(];)'
match = re.search(pattern, content, re.DOTALL)

if match:
    start_pos = match.end(1)
    
    # Generate new entries
    new_entries = []
    current_id = last_id + 1
    
    for shayari in new_shayari:
        entry = f'''  
  {{
    id: {current_id},
    language: 'hindi',
    category: '{shayari['category']}',
    author: 'राहत इंदौरी',
    text: `{shayari['text']}`,
  }},'''
        new_entries.append(entry)
        current_id += 1
    
    # Insert new entries
    new_content = content[:start_pos] + '\n' + '\n'.join(new_entries) + content[start_pos:]
    
    # Write back
    with open('shayari.js', 'w', encoding='utf-8') as f:
        f.write(new_content)
    
    print(f"Successfully added {len(new_shayari)} shayari by राहत इंदौरी!")
    print(f"New IDs: {last_id + 1} to {current_id - 1}")
else:
    print("Could not find insertion point")

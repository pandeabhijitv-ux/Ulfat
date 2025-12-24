#!/usr/bin/env python3
"""Add additional Irfan Siddiqui shayari to the collection"""

import re

# Read the file
with open('shayari.js', 'r', encoding='utf-8') as f:
    content = f.read()

# Find the last ID
ids = re.findall(r'id:\s*(\d+),', content)
last_id = max([int(id) for id in ids]) if ids else 0
print(f"Last ID found: {last_id}")

# New shayari by Irfan Siddiqui (avoiding duplicates from first batch)
new_shayari = [
    {'category': 'romantic', 'text': '''तुम सुनो या न सुनो हाथ बढ़ाओ न बढ़ाओ
डूबते डूबते इक बार पुकारेंगे तुम्हें'''},
    {'category': 'romantic', 'text': '''उस की आँखें हैं कि इक डूबने वाला इंसाँ
दूसरे डूबने वाले को पुकारे जैसे'''},
    {'category': 'romantic', 'text': '''मेरे होने में किसी तौर से शामिल हो जाओ
तुम मसीहा नहीं होते हो तो क़ातिल हो जाओ'''},
    {'category': 'life', 'text': '''हम सब आईना-दर-आईना-दर-आईना हैं
क्या ख़बर कौन कहाँ किस की तरफ़ देखता है'''},
    {'category': 'sad', 'text': '''आख़िर-ए-शब हुई आग़ाज़ कहानी अपनी
हम ने पाया भी तो इक उम्र गँवा कर उस को'''},
    {'category': 'life', 'text': '''उड़े तो फिर न मिलेंगे रफ़ाक़तों के परिंद
शिकायतों से भरी टहनियाँ न छू लेना'''},
    {'category': 'romantic', 'text': '''आज तक उन की ख़ुदाई से है इंकार मुझे
मैं तो इक उम्र से काफ़िर हूँ सनम जानते हैं'''},
    {'category': 'life', 'text': '''हम भी पत्थर तुम भी पत्थर सब पत्थर टकराओ
हम भी टूटें तुम भी टूटो सब टूटें आमीन'''},
    {'category': 'life', 'text': '''ये हम ने भी सुना है आलम-ए-असबाब है दुनिया
यहाँ फिर भी बहुत कुछ बे-सबब होता ही रहता है'''},
    {'category': 'sad', 'text': '''उस से बिछड़े तो तुम्हें कोई न पहचानेगा
तुम तो परछाईं हो पैकर की तरफ़ लौट चलो'''},
    {'category': 'sad', 'text': '''वो मुझ में बोलने वाला तो चुप है बरसों से
ये कौन है जो तिरे रू-ब-रू पुकारता है'''},
    {'category': 'romantic', 'text': '''मैं ख़्वाब देख रहा हूँ कि वो पुकारता है
और अपने जिस्म से बाहर निकल रहा हूँ मैं'''},
    {'category': 'sad', 'text': '''क्या जज़्ब-ए-इश्क़ मुझ से ज़ियादा था ग़ैर में
उस का हबीब उस से जुदा क्यूँ नहीं हुआ'''}
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
    author: 'इरफ़ान सिद्दीक़ी',
    text: `{shayari['text']}`,
  }},'''
        new_entries.append(entry)
        current_id += 1
    
    # Insert new entries
    new_content = content[:start_pos] + '\n' + '\n'.join(new_entries) + content[start_pos:]
    
    # Write back
    with open('shayari.js', 'w', encoding='utf-8') as f:
        f.write(new_content)
    
    print(f"Successfully added {len(new_shayari)} additional shayari by इरफ़ान सिद्दीक़ी!")
    print(f"New IDs: {last_id + 1} to {current_id - 1}")
else:
    print("Could not find insertion point")

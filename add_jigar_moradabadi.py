#!/usr/bin/env python3
"""Add Jigar Moradabadi shayari to the collection"""

import re

# Read the file
with open('shayari.js', 'r', encoding='utf-8') as f:
    content = f.read()

# Find the last ID
ids = re.findall(r'id:\s*(\d+),', content)
last_id = max([int(id) for id in ids]) if ids else 0
print(f"Last ID found: {last_id}")

# New shayari by Jigar Moradabadi
new_shayari = [
    {'category': 'sad', 'text': '''तेरी आँखों का कुछ क़ुसूर नहीं
हाँ मुझी को ख़राब होना था'''},
    {'category': 'romantic', 'text': '''तिरे जमाल की तस्वीर खींच दूँ लेकिन
ज़बाँ में आँख नहीं आँख में ज़बान नहीं'''},
    {'category': 'romantic', 'text': '''उस ने अपना बना के छोड़ दिया
क्या असीरी है क्या रिहाई है'''},
    {'category': 'romantic', 'text': '''मेरी निगाह-ए-शौक़ भी कुछ कम नहीं मगर
फिर भी तिरा शबाब तिरा ही शबाब है'''},
    {'category': 'life', 'text': '''आबाद अगर न दिल हो तो बरबाद कीजिए
गुलशन न बन सके तो बयाबाँ बनाइए'''},
    {'category': 'romantic', 'text': '''सुना है हश्र में हर आँख उसे बे-पर्दा देखेगी
मुझे डर है न तौहीन-ए-जमाल-ए-यार हो जाए'''},
    {'category': 'romantic', 'text': '''कभी उन मद-भरी आँखों से पिया था इक जाम
आज तक होश नहीं होश नहीं होश नहीं'''},
    {'category': 'romantic', 'text': '''वो चीज़ कहते हैं फ़िरदौस-ए-गुमशुदा जिस को
कभी कभी तिरी आँखों में पाई जाती है'''},
    {'category': 'romantic', 'text': '''कुछ इस अदा से आज वो पहलू-नशीं रहे
जब तक हमारे पास रहे हम नहीं रहे'''},
    {'category': 'romantic', 'text': '''मैं जहाँ हूँ तिरे ख़याल में हूँ
तू जहाँ है मिरी निगाह में है'''},
    {'category': 'romantic', 'text': '''मोहब्बत में हम तो जिए हैं जिएँगे
वो होंगे कोई और मर जाने वाले'''},
    {'category': 'romantic', 'text': '''कूचा-ए-इश्क़ में निकल आया
जिस को ख़ाना-ख़राब होना था'''},
    {'category': 'romantic', 'text': '''वो थे न मुझ से दूर न मैं उन से दूर था
आता न था नज़र तो नज़र का क़ुसूर था'''},
    {'category': 'romantic', 'text': '''लाखों में इंतिख़ाब के क़ाबिल बना दिया
जिस दिल को तुम ने देख लिया दिल बना दिया'''},
    {'category': 'romantic', 'text': '''लबों पे मौज-ए-तबस्सुम निगह में बर्क़-ए-ग़ज़ब
कोई बताए ये अंदाज़-ए-बरहमी क्या है'''},
    {'category': 'romantic', 'text': '''पी रहा हूँ आँखों आँखों में शराब
अब न शीशा है न कोई जाम है'''},
    {'category': 'romantic', 'text': '''आँखों में नूर जिस्म में बन कर वो जाँ रहे
या'नी हमीं में रह के वो हम से निहाँ रहे'''},
    {'category': 'sad', 'text': '''क्या ख़बर थी ख़लिश-ए-नाज़ न जीने देगी
ये तिरी प्यार की आवाज़ न जीने देगी'''},
    {'category': 'sad', 'text': '''निगाह-ए-यास मिरी काम कर गई अपना
रुला के उट्ठे थे वो मुस्कुरा के बैठ गए'''},
    {'category': 'romantic', 'text': '''नश्शा-ए-हुस्न को इस तरह उतरते देखा
ऐब पर अपने कोई जैसे पशेमाँ हो जाए'''}
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
    author: 'जिगर मुरादाबादी',
    text: `{shayari['text']}`,
  }},'''
        new_entries.append(entry)
        current_id += 1
    
    # Insert new entries
    new_content = content[:start_pos] + '\n' + '\n'.join(new_entries) + content[start_pos:]
    
    # Write back
    with open('shayari.js', 'w', encoding='utf-8') as f:
        f.write(new_content)
    
    print(f"Successfully added {len(new_shayari)} shayari by जिगर मुरादाबादी!")
    print(f"New IDs: {last_id + 1} to {current_id - 1}")
else:
    print("Could not find insertion point")

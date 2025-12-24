#!/usr/bin/env python3
"""Add Firaq Gorakhpuri shayari to the collection"""

import re

# Read the file
with open('shayari.js', 'r', encoding='utf-8') as f:
    content = f.read()

# Find the last ID
ids = re.findall(r'id:\s*(\d+),', content)
last_id = max([int(id) for id in ids]) if ids else 0
print(f"Last ID found: {last_id}")

# New shayari by Firaq Gorakhpuri
new_shayari = [
    {'category': 'romantic', 'text': '''एक मुद्दत से तिरी याद भी आई न हमें
और हम भूल गए हों तुझे ऐसा भी नहीं'''},
    {'category': 'sad', 'text': '''शाम भी थी धुआँ धुआँ हुस्न भी था उदास उदास
दिल को कई कहानियाँ याद सी आ के रह गईं'''},
    {'category': 'life', 'text': '''बहुत पहले से उन क़दमों की आहट जान लेते हैं
तुझे ऐ ज़िंदगी हम दूर से पहचान लेते हैं'''},
    {'category': 'romantic', 'text': '''तुम मुख़ातिब भी हो क़रीब भी हो
तुम को देखें कि तुम से बात करें'''},
    {'category': 'romantic', 'text': '''कोई समझे तो एक बात कहूँ
इश्क़ तौफ़ीक़ है गुनाह नहीं'''},
    {'category': 'sad', 'text': '''हम से क्या हो सका मोहब्बत में
ख़ैर तुम ने तो बेवफ़ाई की'''},
    {'category': 'life', 'text': '''आए थे हँसते खेलते मय-ख़ाने में 'फ़िराक़'
जब पी चुके शराब तो संजीदा हो गए'''},
    {'category': 'life', 'text': '''ग़रज़ कि काट दिए ज़िंदगी के दिन ऐ दोस्त
वो तेरी याद में हों या तुझे भुलाने में'''},
    {'category': 'sad', 'text': '''अब तो उन की याद भी आती नहीं
कितनी तन्हा हो गईं तन्हाइयाँ'''},
    {'category': 'romantic', 'text': '''सुनते हैं इश्क़ नाम के गुज़रे हैं इक बुज़ुर्ग
हम लोग भी फ़क़ीर उसी सिलसिले के हैं'''},
    {'category': 'romantic', 'text': '''रात भी नींद भी कहानी भी
हाए क्या चीज़ है जवानी भी'''},
    {'category': 'romantic', 'text': '''इक उम्र कट गई है तिरे इंतिज़ार में
ऐसे भी हैं कि कट न सकी जिन से एक रात'''},
    {'category': 'romantic', 'text': '''ज़रा विसाल के बाद आइना तो देख ऐ दोस्त
तिरे जमाल की दोशीज़गी निखर आई'''},
    {'category': 'sad', 'text': '''इसी खंडर में कहीं कुछ दिए हैं टूटे हुए
इन्हीं से काम चलाओ बड़ी उदास है रात'''},
    {'category': 'romantic', 'text': '''लाई न ऐसों-वैसों को ख़ातिर में आज तक
ऊँची है किस क़दर तिरी नीची निगाह भी'''},
    {'category': 'romantic', 'text': '''ज़ब्त कीजे तो दिल है अँगारा
और अगर रोइए तो पानी है'''},
    {'category': 'life', 'text': '''कौन ये ले रहा है अंगड़ाई
आसमानों को नींद आती है'''},
    {'category': 'life', 'text': '''कमी न की तिरे वहशी ने ख़ाक उड़ाने में
जुनूँ का नाम उछलता रहा ज़माने में'''}
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
    author: 'फ़िराक़ गोरखपुरी',
    text: `{shayari['text']}`,
  }},'''
        new_entries.append(entry)
        current_id += 1
    
    # Insert new entries
    new_content = content[:start_pos] + '\n' + '\n'.join(new_entries) + content[start_pos:]
    
    # Write back
    with open('shayari.js', 'w', encoding='utf-8') as f:
        f.write(new_content)
    
    print(f"Successfully added {len(new_shayari)} shayari by फ़िराक़ गोरखपुरी!")
    print(f"New IDs: {last_id + 1} to {current_id - 1}")
else:
    print("Could not find insertion point")

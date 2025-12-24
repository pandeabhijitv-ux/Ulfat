#!/usr/bin/env python3
"""Add Sahir Ludhianvi shayari to the collection"""

import re

# Read the file
with open('shayari.js', 'r', encoding='utf-8') as f:
    content = f.read()

# Find the last ID
ids = re.findall(r'id:\s*(\d+),', content)
last_id = max([int(id) for id in ids]) if ids else 0
print(f"Last ID found: {last_id}")

# New shayari by Sahir Ludhianvi
new_shayari = [
    {'category': 'life', 'text': '''ले दे के अपने पास फ़क़त इक नज़र तो है
क्यूँ देखें ज़िंदगी को किसी की नज़र से हम'''},
    {'category': 'life', 'text': '''ग़म और ख़ुशी में फ़र्क़ न महसूस हो जहाँ
मैं दिल को उस मक़ाम पे लाता चला गया'''},
    {'category': 'romantic', 'text': '''तेरा मिलना ख़ुशी की बात सही
तुझ से मिल कर उदास रहता हूँ'''},
    {'category': 'life', 'text': '''देखा है ज़िंदगी को कुछ इतने क़रीब से
चेहरे तमाम लगने लगे हैं अजीब से'''},
    {'category': 'life', 'text': '''इक शहंशाह ने दौलत का सहारा ले कर
हम ग़रीबों की मोहब्बत का उड़ाया है मज़ाक़'''},
    {'category': 'sad', 'text': '''चंद कलियाँ नशात की चुन कर मुद्दतों महव-ए-यास रहता हूँ
तेरा मिलना ख़ुशी की बात सही तुझ से मिल कर उदास रहता हूँ'''},
    {'category': 'life', 'text': '''तंग आ चुके हैं कशमकश-ए-ज़िंदगी से हम
ठुकरा न दें जहाँ को कहीं बे-दिली से हम'''},
    {'category': 'life', 'text': '''दुनिया ने तजरबात ओ हवादिस की शक्ल में
जो कुछ मुझे दिया है वो लौटा रहा हूँ मैं'''},
    {'category': 'romantic', 'text': '''अपनी तबाहियों का मुझे कोई ग़म नहीं
तुम ने किसी के साथ मोहब्बत निभा तो दी'''},
    {'category': 'romantic', 'text': '''तू मुझे छोड़ के ठुकरा के भी जा सकती है
तेरे हाथों में मिरे हाथ हैं ज़ंजीर नहीं'''},
    {'category': 'sad', 'text': '''हम ग़म-ज़दा हैं लाएँ कहाँ से ख़ुशी के गीत
देंगे वही जो पाएँगे इस ज़िंदगी से हम'''},
    {'category': 'life', 'text': '''अभी ज़िंदा हूँ लेकिन सोचता रहता हूँ ख़ल्वत में
कि अब तक किस तमन्ना के सहारे जी लिया मैं ने'''},
    {'category': 'life', 'text': '''ऐ ग़म-ए-दुनिया तुझे क्या इल्म तेरे वास्ते
किन बहानों से तबीअ'त राह पर लाई गई'''},
    {'category': 'sad', 'text': '''मोहब्बत तर्क की मैं ने गरेबाँ सी लिया मैं ने
ज़माने अब तो ख़ुश हो ज़हर ये भी पी लिया मैं ने'''},
    {'category': 'romantic', 'text': '''इस तरह निगाहें मत फेरो, ऐसा न हो धड़कन रुक जाए
सीने में कोई पत्थर तो नहीं एहसास का मारा, दिल ही तो है'''},
    {'category': 'life', 'text': '''अँधेरी शब में भी तामीर-ए-आशियाँ न रुके
नहीं चराग़ तो क्या बर्क़ तो चमकती है'''},
    {'category': 'sad', 'text': '''बहुत घुटन है कोई सूरत-ए-बयाँ निकले
अगर सदा न उठे कम से कम फ़ुग़ाँ निकले'''}
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
    author: 'साहिर लुधियानवी',
    text: `{shayari['text']}`,
  }},'''
        new_entries.append(entry)
        current_id += 1
    
    # Insert new entries
    new_content = content[:start_pos] + '\n' + '\n'.join(new_entries) + content[start_pos:]
    
    # Write back
    with open('shayari.js', 'w', encoding='utf-8') as f:
        f.write(new_content)
    
    print(f"Successfully added {len(new_shayari)} shayari by साहिर लुधियानवी!")
    print(f"New IDs: {last_id + 1} to {current_id - 1}")
else:
    print("Could not find insertion point")

#!/usr/bin/env python3
"""Add Shahryar shayari to the collection"""

import re

# Read the file
with open('shayari.js', 'r', encoding='utf-8') as f:
    content = f.read()

# Find the last ID
ids = re.findall(r'id:\s*(\d+),', content)
last_id = max([int(id) for id in ids]) if ids else 0
print(f"Last ID found: {last_id}")

# New shayari by Shahryar
new_shayari = [
    {'category': 'romantic', 'text': '''शदीद प्यास थी फिर भी छुआ न पानी को
मैं देखता रहा दरिया तिरी रवानी को'''},
    {'category': 'romantic', 'text': '''जहाँ में होने को ऐ दोस्त यूँ तो सब होगा
तिरे लबों पे मिरे लब हों ऐसा कब होगा'''},
    {'category': 'life', 'text': '''जुस्तुजू जिस की थी उस को तो न पाया हम ने
इस बहाने से मगर देख ली दुनिया हम ने'''},
    {'category': 'romantic', 'text': '''सियाह रात नहीं लेती नाम ढलने का
यही तो वक़्त है सूरज तिरे निकलने का'''},
    {'category': 'life', 'text': '''क्या कोई नई बात नज़र आती है हम में
आईना हमें देख के हैरान सा क्यूँ है'''},
    {'category': 'sad', 'text': '''शिकवा कोई दरिया की रवानी से नहीं है
रिश्ता ही मिरी प्यास का पानी से नहीं है'''},
    {'category': 'life', 'text': '''घर की तामीर तसव्वुर ही में हो सकती है
अपने नक़्शे के मुताबिक़ ये ज़मीं कुछ कम है'''},
    {'category': 'romantic', 'text': '''ये क्या है मोहब्बत में तो ऐसा नहीं होता
मैं तुझ से जुदा हो के भी तन्हा नहीं होता'''},
    {'category': 'romantic', 'text': '''या तेरे अलावा भी किसी शय की तलब है
या अपनी मोहब्बत पे भरोसा नहीं हम को'''},
    {'category': 'life', 'text': '''जम्अ करते रहे जो अपने को ज़र्रा ज़र्रा
वो ये क्या जानें बिखरने में सुकूँ कितना है'''},
    {'category': 'life', 'text': '''उम्र का लम्बा हिस्सा कर के दानाई के नाम
हम भी अब ये सोच रहे हैं पागल हो जाएँ'''},
    {'category': 'life', 'text': '''सभी को ग़म है समुंदर के ख़ुश्क होने का
कि खेल ख़त्म हुआ कश्तियाँ डुबोने का'''},
    {'category': 'life', 'text': '''इक बूँद ज़हर के लिए फैला रहे हो हाथ
देखो कभी ख़ुद अपने बदन को निचोड़ के'''},
    {'category': 'sad', 'text': '''पहले नहाई ओस में फिर आँसुओं में रात
यूँ बूँद बूँद उतरी हमारे घरों में रात'''},
    {'category': 'life', 'text': '''अब रात की दीवार को ढाना है ज़रूरी
ये काम मगर मुझ से अकेले नहीं होगा'''},
    {'category': 'sad', 'text': '''आँख की ये एक हसरत थी कि बस पूरी हुई
आँसुओं में भीग जाने की हवस पूरी हुई'''},
    {'category': 'sad', 'text': '''आसमाँ कुछ भी नहीं अब तेरे करने के लिए
मैं ने सब तय्यारियाँ कर ली हैं मरने के लिए'''},
    {'category': 'romantic', 'text': '''ये जब है कि इक ख़्वाब से रिश्ता है हमारा
दिन ढलते ही दिल डूबने लगता है हमारा'''},
    {'category': 'romantic', 'text': '''तू कहाँ है तुझ से इक निस्बत थी मेरी ज़ात को
कब से पलकों पर उठाए फिर रहा हूँ रात को'''},
    {'category': 'romantic', 'text': '''आँखों में तेरी देख रहा हूँ मैं अपनी शक्ल
ये कोई वाहिमा ये कोई ख़्वाब तो नहीं'''}
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
    author: 'शहरयार',
    text: `{shayari['text']}`,
  }},'''
        new_entries.append(entry)
        current_id += 1
    
    # Insert new entries
    new_content = content[:start_pos] + '\n' + '\n'.join(new_entries) + content[start_pos:]
    
    # Write back
    with open('shayari.js', 'w', encoding='utf-8') as f:
        f.write(new_content)
    
    print(f"Successfully added {len(new_shayari)} shayari by शहरयार!")
    print(f"New IDs: {last_id + 1} to {current_id - 1}")
else:
    print("Could not find insertion point")

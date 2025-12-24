#!/usr/bin/env python3
"""Add Zeb Ghauri shayari to the collection"""

import re

# Read the file
with open('shayari.js', 'r', encoding='utf-8') as f:
    content = f.read()

# Find the last ID
ids = re.findall(r'id:\s*(\d+),', content)
last_id = max([int(id) for id in ids]) if ids else 0
print(f"Last ID found: {last_id}")

# New shayari by Zeb Ghauri
new_shayari = [
    {'category': 'life', 'text': '''ज़ख़्म लगा कर उस का भी कुछ हाथ खुला
मैं भी धोका खा कर कुछ चालाक हुआ'''},
    {'category': 'life', 'text': '''बड़े अज़ाब में हूँ मुझ को जान भी है अज़ीज़
सितम को देख के चुप भी रहा नहीं जाता'''},
    {'category': 'romantic', 'text': '''दिल है कि तिरी याद से ख़ाली नहीं रहता
शायद ही कभी मैं ने तुझे याद किया हो'''},
    {'category': 'romantic', 'text': '''मिरी जगह कोई आईना रख लिया होता
न जाने तेरे तमाशे में मेरा काम है क्या'''},
    {'category': 'sad', 'text': '''दिल को सँभाले हँसता बोलता रहता हूँ लेकिन
सच पूछो तो 'ज़ेब' तबीअत ठीक नहीं होती'''},
    {'category': 'sad', 'text': '''अधूरी छोड़ के तस्वीर मर गया वो 'ज़ेब'
कोई भी रंग मयस्सर न था लहू के सिवा'''},
    {'category': 'life', 'text': '''घसीटते हुए ख़ुद को फिरोगे 'ज़ेब' कहाँ
चलो कि ख़ाक को दे आएँ ये बदन उस का'''},
    {'category': 'romantic', 'text': '''जाग के मेरे साथ समुंदर रातें करता है
जब सब लोग चले जाएँ तो बातें करता है'''},
    {'category': 'romantic', 'text': '''ये कम है क्या कि मिरे पास बैठा रहता है
वो जब तलक मिरे दिल को दुखा नहीं जाता'''},
    {'category': 'life', 'text': '''मैं तो चाक पे कूज़ा-गर के हाथ की मिट्टी हूँ
अब ये मिट्टी देख खिलौना कैसे बनती है'''},
    {'category': 'romantic', 'text': '''ये डूबती हुई क्या शय है तेरी आँखों में
तिरे लबों पे जो रौशन है उस का नाम है क्या'''},
    {'category': 'sad', 'text': '''खुली छतों से चाँदनी रातें कतरा जाएँगी
कुछ हम भी तन्हाई के आदी हो जाएँगे'''},
    {'category': 'life', 'text': '''उलट रही थीं हवाएँ वरक़ वरक़ उस का
लिखी गई थी जो मिट्टी पे वो किताब था वो'''},
    {'category': 'romantic', 'text': '''न जाने क्या है कि जब भी मैं उस को देखता हूँ
तो कोई और मिरे रू-ब-रू निकलता है'''},
    {'category': 'sad', 'text': '''धो के तू मेरा लहू अपने हुनर को न छुपा
कि ये सुर्ख़ी तिरी शमशीर का जौहर ही तो है'''},
    {'category': 'sad', 'text': '''एक झोंका हवा का आया 'ज़ेब'
और फिर मैं ग़ुबार भी न रहा'''},
    {'category': 'sad', 'text': '''देख कभी आ कर ये ला-महदूद फ़ज़ा
तू भी मेरी तन्हाई में शामिल हो'''}
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
    author: 'ज़ेब ग़ौरी',
    text: `{shayari['text']}`,
  }},'''
        new_entries.append(entry)
        current_id += 1
    
    # Insert new entries
    new_content = content[:start_pos] + '\n' + '\n'.join(new_entries) + content[start_pos:]
    
    # Write back
    with open('shayari.js', 'w', encoding='utf-8') as f:
        f.write(new_content)
    
    print(f"Successfully added {len(new_shayari)} shayari by ज़ेब ग़ौरी!")
    print(f"New IDs: {last_id + 1} to {current_id - 1}")
else:
    print("Could not find insertion point")

#!/usr/bin/env python3
"""Add Mir Taqi Mir shayari to the collection"""

import re

# Read the file
with open('shayari.js', 'r', encoding='utf-8') as f:
    content = f.read()

# Find the last ID
ids = re.findall(r'id:\s*(\d+),', content)
last_id = max([int(id) for id in ids]) if ids else 0
print(f"Last ID found: {last_id}")

# New shayari by Mir Taqi Mir
new_shayari = [
    {'category': 'romantic', 'text': '''नाज़ुकी उस के लब की क्या कहिए
पंखुड़ी इक गुलाब की सी है'''},
    {'category': 'romantic', 'text': '''आग थे इब्तिदा-ए-इश्क़ में हम
अब जो हैं ख़ाक इंतिहा है ये'''},
    {'category': 'life', 'text': '''ले साँस भी आहिस्ता कि नाज़ुक है बहुत काम
आफ़ाक़ की इस कारगह-ए-शीशागरी का'''},
    {'category': 'sad', 'text': '''बे-ख़ुदी ले गई कहाँ हम को
देर से इंतिज़ार है अपना'''},
    {'category': 'romantic', 'text': '''दिखाई दिए यूँ कि बे-ख़ुद किया
हमें आप से भी जुदा कर चले'''},
    {'category': 'romantic', 'text': '''हमारे आगे तिरा जब किसू ने नाम लिया
दिल-ए-सितम-ज़दा को हम ने थाम थाम लिया'''},
    {'category': 'life', 'text': '''गुफ़्तुगू रेख़्ते में हम से न कर
ये हमारी ज़बान है प्यारे'''},
    {'category': 'sad', 'text': '''हम जानते तो इश्क़ न करते किसू के साथ
ले जाते दिल को ख़ाक में इस आरज़ू के साथ'''},
    {'category': 'life', 'text': '''आफ़ाक़ की मंज़िल से गया कौन सलामत
अस्बाब लुटा राह में याँ हर सफ़री का'''},
    {'category': 'sad', 'text': '''किन नींदों अब तू सोती है ऐ चश्म-ए-गिर्या-नाक
मिज़्गाँ तो खोल शहर को सैलाब ले गया'''},
    {'category': 'sad', 'text': '''जम गया ख़ूँ कफ़-ए-क़ातिल पे तिरा \'मीर\' ज़ि-बस
उन ने रो रो दिया कल हाथ को धोते धोते'''},
    {'category': 'romantic', 'text': '''अब के जुनूँ में फ़ासला शायद न कुछ रहे
दामन के चाक और गिरेबाँ के चाक में'''},
    {'category': 'sad', 'text': '''मसाइब और थे पर दिल का जाना
अजब इक सानेहा सा हो गया है'''},
    {'category': 'romantic', 'text': '''हम फ़क़ीरों से बे-अदाई क्या
आन बैठे जो तुम ने प्यार किया'''},
    {'category': 'romantic', 'text': '''हम न कहते थे कि नक़्श उस का नहीं नक़्क़ाश सहल
चाँद सारा लग गया तब नीम-रुख़ सूरत हुई'''},
    {'category': 'romantic', 'text': '''कुछ हो रहेगा इश्क़-ओ-हवस में भी इम्तियाज़
आया है अब मिज़ाज तिरा इम्तिहान पर'''},
    {'category': 'sad', 'text': '''बाल-ओ-पर भी गए बहार के साथ
अब तवक़्क़ो नहीं रिहाई की'''},
    {'category': 'romantic', 'text': '''आलम आलम इश्क़-ओ-जुनूँ है दुनिया दुनिया तोहमत है
दरिया दरिया रोता हूँ मैं सहरा सहरा वहशत है'''},
    {'category': 'life', 'text': '''इज्ज़-ओ-नियाज़ अपना अपनी तरफ़ है सारा
इस मुश्त-ए-ख़ाक को हम मसजूद जानते हैं'''},
    {'category': 'sad', 'text': '''कहना था किसू से कुछ तकता था किसू का मुँह
कल \'मीर\' खड़ा था याँ सच है कि दिवाना था'''}
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
    author: 'मीर तक़ी मीर',
    text: `{shayari['text']}`,
  }},'''
        new_entries.append(entry)
        current_id += 1
    
    # Insert new entries
    new_content = content[:start_pos] + '\n' + '\n'.join(new_entries) + content[start_pos:]
    
    # Write back
    with open('shayari.js', 'w', encoding='utf-8') as f:
        f.write(new_content)
    
    print(f"Successfully added {len(new_shayari)} shayari by मीर तक़ी मीर!")
    print(f"New IDs: {last_id + 1} to {current_id - 1}")
else:
    print("Could not find insertion point")

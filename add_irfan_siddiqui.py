#!/usr/bin/env python3
"""Add Irfan Siddiqui shayari to the collection"""

import re

# Read the file
with open('shayari.js', 'r', encoding='utf-8') as f:
    content = f.read()

# Find the last ID
ids = re.findall(r'id:\s*(\d+),', content)
last_id = max([int(id) for id in ids]) if ids else 0
print(f"Last ID found: {last_id}")

# New shayari by Irfan Siddiqui
new_shayari = [
    {'category': 'life', 'text': '''उठो ये मंज़र-ए-शब-ताब देखने के लिए
कि नींद शर्त नहीं ख़्वाब देखने के लिए'''},
    {'category': 'romantic', 'text': '''बदन में जैसे लहू ताज़ियाना हो गया है
उसे गले से लगाए ज़माना हो गया है'''},
    {'category': 'life', 'text': '''तुम परिंदों से ज़ियादा तो नहीं हो आज़ाद
शाम होने को है अब घर की तरफ़ लौट चलो'''},
    {'category': 'life', 'text': '''रात को जीत तो पाता नहीं लेकिन ये चराग़
कम से कम रात का नुक़सान बहुत करता है'''},
    {'category': 'life', 'text': '''होशियारी दिल-ए-नादान बहुत करता है
रंज कम सहता है एलान बहुत करता है'''},
    {'category': 'romantic', 'text': '''बदन के दोनों किनारों से जल रहा हूँ मैं
कि छू रहा हूँ तुझे और पिघल रहा हूँ मैं'''},
    {'category': 'life', 'text': '''सर अगर सर है तो नेज़ों से शिकायत कैसी
दिल अगर दिल है तो दरिया से बड़ा होना है'''},
    {'category': 'life', 'text': '''जो कुछ हुआ वो कैसे हुआ जानता हूँ मैं
जो कुछ नहीं हुआ वो बता क्यूँ नहीं हुआ'''},
    {'category': 'life', 'text': '''रेत पर थक के गिरा हूँ तो हवा पूछती है
आप इस दश्त में क्यूँ आए थे वहशत के बग़ैर'''},
    {'category': 'sad', 'text': '''हमें तो ख़ैर बिखरना ही था कभी न कभी
हवा-ए-ताज़ा का झोंका बहाना हो गया है'''},
    {'category': 'sad', 'text': '''अजब हरीफ़ था मेरे ही साथ डूब गया
मिरे सफ़ीने को ग़र्क़ाब देखने के लिए'''},
    {'category': 'life', 'text': '''सरहदें अच्छी कि सरहद पे न रुकना अच्छा
सोचिए आदमी अच्छा कि परिंदा अच्छा'''},
    {'category': 'romantic', 'text': '''अपने किस काम में लाएगा बताता भी नहीं
हम को औरों पे गँवाना भी नहीं चाहता है'''},
    {'category': 'life', 'text': '''मैं चाहता हूँ यहीं सारे फ़ैसले हो जाएँ
कि इस के ब'अद ये दुनिया कहाँ से लाऊँगा मैं'''},
    {'category': 'sad', 'text': '''हम ने देखा ही था दुनिया को अभी उस के बग़ैर
लीजिए बीच में फिर दीदा-ए-तर आ गए हैं'''},
    {'category': 'romantic', 'text': '''रूह को रूह से मिलने नहीं देता है बदन
ख़ैर ये बीच की दीवार गिरा चाहती है'''},
    {'category': 'romantic', 'text': '''कहा था तुम ने कि लाता है कौन इश्क़ की ताब
सो हम जवाब तुम्हारे सवाल ही के तो हैं'''},
    {'category': 'romantic', 'text': '''शोला-ए-इश्क़ बुझाना भी नहीं चाहता है
वो मगर ख़ुद को जलाना भी नहीं चाहता है'''},
    {'category': 'life', 'text': '''हमारे दिल को इक आज़ार है ऐसा नहीं लगता
कि हम दफ़्तर भी जाते हैं ग़ज़ल-ख़्वानी भी करते हैं'''},
    {'category': 'romantic', 'text': '''मगर गिरफ़्त में आता नहीं बदन उस का
ख़याल ढूँढता रहता है इस्तिआरा कोई'''}
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
    
    print(f"Successfully added {len(new_shayari)} shayari by इरफ़ान सिद्दीक़ी!")
    print(f"New IDs: {last_id + 1} to {current_id - 1}")
else:
    print("Could not find insertion point")

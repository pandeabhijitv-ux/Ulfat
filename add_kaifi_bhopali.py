#!/usr/bin/env python3
"""Add Kaifi Bhopali shayari to the collection"""

import re

# Read the file
with open('shayari.js', 'r', encoding='utf-8') as f:
    content = f.read()

# Find the last ID
ids = re.findall(r'id:\s*(\d+),', content)
last_id = max([int(id) for id in ids]) if ids else 0
print(f"Last ID found: {last_id}")

# New shayari by Kaifi Bhopali
new_shayari = [
    {'category': 'life', 'text': '''ज़िंदगी शायद इसी का नाम है
दूरियाँ मजबूरियाँ तन्हाइयाँ'''},
    {'category': 'romantic', 'text': '''तुझे कौन जानता था मिरी दोस्ती से पहले
तिरा हुस्न कुछ नहीं था मिरी शाइरी से पहले'''},
    {'category': 'sad', 'text': '''कौन आएगा यहाँ कोई न आया होगा
मेरा दरवाज़ा हवाओं ने हिलाया होगा'''},
    {'category': 'life', 'text': '''आग का क्या है पल दो पल में लगती है
बुझते बुझते एक ज़माना लगता है'''},
    {'category': 'life', 'text': '''साया है कम खजूर के ऊँचे दरख़्त का
उम्मीद बाँधिए न बड़े आदमी के साथ'''},
    {'category': 'life', 'text': '''माँ की आग़ोश में कल मौत की आग़ोश में आज
हम को दुनिया में ये दो वक़्त सुहाने से मिले'''},
    {'category': 'sad', 'text': '''इक नया ज़ख़्म मिला एक नई उम्र मिली
जब किसी शहर में कुछ यार पुराने से मिले'''},
    {'category': 'life', 'text': '''गुल से लिपटी हुई तितली को गिरा कर देखो
आँधियो तुम ने दरख़्तों को गिराया होगा'''},
    {'category': 'romantic', 'text': '''इधर आ रक़ीब मेरे मैं तुझे गले लगा लूँ
मिरा इश्क़ बे-मज़ा था तिरी दुश्मनी से पहले'''},
    {'category': 'life', 'text': '''जनाब-ए-'कैफ़' ये दिल्ली है 'मीर' ओ 'ग़ालिब' की
यहाँ किसी की तरफ़-दारियाँ नहीं चलतीं'''},
    {'category': 'sad', 'text': '''\'कैफ़\' परदेस में मत याद करो अपना मकाँ
अब के बारिश ने उसे तोड़ गिराया होगा'''},
    {'category': 'life', 'text': '''वो दिन भी हाए क्या दिन थे जब अपना भी तअल्लुक़ था
दशहरे से दिवाली से बसंतों से बहारों से'''},
    {'category': 'romantic', 'text': '''कुछ मोहब्बत को न था चैन से रखना मंज़ूर
और कुछ उन की इनायात ने जीने न दिया'''},
    {'category': 'life', 'text': '''जिस दिन मिरी जबीं किसी दहलीज़ पर झुके
उस दिन ख़ुदा शिगाफ़ मिरे सर में डाल दे'''},
    {'category': 'sad', 'text': '''दर-ओ-दीवार पे शक्लें सी बनाने आई
फिर ये बारिश मिरी तंहाई चुराने आई'''},
    {'category': 'sad', 'text': '''मत देख कि फिरता हूँ तिरे हिज्र में ज़िंदा
ये पूछ कि जीने में मज़ा है कि नहीं है'''},
    {'category': 'romantic', 'text': '''चाहता हूँ फूँक दूँ इस शहर को
शहर में इन का भी घर है क्या करूँ'''},
    {'category': 'life', 'text': '''चार जानिब देख कर सच बोलिए
आदमी फिरते हैं सरकारी बहुत'''},
    {'category': 'sad', 'text': '''उन से मिल कर और भी कुछ बढ़ गईं
उलझनें फ़िक्रें क़यास-आराइयाँ'''},
    {'category': 'romantic', 'text': '''थोड़ा सा अक्स चाँद के पैकर में डाल दे
तू आ के जान रात के मंज़र में डाल दे'''}
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
    author: 'कैफ़ भोपाली',
    text: `{shayari['text']}`,
  }},'''
        new_entries.append(entry)
        current_id += 1
    
    # Insert new entries
    new_content = content[:start_pos] + '\n' + '\n'.join(new_entries) + content[start_pos:]
    
    # Write back
    with open('shayari.js', 'w', encoding='utf-8') as f:
        f.write(new_content)
    
    print(f"Successfully added {len(new_shayari)} shayari by कैफ़ भोपाली!")
    print(f"New IDs: {last_id + 1} to {current_id - 1}")
else:
    print("Could not find insertion point")

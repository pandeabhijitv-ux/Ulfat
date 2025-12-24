#!/usr/bin/env python3
"""Add Akbar Allahabadi shayari to the collection"""

import re

# Read the file
with open('shayari.js', 'r', encoding='utf-8') as f:
    content = f.read()

# Find the last ID
ids = re.findall(r'id:\s*(\d+),', content)
last_id = max([int(id) for id in ids]) if ids else 0
print(f"Last ID found: {last_id}")

# New shayari by Akbar Allahabadi (satirical/humorous poet)
new_shayari = [
    {'category': 'life', 'text': '''हम आह भी करते हैं तो हो जाते हैं बदनाम
वो क़त्ल भी करते हैं तो चर्चा नहीं होता'''},
    {'category': 'romantic', 'text': '''इश्क़ नाज़ुक-मिज़ाज है बेहद
अक़्ल का बोझ उठा नहीं सकता'''},
    {'category': 'life', 'text': '''दुनिया में हूँ दुनिया का तलबगार नहीं हूँ
बाज़ार से गुज़रा हूँ ख़रीदार नहीं हूँ'''},
    {'category': 'life', 'text': '''पैदा हुआ वकील तो शैतान ने कहा
लो आज हम भी साहिब-ए-औलाद हो गए'''},
    {'category': 'romantic', 'text': '''हया से सर झुका लेना अदा से मुस्कुरा देना
हसीनों को भी कितना सहल है बिजली गिरा देना'''},
    {'category': 'life', 'text': '''मज़हबी बहस मैं ने की ही नहीं
फ़ालतू अक़्ल मुझ में थी ही नहीं'''},
    {'category': 'romantic', 'text': '''जो कहा मैं ने कि प्यार आता है मुझ को तुम पर
हँस के कहने लगा और आप को आता क्या है'''},
    {'category': 'life', 'text': '''रहता है इबादत में हमें मौत का खटका
हम याद-ए-ख़ुदा करते हैं कर ले न ख़ुदा याद'''},
    {'category': 'life', 'text': '''अकबर दबे नहीं किसी सुल्ताँ की फ़ौज से
लेकिन शहीद हो गए बीवी की नौज से'''},
    {'category': 'life', 'text': '''हम ऐसी कुल किताबें क़ाबिल-ए-ज़ब्ती समझते हैं
कि जिन को पढ़ के लड़के बाप को ख़ब्ती समझते हैं'''},
    {'category': 'life', 'text': '''मैं भी ग्रेजुएट हूँ तुम भी ग्रेजुएट
इल्मी मुबाहिसे हों ज़रा पास आ के लेट'''},
    {'category': 'life', 'text': '''हंगामा है क्यूँ बरपा थोड़ी सी जो पी ली है
डाका तो नहीं मारा चोरी तो नहीं की है'''},
    {'category': 'life', 'text': '''बी.ए भी पास हों मिले बी-बी भी दिल-पसंद
मेहनत की है वो बात ये क़िस्मत की बात है'''},
    {'category': 'romantic', 'text': '''लिपट भी जा न रुक 'अकबर' ग़ज़ब की ब्यूटी है
नहीं नहीं पे न जा ये हया की ड्यूटी है'''},
    {'category': 'life', 'text': '''हक़ीक़ी और मजाज़ी शायरी में फ़र्क़ ये पाया
कि वो जामे से बाहर है ये पाजामे से बाहर है'''},
    {'category': 'life', 'text': '''इस क़दर था खटमलों का चारपाई में हुजूम
वस्ल का दिल से मिरे अरमान रुख़्सत हो गया'''},
    {'category': 'life', 'text': '''कोट और पतलून जब पहना तो मिस्टर बन गया
जब कोई तक़रीर की जलसे में लीडर बन गया'''},
    {'category': 'life', 'text': '''धमका के बोसे लूँगा रुख़-ए-रश्क-ए-माह का
चंदा वसूल होता है साहब दबाव से'''}
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
    author: 'अकबर इलाहाबादी',
    text: `{shayari['text']}`,
  }},'''
        new_entries.append(entry)
        current_id += 1
    
    # Insert new entries
    new_content = content[:start_pos] + '\n' + '\n'.join(new_entries) + content[start_pos:]
    
    # Write back
    with open('shayari.js', 'w', encoding='utf-8') as f:
        f.write(new_content)
    
    print(f"✅ Successfully added {len(new_shayari)} shayari by अकबर इलाहाबादी!")
    print(f"New IDs: {last_id + 1} to {current_id - 1}")
else:
    print("❌ Could not find insertion point")

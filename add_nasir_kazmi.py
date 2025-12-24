#!/usr/bin/env python3
"""Add Nasir Kazmi shayari to the collection"""

import re

# Read the file
with open('shayari.js', 'r', encoding='utf-8') as f:
    content = f.read()

# Find the last ID
ids = re.findall(r'id:\s*(\d+),', content)
last_id = max([int(id) for id in ids]) if ids else 0
print(f"Last ID found: {last_id}")

# New shayari by Nasir Kazmi
new_shayari = [
    {'category': 'romantic', 'text': '''आज देखा है तुझ को देर के बअ'द
आज का दिन गुज़र न जाए कहीं'''},
    {'category': 'romantic', 'text': '''ऐ दोस्त हम ने तर्क-ए-मोहब्बत के बावजूद
महसूस की है तेरी ज़रूरत कभी कभी'''},
    {'category': 'romantic', 'text': '''आरज़ू है कि तू यहाँ आए
और फिर उम्र भर न जाए कहीं'''},
    {'category': 'sad', 'text': '''जुदाइयों के ज़ख़्म दर्द-ए-ज़िंदगी ने भर दिए
तुझे भी नींद आ गई मुझे भी सब्र आ गया'''},
    {'category': 'sad', 'text': '''मुझे ये डर है तिरी आरज़ू न मिट जाए
बहुत दिनों से तबीअत मिरी उदास नहीं'''},
    {'category': 'sad', 'text': '''ज़रा सी बात सही तेरा याद आ जाना
ज़रा सी बात बहुत देर तक रुलाती थी'''},
    {'category': 'sad', 'text': '''याद है अब तक तुझ से बिछड़ने की वो अँधेरी शाम मुझे
तू ख़ामोश खड़ा था लेकिन बातें करता था काजल'''},
    {'category': 'sad', 'text': '''आज तो बे-सबब उदास है जी
इश्क़ होता तो कोई बात भी थी'''},
    {'category': 'romantic', 'text': '''इस शहर-ए-बे-चराग़ में जाएगी तू कहाँ
आ ऐ शब-ए-फ़िराक़ तुझे घर ही ले चलें'''},
    {'category': 'romantic', 'text': '''उस ने मंज़िल पे ला के छोड़ दिया
उम्र भर जिस का रास्ता देखा'''},
    {'category': 'sad', 'text': '''कुछ यादगार-ए-शहर-ए-सितमगर ही ले चलें
आए हैं इस गली में तो पत्थर ही ले चलें'''},
    {'category': 'sad', 'text': '''वो रात का बे-नवा मुसाफ़िर वो तेरा शाइर वो तेरा 'नासिर'
तिरी गली तक तो हम ने देखा था फिर न जाने किधर गया वो'''},
    {'category': 'life', 'text': '''यूँ तो हर शख़्स अकेला है भरी दुनिया में
फिर भी हर दिल के मुक़द्दर में नहीं तन्हाई'''},
    {'category': 'life', 'text': '''कल जो था वो आज नहीं जो आज है कल मिट जाएगा
रूखी-सूखी जो मिल जाए शुक्र करो तो बेहतर है'''},
    {'category': 'romantic', 'text': '''मैं सोते सोते कई बार चौंक चौंक पड़ा
तमाम रात तिरे पहलुओं से आँच आई'''},
    {'category': 'sad', 'text': '''ज़िंदगी जिन के तसव्वुर से जिला पाती थी
हाए क्या लोग थे जो दाम-ए-अजल में आए'''},
    {'category': 'sad', 'text': '''मुद्दत से कोई आया न गया सुनसान पड़ी है घर की फ़ज़ा
इन ख़ाली कमरों में 'नासिर' अब शम्अ जलाऊँ किस के लिए'''},
    {'category': 'romantic', 'text': '''तिरे फ़िराक़ की रातें कभी न भूलेंगी
मज़े मिले उन्हीं रातों में उम्र भर के मुझे'''},
    {'category': 'romantic', 'text': '''आँच आती है तिरे जिस्म की उर्यानी से
पैरहन है कि सुलगती हुई शब है कोई'''},
    {'category': 'life', 'text': '''सारा दिन तपते सूरज की गर्मी में जलते रहे
ठंडी ठंडी हवा फिर चली सो रहो सो रहो'''}
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
    author: 'नासिर काज़मी',
    text: `{shayari['text']}`,
  }},'''
        new_entries.append(entry)
        current_id += 1
    
    # Insert new entries
    new_content = content[:start_pos] + '\n' + '\n'.join(new_entries) + content[start_pos:]
    
    # Write back
    with open('shayari.js', 'w', encoding='utf-8') as f:
        f.write(new_content)
    
    print(f"Successfully added {len(new_shayari)} shayari by नासिर काज़मी!")
    print(f"New IDs: {last_id + 1} to {current_id - 1}")
else:
    print("Could not find insertion point")

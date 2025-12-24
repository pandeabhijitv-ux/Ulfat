#!/usr/bin/env python3
"""Add Adil Mansuri shayari to the collection"""

import re

# Read the file
with open('shayari.js', 'r', encoding='utf-8') as f:
    content = f.read()

# Find the last ID
ids = re.findall(r'id:\s*(\d+),', content)
last_id = max([int(id) for id in ids]) if ids else 0
print(f"Last ID found: {last_id}")

# New shayari by Adil Mansuri
new_shayari = [
    {'category': 'sad', 'text': '''मेरे टूटे हौसले के पर निकलते देख कर
उस ने दीवारों को अपनी और ऊँचा कर दिया'''},
    {'category': 'romantic', 'text': '''किस तरह जमा कीजिए अब अपने आप को
काग़ज़ बिखर रहे हैं पुरानी किताब के'''},
    {'category': 'sad', 'text': '''वो कौन था जो दिन के उजाले में खो गया
ये चाँद किस को ढूँडने निकला है शाम से'''},
    {'category': 'sad', 'text': '''कोई ख़ुद-कुशी की तरफ़ चल दिया
उदासी की मेहनत ठिकाने लगी'''},
    {'category': 'sad', 'text': '''जो चुप-चाप रहती थी दीवार पर
वो तस्वीर बातें बनाने लगी'''},
    {'category': 'romantic', 'text': '''जीता है सिर्फ़ तेरे लिए कौन मर के देख
इक रोज़ मेरी जान ये हरकत भी कर के देख'''},
    {'category': 'life', 'text': '''मुझे पसंद नहीं ऐसे कारोबार में हूँ
ये जब्र है कि मैं ख़ुद अपने इख़्तियार में हूँ'''},
    {'category': 'romantic', 'text': '''दरिया के किनारे पे मिरी लाश पड़ी थी
और पानी की तह में वो मुझे ढूँड रहा था'''},
    {'category': 'sad', 'text': '''कब तक पड़े रहोगे हवाओं के हाथ में
कब तक चलेगा खोखले शब्दों का कारोबार'''},
    {'category': 'sad', 'text': '''नींद भी जागती रही पूरे हुए न ख़्वाब भी
सुब्ह हुई ज़मीन पर रात ढली मज़ार में'''},
    {'category': 'sad', 'text': '''सोए तो दिल में एक जहाँ जागने लगा
जागे तो अपनी आँख में जाले थे ख़्वाब के'''},
    {'category': 'life', 'text': '''कभी ख़ाक वालों की बातें भी सुन
कभी आसमानों से नीचे उतर'''},
    {'category': 'life', 'text': '''अल्लाह जाने किस पे अकड़ता था रात दिन
कुछ भी नहीं था फिर भी बड़ा बद-ज़बान था'''},
    {'category': 'life', 'text': '''हम्माम के आईने में शब डूब रही थी
सिगरेट से नए दिन का धुआँ फैल रहा था'''},
    {'category': 'romantic', 'text': '''कब से टहल रहे हैं गरेबान खोल कर
ख़ाली घटा को क्या करें बरसात भी तो हो'''},
    {'category': 'life', 'text': '''बिस्मिल के तड़पने की अदाओं में नशा था
मैं हाथ में तलवार लिए झूम रहा था'''},
    {'category': 'life', 'text': '''हर आँख में थी टूटते लम्हों की तिश्नगी
हर जिस्म पे था वक़्त का साया पड़ा हुआ'''},
    {'category': 'life', 'text': '''जाने किस को ढूँडने दाख़िल हुआ है जिस्म में
हड्डियों में रास्ता करता हुआ पीला बुख़ार'''},
    {'category': 'sad', 'text': '''न कोई रोक सका ख़्वाब के सफ़ीरों को
उदास कर गए नींदों के राहगीरों को'''},
    {'category': 'sad', 'text': '''लहू में उतरती रही चाँदनी
बदन रात का कितना ठंडा लगा'''},
    {'category': 'life', 'text': '''फिर कोई वुसअत-ए-आफ़ाक़ पे साया डाले
फिर किसी आँख के नुक़्ते में उतारा जाऊँ'''}
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
    author: 'आदिल मंसूरी',
    text: `{shayari['text']}`,
  }},'''
        new_entries.append(entry)
        current_id += 1
    
    # Insert new entries
    new_content = content[:start_pos] + '\n' + '\n'.join(new_entries) + content[start_pos:]
    
    # Write back
    with open('shayari.js', 'w', encoding='utf-8') as f:
        f.write(new_content)
    
    print(f"Successfully added {len(new_shayari)} shayari by आदिल मंसूरी!")
    print(f"New IDs: {last_id + 1} to {current_id - 1}")
else:
    print("Could not find insertion point")

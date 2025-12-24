#!/usr/bin/env python3
"""Add Ubaidullah Aleem shayari to the collection"""

import re

# Read the file
with open('shayari.js', 'r', encoding='utf-8') as f:
    content = f.read()

# Find the last ID
ids = re.findall(r'id:\s*(\d+),', content)
last_id = max([int(id) for id in ids]) if ids else 0
print(f"Last ID found: {last_id}")

# New shayari by Ubaidullah Aleem
new_shayari = [
    {'category': 'romantic', 'text': '''अज़ीज़ इतना ही रक्खो कि जी सँभल जाए
अब इस क़दर भी न चाहो कि दम निकल जाए'''},
    {'category': 'life', 'text': '''हवा के दोश पे रक्खे हुए चराग़ हैं हम
जो बुझ गए तो हवा से शिकायतें कैसी'''},
    {'category': 'romantic', 'text': '''एक चेहरे में तो मुमकिन नहीं इतने चेहरे
किस से करते जो कोई इश्क़ दोबारा करते'''},
    {'category': 'life', 'text': '''जवानी क्या हुई इक रात की कहानी हुई
बदन पुराना हुआ रूह भी पुरानी हुई'''},
    {'category': 'sad', 'text': '''हज़ार तरह के सदमे उठाने वाले लोग
न जाने क्या हुआ इक आन में बिखर से गए'''},
    {'category': 'sad', 'text': '''हाए वो लोग गए चाँद से मिलने और फिर
अपने ही टूटे हुए ख़्वाब उठा कर ले आए'''},
    {'category': 'romantic', 'text': '''ज़मीं के लोग तो क्या दो दिलों की चाहत में
ख़ुदा भी हो तो उसे दरमियान लाओ मत'''},
    {'category': 'life', 'text': '''रौशनी आधी इधर आधी उधर
इक दिया रक्खा है दीवारों के बीच'''},
    {'category': 'sad', 'text': '''ये कैसी बिछड़ने की सज़ा है
आईने में चेहरा रख गया है'''},
    {'category': 'romantic', 'text': '''मैं उस को भूल गया हूँ वो मुझ को भूल गया
तो फिर ये दिल पे क्यूँ दस्तक सी ना-गहानी हुई'''},
    {'category': 'romantic', 'text': '''मैं एक से किसी मौसम में रह नहीं सकता
कभी विसाल कभी हिज्र से रिहाई दे'''},
    {'category': 'life', 'text': '''अगर हों कच्चे घरोंदों में आदमी आबाद
तो एक अब्र भी सैलाब के बराबर है'''},
    {'category': 'romantic', 'text': '''तुम अपने रंग नहाओ मैं अपनी मौज उड़ूँ
वो बात भूल भी जाओ जो आनी-जानी हुई'''},
    {'category': 'sad', 'text': '''शिकस्ता-हाल सा बे-आसरा सा लगता है
ये शहर दिल से ज़ियादा दुखा सा लगता है'''},
    {'category': 'life', 'text': '''जो आ रही है सदा ग़ौर से सुनो उस को
कि इस सदा में ख़ुदा बोलता सा लगता है'''},
    {'category': 'sad', 'text': '''मुझ से मिरा कोई मिलने वाला
बिछड़ा तो नहीं मगर मिला दे'''},
    {'category': 'life', 'text': '''खा गया इंसाँ को आशोब-ए-मआश
आ गए हैं शहर बाज़ारों के बीच'''},
    {'category': 'sad', 'text': '''दोस्तो जश्न मनाओ कि बहार आई है
फूल गिरते हैं हर इक शाख़ से आँसू की तरह'''}
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
    author: 'उबैदुल्लाह अलीम',
    text: `{shayari['text']}`,
  }},'''
        new_entries.append(entry)
        current_id += 1
    
    # Insert new entries
    new_content = content[:start_pos] + '\n' + '\n'.join(new_entries) + content[start_pos:]
    
    # Write back
    with open('shayari.js', 'w', encoding='utf-8') as f:
        f.write(new_content)
    
    print(f"Successfully added {len(new_shayari)} shayari by उबैदुल्लाह अलीम!")
    print(f"New IDs: {last_id + 1} to {current_id - 1}")
else:
    print("Could not find insertion point")

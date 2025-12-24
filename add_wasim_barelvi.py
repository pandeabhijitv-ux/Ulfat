#!/usr/bin/env python3
"""Add Wasim Barelvi shayari to the collection"""

import re

# Read the file
with open('shayari.js', 'r', encoding='utf-8') as f:
    content = f.read()

# Find the last ID
ids = re.findall(r'id:\s*(\d+),', content)
last_id = max([int(id) for id in ids]) if ids else 0
print(f"Last ID found: {last_id}")

# New shayari by Wasim Barelvi
new_shayari = [
    {
        'category': 'sad',
        'text': '''तुझे पाने की कोशिश में कुछ इतना खो चुका हूँ मैं
कि तू मिल भी अगर जाए तो अब मिलने का ग़म होगा'''
    },
    {
        'category': 'life',
        'text': '''जहाँ रहेगा वहीं रौशनी लुटाएगा
किसी चराग़ का अपना मकाँ नहीं होता'''
    },
    {
        'category': 'sad',
        'text': '''वो झूट बोल रहा था बड़े सलीक़े से
मैं ए'तिबार न करता तो और क्या करता'''
    },
    {
        'category': 'life',
        'text': '''रात तो वक़्त की पाबंद है ढल जाएगी
देखना ये है चराग़ों का सफ़र कितना है'''
    },
    {
        'category': 'sad',
        'text': '''वैसे तो इक आँसू ही बहा कर मुझे ले जाए
ऐसे कोई तूफ़ान हिला भी नहीं सकता'''
    },
    {
        'category': 'life',
        'text': '''शाम तक सुब्ह की नज़रों से उतर जाते हैं
इतने समझौतों पे जीते हैं कि मर जाते हैं'''
    },
    {
        'category': 'romantic',
        'text': '''मोहब्बत में बिछड़ने का हुनर सब को नहीं आता
किसी को छोड़ना हो तो मुलाक़ातें बड़ी करना'''
    },
    {
        'category': 'sad',
        'text': '''मुसलसल हादसों से बस मुझे इतनी शिकायत है
कि ये आँसू बहाने की भी तो मोहलत नहीं देते'''
    },
    {
        'category': 'sad',
        'text': '''मैं उस को आँसुओं से लिख रहा हूँ
कि मेरे ब'अद कोई पढ़ न पाए'''
    },
    {
        'category': 'romantic',
        'text': '''ऐसे रिश्ते का भरम रखना कोई खेल नहीं
तेरा होना भी नहीं और तिरा कहलाना भी'''
    },
    {
        'category': 'sad',
        'text': '''हमारे घर का पता पूछने से क्या हासिल
उदासियों की कोई शहरियत नहीं होती'''
    },
    {
        'category': 'life',
        'text': '''बहुत से ख़्वाब देखोगे तो आँखें
तुम्हारा साथ देना छोड़ देंगी'''
    },
    {
        'category': 'life',
        'text': '''थके-हारे परिंदे जब बसेरे के लिए लौटें
सलीक़ा-मंद शाख़ों का लचक जाना ज़रूरी है'''
    },
    {
        'category': 'romantic',
        'text': '''मैं जिन दिनों तिरे बारे में सोचता हूँ बहुत
उन्हीं दिनों तो ये दुनिया समझ में आती है'''
    },
    {
        'category': 'romantic',
        'text': '''जो मुझ में तुझ में चला आ रहा है बरसों से
कहीं हयात इसी फ़ासले का नाम न हो'''
    },
    {
        'category': 'romantic',
        'text': '''तिरे ख़याल के हाथों कुछ ऐसा बिखरा हूँ
कि जैसे बच्चा किताबें इधर उधर कर दे'''
    }
]

# Find the position to insert (before the closing bracket of hindiShayari array)
# Look for the pattern that marks end of hindi shayari
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
    author: 'वसीम बरेलवी',
    text: `{shayari['text']}`,
  }},'''
        new_entries.append(entry)
        current_id += 1
    
    # Insert new entries
    new_content = content[:start_pos] + '\n' + '\n'.join(new_entries) + content[start_pos:]
    
    # Write back
    with open('shayari.js', 'w', encoding='utf-8') as f:
        f.write(new_content)
    
    print(f"✅ Successfully added {len(new_shayari)} shayari by वसीम बरेलवी!")
    print(f"New IDs: {last_id + 1} to {current_id - 1}")
else:
    print("❌ Could not find insertion point")

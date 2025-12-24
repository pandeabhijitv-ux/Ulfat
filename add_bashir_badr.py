#!/usr/bin/env python3
"""Add Bashir Badr shayari to the collection"""

import re

# Read the file
with open('shayari.js', 'r', encoding='utf-8') as f:
    content = f.read()

# Find the last ID
ids = re.findall(r'id:\s*(\d+),', content)
last_id = max([int(id) for id in ids]) if ids else 0
print(f"Last ID found: {last_id}")

# New shayari by Bashir Badr
new_shayari = [
    {'category': 'life', 'text': '''उजाले अपनी यादों के हमारे साथ रहने दो
न जाने किस गली में ज़िंदगी की शाम हो जाए'''},
    {'category': 'life', 'text': '''हम भी दरिया हैं हमें अपना हुनर मालूम है
जिस तरफ़ भी चल पड़ेंगे रास्ता हो जाएगा'''},
    {'category': 'sad', 'text': '''ज़िंदगी तू ने मुझे क़ब्र से कम दी है ज़मीं
पाँव फैलाऊँ तो दीवार में सर लगता है'''},
    {'category': 'life', 'text': '''यहाँ लिबास की क़ीमत है आदमी की नहीं
मुझे गिलास बड़े दे शराब कम कर दे'''},
    {'category': 'sad', 'text': '''हम तो कुछ देर हँस भी लेते हैं
दिल हमेशा उदास रहता है'''},
    {'category': 'sad', 'text': '''लोग टूट जाते हैं एक घर बनाने में
तुम तरस नहीं खाते बस्तियाँ जलाने में'''},
    {'category': 'life', 'text': '''अभी राह में कई मोड़ हैं कोई आएगा कोई जाएगा
तुम्हें जिस ने दिल से भुला दिया उसे भूलने की दुआ करो'''},
    {'category': 'romantic', 'text': '''तुम्हारे साथ ये मौसम फ़रिश्तों जैसा है
तुम्हारे बा'द ये मौसम बहुत सताएगा'''},
    {'category': 'life', 'text': '''अगर फ़ुर्सत मिले पानी की तहरीरों को पढ़ लेना
हर इक दरिया हज़ारों साल का अफ़्साना लिखता है'''},
    {'category': 'sad', 'text': '''चराग़ों को आँखों में महफ़ूज़ रखना
बड़ी दूर तक रात ही रात होगी'''},
    {'category': 'romantic', 'text': '''अजीब शख़्स है नाराज़ हो के हँसता है
मैं चाहता हूँ ख़फ़ा हो तो वो ख़फ़ा ही लगे'''},
    {'category': 'romantic', 'text': '''ख़ुदा ऐसे एहसास का नाम है
रहे सामने और दिखाई न दे'''},
    {'category': 'romantic', 'text': '''आँखों में रहा दिल में उतर कर नहीं देखा
कश्ती के मुसाफ़िर ने समुंदर नहीं देखा'''},
    {'category': 'life', 'text': '''काग़ज़ में दब के मर गए कीड़े किताब के
दीवाना बे-पढ़े-लिखे मशहूर हो गया'''},
    {'category': 'life', 'text': '''वो इत्र-दान सा लहजा मिरे बुज़ुर्गों का
रची-बसी हुई उर्दू ज़बान की ख़ुश्बू'''},
    {'category': 'life', 'text': '''सब लोग अपने अपने ख़ुदाओं को लाए थे
इक हम ही ऐसे थे कि हमारा ख़ुदा न था'''},
    {'category': 'romantic', 'text': '''मैं ने दिन रात ख़ुदा से ये दुआ माँगी थी
कोई आहट न हो दर पर मिरे जब तू आए'''},
    {'category': 'sad', 'text': '''वो इंतिज़ार की चौखट पे सो गया होगा
किसी से वक़्त तो पूछें कि क्या बजा होगा'''}
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
    author: 'बशीर बद्र',
    text: `{shayari['text']}`,
  }},'''
        new_entries.append(entry)
        current_id += 1
    
    # Insert new entries
    new_content = content[:start_pos] + '\n' + '\n'.join(new_entries) + content[start_pos:]
    
    # Write back
    with open('shayari.js', 'w', encoding='utf-8') as f:
        f.write(new_content)
    
    print(f"Successfully added {len(new_shayari)} shayari by बशीर बद्र!")
    print(f"New IDs: {last_id + 1} to {current_id - 1}")
else:
    print("Could not find insertion point")

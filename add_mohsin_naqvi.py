#!/usr/bin/env python3
"""Add Mohsin Naqvi shayari to the collection"""

import re

# Read the file
with open('shayari.js', 'r', encoding='utf-8') as f:
    content = f.read()

# Find the last ID
ids = re.findall(r'id:\s*(\d+),', content)
last_id = max([int(id) for id in ids]) if ids else 0
print(f"Last ID found: {last_id}")

# New shayari by Mohsin Naqvi
new_shayari = [
    {'category': 'life', 'text': '''हर वक़्त का हँसना तुझे बर्बाद न कर दे
तन्हाई के लम्हों में कभी रो भी लिया कर'''},
    {'category': 'life', 'text': '''सिर्फ़ हाथों को न देखो कभी आँखें भी पढ़ो
कुछ सवाली बड़े ख़ुद्दार हुआ करते हैं'''},
    {'category': 'life', 'text': '''कल थके-हारे परिंदों ने नसीहत की मुझे
शाम ढल जाए तो 'मोहसिन' तुम भी घर जाया करो'''},
    {'category': 'romantic', 'text': '''वफ़ा की कौन सी मंज़िल पे उस ने छोड़ा था
कि वो तो याद हमें भूल कर भी आता है'''},
    {'category': 'sad', 'text': '''ये किस ने हम से लहू का ख़िराज फिर माँगा
अभी तो सोए थे मक़्तल को सुर्ख़-रू कर के'''},
    {'category': 'romantic', 'text': '''कितने लहजों के ग़िलाफ़ों में छुपाऊँ तुझ को
शहर वाले मिरा मौज़ू-ए-सुख़न जानते हैं'''},
    {'category': 'romantic', 'text': '''अब तक मिरी यादों से मिटाए नहीं मिटता
भीगी हुई इक शाम का मंज़र तिरी आँखें'''},
    {'category': 'sad', 'text': '''कहाँ मिलेगी मिसाल मेरी सितमगरी की
कि मैं गुलाबों के ज़ख़्म काँटों से सी रहा हूँ'''},
    {'category': 'sad', 'text': '''अब के बारिश में तो ये कार-ए-ज़ियाँ होना ही था
अपनी कच्ची बस्तियों को बे-निशाँ होना ही था'''},
    {'category': 'sad', 'text': '''जो दे सका न पहाड़ों को बर्फ़ की चादर
वो मेरी बाँझ ज़मीं को कपास क्या देगा'''},
    {'category': 'sad', 'text': '''सुना है शहर में ज़ख़्मी दिलों का मेला है
चलेंगे हम भी मगर पैरहन रफ़ू कर के'''},
    {'category': 'sad', 'text': '''मौसम-ए-ज़र्द में एक दिल को बचाऊँ कैसे
ऐसी रुत में तो घने पेड़ भी झड़ जाते हैं'''},
    {'category': 'life', 'text': '''ढलते सूरज की तमाज़त ने बिखर कर देखा
सर-कशीदा मिरा साया सफ़-ए-अशजार के बीच'''},
    {'category': 'life', 'text': '''हम अपनी धरती से अपनी हर सम्त ख़ुद तलाशें
हमारी ख़ातिर कोई सितारा नहीं चलेगा'''},
    {'category': 'life', 'text': '''वो मुझ से बढ़ के ज़ब्त का आदी था जी गया
वर्ना हर एक साँस क़यामत उसे भी थी'''},
    {'category': 'sad', 'text': '''पलट के आ गई ख़ेमे की सम्त प्यास मिरी
फटे हुए थे सभी बादलों के मश्कीज़े'''},
    {'category': 'romantic', 'text': '''बड़ी उम्र के बा'द इन आँखों में कोई अब्र उतरा तिरी यादों का
मिरे दिल की ज़मीं आबाद हुई मिरे ग़म का नगर शादाब हुआ'''},
    {'category': 'sad', 'text': '''दश्त-ए-हस्ती में शब-ए-ग़म की सहर करने को
हिज्र वालों ने लिया रख़्त-ए-सफ़र सन्नाटा'''},
    {'category': 'romantic', 'text': '''चुनती हैं मेरे अश्क रुतों की भिकारनें
'मोहसिन' लुटा रहा हूँ सर-ए-आम चाँदनी'''},
    {'category': 'life', 'text': '''जो अपनी ज़ात से बाहर न आ सका अब तक
वो पत्थरों को मता-ए-हवास क्या देगा'''}
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
    author: 'मोहसिन नक़वी',
    text: `{shayari['text']}`,
  }},'''
        new_entries.append(entry)
        current_id += 1
    
    # Insert new entries
    new_content = content[:start_pos] + '\n' + '\n'.join(new_entries) + content[start_pos:]
    
    # Write back
    with open('shayari.js', 'w', encoding='utf-8') as f:
        f.write(new_content)
    
    print(f"Successfully added {len(new_shayari)} shayari by मोहसिन नक़वी!")
    print(f"New IDs: {last_id + 1} to {current_id - 1}")
else:
    print("Could not find insertion point")

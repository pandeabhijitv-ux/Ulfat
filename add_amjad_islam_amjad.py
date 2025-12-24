#!/usr/bin/env python3
"""Add Amjad Islam Amjad shayari to the collection"""

import re

# Read the file
with open('shayari.js', 'r', encoding='utf-8') as f:
    content = f.read()

# Find the last ID
ids = re.findall(r'id:\s*(\d+),', content)
last_id = max([int(id) for id in ids]) if ids else 0
print(f"Last ID found: {last_id}")

# New shayari by Amjad Islam Amjad
new_shayari = [
    {'category': 'romantic', 'text': '''जिस तरफ़ तू है उधर होंगी सभी की नज़रें
ईद के चाँद का दीदार बहाना ही सही'''},
    {'category': 'romantic', 'text': '''चेहरे पे मिरे ज़ुल्फ़ को फैलाओ किसी दिन
क्या रोज़ गरजते हो बरस जाओ किसी दिन'''},
    {'category': 'life', 'text': '''क्या हो जाता है इन हँसते जीते जागते लोगों को
बैठे बैठे क्यूँ ये ख़ुद से बातें करने लगते हैं'''},
    {'category': 'sad', 'text': '''बड़े सुकून से डूबे थे डूबने वाले
जो साहिलों पे खड़े थे बहुत पुकारे भी'''},
    {'category': 'life', 'text': '''लिखा था एक तख़्ती पर कोई भी फूल मत तोड़े मगर आँधी तो अन-पढ़ थी
सो जब वो बाग़ से गुज़री कोई उखड़ा कोई टूटा ख़िज़ाँ के आख़िरी दिन थे'''},
    {'category': 'sad', 'text': '''जैसे बारिश से धुले सेहन-ए-गुलिस्ताँ 'अमजद'
आँख जब ख़ुश्क हुई और भी चेहरा चमका'''},
    {'category': 'romantic', 'text': '''किस क़दर यादें उभर आई हैं तेरे नाम से
एक पत्थर फेंकने से पड़ गए कितने भँवर'''},
    {'category': 'sad', 'text': '''हर समुंदर का एक साहिल है
हिज्र की रात का किनारा नहीं'''},
    {'category': 'romantic', 'text': '''गुज़रें जो मेरे घर से तो रुक जाएँ सितारे
इस तरह मिरी रात को चमकाओ किसी दिन'''},
    {'category': 'romantic', 'text': '''एक नज़र देखा था उस ने आगे याद नहीं
खुल जाती है दरिया की औक़ात समुंदर में'''},
    {'category': 'life', 'text': '''हादिसा भी होने में वक़्त कुछ तो लेता है
बख़्त के बिगड़ने में देर कुछ तो लगती है'''},
    {'category': 'sad', 'text': '''कुछ ऐसी बे-यक़ीनी थी फ़ज़ा में
जो अपने थे वो बेगाने लगे हैं'''},
    {'category': 'life', 'text': '''बे-समर पेड़ों को चूमेंगे सबा के सब्ज़ लब
देख लेना ये ख़िज़ाँ बे-दस्त-ओ-पा रह जाएगी'''},
    {'category': 'romantic', 'text': '''कमाल-ए-हुस्न है हुस्न-ए-कमाल से बाहर
अज़ल का रंग है जैसे मिसाल से बाहर'''},
    {'category': 'romantic', 'text': '''यूँ तो हर रात चमकते हैं सितारे लेकिन
वस्ल की रात बहुत सुब्ह का तारा चमका'''},
    {'category': 'life', 'text': '''ये जो साए से भटकते हैं हमारे इर्द-गिर्द
छू के उन को देखिए तो वाहिमा कोई नहीं'''},
    {'category': 'sad', 'text': '''आँख भी अपनी सराब-आलूद है
और इस दरिया में पानी भी नहीं'''},
    {'category': 'sad', 'text': '''दर्द का रस्ता है या है साअ'त-ए-रोज़-ए-हिसाब
सैकड़ों लोगों को रोका एक भी ठहरा नहीं'''},
    {'category': 'life', 'text': '''फ़ज़ा में तैरते रहते हैं नक़्श से क्या क्या
मुझे तलाश न करती हों ये बलाएँ कहीं'''},
    {'category': 'romantic', 'text': '''न उस का अंत है कोई न इस्तिआ'रा है
ये दास्तान है हिज्र-ओ-विसाल से बाहर'''}
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
    author: 'अमजद इस्लाम अमजद',
    text: `{shayari['text']}`,
  }},'''
        new_entries.append(entry)
        current_id += 1
    
    # Insert new entries
    new_content = content[:start_pos] + '\n' + '\n'.join(new_entries) + content[start_pos:]
    
    # Write back
    with open('shayari.js', 'w', encoding='utf-8') as f:
        f.write(new_content)
    
    print(f"Successfully added {len(new_shayari)} shayari by अमजद इस्लाम अमजद!")
    print(f"New IDs: {last_id + 1} to {current_id - 1}")
else:
    print("Could not find insertion point")

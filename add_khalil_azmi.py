#!/usr/bin/env python3
"""Add Khalil-ur-Rahman Azmi shayari to the collection"""

import re

# Read the file
with open('shayari.js', 'r', encoding='utf-8') as f:
    content = f.read()

# Find the last ID
ids = re.findall(r'id:\s*(\d+),', content)
last_id = max([int(id) for id in ids]) if ids else 0
print(f"Last ID found: {last_id}")

# New shayari by Khalil-ur-Rahman Azmi
new_shayari = [
    {'category': 'sad', 'text': '''न जाने किस की हमें उम्र भर तलाश रही
जिसे क़रीब से देखा वो दूसरा निकला'''},
    {'category': 'sad', 'text': '''सुना रहा हूँ उन्हें झूट-मूट इक क़िस्सा
कि एक शख़्स मोहब्बत में कामयाब रहा'''},
    {'category': 'romantic', 'text': '''तुम मुझे चाहो न चाहो लेकिन इतना तो करो
झूट ही कह दो कि जीने का बहाना मिल सके'''},
    {'category': 'sad', 'text': '''देखने वाला कोई मिले तो दिल के दाग़ दिखाऊँ
ये नगरी अँधों की नगरी किस को क्या समझाऊँ'''},
    {'category': 'life', 'text': '''हज़ार तरह की मय पी हज़ार तरह के ज़हर
न प्यास ही बुझी अपनी न हौसला निकला'''},
    {'category': 'sad', 'text': '''यूँ जी बहल गया है तिरी याद से मगर
तेरा ख़याल तेरे बराबर न हो सका'''},
    {'category': 'life', 'text': '''ये तमन्ना नहीं अब दाद-ए-हुनर दे कोई
आ के मुझ को मिरे होने की ख़बर दे कोई'''},
    {'category': 'life', 'text': '''हम पे जो गुज़री है बस उस को रक़म करते हैं
आप-बीती कहो या मर्सिया-ख़्वानी कह लो'''},
    {'category': 'romantic', 'text': '''आरिज़ पे तेरे मेरी मोहब्बत की सुर्ख़ियाँ
मेरी जबीं पे तेरी वफ़ा का ग़ुरूर है'''},
    {'category': 'sad', 'text': '''हमें तो रास न आई किसी की महफ़िल भी
कोई ख़ुदा कोई हम-साया-ए-ख़ुदा निकला'''},
    {'category': 'sad', 'text': '''तमाम यादें महक रही हैं हर एक ग़ुंचा खिला हुआ है
ज़माना बीता मगर गुमाँ है कि आज ही वो जुदा हुआ है'''},
    {'category': 'life', 'text': '''हंगामा-ए-हयात से जाँ-बर न हो सका
ये दिल अजीब दिल है कि पत्थर न हो सका'''},
    {'category': 'life', 'text': '''मैं अपने घर को बुलंदी पे चढ़ के क्या देखूँ
उरूज-ए-फ़न मिरी दहलीज़ पर उतार मुझे'''},
    {'category': 'romantic', 'text': '''अज़ल से था वो हमारे वजूद का हिस्सा
वो एक शख़्स कि जो हम पे मेहरबान हुआ'''},
    {'category': 'romantic', 'text': '''ये और बात कि तर्क-ए-वफ़ा पे माइल हैं
तिरी वफ़ा की हमें आज भी ज़रूरत है'''},
    {'category': 'sad', 'text': '''हमारे ब'अद उस मर्ग-ए-जवाँ को कौन समझेगा
इरादा है कि अपना मर्सिया भी आप ही लिख लें'''},
    {'category': 'romantic', 'text': '''आज डूबा हुआ ख़ुशबू में है पैराहन-ए-जाँ
ऐ सबा किस ने ये पूछा है तिरा नाम-ओ-निशाँ'''},
    {'category': 'sad', 'text': '''तेरी गली से छुट के न जा-ए-अमाँ मिली
अब के तो मेरा घर भी मिरा घर न हो सका'''},
    {'category': 'romantic', 'text': '''ज़रा आ के सामने बैठ जा मिरी चश्म-ए-तर के क़रीब आ
मिरे आइने में भी देख ले कभी अपनी ज़ुल्फ़ की बरहमी'''},
    {'category': 'sad', 'text': '''ज़िंदगी भी मिरे नालों की शनासा निकली
दिल जो टूटा तो मिरे घर में कोई शम्अ जली'''}
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
    author: 'ख़लील-उर-रहमान आज़मी',
    text: `{shayari['text']}`,
  }},'''
        new_entries.append(entry)
        current_id += 1
    
    # Insert new entries
    new_content = content[:start_pos] + '\n' + '\n'.join(new_entries) + content[start_pos:]
    
    # Write back
    with open('shayari.js', 'w', encoding='utf-8') as f:
        f.write(new_content)
    
    print(f"Successfully added {len(new_shayari)} shayari by ख़लील-उर-रहमान आज़मी!")
    print(f"New IDs: {last_id + 1} to {current_id - 1}")
else:
    print("Could not find insertion point")

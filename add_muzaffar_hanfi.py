#!/usr/bin/env python3
"""Add Muzaffar Hanfi shayari to the collection"""

import re

# Read the file
with open('shayari.js', 'r', encoding='utf-8') as f:
    content = f.read()

# Find the last ID
ids = re.findall(r'id:\s*(\d+),', content)
last_id = max([int(id) for id in ids]) if ids else 0
print(f"Last ID found: {last_id}")

# New shayari by Muzaffar Hanfi
new_shayari = [
    {
        'category': 'life',
        'text': '''रोती हुई एक भीड़ मिरे गिर्द खड़ी थी
शायद ये तमाशा मिरे हँसने के लिए था'''
    },
    {
        'category': 'sad',
        'text': '''शुक्रिया रेशमी दिलासे का
तीर तो आप ने भी मारा था'''
    },
    {
        'category': 'life',
        'text': '''सुनाइए वो लतीफ़ा हर एक जाम के साथ
कि एक बूँद से ईमान टूट जाता है'''
    },
    {
        'category': 'friendship',
        'text': '''हज़ारों मुश्किलें हैं दोस्तों से दूर रहने में
मगर इक फ़ाएदा है पीठ पर ख़ंजर नहीं लगता'''
    },
    {
        'category': 'life',
        'text': '''काँटों में रख के फूल हवा में उड़ा के ख़ाक
करता है सौ तरह से इशारे मुझे कोई'''
    },
    {
        'category': 'life',
        'text': '''उगल देते हैं जो कुछ पेट में हो घर में आते ही
परिंदे अपने बच्चों से अदाकारी नहीं करते'''
    },
    {
        'category': 'romantic',
        'text': '''यूँ पलक पर जगमगाना दो घड़ी का ऐश है
रौशनी बन कर मिरे अंदर ही अंदर फैल जा'''
    },
    {
        'category': 'romantic',
        'text': '''देखना कैसे हुमकने लगे सारे पत्थर
मेरी वहशत को तुम्हारी गली पहचानती है'''
    },
    {
        'category': 'life',
        'text': '''शिकस्त खा चुके हैं हम मगर अज़ीज़ फ़ातेहो
हमारे क़द से कम न हो फ़राज़-ए-दार देखना'''
    },
    {
        'category': 'life',
        'text': '''ख़ुद ही न डूब जाऊँ कि फ़ुर्सत मिले मुझे
नेकी लदी है पुश्त पे दरिया है सामने'''
    },
    {
        'category': 'life',
        'text': '''अब 'उम्र का एहसास दिलाने लगे जुगनू
दामन से मिरी आँख में आने लगे जुगनू'''
    },
    {
        'category': 'life',
        'text': '''दरवाज़े पे तहरीर यहाँ कोई नहीं है
अन्दर कोई ज़ंजीर हिलाता है कि मैं हूँ'''
    },
    {
        'category': 'sad',
        'text': '''यहाँ 'अदू के सिवा कौन पूछता है हमें
लहू-लुहान सही कुछ नहीं हुआ है हमें'''
    },
    {
        'category': 'life',
        'text': '''ख़फ़ीफ़ रहते हैं अक्सर ज़मीर के आगे
ये तू ने कैसे तराज़ू पे रख दिया है हमें'''
    },
    {
        'category': 'life',
        'text': '''अभी तो मैं दो क़दम चला हूँ ज़मीन क्यों तंग हो रही है
मुझी पे क्यों आसमान टूटे अभी तो मैं पर निकालता था'''
    },
    {
        'category': 'life',
        'text': '''फ़ाख़्ता कहती रही फ़स्लें जला दी जाएँगी
झूम कर आगे बढ़े बादल कि हम तो जाएँगे'''
    },
    {
        'category': 'life',
        'text': '''सूरज को तोड़-मोड़ के जब दिन किया तमाम
तारों के टूटने से शब-ए-तार हिल गई'''
    },
    {
        'category': 'life',
        'text': '''वहाँ भी 'अक़्ल ही मसनद-नशीं मिली कि जहाँ
मता'-ए-फ़िक्र-ओ-नज़र का कोई सवाल न था'''
    },
    {
        'category': 'life',
        'text': '''उस वक़्त जब तिलिस्म-ए-फ़लक टूटने को था
ऐसा हुआ कि मुझ को बुलाने लगी ज़मीं'''
    }
]

# Find the position to insert (before the closing bracket of hindiShayari array)
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
    author: 'मुज़फ़्फ़र हनफ़ी',
    text: `{shayari['text']}`,
  }},'''
        new_entries.append(entry)
        current_id += 1
    
    # Insert new entries
    new_content = content[:start_pos] + '\n' + '\n'.join(new_entries) + content[start_pos:]
    
    # Write back
    with open('shayari.js', 'w', encoding='utf-8') as f:
        f.write(new_content)
    
    print(f"✅ Successfully added {len(new_shayari)} shayari by मुज़फ़्फ़र हनफ़ी!")
    print(f"New IDs: {last_id + 1} to {current_id - 1}")
else:
    print("❌ Could not find insertion point")

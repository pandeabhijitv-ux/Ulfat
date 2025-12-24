#!/usr/bin/env python3
"""Add Jamal Ehsani shayari to the collection"""

import re

# Read the file
with open('shayari.js', 'r', encoding='utf-8') as f:
    content = f.read()

# Find the last ID
ids = re.findall(r'id:\s*(\d+),', content)
last_id = max([int(id) for id in ids]) if ids else 0
print(f"Last ID found: {last_id}")

# New shayari by Jamal Ehsani
new_shayari = [
    {'category': 'life', 'text': '''तमाम रात नहाया था शहर बारिश में
वो रंग उतर ही गए जो उतरने वाले थे'''},
    {'category': 'romantic', 'text': '''क़रार दिल को सदा जिस के नाम से आया
वो आया भी तो किसी और काम से आया'''},
    {'category': 'life', 'text': '''\'जमाल\' हर शहर से है प्यारा वो शहर मुझ को
जहाँ से देखा था पहली बार आसमान मैं ने'''},
    {'category': 'sad', 'text': '''इक सफ़र में कोई दो बार नहीं लुट सकता
अब दोबारा तिरी चाहत नहीं की जा सकती'''},
    {'category': 'sad', 'text': '''हज़ार तरह के थे रंज पिछले मौसम में
पर इतना था कि कोई साथ रोने वाला था'''},
    {'category': 'life', 'text': '''हारने वालों ने इस रुख़ से भी सोचा होगा
सर कटाना है तो हथियार न डाले जाएँ'''},
    {'category': 'sad', 'text': '''सुब्ह आता हूँ यहाँ और शाम हो जाने के बा\'द
लौट जाता हूँ मैं घर नाकाम हो जाने के बा\'द'''},
    {'category': 'sad', 'text': '''ये किस मक़ाम पे सूझी तुझे बिछड़ने की
कि अब तो जा के कहीं दिन सँवरने वाले थे'''},
    {'category': 'life', 'text': '''थकन बहुत थी मगर साया-ए-शजर में \'जमाल\'
मैं बैठता तो मिरा हम-सफ़र चला जाता'''},
    {'category': 'sad', 'text': '''चराग़ बुझते चले जा रहे हैं सिलसिला-वार
मैं ख़ुद को देख रहा हूँ फ़साना होते हुए'''},
    {'category': 'life', 'text': '''और अब ये चाहता हूँ कोई ग़म बटाए मिरा
मैं अपनी मिट्टी कभी आप ढोने वाला था'''},
    {'category': 'sad', 'text': '''चराग़ सामने वाले मकान में भी न था
ये सानेहा मिरे वहम-ओ-गुमान में भी न था'''},
    {'category': 'sad', 'text': '''वो लोग मेरे बहुत प्यार करने वाले थे
गुज़र गए हैं जो मौसम गुज़रने वाले थे'''},
    {'category': 'sad', 'text': '''बिखर गया है जो मोती पिरोने वाला था
वो हो रहा है यहाँ जो न होने वाला था'''},
    {'category': 'life', 'text': '''जो मेरे ज़िक्र पर अब क़हक़हे लगाता है
बिछड़ते वक़्त कोई हाल देखता उस का'''},
    {'category': 'life', 'text': '''उस रस्ते पर पीछे से इतनी आवाज़ें आईं \'जमाल\'
एक जगह तो घूम के रह गई एड़ी सीधे पाँव की'''},
    {'category': 'life', 'text': '''मिरा कमाल कि मैं इस फ़ज़ा में ज़िंदा हूँ
दु\'आ न मिलते हुए और हवा न होते हुए'''},
    {'category': 'sad', 'text': '''दिन गुज़रते जा रहे हैं और हुजूम-ए-ख़ुश-गुमाँ
मुंतज़िर बैठा है आब ओ ख़ाक से बिछड़ा हुआ'''},
    {'category': 'romantic', 'text': '''क्या उस से मुलाक़ात का इम्काँ भी नहीं अब
क्यूँ इन दिनों मैली तिरी पोशाक बहुत है'''},
    {'category': 'sad', 'text': '''वो भी मिलने नई पोशाक बदल कर आया
मैं जो कल पैरहन-ए-ख़ाक बदल कर आया'''}
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
    author: 'जमाल एहसानी',
    text: `{shayari['text']}`,
  }},'''
        new_entries.append(entry)
        current_id += 1
    
    # Insert new entries
    new_content = content[:start_pos] + '\n' + '\n'.join(new_entries) + content[start_pos:]
    
    # Write back
    with open('shayari.js', 'w', encoding='utf-8') as f:
        f.write(new_content)
    
    print(f"Successfully added {len(new_shayari)} shayari by जमाल एहसानी!")
    print(f"New IDs: {last_id + 1} to {current_id - 1}")
else:
    print("Could not find insertion point")

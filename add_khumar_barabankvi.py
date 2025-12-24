#!/usr/bin/env python3
"""Add Khumar Barabankvi shayari to the collection"""

import re

# Read the file
with open('shayari.js', 'r', encoding='utf-8') as f:
    content = f.read()

# Find the last ID
ids = re.findall(r'id:\s*(\d+),', content)
last_id = max([int(id) for id in ids]) if ids else 0
print(f"Last ID found: {last_id}")

# New shayari by Khumar Barabankvi
new_shayari = [
    {'category': 'sad', 'text': '''भूले हैं रफ़्ता रफ़्ता उन्हें मुद्दतों में हम
क़िस्तों में ख़ुद-कुशी का मज़ा हम से पूछिए'''},
    {'category': 'sad', 'text': '''वही फिर मुझे याद आने लगे हैं
जिन्हें भूलने में ज़माने लगे हैं'''},
    {'category': 'romantic', 'text': '''ये कहना था उन से मोहब्बत है मुझ को
ये कहने में मुझ को ज़माने लगे हैं'''},
    {'category': 'romantic', 'text': '''मोहब्बत को समझना है तो नासेह ख़ुद मोहब्बत कर
किनारे से कभी अंदाज़ा-ए-तूफ़ाँ नहीं होता'''},
    {'category': 'romantic', 'text': '''सुना है हमें वो भुलाने लगे हैं
तो क्या हम उन्हें याद आने लगे हैं'''},
    {'category': 'sad', 'text': '''अब इन हुदूद में लाया है इंतिज़ार मुझे
वो आ भी जाएँ तो आए न ए'तिबार मुझे'''},
    {'category': 'sad', 'text': '''ऐसा नहीं कि उन से मोहब्बत नहीं रही
जज़्बात में वो पहली सी शिद्दत नहीं रही'''},
    {'category': 'sad', 'text': '''तुझ को बर्बाद तो होना था बहर-हाल 'ख़ुमार'
नाज़ कर नाज़ कि उस ने तुझे बर्बाद किया'''},
    {'category': 'life', 'text': '''चराग़ों के बदले मकाँ जल रहे हैं
नया है ज़माना नई रौशनी है'''},
    {'category': 'sad', 'text': '''सहरा को बहुत नाज़ है वीरानी पे अपनी
वाक़िफ़ नहीं शायद मिरे उजड़े हुए घर से'''},
    {'category': 'sad', 'text': '''ओ जाने वाले आ कि तिरे इंतिज़ार में
रस्ते को घर बनाए ज़माने गुज़र गए'''},
    {'category': 'romantic', 'text': '''ये वफ़ा की सख़्त राहें ये तुम्हारे पाँव नाज़ुक
न लो इंतिक़ाम मुझ से मिरे साथ साथ चल के'''},
    {'category': 'sad', 'text': '''रात बाक़ी थी जब वो बिछड़े थे
कट गई उम्र रात बाक़ी है'''},
    {'category': 'life', 'text': '''दुश्मनों से पशेमान होना पड़ा है
दोस्तों का ख़ुलूस आज़माने के बाद'''},
    {'category': 'romantic', 'text': '''न हारा है इश्क़ और न दुनिया थकी है
दिया जल रहा है हवा चल रही है'''},
    {'category': 'life', 'text': '''हम भी कर लें जो रौशनी घर में
फिर अंधेरे कहाँ क़याम करें'''},
    {'category': 'life', 'text': '''उम्र भर चल के भी पाई नहीं मंज़िल हम ने
कुछ समझ में नहीं आता ये सफ़र कैसा है'''},
    {'category': 'life', 'text': '''जलते दियों में जलते घरों जैसी ज़ौ कहाँ
सरकार रौशनी का मज़ा हम से पूछिए'''},
    {'category': 'life', 'text': '''हाल-ए-ग़म कह के ग़म बढ़ा बैठे
तीर मारे थे तीर खा बैठे'''},
    {'category': 'romantic', 'text': '''कहीं शेर ओ नग़्मा बन के कहीं आँसुओं में ढल के
वो मुझे मिले तो लेकिन कई सूरतें बदल के'''}
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
    author: 'ख़ुमार बाराबंकवी',
    text: `{shayari['text']}`,
  }},'''
        new_entries.append(entry)
        current_id += 1
    
    # Insert new entries
    new_content = content[:start_pos] + '\n' + '\n'.join(new_entries) + content[start_pos:]
    
    # Write back
    with open('shayari.js', 'w', encoding='utf-8') as f:
        f.write(new_content)
    
    print(f"Successfully added {len(new_shayari)} shayari by ख़ुमार बाराबंकवी!")
    print(f"New IDs: {last_id + 1} to {current_id - 1}")
else:
    print("Could not find insertion point")

import re

# Read the current shayari.js file
with open('shayari.js', 'r', encoding='utf-8') as f:
    content = f.read()

# Find all existing IDs to determine the next ID
ids = re.findall(r'id:\s*(\d+),', content)
last_id = max([int(id) for id in ids]) if ids else 0

print(f"Last ID found: {last_id}")

# Mohammed Rafi collection ghazals + others
new_shayari = [
    # Sahir Ludhianvi - कभी ख़ुद पे कभी हालात पे रोना आया
    {'category': 'sad', 'author': 'साहिर लुधियानवी', 'text': 'कभी ख़ुद पे कभी हालात पे रोना आया\nबात निकली तो हर इक बात पे रोना आया'},
    {'category': 'sad', 'author': 'साहिर लुधियानवी', 'text': 'हम तो समझे थे कि हम भूल गए हैं उन को\nक्या हुआ आज ये किस बात पे रोना आया'},
    {'category': 'life', 'author': 'साहिर लुधियानवी', 'text': 'किस लिए जीते हैं हम किस के लिए जीते हैं\nबारहा ऐसे सवालात पे रोना आया'},
    {'category': 'sad', 'author': 'साहिर लुधियानवी', 'text': 'कौन रोता है किसी और की ख़ातिर ऐ दोस्त\nसब को अपनी ही किसी बात पे रोना आया'},
    
    # Sahir Ludhianvi - मैं ज़िंदगी का साथ निभाता चला गया
    {'category': 'life', 'author': 'साहिर लुधियानवी', 'text': 'मैं ज़िंदगी का साथ निभाता चला गया\nहर फ़िक्र को धुएँ में उड़ाता चला गया'},
    {'category': 'life', 'author': 'साहिर लुधियानवी', 'text': 'बर्बादियों का सोग मनाना फ़ुज़ूल था\nबर्बादियों का जश्न मनाता चला गया'},
    {'category': 'life', 'author': 'साहिर लुधियानवी', 'text': 'जो मिल गया उसी को मुक़द्दर समझ लिया\nजो खो गया मैं उस को भुलाता चला गया'},
    {'category': 'life', 'author': 'साहिर लुधियानवी', 'text': 'ग़म और ख़ुशी में फ़र्क़ न महसूस हो जहाँ\nमैं दिल को उस मक़ाम पे लाता चला गया'},
    
    # Kaifi Azmi - मिले न फूल तो काँटों से दोस्ती कर ली
    {'category': 'life', 'author': 'कैफ़ी आज़मी', 'text': 'मिले न फूल तो काँटों से दोस्ती कर ली\nइसी तरह से बसर हम ने ज़िंदगी कर ली'},
    {'category': 'life', 'author': 'कैफ़ी आज़मी', 'text': 'अब आगे जो भी हो अंजाम देखा जाएगा\nख़ुदा तलाश लिया और बंदगी कर ली'},
    {'category': 'romantic', 'author': 'कैफ़ी आज़मी', 'text': 'नज़र मिली भी न थी और उन को देख लिया\nज़बाँ खुली भी न थी और बात भी कर ली'},
    {'category': 'life', 'author': 'कैफ़ी आज़मी', 'text': 'वो जिन को प्यार है चाँदी से इश्क़ सोने से\nवही कहेंगे कभी हम ने ख़ुद-कुशी कर ली'},
    
    # Hasrat Jaipuri - छलके तिरी आँखों से शराब और ज़ियादा
    {'category': 'romantic', 'author': 'हसरत जयपुरी', 'text': 'छलके तिरी आँखों से शराब और ज़ियादा\nखिलते रहें होंठों के गुलाब और ज़ियादा'},
    {'category': 'romantic', 'author': 'हसरत जयपुरी', 'text': 'क्या बात है जाने तिरी महफ़िल में सितमगर\nधड़के है दिल-ए-ख़ाना-ख़राब और ज़ियादा'},
    {'category': 'romantic', 'author': 'हसरत जयपुरी', 'text': 'इस दिल में अभी और भी ज़ख़्मों की जगह है\nअबरू की कटारी को दो आब और ज़ियादा'},
    {'category': 'romantic', 'author': 'हसरत जयपुरी', 'text': 'तू इश्क़ के तूफ़ान को बाँहों में जकड़ ले\nअल्लाह करे ज़ोर-ए-शबाब और ज़ियादा'}
]

# Generate new entries with incremented IDs
new_entries = []
for i, shayari in enumerate(new_shayari, 1):
    new_id = last_id + i
    entry = f"""  {{
    id: {new_id},
    language: 'urdu',
    category: '{shayari['category']}',
    author: '{shayari['author']}',
    text: `{shayari['text']}`
  }}"""
    new_entries.append(entry)

# Join all new entries with commas
new_entries_text = ',\n'.join(new_entries)

# Find the last entry in the array and add new entries before the closing bracket
pattern = r'(const hindiShayari = \[.*?)(];)'
replacement = r'\1,\n' + new_entries_text + r'\n\2'

# Replace in content
new_content = re.sub(pattern, replacement, content, flags=re.DOTALL)

# Write back to file
with open('shayari.js', 'w', encoding='utf-8') as f:
    f.write(new_content)

print(f"Successfully added {len(new_shayari)} legendary ghazals from Mohammed Rafi collection!")
print(f"New IDs: {last_id + 1} to {last_id + len(new_shayari)}")

import re

# Read the file
with open(r'c:\Ulfat\src\data\shayariData.js', 'r', encoding='utf-8') as f:
    content = f.read()

# Extract all entries using regex
pattern = r'(\{[^}]*id:\s*\d+,[^}]*language:\s*\'(hindi|urdu|marathi)\',[^}]*\})'
matches = re.findall(pattern, content, re.DOTALL)

# Separate by language
hindi_entries = []
urdu_entries = []
marathi_entries = []

for entry_text, lang in matches:
    if lang == 'hindi':
        hindi_entries.append(entry_text)
    elif lang == 'urdu':
        urdu_entries.append(entry_text)
    elif lang == 'marathi':
        marathi_entries.append(entry_text)

print(f'Hindi: {len(hindi_entries)}')
print(f'Urdu: {len(urdu_entries)}')
print(f'Marathi: {len(marathi_entries)}')
print(f'Total: {len(hindi_entries) + len(urdu_entries) + len(marathi_entries)}')

# Create Hindi file
with open(r'c:\Ulfat\hindiShayari.js', 'w', encoding='utf-8') as f:
    f.write('// Hindi Shayari Collection\n')
    f.write('const hindiShayari = [\n')
    for i, entry in enumerate(hindi_entries):
        f.write('  ' + entry)
        if i < len(hindi_entries) - 1:
            f.write(',\n')
        else:
            f.write('\n')
    f.write('];\n\n')
    f.write('export default hindiShayari;\n')

# Create Urdu file
with open(r'c:\Ulfat\urduShayari.js', 'w', encoding='utf-8') as f:
    f.write('// Urdu Shayari Collection\n')
    f.write('const urduShayari = [\n')
    for i, entry in enumerate(urdu_entries):
        f.write('  ' + entry)
        if i < len(urdu_entries) - 1:
            f.write(',\n')
        else:
            f.write('\n')
    f.write('];\n\n')
    f.write('export default urduShayari;\n')

# Create Marathi file
with open(r'c:\Ulfat\marathiShayari.js', 'w', encoding='utf-8') as f:
    f.write('// Marathi Shayari Collection\n')
    f.write('const marathiShayari = [\n')
    for i, entry in enumerate(marathi_entries):
        f.write('  ' + entry)
        if i < len(marathi_entries) - 1:
            f.write(',\n')
        else:
            f.write('\n')
    f.write('];\n\n')
    f.write('export default marathiShayari;\n')

print('\nFiles created successfully!')

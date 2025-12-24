import re

# Read with utf-8
with open('shayari.js', 'r', encoding='utf-8') as f:
    content = f.read()

# Write back with utf-8
with open('shayari.js', 'w', encoding='utf-8') as f:
    f.write(content)

print("Encoding fixed!")

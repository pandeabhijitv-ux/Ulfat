#!/usr/bin/env python3
"""Remove all devotional (Bhakti) shayari entries from shayari.js"""

import re

# Read the file
with open('shayari.js', 'r', encoding='utf-8') as f:
    content = f.read()

# Find the shayariData array
# Pattern to match individual shayari objects with devotional category
pattern = r',?\s*\{\s*id:\s*\d+,\s*language:\s*[\'"][^\'"]*[\'"],[^}]*category:\s*[\'"]devotional[\'"][^}]*\}'

# Remove all devotional entries
cleaned_content = re.sub(pattern, '', content, flags=re.MULTILINE | re.DOTALL)

# Clean up any double commas that might result
cleaned_content = re.sub(r',\s*,', ',', cleaned_content)

# Clean up comma before closing bracket
cleaned_content = re.sub(r',(\s*\])', r'\1', cleaned_content)

# Write back
with open('shayari.js', 'w', encoding='utf-8') as f:
    f.write(cleaned_content)

print("✅ Successfully removed all Bhakti (devotional) shayari entries!")
print("Total entries removed: ", content.count("category: 'devotional'"))

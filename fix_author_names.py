# -*- coding: utf-8 -*-
import json
import re

# Read the file
with open('ghazal_data.js', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace the corrupted author names with correct Hindi text
# First, fix the corrupted entries
content = content.replace("author: 'शर. अटल बहर वजपय',", "author: 'श्री. अटल बिहारी वाजपेयी',")

# Also handle if there are any English versions left
content = content.replace("author: 'Atal Bihari Vajpayee',", "author: 'श्री. अटल बिहारी वाजपेयी',")

# Write back
with open('ghazal_data.js', 'w', encoding='utf-8') as f:
    f.write(content)

print("✅ Fixed all Atal Bihari Vajpayee author names to 'श्री. अटल बिहारी वाजपेयी'")
print("✅ All Suresh Bhat entries remain as 'Suresh Bhat'")

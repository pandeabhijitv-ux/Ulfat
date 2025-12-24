# -*- coding: utf-8 -*-
# Renumber IDs for Atal Bihari Vajpayee poems after adding new first poem

with open('ghazal_data.js', 'r', encoding='utf-8') as f:
    content = f.read()

# Renumber from 10087 down to 10077 (increment each by 1)
# Start from the highest to avoid conflicts
for old_id in range(10087, 10076, -1):
    new_id = old_id + 1
    content = content.replace(f'id: {old_id},', f'id: {new_id},')

with open('ghazal_data.js', 'w', encoding='utf-8') as f:
    f.write(content)

print("✅ Renumbered all IDs after inserting 'गीत नया गाता हूँ' as first poem")
print("   New poem: ID 10076 - गीत नया गाता हूँ")
print("   Other poems shifted: 10077-10088")

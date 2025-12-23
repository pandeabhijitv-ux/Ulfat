import re

# Read the source file
with open('src/data/shayariData.js', 'r', encoding='utf-8') as f:
    content = f.read()

# Extract all shayari objects
pattern = r'\{\s*id:\s*\d+,\s*language:\s*["\'](\w+)["\'],\s*category:.*?\},\s*(?=\{|$)'
matches = re.finditer(pattern, content, re.DOTALL)

hindi = []
urdu = []
marathi = []

for match in matches:
    lang = match.group(1)
    shayari = match.group(0)
    
    if lang == 'hindi':
        hindi.append(shayari)
    elif lang == 'urdu':
        urdu.append(shayari)
    elif lang == 'marathi':
        marathi.append(shayari)

print(f"Found: {len(hindi)} Hindi, {len(urdu)} Urdu, {len(marathi)} Marathi")
print(f"Total: {len(hindi) + len(urdu) + len(marathi)}")

# Create the new shayari.js with separated languages
with open('shayari_new.js', 'w', encoding='utf-8') as f:
    f.write("// Shayari Data organized by language\n\n")
    
    # Hindi Shayari
    f.write("// === HINDI SHAYARI ===\n")
    f.write("const hindiShayari = [\n")
    for s in hindi:
        f.write("  " + s + "\n")
    f.write("];\n\n")
    
    # Urdu Shayari
    f.write("// === URDU SHAYARI ===\n")
    f.write("const urduShayari = [\n")
    for s in urdu:
        f.write("  " + s + "\n")
    f.write("];\n\n")
    
    # Marathi Shayari
    f.write("// === MARATHI SHAYARI ===\n")
    f.write("const marathiShayari = [\n")
    for s in marathi:
        f.write("  " + s + "\n")
    f.write("];\n\n")
    
    # Combined
    f.write("// Combined all languages\n")
    f.write("const shayariData = [...hindiShayari, ...urduShayari, ...marathiShayari];\n")

print("Created shayari_new.js")

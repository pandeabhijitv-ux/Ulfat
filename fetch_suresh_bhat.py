import requests
from bs4 import BeautifulSoup
import json
import re
import urllib3

# Disable SSL warnings
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

urls = [
    # First batch
    "https://www.sureshbhat.in/node/1496",
    "https://www.sureshbhat.in/node/499",
    "https://www.sureshbhat.in/node/498",
    "https://www.sureshbhat.in/node/474",
    "https://www.sureshbhat.in/node/473",
    "https://www.sureshbhat.in/node/472",
    "https://www.sureshbhat.in/node/471",
    "https://www.sureshbhat.in/node/75",
    "https://www.sureshbhat.in/node/76",
    "https://www.sureshbhat.in/node/78",
    "https://www.sureshbhat.in/node/96",
    "https://www.sureshbhat.in/node/122",
    "https://www.sureshbhat.in/node/125",
    "https://www.sureshbhat.in/node/134",
    "https://www.sureshbhat.in/node/161",
    "https://www.sureshbhat.in/node/176",
    "https://www.sureshbhat.in/node/206",
    "https://www.sureshbhat.in/node/208",
    "https://www.sureshbhat.in/node/209",
    "https://www.sureshbhat.in/node/210",
    "https://www.sureshbhat.in/node/211",
    "https://www.sureshbhat.in/node/212",
    "https://www.sureshbhat.in/node/213",
    "https://www.sureshbhat.in/node/214",
    "https://www.sureshbhat.in/node/215",
    "https://www.sureshbhat.in/node/216",
    "https://www.sureshbhat.in/node/220",
    "https://www.sureshbhat.in/node/231",
    "https://www.sureshbhat.in/node/232",
    "https://www.sureshbhat.in/node/268",
    "https://www.sureshbhat.in/node/381",
    "https://www.sureshbhat.in/node/393",
    "https://www.sureshbhat.in/node/395",
    "https://www.sureshbhat.in/node/397",
    "https://www.sureshbhat.in/node/398",
    "https://www.sureshbhat.in/node/402",
    "https://www.sureshbhat.in/node/403",
    # Second batch
    "https://www.sureshbhat.in/node/404",
    "https://www.sureshbhat.in/node/405",
    "https://www.sureshbhat.in/node/406",
    "https://www.sureshbhat.in/node/407",
    "https://www.sureshbhat.in/node/408",
    "https://www.sureshbhat.in/node/409",
    "https://www.sureshbhat.in/node/470",
    "https://www.sureshbhat.in/node/497",
    "https://www.sureshbhat.in/node/500",
    "https://www.sureshbhat.in/node/1327",
    "https://www.sureshbhat.in/node/1213",
    "https://www.sureshbhat.in/node/2185"
]

# Remove duplicates
urls = list(set(urls))

ghazals = []

print(f"Fetching {len(urls)} ghazals from sureshbhat.in...")

for idx, url in enumerate(urls, 1):
    try:
        print(f"\n[{idx}/{len(urls)}] Fetching: {url}")
        response = requests.get(url, timeout=10, verify=False)
        response.raise_for_status()
        
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Find title
        title_elem = soup.find('h1', class_='title')
        title = title_elem.get_text(strip=True) if title_elem else "Untitled"
        
        # Find the content div
        content_div = soup.find('div', class_='content')
        if not content_div:
            print(f"  ⚠️ No content found")
            continue
        
        # Get all paragraphs
        paragraphs = content_div.find_all('p')
        
        # Extract shers (couplets)
        shers = []
        for p in paragraphs:
            text = p.get_text(strip=True)
            # Skip empty paragraphs
            if text and len(text) > 5:
                # Clean up the text
                text = re.sub(r'\s+', ' ', text)
                shers.append(text)
        
        if shers:
            ghazal = {
                "title": title,
                "author": "सुरेश भट",
                "language": "marathi",
                "shers": shers
            }
            ghazals.append(ghazal)
            print(f"  ✅ Extracted: {title} ({len(shers)} shers)")
        else:
            print(f"  ⚠️ No shers found")
            
    except Exception as e:
        print(f"  ❌ Error: {e}")

print(f"\n{'='*60}")
print(f"Successfully fetched {len(ghazals)} ghazals!")
print(f"{'='*60}\n")

# Generate JavaScript output
print("// Add these to ghazal_data.js\n")
print("// Suresh Bhat Ghazals:")

for i, ghazal in enumerate(ghazals, 1):
    print(f"  {{")
    print(f"    title: `{ghazal['title']}`,")
    print(f"    author: '{ghazal['author']}',")
    print(f"    language: '{ghazal['language']}',")
    print(f"    shers: [")
    for sher in ghazal['shers']:
        # Escape backticks and backslashes
        sher_escaped = sher.replace('\\', '\\\\').replace('`', '\\`')
        print(f"      `{sher_escaped}`,")
    print(f"    ]")
    print(f"  }}{'' if i == len(ghazals) else ','}")

# Save to file
output_file = 'suresh_bhat_ghazals.txt'
with open(output_file, 'w', encoding='utf-8') as f:
    f.write("// Suresh Bhat Ghazals:\n")
    for i, ghazal in enumerate(ghazals, 1):
        f.write(f"  {{\n")
        f.write(f"    title: `{ghazal['title']}`,\n")
        f.write(f"    author: '{ghazal['author']}',\n")
        f.write(f"    language: '{ghazal['language']}',\n")
        f.write(f"    shers: [\n")
        for sher in ghazal['shers']:
            sher_escaped = sher.replace('\\', '\\\\').replace('`', '\\`')
            f.write(f"      `{sher_escaped}`,\n")
        f.write(f"    ]\n")
        f.write(f"  }}{'' if i == len(ghazals) else ','}\n")

print(f"\n✅ Ghazals saved to: {output_file}")

import requests
from bs4 import BeautifulSoup
import json
import re

urls = [
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
    "https://www.sureshbhat.in/node/403"
]

ghazals = []
start_id = 53  # Start after existing 52 ghazals

for idx, url in enumerate(urls):
    try:
        print(f"Fetching {url}...")
        response = requests.get(url, timeout=10)
        response.encoding = 'utf-8'
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Get title from h1
        title_tag = soup.find('h1')
        if not title_tag:
            print(f"  ⚠️ No title found for {url}")
            continue
        title = title_tag.get_text().strip()
        
        # Get content - look for the main content area
        content_div = soup.find('div', class_='content')
        if not content_div:
            print(f"  ⚠️ No content found for {url}")
            continue
        
        # Extract text and split into couplets
        text = content_div.get_text()
        
        # Clean up the text
        lines = [line.strip() for line in text.split('\n') if line.strip()]
        
        # Filter out navigation/footer text
        shers = []
        for line in lines:
            # Skip common navigation/footer text
            if any(skip in line for skip in ['You are here', 'माहितीसाठी', 'येण्याची नोंद', 
                                             'Additional Links', 'Copyright', 'CAPTCHA',
                                             'Math question', 'सुरेश भटांची', 'मुखपृष्ठ',
                                             'स्वगृह', 'एकूण नवे', 'नवे लेख', 'चित्रदालन',
                                             'साहाय्य', 'ध्वनिफिती', 'अभिप्राय', 'बाराखडी',
                                             'वापरायचे नाव', 'परवलीचा शब्द', 'भटांच्या निवडक']):
                continue
            
            # Skip very short lines (likely noise)
            if len(line) < 10:
                continue
                
            # Skip lines that are just the title
            if line == title:
                continue
            
            # Add as sher
            shers.append(line)
        
        if shers:
            ghazal = {
                "id": start_id + idx,
                "title": title,
                "author": "सुरेश भट",
                "language": "marathi",
                "shers": shers[:15]  # Limit to first 15 shers to avoid noise
            }
            ghazals.append(ghazal)
            print(f"  ✅ Added: {title} ({len(ghazal['shers'])} shers)")
        else:
            print(f"  ⚠️ No shers extracted for {url}")
            
    except Exception as e:
        print(f"  ❌ Error fetching {url}: {e}")

print(f"\n📊 Total ghazals extracted: {len(ghazals)}")

# Write to file
with open('suresh_bhat_ghazals.json', 'w', encoding='utf-8') as f:
    json.dump(ghazals, f, ensure_ascii=False, indent=2)

print("✅ Saved to suresh_bhat_ghazals.json")

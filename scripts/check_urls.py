import urllib.request, json, re

urls = set()

with open('index.html', 'r', encoding='utf-8') as f:
    for match in re.finditer(r'https?://[^\s\"\'\>\)]+', f.read()):
        urls.add(match.group(0))

with open('offers_data.js', 'r', encoding='utf-8') as f:
    for match in re.finditer(r'https?://[^\s\"\'\>\)]+', f.read()):
        urls.add(match.group(0))

req_headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}

print(f'Checking {len(urls)} external URLs...')
for u in sorted(urls):
    if not any(ext in u for ext in ['.jpg', '.png', '.jpeg', '.webp', 'unsplash', 'gestionaweb', 'images']):
        continue
    try:
        req = urllib.request.Request(u, headers=req_headers)
        with urllib.request.urlopen(req, timeout=5) as res:
            print(f'OK [{res.status}]: {u}')
    except Exception as e:
        print(f'FAILED [{e}]: {u}')

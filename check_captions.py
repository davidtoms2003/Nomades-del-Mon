import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

captions = re.findall(r'data-caption=["\']([^"\']+)["\']', html)
unique_captions = sorted(list(set(captions)))

print(f'Total unique captions: {len(unique_captions)}')
for c in unique_captions:
    if c != 'Galeria de viatgers - Nòmades del Món':
        print(c)

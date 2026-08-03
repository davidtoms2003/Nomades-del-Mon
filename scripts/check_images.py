import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

urls = re.findall(r'https?://images\.gestionaweb\.cat/[^\s\'"><]+', html)
unique_urls = sorted(list(set(urls)))

print(f"Total image references: {len(urls)}")
print(f"Total unique URLs: {len(unique_urls)}")
print("\nSample URLs:")
for u in unique_urls[:10]:
    print(u)

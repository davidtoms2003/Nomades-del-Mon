import re
import random

# Category mapping based on caption keywords
CATEGORY_RULES = [
    ('asia', ['tailàndia', 'indonèsia', 'japó', 'xina', 'índia', 'camboja', 'himalaia', 'bali']),
    ('europa', ['parís', 'berlín', 'praga', 'suïssa', 'terol', 'lisboa', 'billund', 'normandia', 'mont-saint-michel', 'illes gregues', 'santorini', 'toscana', 'sardenya', 'alemanya', 'frança', 'itàlia', 'república txeca', 'dinamarca', 'portugal']),
    ('carib-america', ['nova york', 'costa oest', 'riviera maya', 'royalton', 'carib', 'mèxic', 'amazones', 'cap verd', 'canadà', 'brasil', 'eua', 'mexic']),
    ('escapades-creuers', ['creuer', 'menorca', 'formentera', 'lanzarote', 'fuerteventura', 'islàndia', 'disneyland', 'abu dhabi', 'dubai', 'eau', 'futuroscope', 'egipte'])
]

def get_category(caption, filename):
    text = (caption + ' ' + filename).lower()
    for cat, keywords in CATEGORY_RULES:
        for kw in keywords:
            if kw in text:
                return cat
    # Default fallback category if ambiguous
    return 'escapades-creuers'

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Sizes for Masonry variety
sizes = ['short', 'medium', 'tall', 'medium']

counts = {'all': 0, 'asia': 0, 'europa': 0, 'carib-america': 0, 'escapades-creuers': 0}

item_index = 0
def categorize_item(match):
    global item_index
    full_block = match.group(0)
    
    caption_match = re.search(r'data-caption=["\']([^"\']+)["\']', full_block)
    src_match = re.search(r'src=["\']([^"\']+)["\']', full_block)
    
    caption = caption_match.group(1) if caption_match else ''
    src = src_match.group(1) if src_match else ''
    
    cat = get_category(caption, src)
    counts[cat] += 1
    counts['all'] += 1
    
    size_class = sizes[item_index % len(sizes)]
    item_index += 1
    
    # Add data-category and size class to gallery-item
    updated_block = re.sub(
        r'<div class="gallery-item"',
        f'<div class="gallery-item {size_class}" data-category="{cat}"',
        full_block,
        count=1
    )
    return updated_block

pattern = r'<div class="gallery-item"[^>]*>.*?</div>\s*</div>'
updated_html, total = re.subn(pattern, categorize_item, html, flags=re.DOTALL)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(updated_html)

print(f'Categorized {total} gallery items!')
print('Counts:', counts)

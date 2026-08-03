import re

def clean_caption(filename):
    base = filename.rsplit('/', 1)[-1].rsplit('.', 1)[0]
    
    alpha_chars = re.sub(r'[\d\-]', '', base)
    if len(alpha_chars) < 3:
        return 'Galeria de viatgers - Nòmades del Món'

    base = re.sub(r'[\-_]?\d+$', '', base)
    words = base.replace('-', ' ').replace('_', ' ').split()
    
    filtered_words = [w for w in words if not w.isdigit()]
    if not filtered_words:
        return 'Galeria de viatgers - Nòmades del Món'
        
    text = ' '.join(filtered_words).title()
    
    replacements = [
        (r'\bHotel Royalton Riviera Maya\b|\bHotel Royalton Rivivera Maya\b', 'Hotel Royalton, Riviera Maya'),
        (r'\bRiviera Maya\b', 'Riviera Maya (Mèxic)'),
        (r'\bThailandia\b|\bThailand\b', 'Tailàndia'),
        (r'\bIndonesia\b', 'Indonèsia'),
        (r'\bMexico\b', 'Mèxic'),
        (r'\bParis\b', 'París'),
        (r'\bNew York\b|\bNova York\b', 'Nova York'),
        (r'\bTromso\b', 'Tromsø (Noruega)'),
        (r'\bCosta Oest\b', 'Costa Oest (EUA)'),
        (r'\bDisney\b|\bDisneyland\b', 'Disneyland París'),
        (r'\bNormandia\b', 'Normandía'),
        (r'\bMont Saint Michel\b', 'Mont-Saint-Michel'),
        (r'\bJapo\b|\bJapan\b', 'Japó'),
        (r'\bTimisoara\b', 'Timișoara (Romania)'),
        (r'\bSri Lanka\b', 'Sri Lanka'),
        (r'\bMaldives\b', 'Maldives')
    ]
    
    for pat, rep in replacements:
        text = re.sub(pat, rep, text, flags=re.IGNORECASE)
        
    text = re.sub(r'\s+', ' ', text).strip()
    return text

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

def replace_item(match):
    full_block = match.group(0)
    src_match = re.search(r'src=["\']([^"\']+)["\']', full_block)
    if src_match:
        src_url = src_match.group(1)
        caption = clean_caption(src_url)
        updated_block = re.sub(r'data-caption=["\'][^"\']*["\']', f'data-caption="{caption}"', full_block)
        updated_block = re.sub(r'(<div class="gallery-overlay">.*?<span>)(.*?)(</span>)', rf'\1{caption}\3', updated_block, flags=re.DOTALL)
        return updated_block
    return full_block

pattern = r'<div class="gallery-item"[^>]*>.*?</div>\s*</div>'
updated_html, count = re.subn(pattern, replace_item, html, flags=re.DOTALL)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(updated_html)

print(f'Successfully re-updated captions for {count} gallery items!')

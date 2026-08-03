import re

# Comprehensive map of file slug / caption fragments to pure clean destination names
LOCATION_RULES = [
    (r'.*abu dhabi.*', 'Abu Dhabi (EAU)'),
    (r'.*alida.*', 'Carib'),
    (r'.*amazones.*', 'Amazones (Brasil)'),
    (r'.*menorca.*', 'Menorca'),
    (r'.*egipte.*', 'Egipte'),
    (r'.*loira.*|.*mont-saint-michel.*', 'Disneyland París, Normandia & Mont-Saint-Michel'),
    (r'.*praga.*', 'Praga (República Txeca)'),
    (r'.*bali.*', 'Bali (Indonèsia)'),
    (r'.*berlin.*', 'Berlín (Alemanya)'),
    (r'.*billund.*', 'Billund (Dinamarca)'),
    (r'.*cabo verde.*', 'Cap Verd'),
    (r'.*camboja.*', 'Camboja'),
    (r'.*canada.*', 'Canadà'),
    (r'.*notre damme.*|.*eiffel.*', 'París (França)'),
    (r'.*china.*|.*muralla xina.*|.*xina.*', 'Xina'),
    (r'.*costa oest.*|.*gran canon.*|.*yosemite.*', 'Costa Oest (EUA)'),
    (r'.*creuer.*grecia.*|.*santorini.*', 'Santorini & Grècia'),
    (r'.*creuer.*', 'Creuer pel Mediterrani'),
    (r'.*disney.*|.*futuroscope.*', 'Disneyland París'),
    (r'.*dubai.*', 'Dubai (EAU)'),
    (r'.*himalaya.*|.*nepal.*', 'Himalaia (Nepal)'),
    (r'.*toscana.*', 'La Toscana (Itàlia)'),
    (r'.*suissa.*', 'Suïssa'),
    (r'.*fuerteventura.*', 'Fuerteventura'),
    (r'.*fushimi.*|.*nikko.*|.*japo.*|.*japan.*', 'Japó'),
    (r'.*royalton.*|.*rivera maya.*|.*riviera maya.*', 'Hotel Royalton, Riviera Maya (Mèxic)'),
    (r'.*illes gregues.*', 'Illes Gregues'),
    (r'.*india.*', 'Índia'),
    (r'.*indonesia.*', 'Indonèsia'),
    (r'.*islandia.*', 'Islàndia'),
    (r'.*lanzarote.*', 'Lanzarote'),
    (r'.*maldives.*', 'Maldives'),
    (r'.*teruel.*', 'Terol'),
    (r'.*nyc.*|.*nova york.*|.*new york.*', 'Nova York (EUA)'),
    (r'.*mexic.*|.*punta cana.*', 'Carib & Mèxic'),
    (r'.*formentera.*', 'Formentera'),
    (r'.*sardenya.*', 'Sardenya (Itàlia)'),
    (r'.*tailandia.*', 'Tailàndia'),
    (r'.*lisboa.*', 'Lisboa (Portugal)')
]

def sanitize_caption(caption, filename=''):
    text = (caption + ' ' + filename).lower()
    
    for pat, clean_name in LOCATION_RULES:
        if re.search(pat, text):
            return clean_name
            
    return 'Galeria de viatgers - Nòmades del Món'

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

def replace_item(match):
    full_block = match.group(0)
    src_match = re.search(r'src=["\']([^"\']+)["\']', full_block)
    caption_match = re.search(r'data-caption=["\']([^"\']+)["\']', full_block)
    
    current_cap = caption_match.group(1) if caption_match else ''
    src_url = src_match.group(1) if src_match else ''
    
    clean = sanitize_caption(current_cap, src_url)
    
    updated_block = re.sub(r'data-caption=["\'][^"\']*["\']', f'data-caption="{clean}"', full_block)
    updated_block = re.sub(r'(<div class="gallery-overlay">.*?<span>)(.*?)(</span>)', rf'\1{clean}\3', updated_block, flags=re.DOTALL)
    return updated_block

pattern = r'<div class="gallery-item"[^>]*>.*?</div>\s*</div>'
updated_html, count = re.subn(pattern, replace_item, html, flags=re.DOTALL)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(updated_html)

print(f'Successfully sanitized captions for {count} items!')

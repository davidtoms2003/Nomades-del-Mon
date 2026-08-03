import urllib.request
import re

url = 'https://www.nomadesdelmon.com/ca/el-mon-dels-nomades/'
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
try:
    html = urllib.request.urlopen(req).read().decode('utf-8')
    urls = re.findall(r'https://images\.gestionaweb\.cat/1231/img-960-0/[a-zA-Z0-9_.-]+\.jpg', html)
    urls = list(dict.fromkeys(urls))
    
    html_blocks = []
    for u in urls:
        html_blocks.append(f'''                    <div class="gallery-item" data-caption="Galeria de viatgers">
                        <img src="{u}" alt="Foto galeria" loading="lazy">
                        <div class="gallery-overlay">
                            <i class="fa-solid fa-magnifying-glass-plus"></i>
                            <span>Veure imatge</span>
                        </div>
                    </div>''')

    with open('index.html', 'r', encoding='utf-8') as f:
        page_html = f.read()

    # Find the section and replace it
    pattern = r'(<!-- VIEW: EL MÓN DELS NÒMADES \(TRAVEL GALLERY\) -->.*?<div class="offer-gallery-grid">)(.*?)(</div>\s*</div>\s*</section>)'
    
    match = re.search(pattern, page_html, re.DOTALL)
    if match:
        new_html = re.sub(pattern, lambda m: m.group(1) + '\n' + '\n'.join(html_blocks) + '\n                ' + m.group(3), page_html, flags=re.DOTALL)
        with open('index.html', 'w', encoding='utf-8') as f:
            f.write(new_html)
        print('Successfully replaced images in index.html with', len(urls), 'images.')
    else:
        print('Pattern not found in index.html!')
except Exception as e:
    print('Error:', e)

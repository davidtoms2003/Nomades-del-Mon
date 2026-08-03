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
        html_blocks.append(f'''                    <div class="gallery-item" data-caption="Galeria de viatgers - Nòmades del Món">
                        <img src="{u}" alt="Foto galeria" loading="lazy">
                        <div class="gallery-overlay">
                            <i class="fa-solid fa-magnifying-glass-plus"></i>
                            <span>Veure imatge</span>
                        </div>
                    </div>''')

    with open('index.html', 'r', encoding='utf-8') as f:
        page_html = f.read()

    start_str = '<div class="offer-gallery-grid">'
    end_str = '</div>\n            </div>\n        </section>\n\n        <!-- ==========================================\n        <!-- VIEW: COMENTARIS'

    # Actually let's just find <div class="offer-gallery-grid"> and the closing </div> of it.
    idx_start = page_html.find(start_str)
    
    # We know the next section is VIEW: COMENTARIS
    idx_end = page_html.find('<!-- VIEW: COMENTARIS -->', idx_start)
    
    # the closing of the grid is a few divs before the comment
    # Let's just find the last </div> before idx_end that closes the container
    # Or just replace the string between them
    
    if idx_start != -1 and idx_end != -1:
        prefix = page_html[:idx_start + len(start_str)]
        
        # we need to find the end of the grid.
        # It's at 
        #                 </div>
        #             </div>
        #         </section>
        
        # so let's just search for '                </div>\n            </div>\n        </section>'
        suffix_str = '                </div>\n            </div>\n        </section>'
        idx_suffix = page_html.find(suffix_str, idx_start)
        
        if idx_suffix != -1:
            suffix = page_html[idx_suffix:]
            new_html = prefix + '\n' + '\n'.join(html_blocks) + '\n' + suffix
            with open('index.html', 'w', encoding='utf-8') as f:
                f.write(new_html)
            print('Successfully replaced images in index.html with', len(urls), 'images.')
        else:
            print('Suffix not found')
    else:
        print('Start or end not found')

except Exception as e:
    print('Error:', e)

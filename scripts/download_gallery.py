import urllib.request
import re
import os
import concurrent.futures

url = 'https://www.nomadesdelmon.com/ca/el-mon-dels-nomades/'
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
try:
    html = urllib.request.urlopen(req).read().decode('utf-8')
    urls = re.findall(r'https://images\.gestionaweb\.cat/1231/img-960-0/[a-zA-Z0-9_.-]+\.jpg', html)
    urls = list(dict.fromkeys(urls))
    
    os.makedirs('galeria_viatgers', exist_ok=True)
    
    def download_image(u):
        filename = u.split('/')[-1]
        filepath = os.path.join('galeria_viatgers', filename)
        if not os.path.exists(filepath):
            try:
                req = urllib.request.Request(u, headers={
                    'User-Agent': 'Mozilla/5.0',
                    'Referer': 'https://www.nomadesdelmon.com/'
                })
                img_data = urllib.request.urlopen(req, timeout=10).read()
                with open(filepath, 'wb') as f:
                    f.write(img_data)
                return True
            except Exception as e:
                return False
        return True

    print(f'Starting download of {len(urls)} images...')
    success = 0
    with concurrent.futures.ThreadPoolExecutor(max_workers=20) as executor:
        results = list(executor.map(download_image, urls))
        success = sum(1 for r in results if r)
    
    print(f'Downloaded {success} out of {len(urls)} images.')
    
    # Update index.html to point to local files
    with open('index.html', 'r', encoding='utf-8') as f:
        page_html = f.read()

    # We can just replace the prefix
    page_html = page_html.replace('https://images.gestionaweb.cat/1231/img-960-0/', 'galeria_viatgers/')
    
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(page_html)
    print('Updated index.html to use local images')
except Exception as e:
    print('Error:', e)

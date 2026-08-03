import urllib.request
import re

url = 'https://www.nomadesdelmon.com/ca/el-mon-dels-nomades/'
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
try:
    html = urllib.request.urlopen(req).read().decode('utf-8')
    imgs = re.findall(r'<img[^>]+src=[\"\'](https?://[^\"\']+)[\"\'][^>]*>', html)
    print(f'Found {len(imgs)} images.')
    for img in imgs:
        if 'logo' not in img.lower() and 'icon' not in img.lower() and 'bandera' not in img.lower():
            print(img)
except Exception as e:
    print('Error:', e)

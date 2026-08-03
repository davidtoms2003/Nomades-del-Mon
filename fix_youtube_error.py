import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Remove meta referrer from head
html = re.sub(r'\s*<meta name="referrer" content="no-referrer">\s*', '\n', html)

# 2. Update YouTube iframe
old_iframe = r'<iframe\s+loading="lazy"\s+src="https://www\.youtube\.com/embed/Ed6KMSmxv3k[^"]*".*?</iframe>'
new_iframe = '''<iframe 
                                loading="lazy"
                                src="https://www.youtube.com/embed/Ed6KMSmxv3k"
                                title="Vídeo Nòmades Del Món"
                                allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share"
                                referrerpolicy="strict-origin-when-cross-origin"
                                allowfullscreen>
                            </iframe>'''

html = re.sub(old_iframe, new_iframe, html, flags=re.DOTALL)

# 3. Add referrerpolicy="no-referrer" to all gallery <img> tags that don't already have it
def add_ref_policy(match):
    img_tag = match.group(0)
    if 'referrerpolicy' not in img_tag:
        img_tag = img_tag.replace('loading="lazy"', 'loading="lazy" referrerpolicy="no-referrer"')
    return img_tag

html = re.sub(r'<img[^>]+gestionaweb[^>]+>', add_ref_policy, html)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print('Updated index.html: removed global meta referrer, updated iframe & added referrerpolicy to gallery images.')

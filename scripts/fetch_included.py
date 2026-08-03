import urllib.request, re

urls = [
    'https://www.nomadesdelmon.com/ca/ofertes-2/combinat-sri-lanka-maldives-amb-overwater-13-dies-11-nits-especial-nuvis/',
    'https://www.nomadesdelmon.com/ca/ofertes-2/nova-york-8-dies-7-nits/',
    'https://www.nomadesdelmon.com/ca/ofertes-2/paris-romantica-4-dies-3-nits/',
    'https://www.nomadesdelmon.com/ca/ofertes-2/vietnam-16-dies-15-nits/'
]

for url in urls:
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    try:
        html = urllib.request.urlopen(req).read().decode('utf-8')
        
        # We can extract text from the DOM.
        from html.parser import HTMLParser
        class MyHTMLParser(HTMLParser):
            def __init__(self):
                super().__init__()
                self.text = []
            def handle_data(self, data):
                if data.strip(): self.text.append(data.strip())
        parser = MyHTMLParser()
        parser.feed(html)
        text_content = '\n'.join(parser.text)
        
        print(f'=== URL: {url} ===')
        idx = text_content.upper().find('EL PREU INCLOU')
        if idx != -1:
            print(text_content[idx:idx+2000])
        else:
            print('NOT FOUND')
    except Exception as e:
        print(e)

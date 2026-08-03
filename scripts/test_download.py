import urllib.request
import time

urls = [
    "https://images.gestionaweb.cat/1231/pimg-1600-1600/04-05-montse-pedro-costa-oest-eeuu.jpg",
    "https://images.gestionaweb.cat/1231/pimg-1600-1600/04-05-montse-pedro-costa-oest2.jpg",
    "https://images.gestionaweb.cat/1231/pimg-1600-1600/04-05-moteros-a-teruel.jpg"
]

for u in urls:
    try:
        t0 = time.time()
        req = urllib.request.Request(u, headers={'User-Agent': 'Mozilla/5.0'})
        data = urllib.request.urlopen(req).read()
        print(f"Downloaded {u.split('/')[-1]}: {len(data)/1024:.1f} KB in {time.time()-t0:.2f}s")
    except Exception as e:
        print(f"Error {u}: {e}")

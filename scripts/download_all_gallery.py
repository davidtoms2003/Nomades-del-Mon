import os
import re
import urllib.request
from concurrent.futures import ThreadPoolExecutor, as_completed

def main():
    repo_dir = r"D:\Nomades Del Món\Pagina Web"
    output_dir = os.path.join(repo_dir, "galeria_nomades")
    os.makedirs(output_dir, exist_ok=True)

    index_path = os.path.join(repo_dir, "index.html")
    with open(index_path, "r", encoding="utf-8") as f:
        html = f.read()

    urls = re.findall(r'https?://images\.gestionaweb\.cat/[^\s\'"><]+', html)
    unique_urls = sorted(list(set(urls)))

    print(f"Trobat {len(unique_urls)} imatges úniques per descarregar...")

    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}

    def download_image(url):
        filename = url.split('/')[-1]
        filepath = os.path.join(output_dir, filename)
        
        # Avoid re-downloading if already exists and non-empty
        if os.path.exists(filepath) and os.path.getsize(filepath) > 0:
            return True, filename

        try:
            req = urllib.request.Request(url, headers=headers)
            with urllib.request.urlopen(req, timeout=15) as resp:
                data = resp.read()
                with open(filepath, 'wb') as f:
                    f.write(data)
            return True, filename
        except Exception as e:
            print(f"Error descarregant {filename}: {e}", flush=True)
            return False, filename

    success_count = 0
    fail_count = 0

    with ThreadPoolExecutor(max_workers=20) as executor:
        futures = {executor.submit(download_image, u): u for u in unique_urls}
        for idx, future in enumerate(as_completed(futures), 1):
            success, name = future.result()
            if success:
                success_count += 1
            else:
                fail_count += 1
            if idx % 50 == 0 or idx == len(unique_urls):
                print(f"Progrés: {idx}/{len(unique_urls)} (Exitós: {success_count}, Errors: {fail_count})", flush=True)

    print(f"\nProcés completat! {success_count} imatges descarregades a {output_dir}")

if __name__ == "__main__":
    main()

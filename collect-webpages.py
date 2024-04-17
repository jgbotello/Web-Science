import sys
import requests
from bs4 import BeautifulSoup
import random

def get_links(url):
    try:
        response = requests.get(url, timeout=5)
        soup = BeautifulSoup(response.content, 'html.parser')
        links = [link.get('href') for link in soup.find_all('a')]
        return links
    except Exception as e:
        print(f"Error fetching links from {url}: {e}")
        return []

def is_html(url):
    try:
        response = requests.head(url, timeout=5)
        content_type = response.headers.get('Content-Type', '')
        content_length = int(response.headers.get('Content-Length', 0))
        return 'text/html' in content_type and content_length > 1000
    except Exception as e:
        print(f"Error checking HTML for {url}: {e}")
        return False

def collect_uris(seed_url, max_uris=500):
    collected_uris = set()
    seed_urls = [seed_url]

    while len(collected_uris) < max_uris and seed_urls:
        random_seed = random.choice(seed_urls)
        seed_urls.remove(random_seed)

        links = get_links(random_seed)
        for link in links:
            if link and link.startswith('http'):
                if link not in collected_uris and is_html(link):
                    collected_uris.add(link)
                    print(link)

        seed_urls.extend(links)

    return collected_uris

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 collect-webpages.py <seed_url>")
        sys.exit(1)

    seed_url = sys.argv[1]
    uris = collect_uris(seed_url)

    with open('collected_uris.txt', 'w') as file:
        for uri in uris:
            file.write(uri + '\n')
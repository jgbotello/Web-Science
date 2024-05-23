import os
import requests
from bs4 import BeautifulSoup
import hashlib

def get_main_text(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    # Remove script and style tags
    for script in soup(["script", "style"]):
        script.extract()
    # Get text
    text = soup.get_text()
    return text

def download_html_content(uri):
    try:
        response = requests.get(uri, timeout=10)
        if response.status_code == 200:
            return response.text
        else:
            print(f"Failed to download HTML content from {uri}. Status code: {response.status_code}")
            return None
    except Exception as e:
        print(f"Error downloading HTML content from {uri}: {e}")
        return None

def save_content_to_file(content, filename):
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)

def save_uri_mapping(uri, hashed_uri, filename):
    with open(filename, 'a', encoding='utf-8') as f:
        f.write(f"{uri}\t{hashed_uri}\n")

def main():
    input_file = 'collected_uris.txt'
    output_directory = 'html_files'
    uri_mapping_file = 'uri_mapping.txt'

    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    with open(input_file, 'r', encoding='utf-8') as f:
        uris = f.read().splitlines()

    for uri in uris:
        html_content = download_html_content(uri)
        if html_content:
            hashed_uri = hashlib.md5(uri.strip().encode()).hexdigest()
            main_text = get_main_text(html_content)
            filename = os.path.join(output_directory, f"{hashed_uri}.html")
            save_content_to_file(main_text, filename)
            save_uri_mapping(uri, hashed_uri, uri_mapping_file)

if __name__ == "__main__":
    main()
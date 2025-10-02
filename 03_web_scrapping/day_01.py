import requests
from bs4 import BeautifulSoup

URL = 'https://en.wikipedia.org/wiki/Python_(programming_language)'

def get_h2_headers(url):
    headers = {
        "User-Agent": (
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/117.0.0.0 Safari/537.36"
        )
    }

    try:
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
    except requests.RequestException as e:
        print(f"Failed to fetch page:\n{e}")
        return []

    soup = BeautifulSoup(response.text, 'html.parser')
    h2_tags = soup.find_all('h2')

    headers = []
    for tag in h2_tags:
        header_text = tag.get_text(strip=True).replace("[edit]", "")
        if header_text and header_text.lower() != 'contents':
            headers.append(header_text)

    print(headers)

get_h2_headers(URL)



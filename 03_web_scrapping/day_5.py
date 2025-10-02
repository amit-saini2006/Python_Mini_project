import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import re
import wget

BASE_URL = "https://books.toscrape.com/"
IMAGE_DIR = "images"

def sanitize_filename(title):
    return re.sub(r'[^\w\-_. ]', '', title).replace(" ", '_')

def download_image(image_url, filename):
    try:
        response = requests.get(image_url, stream=True, timeout=10)
        response.raise_for_status()
        with open(filename, 'wb') as f:
            for chunk in response.iter_content(8192):
                f.write(chunk)
    except Exception as e:
        print(f"Failed to download {filename} - {e}")

def scrape_and_download_images():
    url = BASE_URL
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    books = soup.select("article.product_pod")[:10]

    if not os.path.exists(IMAGE_DIR):
        os.makedirs(IMAGE_DIR)

    for book in books:
        title = book.h3.a['title']  # can check day3 code for long method
        relative_img = book.find('img')['src']
        img_url = urljoin(BASE_URL, relative_img)
        print(f"url - {img_url}")

        filename = sanitize_filename(title) + ".jpg"
        filepath = os.path.join(IMAGE_DIR, filename)
        print(f"filepath: {filepath}")

        print(f"Dowloading: {title}")
        # download_image(img_url, filepath)
        wget.download(img_url, filepath)
    print("All books covers downloaded to images/")

if __name__ == '__main__':
    scrape_and_download_images()

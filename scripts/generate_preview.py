import requests
from bs4 import BeautifulSoup
import json
import os

def fetch_og_data(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    og_data = {
        'title': soup.find('meta', property='og:title')["content"] if soup.find('meta', property='og:title') else 'No Title',
        'description': soup.find('meta', property='og:description')["content"] if soup.find('meta', property='og:description') else 'No Description',
        'image': soup.find('meta', property='og:image')["content"] if soup.find('meta', property='og:image') else '',
        'url': url
    }
    return og_data

def save_html_preview(og_data, output_dir='output'):
    os.makedirs(output_dir, exist_ok=True)
    html_content = f"""
    <html>
    <head><title>URL Preview</title></head>
    <body>
        <h1>{og_data['title']}</h1>
        <p>{og_data['description']}</p>
        <img src="{og_data['image']}" alt="Preview Image" width="300">
        <p><a href="{og_data['url']}">Visit Site</a></p>
    </body>
    </html>
    """
    with open(f"{output_dir}/preview.html", 'w') as file:
        file.write(html_content)

if __name__ == "__main__":
    url = input("Enter the URL: ")
    og_data = fetch_og_data(url)
    save_html_preview(og_data)

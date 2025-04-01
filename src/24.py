import requests
from bs4 import BeautifulSoup

def get_html(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.text
    else:
        return None

def parse_html(html):
    soup = BeautifulSoup(html, 'html.parser')
    # Add your code to process the HTML and extract relevant information here
    pass

url = "https://example.com"
html_content = get_html(url)
if html_content is not None:
    parsed_html = parse_html(html_content)
    print(parsed_html)
else:
    print("Failed to load the webpage")

import requests
from bs4 import BeautifulSoup

def fetch(url):
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        # Add your code here to parse the HTML and extract data or perform any necessary operations
        pass

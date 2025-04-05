import requests
from bs4 import BeautifulSoup

def fetch_weather_data():
    url = "https://www.google.com/search?q=weather+in+location&biw=1024&bih=658&tbm=nws"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    weather_data = soup.find("div", class_="bq")  # Adjust the class attribute as needed
    return weather_data

# Example usage:
weather_data = fetch_weather_data()
print(weather_data)

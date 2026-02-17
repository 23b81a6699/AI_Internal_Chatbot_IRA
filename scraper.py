import requests
from bs4 import BeautifulSoup

def scrape_website(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    text = ""
    for p in soup.find_all("p"):
        text += p.get_text() + " "

    with open("data/website_text.txt", "w", encoding="utf-8") as f:
        f.write(text)

    return text

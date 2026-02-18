import os
import time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

def scrape_website(url):
    os.makedirs("data", exist_ok=True)

    if not url.startswith("http"):
        url = "https://" + url

    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")
    chrome_options.add_argument("--disable-blink-features=AutomationControlled")

    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=chrome_options
    )

    driver.get(url)
    time.sleep(6)

    html = driver.page_source
    driver.quit()

    soup = BeautifulSoup(html, "html.parser")

    # Remove unwanted sections
    for tag in soup(["script", "style", "footer", "nav"]):
        tag.decompose()

    texts = []

    for tag in soup.find_all(["p", "li", "h1", "h2", "h3"]):
        text = tag.get_text(strip=True)

        # REMOVE unwanted text
        if (
            len(text) > 40 and
            "copyright" not in text.lower() and
            "all rights reserved" not in text.lower() and
            "best viewed" not in text.lower()
        ):
            texts.append(text)

    final_text = ". ".join(texts)

    with open("data/website_text.txt", "w", encoding="utf-8") as f:
        f.write(final_text)

    return final_text

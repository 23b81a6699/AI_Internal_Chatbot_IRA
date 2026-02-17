from collections import deque
from pathlib import Path
from urllib.parse import urljoin, urlparse

import requests
from bs4 import BeautifulSoup

DATA_DIR = Path("data")
DATA_DIR.mkdir(exist_ok=True)


def _clean_text(items: list[str]) -> str:
    return " ".join(" ".join(items).split())


def scrape_website(start_url: str, max_pages: int = 12, timeout: int = 10) -> tuple[str, list[str]]:
    """Scrape a college website and return extracted plain text + crawled URLs."""
    parsed_start = urlparse(start_url)
    if not parsed_start.scheme:
        start_url = f"https://{start_url}"
        parsed_start = urlparse(start_url)

    domain = parsed_start.netloc
    queue = deque([start_url])
    visited = set()
    crawled_urls = []
    full_text_parts = []

    headers = {"User-Agent": "IRA-bot/1.0 (+educational assistant)"}

    while queue and len(crawled_urls) < max_pages:
        url = queue.popleft()
        if url in visited:
            continue
        visited.add(url)

        try:
            response = requests.get(url, timeout=timeout, headers=headers)
            response.raise_for_status()
        except Exception:
            continue

        soup = BeautifulSoup(response.text, "html.parser")

        for tag in soup(["script", "style", "noscript"]):
            tag.extract()

        content_blocks = []
        for node in soup.find_all(["h1", "h2", "h3", "p", "li"]):
            txt = node.get_text(" ", strip=True)
            if txt:
                content_blocks.append(txt)

        if content_blocks:
            full_text_parts.append(_clean_text(content_blocks))
            crawled_urls.append(url)

        for a in soup.find_all("a", href=True):
            next_url = urljoin(url, a["href"]).split("#")[0]
            parsed_next = urlparse(next_url)

            is_http = parsed_next.scheme in {"http", "https"}
            is_same_domain = parsed_next.netloc == domain
            is_new = next_url not in visited
            looks_page = not any(next_url.lower().endswith(ext) for ext in [".pdf", ".jpg", ".jpeg", ".png", ".zip"])

            if is_http and is_same_domain and is_new and looks_page:
                queue.append(next_url)

    combined_text = "\n".join(full_text_parts)
    (DATA_DIR / "website_text.txt").write_text(combined_text, encoding="utf-8")

    return combined_text, crawled_urls

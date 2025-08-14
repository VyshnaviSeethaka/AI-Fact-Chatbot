from ddgs import DDGS
import requests
from bs4 import BeautifulSoup
from typing import List, Dict
from config.settings import SEARCH_MAX_RESULTS, FETCH_TIMEOUT

def search_web(query: str, max_results: int = SEARCH_MAX_RESULTS) -> List[Dict]:
    q = (query or "").strip()
    if not q:
        return []
    with DDGS() as ddgs:
        return list(ddgs.text(q, max_results=max_results))

def fetch_page(url: str) -> str:
    if not url:
        return ""
    try:
        r = requests.get(url, timeout=FETCH_TIMEOUT, headers={"User-Agent": "Mozilla/5.0"})
        r.raise_for_status()
        soup = BeautifulSoup(r.text, "html.parser")
        return soup.get_text(" ", strip=True)
    except Exception:
        return ""

def search_and_fetch(query: str, max_results: int = SEARCH_MAX_RESULTS) -> str:
    snippets = []
    for item in search_web(query, max_results=max_results):
        text = fetch_page(item.get("href", ""))
        if not text:
            continue
        snippets.append(f"[{item.get('title','(no title)')}] {text[:1200]}")
    return "\n\n".join(snippets)

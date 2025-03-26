import requests
from bs4 import BeautifulSoup
import re

def scrape_emails(url):
    try:
        response = requests.get(url, timeout=5, headers={"User-Agent": "Mozilla/5.0"})
        soup = BeautifulSoup(response.text, "lxml")
        text = soup.get_text()
        emails = re.findall(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}", text)
        return list(set(emails))
    except:
        return []

def scrape_social_links(url):
    try:
        response = requests.get(url, timeout=5, headers={"User-Agent": "Mozilla/5.0"})
        soup = BeautifulSoup(response.text, "lxml")
        links = [a.get("href") for a in soup.find_all("a", href=True)]
        socials = [link for link in links if any(s in link for s in ['linkedin.com', 'instagram.com', 'twitter.com', 'facebook.com'])]
        return list(set(socials))
    except:
        return []

def scrape_about_section(url):
    try:
        response = requests.get(url, timeout=5, headers={"User-Agent": "Mozilla/5.0"})
        soup = BeautifulSoup(response.text, "lxml")
        paragraphs = [p.get_text(strip=True) for p in soup.find_all('p')]
        long_paragraphs = [p for p in paragraphs if len(p.split()) > 10]
        return sorted(long_paragraphs, key=lambda x: -len(x))[0] if long_paragraphs else ""
    except:
        return ""

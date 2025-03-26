from utils.scraping import scrape_emails, scrape_social_links, scrape_about_section
from utils.ai_helpers import summarize_about_page, ask_ai  
from bs4 import BeautifulSoup
from bs4.element import Comment
import requests

def is_visible_text(element):
    if element.parent.name in ['style', 'script', 'head', 'meta', '[document]']:
        return False
    if isinstance(element, Comment):
        return False
    return True

def process_website(url, custom_fields=[]):
    emails = scrape_emails(url)
    qualified = "Yes" if emails else "No"
    socials = scrape_social_links(url)
    about_text = scrape_about_section(url)
    summary = summarize_about_page(about_text) if about_text else "(No summary available)"

    result = {
        "Website": url,
        "Email": ', '.join(emails),
        "Socials": ', '.join(socials),
        "Summary": summary,
        "Qualified Lead": qualified
    }

    try:
        page = requests.get(url, timeout=10).text
        soup = BeautifulSoup(page, 'html.parser')
    except:
        soup = None

    for field in custom_fields:
        if field["mode"] == "Web Scraping":
            try:
                instruction = field["instruction"].strip()
                
                # If user typed a CSS selector 
                if any(instruction.startswith(c) for c in ['.', '#', '[']) or " " in instruction:
                    value = soup.select_one(instruction).get_text(strip=True) if soup.select_one(instruction) else "N/A"
                
                # Else, treat as keyword to search in visible text
                else:
                    matches = soup.find_all(string=lambda text: (
                        text and instruction.lower() in text.lower() and is_visible_text(text)
                    ))

                    value = matches[0].strip() if matches else "(Not found)"

            except Exception as e:
                value = "(Error)"

        elif field["mode"] == "AI Assistance":
            value = ask_ai(summary, field["instruction"])
        else:
            value = "N/A"
        result[field["name"]] = value

    return result

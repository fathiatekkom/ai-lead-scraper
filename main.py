from dotenv import load_dotenv
load_dotenv()

import streamlit as st
import pandas as pd

st.set_page_config(page_title="AI Lead Scraper", layout="wide")

st.title("Welcome to AI Lead Scraper! 😁")

st.write("""
Use the sidebar to choose:

- 📝 **Manual Input** to add websites one-by-one
- 📁 **Upload CSV** to bulk upload websites
- ⚙️ **Settings** to add your own custom columns using:
    - 🧠 AI Assistance (e.g. "Does the company provide a virtual assistant?")
    - 🌐 Web Scraping (e.g. Type a keyword like 'founder', 'careers', or 'email'.)

After inputting websites, you're ready to scrape!
""")

if 'manual_websites' in st.session_state and st.session_state.manual_websites:
    st.subheader("📌 Current Websites in Session")
    st.table(pd.DataFrame(st.session_state.manual_websites, columns=["Website"]))

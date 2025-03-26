from dotenv import load_dotenv
load_dotenv()

import streamlit as st
import pandas as pd
from utils.processor import process_website

st.set_page_config(page_title="Web Scraping", layout="wide")
st.title("📝 Web Scraping")

if 'manual_websites' not in st.session_state:
    st.session_state.manual_websites = []

if 'results_df' not in st.session_state:
    st.session_state.results_df = pd.DataFrame(columns=["Website", "Email", "Socials", "Summary"])

if 'delete_websites_flags' not in st.session_state:
    st.session_state.delete_websites_flags = []

if 'delete_results_flags' not in st.session_state:
    st.session_state.delete_results_flags = []

st.subheader("Enter Company Websites")
website_input = st.text_input("Type a company website (e.g. https://tokopedia.com)")

if st.button("➕ Add Website"):
    if website_input and website_input not in st.session_state.manual_websites:
        st.session_state.manual_websites.append(website_input)
        st.session_state.delete_websites_flags.append(False) 
    elif website_input in st.session_state.manual_websites:
        st.warning("Website already added!")

if st.session_state.manual_websites:
    st.markdown("### ✅ Websites to Process")

    st.session_state.delete_websites_flags = [
        st.checkbox(f"{url}", key=f"del_site_{i}", value=st.session_state.delete_websites_flags[i] if i < len(st.session_state.delete_websites_flags) else False)
        for i, url in enumerate(st.session_state.manual_websites)
    ]

    col1, col2 = st.columns(2)
    with col1:
        if st.button("❌ Delete Selected Websites"):
            st.session_state.manual_websites = [
                url for i, url in enumerate(st.session_state.manual_websites)
                if not st.session_state.delete_websites_flags[i]
            ]
            st.session_state.delete_websites_flags = [
                flag for i, flag in enumerate(st.session_state.delete_websites_flags)
                if not flag
            ]
            st.rerun()

    with col2:
        if st.button("🚀 Run Scraping"):
            result_rows = []
            with st.spinner("Scraping websites..."):
                for url in st.session_state.manual_websites:
                    result = process_website(url, st.session_state.get("custom_fields", []))
                    result_rows.append(result)
            st.session_state.results_df = pd.DataFrame(result_rows)
            st.session_state.delete_results_flags = [False] * len(result_rows)
            st.rerun()


    st.dataframe(pd.DataFrame(st.session_state.manual_websites, columns=["Website"]))


st.markdown("---")

if not st.session_state.results_df.empty:
    st.subheader("📋 Scraping Results")

    st.session_state.delete_results_flags = [
        st.checkbox(f"🗑️ Row {i+1}", key=f"del_result_{i}", value=st.session_state.delete_results_flags[i] if i < len(st.session_state.delete_results_flags) else False)
        for i in range(len(st.session_state.results_df))
    ]

    if st.button("❌ Delete Selected Results"):
        st.session_state.results_df = st.session_state.results_df.loc[
            ~pd.Series(st.session_state.delete_results_flags)
        ].reset_index(drop=True)
        st.session_state.delete_results_flags = [False] * len(st.session_state.results_df)
        st.rerun()


    st.dataframe(st.session_state.results_df)

    st.download_button(
        "⬇️ Download CSV",
        data=st.session_state.results_df.to_csv(index=False),
        file_name="lead_scraper_results.csv",
        mime="text/csv"
    )

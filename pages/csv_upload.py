import streamlit as st
import pandas as pd

st.set_page_config(page_title="CSV Upload", layout="wide")
st.title("📁 Upload Websites from CSV")

if 'manual_websites' not in st.session_state:
    st.session_state.manual_websites = []

uploaded_file = st.file_uploader("Upload a CSV file with a 'Website' column", type=["csv"])

if uploaded_file is not None:
    try:
        df = pd.read_csv(uploaded_file)
        if "Website" not in df.columns:
            st.error("❌ The CSV must contain a column named 'Website'.")
        else:
            st.success("✅ File uploaded successfully! Please go to the Web Scraper to start scraping!")
            st.dataframe(df)

            websites = df["Website"].dropna().unique().tolist()
            existing = set(st.session_state.manual_websites)

            new_websites = [w for w in websites if w not in existing]

            if new_websites:
                if st.button(f"➕ Add {len(new_websites)} New Website(s)"):
                    st.session_state.manual_websites.extend(new_websites)
                    st.success(f"Added {len(new_websites)} website(s) to your list. Please go to the Web Scraper to start scraping!")
                    st.toast(f"✅ Added {len(new_websites)} website(s)! Please go to the Web Scraper to start scraping!")
            else:
                st.info("All websites in the file already exist in your session.")
    except Exception as e:
        st.error(f"⚠️ Error reading file: {e}")




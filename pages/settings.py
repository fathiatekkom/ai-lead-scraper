import streamlit as st

st.set_page_config(page_title="Settings", layout="wide")
st.title("⚙️ Column Settings")

st.markdown("The following fields are always included: **Email, Socials, Summary**")

if 'custom_fields' not in st.session_state:
    st.session_state.custom_fields = []

st.markdown("### ➕ Add Custom Column")

with st.form("add_column_form"):
    col1, col2 = st.columns(2)
    with col1:
        mode = st.radio("Mode", ["Web Scraping", "AI Assistance"])
        column_name = st.text_input(
            "Column Name",
            help="Name of the column to show in the output (e.g. 'Founders', 'Has Chatbot')"
        )
    with col2:
        prompt_or_selector = st.text_area(
            "Prompt (AI) or Keyword (Web)",
            help="For Web Scraping, use a CSS selector like 'meta[name=author]'or a keyword like 'founder', 'careers', or 'email'. For AI, enter a question like 'Does the company offer delivery service?'",
            height=100
        )

    submitted = st.form_submit_button("Add Column")

    if submitted:
        if column_name and prompt_or_selector:
            st.session_state.custom_fields.append({
                "name": column_name,
                "mode": mode,
                "instruction": prompt_or_selector
            })
            st.success(f"Added column: {column_name} ({mode})")

if st.session_state.custom_fields:
    st.markdown("### 📋 Current Custom Columns")

    delete_flags = []
    for i, field in enumerate(st.session_state.custom_fields):
        col = st.columns([0.05, 0.95])  
        with col[0]:
            delete_flags.append(st.checkbox("", key=f"del_custom_{i}"))
        with col[1]:
            st.markdown(f"**{field['name']}** ({field['mode']}): `{field['instruction']}`")

    if st.button("🗑️ Delete Selected Columns"):
        st.session_state.custom_fields = [
            field for i, field in enumerate(st.session_state.custom_fields)
            if not delete_flags[i]
        ]
        st.rerun()


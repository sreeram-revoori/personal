import streamlit as st
import streamlit.components.v1 as components
from pathlib import Path

st.set_page_config(
    page_title="Valentine 💕",
    page_icon="💕",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# IMPORTANT: keep this OFF while debugging, so you can see errors
HIDE_STREAMLIT_CHROME = False

if HIDE_STREAMLIT_CHROME:
    st.markdown(
        """
        <style>
        header {visibility: hidden;}
        footer {visibility: hidden;}
        .block-container { padding-top: 0rem; padding-bottom: 0rem; }
        </style>
        """,
        unsafe_allow_html=True,
    )

# Load index.html from the same folder as app.py
html_path = Path(__file__).parent / "index.html"

if not html_path.exists():
    st.error(f"❌ index.html not found at: {html_path}")
    st.write("Your repo root should contain: app.py, index.html, requirements.txt")
    st.stop()

html_content = html_path.read_text(encoding="utf-8")

# Render HTML
components.html(html_content, height=1000, scrolling=False)

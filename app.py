"""Suit Up — entry point.   streamlit run app.py

Two pages in a top menu: Know Your Rights (default landing page) · Start My Case (the chat).
`from core import config` first: it loads .env / Streamlit secrets into the environment before Groq starts.
"""
from pathlib import Path

import streamlit as st

from core import config, ui  # noqa: F401  (config must load first)

HERE = Path(__file__).resolve().parent

st.set_page_config(page_title=f"{ui.BRAND} · Stand up for what's yours", page_icon="⚖️", layout="wide",
                   initial_sidebar_state="expanded")
st.markdown(ui.CSS, unsafe_allow_html=True)
try:
    st.logo(str(HERE / "assets" / "logo.svg"), size="large", icon_image=str(HERE / "assets" / "icon.svg"))
except Exception:  # older Streamlit / image type not supported -> no logo, app still works
    pass

pages = [st.Page(HERE / "views" / "home.py", title="Know Your Rights", icon="⚖️", default=True),
         st.Page(HERE / "views" / "chat.py", title="Start My Case", icon="💬", url_path="case")]
try:
    nav = st.navigation(pages, position="top")
except TypeError:  # Streamlit without top navigation -> menu in the sidebar
    nav = st.navigation(pages)
nav.run()

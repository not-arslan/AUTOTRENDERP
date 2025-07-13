# components/mcx_news.py

import streamlit as st
import requests
from datetime import datetime

def render_mcx_news():
    st.subheader("🛢 Crude Oil & MCX News")
    st.caption(f"Updated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

    news_items = [
        {
            "title": "Crude Oil Prices Climb Amid Supply Worries",
            "link": "https://finance.yahoo.com",
            "image": "https://img.icons8.com/?size=512&id=48163&format=png"
        },
        {
            "title": "Natural Gas Surges After Inventory Data",
            "link": "https://finance.yahoo.com",
            "image": "https://img.icons8.com/?size=512&id=48163&format=png"
        },
    ]

    for news in news_items:
        st.markdown(f"### 🔹 [{news['title']}]({news['link']})", unsafe_allow_html=True)
        st.image(news["image"], width=50)
        st.markdown("---")

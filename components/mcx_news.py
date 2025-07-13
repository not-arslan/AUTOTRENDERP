import streamlit as st
import requests
from bs4 import BeautifulSoup
from datetime import datetime

def fetch_news(feed_url, count=4):
    try:
        response = requests.get(feed_url, timeout=5)
        soup = BeautifulSoup(response.content, "xml")
        items = soup.findAll("item")[:count]
        news_data = []
        for item in items:
            title = item.title.text
            link = item.link.text
            pub_date = item.pubDate.text
            news_data.append((title, link, pub_date))
        return news_data
    except Exception as e:
        st.error(f"❌ Failed to fetch news: {e}")
        return []

def render_news_block(title, feed_url):
    st.subheader(title)
    news_items = fetch_news(feed_url)
    for title, link, pub in news_items:
        st.markdown(f"#### 🔸 [{title}]({link})")
        st.caption(f"🕒 {pub}")
        st.image("https://img.icons8.com/?size=512&id=48163&format=png", width=50)
        st.markdown("---")

def render_mcx_news():
    col1, col2 = st.columns(2)

    with col1:
        render_news_block("🛢 MCX Crude Oil News", "https://feeds.finance.yahoo.com/rss/2.0/headline?s=CL=F&region=US&lang=en-US")
        render_news_block("🔥 Natural Gas News", "https://feeds.finance.yahoo.com/rss/2.0/headline?s=NG=F&region=US&lang=en-US")

    with col2:
        render_news_block("🪙 Gold & Silver News", "https://feeds.finance.yahoo.com/rss/2.0/headline?s=GC=F&region=US&lang=en-US")
        render_news_block("⚡ Electricity/Power News", "https://feeds.finance.yahoo.com/rss/2.0/headline?s=ELEC&region=US&lang=en-US")

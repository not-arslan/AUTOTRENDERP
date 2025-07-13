import streamlit as st
import requests
from datetime import datetime

def render_mcx_news():
    st.subheader("🛢 MCX Crude Oil News & LTP")

    try:
        # Static Yahoo Finance crude oil news feed
        rss_url = "https://feeds.finance.yahoo.com/rss/2.0/headline?s=CL=F&region=US&lang=en-US"
        response = requests.get(rss_url)
        if response.status_code != 200:
            st.error("Failed to fetch news.")
            return

        st.metric("🛢 Crude Oil LTP", value="₹6860.75")
        st.caption(f"Updated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        st.markdown("---")

        items = response.text.split("<item>")[1:6]
        for item in items:
            try:
                title = item.split("<title>")[1].split("</title>")[0]
                link = item.split("<link>")[1].split("</link>")[0]
                st.image("https://img.icons8.com/?size=512&id=48163&format=png", width=40)
                st.markdown(f"### 🔗 [{title}]({link})")
                st.markdown("---")
            except:
                pass
    except Exception as e:
        st.error(f"⚠️ Error fetching news: {e}")

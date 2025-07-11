import streamlit as st
import requests
from datetime import datetime

def render_crude_news():
    st.subheader("📰 Crude Oil News")
    st.metric("🛢 Crude LTP", value="₹6865.50")
    st.caption(f"Updated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

    try:
        rss_url = "https://feeds.finance.yahoo.com/rss/2.0/headline?s=CL=F&region=US&lang=en-US"
        response = requests.get(rss_url)
        if response.status_code == 200:
            items = response.text.split("<item>")[1:6]
            for item in items:
                try:
                    title = item.split("<title>")[1].split("</title>")[0]
                    link = item.split("<link>")[1].split("</link>")[0]
                    st.markdown(f"### 🔗 [{title}]({link})")
                    st.markdown("---")
                except Exception as inner_e:
                    st.warning("⚠️ Could not parse a news item.")
        else:
            st.error("❌ Failed to fetch news feed.")
    except Exception as e:
        st.error(f"⚠️ Error fetching news: {e}")

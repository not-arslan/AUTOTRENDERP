import streamlit as st
import requests
from datetime import datetime

def render_crude_news():
    st.subheader("📰 Crude Oil News")
    st.metric("🛢 Crude LTP", value="₹6865.50")
    st.caption(f"Updated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

    try:
        rss_url = "https://feeds.finance.yahoo.com/rss/2.0/headline?s=CL=F&region=US&lang=en-US"
        r = requests.get(rss_url)
        items = r.text.split("<item>")[1:5]

        for item in items:
            title = item.split("<title>")[1].split("</title>")[0]
            link = item.split("<link>")[1].split("</link>")[0]
            st.markdown(f"### [{title}]({link})")
            st.markdown("---")
    except Exception as e:
        st.error("⚠️ Unable to load news feed.")

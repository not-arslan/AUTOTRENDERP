import streamlit as st
import requests
from datetime import datetime

def render_mcx_section(lang):
    st.markdown("## 🛢 MCX Crude Oil Dashboard")

    # Placeholder LTP (replace with live API later)
    ltp = 6852.50

    st.metric("📈 MCX Crude Oil LTP", value=f"₹{ltp:.2f}")
    st.caption(f"Last updated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

    st.markdown("---")

    # Language-based Info
    if lang == "Hindi":
        st.info("यह सेक्शन क्रूड ऑइल की ताज़ा कीमत और न्यूज़ दिखाएगा।")
    elif lang == "Hinglish":
        st.info("Yahan Crude Oil ka price aur news latest update ke sath dikhaya jaayega.")
    else:
        st.info("This section displays Crude Oil LTP and latest news updates.")

    st.markdown("## 📰 Crude Oil News (Hinglish 🗞️)")

    try:
        rss_url = "https://feeds.finance.yahoo.com/rss/2.0/headline?s=CL=F&region=US&lang=en-US"
        response = requests.get(rss_url)
        items = response.text.split("<item>")[1:6]

        for item in items:
            title = item.split("<title>")[1].split("</title>")[0]
            link = item.split("<link>")[1].split("</link>")[0]
            image = "https://img.icons8.com/?size=512&id=48163&format=png"  # static image

            st.markdown("### 🔸 " + title)
            st.image(image, width=40)
            st.markdown(f"[🔗 Click to Read Full News]({link})", unsafe_allow_html=True)
            st.markdown("---")

    except Exception as e:
        st.error("News fetch karne me dikkat aa rahi hai. Please check internet or feed URL.")

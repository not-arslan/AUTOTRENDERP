import streamlit as st
from components.login import angel_login
from components.chatbot import render_chatbot
from components.charts import render_charts
from components.news import render_crude_news
from components.sector_heatmap import render_sector_heatmap

st.set_page_config(page_title="FS Traders Official", layout="wide")

angel_token = angel_login()

menu = st.sidebar.radio("📊 Dashboard", ["📉 Charts", "📰 Crude News", "🔥 Sector Heatmap", "🤖 Chatbot"])

if menu == "📉 Charts":
    render_charts()
elif menu == "📰 Crude News":
    render_crude_news()
elif menu == "🔥 Sector Heatmap":
    render_sector_heatmap()
elif menu == "🤖 Chatbot":
    render_chatbot()

st.markdown("---")
st.caption("Built by FS Traders 💹")

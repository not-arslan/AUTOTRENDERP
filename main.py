# FS Traders Official - AI Powered Stock Market Dashboard

import streamlit as st
from components.admin_login import login_admin
from components.broker_login import angel_login
from components.chatbot import render_chatbot
from components.news import render_crude_news
from components.charts import render_charts
from components.calls import render_calls
from components.sector_heatmap import render_sector_heatmap
from components.option_chain import render_option_chain

import pandas as pd

# ---------------------------
# Config
# ---------------------------
st.set_page_config(page_title="FS Traders Official", layout="wide")

# ---------------------------
# Admin Login
# ---------------------------
admin_logged_in = login_admin()

if not admin_logged_in:
    st.stop()

# ---------------------------
# Angel One Broker Login
# ---------------------------
token = angel_login()

# ---------------------------
# Language Selection
# ---------------------------
lang = st.sidebar.selectbox("Language / भाषा", ["English", "Hindi", "Hinglish"])

# ---------------------------
# Sidebar Navigation
# ---------------------------
page = st.sidebar.radio("📊 Navigate", [
    "📈 Option Chain",
    "📌 PCR Dashboard",
    "📰 Crude News",
    "📉 Charts",
    "🤖 Chatbot",
    "📞 AI Calls",
    "🔥 Sector Heatmap"
])

# ---------------------------
# Render Pages
# ---------------------------
if page == "📈 Option Chain":
    render_option_chain(lang)

elif page == "📌 PCR Dashboard":
    st.title("📌 PCR Dashboard")
    st.info("PCR chart using live OI data coming soon...")

elif page == "📰 Crude News":
    render_crude_news()

elif page == "📉 Charts":
    render_charts()

elif page == "🤖 Chatbot":
    render_chatbot()

elif page == "📞 AI Calls":
    render_calls(lang)

elif page == "🔥 Sector Heatmap":
    render_sector_heatmap()

# ---------------------------
# Footer
# ---------------------------
st.markdown("---")
st.markdown("Built with ❤️ by FS Traders Official")

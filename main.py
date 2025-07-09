# FS Traders Official – AI Powered Stock Market Dashboard

import streamlit as st
from components.auth import login_user
from components.pcr import render_pcr
from components.option_chain import render_option_chain
from components.sector_heatmap import render_heatmap
from components.calls import render_calls
from components.chatbot import render_chatbot
from components.news import render_news
from components.swing_positional import render_swing_calls
from components.charts import render_charts

# Set page config
st.set_page_config(page_title="FS Traders Official", layout="wide")

# Theme setup
if 'theme' not in st.session_state:
    st.session_state.theme = 'dark'

# Language selector
lang = st.sidebar.selectbox("🌐 Language / भाषा", ["English", "Hindi", "Hinglish"])

# Login first
if not login_user():
    st.stop()

# Sidebar menu
page = st.sidebar.radio("📊 Navigate", [
    "📌 PCR Dashboard",
    "📈 Option Chain",
    "🔥 Sector Heatmap",
    "🤖 AI Auto Calls",
    "📊 Swing/Positional",
    "📈 Charts",
    "📰 News",
    "💬 AI Assistant"
])

# Page router
if page == "📌 PCR Dashboard":
    render_pcr(lang)
elif page == "📈 Option Chain":
    render_option_chain(lang)
elif page == "🔥 Sector Heatmap":
    render_heatmap(lang)
elif page == "🤖 AI Auto Calls":
    render_calls(lang)
elif page == "📊 Swing/Positional":
    render_swing_calls(lang)
elif page == "📈 Charts":
    render_charts(lang)
elif page == "📰 News":
    render_news(lang)
elif page == "💬 AI Assistant":
    render_chatbot(lang)

# Footer
st.markdown("---")
st.markdown("Built with ❤️ by FS Traders Official")

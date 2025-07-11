# FS Traders Official - AI Powered Stock Market Dashboard

import streamlit as st
from components.login import angel_login
from components.news import render_crude_news
from components.charts import render_charts
from components.chatbot import render_chatbot
from components.sector_heatmap import render_sector_heatmap

import pandas as pd

st.set_page_config(page_title="FS Traders Official", layout="wide")
token = angel_login()

page = st.sidebar.radio("📊 Navigate", [
    "📌 PCR Dashboard",
    "📈 Option Chain",
    "📰 Crude News",
    "📉 Charts",
    "🤖 Chatbot",
    "🔥 Sector Heatmap"
])

if page == "📌 PCR Dashboard":
    st.title("📌 PCR Dashboard")
    st.info("PCR chart using live OI data coming soon...")

elif page == "📈 Option Chain":
    st.title("📈 Option Chain")
    option_data = [
        {"Strike": 47500, "CE_LTP": 105, "CE_OI": 95000, "PE_OI": 120000, "PE_LTP": 98},
        {"Strike": 47600, "CE_LTP": 90,  "CE_OI": 102000, "PE_OI": 110500, "PE_LTP": 110},
    ]
    df = pd.DataFrame(option_data)
    df["PCR"] = (df["PE_OI"] / df["CE_OI"]).round(2)
    st.dataframe(df, use_container_width=True)
    st.metric("📊 Market-wide PCR", value=f"{(df['PE_OI'].sum() / df['CE_OI'].sum()):.2f}")

elif page == "📰 Crude News":
    render_crude_news()
elif page == "📉 Charts":
    render_charts()
elif page == "🤖 Chatbot":
    render_chatbot()
elif page == "🔥 Sector Heatmap":
    render_sector_heatmap()

st.markdown("---")
st.markdown("Built with ❤️ by FS Traders Official")

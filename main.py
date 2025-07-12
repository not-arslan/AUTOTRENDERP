# FS Traders Official - AI Powered Stock Market Dashboard
# main.py - Streamlit Dashboard Launcher

import streamlit as st
import pandas as pd
from components.news import render_crude_news
from components.chatbot import render_chatbot
from components.sector_heatmap import render_sector_heatmap

# ---------------------------
# Config
# ---------------------------
st.set_page_config(page_title="FS Traders Official", layout="wide")

# ---------------------------
# Sidebar Navigation
# ---------------------------
page = st.sidebar.radio("📊 Navigate", [
    "📌 OI Table + PCR",
    "📰 Crude News",
    "🤖 Chatbot",
    "🔥 Sector Heatmap"
])

# ---------------------------
# Render Pages
# ---------------------------

if page == "📌 OI Table + PCR":
    st.title("📌 OI Table + PCR")

    # Dummy sample data for now. Replace with live API logic
    option_data = [
        {"Strike": 47500, "CE_OI": 95000, "PE_OI": 120000},
        {"Strike": 47600, "CE_OI": 102000, "PE_OI": 110500},
        {"Strike": 47700, "CE_OI": 116000, "PE_OI": 108000},
        {"Strike": 47800, "CE_OI": 131000, "PE_OI": 95000},
        {"Strike": 47900, "CE_OI": 148000, "PE_OI": 84000},
        {"Strike": 48000, "CE_OI": 162000, "PE_OI": 73000},
    ]

    df = pd.DataFrame(option_data)
    df["PCR"] = (df["PE_OI"] / df["CE_OI"]).round(2)

    def color_pcr(val):
        if val > 1.2:
            return "background-color: lightgreen"
        elif val < 0.8:
            return "background-color: lightcoral"
        return ""

    st.dataframe(
        df.style.applymap(color_pcr, subset=["PCR"]),
        use_container_width=True
    )

    st.metric("🟢 Total CE OI", value=f"{df['CE_OI'].sum():,}")
    st.metric("🔴 Total PE OI", value=f"{df['PE_OI'].sum():,}")
    st.metric("📊 Market-wide PCR", value=f"{(df['PE_OI'].sum() / df['CE_OI'].sum()):.2f}")

elif page == "📰 Crude News":
    render_crude_news()

elif page == "🤖 Chatbot":
    render_chatbot()

elif page == "🔥 Sector Heatmap":
    render_sector_heatmap()

# ---------------------------
# Footer
# ---------------------------
st.markdown("---")
st.markdown("Built with ❤️ by FS Traders Official")

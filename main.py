import streamlit as st
from components.news import render_crude_news
from components.charts import render_charts
from components.chatbot import render_chatbot
from components.sector_heatmap import render_sector_heatmap
import pandas as pd

# ---------------------------
# Config
# ---------------------------
st.set_page_config(page_title="FS Traders Official", layout="wide")

# ---------------------------
# Sidebar Navigation
# ---------------------------
page = st.sidebar.radio("📊 Navigate", [
    "📌 PCR Dashboard",
    "📈 Option Chain",
    "📰 Crude News",
    "📉 Charts",
    "🤖 Chatbot",
    "🔥 Sector Heatmap"
])

# ---------------------------
# Render Pages
# ---------------------------
if page == "📌 PCR Dashboard":
    st.title("📌 PCR Dashboard")
    st.info("PCR chart using live OI data coming soon...")

elif page == "📈 Option Chain":
    st.title("📈 Option Chain")

    option_data = [
        {"Strike": 47500, "CE_LTP": 105, "CE_OI": 95000, "PE_OI": 120000, "PE_LTP": 98},
        {"Strike": 47600, "CE_LTP": 90,  "CE_OI": 102000, "PE_OI": 110500, "PE_LTP": 110},
        {"Strike": 47700, "CE_LTP": 72,  "CE_OI": 116000, "PE_OI": 108000, "PE_LTP": 120},
        {"Strike": 47800, "CE_LTP": 55,  "CE_OI": 131000, "PE_OI": 95000,  "PE_LTP": 135},
        {"Strike": 47900, "CE_LTP": 40,  "CE_OI": 148000, "PE_OI": 84000,  "PE_LTP": 150},
        {"Strike": 48000, "CE_LTP": 28,  "CE_OI": 162000, "PE_OI": 73000,  "PE_LTP": 165},
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
        df.style.format({
            "CE_LTP": "{:.2f}",
            "PE_LTP": "{:.2f}",
            "PCR": "{:.2f}"
        }).applymap(color_pcr, subset=["PCR"]),
        use_container_width=True
    )

    st.metric("🟢 Total CE OI", value=f"{df['CE_OI'].sum():,}")
    st.metric("🔴 Total PE OI", value=f"{df['PE_OI'].sum():,}")
    st.metric("📊 Market-wide PCR", value=f"{(df['PE_OI'].sum() / df['CE_OI'].sum()):.2f}")

elif page == "📰 Crude News":
    render_crude_news()

elif page == "📉 Charts":
    render_charts()

elif page == "🤖 Chatbot":
    render_chatbot()

elif page == "🔥 Sector Heatmap":
    render_sector_heatmap()

# ---------------------------
# Footer
# ---------------------------
st.markdown("---")
st.markdown("Built with ❤️ by FS Traders Official")

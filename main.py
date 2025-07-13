# FS Traders Official - AI Powered Stock Market Dashboard

import streamlit as st
from components.calls import render_ai_calls
from components.mcx_news import render_mcx_news
from components.oi_table import render_oi_tables
from components.sector_heatmap import render_sector_heatmap

# ---------------------------
# Config
# ---------------------------
st.set_page_config(page_title="FS Traders Official", layout="wide")

# ---------------------------
# Header Quote / Slogan
# ---------------------------
st.markdown("""
<div style='text-align: center; padding: 1rem; background: #111111; border-radius: 12px; margin-bottom: 2rem;'>
    <h3 style='color: #FFD700;'>Once a <span style="color:#00FFFF;">LEGEND</span> said:</h3>
    <h2 style='color: white; font-style: italic;'>
        “Be fearful when others are greedy, and greedy when others are fearful.”
    </h2>
    <p style='color: #888888;'>— Warren Buffett</p>
</div>
""", unsafe_allow_html=True)

# ---------------------------
# Sidebar Navigation
# ---------------------------
page = st.sidebar.radio("📊 Navigate", [
    "📌 OI & PCR Tables",
    "📈 AI Calls",
    "📰 News",
    "🔥 Sector Heatmap"
])

# ---------------------------
# Page Rendering
# ---------------------------
if page == "📌 OI & PCR Tables":
    st.title("📌 OI & PCR Tables (MCX + F&O)")
    render_oi_tables()

elif page == "📈 AI Calls":
    st.title("📈 AI-Powered Buy/Sell Ideas")
    render_ai_calls()

elif page == "📰 News":
    st.title("📰 Market News - MCX & Stocks")
    render_mcx_news()

elif page == "🔥 Sector Heatmap":
    st.title("🔥 Sector Strength & Heatmap")
    render_sector_heatmap()

# ---------------------------
# Footer
# ---------------------------
st.markdown("---")
st.markdown("Built with ❤️ by FS Traders Official")

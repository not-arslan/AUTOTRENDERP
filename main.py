# FS Traders Official - AI Powered Stock Market Dashboard
# main.py - Streamlit Dashboard Launcher

import streamlit as st
import pyotp
import requests
import json
import pandas as pd
from datetime import datetime

# ---------------------------
# Config
# ---------------------------
st.set_page_config(page_title="FS Traders Official", layout="wide")

if 'theme' not in st.session_state:
    st.session_state.theme = 'dark'

lang = st.sidebar.selectbox("Language / भाषा", ["English", "Hindi", "Hinglish"])

# ---------------------------
# AngelOne Auto Login
# ---------------------------
st.sidebar.title("🔐 FS Traders Login")

try:
    api_key = st.secrets["angelone"]["api_key"]
    client_id = st.secrets["angelone"]["client_id"]
    password = st.secrets["angelone"]["password"]
    totp_secret = st.secrets["angelone"]["totp_secret"]
except:
    st.error("⚠️ AngelOne credentials missing in secrets.")
    st.stop()

if 'angel_token' not in st.session_state:
    st.sidebar.info("🔁 Generating TOTP...")
    totp = pyotp.TOTP(totp_secret).now()
    payload = {
        "client_id": client_id,
        "password": password,
        "totp": totp
    }
    headers = {"Content-Type": "application/json"}

    try:
        res = requests.post("https://smartapi.angelbroking.com/v1.0/session", headers=headers, data=json.dumps(payload))
        data = res.json()
        if data.get("status") and "data" in data:
            st.session_state.angel_token = data["data"]["access_token"]
            st.sidebar.success("✅ Angel Login Success")
        else:
            st.sidebar.error("❌ Login Failed")
            st.stop()
    except Exception as e:
        st.sidebar.error(f"❌ Error: {e}")
        st.stop()

# ---------------------------
# Sidebar Navigation
# ---------------------------
page = st.sidebar.radio("📊 Navigate", [
    "📌 PCR Dashboard",
    "📈 Option Chain",
    "📰 Crude News",
    "📉 Charts"
])

# ---------------------------
# Render Pages
# ---------------------------

if page == "📌 PCR Dashboard":
    st.title("📌 PCR Dashboard")
    st.info("PCR Chart from Live Option Chain Coming Soon!")

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
    st.title("📰 Crude Oil News")
    st.metric("📈 MCX Crude LTP", value="₹6852.50")
    st.caption(f"Updated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

    try:
        rss_url = "https://feeds.finance.yahoo.com/rss/2.0/headline?s=CL=F&region=US&lang=en-US"
        r = requests.get(rss_url)
        items = r.text.split("<item>")[1:5]

        for item in items:
            title = item.split("<title>")[1].split("</title>")[0]
            link = item.split("<link>")[1].split("</link>")[0]
            st.markdown(f"### [{title}]({link})")
            st.image("https://img.icons8.com/?size=512&id=48163&format=png", width=40)
            st.markdown("---")

    except Exception as e:
        st.error("Unable to load news feed.")

elif page == "📉 Charts":
    st.title("📉 Crude Oil Chart")
    st.info("Coming Soon: Live MCX charts via TradingView or Plotly")

# ---------------------------
# Footer
# ---------------------------
st.markdown("---")
st.markdown("Built with ❤️ by FS Traders Official")


import streamlit as st
import pandas as pd
import requests

def fetch_option_chain(token, symbol="NIFTY", exchange="NSE"):
    url = f"https://smartapi.angelbroking.com/option_chain_api_here"  # Replace with actual endpoint
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {token}"
    }
    payload = {
        "symbol": symbol,
        "exchange": exchange
    }

    try:
        res = requests.post(url, headers=headers, json=payload)
        if res.status_code == 200:
            return res.json()
        else:
            st.error("⚠️ Failed to fetch Option Chain")
    except Exception as e:
        st.error(f"❌ Error: {e}")
    return None

def render_option_chain(lang="English"):
    st.subheader("🔄 Live Option Chain")
    token = st.session_state.get("angel_token")
    if not token:
        st.error("🔐 Please login first.")
        return

    # Fetch data
    data = fetch_option_chain(token)
    if data is None:
        return

    # Dummy example until real API used
    df = pd.DataFrame([
        {"Strike": 47500, "CE_OI": 100000, "PE_OI": 120000, "CE_LTP": 95, "PE_LTP": 108},
        {"Strike": 47600, "CE_OI": 98000, "PE_OI": 114000, "CE_LTP": 88, "PE_LTP": 115},
    ])
    df["PCR"] = (df["PE_OI"] / df["CE_OI"]).round(2)

    st.dataframe(df, use_container_width=True)
    st.metric("📊 Market-wide PCR", value=f"{(df['PE_OI'].sum() / df['CE_OI'].sum()):.2f}")

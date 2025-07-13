# components/oi_table.py

import streamlit as st
import pandas as pd
import requests

def fetch_oi_data(token):
    # Replace this with your actual Angel One Option Chain API endpoint
    url = "https://apiconnect.angelbroking.com/rest/secure/angelbroking/order/v1/getOptionChain"
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json",
        "Accept": "application/json"
    }
    payload = {
        "symbol": "NIFTY",
        "exchange": "NSE"
    }

    try:
        response = requests.post(url, headers=headers, json=payload)
        if response.status_code == 200:
            return response.json()
        else:
            st.error("Failed to fetch live OI data from Angel One.")
            return None
    except Exception as e:
        st.error(f"Error fetching OI data: {e}")
        return None

def render_oi_table():
    st.title("📊 Live OI Table with PCR")
    
    token = st.session_state.get("angel_token")
    if not token:
        st.warning("🔐 Please login with Angel One credentials.")
        return

    data = fetch_oi_data(token)
    if not data:
        return

    # Parse data and build a table — adjust this depending on actual API response structure
    try:
        options = data["data"]["records"]["data"]
        rows = []
        for item in options:
            if "CE" in item and "PE" in item:
                rows.append({
                    "Strike": item["strikePrice"],
                    "CE_OI": item["CE"].get("openInterest", 0),
                    "PE_OI": item["PE"].get("openInterest", 0),
                    "CE_LTP": item["CE"].get("lastPrice", 0.0),
                    "PE_LTP": item["PE"].get("lastPrice", 0.0)
                })

        df = pd.DataFrame(rows)
        df["PCR"] = (df["PE_OI"] / df["CE_OI"]).replace([float('inf'), -float('inf')], 0).fillna(0).round(2)

        def style_pcr(val):
            if val > 1.2:
                return "background-color: lightgreen"
            elif val < 0.8:
                return "background-color: lightcoral"
            return ""

        st.dataframe(df.style.applymap(style_pcr, subset=["PCR"]), use_container_width=True)
        st.metric("📈 Total CE OI", f"{df['CE_OI'].sum():,}")
        st.metric("📉 Total PE OI", f"{df['PE_OI'].sum():,}")
        st.metric("📊 Market-wide PCR", f"{(df['PE_OI'].sum() / df['CE_OI'].sum()):.2f}")
    
    except Exception as e:
        st.error(f"Parsing error: {e}")

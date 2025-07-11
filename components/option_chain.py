# components/option_chain.py

import streamlit as st
import requests
import pandas as pd

def fetch_option_chain_data(token, symbol="BANKNIFTY"):
    """
    Placeholder logic to simulate fetching CE/PE OI & LTP from Angel API.
    Replace with actual loop for all strike prices if needed.
    """

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {token}",
        "X-ClientLocalIP": "127.0.0.1",
        "X-ClientPublicIP": "127.0.0.1",
        "X-MACAddress": "00:00:00:00:00:00"
    }

    # Example symbols (replace with actual data from Angel instruments)
    options = [
        {"strike": 47800, "CE_symbol": "BANKNIFTY24J1147800CE", "PE_symbol": "BANKNIFTY24J1147800PE", "symboltoken_CE": "999999", "symboltoken_PE": "888888"},
        {"strike": 48000, "CE_symbol": "BANKNIFTY24J1148000CE", "PE_symbol": "BANKNIFTY24J1148000PE", "symboltoken_CE": "999998", "symboltoken_PE": "888887"},
    ]

    records = []

    for opt in options:
        payload_CE = {
            "exchange": "NFO",
            "tradingsymbol": opt["CE_symbol"],
            "symboltoken": opt["symboltoken_CE"]
        }

        payload_PE = {
            "exchange": "NFO",
            "tradingsymbol": opt["PE_symbol"],
            "symboltoken": opt["symboltoken_PE"]
        }

        try:
            ce = requests.post("https://apiconnect.angelbroking.com/rest/secure/angelbroking/order/v1/getLtpData",
                               headers=headers, json=payload_CE).json()
            pe = requests.post("https://apiconnect.angelbroking.com/rest/secure/angelbroking/order/v1/getLtpData",
                               headers=headers, json=payload_PE).json()

            records.append({
                "Strike": opt["strike"],
                "CE_LTP": float(ce["data"]["ltp"]) if "data" in ce else None,
                "PE_LTP": float(pe["data"]["ltp"]) if "data" in pe else None,
                "CE_OI": float(ce["data"]["oi"]) if "data" in ce else None,
                "PE_OI": float(pe["data"]["oi"]) if "data" in pe else None
            })

        except Exception as e:
            st.warning(f"⚠️ Failed to fetch for {opt['strike']}: {e}")

    return pd.DataFrame(records)

def render_option_chain():
    st.subheader("📈 Live Option Chain")

    token = st.session_state.get("angel_token")
    if not token:
        st.error("❌ AngelOne login required.")
        return

    df = fetch_option_chain_data(token)
    if df.empty:
        st.error("❌ No data returned from Angel API.")
        return

    df["PCR"] = (df["PE_OI"] / df["CE_OI"]).round(2)

    def highlight_pcr(val):
        if val > 1.2:
            return "background-color: lightgreen"
        elif val < 0.8:
            return "background-color: lightcoral"
        return ""

    st.dataframe(
        df.style.format({
            "CE_LTP": "{:.2f}",
            "PE_LTP": "{:.2f}",
            "CE_OI": "{:,.0f}",
            "PE_OI": "{:,.0f}",
            "PCR": "{:.2f}"
        }).applymap(highlight_pcr, subset=["PCR"]),
        use_container_width=True
    )

    st.metric("🟢 Total CE OI", f"{df['CE_OI'].sum():,.0f}")
    st.metric("🔴 Total PE OI", f"{df['PE_OI'].sum():,.0f}")
    st.metric("📊 Market-wide PCR", value=f"{(df['PE_OI'].sum() / df['CE_OI'].sum()):.2f}")

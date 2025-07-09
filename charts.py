import streamlit as st
import streamlit.components.v1 as components

def render_charts(lang):
    st.subheader("📈 Interactive Technical Chart (TradingView)")

    # 🔹 Step 1: Dropdown for Symbol
    symbol_map = {
        "RELIANCE": "NSE:RELIANCE",
        "TCS": "NSE:TCS",
        "HDFCBANK": "NSE:HDFCBANK",
        "INFY": "NSE:INFY",
        "BANKNIFTY": "NSE:BANKNIFTY"
    }
    selected_stock = st.selectbox("Select Stock:", list(symbol_map.keys()))
    selected_symbol = symbol_map[selected_stock]

    # 🔹 Step 2: Dropdown for Timeframe
    timeframe_map = {
        "15 min": "15",
        "1 hour": "60",
        "1 Day": "1D"
    }
    selected_tf = st.selectbox("Select Timeframe:", list(timeframe_map.keys()))
    selected_interval = timeframe_map[selected_tf]

    # 🔹 Step 3: Embed the TradingView chart with dynamic symbol + interval
    tv_url = f"""
    <iframe src="https://s.tradingview.com/widgetembed/?frameElementId=tradingview_widget&symbol={selected_symbol}&interval={selected_interval}&hidesidetoolbar=1&saveimage=1&toolbarbg=f1f3f6&theme=dark&style=1&timezone=Asia%2FKolkata&hideideas=1" width="100%" height="500" frameborder="0" allowfullscreen></iframe>
    """

    components.html(tv_url, height=520)

    st.caption("This chart is powered by TradingView. Your custom indicator will load if saved in the public layout of your account.")

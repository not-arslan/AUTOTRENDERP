import streamlit as st

def render_ai_calls():
    tabs = st.tabs(["📈 F&O", "🛢 MCX", "🏦 Stocks"])

    with tabs[0]:
        st.subheader("📈 F&O Calls")
        st.success("BUY: BANKNIFTY 47500 CE @ ₹105 | SL: ₹95 | TP: ₹130 | Confidence: 92%")
        st.error("SELL: NIFTY 18500 PE @ ₹80 | SL: ₹90 | TP: ₹65 | Confidence: 88%")
        st.caption("🔍 AI logic: OI buildup, trend traps, RSI reversals")

    with tabs[1]:
        st.subheader("🛢 MCX Calls")
        st.success("BUY: CRUDEOIL @ ₹6850 | SL: ₹6810 | TP: ₹6920 | Confidence: 94%")
        st.error("SELL: NATURALGAS @ ₹215 | SL: ₹220 | TP: ₹208 | Confidence: 90%")
        st.caption("🔍 Trend + Volume + Delivery + AI trap analysis")

    with tabs[2]:
        st.subheader("🏦 Equity Stock Calls")
        st.success("BUY: TATASTEEL @ ₹118.5 | SL: ₹116 | TP: ₹123 | Confidence: 89%")
        st.error("SELL: HDFCBANK @ ₹1652 | SL: ₹1668 | TP: ₹1620 | Confidence: 91%")
        st.caption("🔍 Based on Delivery + Bulk Volume + Trend")

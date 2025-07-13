# components/calls.py

import streamlit as st

def render_ai_calls():
    st.subheader("🤖 AI-Powered Buy/Sell Calls")

    st.markdown("### 📦 MCX")
    st.success("BUY: CRUDEOIL @ ₹6850 | SL: ₹6810 | Target: ₹6950")
    st.info("Confidence: 88% | Trapped sellers + OI support")

    st.markdown("### 📊 F&O")
    st.success("BUY: RELIANCE @ ₹2820 | SL: ₹2785 | Target: ₹2890")
    st.warning("Confidence: 92% | Based on OI, trend reversal, bulk volumes")

    st.markdown("### 📈 Stocks")
    st.error("SELL: INFY @ ₹1645 | SL: ₹1662 | Target: ₹1600")
    st.caption("Confidence: 84% | RSI divergence, insider volume spike")

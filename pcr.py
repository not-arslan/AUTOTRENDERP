import streamlit as st

def render_pcr(lang):
    st.subheader("📌 PCR Dashboard")
    
    st.metric("NIFTY PCR", "1.14", "+0.05")
    st.metric("BANKNIFTY PCR", "0.89", "-0.02")
    
    st.write("Put/Call Ratio (PCR) gives insight into market sentiment.")
    st.info("A PCR > 1 indicates bullish sentiment, while < 1 may suggest bearish.")


import streamlit as st
import requests
from datetime import datetime

def render_mcx_section(lang):
    st.markdown("## 🛢 MCX Crude Oil Dashboard")
    ltp = 6852.50
    st.metric("📈 MCX Crude Oil LTP", value=f"₹{ltp:.2f}")
    st.caption(f"Last updated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

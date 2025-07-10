import streamlit as st
import pandas as pd
from datetime import datetime

def render_pcr(lang):
    st.markdown("## 📌 OI Table & PCR Dashboard")

    # Placeholder: Simulated Option Chain data (replace with Angel One API response)
    data = [
        {"Strike": 47500, "CE_OI": 102500, "PE_OI": 145600},
        {"Strike": 47600, "CE_OI": 109000, "PE_OI": 130500},
        {"Strike": 47700, "CE_OI": 125000, "PE_OI": 118000},
        {"Strike": 47800, "CE_OI": 142000, "PE_OI": 110500},
        {"Strike": 47900, "CE_OI": 158000, "PE_OI": 98000},
        {"Strike": 48000, "CE_OI": 162000, "PE_OI": 85000},
    ]
    df = pd.DataFrame(data)
    df["PCR"] = df["PE_OI"] / df["CE_OI"]

    # Color formatting
    def highlight_pcr(val):
        if val > 1.2:
            return 'background-color: lightgreen'
        elif val < 0.8:
            return 'background-color: lightcoral'
        else:
            return ''

    st.markdown("### 🔁 Option Chain OI Table")
    st.dataframe(
        df.style.format({"PCR": "{:.2f}"}).applymap(highlight_pcr, subset=["PCR"]),
        use_container_width=True
    )

    # Summary
    total_ce = df["CE_OI"].sum()
    total_pe = df["PE_OI"].sum()
    total_pcr = total_pe / total_ce if total_ce != 0 else 0

    st.markdown("---")
    st.markdown("### 📊 Total Market PCR")

    st.metric(label="📈 Total PE OI", value=f"{total_pe:,}")
    st.metric(label="📉 Total CE OI", value=f"{total_ce:,}")
    st.metric(label="🧮 PCR Ratio", value=f"{total_pcr:.2f}")

    # Hindi or Hinglish message if needed
    if lang == "Hindi":
        st.info("यदि PCR 1 से अधिक है, तो यह बुलिश संकेत हो सकता है। 0.8 से कम होने पर मार्केट कमजोर हो सकता है।")
    elif lang == "Hinglish":
        st.info("Agar PCR 1.2+ ho to bullish sentiment hai. Neeche 0.8 ho to bearish zone me aata hai.")
    else:
        st.info("PCR above 1.2 may indicate bullish sentiment; below 0.8 may indicate weakness.")

    st.markdown("---")
    st.caption(f"Last Updated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

import streamlit as st
import pandas as pd
from datetime import datetime

def render_option_chain(lang):
    st.markdown("## 📈 Option Chain Open Interest Table")

    # Placeholder dummy data — replace with Angel One API later
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

    # Highlight PCR color logic
    def color_pcr(val):
        if val > 1.2:
            return "background-color: lightgreen"
        elif val < 0.8:
            return "background-color: lightcoral"
        return ""

    # Show Data Table
    st.markdown("### 🔁 Option Chain Table")
    st.dataframe(
        df.style.format({
            "CE_LTP": "{:.2f}",
            "PE_LTP": "{:.2f}",
            "PCR": "{:.2f}"
        }).applymap(color_pcr, subset=["PCR"]),
        use_container_width=True
    )

    # Totals
    total_ce_oi = df["CE_OI"].sum()
    total_pe_oi = df["PE_OI"].sum()
    total_pcr = round(total_pe_oi / total_ce_oi, 2)

    st.markdown("---")
    st.markdown("### 📊 Summary")
    st.metric(label="🟢 Total CE OI", value=f"{total_ce_oi:,}")
    st.metric(label="🔴 Total PE OI", value=f"{total_pe_oi:,}")
    st.metric(label="📈 Market-wide PCR", value=f"{total_pcr:.2f}")

    # Language-specific info box
    st.markdown("---")
    if lang == "Hindi":
        st.info("यह ऑप्शन चेन डाटा लाइव होगा जैसे ही एपीआई सक्रिय हो जाता है। PCR से ट्रेंड का अंदाज़ा लगाया जाता है।")
    elif lang == "Hinglish":
        st.info("Option Chain table yahan live dikhayegi jab API active ho jaayegi. PCR se trend clear hota hai.")
    else:
        st.info("This table will show live option chain data once your Angel One API is connected. PCR helps detect sentiment.")

    st.caption(f"Last Updated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

import streamlit as st
import pandas as pd

def render_sector_heatmap():
    st.subheader("🔥 Sector Heatmap (Mock)")

    # Placeholder data
    data = {
        "Sector": ["IT", "Auto", "Banking", "FMCG", "Pharma"],
        "Change %": [1.25, -0.4, 0.8, -1.1, 2.3]
    }
    df = pd.DataFrame(data)

    def highlight(val):
        if val > 0:
            return "background-color: lightgreen"
        elif val < 0:
            return "background-color: salmon"
        return ""

    st.dataframe(df.style.applymap(highlight, subset=["Change %"]))

import streamlit as st
import pandas as pd

def render_sector_heatmap():
    st.markdown("### 🔥 Sector Strength")

    data = {
        "Sector": ["IT", "BANK", "AUTO", "FMCG", "METALS", "PHARMA"],
        "Change (%)": [1.8, -0.5, 0.9, -0.2, 2.1, 0.3]
    }
    df = pd.DataFrame(data)
    df["Color"] = df["Change (%)"].apply(lambda x: "green" if x > 0 else "red")

    st.dataframe(df[["Sector", "Change (%)"]], use_container_width=True)

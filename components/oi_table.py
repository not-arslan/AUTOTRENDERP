
import streamlit as st
import pandas as pd

def render_oi_table():
    st.subheader("🔍 Live OI Table")
    data = [
        {"Strike": 47500, "CE_OI": 100000, "PE_OI": 120000},
        {"Strike": 47600, "CE_OI": 98000, "PE_OI": 114000},
    ]
    df = pd.DataFrame(data)
    df["PCR"] = (df["PE_OI"] / df["CE_OI"]).round(2)
    st.dataframe(df, use_container_width=True)

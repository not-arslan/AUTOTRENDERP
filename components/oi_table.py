import streamlit as st
import pandas as pd

def render_oi_tables():
    col1, col2 = st.columns(2)

    # Live-ready placeholder logic — replace with real Angel One API if available
    mcx_data = pd.DataFrame([
        {"Symbol": "CRUDEOIL", "CE_OI": 165000, "PE_OI": 120000},
        {"Symbol": "NATURALGAS", "CE_OI": 95000, "PE_OI": 115000},
        {"Symbol": "GOLD", "CE_OI": 125000, "PE_OI": 142000},
        {"Symbol": "SILVER", "CE_OI": 118000, "PE_OI": 104000},
        {"Symbol": "ELECTRICITY", "CE_OI": 90000, "PE_OI": 86000},
    ])
    mcx_data["PCR"] = (mcx_data["PE_OI"] / mcx_data["CE_OI"]).round(2)

    fno_data = pd.DataFrame([
        {"Symbol": "NIFTY", "CE_OI": 182000, "PE_OI": 210000},
        {"Symbol": "BANKNIFTY", "CE_OI": 157000, "PE_OI": 180000},
        {"Symbol": "RELIANCE", "CE_OI": 131000, "PE_OI": 99000},
        {"Symbol": "INFY", "CE_OI": 98000, "PE_OI": 110000},
    ])
    fno_data["PCR"] = (fno_data["PE_OI"] / fno_data["CE_OI"]).round(2)

    with col1:
        st.markdown("### 🛢 MCX OI Table")
        st.dataframe(mcx_data, use_container_width=True)

    with col2:
        st.markdown("### 📈 F&O OI Table")
        st.dataframe(fno_data, use_container_width=True)

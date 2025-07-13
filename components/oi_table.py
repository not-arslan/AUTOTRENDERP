import streamlit as st
import pandas as pd

def render_oi_tables():
    st.subheader("🪙 OI Table with PCR - MCX & F&O Side-by-Side")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("### 🛢 MCX Contracts (Crude, NG, Gold, Silver, Electricity)")
        mcx_data = [
            {"Symbol": "CrudeOil", "CE_OI": 125000, "PE_OI": 162000},
            {"Symbol": "NaturalGas", "CE_OI": 88000, "PE_OI": 99000},
            {"Symbol": "Gold", "CE_OI": 157000, "PE_OI": 152000},
            {"Symbol": "Silver", "CE_OI": 123000, "PE_OI": 118000},
            {"Symbol": "Electricity", "CE_OI": 93000, "PE_OI": 105000},
        ]
        mcx_df = pd.DataFrame(mcx_data)
        mcx_df["PCR"] = (mcx_df["PE_OI"] / mcx_df["CE_OI"]).round(2)
        st.dataframe(mcx_df, use_container_width=True)

    with col2:
        st.markdown("### 📈 F&O Stocks")
        fo_data = [
            {"Symbol": "RELIANCE", "CE_OI": 184000, "PE_OI": 203000},
            {"Symbol": "HDFCBANK", "CE_OI": 99000, "PE_OI": 91000},
            {"Symbol": "TATASTEEL", "CE_OI": 157000, "PE_OI": 149000},
            {"Symbol": "INFY", "CE_OI": 78000, "PE_OI": 92000},
        ]
        fo_df = pd.DataFrame(fo_data)
        fo_df["PCR"] = (fo_df["PE_OI"] / fo_df["CE_OI"]).round(2)
        st.dataframe(fo_df, use_container_width=True)

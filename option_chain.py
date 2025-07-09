import streamlit as st

def render_option_chain(lang):
    st.subheader("📈 Option Chain")

    st.dataframe({
        "Strike": [19800, 19900],
        "Call OI": [120000, 140000],
        "Put OI": [110000, 130000],
        "Call LTP": [220, 180],
        "Put LTP": [160, 175]
    }, use_container_width=True)

    st.caption("Sample Option Chain Data — Live version can be integrated with Angel One SmartAPI.")

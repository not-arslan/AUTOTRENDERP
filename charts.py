import streamlit as st

def render_charts(lang):
    st.subheader("📈 Technical Charts")

    st.line_chart({
        "RELIANCE": [2810, 2825, 2805, 2850, 2835],
        "HDFCBANK": [1625, 1630, 1620, 1615, 1608]
    })

    st.caption("Live chart integration can be added via TradingView widgets or WebSocket charts.")

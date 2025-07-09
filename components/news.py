import streamlit as st

def render_news(lang):
    st.subheader("📰 Live Market News")

    st.write("📈 Market opens higher amid global rally")
    st.write("🛢️ Crude prices climb as OPEC hints at further supply cuts")
    st.write("📉 Tech stocks under pressure as bond yields spike")
    st.write("💸 FII inflows remain strong with ₹1,200 crore invested yesterday")

    st.caption("These are static headlines. Connect Yahoo Finance or Moneycontrol API for live updates.")

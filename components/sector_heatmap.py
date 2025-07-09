import streamlit as st

def render_heatmap(lang):
    st.subheader("🔥 Sector Heatmap")

    st.image("https://i.imgur.com/OfN2z5N.png", caption="Sector Performance Heatmap")

    st.caption("This is a sample static heatmap. In the full version, this will be updated every 3 minutes using real-time data.")

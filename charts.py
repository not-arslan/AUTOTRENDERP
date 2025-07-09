import streamlit as st
import streamlit.components.v1 as components

def render_charts(lang):
    st.subheader("📈 Technical Charts with Your Custom Indicator")

    st.markdown("Below is your TradingView chart loaded with your custom indicator.")

    # 🔁 Replace `symbol` and `interval` with your actual chart settings
    # If your indicator is saved in a public layout, it will appear

    tradingview_embed = """
    <iframe src="https://s.tradingview.com/widgetembed/?frameElementId=tradingview_widget&symbol=NSE:RELIANCE&interval=15&hidesidetoolbar=1&symboledit=1&saveimage=1&toolbarbg=f1f3f6&studies=[]&theme=dark&style=1&timezone=Asia%2FKolkata&withdateranges=1&hidevolume=0&hideideas=1&studies_overrides={}" width="100%" height="500" frameborder="0" allowfullscreen></iframe>
    """

    components.html(tradingview_embed, height=520)

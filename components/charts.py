import streamlit as st

def render_charts(lang):
    st.markdown("## 📈 Live Charts & Technicals")

    if lang == "Hindi":
        st.info("यह सेक्शन चार्ट, तकनीकी संकेतक और विश्लेषण दिखाएगा।")
    elif lang == "Hinglish":
        st.info("Yeh section charts aur indicators ka combo dikhayega.")
    else:
        st.info("This section will show live charts, indicators, and technical insights.")

    st.markdown("---")
    st.subheader("🧠 TradingView Widget")

    # Embed a TradingView widget (replace symbol if needed)
    tradingview_html = """
    <iframe src="https://s.tradingview.com/embed-widget/mini-symbol-overview/?locale=en#%7B%22symbol%22%3A%22MCX%3ACRUDEOIL1%21%22%2C%22width%22%3A%22600%22%2C%22height%22%3A%22350%22%2C%22locale%22%3A%22en%22%2C%22dateRange%22%3A%22D%22%2C%22colorTheme%22%3A%22dark%22%2C%22isTransparent%22%3Afalse%2C%22autosize%22%3Afalse%2C%22largeChartUrl%22%3A%22%22%7D" 
    width="100%" height="350" frameborder="0" allowtransparency="true" scrolling="no"></iframe>
    """
    st.components.v1.html(tradingview_html, height=370, scrolling=False)

    st.markdown("---")
    st.write("📌 You can add more indicators here (like RSI, MACD, EMA crossover etc).")

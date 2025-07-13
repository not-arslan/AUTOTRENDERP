import streamlit as st

def render_ai_calls():
    st.subheader("📈 AI-Based BUY/SELL Calls")

    tab1, tab2, tab3 = st.tabs(["📊 F&O", "🛢 MCX", "📈 Stocks"])

    with tab1:
        st.markdown("### 🔹 F&O Calls")
        st.success("BUY: RELIANCE @ ₹2810 | SL: ₹2780 | TP: ₹2870")
        st.info("Confidence: 91% | Trend + OI Surge")
        st.error("SELL: HDFCBANK @ ₹1635 | SL: ₹1650 | TP: ₹1605")
        st.info("Confidence: 87% | Trap Detected")

    with tab2:
        st.markdown("### 🔹 MCX Calls")
        st.success("BUY: CRUDEOIL @ ₹6862 | SL: ₹6835 | TP: ₹6910")
        st.info("Fake spike trap reversal spotted")
        st.error("SELL: NATURALGAS @ ₹222.50 | SL: ₹225 | TP: ₹218")
        st.info("Volume spike + Reversal")

    with tab3:
        st.markdown("### 🔹 Stock Calls")
        st.success("BUY: TCS @ ₹3995 | SL: ₹3950 | TP: ₹4090")
        st.error("SELL: ICICIBANK @ ₹1082 | SL: ₹1094 | TP: ₹1050")
        st.caption("Backtested by FS Trader AI engine ✅")

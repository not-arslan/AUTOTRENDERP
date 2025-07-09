import streamlit as st

def render_chatbot(lang):
    st.subheader("💬 Ask NIFTY.AI")

    q = st.text_input("Ask anything about market trend, stocks, PCR, OI etc:")

    if q:
        # Placeholder response — can be replaced with OpenAI or Gemini API
        st.info("🤖 NIFTY.AI: The market shows a bullish bias today due to positive global cues and strong OI buildup in NIFTY.")
        st.caption("Note: This is a static placeholder. Connect GPT API to make it dynamic.")
    else:
        st.caption("Type a question above and press Enter.")

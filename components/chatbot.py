import streamlit as st
import openai

def render_chatbot():
    st.subheader("🤖 MISS.TRADER Chatbot")

    try:
        openai.api_key = st.secrets["openai"]["api_key"]
    except:
        st.error("❌ OpenAI API key missing in secrets.toml")
        return

    user_input = st.text_input("Ask your stock/market question:")
    if user_input:
        with st.spinner("Thinking..."):
            try:
                response = openai.ChatCompletion.create(
                    model="gpt-3.5-turbo",
                    messages=[
                        {"role": "system", "content": "You are MISS.TRADER, an Indian stock market expert."},
                        {"role": "user", "content": user_input}
                    ]
                )
                answer = response['choices'][0]['message']['content']
                st.success(answer)
            except Exception as e:
                st.error(f"⚠️ OpenAI error: {e}")


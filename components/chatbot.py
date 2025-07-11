import streamlit as st
import openai

def render_chatbot():
    st.title("🤖 MISS.TRADER - AI Chat Assistant")

    # Set your OpenAI API key from secrets
    openai.api_key = st.secrets["openai_api_key"]

    # Initialize session state for chat history
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []

    st.markdown("Ask anything about stock market. I support English, Hindi, Hinglish 🗣️")

    # Display previous chats
    for chat in st.session_state.chat_history:
        with st.chat_message(chat["role"]):
            st.markdown(chat["content"])

    # New user message input
    user_input = st.chat_input("Enter your query...")

    if user_input:
        # Show user input
        st.chat_message("user").markdown(user_input)
        st.session_state.chat_history.append({"role": "user", "content": user_input})

        try:
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=st.session_state.chat_history,
                temperature=0.7,
                max_tokens=500,
            )
            reply = response.choices[0].message["content"]
            st.chat_message("assistant").markdown(reply)
            st.session_state.chat_history.append({"role": "assistant", "content": reply})

        except Exception as e:
            st.error(f"❌ OpenAI Error: {e}")

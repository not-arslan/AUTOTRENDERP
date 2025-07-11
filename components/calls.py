import streamlit as st
import openai

def render_calls(lang):
    st.subheader("🤖 AI Auto Calls")

    # Language prompt prefix
    lang_prefix = {
        "English": "",
        "Hindi": "Respond in Hindi. ",
        "Hinglish": "Respond in Hinglish. "
    }

    user_prompt = st.text_input("📥 Enter Market Summary or Conditions", 
        value="Give intraday trading calls based on today's market open, OI, RSI, and trend.")

    if st.button("🔍 Generate AI Calls"):
        try:
            openai.api_key = st.secrets["openai"]["api_key"]

            prompt = lang_prefix.get(lang, "") + user_prompt

            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "You are a professional trading analyst. Return 2 clear intraday stock trading calls with SL, target, and confidence rating. Use bullet points or structured output."},
                    {"role": "user", "content": prompt}
                ]
            )

            ai_output = response["choices"][0]["message"]["content"]
            st.success("✅ AI Calls Generated")
            st.markdown(ai_output)

        except Exception as e:
            st.error(f"❌ Error: {str(e)}")

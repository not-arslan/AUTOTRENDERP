import streamlit as st

st.set_page_config(page_title="🔐 FS Traders Login", layout="centered")
st.title("🔐 FS Traders Login")

# Load credentials from secrets.toml
api_key = st.secrets["api"]["api_key"]
secret_key = st.secrets["api"]["secret_key"]
client_id_secret = st.secrets["api"]["client_id"]
password_secret = st.secrets["api"]["password"]

# UI
st.subheader("Login")
client_id = st.text_input("Client ID", max_chars=30)
password = st.text_input("Password", type="password")

if st.button("Login"):
    if client_id == client_id_secret and password == password_secret:
        st.success("✅ Login successful!")
        st.code(f"API Key: {api_key}\nSecret Key: {secret_key}", language="python")
    else:
        st.error("❌ Invalid credentials. Try again.")

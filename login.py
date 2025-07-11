import streamlit as st
import pyotp
import requests
import json

def angel_login():
    st.sidebar.title("🔐 FS Traders Login")

    try:
        api_key = st.secrets["angelone"]["api_key"]
        client_id = st.secrets["angelone"]["client_id"]
        password = st.secrets["angelone"]["password"]
        totp_secret = st.secrets["angelone"]["totp_secret"]
    except:
        st.error("⚠️ AngelOne credentials missing.")
        st.stop()

    if 'angel_token' not in st.session_state:
        totp = pyotp.TOTP(totp_secret).now()
        payload = {"client_id": client_id, "password": password, "totp": totp}
        headers = {"Content-Type": "application/json"}

        try:
            res = requests.post("https://smartapi.angelbroking.com/v1.0/session", headers=headers, data=json.dumps(payload))
            data = res.json()
            if data.get("status") and "data" in data:
                st.session_state.angel_token = data["data"]["access_token"]
                st.sidebar.success("✅ Login Successful")
            else:
                st.sidebar.error("❌ Login Failed")
                st.stop()
        except Exception as e:
            st.sidebar.error(f"❌ Error: {e}")
            st.stop()
    return st.session_state.angel_token

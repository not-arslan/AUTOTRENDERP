import streamlit as st
from smartapi import SmartConnect
import pyotp

@st.cache_resource(show_spinner=False)
def angel_login():
    try:
        api_key = st.secrets["angelone"]["api_key"]
        client_id = st.secrets["angelone"]["client_id"]
        password = st.secrets["angelone"]["password"]
        totp_secret = st.secrets["angelone"]["totp_secret"]

        obj = SmartConnect(api_key=api_key)

        # Generate TOTP
        totp_code = pyotp.TOTP(totp_secret).now()

        # Login
        data = obj.generateSession(client_id, password, totp_code)

        # Save tokens
        st.session_state["angel_object"] = obj
        st.session_state["feed_token"] = data["data"]["feedToken"]
        st.session_state["refresh_token"] = data["data"]["refreshToken"]

        return obj

    except Exception as e:
        st.error(f"Angel One login failed: {e}")
        return None

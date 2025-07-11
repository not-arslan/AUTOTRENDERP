try:
    api_key = st.secrets["angelone"]["api_key"]
    client_id = st.secrets["angelone"]["client_id"]
    password = st.secrets["angelone"]["password"]
    totp_secret = st.secrets["angelone"]["totp_secret"]
except Exception as e:
    st.error("❌ AngelOne credentials missing in secrets.toml")
    st.stop()

totp = pyotp.TOTP(totp_secret).now()
payload = {
    "client_id": client_id,
    "password": password,
    "totp": totp
}
headers = {
    "Content-Type": "application/json",
    "X-Api-Key": api_key
}

login_url = "https://apiconnect.angelbroking.com/rest/auth/angelbroking/user/v1/loginByPassword"

try:
    res = requests.post(login_url, headers=headers, data=json.dumps(payload))
    st.sidebar.code(f"Status: {res.status_code}")
    st.sidebar.code(f"Response: {res.text}")

    if res.status_code != 200:
        st.error("❌ Login failed.")
        st.stop()

    data = res.json()
    if "data" in data and "jwtToken" in data["data"]:
        st.session_state.angel_token = data["data"]["jwtToken"]
        st.sidebar.success("✅ Login Successful")
    else:
        st.error("❌ Login response incomplete.")
        st.json(data)
        st.stop()

except Exception as e:
    st.sidebar.error(f"❌ Error: {e}")
    st.stop()

return st.session_state.angel_token

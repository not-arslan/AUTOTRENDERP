import streamlit as st

# Dummy database (you can connect this to your real DB or Google Sheet later)
USERS = {
    "fsadmin@gmail.com": {
        "password": "admin123",
        "role": "admin"
    },
    "testuser@gmail.com": {
        "password": "test123",
        "role": "user"
    }
}

def login_user():
    st.sidebar.subheader("Login")

    email = st.sidebar.text_input("Email", key="email_login")
    password = st.sidebar.text_input("Password", type="password", key="pass_login")

    if st.sidebar.button("🔓 Login"):
        user = USERS.get(email)
        if user and user["password"] == password:
            st.session_state.logged_in = True
            st.session_state.user_email = email
            st.session_state.user_role = user["role"]
            st.success(f"✅ Logged in as {email}")
            return True
        else:
            st.sidebar.error("❌ Invalid Credentials")
            return False

    if st.session_state.get("logged_in"):
        return True
    return False

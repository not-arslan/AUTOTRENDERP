import streamlit as st

def login_admin():
    st.sidebar.subheader("🔐 Admin Login")
    email = st.sidebar.text_input("Email")
    password = st.sidebar.text_input("Password", type="password")
    login = st.sidebar.button("Login")

    if login and email == "admin@gmail.com" and password == "Anis@1978":
        st.sidebar.success("✅ Admin login successful")
        return True
    elif login:
        st.sidebar.error("Invalid admin credentials")
    return False

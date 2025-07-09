import streamlit as st

def login_user():
    st.sidebar.subheader("🔐 Login")
    email = st.sidebar.text_input("Email")
    password = st.sidebar.text_input("Password", type="password")
    login = st.sidebar.button("Login")
    
    if login and email == "admin@gmail.com" and password == "Anis@1978":
        return True
    elif login:
        st.sidebar.error("Invalid credentials")
    
    return False


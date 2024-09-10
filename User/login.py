import streamlit as st
import webbrowser
from database import authenticate_user

def login():
        st.title("Login")
        username = st.text_input("Username", key="login_username")
        password = st.text_input("Password", type="password", key="login_password")
        if st.button("Login"):
            user = authenticate_user(username, password)
            if user:
                st.success("Logged in successfully")
                st.session_state['logged_in'] = True
                st.session_state['user_id'] = user[0]
                webbrowser.open('http://localhost:8501')  # Redirect to main.py after login
            else:
                st.error("Invalid username or password")

if __name__ == "__main__":
        login()

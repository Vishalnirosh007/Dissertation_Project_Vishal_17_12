import streamlit as st
from database import authenticate_expert  # This should authenticate expert from a database

def expert_login():
    st.title("Expert Login")
    email = st.text_input("Email", key="expert_login_email")
    password = st.text_input("Password", type="password", key="expert_login_password")

    if st.button("Login", key="expert_login_button"):
        expert = authenticate_expert(email, password)
        if expert:
            st.session_state['expert_logged_in'] = True
            st.session_state['expert_id'] = expert[0]
            st.success("Logged in successfully as an expert.")
            st.experimental_rerun()
        else:
            st.error("Invalid email or password.")

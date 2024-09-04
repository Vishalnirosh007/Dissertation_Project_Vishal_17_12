import streamlit as st
from database import store_inquiry

def contact_expert():
    st.header("Contact an Expert")
    
    with st.form("contact_form"):
        name = st.text_input("Name")
        email = st.text_input("Email")
        message = st.text_area("Message")
        submitted = st.form_submit_button("Submit")

        if submitted:
            if not name or not email or not message:
                st.error("Please fill out all fields.")
            else:
                store_inquiry(name, email, message)
                st.success("Your inquiry has been sent successfully!")

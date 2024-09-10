import streamlit as st
from database import store_inquiry

def contact_expert():
    # Page Header
    st.markdown("<h1 style='text-align: center; color: green;'>📞 Contact an Expert</h1>", unsafe_allow_html=True)
    st.markdown("""
    <p style='text-align: center; font-size: 18px;'>Need help with plant diseases or farming advice? Send your inquiry to an expert and get professional advice.</p>
    <hr style='border:1px solid #ddd;'>
    """, unsafe_allow_html=True)

    # Contact form
    with st.form("contact_form"):
        st.markdown("<h3 style='text-align: left;'>Fill Out the Form Below</h3>", unsafe_allow_html=True)
        name = st.text_input("Name", placeholder="Enter your full name")
        email = st.text_input("Email", placeholder="Enter your email address")
        message = st.text_area("Message", placeholder="Type your inquiry here")
        submitted = st.form_submit_button("Submit")

        if submitted:
            if not name or not email or not message:
                st.error("⚠️ Please fill out all fields.")
            else:
                store_inquiry(name, email, message)
                st.success("✅ Your inquiry has been sent successfully! We'll get back to you shortly.")

if __name__ == "__main__":
    contact_expert()

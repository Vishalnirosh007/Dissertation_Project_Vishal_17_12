import streamlit as st
from database import store_inquiry, get_user_inquiries_with_responses

def contact_expert():
    st.markdown("<h1 style='text-align: center; color: green;'>📞 Contact an Expert</h1>", unsafe_allow_html=True)
    st.markdown("""
    <p style='text-align: center; font-size: 18px;'>Need help with plant diseases or farming advice? Send your inquiry to an expert and get professional advice.</p>
    <hr style='border:1px solid #ddd;'>
    """, unsafe_allow_html=True)

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

def view_responses(user_email):
    st.header("📋 Your Inquiries and Responses")
    
    inquiries_with_responses = get_user_inquiries_with_responses(user_email)
    
    if inquiries_with_responses:
        for inquiry in inquiries_with_responses:
            with st.container():
                st.markdown(f"""
                    <div style="border: 1px solid #ddd; border-radius: 10px; padding: 15px; margin: 10px 0;">
                        <h4>Inquiry:</h4>
                        <p>{inquiry[1]}</p>  <!-- Inquiry message -->
                        <p><strong>Submitted at:</strong> {inquiry[2]}</p>  <!-- Inquiry timestamp -->
                        <h4>Response:</h4>
                        <p>{inquiry[3] if inquiry[3] else "No response yet"}</p>  <!-- Show response if available -->
                        <p><strong>Response Time:</strong> {inquiry[4] if inquiry[4] else "N/A"}</p>  <!-- Response timestamp -->
                    </div>
                """, unsafe_allow_html=True)
    else:
        st.warning("No inquiries found.")
        st.warning("No inquiries found.")

if __name__ == "__main__":
    user_email = st.text_input("Enter your email to view responses", placeholder="Your email")
    if user_email:
        view_responses(user_email)

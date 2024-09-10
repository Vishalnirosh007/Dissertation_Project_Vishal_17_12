import streamlit as st
from database import get_user_inquiries_with_responses

def view_responses(user_email):
    st.header("📋 Your Inquiries and Responses")
    
    inquiries_with_responses = get_user_inquiries_with_responses(user_email)
    
    if inquiries_with_responses:
        for inquiry in inquiries_with_responses:
            with st.container():
                st.markdown(f"""
                    <div style="border: 1px solid #ddd; border-radius: 10px; padding: 15px; margin: 10px 0;">
                        <h4>Inquiry:</h4>
                        <p>{inquiry[1]}</p>
                        <p><strong>Submitted at:</strong> {inquiry[2]}</p>
                        <h4>Response:</h4>
                        <p>{inquiry[3] if inquiry[3] else "No response yet"}</p>
                        <p><strong>Response Time:</strong> {inquiry[4] if inquiry[4] else "N/A"}</p>
                    </div>
                """, unsafe_allow_html=True)
    else:
        st.warning("No inquiries found.")

if __name__ == "__main__":
    user_email = st.text_input("Enter your email to view responses", placeholder="Your email")
    if user_email:
        view_responses(user_email)

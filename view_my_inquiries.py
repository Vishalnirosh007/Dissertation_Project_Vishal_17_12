import streamlit as st
from database import get_user_inquiries

def view_my_inquiries():
    st.header("My Inquiries")

    inquiries = get_user_inquiries(st.session_state['user_id'])

    if inquiries:
        for inquiry in inquiries:
            st.subheader(f"Inquiry: {inquiry['subject']}")
            st.text(f"Message: {inquiry['message']}")
            st.text(f"Date Submitted: {inquiry['submitted_at']}")

            if inquiry['response']:
                st.markdown(f"**Expert's Response:** {inquiry['response']}")
            else:
                st.warning("No response yet.")
    else:
        st.warning("You have not submitted any inquiries yet.")

import streamlit as st
from expert.expert_login import expert_login
from expert.expert_home import expert_home
from expert.view_inquiries import view_inquiries

if 'expert_logged_in' not in st.session_state:
    st.session_state['expert_logged_in'] = False
if 'expert_id' not in st.session_state:
    st.session_state['expert_id'] = None

if st.session_state['expert_logged_in']:
    st.sidebar.title("Navigation")
    expert_mode = st.sidebar.selectbox("Select Page", ["Home", "View Inquiries"], key="expert_mode")

    if expert_mode == "Home":
        expert_home()
    elif expert_mode == "View Inquiries":
        view_inquiries()

    col1, col2 = st.sidebar.columns([1, 1])

    if col1.button("Logout", key="logout_button"):
        st.session_state['expert_logged_in'] = False
        st.session_state['expert_id'] = None
        st.success("Logged out successfully.")
        st.experimental_rerun()

    #Clear Inquiries button
    ##if col2.button("Clear Inquiries", key="clear_inquiries_button"):
      ##  clear_all_inquiries()  # Call the function to clear all inquiries
        ##st.success("All inquiries have been cleared.")
        ##st.experimental_rerun()  # Rerun the app to update the inquiries list
else:
    expert_login()

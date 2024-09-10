import streamlit as st
from expert.expert_login import expert_login  # Import from the expert folder
from expert.expert_home import expert_home    # Import from the expert folder
from expert.view_inquiries import view_inquiries  # Import from the expert folder
from database import clear_all_inquiries  # Import the function to clear all inquiries

# Initialize session state for expert login
if 'expert_logged_in' not in st.session_state:
    st.session_state['expert_logged_in'] = False
if 'expert_id' not in st.session_state:
    st.session_state['expert_id'] = None

# Main navigation for expert side
if st.session_state['expert_logged_in']:
    # Expert is logged in
    st.sidebar.title("Navigation")
    expert_mode = st.sidebar.selectbox("Select Page", ["Home", "View Inquiries"], key="expert_mode")

    if expert_mode == "Home":
        expert_home()
    elif expert_mode == "View Inquiries":
        view_inquiries()

    # Logout and Clear Inquiries buttons
    col1, col2 = st.sidebar.columns([1, 1])  # Create two side-by-side columns

    # Logout button
    if col1.button("Logout", key="logout_button"):
        st.session_state['expert_logged_in'] = False
        st.session_state['expert_id'] = None
        st.success("Logged out successfully.")
        st.experimental_rerun()

    #Clear Inquiries button
    if col2.button("Clear Inquiries", key="clear_inquiries_button"):
     clear_all_inquiries()  # Call the function to clear all inquiries
     st.success("All inquiries have been cleared.")
     st.experimental_rerun()  # Rerun the app to update the inquiries list
else:
    # Expert not logged in, show login page
    expert_login()

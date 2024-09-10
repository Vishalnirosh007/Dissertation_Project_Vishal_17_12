import streamlit as st
from expert.expert_login import expert_login  # Import from the expert folder
from expert.expert_home import expert_home    # Import from the expert folder
from expert.view_inquiries import view_inquiries  # Import from the expert folder

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

    # Logout button
    if st.sidebar.button("Logout", key="logout_button"):
        st.session_state['expert_logged_in'] = False
        st.session_state['expert_id'] = None
        st.success("Logged out successfully.")
        st.experimental_rerun()
else:
    # Expert not logged in, show login page
    expert_login()

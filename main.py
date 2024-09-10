# Main.py
import streamlit as st
from database import init_db, create_user, authenticate_user, get_user_records, save_disease_record, delete_user_records
from User.home import home
from User.about import about
from User.disease_recognition import disease_recognition
from User.learn import learn, learn_tutorials, learn_video_tutorials, learn_disease_locations, learn_disease_locations_with_fertilizers_location
from User.chatbot import main as chatbot
from User.my_records import my_records, prediction_confidence_over_time
from User.contact_expert import contact_expert, view_responses  # Import both contact_expert and view_responses

# Initialize the database
init_db()

# Session State for User Authentication
if 'logged_in' not in st.session_state:
    st.session_state['logged_in'] = False
if 'user_id' not in st.session_state:
    st.session_state['user_id'] = None

def login():
    st.title("Login")
    username = st.text_input("Username", key="login_username")
    password = st.text_input("Password", type="password", key="login_password")
    if st.button("Login", key="login_button"):
        user = authenticate_user(username, password)
        if user:
            st.session_state['logged_in'] = True
            st.session_state['user_id'] = user[0]
            st.success("Logged in successfully")
            st.experimental_rerun()
        else:
            st.error("Invalid username or password")

def register():
    st.title("Register")
    username = st.text_input("Username", key="register_username")
    password = st.text_input("Password", type="password", key="register_password")
    if st.button("Register", key="register_button"):
        if create_user(username, password):
            st.success("User registered successfully")
        else:
            st.error("Username already exists. Please choose a different username.")

def logout():
    if st.sidebar.button("Logout", key="logout_button"):
        st.session_state['logged_in'] = False
        st.session_state['user_id'] = None
        st.success("Logged out successfully")
        st.experimental_rerun()

if st.session_state['logged_in']:
    st.sidebar.title("Navigation")
    logout()

    website_mode = st.sidebar.selectbox("Select Page", ["Home", "About", "Disease Recognition", "Learn", "Plant Disease Chatbot", "My Records", "Contact Expert"], key="website_mode")
    
    if website_mode == "Learn":
        learn_subpage = st.sidebar.radio("Subpage", ["Learn About Plant Diseases", "Detailed Tutorials", "Video Tutorial", "Where Diseases Are Found Locally and Globally", "Find Fertilizer and Pesticide near you"], key="learn_subpage")
        if learn_subpage == "Learn About Plant Diseases":
            learn()
        elif learn_subpage == "Detailed Tutorials":
            learn_tutorials()
        elif learn_subpage == "Video Tutorial":
            learn_video_tutorials()
        elif learn_subpage == "Where Diseases Are Found Locally and Globally":
            learn_disease_locations()
        elif learn_subpage == "Find Fertilizer and Pesticide near you":
            learn_disease_locations_with_fertilizers_location()
    elif website_mode == "My Records":
        subpage = st.sidebar.radio("Subpage", ["Records", "Prediction Confidence Over Time"], key="subpage")
        if subpage == "Records":
            my_records()
        elif subpage == "Prediction Confidence Over Time":
            prediction_confidence_over_time()
    elif website_mode == "Home":
        home()
    elif website_mode == "About":
        about()
    elif website_mode == "Disease Recognition":
        disease_recognition()
    elif website_mode == "Plant Disease Chatbot":
        chatbot()
    elif website_mode == "Contact Expert":
        # Subpage logic for Contact Expert
        contact_expert_subpage = st.sidebar.radio("Subpage", ["Contact Expert", "View Responses"], key="contact_expert_subpage")
        if contact_expert_subpage == "Contact Expert":
            contact_expert()
        elif contact_expert_subpage == "View Responses":
            user_email = st.text_input("Enter your email to view responses", placeholder="Your email")
            if user_email:
                view_responses(user_email)

else:
    auth_mode = st.selectbox("Select Action", ["Login", "Register"], key="auth_mode")
    if auth_mode == "Login":
        login()
    elif auth_mode == "Register":
        register()

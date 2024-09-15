import streamlit as st
from translations import translations
from database import init_db, create_user, authenticate_user, get_user_records, save_disease_record, delete_user_records
from User.home import home
from User.about import about
from User.disease_recognition import disease_recognition
from User.learn import learn, learn_tutorials, learn_video_tutorials, learn_disease_locations, learn_disease_locations_with_fertilizers_location
from User.chatbot import main as chatbot
from User.my_records import my_records, prediction_confidence_over_time
from User.contact_expert import contact_expert, view_responses

init_db()

language_options = {
    "English": "en",
    "தமிழ்": "ta",
    "සිංහල": "si"
}

if 'language' not in st.session_state:
    st.session_state['language'] = 'en'

selected_language_display = st.sidebar.selectbox(
    "Select Language / மொழி / භාෂාව", 
    options=list(language_options.keys()), 
    index=list(language_options.values()).index(st.session_state['language'])  # Ensure the correct default is selected
)

st.session_state['language'] = language_options[selected_language_display]

# Session State for User Authentication
if 'logged_in' not in st.session_state:
    st.session_state['logged_in'] = False
if 'user_id' not in st.session_state:
    st.session_state['user_id'] = None

def login():
    st.title(translations[st.session_state['language']]['login'])
    username = st.text_input("Username", key="login_username")
    password = st.text_input("Password", type="password", key="login_password")
    if st.button(translations[st.session_state['language']]['login'], key="login_button"):
        user = authenticate_user(username, password)
        if user:
            st.session_state['logged_in'] = True
            st.session_state['user_id'] = user[0]
            st.success(translations[st.session_state['language']]['success'])
            st.experimental_rerun()
        else:
            st.error(translations[st.session_state['language']]['invalid'])

def register():
    st.title(translations[st.session_state['language']]['register'])
    username = st.text_input("Username", key="register_username")
    password = st.text_input("Password", type="password", key="register_password")
    if st.button(translations[st.session_state['language']]['register'], key="register_button"):
        if create_user(username, password):
            st.success(translations[st.session_state['language']]['user_registered'])
        else:
            st.error(translations[st.session_state['language']]['username_exists'])

def logout():
    if st.sidebar.button(translations[st.session_state['language']]['logout'], key="logout_button"):
        # Reset session state when logging out
        st.session_state['logged_in'] = False
        st.session_state['user_id'] = None
        st.success(translations[st.session_state['language']]['logout'])
        st.experimental_rerun()  # This forces a rerun to update the UI

if st.session_state['logged_in']:
    logout()

    app_mode = st.sidebar.selectbox(translations[st.session_state['language']]['home'], [
        translations[st.session_state['language']]['home'],
        translations[st.session_state['language']]['about'],
        translations[st.session_state['language']]['disease_recognition'],
        translations[st.session_state['language']]['learn'],
        translations[st.session_state['language']]['plant_disease_chatbot'],
        translations[st.session_state['language']]['my_records'],
        translations[st.session_state['language']]['contact_expert']
    ], key="app_mode")
    
    if app_mode == translations[st.session_state['language']]['home']:
        home()
    elif app_mode == translations[st.session_state['language']]['about']:
        about()
    elif app_mode == translations[st.session_state['language']]['disease_recognition']:
        disease_recognition()
    elif app_mode == translations[st.session_state['language']]['learn']:
        learn_subpage = st.sidebar.radio("Subpage", [
            translations[st.session_state['language']]['learn_about_plant_diseases'], 
            translations[st.session_state['language']]['detailed_tutorials'], 
            translations[st.session_state['language']]['video_tutorial'], 
            translations[st.session_state['language']]['disease_locations'], 
            translations[st.session_state['language']]['fertilizer_nearby']
        ], key="learn_subpage")

        if learn_subpage == translations[st.session_state['language']]['learn_about_plant_diseases']:
            learn()
        elif learn_subpage == translations[st.session_state['language']]['detailed_tutorials']:
            learn_tutorials()
        elif learn_subpage == translations[st.session_state['language']]['video_tutorial']:
            learn_video_tutorials()
        elif learn_subpage == translations[st.session_state['language']]['disease_locations']:
            learn_disease_locations()
        elif learn_subpage == translations[st.session_state['language']]['fertilizer_nearby']:
            learn_disease_locations_with_fertilizers_location()
    elif app_mode == translations[st.session_state['language']]['plant_disease_chatbot']:
        chatbot()
    elif app_mode == translations[st.session_state['language']]['my_records']:
        subpage = st.sidebar.radio("Subpage", [
            translations[st.session_state['language']]['records'], 
            translations[st.session_state['language']]['prediction_confidence']
        ], key="subpage")
        
        if subpage == translations[st.session_state['language']]['records']:
            my_records()
        elif subpage == translations[st.session_state['language']]['prediction_confidence']:
            prediction_confidence_over_time()
    elif app_mode == translations[st.session_state['language']]['contact_expert']:
        contact_expert_subpage = st.sidebar.radio("Subpage", [
            translations[st.session_state['language']]['contact_expert'], 
            translations[st.session_state['language']]['view_responses']
        ], key="contact_expert_subpage")
        
        if contact_expert_subpage == translations[st.session_state['language']]['contact_expert']:
            contact_expert()
        elif contact_expert_subpage == translations[st.session_state['language']]['view_responses']:
            user_email = st.text_input(translations[st.session_state['language']]['enter_email'], placeholder="Your email")
            if user_email:
                view_responses(user_email)

else:
    auth_mode = st.selectbox(translations[st.session_state['language']]['login_register'], [
        translations[st.session_state['language']]['login'], 
        translations[st.session_state['language']]['register']
    ], key="auth_mode")

    if auth_mode == translations[st.session_state['language']]['login']:
        login()
    elif auth_mode == translations[st.session_state['language']]['register']:
        register()

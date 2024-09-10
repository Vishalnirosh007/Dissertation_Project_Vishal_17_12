import streamlit as st
from User.treatments import get_treatment_details

def details():
    if 'disease_name' in st.session_state:
        disease_name = st.session_state['disease_name']
        st.header(f"Details on Treatment for {disease_name}")
        
        details = get_treatment_details(disease_name)
        if details:
            st.markdown(details)
        else:
            st.error("No detailed information available for this disease.")
    else:
        st.warning("No disease selected. Please go back to the Disease Recognition page.")

if __name__ == "__main__":
    details()

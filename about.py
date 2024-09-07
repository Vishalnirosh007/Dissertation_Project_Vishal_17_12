import streamlit as st

def about():
    st.header("About")
    st.markdown("""
    #### About Dataset
    This dataset is recreated using offline augmentation from the original dataset.
    Created by francis vishal nirosh 

    #### Content
    1. train (70295 images)
    2. test (33 images)
    3. validation (17572 images)
    """)

if __name__ == "__main__":
    about()

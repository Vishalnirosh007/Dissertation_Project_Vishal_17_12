import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
from database import get_user_records, delete_user_records

def my_records():
    st.markdown("<h2 style='text-align: center; color: green;'>📋 My Disease Recognition Records 📋</h1>", unsafe_allow_html=True)
    
    # Retrieve records from the database
    records = get_user_records(st.session_state['user_id'])
    
    if records:
        for record in records:
            # Use Markdown for inside the expander title as HTML is not supported there
            expander_title = f"Disease: {record[3]} (Confidence: {float(record[4]):.2f})"
            
            with st.expander(expander_title, expanded=False):
                st.markdown(f"""
                    **Image Path:** {record[2]}  
                    **Prediction Confidence:** {float(record[4]):.2f}  
                    **Timestamp:** {record[5]}
                """, unsafe_allow_html=True)
        
        # Confirmation checkbox for clearing data
        st.markdown("<hr style='border: 1px solid #ddd;'>", unsafe_allow_html=True)
        if st.checkbox("I confirm that I want to clear all records", key="confirm_clear"):
            if st.button("Clear All Records", key="clear_btn"):
                delete_user_records(st.session_state['user_id'])
                st.success("All records have been cleared.")
                st.experimental_rerun()  # Rerun to refresh the page and show that records have been cleared
    else:
        st.warning("No records found.")

def prediction_confidence_over_time():
    st.markdown("<h2 style='text-align: center; color: green;'>📈 Prediction Confidence Over Time 📈</h1>", unsafe_allow_html=True)
    
    # Retrieve records for visualization
    records = get_user_records(st.session_state['user_id'])
    
    if records:
        # Extract data for visualization
        timestamps = [record[5] for record in records]
        confidences = [float(record[4]) for record in records]
        
        # Create a line chart for Prediction Confidence over time
        plt.figure(figsize=(10, 5))
        sns.lineplot(x=timestamps, y=confidences, marker="o", color="royalblue", linestyle='--')
        plt.xticks(rotation=45, ha="right", fontsize=10)
        plt.title("Prediction Confidence Over Time", fontsize=16)
        plt.xlabel("Timestamp", fontsize=14)
        plt.ylabel("Prediction Confidence", fontsize=14)
        plt.tight_layout()
        st.pyplot(plt)
        
    else:
        st.warning("No records found.")

if __name__ == "__main__":
    my_records()
    prediction_confidence_over_time()

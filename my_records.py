import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
from database import get_user_records, delete_user_records

def my_records():
    st.header("📋 My Disease Recognition Records")
    
    # Retrieve records
    records = get_user_records(st.session_state['user_id'])
    
    if records:
        for record in records:
            with st.expander(f"Disease: {record[3]} (Confidence: {float(record[4]):.2f})", expanded=False):
                st.markdown(f"""
                    **Image Path:** {record[2]}  
                    **Prediction Confidence:** {float(record[4]):.2f}  
                    **Timestamp:** {record[5]}
                """)
        
        # Confirmation checkbox for clearing data
        if st.checkbox("I confirm that I want to clear all records", key="confirm_clear"):
            if st.button("Clear All Records"):
                delete_user_records(st.session_state['user_id'])
                st.success("All records have been cleared.")
                st.experimental_rerun()  # Rerun to refresh the page and show that records have been cleared
    else:
        st.warning("No records found.")
        
def prediction_confidence_over_time():
    st.header("📈 Prediction Confidence Over Time")
    
    # Retrieve records
    records = get_user_records(st.session_state['user_id'])
    
    if records:
        # Extract data for visualization
        timestamps = [record[5] for record in records]
        confidences = [float(record[4]) for record in records]
        
        # Create a line chart for Prediction Confidence over time
        plt.figure(figsize=(10, 5))
        sns.lineplot(x=timestamps, y=confidences, marker="o", color="royalblue", linestyle='--')
        plt.xticks(rotation=45, ha="right")
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

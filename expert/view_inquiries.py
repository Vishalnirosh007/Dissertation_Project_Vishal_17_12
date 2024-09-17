import streamlit as st
import sqlite3

def get_all_inquiries():
    conn = sqlite3.connect('plant_disease_recognition.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM inquiries")
    inquiries = cursor.fetchall()
    conn.close()
    return inquiries

def store_response(inquiry_id, response_text):
    conn = sqlite3.connect('plant_disease_recognition.db')
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO responses (inquiry_id, response_text)
        VALUES (?, ?)
    ''', (inquiry_id, response_text))
    conn.commit()
    conn.close()

def view_inquiries():
    st.header("📋 View Inquiries")
    
    inquiries = get_all_inquiries()
    
    if inquiries:
        for inquiry in inquiries:
            with st.container():
                st.markdown(f"""
                    <div style="border: 1px solid #ddd; border-radius: 10px; padding: 15px; margin: 10px 0;">
                        <h4 style="margin-bottom: 10px;">🆔 Inquiry ID: {inquiry[0]}</h4>
                        <p><strong>Name:</strong> {inquiry[1]}</p>
                        <p><strong>Email:</strong> {inquiry[2]}</p>
                        <p><strong>Message:</strong> {inquiry[3]}</p>
                        <p><strong>Timestamp:</strong> {inquiry[4]}</p>
                    </div>
                """, unsafe_allow_html=True)

                with st.expander("Reply"):
                    with st.form(f"response_form_{inquiry[0]}"):
                        response_text = st.text_area(f"Reply to Inquiry {inquiry[0]}", placeholder="Type your response here")
                        submitted = st.form_submit_button("Send Response")
                        
                        if submitted:
                            if not response_text:
                                st.error("⚠️ Response cannot be empty.")
                            else:
                                store_response(inquiry[0], response_text)
                                st.success("✅ Response sent successfully!")

    else:
        st.warning("No inquiries found.")

if __name__ == "__main__":
    view_inquiries()

import streamlit as st
import time
import nltk
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
from spellchecker import SpellChecker
from User.chat_response import questions, answers, fallback_responses

nltk.download('punkt')

spell = SpellChecker()
vectorizer = TfidfVectorizer()

tfidf_matrix = vectorizer.fit_transform(questions)

def correct_spelling(text):
    words = text.split()
    corrected_words = [spell.correction(word) for word in words]
    return " ".join(corrected_words)

def chatbot_response(query):
    corrected_query = correct_spelling(query)
    
    query_vec = vectorizer.transform([corrected_query])
    
    similarities = cosine_similarity(query_vec, tfidf_matrix)
    
    closest = np.argmax(similarities, axis=1)[0]
    
    if similarities[0][closest] < 0.2:
        return np.random.choice(fallback_responses)
    
    return answers[closest]

def typewrite_text(text, delay=0.02):
    response_placeholder = st.empty()
    typed_text = ""
    for char in text:
        typed_text += char
        response_placeholder.markdown(f"<div class='chatbot-box'><div class='bot-text'>{typed_text}</div></div>", unsafe_allow_html=True)
        time.sleep(delay)

def main():
    st.markdown(
        """
        <style>
        .main {
            padding: 20px;
            border-radius: 10px;
            box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1);
        }
        .css-1q8dd3e {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            font-size: 18px;
        }
        .css-145kmo2 {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        }
        .stTextInput > div > div > input {
            font-size: 18px;
            padding: 10px;
        }
        .chatbot-box {
            border-radius: 10px;
            padding: 10px;
            background-color: #ffffff;
            box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1);
            margin-top: 10px;
        }
        .user-text {
            color: #007BFF;
            font-weight: bold;
            margin-bottom: 5px;
        }
        .bot-text {
            color: #333;
            margin-bottom: 10px;
        }
        </style>
        """, unsafe_allow_html=True
    )

    st.markdown("<h1 style='text-align: center; color: green;'>🌿 Plant Disease Chatbot 🌿</h1>", unsafe_allow_html=True)
    st.markdown("""
    <p style='text-align: justify; font-size: 18px;'>Ask a question about plant diseases, farming techniques, or general plant health, and get helpful responses. Start by typing your query below:</p>
    """, unsafe_allow_html=True)

    user_query = st.text_input("You:", "")
    
    if st.button("Ask"):
        if user_query.strip():
            st.markdown(f"<div class='chatbot-box'><div class='user-text'>You:</div><div class='bot-text'>{user_query}</div></div>", unsafe_allow_html=True)
            
            response = chatbot_response(user_query)
            typewrite_text(response)
        else:
            st.warning("Please ask a question.")

if __name__ == "__main__":
    main()

import streamlit as st
import time
import nltk
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
from spellchecker import SpellChecker
from chat_response import questions, answers, fallback_responses  # Import from chat_response.py

# Download NLTK data (if not already downloaded)
nltk.download('punkt')

# Initialize the spell checker
spell = SpellChecker()

# Use TF-IDF Vectorizer
vectorizer = TfidfVectorizer()

# Vectorize the questions
tfidf_matrix = vectorizer.fit_transform(questions)

# Function to correct spelling mistakes
def correct_spelling(text):
    words = text.split()
    corrected_words = [spell.correction(word) for word in words]
    return " ".join(corrected_words)

# Define the Chatbot Logic
def chatbot_response(query):
    # Correct spelling mistakes in the query
    corrected_query = correct_spelling(query)
    
    # Vectorize the user's query
    query_vec = vectorizer.transform([corrected_query])
    
    # Compute the cosine similarity between the query and all questions
    similarities = cosine_similarity(query_vec, tfidf_matrix)
    
    # Get the index of the most similar question
    closest = np.argmax(similarities, axis=1)[0]
    
    # If the highest similarity is below a threshold, use a fallback response
    if similarities[0][closest] < 0.2:  # Adjust threshold as needed
        return np.random.choice(fallback_responses)
    
    # Return the corresponding answer
    return answers[closest]

# Function to simulate typewriting effect with a faster speed
def typewrite_text(text, delay=0.02):  # Reduced delay for faster typing effect
    response_placeholder = st.empty()
    typed_text = ""
    for char in text:
        typed_text += char
        response_placeholder.markdown(f"<div class='chatbot-box'><div class='bot-text'>{typed_text}</div></div>", unsafe_allow_html=True)
        time.sleep(delay)  # Faster typing speed

# Streamlit App
def main():
    # Custom CSS to style the interface
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

    st.title("🌱 Plant Disease Chatbot")
    st.write("Ask a question about plant diseases or have a general chat!")

    # User query input
    user_query = st.text_input("You:", "")

    if st.button("Ask"):
        if user_query:
            response = chatbot_response(user_query)
            st.markdown(f"<div class='chatbot-box'><div class='user-text'>You:</div><div class='bot-text'>{user_query}</div></div>", unsafe_allow_html=True)
            typewrite_text(response)  # Display the response with typewriting effect
        else:
            st.write("Please ask a question.")

if __name__ == "__main__":
    main()

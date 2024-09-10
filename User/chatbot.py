import streamlit as st
import time
import nltk
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
from spellchecker import SpellChecker
from User.chat_response import questions, answers, fallback_responses  # Import from chat_response.py

# Download NLTK data (if not already downloaded)
nltk.download('punkt')

# Initialize the spell checker and the TF-IDF vectorizer
spell = SpellChecker()
vectorizer = TfidfVectorizer()

# Vectorize the predefined questions for similarity matching
tfidf_matrix = vectorizer.fit_transform(questions)

# Function to correct spelling mistakes in user input
def correct_spelling(text):
    words = text.split()
    corrected_words = [spell.correction(word) for word in words]
    return " ".join(corrected_words)

# Chatbot logic to generate response
def chatbot_response(query):
    # Correct any spelling mistakes in the query
    corrected_query = correct_spelling(query)
    
    # Vectorize the corrected query
    query_vec = vectorizer.transform([corrected_query])
    
    # Compute cosine similarity between query and preloaded questions
    similarities = cosine_similarity(query_vec, tfidf_matrix)
    
    # Find the most similar question
    closest = np.argmax(similarities, axis=1)[0]
    
    # If similarity is below a threshold, return a fallback response
    if similarities[0][closest] < 0.2:  # Adjust threshold as needed
        return np.random.choice(fallback_responses)
    
    # Return the corresponding answer
    return answers[closest]

# Function to simulate typewriting effect for the bot's response
def typewrite_text(text, delay=0.02):
    response_placeholder = st.empty()  # Placeholder for dynamic content
    typed_text = ""
    for char in text:
        typed_text += char
        response_placeholder.markdown(f"<div class='chatbot-box'><div class='bot-text'>{typed_text}</div></div>", unsafe_allow_html=True)
        time.sleep(delay)  # Faster typing speed

# Streamlit App
def main():
    # Custom CSS to style the interface (retaining the design from the first code)
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

    # User input area
    user_query = st.text_input("You:", "")
    
    # Process user query and generate a response
    if st.button("Ask"):
        if user_query.strip():
            # Display user's query with better visibility
            st.markdown(f"<div class='chatbot-box'><div class='user-text'>You:</div><div class='bot-text'>{user_query}</div></div>", unsafe_allow_html=True)
            
            # Generate and display the bot's response with a typewriting effect
            response = chatbot_response(user_query)
            typewrite_text(response)
        else:
            st.warning("Please ask a question.")

# Run the chatbot application
if __name__ == "__main__":
    main()

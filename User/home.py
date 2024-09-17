import streamlit as st

def home():
    
    st.markdown("<h1 style='text-align: center; color: green;'>🌱 PLANT DISEASE RECOGNITION SYSTEM 🌱</h1>", unsafe_allow_html=True)
    
    image_path = "Images/home_page.jpeg"
    st.image(image_path, use_column_width=True, caption="Detect plant diseases with precision.")
    
    st.markdown("""
    <div style="text-align: justify; padding: 20px; font-size: 18px;">
    Welcome to the Plant Disease Recognition System! Our platform is designed to assist farmers, researchers, and agriculturists in efficiently identifying plant diseases through image analysis. Simply upload a picture of your plant, and let our advanced algorithms do the rest. Together, we can protect crops and ensure healthier, more sustainable harvests.
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("<h2 style='color: #4CAF50;'>How It Works</h2>", unsafe_allow_html=True)
    
    st.markdown("""
    <ul style="font-size: 18px; line-height: 1.6;">
        <li><b>Upload Image:</b> Visit the <b>Disease Recognition</b> page and upload an image of a plant displaying signs of disease.</li>
        <li><b>Image Analysis:</b> Using state-of-the-art machine learning models, our system will quickly process the image to detect potential diseases.</li>
        <li><b>Get Results:</b> Receive a detailed report with the diagnosis and actionable recommendations to treat the issue.</li>
    </ul>
    """, unsafe_allow_html=True)

    st.markdown("<h2 style='color: #4CAF50;'>Why Choose Our System?</h2>", unsafe_allow_html=True)
    
    st.markdown("""
    <div style="text-align: justify; font-size: 18px; line-height: 1.6;">
    <b>🔍 Accurate and Reliable:</b> Our machine learning algorithms are designed to provide high accuracy in plant disease detection.<br>
    <b>💡 Easy to Use:</b> With a user-friendly interface, you can upload, analyze, and receive results with ease.<br>
    <b>⚡ Fast and Efficient:</b> Get results within seconds, allowing you to make quick, informed decisions.<br>
    <b>🌍 Global Support:</b> Our system is trained on a wide variety of plant species and diseases, ensuring coverage for crops from different regions.
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("<h2 style='color: #4CAF50;'>Ready to Get Started?</h2>", unsafe_allow_html=True)
    
    st.markdown("""
    <div style="text-align: center; font-size: 18px; line-height: 1.6;">
    <i>Click on the <b>Disease Recognition</b> page in the sidebar to upload your plant image and start diagnosing plant diseases today!</i>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("<h2 style='color: #4CAF50;'>About Us</h2>", unsafe_allow_html=True)

    st.markdown("""
    <div style="text-align: justify; font-size: 18px; line-height: 1.6;">
    I am a final-year Software Engineering student, and this project is my capstone. The Plant Disease Recognition System leverages advanced technology to support efficient plant health monitoring. Find more details about the project and my background on the <b>About Us</b> page.
    </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    home()

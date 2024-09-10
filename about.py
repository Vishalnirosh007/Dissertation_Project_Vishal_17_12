import streamlit as st

def about():
    st.markdown("<h1 style='text-align: center; color: green;'>🌱 About the Plant Disease Recognition System 🌱</h1>", unsafe_allow_html=True)
    
    st.markdown("""
    <div style="text-align: justify; padding: 20px; font-size: 18px;">
    I am <b>Francis Vishal Nirosh</b>, a final-year student pursuing a BSc in Software Engineering. The <b>Plant Disease Recognition System</b> is my capstone project, developed to assist in the early detection and prevention of plant diseases. This system is designed for farmers, researchers, and anyone involved in agriculture who wants to monitor plant health and take preventive measures early on.
    </div>
    """, unsafe_allow_html=True)
    
    # Section about the software
    st.markdown("<h2 style='color: #4CAF50;'>About the Software</h2>", unsafe_allow_html=True)
    
    st.markdown("""
    <div style="text-align: justify; font-size: 18px; line-height: 1.6;">
    The Plant Disease Recognition System is built using cutting-edge machine learning models that analyze images of plants to detect any signs of disease. By simply uploading an image of a potentially infected plant, the system identifies patterns and symptoms to provide accurate disease diagnosis. The ultimate goal is to offer fast, reliable, and actionable information to help users protect their crops and improve agricultural yields.
    </div>
    """, unsafe_allow_html=True)

    # Dataset details
    st.markdown("<h2 style='color: #4CAF50;'>About the Dataset</h2>", unsafe_allow_html=True)
    
    st.markdown("""
    <div style="text-align: justify; font-size: 18px; line-height: 1.6;">
    The dataset used for this project has been carefully curated and augmented offline from the original dataset to improve model accuracy and robustness. The dataset is structured into three parts:
    </div>
    
    <ul style="font-size: 18px; line-height: 1.6;">
        <li><b>Train:</b> 70,295 images used to train the machine learning model.</li>
        <li><b>Test:</b> 33 images to evaluate model performance during development.</li>
        <li><b>Validation:</b> 17,572 images to ensure the model generalizes well to unseen data.</li>
    </ul>
    """, unsafe_allow_html=True)
    
    # More personal details and project goals
    st.markdown("<h2 style='color: #4CAF50;'>More About Me</h2>", unsafe_allow_html=True)
    
    st.markdown("""
    <div style="text-align: justify; font-size: 18px; line-height: 1.6;">
    As a passionate student in the field of Software Engineering, my focus is on applying innovative technology to solve real-world problems. This project combines my interests in artificial intelligence, machine learning, and agriculture to create a tool that has the potential to impact the farming industry positively. Beyond this project, I aim to continue exploring the intersection of technology and agriculture to contribute to more sustainable and efficient farming practices.
    
    Feel free to connect with me for collaborations or to learn more about my work.
    </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    about()

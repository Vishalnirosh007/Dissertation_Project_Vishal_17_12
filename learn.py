import streamlit as st
import folium
from streamlit_folium import folium_static

def learn():
    st.header("Learn About Plant Diseases")
    st.markdown("""
    Understanding the symptoms and causes of various plant diseases is crucial for effective disease management. Below are some common plant diseases along with their images and explanations.

    ### 1. Apple Scab
    **Symptoms:** Dark, olive-green spots on leaves and fruits. Leaves may curl and drop early.
    **Cause:** Fungus (Venturia inaequalis)
    """)
    st.image("Images/apple_scab.jpeg", caption="Apple Scab")

    st.markdown("""
    ### 2. Black Rot (Apple)
    **Symptoms:** Concentric rings on fruit, cankers on branches, and darkened areas on leaves.
    **Cause:** Fungus (Botryosphaeria obtusa)
    """)
    st.image("Images/black_rot.jpeg", caption="Black Rot on Apple")

    st.markdown("""
    ### 3. Late Blight (Potato)
    **Symptoms:** Water-soaked lesions on leaves, stems, and tubers. Lesions may become dark and dry out.
    **Cause:** Fungus-like organism (Phytophthora infestans)
    """)
    st.image("Images/late_blight.jpeg", caption="Late Blight on Potato")

    st.markdown("""
    ### 4. Powdery Mildew (Grape)
    **Symptoms:** White, powdery fungal growth on leaves, shoots, and fruits.
    **Cause:** Fungus (Erysiphe necator)
    """)
    st.image("Images/powdery_mildew.jpeg", caption="Powdery Mildew on Grape")

    st.markdown("""
    ### 5. Tomato Yellow Leaf Curl Virus (TYLCV)
    **Symptoms:** Yellowing of leaf margins, upward curling of leaves, and stunted plant growth.
    **Cause:** Virus (Tomato Yellow Leaf Curl Virus)
    """)
    st.image("Images/tylcv.jpeg", caption="Tomato Yellow Leaf Curl Virus")

    st.markdown("""
    ### 6. Citrus Greening (Huanglongbing)
    **Symptoms:** Yellowing of leaf veins, misshapen fruit, and premature fruit drop.
    **Cause:** Bacterium (Candidatus Liberibacter spp.)
    """)
    st.image("Images/citrus_greening.jpeg", caption="Citrus Greening")

    st.markdown("""
    ### Conclusion
    Learning about plant diseases and recognizing their symptoms is the first step towards managing and preventing them. Regular monitoring and early intervention can help protect crops from severe damage.
    """)

def learn_tutorials():
    st.header("Detailed Tutorials")
    st.markdown("""
    ### Welcome to the Detailed Tutorials
    Here, you'll find in-depth guides on various topics related to plant diseases, integrated pest management, and sustainable farming practices.
    
    #### Example Tutorial: Understanding Plant Disease Life Cycles
    - **Introduction**: Learn about the different stages of plant disease life cycles.
    - **Details**: Explore how diseases spread and how they can be controlled.
    - **Visual Aids**: Diagrams, flowcharts, and more to help you understand complex concepts.
    """)

def learn_video_tutorials():
    st.header("Video Tutorials")
    st.markdown("""
    ### Watch Video Tutorials on Common Plant Diseases
    Below are some helpful video resources explaining common plant diseases, their symptoms, and methods to manage or cure them.
    """)

    # Example YouTube videos (replace with real video URLs)

    # Introduction and general plant disease management
    st.markdown("<h4>Video 1: Introduction to Plant Disease Management</h4>", unsafe_allow_html=True)
    st.video("https://www.youtube.com/watch?v=rwiKxaCrHGM")  # Replace with actual YouTube video link
    
    st.markdown("<h4>Video 2: Effective Ways to Cure Powdery Mildew</h4>", unsafe_allow_html=True)
    st.video("https://www.youtube.com/shorts/WQmgORc7hbo")  # Replace with actual YouTube video link

    st.markdown("<h4>Video 3: How to Prevent Late Blight in Potatoes</h4>", unsafe_allow_html=True)
    st.video("https://www.youtube.com/watch?v=nU3AlBJoqBk")  # Replace with actual YouTube video link

    # Apple diseases
    st.markdown("<h4>Video 4: How Apple Scab Forms</h4>", unsafe_allow_html=True)
    st.video("https://www.youtube.com/watch?v=Qh2P8u79nws")  # Replace with actual YouTube video link

    # Corn (Maize) diseases
    st.markdown("<h4>Video 5: Northern Leaf Blight in Corn - Prevention Tips</h4>", unsafe_allow_html=True)
    st.video("https://www.youtube.com/watch?v=1rZfbtyzUFQ")  # Replace with actual YouTube video link

    # Grape diseases
    st.markdown("<h4>Video 6: Black Rot in Grapes - Key Facts</h4>", unsafe_allow_html=True)
    st.video("https://www.youtube.com/watch?v=R38gR9OaE4Q")  # Replace with actual YouTube video link

    # Citrus diseases
    st.markdown("<h4>Video 7: Citrus Greening (Haunglongbing) - Causes and Solutions</h4>", unsafe_allow_html=True)
    st.video("https://www.youtube.com/watch?v=W5mg3lv9sTI")  # Replace with actual YouTube video link

    # Tomato diseases
    st.markdown("<h4>Video 8: Tomato Yellow Leaf Curl Virus - Management Techniques</h4>", unsafe_allow_html=True)
    st.video("https://www.youtube.com/watch?v=D-58aAFIyCQ")  # Replace with actual YouTube video link

    # Potato diseases
    st.markdown("<h4>Video 9: Late Blight in Potatoes - Effective Prevention and Cure</h4>", unsafe_allow_html=True)
    st.video("https://www.youtube.com/watch?v=nU3AlBJoqBk&t=11s")  # Replace with actual YouTube video link

def learn_disease_locations():
    st.header("Where Common Plant Diseases Are Found in Sri Lanka")

    st.markdown("""
    Here is a visual representation of where common plant diseases are found in different cities and provinces of Sri Lanka.
    """)

    # Create a map centered around Sri Lanka
    sri_lanka_coords = [7.8731, 80.7718]
    disease_map = folium.Map(location=sri_lanka_coords, zoom_start=7)

    # Expanded disease data with coordinates (latitude, longitude) for different regions
    disease_locations = {
        # Apple Diseases
        "Apple Scab": {"location": [6.9497, 80.7891], "city": "Nuwara Eliya"},  # Nuwara Eliya
        "Black Rot (Apple)": {"location": [6.9808, 81.0562], "city": "Badulla"},  # Badulla
        "Cedar Apple Rust": {"location": [7.2906, 80.6337], "city": "Kandy"},  # Kandy

        # Grape Diseases
        "Black Rot (Grape)": {"location": [9.6684, 80.0074], "city": "Jaffna"},  # Jaffna
        "Esca (Black Measles)": {"location": [9.6684, 80.0074], "city": "Jaffna"},  # Jaffna
        "Powdery Mildew (Grape)": {"location": [9.6684, 80.0074], "city": "Jaffna"},  # Jaffna
        "Grape Leaf Blight": {"location": [8.5721, 81.2347], "city": "Kilinochchi"},  # Kilinochchi

        # Corn Diseases
        "Northern Leaf Blight (Corn)": {"location": [8.3114, 80.4037], "city": "Anuradhapura"},  # Anuradhapura
        "Common Rust (Corn)": {"location": [7.9115, 80.6521], "city": "Polonnaruwa"},  # Polonnaruwa
        "Gray Leaf Spot (Corn)": {"location": [7.8731, 80.7718], "city": "Kurunegala"},  # Kurunegala

        # Tomato Diseases
        "Tomato Yellow Leaf Curl Virus": {"location": [7.0834, 79.9985], "city": "Gampaha"},  # Gampaha
        "Early Blight (Tomato)": {"location": [6.9271, 79.8612], "city": "Colombo"},  # Colombo
        "Tomato Mosaic Virus": {"location": [7.5562, 80.7172], "city": "Matale"},  # Matale
        "Spider Mites (Tomato)": {"location": [8.5866, 80.6358], "city": "Trincomalee"},  # Trincomalee

        # Citrus Diseases
        "Citrus Greening (Haunglongbing)": {"location": [6.8721, 81.3294], "city": "Monaragala"},  # Monaragala

        # Potato Diseases
        "Late Blight (Potato)": {"location": [6.9497, 80.7891], "city": "Nuwara Eliya"},  # Nuwara Eliya
        "Early Blight (Potato)": {"location": [6.9808, 81.0562], "city": "Badulla"},  # Badulla

        # Pepper Diseases
        "Bacterial Spot (Pepper)": {"location": [7.8731, 80.7718], "city": "Kurunegala"},  # Kurunegala

        # Strawberry Diseases
        "Strawberry Leaf Scorch": {"location": [6.9497, 80.7891], "city": "Nuwara Eliya"},  # Nuwara Eliya
    }

    # Add markers to the map for each disease
    for disease, info in disease_locations.items():
        folium.Marker(
            location=info["location"],
            popup=f"{disease} - {info['city']}",
            tooltip=f"{disease} in {info['city']}",
            icon=folium.Icon(color="red", icon="info-sign")
        ).add_to(disease_map)

    # Display the map
    folium_static(disease_map)


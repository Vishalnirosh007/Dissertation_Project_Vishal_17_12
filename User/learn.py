import streamlit as st
import folium
from streamlit_folium import folium_static
import requests

def learn():
    st.markdown("<h1 style='text-align: center; color: green;'>🌿 Learn About Plant Diseases 🌿</h1>", unsafe_allow_html=True)
    st.markdown("""
    <p style='text-align: justify; font-size: 18px;'>Understanding the symptoms and causes of various plant diseases is crucial for effective disease management. Below are some common plant diseases along with their images and explanations:</p>
    """, unsafe_allow_html=True)

    st.markdown("""
    ### 1. Apple Scab
    **Symptoms:** Dark, olive-green spots on leaves and fruits. Leaves may curl and drop early.<br>
    **Cause:** Fungus (*Venturia inaequalis*)
    """, unsafe_allow_html=True)
    st.image("Images/apple_scab.jpeg", caption="Apple Scab")

    st.markdown("""
    ### 2. Black Rot (Apple)
    **Symptoms:** Concentric rings on fruit, cankers on branches, and darkened areas on leaves.<br>
    **Cause:** Fungus (*Botryosphaeria obtusa*)
    """, unsafe_allow_html=True)
    st.image("Images/black_rot.jpeg", caption="Black Rot on Apple")

    st.markdown("""
    ### 3. Late Blight (Potato)
    **Symptoms:** Water-soaked lesions on leaves, stems, and tubers. Lesions may become dark and dry out.<br>
    **Cause:** Fungus-like organism (*Phytophthora infestans*)
    """, unsafe_allow_html=True)
    st.image("Images/late_blight.jpeg", caption="Late Blight on Potato")

    st.markdown("""
    ### 4. Powdery Mildew (Grape)
    **Symptoms:** White, powdery fungal growth on leaves, shoots, and fruits.<br>
    **Cause:** Fungus (*Erysiphe necator*)
    """, unsafe_allow_html=True)
    st.image("Images/powdery_mildew.jpeg", caption="Powdery Mildew on Grape")

    st.markdown("""
    ### 5. Tomato Yellow Leaf Curl Virus (TYLCV)
    **Symptoms:** Yellowing of leaf margins, upward curling of leaves, and stunted plant growth.<br>
    **Cause:** Virus (Tomato Yellow Leaf Curl Virus)
    """, unsafe_allow_html=True)
    st.image("Images/tylcv.jpeg", caption="Tomato Yellow Leaf Curl Virus")

    st.markdown("""
    ### 6. Citrus Greening (Huanglongbing)
    **Symptoms:** Yellowing of leaf veins, misshapen fruit, and premature fruit drop.<br>
    **Cause:** Bacterium (*Candidatus Liberibacter spp.*)
    """, unsafe_allow_html=True)
    st.image("Images/citrus_greening.jpeg", caption="Citrus Greening")

    st.markdown("""
    ### Conclusion
    Recognizing plant disease symptoms early is key to managing and preventing them effectively. Regular monitoring and intervention can help protect crops from severe damage.
    """, unsafe_allow_html=True)

def learn_tutorials():
    st.markdown("<h1 style='text-align: center; color: green;'>📚 In-Depth Tutorials 📚</h1>", unsafe_allow_html=True)
    st.markdown("""
    <p style='text-align: justify; font-size: 18px;'>In this section, you'll find detailed guides on a variety of topics related to plant diseases, pest control, and sustainable farming practices. These tutorials will help you gain a deeper understanding of managing plant health effectively.</p>
    """, unsafe_allow_html=True)

    st.markdown("""
    ### Tutorial 1: Integrated Pest Management (IPM)
    **What is IPM?** IPM is a comprehensive approach to pest control that integrates multiple management strategies, aiming to minimize environmental damage while effectively managing pests.
    
    **Key Principles of IPM:**
    - **Prevention:** Implement cultural practices such as crop rotation, intercropping, and proper irrigation to prevent pest outbreaks.
    - **Monitoring:** Regularly inspect crops for signs of pests or diseases.
    - **Intervention:** Use biological controls like natural predators, pheromone traps, and mechanical controls before resorting to chemical pesticides.
    """)
    st.image("Images/ipm_example.jpg", caption="Integrated Pest Management Practices", use_column_width=True)

    st.markdown("""
    **Benefits of IPM:**
    - Reduces the use of chemical pesticides.
    - Promotes biodiversity and soil health.
    - Long-term pest control by disrupting pest life cycles.
    
    **Example:** In vineyards, pheromone traps can help monitor grape pests like the grapevine moth, reducing the need for blanket pesticide applications.
    """)

    st.markdown("""
    ### Tutorial 2: Crop Rotation for Disease Prevention
    **What is Crop Rotation?** Crop rotation involves planting different crops in a particular sequence to reduce the buildup of pathogens and pests that can affect plant health.
    
    **How It Works:**
    - Different crops have different nutrient requirements and attract different pests. By rotating crops, you prevent pests and diseases from accumulating in the soil.
    - For example, alternating a legume crop (like soybeans) with a cereal crop (like maize) improves soil fertility and reduces disease risk.
    """)
    st.image("Images/crop_rotation_diagram.jpg", caption="Crop Rotation for Disease Prevention", use_column_width=True)

    st.markdown("""
    **Benefits of Crop Rotation:**
    - Reduces soil-borne diseases such as root rot.
    - Helps control nematodes and other soil-dwelling pests.
    - Improves soil fertility, reducing the need for synthetic fertilizers.
    
    **Example:** Rotating tomatoes (prone to early blight) with non-susceptible crops like corn or beans helps break the disease cycle.
    """)

    st.markdown("""
    ### Tutorial 3: Sustainable Water Management in Farming
    **Why Water Management is Critical:** Effective water management helps prevent disease outbreaks caused by over-irrigation (e.g., fungal diseases) or drought stress. Watering plants optimally ensures better yield and plant health.
    
    **Techniques:**
    - **Drip Irrigation:** Delivers water directly to the plant roots, reducing the risk of foliar diseases caused by wet leaves.
    - **Rainwater Harvesting:** Collects and stores rainwater for irrigation during dry periods.
    """)
    st.image("Images/drip_irrigation_system.jpg", caption="Drip Irrigation System", use_column_width=True)

    st.markdown("""
    **Benefits:**
    - Prevents diseases caused by excess moisture, such as root rot and powdery mildew.
    - Conserves water resources by minimizing evaporation losses.
    
    **Example:** In dry regions, drip irrigation is used to grow tomatoes, preventing diseases like bacterial spot caused by overhead watering.
    """)

    st.markdown("""
    ### Tutorial 4: Recognizing Plant Disease Symptoms
    **Why Symptom Recognition Matters:** Early detection of plant diseases can help prevent their spread and reduce crop losses.
    
    **Common Symptoms to Watch For:**
    - **Leaf Spots:** Irregular, discolored spots on leaves, often caused by fungal or bacterial infections (e.g., black rot on apple trees).
    - **Wilting:** Drooping or wilting of plants, usually due to water stress, root diseases, or vascular blockages.
    - **Stunted Growth:** Plants that appear smaller than normal, often due to nutrient deficiencies, soil-borne diseases, or pests like root nematodes.
    """)
    st.image("Images/plant_disease_symptoms.jpg", caption="Common Plant Disease Symptoms", use_column_width=True)

    st.markdown("""
    **Example:** Yellowing leaves with upward curling edges can be a sign of Tomato Yellow Leaf Curl Virus (TYLCV).
    
    **What to Do:** If you notice any of these symptoms, consult our disease recognition system to identify the potential disease and take action early.
    """)

    st.markdown("""
    ### Tutorial 5: Organic Farming Practices for Disease Prevention
    **What is Organic Farming?** Organic farming emphasizes using natural inputs and ecological processes to maintain soil fertility and prevent diseases.
    
    **Key Practices:**
    - **Composting:** Adds organic matter to the soil, improving its structure and promoting beneficial microorganisms that outcompete harmful pathogens.
    - **Natural Pesticides:** Use neem oil, garlic spray, or insecticidal soap to control pests without synthetic chemicals.
    - **Companion Planting:** Growing certain plants together to deter pests or attract beneficial insects. For example, planting marigolds alongside tomatoes can help deter nematodes.
    """)
    st.image("Images/organic_farming.jpg", caption="Organic Farming Techniques", use_column_width=True)

    st.markdown("""
    **Benefits of Organic Farming:**
    - Enhances soil health and biodiversity.
    - Reduces reliance on chemical inputs that can lead to resistance in pests and diseases.
    
    **Example:** Organic vineyards use cover crops like clover to improve soil nitrogen and reduce the risk of fungal diseases.
    """, unsafe_allow_html=True)

def learn_video_tutorials():
    st.markdown("<h1 style='text-align: center; color: green;'>🎥 Video Tutorials 🎥</h1>", unsafe_allow_html=True)
    st.markdown("""
    <p style='text-align: justify; font-size: 18px;'>Watch these helpful video resources explaining common plant diseases, their symptoms, and methods to manage or cure them:</p>
    """, unsafe_allow_html=True)

    video_list = [
        ("Introduction to Plant Disease Management", "https://www.youtube.com/watch?v=rwiKxaCrHGM"),
        ("Effective Ways to Cure Powdery Mildew", "https://youtu.be/4GYpcXncLCg?si=tXsHIW6J5_7H7Gfq"),
        ("How to Prevent Late Blight in Potatoes", "https://www.youtube.com/watch?v=nU3AlBJoqBk"),
        ("How Apple Scab Forms", "https://www.youtube.com/watch?v=Qh2P8u79nws"),
        ("Northern Leaf Blight in Corn - Prevention Tips", "https://www.youtube.com/watch?v=1rZfbtyzUFQ"),
        ("Black Rot in Grapes - Key Facts", "https://www.youtube.com/watch?v=R38gR9OaE4Q"),
        ("Citrus Greening (Haunglongbing) - Causes and Solutions", "https://www.youtube.com/watch?v=W5mg3lv9sTI"),
        ("Tomato Yellow Leaf Curl Virus - Management Techniques", "https://www.youtube.com/watch?v=D-58aAFIyCQ"),
        ("Late Blight in Potatoes - Effective Prevention and Cure", "https://www.youtube.com/watch?v=nU3AlBJoqBk&t=11s"),
    ]

    for title, url in video_list:
        st.markdown(f"<h4>{title}</h4>", unsafe_allow_html=True)
        st.video(url)

def learn_disease_locations():
    st.markdown("<h1 style='text-align: center; color: green;'>🗺️ Disease Locations 🗺️</h1>", unsafe_allow_html=True)
    st.markdown("""
    <p style='text-align: justify; font-size: 18px;'>Below are maps showing where common plant diseases are found locally and globally:</p>
    """, unsafe_allow_html=True)

    st.subheader("Sri Lankan Disease Map")
    sri_lanka_coords = [7.8731, 80.7718]
    sri_lanka_map = folium.Map(location=sri_lanka_coords, zoom_start=7)

    local_disease_locations = {
        "Apple Scab": {"location": [6.9497, 80.7891], "city": "Nuwara Eliya"},  
        "Black Rot (Apple)": {"location": [6.9808, 81.0562], "city": "Badulla"},  
        "Cedar Apple Rust": {"location": [7.2906, 80.6337], "city": "Kandy"},  
        "Citrus Greening (Haunglongbing)": {"location": [6.8721, 81.3294], "city": "Monaragala"},  
        "Late Blight (Potato)": {"location": [6.9497, 80.7891], "city": "Nuwara Eliya"},  
        "Tomato Yellow Leaf Curl Virus": {"location": [7.0834, 79.9985], "city": "Gampaha"},  
        "Powdery Mildew (Grape)": {"location": [9.6684, 80.0074], "city": "Jaffna"},  
        "Northern Leaf Blight (Corn)": {"location": [8.3114, 80.4037], "city": "Anuradhapura"},  
        "Black Rot (Grape)": {"location": [9.6684, 80.0074], "city": "Jaffna"},  
    }

    for disease, info in local_disease_locations.items():
        folium.Marker(
            location=info["location"],
            popup=f"{disease} - {info['city']}",
            tooltip=f"{disease} in {info['city']}",
            icon=folium.Icon(color="red", icon="info-sign")
        ).add_to(sri_lanka_map)

    folium_static(sri_lanka_map)

    st.subheader("Global Disease Map")
    global_coords = [20.0, 0.0]
    global_map = folium.Map(location=global_coords, zoom_start=2)

    global_disease_locations = {
        "Apple Scab": {"location": [51.1657, 10.4515], "country": "Germany"},  
        "Black Rot (Apple)": {"location": [40.4637, -3.7492], "country": "Spain"},  
        "Cedar Apple Rust": {"location": [37.7749, -122.4194], "country": "United States (California)"},  
        "Black Rot (Grape)": {"location": [43.6532, -79.3832], "country": "Canada (Ontario)"},  
        "Esca (Black Measles)": {"location": [41.8719, 12.5674], "country": "Italy"},  
        "Powdery Mildew (Grape)": {"location": [38.9637, 35.2433], "country": "Turkey"},  
        "Northern Leaf Blight (Corn)": {"location": [34.0522, -118.2437], "country": "United States (California)"},  
        "Common Rust (Corn)": {"location": [-23.5505, -46.6333], "country": "Brazil (São Paulo)"},  
        "Gray Leaf Spot (Corn)": {"location": [4.5709, -74.2973], "country": "Colombia"},  
        "Tomato Yellow Leaf Curl Virus": {"location": [31.0461, 34.8516], "country": "Israel"},  
        "Early Blight (Tomato)": {"location": [19.4326, -99.1332], "country": "Mexico"},  
        "Tomato Mosaic Virus": {"location": [36.2048, 138.2529], "country": "Japan"},  
        "Spider Mites (Tomato)": {"location": [-33.9249, 18.4241], "country": "South Africa"},  
        "Citrus Greening (Haunglongbing)": {"location": [14.5995, 120.9842], "country": "Philippines"},  
        "Late Blight (Potato)": {"location": [51.5074, -0.1278], "country": "United Kingdom (London)"},  
        "Early Blight (Potato)": {"location": [55.3781, -3.4360], "country": "United Kingdom"},  
        "Bacterial Spot (Pepper)": {"location": [-34.6037, -58.3816], "country": "Argentina (Buenos Aires)"},  
        "Strawberry Leaf Scorch": {"location": [-35.6751, -71.5430], "country": "Chile"},  
    }

    for disease, info in global_disease_locations.items():
        folium.Marker(
            location=info["location"],
            popup=f"{disease} - {info['country']}",
            tooltip=f"{disease} in {info['country']}",
            icon=folium.Icon(color="green", icon="leaf")
        ).add_to(global_map)

    folium_static(global_map)

def geocode_location(location):
    api_key = "AIzaSyC9-_hKY78BIITG4k416Agv6-8RX6eYSbs"
    url = f"https://maps.googleapis.com/maps/api/geocode/json?address={location}&key={api_key}"
    response = requests.get(url)
    results = response.json().get("results", [])
    
    if results:
        location_data = results[0]["geometry"]["location"]
        return location_data["lat"], location_data["lng"]
    else:
        st.error("Location not found. Please enter a valid city or state.")
        return None, None

def get_nearby_stores(lat, lon):
    api_key = "AIzaSyC9-_hKY78BIITG4k416Agv6-8RX6eYSbs"  # Replace with your Google API key
    url = f"https://maps.googleapis.com/maps/api/place/nearbysearch/json?location={lat},{lon}&radius=5000&keyword=agriculture%20store|garden%20center|fertilizer|pesticide&key={api_key}"
    
    response = requests.get(url)
    results = response.json().get("results", [])

    store_locations = []
    for place in results:
        store = {
            "name": place["name"],
            "location": place["geometry"]["location"],
            "address": place.get("vicinity", "Unknown address")
        }
        store_locations.append(store)

    return store_locations

def learn_disease_locations_with_fertilizers_location():
    st.markdown("<h1 style='text-align: center; color: green;'>🌱 Find Nearby Pesticides and Fertilizers 🌱</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: justify; font-size: 18px;'>Enter your location to find nearby stores offering pesticides, fertilizers, and other agricultural supplies:</p>", unsafe_allow_html=True)

    location_input = st.text_input("Enter your City or State:", key="manual_location_input_unique")

    if location_input:
        user_lat, user_lon = geocode_location(location_input)
        if user_lat and user_lon:
            st.success(f"Location coordinates for {location_input}: {user_lat}, {user_lon}")
        else:
            return
    else:
        st.warning("Please enter a location to find nearby stores.")
        return

    if st.button("Find Nearby Pesticides and Fertilizers", key="find_stores_button"):
        stores = get_nearby_stores(user_lat, user_lon)

        user_map = folium.Map(location=[user_lat, user_lon], zoom_start=12)

        folium.Marker(
            location=[user_lat, user_lon],
            popup="You are here",
            tooltip="Your Location",
            icon=folium.Icon(color="blue", icon="user")
        ).add_to(user_map)

        for store in stores:
            folium.Marker(
                location=[store["location"]["lat"], store["location"]["lng"]],
                popup=f"{store['name']} - {store['address']}",
                tooltip=store["name"],
                icon=folium.Icon(color="green", icon="shopping-cart")
            ).add_to(user_map)

        folium_static(user_map)

if __name__ == "__main__":
    learn()
    learn_tutorials()
    learn_video_tutorials()
    learn_disease_locations()
    learn_disease_locations_with_fertilizers_location()

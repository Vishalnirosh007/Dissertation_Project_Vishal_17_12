import streamlit as st
import tensorflow as tf
import numpy as np
from treatments import get_treatments
from database import save_disease_record
from disease_details import get_disease_details  # Import the function here

# Add a mapping of diseases to healthy leaf images
healthy_leaf_images = {
    'Apple___Apple_scab': 'Images/healthy_apple_leaf.jpg',
    'Apple___Black_rot': 'Images/healthy_apple_leaf.jpg',
    'Apple___Cedar_apple_rust': 'Images/healthy_apple_leaf.jpg',
    'Apple___healthy': 'Images/healthy_apple_leaf.jpg',
    'Blueberry___healthy': 'Images/healthy_blueberry_leaf.jpg',
    'Cherry_(including_sour)___Powdery_mildew': 'Images/healthy_cherry_leaf.jpg',
    'Cherry_(including_sour)___healthy': 'Images/healthy_cherry_leaf.jpg',
    'Corn_(maize)___Cercospora_leaf_spot_Gray_leaf_spot': 'Images/healthy_corn_leaf.jpg',
    'Corn_(maize)___Common_rust_': 'Images/healthy_corn_leaf.jpg',
    'Corn_(maize)___Northern_Leaf_Blight': 'Images/healthy_corn_leaf.jpg',
    'Corn_(maize)___healthy': 'Images/healthy_corn_leaf.jpg',
    'Grape___Black_rot': 'Images/healthy_grape_leaf.jpg',
    'Grape___Esca_(Black_Measles)': 'Images/healthy_grape_leaf.jpg',
    'Grape___Leaf_blight_(Isariopsis_Leaf_Spot)': 'Images/healthy_grape_leaf.jpg',
    'Grape___healthy': 'Images/healthy_grape_leaf.jpg',
    'Orange___Haunglongbing_(Citrus_greening)': 'Images/healthy_orange_leaf.jpg',
    'Peach___Bacterial_spot': 'Images/healthy_peach_leaf.jpg',
    'Peach___healthy': 'Images/healthy_peach_leaf.jpg',
    'Pepper,_bell___Bacterial_spot': 'Images/healthy_pepper_leaf.jpg',
    'Pepper,_bell___healthy': 'Images/healthy_pepper_leaf.jpg',
    'Potato___Early_blight': 'Images/healthy_potato_leaf.jpg',
    'Potato___Late_blight': 'Images/healthy_potato_leaf.jpg',
    'Potato___healthy': 'Images/healthy_potato_leaf.jpg',
    'Raspberry___healthy': 'Images/healthy_raspberry_leaf.jpg',
    'Soybean___healthy': 'Images/healthy_soybean_leaf.jpg',
    'Strawberry___Leaf_scorch': 'Images/healthy_strawberry_leaf.jpg',
    'Strawberry___healthy': 'Images/healthy_strawberry_leaf.jpg',
    'Tomato___Bacterial_spot': 'Images/healthy_tomato_leaf.jpg',
    'Tomato___Early_blight': 'Images/healthy_tomato_leaf.jpg',
    'Tomato___Late_blight': 'Images/healthy_tomato_leaf.jpg',
    'Tomato___Leaf_Mold': 'Images/healthy_tomato_leaf.jpg',
    'Tomato___Septoria_leaf_spot': 'Images/healthy_tomato_leaf.jpg',
    'Tomato___Spider_mites Two-spotted_spider_mite': 'Images/healthy_tomato_leaf.jpg',
    'Tomato___Target_Spot': 'Images/healthy_tomato_leaf.jpg',
    'Tomato___Tomato_Yellow_Leaf_Curl_Virus': 'Images/healthy_tomato_leaf.jpg',
    'Tomato___Tomato_mosaic_virus': 'Images/healthy_tomato_leaf.jpg',
    'Tomato___healthy': 'Images/healthy_tomato_leaf.jpg',
}

def model_prediction(test_image):
    model = tf.keras.models.load_model("trained_plant_disease_model.keras")
    image = tf.keras.preprocessing.image.load_img(test_image, target_size=(128,128))
    input_arr = tf.keras.preprocessing.image.img_to_array(image)
    input_arr = np.array([input_arr])  # Convert single image to batch
    predictions = model.predict(input_arr)
    return np.argmax(predictions), np.max(predictions)  # Return index of max element and its confidence

def format_class_name(class_name):
    return class_name.replace("___", " ").replace("_", " ").title()

def disease_recognition():
    st.header("Disease Recognition")
    test_image = st.file_uploader("Choose an Image:")
    
    if test_image is not None:
        if st.button("Show Image"):
            st.image(test_image, use_column_width=True)
        
        if st.button("Predict"):
            with st.spinner("Please wait while we process the image..."):
                import time
                time.sleep(2)

                # Perform prediction
                result_index, confidence = model_prediction(test_image)
                
                # Disease classes
                class_names = ['Apple___Apple_scab', 'Apple___Black_rot', 'Apple___Cedar_apple_rust', 'Apple___healthy',
                               'Blueberry___healthy', 'Cherry_(including_sour)___Powdery_mildew', 
                               'Cherry_(including_sour)___healthy', 'Corn_(maize)___Cercospora_leaf_spot_Gray_leaf_spot', 
                               'Corn_(maize)___Common_rust_', 'Corn_(maize)___Northern_Leaf_Blight', 'Corn_(maize)___healthy', 
                               'Grape___Black_rot', 'Grape___Esca_(Black_Measles)', 'Grape___Leaf_blight_(Isariopsis_Leaf_Spot)', 
                               'Grape___healthy', 'Orange___Haunglongbing_(Citrus_greening)', 'Peach___Bacterial_spot',
                               'Peach___healthy', 'Pepper,_bell___Bacterial_spot', 'Pepper,_bell___healthy', 
                               'Potato___Early_blight', 'Potato___Late_blight', 'Potato___healthy', 
                               'Raspberry___healthy', 'Soybean___healthy', 'Squash___Powdery_mildew', 
                               'Strawberry___Leaf_scorch', 'Strawberry___healthy', 'Tomato___Bacterial_spot', 
                               'Tomato___Early_blight', 'Tomato___Late_blight', 'Tomato___Leaf_Mold', 
                               'Tomato___Septoria_leaf_spot', 'Tomato___Spider_mites Two-spotted_spider_mite', 
                               'Tomato___Target_Spot', 'Tomato___Tomato_Yellow_Leaf_Curl_Virus', 'Tomato___Tomato_mosaic_virus',
                               'Tomato___healthy']
                
                formatted_class_name = format_class_name(class_names[result_index])
                treatments = get_treatments()  # Get the treatment dictionary
                treatment = treatments.get(class_names[result_index], "No treatment information available.")
                
                st.success(f"Model is predicting it's a {formatted_class_name} with {confidence:.2f} confidence")
                st.info(f"Suggested Treatment: {treatment}")

                # Display images side by side using columns
                col1, col2 = st.columns(2)

                with col1:
                    st.image(test_image, caption="Uploaded Image (Disease)", use_column_width=True)

                # Display the corresponding healthy leaf image
                healthy_image_path = healthy_leaf_images.get(class_names[result_index])
                if healthy_image_path:
                    with col2:
                        st.image(healthy_image_path, caption="Healthy Leaf", use_column_width=True)

                # Save the prediction to the database
                if st.session_state['logged_in']:
                    image_path = f"Images/{test_image.name}"  # Adjust based on how you're handling images
                    save_disease_record(st.session_state['user_id'], image_path, formatted_class_name, confidence)
                else:
                    st.warning("You need to be logged in to save records.")
                
                # Expander for detailed information
                with st.expander("Learn More"):
                    detailed_info = get_disease_details(formatted_class_name)
                    st.markdown(detailed_info, unsafe_allow_html=True)

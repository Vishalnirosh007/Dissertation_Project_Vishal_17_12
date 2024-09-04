import streamlit as st
import tensorflow as tf
import numpy as np
from treatments import get_treatments
from database import save_disease_record
from disease_details import get_disease_details  # Import the function here

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

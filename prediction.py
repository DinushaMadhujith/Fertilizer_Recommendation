import streamlit as st
import joblib
import pandas as pd


# Function to load the model
@st.cache_resource
def load_model():
    return joblib.load("model.pkl")  # Adjust path if necessary


# Load the model globally
model = load_model()


# Define CSS for specific components
def load_css():
    css = """
    <style>
    /* Set background color for the main container to light blue */
    .stApp {
        background-color: #ADD8E6;  /* Light blue background */
        font-family: Arial, sans-serif;
    }

    /* Style headings, like st.subheader */
    .stApp h1, .stApp h2, .stApp h3, .stApp h4, .stApp h5, .stApp h6 {
        color: #2c3e50;
    }

    /* Styling for prediction results */
    .result-text {
        font-size: 1.2em;
        color: #2c3e50;
        margin-top: 20px;
        font-weight: bold;
    }
    </style>
    """
    st.markdown(css, unsafe_allow_html=True)


# Encoding dictionaries
soil_type_encoding = {"Sandy": 0, "Clay": 1, "Loam": 2, "Silty": 3}
crop_type_encoding = {"Maize": 0, "Sugarcane": 1, "Cotton": 2, "Tobacco": 3, "Paddy": 4, "Barley": 5, "Wheat": 6, "Millets": 7, "Oil seeds": 8, "Pulses": 9, "Ground Nuts": 10}

def show_prediction():
    load_css()  # Load CSS when showing prediction

    st.subheader("Fertilizer Prediction")

    # Collect user input for all required features
    temperature = st.number_input("Enter Temperature (°C)", min_value=0.0, max_value=50.0, step=0.1)
    humidity = st.number_input("Enter Humidity (%)", min_value=0.0, max_value=100.0, step=0.1)
    moisture = st.number_input("Enter Moisture (%)", min_value=0.0, max_value=100.0, step=0.1)
    soil_type = st.selectbox("Select Soil Type", list(soil_type_encoding.keys()))
    crop_type = st.selectbox("Select Crop Type", list(crop_type_encoding.keys()))
    nitrogen = st.number_input("Enter Nitrogen Level", min_value=0.0, max_value=100.0, step=0.1)
    potassium = st.number_input("Enter Potassium Level", min_value=0.0, max_value=100.0, step=0.1)
    phosphorous = st.number_input("Enter Phosphorous Level", min_value=0.0, max_value=100.0, step=0.1)

    # Button for prediction
    if st.button("Predict"):
        # Encode categorical inputs
        soil_type_encoded = soil_type_encoding[soil_type]
        crop_type_encoded = crop_type_encoding[crop_type]

        # Arrange input in the order expected by the model and convert it to DataFrame
        feature_dict = {
            'temperature': [float(temperature)],
            'humidity': [float(humidity)],
            'moisture': [float(moisture)],
            'soil_type': [soil_type_encoded],
            'crop_type': [crop_type_encoded],
            'nitrogen': [float(nitrogen)],
            'potassium': [float(potassium)],
            'phosphorous': [float(phosphorous)]
        }
        features_df = pd.DataFrame(feature_dict)

        try:
            # Check for NaN values in the DataFrame
            if features_df.isnull().values.any():
                st.error("Some input values are missing. Please provide all required information.")
            elif hasattr(model, 'predict'):
                # Make the prediction
                prediction = model.predict(features_df)
                # Display the prediction result
                st.markdown(f"<div class='result-text'>Recommended Fertilizer: {prediction[0]}</div>",
                            unsafe_allow_html=True)
            else:
                st.error("The loaded model does not have a predict method.")
        except Exception as e:
            st.error(f"An error occurred during prediction: {e}")


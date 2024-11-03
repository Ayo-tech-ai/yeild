import streamlit as st
import pickle

# Load the pre-trained model
with open('rf_model.pkl', 'rb') as file:
    model = pickle.load(file)

# Set up the Streamlit interface
st.title("Crop Yeild Prediction App")
st.write("This app uses a machine learning model to makr crop yeild Predictions.")

# Example input fields for the model
# Adjust the inputs based on your model's requirements
input_1 = st.number_input("Rain Fall (mm)", min_value=400, max_value=1300, step=1)
input_2 = st.number_input("Fertilizer", min_value=50, max_value=80, step=1)
input_3 = st.number_input("Temperatue", min_value=24, max_value=40, step=1)
input_4 = st.number_input("Nitrogen (N)", min_value=59, max_value=80, step=1)
input_5 = st.number_input("Phosphorus (P)", min_value=18, max_value=25, step=1)
input_6 = st.number_input("Potassium (K)", min_value=15, max_value=22, step=1)


# Run prediction when button is clicked
if st.button("Predict"):
    # Prepare input data for prediction
    # Convert inputs into a format the model expects, e.g., a 2D array
    input_data = [[input_1, input_2, input_3,input_4, input_5, input_6]]
    prediction = model.predict(input_data)
    
    # Display prediction result
    st.write("YEILD  (Q/acre):", prediction[0])
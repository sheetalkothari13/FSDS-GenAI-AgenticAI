import streamlit as st
import pickle
import numpy as np

# Load your trained model (update the path to your .pkl file)
model = pickle.load(open(r'C:\Users\Sheetal\SheetalProjects\August\20th-MLR House price\multiple_linear_regression_model.pkl', 'rb'))

st.title("🏡 House Price Prediction App")

st.write("This app predicts house prices using a Multiple Linear Regression model.")

# --- User Inputs ---
bedrooms = st.number_input("Number of Bedrooms", min_value=0, max_value=20, value=3, step=1)
bathrooms = st.number_input("Number of Bathrooms", min_value=0, max_value=10, value=2, step=1)
sqft_living = st.number_input("Living Area (sqft)", min_value=500, max_value=10000, value=1500, step=50)

# --- Prediction ---
if st.button("Predict Price"):
    # Convert input into 2D numpy array
    features = np.array([[bedrooms, bathrooms, sqft_living]])
    prediction = model.predict(features)

    st.success(f"💰 Predicted Price: ${prediction[0]:,.2f}")

import streamlit as st
import pickle
import numpy as np

model = pickle.load(open(r'C:\Users\Sheetal\SheetalProjects\August\19th-SLR Fullstack House Price Prediction\house_price_model.pkl', 'rb'))

st.title("House Price Prediction App ")

st.write("This app predicts the house price based on square footage using a simple linear regression model.")

sqft_living = st.number_input("Enter Square Footage of the House:", min_value=100.0, max_value=10000.0, value=1000.0, step=50.0)

if button := st.button("Predict Price"):
    sqft_input = np.array([[sqft_living]])  # Convert the input to a 2D array for prediction
    prediction = model.predict(sqft_input)
   
    st.success(f"The predicted price for a house with {sqft_living} sqft is: ${prediction[0]:,.2f}")
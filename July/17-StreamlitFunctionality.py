import streamlit as st
import pandas as pd
import numpy as np  

st.title("My first Streamlit app")
st.write("This is a simple app to demonstrate Streamlit functionality.")

st.sidebar.header("User Input Features")

#text input
user_name = st.sidebar.text_input("What is your name", "Streamlit User")

#slider 
age = st.sidebar.slider("How old are you?", 0, 100, 25)

#selectbox 
favorite_color = st.sidebar.selectbox("What is your favorite color?",["Blue", "Red", "Green", "Yellow", "Purple"])

#main content
st.header(f"Welcome, {user_name}!")
st.write(f"You are {age} years old and your favorite color is {favorite_color}.")

#random data 
st.subheader("Here's some random data:")

# sample dataframe ,, NUMPY and PANDAS is used here
data = pd.DataFrame(
    np.random.randn(10, 5), 
    columns=('col %d' % i for i in range(5))
)

st.dataframe(data)

#checkbox
if st.checkbox("Show raw data"):
    st.subheader("Raw Data")
    st.write(data)

#button
if st.button("Say Hello"):
    st.write("Hello there!")
else:
    st.write("goodbye!")
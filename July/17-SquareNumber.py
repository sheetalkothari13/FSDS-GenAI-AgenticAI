import streamlit as st
st.title("Hello Streamlit, This is Sheetal, And I am Learning!")
st.write("This is my first Streamlit app. I am excited to learn more about it!")
st.write("This app creates the square of a number.")

st.header("Select a number to see its square")
number = st.slider("Choose a number", 1, 100, 10)   #min=1, max=100, default=10

st.header("Result")
squared_number = number ** 2
st.write(f"The square of {number} is {squared_number}.")
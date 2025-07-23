import streamlit as st
import numpy as np
from PIL import Image
import requests
from io import BytesIO
import matplotlib.pyplot as plt

# Set Streamlit page config
st.set_page_config(page_title="Elephant Image Processor", layout="centered")

# Title
st.title("Elephant Image - Multi-Color Channel Visualizer")

# Load image from URL
@st.cache_data           #Caches this function so it only downloads once (faster reloads).
def load_image():
    url = "https://upload.wikimedia.org/wikipedia/commons/3/37/African_Bush_Elephant.jpg"
    response = requests.get(url)
    return Image.open(BytesIO(response.content)).convert("RGB")
                    #BytesIO(response.content): Wraps the byte content into a file-like object.

# Load and display image
elephant = load_image()
st.image(elephant, caption="Original Elephant Image", use_container_width=True)

# Convert to NumPy array
elephant_np = np.array(elephant)
R, G, B = elephant_np[:, :, 0], elephant_np[:, :, 1], elephant_np[:, :, 2]

# Create channel images
#Create blank images (all black initially)
#np.zeros_like(elephant_np):- Creates an array of same shape as elephant_np but filled with zeros.Since pixel values are all zeros → it’s a completely black image.Shape is still (height, width, 3) for RGB.
red_img = np.zeros_like(elephant_np)
green_img = np.zeros_like(elephant_np)
blue_img = np.zeros_like(elephant_np)

red_img[:, :, 0] = R
green_img[:, :, 1] = G
blue_img[:, :, 2] = B
#red_img[:, :, 0] = R: This sets all red values (channel 0) from the original image into the red channel of red_img .Puts Red values in the Red channel. Green and Blue channels stay zero => only red hues appear.Same for Green and Blue.

# Display RGB channels
st.subheader("RGB Channel Visualization")
col1, col2, col3 = st.columns(3)

with col1:
    st.image(red_img, caption="Red Channel", use_container_width=True)

with col2:
    st.image(green_img, caption="Green Channel", use_container_width=True)

with col3:
    st.image(blue_img, caption="Blue Channel", use_container_width=True)

# Grayscale + Colormap
st.subheader("Colormapped & Grayscale Image")

colormap = st.selectbox(
    "Choose a Matplotlib colormap",
    ["viridis", "plasma", "inferno", "magma", "cividis", "hot", "cool", "gray"]
)

elephant_gray = elephant.convert("L")
elephant_gray_np = np.array(elephant_gray)
#.convert("L"):- converts it from RGB (color) to grayscale (black & white)..Converts grayscale PIL image into NumPy array.
#"L" stands for luminance. It tells PIL to use 8-bit pixels (values from 0–255) where: 0 → Black, 255 → White, values in between → shades of gray. So, elephant_gray is now a PIL.Image object in grayscale mode.

# Plot using matplotlib with colormap
fig, ax = plt.subplots(figsize=(6,4))
im = ax.imshow(elephant_gray_np, cmap=colormap)  #If you wanted to update the image dynamically (like when user changes colormap in Streamlit), you can reuse 'im' instead of redrawing a new image.
plt.axis("off")
#Hides axes (ticks, grid) with plt.axis("off").
# DO NOT USE: plt.show()
# USE THIS INSTEAD:
st.pyplot(fig)
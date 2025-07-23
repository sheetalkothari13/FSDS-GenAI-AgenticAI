import streamlit as st
import numpy as np
from PIL import Image
import requests
from io import BytesIO
import matplotlib.pyplot as plt

st.set_page_config(page_title="My Image", layout="centered")
st.title("Sheetal's image - Multi-Color Channel Visualizer")

@st.cache_data
def load_image():
    url = r"D:\Naresh It Classes\July\New folder\New folder\IMG-20221216-WA0019.jpg"   #r"" (raw string) to avoid backslash escape issues OR use forward slashes (/)
    return Image.open(url).convert("RGB")  #Since our image is local, we don’t need requests.get().Instead, open it directly using PIL.Image.open()

sheetal = load_image()
st.image(sheetal, caption="Original Image", use_container_width=True)

sheetal_np = np.array(sheetal)
R, G, B = sheetal_np[:, :, 0], sheetal_np[:, :, 1], sheetal_np[:, :, 2]

red_img = np.zeros_like(sheetal_np)
green_img = np.zeros_like(sheetal_np)
blue_img = np.zeros_like(sheetal_np)

red_img[:, :, 0] = R
green_img[:, :, 1] = G
blue_img[:, :, 2] = B

st.subheader("RGB Channel Visualization")
col1, col2, col3 = st.columns(3)

with col1:
    st.image(red_img, caption="Red Channel", use_container_width=True)

with col2:
    st.image(green_img, caption="Green Channel", use_container_width=True)

with col3:
    st.image(blue_img, caption="Blue Channel", use_container_width=True)

st.subheader("Colormapped & Grayscale Image")
colormap = st.selectbox(
    "Choose a Matplotlib colormap",
    ["viridis", "plasma", "inferno", "magma", "cividis", "hot", "cool", "gray"]
)
sheetal_gray = sheetal.convert("L")
sheetal_gray_np = np.array(sheetal_gray)

fig, ax = plt.subplots(figsize=(6, 4))
im = ax.imshow(sheetal_gray_np, cmap=colormap)  #
plt.axis("off")
st.pyplot(fig)
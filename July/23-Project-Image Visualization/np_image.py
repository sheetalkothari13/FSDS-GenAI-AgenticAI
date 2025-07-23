import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from PIL import Image      #python imaging library
import requests      #to handle HTTP requests, used to fetch images from URLs
from io import BytesIO  # to handle byte streams,used for buffer memory to store or capture images


def load_image_from_url(url):
    """
    Load an image from a URL and convert it to a NumPy array.
    
    Parameters:
    url (str): The URL of the image.
    
    Returns:
    np.ndarray: The image as a NumPy array.
    """
    response = requests.get(url)
    img = Image.open(BytesIO(response.content))
    return np.array(img)

# elephant_url = "https://upload.wikimedia.org/wikipedia/commons/3/37/African_Bush_Elephant.jpg"

# elephant = load_image_from_url(elephant_url)

# #display the original image
# plt.figure(figsize=(8, 6))
# plt.imshow(elephant)
# plt.title('Original Image of Elephant')
# plt.axis('off')
# plt.show()


peackock_url = "https://m.media-amazon.com/images/I/81JSw5mE54L._UF894,1000_QL80_.jpg"
peackock = load_image_from_url(peackock_url) 

plt.figure(figsize=(8, 6))
plt.imshow(peackock)
plt.title('Original Image of Peacock')
plt.axis('off')
plt.show()

#image to array
# elephant_np = np.array(elephant)
# print('Elephant image shape:', elephant_np.shape)

# #display grayscale images
# elephant_gray = elephant.convert("L")  # Convert to grayscale

# plt.figure(figsize=(8, 6))
# plt.imshow(elephant_gray, cmap='gray')
# plt.title('Grayscale Image of Elephant')
# plt.axis('off')
# plt.show()
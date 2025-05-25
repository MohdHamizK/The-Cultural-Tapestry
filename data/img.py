from PIL import Image
import streamlit as st

# Open the image file using PIL
image_path = 'images/Madhubani.png'  # Path to your image file

try:
    # Open the image using PIL
    image = Image.open(image_path)

    # Display the image in Streamlit
    st.image(image, caption="Madhubani Art", use_column_width=True)

except FileNotFoundError:
    st.error(f"The file '{image_path}' was not found.")
except Exception as e:
    st.error(f"An error occurred: {str(e)}")

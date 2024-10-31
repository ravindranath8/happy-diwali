import streamlit as st
from PIL import Image, ImageDraw
import random
import time

# Streamlit setup
st.set_page_config(page_title="Happy Diwali!", layout="centered")

# Title
st.markdown("<h1 style='text-align: center; color: yellow;'>🎆 Happy Diwali 🎆</h1>", unsafe_allow_html=True)

# Function to create a fireworks frame
def create_fireworks_frame(width=500, height=500):
    # Create a black background
    img = Image.new("RGB", (width, height), "black")
    draw = ImageDraw.Draw(img)
    
    # Create random fireworks
    for _ in range(5):  # Number of fireworks per frame
        x, y = random.randint(50, width-50), random.randint(50, height-50)
        color = random.choice(["red", "yellow", "blue", "green", "purple", "orange", "white"])
        for radius in range(0, 50, 10):  # Expanding circles
            draw.ellipse((x-radius, y-radius, x+radius, y+radius), outline=color, width=2)
    
    return img

# Display animation
num_frames = 10
frame_display = st.image([])

# Run the animation loop
for _ in range(num_frames):
    frame = create_fireworks_frame()
    frame_display.image(frame)
    time.sleep(1.0)  # Adjust the speed of animation

# Display a greeting message
st.markdown("<h2 style='text-align: center; color: lightblue;'>Wishing you a joyous Diwali filled with prosperity and happiness!</h2>", unsafe_allow_html=True)

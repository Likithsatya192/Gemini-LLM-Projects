from dotenv import load_dotenv
load_dotenv()

from PIL import Image

import streamlit as st
import os
import google.generativeai as genai

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel("gemini-1.5-flash")

def get_gemini_response(input, image):
    if input != "":
        response = model.generate_content([input, image])
    else:
        response = model.generate_content(image)
    return response.text

st.set_page_config(page_title="Gemini Vision Projects", page_icon=":gemini:")
st.title("Gemini Vision Projects")

input_text = st.text_input("Enter your question:", key="input_text")

image_file = st.file_uploader("Upload an image:", type=["jpg", "jpeg", "png"])

if image_file is not None:
    image = Image.open(image_file)
    st.image(image, caption="Uploaded Image", use_column_width=True)

submit = st.button("Tell me about this image")
if submit:
    response = get_gemini_response(input_text, image)

    st.subheader("Response:")
    st.write(response)

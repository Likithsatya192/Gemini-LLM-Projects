from dotenv import load_dotenv
load_dotenv()

import streamlit as st
import os
import google.generativeai as genai

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel("gemini-1.5-flash")

def get_gemini_response(question):
    response = model.generate_content(question)
    return response.text

st.set_page_config(page_title="Gemini LLM Projects", page_icon=":gemini:")
st.title("Gemini LLM Projects")
input_text = st.text_input("Enter your question:", key="input_text")

submit = st.button("Submit")

if submit:
    response = get_gemini_response(input_text)
    st.subheader("Response:")
    st.write(response)

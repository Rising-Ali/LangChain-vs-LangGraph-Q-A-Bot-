%%writefile app.py
#install pre req Libraires
import streamlit as st
import os
from langchain_community.llms import LlamaCpp

# Assuming the model file is in the same directory as the app.py file.
# If not, please provide the correct path to the model file.
MODEL_PATH = "openorca-platypus2-13b.gguf.q4_0.bin"

def get_response_from_OpenAI(question):
    # Instantiate the LlamaCpp class
    llm = LlamaCpp(model_path=MODEL_PATH, temperature=0.4)
    response = llm(question)
    return response

st.set_page_config(page_title="Q&A ChatBot")
st.header("LangChain Application")

input = st.text_input("Input: ", key = "input")
submit = st.button("Ask me anything!")

if submit:
    st.subheader("The Response is: ")
    response = get_response_from_OpenAI(input)
    st.write(response)
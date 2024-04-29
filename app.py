import pathlib
import textwrap
import google.generativeai as genai
import streamlit as st
import load
st.header("Welcome to the summarize easy")
url=st.text_input("Enter the url",placeholder="URL....")
if url:
    response=(load.output(url))
    for chunk in response:
        st.write(chunk.text)
import pathlib
import textwrap
import google.generativeai as genai
import streamlit as st
import load
import website_data
st.header("Welcome to the summarize easy")
url=st.text_input("Enter the url",placeholder="URL....")
if url:
    response=(load.output(website_data.scrape(url)))
    for chunk in response:
        st.write(chunk.text)
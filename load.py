import pathlib
import textwrap
import google.generativeai as genai
def output(text):
    response = model.generate_content(text)
    return response
GOOGLE_API_KEY="AIzaSyCgX2dUhfUNGZ1aSrjUIlXNfor1ylBdw7I"
genai.configure(api_key=GOOGLE_API_KEY)
model = genai.GenerativeModel('gemini-pro')
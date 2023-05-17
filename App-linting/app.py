import streamlit as st
from utils import get_chatgpt_response, get_initial_message, update_chat
import openai

openai.api_key = "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"

import re

def extract_data(text):
    pattern =  r"\{(.*?)\}"
    matches = re.findall(pattern, text)
    return matches


def process_python_code(code):
    # Add your desired code processing logic here
    messages = get_initial_message()
    messages = update_chat(messages, "user", code)
    processed_code = get_chatgpt_response(messages, "gpt-3.5-turbo")

    return processed_code

def main():
    st.title("Python Code Linting Tool")
    
    # Text area for Python code input
    code_input = st.text_area("Enter Python code:")
    
    # Button to trigger code processing
    if st.button("Process Code"):
        processed_code = process_python_code(code_input)
        python_code = processed_code.split("```")[1]
        st.code(python_code)

        
#         # Provide download link for processed code
#         st.markdown(get_download_link(processed_code), unsafe_allow_html=True)

# def get_download_link(code):
#     # Generate a download link for the processed code file
#     href = f'<a href="data:text/plain;charset=utf-8,{code}" download="processed_code.py">Download Processed Code</a>'
#     return href

if __name__ == "__main__":
    main()

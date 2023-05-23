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
    processed_code = ""
    try: 
        st.title("Python Code Linting Tool")
        
        # Text area for Python code input
        code_input = st.text_area("Enter Python code:")
        
        # Button to trigger code processing
        if st.button("Process Code"):
            processed_code = process_python_code(code_input)
            python_code= processed_code.split("```")[1]
            st.write("Code to copy and use it")
            st.code(python_code)
            with st.expander("See explanation and Score"):
                st.write(processed_code)
                # pattern = r'{\s*"score_before":\s*(\d+\.\d+),\s*"score_after":\s*(\d+\.\d+)\s*}'
                # st.write("## Score for codes")
                # matches = re.search(pattern, processed_code, re.MULTILINE)
                # if matches:
                #     json_data = {
                #         "score_before": float(matches.group(1)),
                #         "score_after": float(matches.group(2))
                #     }
                #     st.write(json_data)
                # else:
                #     st.write(processed_code.lower().split('```json')[1])

    except Exception as e: 
        print(e)
        
   
    
if __name__ == "__main__":
    main()

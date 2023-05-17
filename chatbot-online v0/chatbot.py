import streamlit as st
from streamlit_chat import message
from utils import get_initial_message, get_chatgpt_response, update_chat
import os
from dotenv import load_dotenv
load_dotenv()
import openai

openai.api_key = "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"


st.title("Chatbot : ChatGPT and Streamlit Chat")
st.subheader("Find code")

model = st.selectbox(
    "Select a model",
    ("gpt-3.5-turbo", "gpt-4")
)


if 'generated' not in st.session_state:
    st.session_state['generated'] = []
if 'past' not in st.session_state:
    st.session_state['past'] = []

query = st.text_input("Query: ", key="input")

if 'messages' not in st.session_state:
    st.session_state['messages'] = get_initial_message()


if query:
    with st.spinner("generating..."):
        messages = st.session_state['messages']
        messages = update_chat(messages, "user", query)
        response = get_chatgpt_response(messages, model)
        messages = update_chat(messages, "assistant", response)
        st.session_state.past.append(query)
        st.session_state.generated.append(response)

# get the code in the variable 
code = ""
if st.session_state['generated']:

    for i in range(len(st.session_state['generated'])-1, -1, -1):
        message(st.session_state['past'][i], is_user=True, key=str(i) + '_user')
        if "```" in st.session_state["generated"][i] :
            try:  
                code = response.split("```")[1].replace("python", "")
                message(st.code(code, language="python"))
                break 
            except: 
                pass   
        elif "```python" not in st.session_state["generated"][i] : 
            message(st.session_state["generated"][i], key=str(i))
        

if st.button("run_code"): 
    if code :     
        import streamlit as st
        import tempfile
        import os

        temp_file = tempfile.NamedTemporaryFile(suffix='.py', delete=False)
        temp_file.write(code.encode())
        temp_file.close()
        temp_file_path = temp_file.name
        os.system(f"streamlit run {temp_file_path}")

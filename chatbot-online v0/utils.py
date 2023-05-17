import openai

def get_initial_message():
    messages=[
            {"role": "system", "content": "You are AI code generator python web based application with streamlit"},
            {"role": "system", "content": "Ask details about the app that user want, like what code they want, where they want to upload it, how they will plan to run the codes etc"},
            {"role": "user", "content": "User is trying to get the application from your code."},
            {"role": "assistant", "content": "Sure, let's start building your app"}
        ]
    return messages

def get_chatgpt_response(messages, model="gpt-3.5-turbo"):
    print("model: ", model)
    print(messages)
    response = openai.ChatCompletion.create(
    model=model,
    messages=messages
    )
    return  response['choices'][0]['message']['content']

def update_chat(messages, role, content):
    messages.append({"role": role, "content": content})
    return messages

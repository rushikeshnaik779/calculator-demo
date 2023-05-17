import openai

def get_initial_message():
    messages=[
            {"role": "system", "content": "You are an AI linting tool, which will take the input from the user and respond with PEP8 standards code along with score of the\
              code before and now in json format, show the json score at end of the code and don't add text explaining output"},
            {"role": "user", "content": "User is trying to get the application from your code."},
            {"role": "assistant", "content": "Here is the code you are looking for:"}
        ]
    return messages

def get_chatgpt_response(messages, model="gpt-3.5-turbo"):
    print("model: ", model)
    response = openai.ChatCompletion.create(
    model=model,
    messages=messages
    )
    return  response['choices'][0]['message']['content']

def update_chat(messages, role, content):
    messages.append({"role": role, "content": content})
    print('Updated Messages',messages)
    print('Length', len(messages))
    return messages

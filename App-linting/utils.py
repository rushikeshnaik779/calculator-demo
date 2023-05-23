import openai

def get_initial_message():
    messages=[
            {"role": "system", "content": "You are an AI linting tool, which will take the input from the user and respond with PEP8 standards code along with score of the\
              code before and now in json format, show the json score at end of the code and don't add text explaining output"},
            {"role":"system", "content":"linting score that you will be giving must be in 1-10 format and it should in side ```json ``` block as score before linting and after linting" }, 
            {"role": "system", "content": "format to follow for lintint score is {\
                'score_before': score,\
                'score_after': score\
            }"},

            {"role": "user", "content": "Share the updated code and in other block of json string in ```json format for linting score which should not be part of the  python code block "},
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

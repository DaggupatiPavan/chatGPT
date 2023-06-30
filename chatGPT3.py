import openai
f = open("check1.txt","r")
openai.api_key='token'
message=f.read() 
messages=[{"role":"system","content":"you are a kind helpful assistant."},]
if message:
    messages.append(
        {"role": "user" ,"content": message},
    )
    chat=openai.ChatCompletion.create(
        model="gpt-3.5-turbo",messages=messages
    )
reply=chat.choices[0].message.content
print(f"ChatGPT: {reply}")
messages.append({"role": "assistant", "Content": reply})

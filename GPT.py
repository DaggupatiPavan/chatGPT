import openai

openai.api_key = 'token'
mes = "I need jenkins example pipeline contains "
message = mes + input("Which tools you want to integrate in jenkins pipeline, separate by comma: ")
messages = [{"role": "system", "content": "you are a kind helpful assistant."}]

if message:
    messages.append({"role": "user", "content": message})

chat = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=messages
)

reply = chat.choices[0].message.content
# print(f"ChatGPT: {reply}")

# Find start and end positions of the desired content
start_index = reply.find("```") + 3
end_index = reply.rfind("```")

# Trim the content between start and end positions
trimmed_output = reply[start_index:end_index]

print(f"Sample pipeline: {trimmed_output}")

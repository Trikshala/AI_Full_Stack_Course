from ollama import chat

messages = [
    {"role": "system", "content": "Classify the sentiment as Positive, Negative or Neutral. Reply with one word only."},
    {"role": "user", "content": "Great movie!"},
    {"role": "assistant", "content": "Positive"},
    {"role": "user", "content": "Waste of money."},
    {"role": "assistant", "content": "Negative"},
    {"role": "user", "content": "It was okay."},
    {"role": "assistant", "content": "Neutral"},
    # Question
    {"role": "user", "content": "Loved the acting but the ending was dull."}
]

response = chat(model="llama3.2", messages=messages)
print(response.message.content)
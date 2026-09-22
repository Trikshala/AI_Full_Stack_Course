from ollama import chat

response1 = chat(
    model="llama3.2",
    messages=[{"role": "user", "content": "Tell me about dogs"}]
)
print(response1.message.content)

print()

response2 = chat(
    model="llama3.2",
    messages=[{"role": "user", "content": "List 5 dog breeds good for small apartments, with one line each."}]
)

print(response2.message.content)

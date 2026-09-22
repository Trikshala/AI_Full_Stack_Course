from ollama import chat

question = "Why is the sky blue?"

roles = [
    "You are a pirate. Answer in pirate speak. 1 line.",
    "You are a scientist. Be precise and formal. 1 line.",
    "You are a friendly kindergarten teacher. Keep it very simple. 1 line."
]

for role in roles:
    response = chat(
        model="llama3.2",
        messages=[
            {"role": "system", "content": role},
            {"role": "user", "content": question}
        ]
    )
    print(f"--- {role} ---")
    print(response.message.content)
    print()
from ollama import chat

prompt = "Write a one-line tagline for a coffee shop."

for temp in [0, 0.7, 1.5]:
    print(f"=== Temperature: {temp} ===")
    for run in range(3):
        response = chat(
            model="llama3.2",
            messages=[{"role": "user", "content": prompt}],
            options={"temperature": temp}
        )
        print(f"Run {run + 1}: {response.message.content}")
    print()
import ollama

system_msg = "You are a friendly, patient tutor. Keep answers short and simple."

while True:
    question = input("You (Ask something): ").strip()
    if question == "":
        print("Please type something.")
        continue
    if question.lower() == "exit":
        print("AI 🤖 : Goodbye Trikshala! Come back soon!🤧🤧")
        break
    try:
        response = ollama.chat(
            model="llama3.2",
            messages=[{"role": "system", "content": system_msg},
                {"role": "user", "content": question}]
        )

        print(f"AI 🤖: {response.message.content}")
        print()
        
    except Exception as e:
        print("Something went wrong. Is Ollama running?")
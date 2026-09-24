from ollama import chat

system_msg = "You are a friendly, patient tutor. Keep answers short and simple."
history = [{"role": "system", "content": system_msg}]
question_count = 0

while True:
    question = input("You (Ask something): ")
    if question == "":
        print("AI 🤖 : Please type something.")
        continue
    if question.lower().strip() == "exit":
        print("AI 🤖 : Goodbye User! Come back soon!🤧🤧")
        print(f"AI 🤖 : You asked {question_count} question(s) today. Nice work!")
        break
    if question.lower().strip() == "/clear":
        history = [{"role": "system", "content": system_msg}]
        print("AI 🤖 : Memory cleared! Starting fresh.")
        print()
        continue
    if question.lower().strip() == "/history":
        print("--- Conversation so far ---")
        if len(history) < 2:
            print("Nothing to show yet!")
        for msg in history[1:]:  
            if msg["role"] == "user":
                speaker = "You" 
            else:
                speaker = "AI 🤖 "
            print(f"{speaker}: {msg['content']}")
        print("---------------------------")
        print()
        continue
    if question.lower().strip() == "/help":
        print("--- Available commands ---")
        print("/clear   - wipe the conversation memory")
        print("/history - view everything asked so far")
        print("/help    - show this list")
        print("exit     - quit the chatbot")
        print("--------------------------")
        print()
        continue
    history.append({"role": "user", "content": question})
    question_count += 1
    try:
        response = chat(
            model="llama3.2",
            messages=history
        )

        reply = response.message.content
        history.append({"role": "assistant", "content": reply})
        print(f"AI 🤖: {reply}")
        print()
        
    except Exception as e:
        print("Something went wrong. Is Ollama running?")
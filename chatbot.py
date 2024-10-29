import subprocess

def chatbot():
    print("Hello! I'm your AI chatbot. Type 'exit' to end the conversation.")

    user_input = input("You: ")
    
    if user_input.lower() == 'exit':
        print("Chatbot: Goodbye!")
    else:
        result = subprocess.run(
            ['ollama', 'run', 'llama2', user_input],
            capture_output=True,
            text=True
        )
        
        bot_reply = result.stdout.strip()
        print(f"Chatbot: {bot_reply}")

chatbot()

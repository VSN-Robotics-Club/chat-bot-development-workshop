print("Hello! I am a simple chatbot. What's your name?")
name = input("You: ")

print(f"Nice to meet you, {name}!")
print("How can I help you today?")

user_input = input("You: ").lower()

if user_input == "hello":
    print("Chatbot: Hello! How are you?")
elif user_input == "how are you?":
    print("Chatbot: I'm just a bunch of code, but I'm here to help you!")
elif user_input == "what's your favorite color?":
    print("Chatbot: I like all colors! What's yours?")
elif user_input == "bye":
    print("Chatbot: Goodbye! Have a great day!")
else:
    print("Chatbot: I'm not sure how to respond to that. Can you ask me something else?")

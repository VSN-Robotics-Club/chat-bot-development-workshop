# Chatbot

This project demonstrates how to create a simple AI chatbot using the Ollama CLI and a language model. You can follow the instructions below to set up and run your chatbot.

## Prerequisites

Before you start, ensure you have the following installed:

- Python 3.x
- Ollama CLI

## Installation

1. **Install Ollama**: Follow the instructions on the [Ollama website](https://ollama.com/) to install the Ollama CLI.

2. **Pull a Language Model**: Open your terminal and run the following command to pull a language model (e.g., `llama2`):

   ```bash
   ollama pull llama2

## Create the Chatbot Script

1. **Create a Python Script**: Create a new file named `ollama_chatbot.py` and open it in your favorite text editor.

2. **Add the Following Code**:

   ```python
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

## Run the Chatbot

1. **Open Your Terminal**: Navigate to the directory where you saved the `ollama_chatbot.py` file.

2. **Run the Script**:

   ```bash
   python ollama_chatbot.py
   
## Interact with the Chatbot

Type your message and press Enter. To exit, type `exit` and press Enter.

## Example Interaction

Hello! I'm your AI chatbot. Type 'exit' to end the conversation.  
You: Hello!  
Chatbot: Hi there! How can I help you today?  
You: Tell me a joke.  
Chatbot: Why did the scarecrow win an award? Because he was outstanding in his field!  
You: exit  
Chatbot: Goodbye!

## Troubleshooting

- Ensure that you have the necessary permissions to run commands in your terminal.
- If you have any issues, message us at our [Facebook page](https://www.facebook.com/vsnroboticsclub).

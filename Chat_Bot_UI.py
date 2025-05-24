import tkinter as tk
import random
import threading
import time

class SimpleChatBot:
    def __init__(self):
        self.responses = { 
            "hello": ["hi there, i am a chatbot made by haziq", "hello", "i might not be friendly but pleased to meet you", "greetings!"], 
            "how are you": ["i am fine", "i am depressed", "good"],
            "bye": ["going already", "you are leaving me alone? fine!!", "good bye :("],
            "name": ["i am chatbot", "why do you wanna know my name??", "my name is larry"],
            "creator": ["i was created by haziq"],
            "are you an ai": ["no i am just a chatbot whose responses are pre registered and i give a random response for each command for each of your question"],
        }

    def get_response(self, user_input):
        user_input = user_input.lower()
        for key in self.responses:
            if key in user_input:
                return random.choice(self.responses[key])
        return "that statement is something i hadn't learnt"

class ChatbotUI:
    def __init__(self, root):
        self.chatbot = SimpleChatBot()
        self.root = root
        self.root.title("Simple ChatBot")
        self.root.geometry("400x500")

        self.text_area = tk.Text(root, wrap=tk.WORD, state='disabled', bg="#f0f0f0")
        self.text_area.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

        self.entry = tk.Entry(root, font=("Arial", 14))
        self.entry.pack(padx=10, pady=(0,10), fill=tk.X)
        self.entry.bind("<Return>", self.send_message)

        self.send_button = tk.Button(root, text="Send", command=self.send_message)
        self.send_button.pack(padx=10, pady=(0,10))

        self.insert_message("Chatbot: Hi! I am a simple chatbot made in Python.")

    def insert_message(self, message):
        self.text_area.config(state='normal')
        self.text_area.insert(tk.END, message + "\n\n")
        self.text_area.config(state='disabled')
        self.text_area.see(tk.END)

    def send_message(self, event=None):
        user_input = self.entry.get().strip()
        if user_input == "":
            return
        self.insert_message("You: " + user_input)
        self.entry.delete(0, tk.END)

        # Run response generation with delay in a separate thread
        threading.Thread(target=self.delayed_response, args=(user_input,)).start()

    def delayed_response(self, user_input):
        time.sleep(2)  # Wait for 2 seconds
        response = self.chatbot.get_response(user_input)
        # Insert response in main thread using 'after'
        self.root.after(0, lambda: self.insert_message("Chatbot: " + response))
        if user_input.lower() == "bye":
            self.root.after(2500, self.root.destroy)  # Close window shortly after response

if __name__ == "__main__":
    root = tk.Tk()
    app = ChatbotUI(root)
    root.mainloop()

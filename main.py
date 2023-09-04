import nltk
from nltk.chat.util import Chat, reflections
import json
import tkinter as tk
from tkinter import scrolledtext, simpledialog, messagebox, Button
import random


with open('data.json', 'r') as json_file:
    data = json.load(json_file)

reflections = {
  "i am"       : "you are",
  "i was"      : "you were",
  "i"          : "you",
  "i'm"        : "you are",
  "i'd"        : "you would",
  "i've"       : "you have",
  "i'll"       : "you will",
  "my"         : "your",
  "you are"    : "I am",
  "you were"   : "I was",
  "you've"     : "I have",
  "you'll"     : "I will",
  "your"       : "my",
  "yours"      : "mine",
  "you"        : "me",
  "me"         : "you"
}

initial_greetings = [
    "Chatbot: Hello! How can I assist you today?\n",
    "Chatbot: Hi there! What can I help you with?\n",
    "Chatbot: Greetings! Feel free to ask me anything about admissions.\n",
]

chatbot = Chat(data, reflections)

class ChatGUI(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Admission Enquiry Chatbot")
        self.geometry("800x450")

        self.chat_history = scrolledtext.ScrolledText(self, state='disabled')
        self.chat_history.pack(fill=tk.BOTH, expand=True)

        self.input_entry = tk.Entry(self, font=("Helvetica", 14))
        self.input_entry.pack(fill=tk.BOTH, expand=True)
        self.input_entry.bind("<Return>", self.send_message)

        self.send_button = Button(self, text="Send", command=self.send_message)
        self.send_button.pack()

        initial_greeting = random.choice(initial_greetings)
        self.update_chat_history(initial_greeting)

    def send_message(self, event=None):
        user_input = self.input_entry.get()
        self.input_entry.delete(0, tk.END)

        response = chatbot.respond(user_input)
        self.update_chat_history(f"You: {user_input}\nChatbot: {response}\n")

    def update_chat_history(self, message):
        self.chat_history.configure(state='normal')
        self.chat_history.insert(tk.END, message + "\n")
        self.chat_history.configure(state='disabled')
        self.chat_history.see(tk.END)

# Create the GUI instance
gui = ChatGUI()
gui.mainloop()
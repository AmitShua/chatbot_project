
import tkinter as tk
from transformers import pipeline

# Load model
chatbot = pipeline("text-generation", model="gpt2")

def respond():
    user_input = entry.get()
    response = chatbot(user_input, max_new_tokens=100)[0]['generated_text']
    chat_window.insert(tk.END, "You: " + user_input + "\n")
    chat_window.insert(tk.END, "Bot: " + response + "\n\n")
    entry.delete(0, tk.END)

# GUI setup
window = tk.Tk()
window.title("Offline Chatbot")
window.geometry("500x500")

chat_window = tk.Text(window, bg="white", fg="black", wrap="word")
chat_window.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

entry = tk.Entry(window, bg="lightgray")
entry.pack(padx=10, pady=5, fill=tk.X)

send_button = tk.Button(window, text="Send", command=respond)
send_button.pack(pady=5)

window.mainloop()

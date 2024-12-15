import tkinter as tk
from tkinter import scrolledtext, ttk
from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate

# Define the conversation template
# Add your own parameters
template = """
Write and explain code and questions.

Conversation context: {context}

Question: {question}

Answer:
"""

#Add the model of your choice
model = OllamaLLM(model="")  # check your model name by going to cmd and typing ollama list
prompt = ChatPromptTemplate.from_template(template)
chain = prompt | model

context = ""

def send_message():
    global context
    user_input = entry.get()
    if user_input.lower() == "exit":
        root.quit()

    answer = chain.invoke({"context": context, "question": user_input})
    chat_log.config(state=tk.NORMAL)
    chat_log.insert(tk.END, f"User: {user_input}\n")
    chat_log.insert(tk.END, f"Bot: {answer}\n")
    chat_log.config(state=tk.DISABLED)
    context += f"\nUser: {user_input}\nBot: {answer}"
    chat_log.see(tk.END)
    entry.delete(0, tk.END)


root = tk.Tk()
root.title("Conversation Bot")
root.geometry("600x450")  
root.resizable(True, True)  

style = ttk.Style(root)
style.configure('TButton', font=('Helvetica', 12), padding=5)
style.configure('TEntry', font=('Helvetica', 12))

frame = ttk.Frame(root, padding=10)
frame.pack(fill=tk.BOTH, expand=True)

chat_log = scrolledtext.ScrolledText(frame, width=60, height=20, font=('Helvetica', 12), wrap=tk.WORD)
chat_log.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
chat_log.config(state=tk.DISABLED)

entry = ttk.Entry(frame, width=50, style='TEntry')
entry.pack(side=tk.LEFT, padx=10, fill=tk.X, expand=True)

entry.bind("<Return>", lambda event: send_message())

send_button = ttk.Button(frame, text="Send", command=send_message, style='TButton')
send_button.pack(side=tk.LEFT, padx=10)

exit_button = ttk.Button(frame, text="Exit", command=root.quit, style='TButton')
exit_button.pack(side=tk.RIGHT, padx=10)

root.mainloop()

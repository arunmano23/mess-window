import tkinter as tk
from tkinter import scrolledtext, messagebox

# Function to send a message
def send_message():
    message = message_entry.get()
    if message:
        chat_box.config(state=tk.NORMAL)
        chat_box.insert(tk.END, "You: " + message + "\n")
        chat_box.config(state=tk.DISABLED)
        message_entry.delete(0, tk.END)
        # You can implement sending the message over network here if needed
    else:
        messagebox.showwarning("Warning", "Please enter a valid message")

# Create main window
root = tk.Tk()
root.title("Chat Application")

# Create text widget to display chat messages
chat_box = scrolledtext.ScrolledText(root, width=50, height=20)
chat_box.config(state=tk.DISABLED)
chat_box.grid(row=0, column=0, padx=10, pady=10, columnspan=2)

# Create entry widget for typing messages
message_entry = tk.Entry(root, width=40)
message_entry.grid(row=1, column=0, padx=10, pady=10)

# Create send button
send_button = tk.Button(root, text="Send", width=10, command=send_message)
send_button.grid(row=1, column=1, padx=10, pady=10)

# Start the tkinter main loop
root.mainloop()
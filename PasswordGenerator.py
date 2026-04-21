import tkinter as tk
import random
import string

root = tk.Tk()
root.title("Password Generator")
root.geometry("300x250")
root.configure(bg="#1e1e2f")

def generate():
    length = int(entry.get())
    chars = string.ascii_letters + string.digits
    pwd = "".join(random.choice(chars) for _ in range(length))
    label.config(text=pwd)

tk.Label(root, text="Enter Length", fg="white", bg="#1e1e2f",
         font=("Arial", 12)).pack(pady=10)

entry = tk.Entry(root, font=("Arial", 12))
entry.pack()

tk.Button(root, text="Generate Password",
          bg="#007bff", fg="white",
          command=generate).pack(pady=15)

label = tk.Label(root, text="", fg="#00ffcc",
                 bg="#1e1e2f", font=("Arial", 12))
label.pack()

root.mainloop()
import tkinter as tk
from tkinter import filedialog

root = tk.Tk()
root.title("Notepad")
root.geometry("500x400")

text = tk.Text(root, font=("Arial", 12), bg="#1e1e2f", fg="white")
text.pack(fill="both", expand=True)

def save():
    file = filedialog.asksaveasfile(mode='w', defaultextension=".txt")
    if file:
        file.write(text.get("1.0", tk.END))
        file.close()

tk.Button(root, text="Save File",
          bg="#28a745", fg="white",
          command=save).pack(fill="x")

root.mainloop()
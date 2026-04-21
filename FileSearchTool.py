import tkinter as tk
from tkinter import filedialog

root = tk.Tk()
root.title("File Search Tool")
root.geometry("400x300")
root.configure(bg="#0f172a")

def search():
    file = filedialog.askopenfile()
    word = entry.get()

    if file:
        content = file.read()
        if word in content:
            result_label.config(text="✅ Found!", fg="#22c55e")
        else:
            result_label.config(text="❌ Not Found", fg="#ef4444")

# Title
title = tk.Label(root, text="File Search Tool",
                 font=("Segoe UI", 18, "bold"),
                 bg="#0f172a", fg="white")
title.pack(pady=15)

# Entry
entry = tk.Entry(root, font=("Segoe UI", 12),
                 bg="#1e293b", fg="white", bd=0)
entry.pack(padx=20, pady=10, fill="x", ipady=8)

# Button
tk.Button(root, text="Select File & Search",
          bg="#3b82f6", fg="white",
          font=("Segoe UI", 11),
          bd=0, command=search).pack(pady=10)

# Result
result_label = tk.Label(root, text="",
                        font=("Segoe UI", 14),
                        bg="#0f172a")
result_label.pack(pady=20)

root.mainloop()
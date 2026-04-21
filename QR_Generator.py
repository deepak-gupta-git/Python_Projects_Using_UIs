import tkinter as tk
from PIL import Image, ImageTk
import qrcode

root = tk.Tk()
root.title("QR Code Generator")
root.geometry("400x450")
root.configure(bg="#0f172a")

qr_img = None

def generate_qr():
    global qr_img

    data = entry.get()
    if data == "":
        return

    # Generate QR
    qr_img = qrcode.make(data)

    # Resize for UI
    qr_img_resized = qr_img.resize((200, 200))

    # Convert to Tkinter format
    img_tk = ImageTk.PhotoImage(qr_img_resized)

    # Show on screen
    qr_label.config(image=img_tk)
    qr_label.image = img_tk

# Title
tk.Label(root, text="QR Generator",
         font=("Segoe UI", 18, "bold"),
         bg="#0f172a", fg="white").pack(pady=10)

# Input
entry = tk.Entry(root, font=("Segoe UI", 12),
                 bg="#1e293b", fg="white", bd=0)
entry.pack(padx=20, pady=10, fill="x", ipady=8)

# Button
tk.Button(root, text="Generate QR",
          bg="#10b981", fg="white",
          font=("Segoe UI", 11),
          bd=0, command=generate_qr).pack(pady=10)

# QR Display Area
qr_label = tk.Label(root, bg="#0f172a")
qr_label.pack(pady=20)

root.mainloop()
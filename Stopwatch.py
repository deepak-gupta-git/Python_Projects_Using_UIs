import tkinter as tk

root = tk.Tk()
root.title("Stopwatch")
root.geometry("300x300")
root.configure(bg="#1e1e2f")  # background color

time = 0
running = False

def update():
    global time
    if running:
        time += 1
        label.config(text=format_time(time))
        root.after(1000, update)

def format_time(t):
    mins = t // 60
    secs = t % 60
    return f"{mins:02}:{secs:02}"

def start():
    global running
    running = True
    update()

def stop():
    global running
    running = False

def reset():
    global time
    time = 0
    label.config(text="00:00")

# Title
title = tk.Label(root, text="Stopwatch", font=("Arial", 18, "bold"),
                 bg="#1e1e2f", fg="white")
title.pack(pady=10)

# Time Display
label = tk.Label(root, text="00:00", font=("Arial", 40, "bold"),
                 bg="#1e1e2f", fg="#00ffcc")
label.pack(pady=20)

# Buttons Frame
frame = tk.Frame(root, bg="#1e1e2f")
frame.pack()

# Buttons
start_btn = tk.Button(frame, text="Start", command=start,
                      bg="#28a745", fg="white", width=8)
start_btn.grid(row=0, column=0, padx=5)

stop_btn = tk.Button(frame, text="Stop", command=stop,
                     bg="#dc3545", fg="white", width=8)
stop_btn.grid(row=0, column=1, padx=5)

reset_btn = tk.Button(frame, text="Reset", command=reset,
                      bg="#ffc107", fg="black", width=8)
reset_btn.grid(row=0, column=2, padx=5)

root.mainloop()
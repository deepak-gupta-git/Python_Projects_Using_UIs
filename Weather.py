import tkinter as tk
import requests
API_KEY="63a460a3171b36fe7944756affd7f485"

def get_weather():
    city = entry.get()
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid=API_KEY&units=metric"
    
    try:
        data = requests.get(url).json()
        temp = data["main"]["temp"]
        label.config(text=f"{city}: {temp}°C")
    except:
        label.config(text="Error fetching data")

root = tk.Tk()
root.title("Weather App")
root.configure(bg="#1e1e2f")

entry = tk.Entry(root)
entry.pack(pady=10)

tk.Button(root, text="Get Weather", command=get_weather,
          bg="#007bff", fg="white").pack()

label = tk.Label(root, text="", fg="white", bg="#1e1e2f", font=("Arial", 14))
label.pack(pady=20)

root.mainloop()

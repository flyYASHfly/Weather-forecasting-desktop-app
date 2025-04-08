import tkinter as tk
from tkinter import messagebox
import requests
from difflib import get_close_matches

# Full city list including Indian cities
city_list = [
    # International cities
    "New York", "London", "Paris", "Berlin", "Tokyo", "Toronto", "Sydney", "Moscow", "Los Angeles", "Chicago", "Dubai", "Singapore", "Rome", "Bangkok", "Cairo", "Madrid", "Barcelona", "Beijing", "Seoul",
    
    # Indian cities 🇮🇳
    "Delhi", "New Delhi", "Mumbai", "Bangalore", "Hyderabad", "Chennai", "Kolkata", "Pune", "Ahmedabad",
    "Jaipur", "Lucknow", "Surat", "Indore", "Bhopal", "Kanpur", "Nagpur", "Patna", "Ranchi", "Chandigarh",
    "Kochi", "Thiruvananthapuram", "Noida", "Gurgaon", "Visakhapatnam", "Vadodara", "Agra", "Varanasi",
    "Amritsar", "Raipur", "Jodhpur", "Coimbatore", "Vijayawada", "Guwahati", "Mysore", "Aurangabad",
    "Nashik", "Pondicherry", "Madurai", "Dehradun", "Shillong", "Ludhiana", "Jalandhar", "Meerut",
    "Gwalior", "Jammu", "Aligarh", "Bhavnagar", "Bareilly", "Dhanbad", "Srinagar", "Mangalore",
    "Udaipur", "Jamshedpur", "Allahabad (Prayagraj)"
]

def fetch_weather(city_name):
    try:
        # Using wttr.in (no API key needed)
        url = f"https://wttr.in/{city_name}?format=%C+%t"
        response = requests.get(url)
        if response.status_code == 200:
            return response.text
        else:
            return None
    except:
        return None

def get_suggestions(event):
    typed = city_entry.get()
    suggestions = get_close_matches(typed, city_list, n=5, cutoff=0.3)
    suggestion_list.delete(0, tk.END)
    for suggestion in suggestions:
        suggestion_list.insert(tk.END, suggestion)

def select_suggestion(event):
    selected = suggestion_list.get(suggestion_list.curselection())
    city_entry.delete(0, tk.END)
    city_entry.insert(0, selected)

def show_weather():
    city_name = city_entry.get()
    if city_name not in city_list:
        messagebox.showerror("Error", "City not recognized. Please select a valid city!")
        return
    weather_info = fetch_weather(city_name)
    if weather_info:
        result_label.config(text=f"Weather in {city_name}: {weather_info}")
    else:
        result_label.config(text="Could not retrieve weather data.")

# Setting up GUI
root = tk.Tk()
root.title("Current Weather")

root.geometry("400x400")
root.configure(bg="#f0f0f0")

city_entry = tk.Entry(root, width=30, font=("Arial", 14))
city_entry.pack(pady=10)
city_entry.bind("<KeyRelease>", get_suggestions)

suggestion_list = tk.Listbox(root, height=5, font=("Arial", 12))
suggestion_list.pack(pady=5)
suggestion_list.bind("<<ListboxSelect>>", select_suggestion)

search_button = tk.Button(root, text="Get Weather", command=show_weather, font=("Arial", 14), bg="#4CAF50", fg="white")
search_button.pack(pady=10)

result_label = tk.Label(root, text="", font=("Arial", 16), bg="#f0f0f0")
result_label.pack(pady=20)

root.mainloop()

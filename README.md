![Screenshot 2025-04-08 095105](https://github.com/user-attachments/assets/ab1b3e11-216a-464d-bde2-03f73a3ac142)
![Screenshot 2025-04-08 095117](https://github.com/user-attachments/assets/f0aaade5-629f-42a0-92e5-84fb3ee1834e)
![Screenshot 2025-04-08 095132](https://github.com/user-attachments/assets/f1128420-5f30-46aa-8d83-69903db400fb)


🔷 Project Goal:
Build a simple desktop app where a user can:

Type a city name

Get live weather info

See autocomplete suggestions while typing

Get error message if the city name is invalid

🔷 What We Used:
Tool	Purpose
Python	Main programming language
Tkinter	For creating the GUI (Graphical User Interface)
requests library	To fetch weather data from the internet
difflib library	To suggest similar city names when typing
wttr.in	A free weather API (no API key needed)
🔷 How It Is Built – Step-by-Step:
1. Set up a list of cities
Created a big city_list that includes famous cities around the world and major Indian cities (like Mumbai, Delhi, Bangalore, etc.).

This list is used for autocomplete suggestions.

2. Build the GUI using Tkinter
Created the main window using tk.Tk().

Added an Entry box (tk.Entry) where the user types the city name.

Added a Listbox (tk.Listbox) below the entry box to show suggestions live as the user types.

Added a Button (tk.Button) to trigger the weather search.

Added a Label (tk.Label) to display the weather result.

3. Handle typing and suggestions
Used difflib.get_close_matches() to find city names that match what the user is typing.

Showed those suggestions inside the Listbox instantly.

4. When a suggestion is selected
If the user clicks a suggestion from the list, that city name auto-fills into the Entry box.

5. Fetch weather data
When the user clicks Get Weather, the app:

Checks if the city is valid (present in city_list).

If invalid ➔ shows an error message.

If valid ➔ sends an internet request to wttr.in to get the weather.

Displays the weather condition and temperature.

6. Error Handling
If anything goes wrong (e.g., bad spelling, no internet), the app shows a friendly error popup using tkinter.messagebox.

🔷 Key Features:
✅ Simple and clean UI

✅ Live city name suggestions

✅ Error messages for invalid input

✅ Real-time weather without API keys

✅ Focus on Indian cities but includes global ones too

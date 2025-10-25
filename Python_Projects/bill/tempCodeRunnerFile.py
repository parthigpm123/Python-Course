# --------------------------- Importing Required Modules ---------------------------
from tkinter import *
from tkinter import ttk
import requests   # Used to call the weather API from OpenWeatherMap

# --------------------------- Function: Fetch and Display Weather Data ---------------------------
def data_get():
    city = city_name.get()   # Get the city name entered or selected by user

    try:
        # API call to OpenWeatherMap (replace with your own API key if needed)
        data = requests.get(
            f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid=599292d69a88ba0df3c167f0826e343a"
        ).json()

        # If API returns error (e.g., city not found)
        if data.get("cod") != 200:
            w_label1.config(text="N/A")
            wb_label1.config(text="City not found")
            temp_label1.config(text="N/A")
            per_label1.config(text="N/A")
            return

        # Update UI labels with received data
        w_label1.config(text=data["weather"][0]["main"])                          # Weather condition (e.g., Clouds, Rain)
        wb_label1.config(text=data["weather"][0]["description"])                  # More detail (e.g., scattered clouds)
        temp_label1.config(text=str(int(data["main"]["temp"] - 273.15)) + " °C")  # Convert from Kelvin → Celsius
        per_label1.config(text=str(data["main"]["pressure"]) + " hPa")            # Pressure value

    except Exception as e:
        # Handles errors like no internet connection or invalid response
        w_label1.config(text="Error")
        wb_label1.config(text="Check internet")
        temp_label1.config(text="N/A")
        per_label1.config(text="N/A")

# --------------------------- Main Window Setup ---------------------------
win = Tk()
win.title("Weather App")      # Title of window
win.geometry("500x570")       # Window size (width x height)
win.config(bg="#17AFEB")      # Background color (light blue)

# --------------------------- Heading Label ---------------------------
name_label = Label(win, text="Weather App", font=("Time New Roman", 30, "bold"))
name_label.place(x=25, y=50, height=50, width=450)
name_label.config(bg="#2DACDF", fg="black")

# --------------------------- Dropdown (City Selection) ---------------------------
city_name = StringVar()  # Tkinter variable to store selected city

# List of Indian States (as city examples)
list_name = [
    "Andhra Pradesh","Arunachal Pradesh","Assam","Bihar","Chhattisgarh","Goa",
    "Gujarat","Haryana","Himachal Pradesh","Jammu and Kashmir","Jharkhand","Karnataka",
    "Kerala","Madhya Pradesh","Maharashtra","Manipur","Meghalaya","Mizoram","Nagaland",
    "Odisha","Punjab","Rajasthan","Sikkim","Tamil Nadu","Telangana","Tripura",
    "Uttar Pradesh","Uttarakhand","West Bengal","Andaman and Nicobar Islands",
    "Chandigarh","Dadra and Nagar Haveli","Daman and Diu","Lakshadweep",
    "National Capital Territory of Delhi","Puducherry"
]

# Combobox widget (dropdown menu)
com = ttk.Combobox(
    win, values=list_name, font=("Time New Roman", 20, "bold"), textvariable=city_name
)
com.place(x=25, y=120, height=50, width=450)

# --------------------------- Button to Trigger API Call ---------------------------
done_button = Button(win, text="Done", font=("Time New Roman", 20, "bold"), command=data_get)
done_button.place(x=200, y=190, height=50, width=100)

# --------------------------- Weather Output Labels ---------------------------

# Weather Type (e.g., Clear, Cloudy)
w_label = Label(win, text="Weather Climate", font=("Time New Roman", 20))
w_label.place(x=25, y=260, height=50, width=210)
w_label1 = Label(win, text="", font=("Time New Roman", 20))
w_label1.place(x=250, y=260, height=50, width=210)

# Weather Description (e.g., scattered clouds)
wb_label = Label(win, text="Weather Description", font=("Time New Roman", 16))
wb_label.place(x=25, y=330, height=50, width=210)
wb_label1 = Label(win, text="", font=("Time New Roman", 16))
wb_label1.place(x=250, y=330, height=50, width=210)

# Temperature in °C
temp_label = Label(win, text="Temperature", font=("Time New Roman", 20))
temp_label.place(x=25, y=400, height=50, width=210)
temp_label1 = Label(win, text="", font=("Time New Roman", 20))
temp_label1.place(x=250, y=400, height=50, width=210)

# Pressure in hPa
per_label = Label(win, text="Pressure", font=("Time New Roman", 20))
per_label.place(x=25, y=470, height=50, width=210)
per_label1 = Label(win, text="", font=("Time New Roman", 20))
per_label1.place(x=250, y=470, height=50, width=210)

# --------------------------- Run the Main Loop ---------------------------
win.mainloop()

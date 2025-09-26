import calendar
import datetime
import tkinter as tk
from tkinter import scrolledtext

# get today's date
today = datetime.date.today()
year = today.year
month = today.month

# generate current month calendar
month_calendar = calendar.month(year, month, w=3)

# create tkinter window
root = tk.Tk()
root.title("Current Month Calendar")

# add a label
label = tk.Label(root, text=f"Calendar - {calendar.month_name[month]} {year}", 
                 font=("Arial", 16, "bold"))
label.pack(pady=15)

# add scrolled text widget for calendar display
text_area = scrolledtext.ScrolledText(root, width=30, height=10, font=("Courier", 12))
text_area.pack(padx=15, pady=15)

# insert calendar text
text_area.insert(tk.END, month_calendar)
text_area.config(state="disabled")  # make it read-only

# run application
root.mainloop()

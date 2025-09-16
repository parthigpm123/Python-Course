import tkinter as tk

# ******* VARIABLES ********

running = False
hours, minutes, seconds = 0, 0, 0
update_time = None  # initialize update_time

# ******** FUNCTIONS ********

def start():
    global running
    if not running:
        update()
        running = True

def pause():
    global running, update_time
    if running:
        stopwatch_label.after_cancel(update_time)
        running = False

def reset():
    global running, hours, minutes, seconds, update_time
    if running:
        stopwatch_label.after_cancel(update_time)
        running = False
    hours, minutes, seconds = 0, 0, 0
    stopwatch_label.config(text="00:00:00")

def update():
    global hours, minutes, seconds, update_time
    seconds += 1
    if seconds == 60:
        minutes += 1
        seconds = 0
    if minutes == 60:
        hours += 1
        minutes = 0

    hours_string = f"{hours:02}"
    minutes_string = f"{minutes:02}"
    seconds_string = f"{seconds:02}"

    stopwatch_label.config(text=f"{hours_string}:{minutes_string}:{seconds_string}")

    update_time = stopwatch_label.after(1000, update)

# ****** WIDGET SECTION ********

root = tk.Tk()
root.geometry("400x200")
root.title("Stopwatch")

stopwatch_label = tk.Label(root, text="00:00:00", font=("Helvetica", 40), bg="black", fg="red")
stopwatch_label.pack(pady=20)

button_frame = tk.Frame(root)
button_frame.pack()

start_button = tk.Button(button_frame, text="Start", height=2, width=7, font=("Helvetica", 15), command=start)
start_button.grid(row=0, column=0, padx=5)

pause_button = tk.Button(button_frame, text="Pause", height=2, width=7, font=("Helvetica", 15), command=pause)
pause_button.grid(row=0, column=1, padx=5)

reset_button = tk.Button(button_frame, text="Reset", height=2, width=7, font=("Helvetica", 15), command=reset)
reset_button.grid(row=0, column=2, padx=5)

quit_button = tk.Button(button_frame, text="Quit", height=2, width=7, font=("Helvetica", 15), command=root.quit)
quit_button.grid(row=0, column=3, padx=5)

# ******* MAIN LOOP ********

root.mainloop()

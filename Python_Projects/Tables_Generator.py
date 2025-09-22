import tkinter as tk
from tkinter import messagebox

def show_table():
    try:
        num = int(entry.get())
        result_text.delete(1.0, tk.END)  # Clear previous output
        result_text.insert(tk.END, f"{num} TABLE\n")
        result_text.insert(tk.END, "--------------\n")
        for i in range(1, 21):
            result_text.insert(tk.END, f"{i} x {num} = {i * num}\n")
    except ValueError:
        messagebox.showerror("Invalid input", "Please enter a valid integer.")

def clear_all():
    entry.delete(0, tk.END)
    result_text.delete(1.0, tk.END)

root = tk.Tk()
root.title("Tables Generator")
root.geometry("350x500")

label = tk.Label(root, text="Enter Table Number:")
label.pack(pady=10)

entry = tk.Entry(root)
entry.pack(pady=5)
entry.focus()

button_frame = tk.Frame(root)
button_frame.pack(pady=5)

show_button = tk.Button(button_frame, text="Show Table", command=show_table)
show_button.grid(row=0, column=0, padx=5)

clear_button = tk.Button(button_frame, text="Clear", command=clear_all)
clear_button.grid(row=0, column=1, padx=5)

result_text = tk.Text(root, height=25, width=30)
result_text.pack(pady=10)

root.bind('<Return>', lambda event: show_table())

root.mainloop()

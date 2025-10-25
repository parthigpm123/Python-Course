import tkinter as tk
from tkinter import messagebox

# Function to update the listbox display
def show_tasks():
    listbox.delete(0, tk.END)
    for task in tasks:
        listbox.insert(tk.END, task)

# Function to add a new task
def add_task():
    task = task_entry.get()
    if task.strip():
        tasks.append(task.strip())
        show_tasks()
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Input Error", "Please enter a task.")

# Function to delete the selected task
def delete_task():
    try:
        selected_index = listbox.curselection()[0]
        removed_task = tasks.pop(selected_index)
        show_tasks()
    except IndexError:
        messagebox.showwarning("Selection Error", "Please select a task to delete.")

# Create the main window
root = tk.Tk()
root.title("Colorful To-Do List")
root.geometry("400x555")
root.config(bg="#f0f8ff")

tasks = []

# Title Label
title_label = tk.Label(root, text="My To-Do List", font=("Helvetica", 20, "bold"), bg="#f0f8ff", fg="#333")
title_label.pack(pady=10)

# Listbox to show tasks
listbox = tk.Listbox(root, width=40, height=15, font=("Helvetica", 12), bg="#fffacd")
listbox.pack(pady=10)

# Entry to add tasks
task_entry = tk.Entry(root, width=30, font=("Helvetica", 12))
task_entry.pack(pady=5)

# Add Task Button
add_button = tk.Button(root, text="Add Task", width=20, font=("Helvetica", 12, "bold"),
                       bg="#4caf50", fg="white", command=add_task)
add_button.pack(pady=5)

# Delete Task Button
delete_button = tk.Button(root, text="Delete Task", width=20, font=("Helvetica", 12, "bold"),
                          bg="#f44336", fg="white", command=delete_task)
delete_button.pack(pady=5)

# Exit Button
exit_button = tk.Button(root, text="Exit", width=20, font=("Helvetica", 12, "bold"),
                        bg="#2196f3", fg="white", command=root.destroy)
exit_button.pack(pady=20)

# Start the GUI loop
root.mainloop()

import tkinter as tk

# Handle button clicks
def click(event):
    text = event.widget.cget("text")
    if text == "=":
        try:
            expression = entry_var.get()
            expression = expression.replace('x', '*').replace('/', '/')
            result = eval(expression)
            entry_var.set(result)
        except:
            entry_var.set("Error")
    elif text == "C":
        entry_var.set("")
    elif text == "«":
        current = entry_var.get()
        entry_var.set(current[:-1])
    elif text == "+/-":
        current = entry_var.get()
        if current:
            if current.startswith('-'):
                entry_var.set(current[1:])
            else:
                entry_var.set('-' + current)
    else:
        entry_var.set(entry_var.get() + text)

# Create main window
root = tk.Tk()
root.title("Calculator")
root.geometry("320x500")
root.configure(bg="#0f0f23")
root.resizable(False, False)

# Entry display
entry_var = tk.StringVar()
entry = tk.Entry(root, textvariable=entry_var, font=("Segoe UI", 32), bg="#0f0f23", fg="white", bd=0, insertbackground="white", justify="right")
entry.place(x=10, y=20, width=300, height=80)

# Define button properties
btn_font = ("Segoe UI", 20)
btn_width = 70
btn_height = 60
padding = 10

# Colors
num_bg = "#1c1c2e"
num_fg = "white"
op_bg = "#3b5fd1"
op_fg = "white"

# Button definitions with positions matching the image
buttons = [
    # text, x, y, width, height, bg, fg
    ('%', 10, 120, 60, 50, num_bg, num_fg),
    ('C', 80, 120, 60, 50, num_bg, num_fg),
    ('«', 150, 120, 60, 50, num_bg, num_fg),
    ('/', 220, 120, 70, 50, op_bg, op_fg),
    
    ('7', 10, 180, 60, 50, num_bg, num_fg),
    ('8', 80, 180, 60, 50, num_bg, num_fg),
    ('9', 150, 180, 60, 50, num_bg, num_fg),
    ('x', 220, 180, 70, 50, op_bg, op_fg),
    
    ('4', 10, 240, 60, 50, num_bg, num_fg),
    ('5', 80, 240, 60, 50, num_bg, num_fg),
    ('6', 150, 240, 60, 50, num_bg, num_fg),
    ('-', 220, 240, 70, 50, op_bg, op_fg),
    
    ('1', 10, 300, 60, 50, num_bg, num_fg),
    ('2', 80, 300, 60, 50, num_bg, num_fg),
    ('3', 150, 300, 60, 50, num_bg, num_fg),
    ('+', 220, 300, 70, 50, op_bg, op_fg),
    
    ('+/-', 10, 360, 60, 50, num_bg, num_fg),
    ('0', 80, 360, 60, 50, num_bg, num_fg),
    ('.', 150, 360, 60, 50, num_bg, num_fg),
    ('=', 220, 360, 70, 50, op_bg, op_fg)
]

# Create and place buttons
for txt, x, y, w, h, bg, fg in buttons:
    btn = tk.Button(root, text=txt, font=btn_font, bg=bg, fg=fg, bd=0, relief=tk.FLAT,
                    activebackground=bg, activeforeground=fg)
    btn.place(x=x, y=y, width=w, height=h)
    btn.bind("<Button-1>", click)

root.mainloop()

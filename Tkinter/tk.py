'''
import tkinter 

#tkinter allows to  create GUI applications or widgets

#window
root= tkinter.Tk()
root.geometry("750x600")
root.configure(bg="light blue")

#label

label =tkinter.Label(root, 
                     text="Hello Python Developers",fg="blue",
                     bg="sky blue",
                     font="Arial 50"
)

label.pack(expand=True, anchor="center")


#use pack to position and pack a GUI into a container (window or frame)
label.pack()
#Run application
root.mainloop()
'''

file =  open("File_Handling/code.txt","r")

print(file.read())
file.close()
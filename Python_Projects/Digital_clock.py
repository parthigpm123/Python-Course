from tkinter import * # import tkinter module for GUI graphical user interface
import time

def digital():
      t=time.strftime("%I:%M:%S %p")
      #date add
      d=time.strftime("%a/%b/%Y")
      clock.config(text=t + "\n" + d)
      #clock.config(text=d) 
      clock.after(200,digital)
      
root=Tk()

root.title("DIGITAL CLOCK")
clock=Label(root,font=('times',100,'bold'),bg='red')   
clock.grid(row=2,column=1)
digital()
root.mainloop()   
      
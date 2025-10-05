from tkinter import *

class Student:
      def __init__(self,main):
            self.main = main
            self.T_frame = Frame(self.main,height=50, width=1200, background="yellow", bd=2, relief=GROOVE)
            self.T_frame.pack()
            self.title = Label(self.T_frame, text="Student Management System", font="arial 20 bold",width=1200, bg="yellow")
            self.title.pack()
            
            self.frame_1 =Frame(self.main, height=580, width=450, bd=2, relief=GROOVE, bg="yellow")
            self.frame_1.pack(side=LEFT)
            
            self.frame_2 =Frame(self.main, height=580, width=800, bd=2, relief=GROOVE, bg="yellow")
            self.frame_2.pack(side=RIGHT)
            
            
            
            
            



main = Tk()
main.title("Student Management System")
main.resizable(False, False)
main.geometry("1200x600")

Student(main)
main.mainloop()
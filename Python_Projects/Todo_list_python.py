"Create  todo list app with tkinter"
tasks=[]
def addTask():
      task = input('Please Enter a task:>')
      tasks.append(task)
      print(f"Task '{task} added to the list'")
def listTask():
      if not tasks:
            print("There are no tasks currently")
      else:
            print("Current Tasks:")
            for index , task in enumurate(tasks):
                  print(f"Task #{index}.{task}")
                  
                  ###
                   
      
def deleteTsk():
      
      listTasks()
      try:
         taskToDelete = int(input("Choose the number of the task to delete:>")) 
         if taskToDelete >=0 and taskToDelete < len(tasks):
               tasks.pop(taskToDelete)
               print(f"Task #{taskToDelete} has been removed.")
         else:      
            print('fTask #{taskToDelete} was not found')
            
      except:
            print("Invalid input ")     
            
      
      

### create to do list

print("Welcome To The Todo_List_App :)")

while True:
      print("\n")
      print("please select one of the following option")
      print("-----------------------------------------")
      print("1.Add a new task")
      print("2.delete a task")
      print("3.List a task")
      print("4.Quit")
      
      choice =input("Enter your choice:> ")
      
      if choice=="1":
            addTask()
            
      elif choice=="2":
            deleteTask()
      
      elif choice=="3":
            listTask()
      elif choice=="4":
            break   
      else:
            print("Invalid input.please try again")  
            
      print("Good bye  ")        
            
            
        